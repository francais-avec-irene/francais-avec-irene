import asyncio
from playwright.async_api import async_playwright
D='/home/claude/reel/'
F="'Bricolage Grotesque', system-ui, sans-serif"; PX="'Press Start 2P', monospace"
PINK,CY,YEL,GRN,INK='#FF4FA3','#3FE0FF','#FFD23F','#3DFF8A','#12082E'
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Press+Start+2P&display=swap">'
def bg(tint='#12082E'):
    return f'''<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 78%, rgba(255,79,163,.35), rgba(255,79,163,0) 40%), linear-gradient(180deg,{tint} 0%,#1E0B4A 60%,#2A0B52 100%)"></div>
<div style="position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.7) 1.5px, transparent 1.5px);background-size:90px 90px;opacity:.35"></div>
<div style="position:absolute;left:-400px;right:-400px;bottom:-200px;height:700px;transform:perspective(500px) rotateX(62deg);transform-origin:50% 0;background-image:linear-gradient(rgba(255,79,163,.85) 3px, transparent 3px),linear-gradient(90deg, rgba(255,79,163,.85) 3px, transparent 3px);background-size:110px 110px;"></div>'''
def hud(score='0000',hearts=3,lv='LV 4'):
    h=''.join(f'<span style="color:{PINK if i<hearts else "rgba(255,255,255,.25)"}">♥</span>' for i in range(3))
    return f'''<div style="position:absolute;left:50px;right:50px;top:60px;display:flex;align-items:center;justify-content:space-between">
<img src="logo.png" style="width:120px;height:120px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 5px #fff,0 0 30px rgba(63,224,255,.6)">
<div style="display:flex;flex-direction:column;align-items:center;gap:14px"><span style="font-family:{PX};font-size:34px;color:{YEL};text-shadow:0 0 14px rgba(255,210,63,.8)">{lv}</span><span style="font-size:44px;letter-spacing:8px">{h}</span></div>
<div style="display:flex;flex-direction:column;align-items:flex-end;gap:10px"><span style="font-family:{PX};font-size:22px;color:rgba(255,255,255,.8)">SCORE</span><span style="font-family:{PX};font-size:40px;color:{CY};text-shadow:0 0 14px rgba(63,224,255,.9)">{score}</span></div></div>'''
def timer(frac,label):
    return f'''<div style="position:absolute;left:60px;right:60px;top:230px;display:flex;align-items:center;gap:24px"><span style="font-family:{PX};font-size:24px;color:#fff;white-space:nowrap">{label}</span>
<div style="flex:1;height:30px;border:4px solid #fff;padding:4px;box-sizing:border-box"><div style="width:{int(frac*100)}%;height:100%;background:linear-gradient(90deg,{GRN},{YEL})"></div></div></div>'''
def screen(img,pos='center',border=CY):
    return f'''<div style="position:absolute;left:60px;right:60px;top:300px;height:720px;border:8px solid {border};box-shadow:0 0 40px {border}, inset 0 0 0 6px {INK};overflow:hidden;border-radius:6px"><img src="{img}" style="width:100%;height:100%;object-fit:cover;object-position:{pos}"><div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg, rgba(0,0,0,.12) 0 3px, transparent 3px 6px)"></div></div>'''
def btn(t,c,state='idle'):
    if state=='ok':  extra=f'background:{GRN};color:{INK};box-shadow:0 14px 0 #18A050,0 0 60px {GRN};transform:scale(1.06)'
    elif state=='off': extra='background:#3A2A5E;color:rgba(255,255,255,.35);box-shadow:0 14px 0 #21163A'
    else: extra=f'background:{c};color:{INK};box-shadow:0 14px 0 rgba(0,0,0,.45),0 0 40px {c}'
    return f'<div style="width:440px;height:200px;border-radius:30px;display:flex;align-items:center;justify-content:center;font-family:{PX};font-size:90px;{extra}">{t}</div>'
def word(blank,w,it,color='#fff'):
    return f'''<div style="position:absolute;left:0;right:0;top:1060px;text-align:center"><div style="font-family:{F};font-weight:800;font-size:150px;line-height:1;color:#fff;text-shadow:0 6px 0 rgba(0,0,0,.4)"><span style="color:{color}">{blank}</span> {w}</div><div style="margin-top:22px;font-family:{F};font-weight:500;font-size:48px;color:rgba(255,255,255,.8)">{it}</div></div>'''
