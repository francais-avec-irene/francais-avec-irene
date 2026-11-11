import numpy as np, wave, subprocess
SR=48000
def tone(freqs,dur,vol=.5,shape='sin'):
    out=[]
    for f in freqs:
        t=np.arange(int(SR*dur))/SR
        w=np.sign(np.sin(2*np.pi*f*t)) if shape=='sq' else np.sin(2*np.pi*f*t)
        env=np.minimum(1,t*200)*np.exp(-t*6/dur)
        out.append(w*env*vol)
    return np.concatenate(out)
S={
 'coin':tone([988,1319],.09,.35),
 'tick':tone([1200],.06,.3),
 'ok':tone([1047,1319,1568],.09,.35),
 'power':tone([523,659,784,1047,1319],.08,.3),
 'boss':tone([180,140,180,140],.15,.35),
 'win':np.concatenate([tone([523,659,784],.1,.3),tone([1047],.4,.3)]),
}
R=[(14.2,15.45,17.45,20.6),(20.6,21.6,22.95,25.7),(25.7,26.75,28.35,33.7),(33.7,34.65,35.95,38.8)]
P='/home/claude/reel/reel_livello4_'
seq=[(P+'01_titolo.png',0,14.2)]; sfx=[('coin',0.15)]
names=['02_round1','04_round2','06_round3','08_round4']; ans=['03_round1','05_round2','07_round3','09_round4']
for (a,b,c,d),q,r in zip(R,names,ans):
    seq.append((P+q+'_domanda.png',a,b)); step=(c-b)/3
    for j,n in enumerate([3,2,1]):
        seq.append((P+q+f'_domanda_t{n}.png',b+j*step,b+(j+1)*step)); sfx.append(('tick',b+j*step))
    seq.append((P+r+'_risposta.png',c,d)); sfx.append(('ok',c))
seq.append((P+'10_powerup.png',38.8,57.0)); sfx.append(('power',38.8))
seq.append((P+'11_boss_domanda.png',57.0,59.85)); sfx.append(('boss',57.0))
step=(62.1-59.85)/3
for j,n in enumerate([3,2,1]):
    seq.append((P+f'11_boss_domanda_t{n}.png',59.85+j*step,59.85+(j+1)*step)); sfx.append(('tick',59.85+j*step))
seq.append((P+'12_boss_risposta.png',62.1,65.6)); sfx.append(('ok',62.1))
seq.append((P+'13_fine.png',65.6,76.36)); sfx.append(('win',65.6))
with open('list.txt','w') as f:
    for img,a,b in seq: f.write(f"file '{img}'\nduration {b-a:.3f}\n")
    f.write(f"file '{seq[-1][0]}'\n")
tot=int(SR*76.4); trk=np.zeros(tot)
for k,t in sfx:
    s=S[k]; i=int(t*SR); trk[i:i+len(s)]+=s[:tot-i]
trk=np.clip(trk,-1,1); pcm=(trk*32767).astype(np.int16)
w=wave.open('sfx.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
