import numpy as np, wave
SR=44100; DUR=64.0; out=np.zeros(int(SR*DUR))
def add(t,sig):
    i=int(t*SR); n=min(len(sig),len(out)-i); out[i:i+n]+=sig[:n]
def mix(*s):
    n=max(len(x) for x in s); r=np.zeros(n)
    for x in s: r[:len(x)]+=x
    return r
def env(n,a=.005,r=.1):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/r)
def tone(f,d,a=.005,r=.1,typ='sin'):
    n=int(d*SR);fa=np.full(n,f) if np.isscalar(f) else f;ph=2*np.pi*np.cumsum(fa)/SR
    w=np.sin(ph) if typ=='sin' else np.sign(np.sin(ph))*.5+np.sin(ph)*.5
    return w*env(n,a,r)
def sweep(f0,f1,d,r=.2): n=int(d*SR); return tone(np.geomspace(f0,f1,n),d,.01,r)
def noise(d,r=.1): n=int(d*SR); x=np.random.RandomState(1).randn(n); x=np.convolve(x,np.ones(8)/8,'same'); return x*env(n,.01,r)*.4
whoosh=lambda: mix(noise(.35,.12)*.8,sweep(300,1200,.35,.15)*.3)
pop=lambda: sweep(400,900,.09,.04)
blip=lambda: tone(1200,.06,.002,.02)*.5
ding=lambda: mix(tone(1318.5,.6,.003,.25),tone(1975.5,.6,.003,.2)*.6,tone(2637,.5,.003,.12)*.3)
coin=lambda: np.concatenate([tone(988,.07,.002,.05),tone(1319,.3,.002,.12)])
buzz=lambda: mix(tone(110,.45,.01,.3,'sq')*.9,tone(116,.45,.01,.3,'sq')*.6)
def siren(d=1.0):
    n=int(d*SR);t=np.arange(n)/SR;f=700+200*np.sign(np.sin(2*np.pi*3*t));return tone(f,d,.02,10)*np.minimum(1,(d-t)/.15)*.35
thud=lambda: mix(sweep(180,50,.25,.12)*1.2,noise(.15,.05))
import bisect
def pw(x,A,B):
    for i in range(1,len(A)):
        if x<=A[i]: return B[i-1]+(x-A[i-1])*(B[i]-B[i-1])/(A[i]-A[i-1])
    return B[-1]+(x-A[-1])
import json
T=json.load(open('/home/claude/voice/timeline.json'))
SO=T['SO'];HO=T['HO'];HN=T['HN'];EO=T['EO'];EN=T['EN'];S0=T['S0']
_add=add
add(0,whoosh())
for i in range(6): add(pw(.15+i*.24,HO,HN),pop()*.7)
add(pw(1.75,HO,HN),sweep(300,700,.25,.12)); add(S0-.45,noise(.5,.15)*.6)
for si in range(3):
    b0=T['scenes'][si]['start'];SN=T['scenes'][si]['SN']
    def add(x,sig,b0=b0,SN=SN): _add(b0+pw(x,SO,SN),sig)
    b=0
    add(b+.05,whoosh()); add(b+.45,pop())
    for k in range(int((2.3-.75)/.045)): add(b+.75+k*.045,blip()*.35)
    add(b+2.55,buzz()); add(b+2.6,siren(1.1))
    if si==1:
        for k in range(5): add(b+2.75+k*.07,thud()*.7)
    elif si==0: add(b+2.9,sweep(500,1500,.3,.15)*.6)
    else: add(b+2.85,whoosh()); add(b+3.15,noise(.3,.08)*.7)
    add(b+4.0,whoosh()*.7); add(b+7.45,ding()); add(b+7.6,coin()*.8); add(b+9.6,noise(.45,.12)*.6)
E=T['END']
add=lambda x,sig:_add(E+pw(x,EO,EN),sig)
E=0
for k in range(3): add(E+.15+k*.28,ding()*.6)
add(E+1.2,sweep(300,900,.3,.15)); add(E+1.25,ding()*.5); add(E+2.6,coin())
out=out/np.max(np.abs(out))*10**(-14/20)
w=wave.open('sfx.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes());w.close()
