import asyncio
from playwright.async_api import async_playwright
D='/home/claude/zod/'
F="'Bricolage Grotesque', system-ui, sans-serif"; PX="'Silkscreen', monospace"
LIME,MINT,YEL,INK='#C9A7FF','#FFCF5A','#FF7AC6','#120A2E'
HL=f"background: linear-gradient(90deg,{MINT},{YEL}); -webkit-background-clip: text; background-clip: text; color: transparent;"
hl=lambda t:f'<span style="{HL}">{t}</span>'
def pill(t,c,rot,fs=46): return f'<span style="display:inline-block;padding:18px 38px;border-radius:40px;background:{c};color:{INK};font-family:{F};font-weight:800;font-size:{fs}px;transform:rotate({rot}deg);box-shadow:0 14px 30px rgba(0,0,0,.35)">{t}</span>'
def h(t,fs=96): return f'<h2 style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.03;letter-spacing:-2px;color:#fff">{t}</h2>'
def num(t): return f'<span style="font-family:{PX};font-size:40px;color:{MINT};text-shadow:0 0 16px rgba(255,207,90,.8)">{t}</span>'
def eq(t,fs=58): return f'<p style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.1;color:#fff">= <span style="color:{YEL}">{t}</span></p>'
def quote(t): return f'<p style="margin:0;padding-left:30px;border-left:8px solid {MINT};font-family:{F};font-weight:500;font-size:40px;line-height:1.3;color:rgba(255,255,255,.93)">{t}</p>'
def p(t): return f'<p style="margin:0;font-family:{F};font-weight:500;font-size:40px;line-height:1.3;color:rgba(255,255,255,.93)">{t}</p>'
def pron(t): return f'<p style="margin:0;font-family:{F};font-weight:800;font-size:54px;color:#fff">si pronuncia <span style="color:{LIME}">[{t}]</span></p>'
def row(fr,pr,it): return f'<div style="display:flex;align-items:baseline;justify-content:space-between;gap:20px;padding:18px 0;border-bottom:2px solid rgba(255,255,255,.18)"><span style="font-family:{F};font-weight:800;font-size:64px;{HL}">{fr}</span><span style="font-family:{F};font-weight:800;font-size:42px;color:{LIME}">[{pr}]</span><span style="font-family:{F};font-weight:500;font-size:40px;color:rgba(255,255,255,.9)">= {it}</span></div>'
SL=[
 ('z_eiffel.jpg','top:-80px;height:1440px;object-position:50% 40%',[h('Di che segno siete?<br>In francese '+hl('non lo riconoscerete!'),82),f'<span style="align-self:flex-start;padding:14px 28px;border-radius:12px;background:{MINT};color:{INK};font-family:{F};font-weight:800;font-size:32px;letter-spacing:2px;transform:rotate(-2deg)">I SEGNI ZODIACALI IN FRANCESE</span>','<div style="display:flex;gap:22px;flex-wrap:wrap;margin-top:6px">'+pill('Bélier',YEL,-4)+pill('Verseau',LIME,3)+pill('Poissons',MINT,-2)+'</div>'],'1/7 · scorri →'),
 ('z_belier.jpg','top:0;height:1050px;object-position:45% 40%',[num("L'ARIETE"),h(hl('Bélier'),124),pron('belié'),quote('È il montone maschio. Niente a che vedere con «ariete»!')],'2/7 · scorri →'),
 ('z_alpes.jpg','top:0;height:1150px;object-position:50% 30%',[num('I GEMELLI'),h(hl('Gémeaux'),124),pron('jemò'),quote('È una parola antica: oggi «gemelli» si dice jumeaux!')],'3/7 · scorri →'),
 ('z_verseau.jpg','top:0;height:1100px;object-position:50% 40%',[num("L'ACQUARIO"),h(hl('Verseau'),124),pron('versò'),quote("Viene da verser + eau: «quello che versa l'acqua».")],'4/7 · scorri →'),
 ('z_poissons.jpg','top:0;height:1100px;object-position:40% 40%',[num('I PESCI'),h(hl('Poissons'),124),pron('puassòn'),quote('Sempre con la S! E attenzione: poison, con una S sola, è il veleno.')],'5/7 · scorri →'),
 ('z_taureau.jpg','top:0;height:1000px;object-position:45% 50%',[num('ATTENZIONE ALLA PRONUNCIA'),'<div>'+row('Taureau','torò','Toro')+row('Vierge','vièrj','Vergine')+row('Balance','balàns','Bilancia')+'</div>'],'6/7 · scorri →'),
]
SIGNS=[('Bélier','Ariete',1),('Taureau','Toro',0),('Gémeaux','Gemelli',1),('Cancer','Cancro',0),('Lion','Leone',0),('Vierge','Vergine',0),('Balance','Bilancia',0),('Scorpion','Scorpione',0),('Sagittaire','Sagittario',0),('Capricorne','Capricorno',0),('Verseau','Acquario',1),('Poissons','Pesci',1)]
def lista():
    cells=''.join(f'<div style="padding:16px 22px;border-radius:20px;background:{"rgba(255,122,198,.22)" if d else "rgba(255,255,255,.07)"};border:2px solid {YEL if d else "rgba(255,255,255,.15)"}"><div style="font-family:{F};font-weight:800;font-size:46px;color:{"#fff" if not d else YEL}">{fr}</div><div style="font-family:{F};font-weight:500;font-size:32px;color:rgba(255,255,255,.8)">{it}</div></div>' for fr,it,d in SIGNS)
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Silkscreen&display=swap">
<style>body{{margin:0}}</style></head><body>
<div style="position:relative;width:1080px;height:1350px;overflow:hidden;color:#fff;background:radial-gradient(circle at 85% 8%,rgba(255,207,90,.35),rgba(255,207,90,0) 30%),radial-gradient(circle at 8% 95%,rgba(255,122,198,.35),rgba(255,122,198,0) 30%),linear-gradient(180deg,#1B1150 0%,#0B0A2E 100%)">
<div style="position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.8) 1.6px,transparent 1.6px),radial-gradient(rgba(255,207,90,.7) 1.2px,transparent 1.2px);background-size:80px 80px,130px 130px;background-position:0 0,40px 60px;opacity:.5"></div>
<div style="position:absolute;left:60px;right:60px;top:50px;display:flex;align-items:center;justify-content:space-between">
<img src="logo.png" style="width:150px;height:150px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 6px #fff,0 12px 30px rgba(0,0,0,.45)">
<span style="font-family:{PX};font-size:38px;letter-spacing:2px;color:{MINT};text-shadow:0 0 20px rgba(255,207,90,.9)">OROSCOPO IN FRANCESE</span></div>
<div style="position:absolute;left:60px;right:60px;top:240px"><h2 style="margin:0 0 26px;font-family:{F};font-weight:800;font-size:72px;letter-spacing:-1px">Tutti i <span style="{HL}">segni</span></h2>
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px">{cells}</div>
<div style="margin-top:34px;text-align:center">{pill("Di che segno siete? Scrivetelo in francese!",YEL,-2,40)}</div></div>
<div style="position:absolute;left:70px;right:70px;bottom:44px;height:70px;display:flex;align-items:center;justify-content:space-between;font-family:{F};font-weight:500;font-size:36px;color:rgba(255,255,255,.92)"><span>Irene · Francese per italiani</span><span style="padding:14px 34px;border-radius:40px;background:{MINT};color:{INK};font-weight:800">Salva ★</span></div>
</div></body></html>'''
def page(img,css,parts,n):
    right = f'<span>{n}</span>' if n else f'<span style="padding:14px 34px;border-radius:40px;background:{MINT};color:{INK};font-weight:800">Salva ★</span>'
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Silkscreen&display=swap">
<style>body{{margin:0}}</style></head><body>
<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background:#0B0A2E;color:#fff">
<img src="{img}" style="position:absolute;left:0;width:1080px;object-fit:cover;{css}">
<div style="position:absolute;inset:0;background:radial-gradient(circle at 92% 4%,rgba(255,207,90,.4),rgba(255,207,90,0) 28%),radial-gradient(circle at 4% 98%,rgba(255,122,198,.4),rgba(255,122,198,0) 28%),linear-gradient(180deg,rgba(27,17,80,.35) 0%,rgba(27,17,80,0) 22%,rgba(27,17,80,.3) 48%,rgba(11,10,46,.96) 92%)"></div>
<div style="position:absolute;left:60px;right:60px;top:50px;display:flex;align-items:center;justify-content:space-between">
<img src="logo.png" style="width:150px;height:150px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 6px #fff,0 12px 30px rgba(0,0,0,.45)">
<span style="font-family:{PX};font-size:38px;letter-spacing:2px;color:{MINT};text-shadow:0 0 20px rgba(255,207,90,.9),0 2px 6px rgba(0,0,0,.8),0 2px 6px rgba(3,34,22,.9)">OROSCOPO IN FRANCESE</span></div>
<div style="position:absolute;left:46px;right:46px;bottom:126px;padding:50px 50px 56px;border-radius:48px;background:rgba(40,22,110,.55);border:2px solid rgba(255,255,255,.28);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);display:flex;flex-direction:column;gap:26px">{''.join(parts)}</div>
<div style="position:absolute;left:70px;right:70px;bottom:44px;height:70px;display:flex;align-items:center;justify-content:space-between;font-family:{F};font-weight:500;font-size:36px;color:rgba(255,255,255,.92)"><span>Irene · Francese per italiani</span>{right}</div>
</div></body></html>'''
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,s in enumerate(SL,1):
            open(D+f'zod{i}.html','w').write(page(*s))
            await pg.goto(f'file://{D}zod{i}.html'); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=D+f'segni_zodiacali_{i}.png')
        open(D+'zod7.html','w').write(lista()); await pg.goto(f'file://{D}zod7.html'); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400); await pg.screenshot(path=D+'segni_zodiacali_7.png')
        await b.close()
asyncio.run(main())
from PIL import Image
W=Image.new('RGB',(7*300,375))
for i in range(7): W.paste(Image.open(D+f'segni_zodiacali_{i+1}.png').convert('RGB').resize((300,375)),(i*300,0))
W.save('/home/claude/prev2.png')
