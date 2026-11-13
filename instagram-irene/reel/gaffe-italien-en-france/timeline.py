import json
clips={'hook':(0.0,2.25),
 'b1':(3.10,6.55),'e1a':(7.40,9.40),'e1b':(10.10,12.70),'c1':(13.60,15.00),
 'b2':(16.60,19.05),'e2a':(19.90,22.25),'e2b':(22.65,24.90),'c2':(25.92,27.50),
 'b3':(29.92,33.10),'e3a':(34.18,37.10),'e3b':(37.38,41.10),'c3':(41.72,43.30),
 'end':(44.00,48.65)}
D={k:b-a for k,(a,b) in clips.items()}
place={'hook':0.1}
S0=3.6
SO=[0,.45,.8,2.3,2.55,4.0,5.2,7.45,9.75,10]
scenes=[];t=S0
for k in (1,2,3):
    Db,D1,D2,Dc=D[f'b{k}'],D[f'e{k}a'],D[f'e{k}b'],D[f'c{k}']
    typ_end=1.0+Db; e=typ_end+0.7; x1=e+1.8; x2=x1+0.2+D1+0.3; c=x2+D2+0.9; ce=c+0.25+Dc+1.5
    SN=[0,.7,1.0,typ_end,e,x1,x2,c,ce,ce+.4]
    place[f'b{k}']=t+1.0; place[f'e{k}a']=t+x1+0.2; place[f'e{k}b']=t+x2; place[f'c{k}']=t+c+0.25
    scenes.append({'start':t,'dur':SN[-1],'SN':SN}); t+=SN[-1]
END=t; EN=[0,2.0,2.4,5.3,5.7,9.0]; place['end']=END+2.0
DUR=END+EN[-1]
json.dump({'S0':S0,'SO':SO,'scenes':scenes,'END':END,'EO':[0,1.2,1.6,2.6,2.95,6.2],'EN':EN,'HO':[0,1.75,2.15,3.2],'HN':[0,2.0,2.5,3.6],'DUR':DUR,'clips':clips,'place':place},open('timeline.json','w'),indent=1)
print('DUR',DUR,[round(s['start'],2) for s in scenes],END)