def buttons(a='idle',b='idle'):
    return f'<div style="position:absolute;left:60px;right:60px;top:1420px;display:flex;justify-content:space-between">{btn("LE",CY,a)}{btn("LA",PINK,b)}</div>'
def foot(): return f'<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-family:{F};font-weight:500;font-size:34px;color:rgba(255,255,255,.75)">Irene · Francese per italiani</div>'
def wrap(inner,tint='#12082E'):
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>body{{margin:0}}</style></head><body><div style="position:relative;width:1080px;height:1920px;overflow:hidden;color:#fff">{bg(tint)}{inner}</div></body></html>'
FR={}
FR['01_titolo']=wrap(f'''<div style="position:absolute;left:0;right:0;top:120px;display:flex;justify-content:center"><img src="logo.png" style="width:220px;height:220px;border-radius:50%;box-shadow:0 0 0 8px #fff,0 0 60px rgba(63,224,255,.7)"></div>
<div style="position:absolute;left:0;right:0;top:470px;text-align:center"><div style="font-family:{PX};font-size:110px;color:{YEL};text-shadow:0 0 30px rgba(255,210,63,.9),0 8px 0 #B8580F">LIVELLO 4</div>
<div style="margin-top:110px;font-family:{F};font-weight:800;font-size:230px;line-height:1"><span style="color:{CY};text-shadow:0 0 40px {CY}">LE</span> <span style="font-size:110px">o</span> <span style="color:{PINK};text-shadow:0 0 40px {PINK}">LA</span>?</div>
<div style="margin-top:50px;font-family:{F};font-weight:800;font-size:64px;line-height:1.15">Il genere che inganna<br>gli italiani</div>
<div style="margin:70px auto 0;display:inline-block;padding:22px 40px;border:5px solid #fff;font-family:{PX};font-size:30px;line-height:1.6">5 ROUND · 3 SECONDI</div>
<div style="margin-top:90px;font-family:{PX};font-size:46px;color:#fff;text-shadow:0 0 20px {PINK}">▶ PRESS START</div></div>{foot()}''')

R=[('mer.jpg','60% 50%','mer','(il mare)','LA'),('fleur.jpg','center 40%','fleur','(il fiore)','LA'),('printemps.jpg','center 50%','printemps','(la primavera)','LE'),('couleur.jpg','30% 50%','couleur','(il colore)','LA')]
n=2
for i,(img,pos,w,it,ok) in enumerate(R):
    FR[f'{n:02d}_round{i+1}_domanda']=wrap(hud(f'{i*100:04d}',3)+timer(1,f'ROUND {i+1}/5')+screen(img,pos)+word('___',w,it,YEL)+buttons()+foot()); n+=1
    FR[f'{n:02d}_round{i+1}_risposta']=wrap(hud(f'{(i+1)*100:04d}',3)+timer(.35,f'ROUND {i+1}/5')+screen(img,pos,GRN)+f'<div style="position:absolute;left:0;right:0;top:560px;text-align:center"><span style="display:inline-block;padding:26px 50px;background:{GRN};color:{INK};font-family:{PX};font-size:64px;transform:rotate(-4deg);box-shadow:0 12px 0 #18A050">PERFECT! +100</span></div>'+word(ok,w,it,GRN)+(buttons('ok','off') if ok=='LE' else buttons('off','ok'))+foot()); n+=1
