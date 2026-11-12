import asyncio; from render import *
P=dict(a1='#FFE9A8',a2='#A8DCFF',a3='#fff',ink='#3D0414')
k=kit(P); h,p,ex,tag,pill,pills,hl,num,c,row,bub=k['h'],k['p'],k['ex'],k['tag'],k['pill'],k['pills'],k['hl'],k['num'],k['c'],k['row'],k['bubble']
CH=('#B5123A','#3D0414','rgba(181,18,58,.5)'); TC=('#1D5C8C','#08223A','rgba(29,92,140,.55)'); BX=('#B8432A','#3E1206','rgba(184,67,42,.55)')
REX='s_rex.jpg' if True or __import__('os').path.exists(D+'s_rex.jpg') and __import__('os').path.getsize(D+'s_rex.jpg')>10000 else 's_canal.jpg'
SL=[
 ('s_villette.jpg','top:0;height:950px;object-position:30% 50%',[tag('C1 · LE FRANÇAIS PARLÉ'),h('Quello che '+hl('i libri')+'<br>non vi dicono',96),bub('T\'as vu ?',P['a1'],'left',-2),bub('Chais pas !',P['a2'],'right',2)],'1/6 · scorri →',CH),
 (REX,'top:0;height:900px;object-position:50% 40%',[num('1 · ON'),h(hl('On')+' = nous',110),ex('On va au cinéma ce soir ?','Andiamo al cinema stasera?'),p('Il verbo resta alla 3ª singolare, ma l\'aggettivo segue il senso: <b>On est contents.</b>',34)],'2/6 · scorri →',TC),
 ('s_luxembourg.jpg','top:0;height:900px;object-position:50% 70%',[num('2 · IL NE'),h('Il « ne »<br>'+hl('sparisce'),100),ex('Je sais pas. · C\'est pas grave.','Non lo so. · Non fa niente.'),p('Nel parlato è quasi sistematico. Per iscritto, in una mail di lavoro o al DALF, il <b>ne</b> resta.',34)],'3/6 · scorri →',BX),
 ('s_plages.jpg','top:0;height:900px;object-position:50% 50%',[num('3 · LE CONTRAZIONI'),h('Si '+hl('accorcia')+' tutto',96),row('tu as','T\'as vu ?'),row('je ne sais','Chais pas'),row('il y a','Y a du monde !'),row('oui','Ouais')],'4/6 · scorri →',CH),
 ('s_canal.jpg','top:0;height:900px;object-position:50% 45%',[num('4 · TRE REGISTRI'),h('Una frase,<br>'+hl('tre stili'),96),row('fam.','T\'as pas faim ?'),row('corr.','Tu n\'as pas faim ?'),row('sost.','N\'as-tu pas faim ?'),p('Non hai fame?',32)],'5/6 · scorri →',TC),
 ('s_baguettes.jpg','top:-120px;height:1150px;object-position:50% 40%',[h('La '+hl('sfida')+'!',116),p('Dite in <b>francese parlato</b>, nei commenti:',40),f'<p style="margin:0;font-family:{F};font-weight:800;font-style:italic;font-size:52px;line-height:1.2;color:{P["a1"]};transform:rotate(-1deg)">« Je ne sais pas s\'il y a du pain. »</p>'],None,BX),
]
asyncio.run(render('francese_parlato',P,SL,'FRANCESE<br>PARLATO'))
