import asyncio
from playwright.async_api import async_playwright
D='/home/claude/r6/'
F="'Bricolage Grotesque', system-ui, sans-serif"; PX="'Press Start 2P', monospace"
PINK,CY,YEL,GRN,BLU,RED,INK='#FF4FA3','#3FE0FF','#FFD23F','#3DFF8A','#4D8BFF','#FF3B3B','#12082E'
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Press+Start+2P&display=swap">'
def bg():
    return '''<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 80%, rgba(255,79,163,.35), rgba(255,79,163,0) 40%), linear-gradient(180deg,#12082E 0%,#1E0B4A 60%,#2A0B52 100%)"></div>
<div style="position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.7) 1.5px, transparent 1.5px);background-size:90px 90px;opacity:.35"></div>
<div style="position:absolute;left:-400px;right:-400px;bottom:-220px;height:600px;transform:perspective(500px) rotateX(62deg);transform-origin:50% 0;background-image:linear-gradient(rgba(255,79,163,.8) 3px, transparent 3px),linear-gradient(90deg, rgba(255,79,163,.8) 3px, transparent 3px);background-size:110px 110px;"></div>'''
def hud():
    return f'''<div style="position:absolute;left:50px;right:50px;top:60px;display:flex;align-items:center;justify-content:space-between">
<img src="logo.png" style="width:120px;height:120px;border-radius:50%;box-shadow:0 0 0 5px #fff,0 0 30px rgba(63,224,255,.6)">
<span style="font-family:{PX};font-size:34px;color:{YEL};text-shadow:0 0 14px rgba(255,210,63,.8)">LV 6</span>
<span style="font-family:{PX};font-size:20px;line-height:1.6;text-align:right;color:{PINK};text-shadow:0 0 12px rgba(255,79,163,.8)">ERRORI<br>TIPICI #3</span></div>'''
def foot(): return f'<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-family:{F};font-weight:500;font-size:34px;color:rgba(255,255,255,.75)">Irene · Francese per italiani</div>'
def wrap(inner): return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>body{{margin:0}}</style></head><body><div style="position:relative;width:1080px;height:1920px;overflow:hidden;color:#fff;font-family:{F}">{bg()}{inner}</div></body></html>'
def screen(img,pos,c,top=230,h=560):
    return f'<div style="position:absolute;left:60px;right:60px;top:{top}px;height:{h}px;border:8px solid {c};box-shadow:0 0 40px {c};overflow:hidden;border-radius:6px"><img src="{img}" style="width:100%;height:100%;object-fit:cover;object-position:{pos}"><div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg, rgba(0,0,0,.12) 0 3px, transparent 3px 6px)"></div></div>'
def badge(word,c,sub,top):
    return f'<div style="position:absolute;left:0;right:0;top:{top}px;text-align:center"><span style="display:inline-block;padding:24px 50px;border-radius:24px;background:{c};color:{INK};font-family:{PX};font-size:64px;box-shadow:0 12px 0 rgba(0,0,0,.45),0 0 50px {c}">{word}</span><div style="margin-top:28px;font-family:{PX};font-size:30px;color:{c};text-shadow:0 0 14px {c}">{sub}</div></div>'
def fr(t,it,top,fs=74):
    return f'<div style="position:absolute;left:70px;right:70px;top:{top}px;text-align:center"><div style="font-weight:800;font-size:{fs}px;line-height:1.12">{t}</div><div style="margin-top:22px;font-weight:500;font-size:44px;color:rgba(255,255,255,.75)">{it}</div></div>'
def tl(kind,c,top):
    # timeline svg 940x170: passato | oggi | futuro
    oggi=560
    base=f'<line x1="40" y1="90" x2="900" y2="90" stroke="rgba(255,255,255,.5)" stroke-width="6"/><line x1="{oggi}" y1="55" x2="{oggi}" y2="125" stroke="#fff" stroke-width="6"/><text x="{oggi}" y="165" fill="#fff" font-size="30" font-family="Bricolage Grotesque" font-weight="800" text-anchor="middle">oggi</text><text x="40" y="40" fill="rgba(255,255,255,.7)" font-size="28" font-family="Bricolage Grotesque">passato</text><text x="900" y="40" fill="rgba(255,255,255,.7)" font-size="28" font-family="Bricolage Grotesque" text-anchor="end">futuro</text>'
    if kind=='pendant': seg=f'<rect x="120" y="70" width="300" height="40" rx="8" fill="{c}"/><line x1="120" y1="55" x2="120" y2="125" stroke="{c}" stroke-width="8"/><line x1="420" y1="55" x2="420" y2="125" stroke="{c}" stroke-width="8"/>'
    elif kind=='pour': seg=f'<rect x="{oggi+30}" y="70" width="260" height="40" rx="8" fill="{c}" opacity=".9"/><polygon points="{oggi+290},60 {oggi+330},90 {oggi+290},120" fill="{c}"/>'
    else: seg=f'<rect x="200" y="70" width="{oggi-200}" height="40" rx="8" fill="{c}"/><polygon points="{oggi},60 {oggi+40},90 {oggi},120" fill="{c}"/><line x1="200" y1="55" x2="200" y2="125" stroke="{c}" stroke-width="8"/>'
    return f'<div style="position:absolute;left:70px;right:70px;top:{top}px"><svg width="940" height="180" viewBox="0 0 940 180" aria-hidden="true">{base}{seg}</svg></div>'
