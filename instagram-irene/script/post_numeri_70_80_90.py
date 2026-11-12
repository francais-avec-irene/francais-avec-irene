import asyncio; from render import *
P=dict(a1='#FFE14D',a2='#9FE7FF',a3='#fff',ink='#2A0E00')
k=kit(P); h,p,ex,tag,pill,pills,hl,num,c,row=k['h'],k['p'],k['ex'],k['tag'],k['pill'],k['pills'],k['hl'],k['num'],k['c'],k['row']
OR=('#E0561B','#5A1A05','rgba(224,86,27,.55)'); RO=('#C7302A','#4A0B08','rgba(199,48,42,.52)'); AM=('#D9871A','#4D2A03','rgba(190,110,10,.55)')
SL=[
 ('g_abricots.jpg','top:-80px;height:1100px;object-position:50% 40%',[tag('A1 · I NUMERI'),h(hl('97')+' = 4 × 20<br>+ 10 + 7',112),p('Benvenuti nella <b>matematica francese</b>!',42),pills(pill('70',P['a1'],-4),pill('80',P['a2'],3),pill('90','#fff',-2))],'1/6 · scorri →',OR),
 ('g_peches.jpg','top:-60px;height:1100px;object-position:50% 50%',[num('70 = 60 + 10'),h(hl('soixante-dix'),104),row('71','soixante et onze'),row('75','soixante-quinze'),row('79','soixante-dix-neuf')],'2/6 · scorri →',RO),
 ('g_tomates.jpg','top:0;height:900px;object-position:40% 50%',[num('80 = 4 × 20'),h(hl('quatre-vingts'),100),p('<b>Con la S!</b> Quattro « venti ».',40),row('81','quatre-vingt-un'),p('Niente S e niente « et ».',36)],'3/6 · scorri →',AM),
 ('g_etal.jpg','top:-60px;height:1100px;object-position:50% 40%',[num('90 = 4 × 20 + 10'),h(hl('quatre-vingt-dix'),94),row('91','quatre-vingt-onze'),row('99','quatre-vingt-dix-neuf')],'4/6 · scorri →',OR),
 ('g_ouchy.jpg','top:0;height:900px;object-position:50% 50%',[num('IN BELGIO E IN SVIZZERA'),h('Più '+hl('semplice')+'!',100),row('70','septante'),row('90','nonante'),p('In alcuni cantoni svizzeri (Vaud, Vallese, Friburgo) anche <b>80 = huitante</b>.',34)],'5/6 · scorri →',RO),
 ('g_marche_bleu.jpg','top:0;height:900px;object-position:50% 50%',[h('La '+hl('sfida')+'!',116),p('Scrivete in lettere il vostro <b>anno di nascita</b> nei commenti.',42),ex('1987 = mille neuf cent quatre-vingt-sept',None,40)],None,AM),
]
asyncio.run(render('numeri_70_80_90',P,SL,'MATEMATICA<br>FRANCESE'))
