import numpy as np, wave, subprocess
SR=48000
SRC='/mnt/user-data/uploads/4d9211c7-c_est_ou_il_est.m4a'
subprocess.run(['ffmpeg','-v','error','-y','-i',SRC,'-af','highpass=f=80,lowpass=f=12000,afftdn=nf=-30,acompressor=threshold=-26dB:ratio=3:attack=10:release=150:makeup=4,loudnorm=I=-15:TP=-1.5:LRA=9','-ac','1','-ar',str(SR),'-f','s16le','v6p.raw'],check=True)
v=np.frombuffer(open('v6p.raw','rb').read(),dtype=np.int16).astype(np.float32)
keep=[(0,61.6),(69.1,77.6),(80.4,115.2),(117.6,136.5),(140.9,len(v)/SR)]
def fade(x):
    n=min(len(x),int(.02*SR)); x=x.copy(); x[:n]*=np.linspace(0,1,n); x[-n:]*=np.linspace(1,0,n); return x
voice=np.concatenate([fade(v[int(a*SR):int(b*SR)]) for a,b in keep])
w=wave.open('voce6.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(voice.astype(np.int16).tobytes()); w.close()
TOT=len(voice)/SR
def nt(t):
    off=0
    for (a,b),(c,d) in zip(keep,keep[1:]):
        if t>=c: off+=c-b
    return t-off
def tone(freqs,dur,vol=.5):
    out=[]
    for f in freqs:
        t=np.arange(int(SR*dur))/SR; out.append(np.sin(2*np.pi*f*t)*np.minimum(1,t*200)*np.exp(-t*6/dur)*vol)
    return np.concatenate(out)
S={'coin':tone([988,1319],.09,.35),'err':tone([220,160],.18,.35),'power':tone([523,659,784,1047],.08,.3),'ok':tone([1047,1319,1568],.09,.3),'win':np.concatenate([tone([523,659,784],.1,.3),tone([1047],.4,.3)])}
P='/home/claude/r6/reel_livello6_'
cuts=[('01_titolo',0,5.0),('02_hook',5.0,15.2),('03_cest_nome',15.2,30.8),('04_ilest_agg',30.8,47.0),('05_professione',47.0,61.6),('06_prof_agg',69.1,83.2),('07_giudizio',83.2,111.0),('08_riepilogo',111.0,126.5),('09_fine',126.5,999)]
seq=[]
for k,a,b in cuts:
    A=nt(a) if k!='06_prof_agg' else 61.6
    B=TOT if b==999 else (nt(b) if k!='05_professione' else 61.6)
    seq.append((k,A,B))
sfx=[('coin',0.1),('power',nt(15.2)),('power',nt(30.8)),('err',nt(47.0)),('ok',61.6),('power',nt(83.2)),('ok',nt(111.0)),('win',nt(126.5))]
with open('list6.txt','w') as f:
    for k,a,b in seq: f.write(f"file '{P}{k}.png'\nduration {b-a:.3f}\n")
    f.write(f"file '{P}{seq[-1][0]}.png'\n")
trk=np.zeros(int(SR*(TOT+1)))
for k,t in sfx:
    s=S[k]; i=int(t*SR); trk[i:i+len(s)]+=s[:len(trk)-i]
w=wave.open('sfx6.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(trk,-1,1)*32767).astype(np.int16).tobytes()); w.close()
print(round(TOT,1)); [print(k,round(a,1),round(b,1)) for k,a,b in seq]
