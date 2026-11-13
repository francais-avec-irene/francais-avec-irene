import json,subprocess,numpy as np,wave
T=json.load(open('/home/claude/voice/timeline.json'));SR=44100
v=np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i','/home/claude/voice/v.m4a','-ac','1','-ar',str(SR),'-af','highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=120','-f','f32le','-'],capture_output=True).stdout,np.float32)
w=wave.open('sfx.wav');sfx=np.frombuffer(w.readframes(w.getnframes()),np.int16)/32767.;w.close()
n=int(T['DUR']*SR)+SR;voice=np.zeros(n);fx=np.zeros(n);fx[:min(n,len(sfx))]=sfx[:n]
for k,(a,b) in T['clips'].items():
    c=v[int(a*SR):int(b*SR)].astype(float).copy();f=int(.03*SR);c[:f]*=np.linspace(0,1,f);c[-f:]*=np.linspace(1,0,f)
    i=int(T['place'][k]*SR);voice[i:i+len(c)]+=c
voice=voice/np.max(np.abs(voice))*10**(-2/20)
# duck sfx under voice
env=np.convolve(np.abs(voice),np.ones(int(.2*SR))/(.2*SR),'same');duck=np.where(env>0.02,0.45,1.0)
duck=np.convolve(duck,np.ones(int(.1*SR))/(.1*SR),'same')
out=voice+fx*0.8*duck;out=out/max(1,np.max(np.abs(out))/0.97)
w=wave.open('mix.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes());w.close()
