import numpy as np, wave, subprocess
SR=48000
SRC='/mnt/user-data/uploads/38bf0c90-reel_2_ok.m4a'
subprocess.run(['ffmpeg','-v','error','-y','-i',SRC,'-af','highpass=f=80,lowpass=f=12000,afftdn=nf=-30,acompressor=threshold=-26dB:ratio=3:attack=10:release=150:makeup=4,loudnorm=I=-15:TP=-1.5:LRA=9','-ac','1','-ar',str(SR),'-f','s16le','voce.raw'],check=True)
v=np.frombuffer(open('voce.raw','rb').read(),dtype=np.int16).astype(np.float32)
# pauses (q_end, a_start) in original time; insert silence to reach 2.7 s
P=[(12.95,14.72),(17.60,19.21),(22.45,23.67),(29.13,30.61),(52.42,54.19)]
ins=[(round((a+b)/2,3),max(0,2.7-(b-a))) for a,b in P]
def nt(t): return t+sum(d for p,d in ins if p<t)
parts=[];last=0
for p,d in ins:
    i=int(p*SR); parts+= [v[last:i], np.zeros(int(d*SR),dtype=np.float32)]; last=i
parts.append(v[last:]); voice=np.concatenate(parts)
w=wave.open('voce_finale.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(voice.astype(np.int16).tobytes()); w.close()
TOT=len(voice)/SR
def tone(freqs,dur,vol=.5):
    out=[]
    for f in freqs:
        t=np.arange(int(SR*dur))/SR; out.append(np.sin(2*np.pi*f*t)*np.minimum(1,t*200)*np.exp(-t*6/dur)*vol)
    return np.concatenate(out)
S={'coin':tone([988,1319],.09,.35),'tick':tone([1200],.06,.3),'ok':tone([1047,1319,1568],.09,.35),
   'power':tone([523,659,784,1047,1319],.08,.3),'boss':tone([180,140,180,140],.15,.35),
   'win':np.concatenate([tone([523,659,784],.1,.3),tone([1047],.4,.3)])}
P_='/home/claude/reel/reel_livello4_'
# (q_start, q_end, a_start, a_end) original
R=[(12.2,12.95,14.72,16.7),(16.7,17.60,19.21,21.5),(21.5,22.45,23.67,28.2),(28.2,29.13,30.61,33.0)]
q=['02_round1','04_round2','06_round3','08_round4']; r=['03_round1','05_round2','07_round3','09_round4']
seq=[(P_+'01_titolo.png',0,nt(12.2))]; sfx=[('coin',0.1)]
def round_(qs,qe,as_,ae,qimg,aimg):
    a,b,c,d=nt(qs),nt(qe)+.05,nt(as_)-.05,nt(ae)
    seq.append((qimg,a,b)); st=(c-b)/3
    for j,n in enumerate([3,2,1]):
        seq.append((qimg.replace('.png',f'_t{n}.png'),b+j*st,b+(j+1)*st)); sfx.append(('tick',b+j*st))
    seq.append((aimg,c,d)); sfx.append(('ok',c))
for (qs,qe,as_,ae),qq,rr in zip(R,q,r): round_(qs,qe,as_,ae,P_+qq+'_domanda.png',P_+rr+'_risposta.png')
seq.append((P_+'10_powerup.png',nt(33.0),nt(49.7))); sfx.append(('power',nt(33.0)))
sfx.append(('boss',nt(49.7)))
round_(49.7,52.42,54.19,57.9,P_+'11_boss_domanda.png',P_+'12_boss_risposta.png')
seq.append((P_+'13_fine.png',nt(57.9),TOT)); sfx.append(('win',nt(57.9)))
with open('list2.txt','w') as f:
    for img,a,b in seq: f.write(f"file '{img}'\nduration {b-a:.3f}\n")
    f.write(f"file '{seq[-1][0]}'\n")
trk=np.zeros(int(SR*(TOT+1)))
for k,t in sfx:
    s=S[k]; i=int(t*SR); trk[i:i+len(s)]+=s[:len(trk)-i]
w=wave.open('sfx2.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(trk,-1,1)*32767).astype(np.int16).tobytes()); w.close()
print('durata',round(TOT,2)); [print(round(a,2),round(b,2),img.split('_livello4_')[1]) for img,a,b in seq]
