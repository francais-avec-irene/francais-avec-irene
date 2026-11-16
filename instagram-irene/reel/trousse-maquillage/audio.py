import subprocess,json,numpy as np
SR=44100
d=subprocess.run(['ffmpeg','-loglevel','error','-i','voice.wav','-af','highpass=f=70,afftdn=nf=-30','-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout
x=np.frombuffer(d,np.int16).astype(np.float32)/32768
P=0.09
def seg(a,b): return x[int((a-P)*SR):int((b+P)*SR)]
# segments (start,end) from silencedetect
L={'1a':(2.97,5.42),'1b':(6.23,8.02),'2a':(8.80,9.96),'2b':(10.46,12.15),
 '3':(13.48,14.39),'4':(15.06,16.65),'5':(17.87,19.17),'6':(20.23,21.52),'7':(22.74,23.53),'8':(24.67,25.48),
 '9':(26.85,27.89),'10':(29.31,30.11),'11':(31.19,31.99),'12':(32.82,33.77),'13':(34.82,35.73),
 '14':(37.59,39.89),'15':(40.91,43.01),'16':(44.35,48.35)}
out=[];t=0.0;T={}
def sil(s):
    global t;out.append(np.zeros(int(s*SR),np.float32));t+=s
def put(k):
    global t;a=seg(*L[k]);T[k]=(round(t+P,3),round(t+len(a)/SR-P,3));out.append(a);t+=len(a)/SR
sil(0.7);put('1a');sil(0.45);put('1b');sil(0.7);put('2a');sil(0.35);put('2b');sil(0.6)
for k in ['3','4','5','6','7','8']:
    T['cd'+k]=round(t,3);sil(2.3);put(k);sil(1.25)
put('9');sil(0.9)
for k in ['10','11','12','13']:
    T['cd'+k]=round(t,3);sil(2.3);put(k);sil(1.35)
sil(0.2);put('14');sil(0.6);put('15');sil(0.8);put('16');sil(3.2)
T['end']=round(t,3)
y=np.concatenate(out)
y=(np.clip(y,-1,1)*32767).astype(np.int16)
open('raw.pcm','wb').write(y.tobytes())
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','s16le','-ar',str(SR),'-ac','1','-i','raw.pcm','-af','loudnorm=I=-15:TP=-1.5:LRA=9','-ar','48000','-c:a','aac','-b:a','192k','voice_final.m4a'])
json.dump(T,open('timeline.json','w'),indent=1);print(T['end'])