FR['10_powerup']=wrap(hud('0400',3)+f'''<div style="position:absolute;left:60px;right:60px;top:290px;bottom:220px;border:8px solid {YEL};border-radius:30px;background:rgba(18,8,46,.88);box-shadow:0 0 60px rgba(255,210,63,.6);padding:70px 60px;box-sizing:border-box;display:flex;flex-direction:column;gap:46px">
<div style="font-family:{PX};font-size:54px;color:{YEL};text-align:center;text-shadow:0 0 20px rgba(255,210,63,.8)">★ POWER-UP ★</div>
<img src="fleur.jpg" style="width:100%;height:420px;object-fit:cover;border-radius:18px;border:5px solid #fff">
<div style="font-family:{F};font-weight:800;font-size:76px;line-height:1.1">Le parole in <span style="color:{PINK}">-EUR</span><br>sono quasi sempre <span style="color:{PINK}">LA</span></div>
<div style="font-family:{F};font-weight:500;font-size:52px;line-height:1.4">la coul<b style="color:{PINK}">eur</b> · la fl<b style="color:{PINK}">eur</b><br>la p<b style="color:{PINK}">eur</b> · la doul<b style="color:{PINK}">eur</b></div>
<div style="padding:30px 36px;border-radius:20px;background:rgba(63,224,255,.15);border:4px dashed {CY};font-family:{F};font-weight:800;font-size:50px;line-height:1.3"><span style="font-family:{PX};font-size:30px;color:{CY}">ATTENZIONE!</span><br>le bonheur · le malheur · l'honneur</div></div>'''+foot())
FR['11_boss_domanda']=wrap(hud('0400',3,'BOSS')+f'<div style="position:absolute;left:60px;right:60px;top:230px;text-align:center;font-family:{PX};font-size:44px;color:#FF3B3B;text-shadow:0 0 24px #FF3B3B">!! BOSS FINALE !!</div>'+screen('hd_danse.jpg','30% 75%','#FF3B3B')+word('___','bonheur','(la felicità)','#FF6B6B')+buttons()+foot(),'#3A0820')
FR['12_boss_risposta']=wrap(hud('0500',3,'BOSS')+f'<div style="position:absolute;left:60px;right:60px;top:230px;text-align:center;font-family:{PX};font-size:44px;color:#FF3B3B;text-shadow:0 0 24px #FF3B3B">!! BOSS FINALE !!</div>'+screen('hd_danse.jpg','30% 75%',GRN)+f'<div style="position:absolute;left:0;right:0;top:540px;text-align:center"><span style="display:inline-block;padding:26px 44px;background:{GRN};color:{INK};font-family:{PX};font-size:50px;line-height:1.5;transform:rotate(-4deg);box-shadow:0 12px 0 #18A050">BOSS SCONFITTO!<br>+100</span></div>'+word('LE','bonheur','(la felicità)',GRN)+buttons('ok','off')+foot(),'#3A0820')
FR['13_fine']=wrap(f'''<div style="position:absolute;left:0;right:0;top:200px;text-align:center"><div style="font-family:{PX};font-size:78px;line-height:1.4;color:{GRN};text-shadow:0 0 30px {GRN}">LIVELLO 4<br>SUPERATO!</div>
<div style="margin-top:70px;font-size:150px;color:{YEL};letter-spacing:20px;text-shadow:0 0 30px rgba(255,210,63,.8)">★★★</div>
<div style="margin-top:40px;font-family:{PX};font-size:56px;color:{CY}">SCORE 0500</div>
<div style="margin-top:100px;font-family:{F};font-weight:800;font-size:80px;line-height:1.15">Quanti punti<br>avete fatto?</div>
<div style="margin-top:40px;font-family:{F};font-weight:500;font-size:50px;color:rgba(255,255,255,.85)">Scrivetelo nei commenti<br>e salvate il reel per ripassare</div>
<div style="margin:90px auto 0;display:inline-block;padding:34px 50px;border-radius:30px;background:{PINK};color:#fff;font-family:{PX};font-size:36px;line-height:1.5;box-shadow:0 14px 0 #A01E62,0 0 50px {PINK}">SEGUITEMI ▶<br>LIVELLO 5</div></div>
<div style="position:absolute;left:0;right:0;bottom:150px;display:flex;justify-content:center"><img src="logo.png" style="width:150px;height:150px;border-radius:50%;box-shadow:0 0 0 6px #fff"></div>{foot()}''')
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        for k,html in FR.items():
            open(D+k+'.html','w').write(html)
            await pg.goto(f'file://{D}{k}.html'); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=D+f'reel_livello4_{k}.png')
        await b.close()
asyncio.run(main())
from PIL import Image
ks=list(FR); W=Image.new('RGB',(len(ks)*360+ (len(ks)-1)*20,640),'white')
for i,k in enumerate(ks): W.paste(Image.open(D+f'reel_livello4_{k}.png').convert('RGB').resize((360,640)),(i*380,0))
W.save(D+'reel_livello4_anteprima.png')