B=lambda t,c: f'<span style="color:{c};text-shadow:0 0 20px {c}">{t}</span>'
MAG='#FF3DF0'
def door(t,c,on):
    st=f'background:{c};color:{INK};box-shadow:0 12px 0 rgba(0,0,0,.45),0 0 60px {c}' if on else 'background:#2A1A50;color:rgba(255,255,255,.35);box-shadow:0 12px 0 #160C30'
    return f'<div style="width:440px;height:180px;border-radius:26px;display:flex;align-items:center;justify-content:center;font-family:{PX};font-size:62px;{st}">{t}</div>'
def doors(a,b,top=1460): return f'<div style="position:absolute;left:60px;right:60px;top:{top}px;display:flex;justify-content:space-between">{door("C\'EST",CY,a)}{door("IL EST",MAG,b)}</div>'
def rule(n,t,c,top): return f'<div style="position:absolute;left:0;right:0;top:{top}px;text-align:center"><div style="font-family:{PX};font-size:30px;color:{YEL}">REGOLA {n}</div><div style="margin-top:20px;font-weight:800;font-size:66px;color:{c};text-shadow:0 0 20px {c}">{t}</div></div>'
def ex(lines,top,fs=64): return f'<div style="position:absolute;left:70px;right:70px;top:{top}px;text-align:center;display:flex;flex-direction:column;gap:26px">'+''.join(f'<div><div style="font-weight:800;font-size:{fs}px;line-height:1.1">{a}</div><div style="margin-top:8px;font-weight:500;font-size:40px;color:rgba(255,255,255,.75)">{b}</div></div>' for a,b in lines)+'</div>'
FR={}
FR['01_titolo']=wrap(f'''<div style="position:absolute;left:0;right:0;top:120px;display:flex;justify-content:center"><img src="logo.png" style="width:200px;height:200px;border-radius:50%;box-shadow:0 0 0 8px #fff,0 0 60px rgba(63,224,255,.7)"></div>
<div style="position:absolute;left:0;right:0;top:430px;text-align:center"><div style="font-family:{PX};font-size:100px;color:{YEL};text-shadow:0 0 30px rgba(255,210,63,.9),0 8px 0 #B8580F">LIVELLO 6</div>
<div style="margin-top:60px;display:inline-block;padding:18px 36px;border:5px solid {MAG};font-family:{PX};font-size:28px;line-height:1.6;color:{MAG};text-shadow:0 0 12px {MAG}">LES ERREURS<br>TYPIQUEMENT ITALIENNES #3</div>
<div style="margin-top:110px;font-weight:800;font-size:150px;line-height:1">{B("C'est",CY)}<br><span style="font-size:80px">o</span><br>{B("il est",MAG)}?</div>
<div style="margin-top:100px;font-family:{PX};font-size:42px;text-shadow:0 0 20px {MAG}">▶ PRESS START</div></div>{foot()}''')
FR['02_hook']=wrap(hud()+f'''<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div style="font-family:{PX};font-size:34px;color:rgba(255,255,255,.8)">ITALIANO</div>
<div style="margin-top:30px;font-weight:800;font-size:260px;line-height:1">è</div>
<div style="margin-top:70px;font-size:110px;color:{YEL}">▼</div>
<div style="margin-top:50px;font-family:{PX};font-size:34px;color:rgba(255,255,255,.8)">FRANCESE</div></div>'''+doors(True,True,1080)+f'<div style="position:absolute;left:90px;right:90px;top:1360px;text-align:center;font-weight:800;font-size:56px;line-height:1.25;color:{YEL}">1 parola in italiano,<br>2 in francese!</div>'+foot())
FR['03_cest_nome']=wrap(hud()+screen('s_fete.jpg','40% 50%',CY,230,520)+rule(1,"C'EST + NOME",CY,800)+ex([("C'est mon frère.","È mio fratello."),("C'est un bon film.","È un bel film.")],990)+doors(True,False)+foot())
FR['04_ilest_agg']=wrap(hud()+screen('s_vitrine.jpg','50% 45%',MAG,230,520)+rule(2,"IL / ELLE EST + AGGETTIVO",MAG,800)+ex([("Ton frère ? Il est sympa.","Tuo fratello? È simpatico."),("Cette robe ? Elle est chère.","Quel vestito? È caro.")],990,60)+doors(False,True)+foot())
FR['05_professione']=wrap(hud()+f'''<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><span style="display:inline-block;padding:24px 46px;background:{RED};color:#fff;font-family:{PX};font-size:48px;transform:rotate(-3deg);box-shadow:0 12px 0 #8A1010,0 0 50px {RED}">TRAPPOLA!</span>
<div style="margin-top:60px;font-family:{PX};font-size:34px;color:{YEL}">LE PROFESSIONI</div>
<div style="margin-top:90px;font-weight:500;font-size:56px;color:rgba(255,255,255,.75)">Italiano: è medico</div>
<div style="margin-top:50px;font-weight:800;font-size:110px;line-height:1.1">Il est <span style="color:{RED};text-decoration:line-through;text-decoration-thickness:12px;opacity:.85">un</span><br>{B("médecin",MAG)}.</div>
<div style="margin-top:60px;font-weight:800;font-size:60px;color:{YEL}">Senza articolo!</div></div>'''+doors(False,True)+foot())
FR['06_prof_agg']=wrap(hud()+f'''<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div style="font-family:{PX};font-size:34px;color:{YEL}">MA SE AGGIUNGETE UN AGGETTIVO…</div>
<div style="margin-top:120px;font-weight:800;font-size:100px;line-height:1.15">{B("C'est",CY)} un<br><span style="color:{YEL}">excellent</span><br>médecin.</div>
<div style="margin-top:60px;font-weight:500;font-size:46px;color:rgba(255,255,255,.8)">È un ottimo medico.<br>L'articolo torna… e torna anche c'est!</div></div>'''+doors(True,False)+foot())
FR['07_giudizio']=wrap(hud()+screen('s_pontneuf.jpg','50% 50%',CY,230,520)+rule(3,"C'EST + AGG. MASCHILE",CY,800)+ex([("Paris, c'est "+B("beau",CY)+" !","Giudizio generale: l'esperienza di Parigi"),("La ville est "+B("belle",MAG)+".","Proprio la città: femminile")],990,64)+foot())
row=lambda w,c,t: f'<div style="display:flex;align-items:center;gap:30px;padding:30px 36px;border-radius:28px;background:rgba(18,8,46,.85);border:5px solid {c};box-shadow:0 0 30px {c}"><span style="min-width:300px;font-family:{PX};font-size:40px;color:{c}">{w}</span><span style="font-weight:800;font-size:50px;line-height:1.15">{t}</span></div>'
FR['08_riepilogo']=wrap(hud()+f'<div style="position:absolute;left:0;right:0;top:300px;text-align:center;font-family:{PX};font-size:48px;color:{YEL};text-shadow:0 0 20px rgba(255,210,63,.8)">RIEPILOGO</div><div style="position:absolute;left:60px;right:60px;top:450px;display:flex;flex-direction:column;gap:40px">'+row("C'EST",CY,"+ nome")+row("IL EST",MAG,"+ aggettivo<br>o professione")+row("C'EST",CY,"+ aggettivo maschile<br>(giudizio generale)")+'</div>'+foot())
FR['09_fine']=wrap(f'''<div style="position:absolute;left:0;right:0;top:200px;text-align:center"><div style="font-family:{PX};font-size:76px;line-height:1.4;color:{GRN};text-shadow:0 0 30px {GRN}">LIVELLO 6<br>SUPERATO!</div>
<div style="margin-top:90px;font-family:{PX};font-size:32px;color:{YEL}">TOCCA A VOI</div>
<div style="margin-top:40px;font-weight:800;font-size:92px;line-height:1.15">Le français,<br><span style="color:{YEL}">______</span><br>difficile ?</div>
<div style="margin-top:40px;font-weight:500;font-size:48px;color:rgba(255,255,255,.85)">C'est o il est? Rispondete nei commenti</div>
<div style="margin:80px auto 0;display:inline-block;padding:34px 50px;border-radius:30px;background:{MAG};color:#fff;font-family:{PX};font-size:36px;line-height:1.5;box-shadow:0 14px 0 #9A1E90,0 0 50px {MAG}">SEGUITEMI ▶<br>LIVELLO 7</div></div>
<div style="position:absolute;left:0;right:0;bottom:150px;display:flex;justify-content:center"><img src="logo.png" style="width:150px;height:150px;border-radius:50%;box-shadow:0 0 0 6px #fff"></div>{foot()}''')
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        for k,html in FR.items():
            open(D+k+'.html','w').write(html)
            await pg.goto(f'file://{D}{k}.html'); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=D+f'reel_livello6_{k}.png')
        await b.close()
asyncio.run(main())
from PIL import Image
ks=list(FR); W=Image.new('RGB',(len(ks)*250,444),'white')
for i,k in enumerate(ks): W.paste(Image.open(D+f'reel_livello6_{k}.png').convert('RGB').resize((250,444)),(i*250,0))
W.save('/home/claude/prev7.png')
