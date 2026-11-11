import numpy as np, wave, subprocess
SR=48000
SRC='/mnt/user-data/uploads/69f2f12d-pour_pendant.m4a'
subprocess.run(['ffmpeg','-v','error','-y','-i',SRC,'-af','highpass=f=80,lowpass=f=12000,afftdn=nf=-30,acompressor=threshold=-26dB:ratio=3:attack=10:release=150:makeup=4,loudnorm=I=-15:TP=-1.5:LRA=9','-ac','1','-ar',str(SR),'voce5.wav'],check=True)
TOT=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','voce5.wav']))
def tone(freqs,dur,vol=.5):
    out=[]
    for f in freqs:
        t=np.arange(int(SR*dur))/SR; out.append(np.sin(2*np.pi*f*t)*np.minimum(1,t*200)*np.exp(-t*6/dur)*vol)
    return np.concatenate(out)
S={'coin':tone([988,1319],.09,.35),'err':tone([220,160],.18,.35),'power':tone([523,659,784,1047],.08,.3),
   'ok':tone([1047,1319,1568],.09,.3),'bonus':tone([784,988,1175,1568],.07,.3),'win':np.concatenate([tone([523,659,784],.1,.3),tone([1047],.4,.3)])}
P='/home/claude/r5/reel_livello5_'
seq=[('01_titolo',0,9.6),('02_errore',9.6,22.1),('03_pendant',22.1,34.9),('04_pendant2',34.9,47.5),('05_pour',47.5,69.8),('06_depuis',69.8,89.8),('07_riepilogo',89.8,101.5),('08_bonus',101.5,114.8),('09_fine',114.8,TOT)]
sfx=[('coin',0.1),('err',13.8),('power',22.1),('power',47.5),('power',69.8),('ok',89.8),('bonus',101.5),('win',114.8)]
with open('list5.txt','w') as f:
    for k,a,b in seq: f.write(f"file '{P}{k}.png'\nduration {b-a:.3f}\n")
    f.write(f"file '{P}{seq[-1][0]}.png'\n")
trk=np.zeros(int(SR*(TOT+1)))
for k,t in sfx:
    s=S[k]; i=int(t*SR); trk[i:i+len(s)]+=s[:len(trk)-i]
w=wave.open('sfx5.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(trk,-1,1)*32767).astype(np.int16).tobytes()); w.close()
