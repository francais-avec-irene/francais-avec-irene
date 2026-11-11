import asyncio
from playwright.async_api import async_playwright
D='/home/claude/render/'
F="'Bricolage Grotesque', system-ui, sans-serif"; PX="'Silkscreen', monospace"
PINK,ORA,CY,INK='#FF5FA2','#FFB86B','#7FE3FF','#1A0B3D'
HL="background: linear-gradient(90deg,#FF5FA2,#FFB86B); -webkit-background-clip: text; background-clip: text; color: transparent;"
def pill(t,c,rot,fs=44):
    col='#FFFFFF' if c==PINK else INK
    return f'<span style="display:inline-block;padding:18px 36px;border-radius:40px;background:{c};color:{col};font-family:{F};font-weight:800;font-size:{fs}px;transform:rotate({rot}deg);box-shadow:0 14px 30px rgba(0,0,0,.3)">{t}</span>'
def tag(t): return f'<span style="align-self:flex-start;padding:12px 26px;border-radius:12px;background:{ORA};color:{INK};font-family:{F};font-weight:800;font-size:32px;letter-spacing:3px;transform:rotate(-2deg)">{t}</span>'
def h(t,fs=96,extra=''): return f'<h2 style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.03;letter-spacing:-2px;color:#fff;{extra}">{t}</h2>'
def p(t,fs=40): return f'<p style="margin:0;font-family:{F};font-weight:500;font-size:{fs}px;line-height:1.3;color:rgba(255,255,255,.95)">{t}</p>'
hl=lambda t:f'<span style="{HL}">{t}</span>'
# (image, css for img box)
SL=[
 ('hd_trocadero.jpg','top:-330px;height:1700px;object-position:52% 50%',[tag('IN FRANCESE'),h('Come si dice<br>'+hl('«mi manchi»')+'?',104),'<div style="margin-top:6px">'+pill('Attenzione, è al contrario! ♥',PINK,-3)+'</div>'],'1/5 · scorri →'),
 ('p026.jpg','top:-80px;height:1500px;object-position:center 25%',[tag('LA FRASE GIUSTA'),h(hl('Tu me manques'),112),h('= mi manchi',60),p('Letteralmente: «tu manchi a me».<br>Il soggetto è la persona che manca!')],'2/5 · scorri →'),
 ('p_kiss.jpg','top:-40px;height:1500px;object-position:center 10%',[tag("L'ERRORE TIPICO"),h('Je te manque',112,f'color:rgba(255,255,255,.75);text-decoration:line-through;text-decoration-color:{PINK};text-decoration-thickness:11px'),'<div>'+pill('= ti manco (io a te!)',ORA,-2,48)+'</div>',p('Se lo dici pensando «mi manchi»,<br>stai dicendo il contrario.')],'3/5 · scorri →'),
 ('hd_danse.jpg','top:-720px;height:1700px;object-position:30% 50%',[tag('ALTRE FRASI'),h(hl('Il me manque'),92),'<div>'+pill('= mi manca (lui)',CY,-2)+'</div>',h(hl('Tu vas me manquer'),92),'<div>'+pill('= mi mancherai',ORA,2)+'</div>'],'4/5 · scorri →'),
 ('p042.jpg','top:-60px;height:1500px;object-position:center 25%',[h('Manda questo post<br>'+hl('a chi ti manca'),96),'<div style="margin-top:6px">'+pill('Tu me manques… ♥',PINK,-3,52)+'</div>'],'5/5'),
]
def page(img,css,parts,num):
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Silkscreen&display=swap">
<style>body{{margin:0}}</style></head><body>
<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background:#160936;color:#fff">
<img src="{img}" style="position:absolute;left:0;width:1080px;object-fit:cover;{css}">
<div style="position:absolute;inset:0;background:radial-gradient(circle at 92% 4%,rgba(255,95,162,.55),rgba(255,95,162,0) 30%),radial-gradient(circle at 4% 98%,rgba(255,184,107,.45),rgba(255,184,107,0) 28%),linear-gradient(180deg,rgba(40,10,110,.45) 0%,rgba(58,20,144,.18) 30%,rgba(50,16,130,.55) 55%,rgba(22,9,54,.93) 100%)"></div>
<div style="position:absolute;left:60px;right:60px;top:50px;display:flex;align-items:center;justify-content:space-between">
<img src="logo.png" style="width:150px;height:150px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 6px #fff,0 12px 30px rgba(0,0,0,.45)">
<span style="font-family:{PX};font-size:38px;letter-spacing:2px;color:{PINK};text-shadow:0 0 22px rgba(255,95,162,.9),0 2px 6px rgba(22,9,54,.8)">LEÇON D'AMOUR ♥</span></div>
<div style="position:absolute;left:46px;right:46px;bottom:126px;padding:50px 50px 56px;border-radius:48px;background:rgba(46,16,120,.5);border:2px solid rgba(255,255,255,.28);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);display:flex;flex-direction:column;gap:28px">{''.join(parts)}</div>
<div style="position:absolute;left:70px;right:70px;bottom:52px;display:flex;justify-content:space-between;font-family:{F};font-weight:500;font-size:36px;color:rgba(255,255,255,.92)"><span>Irene · Francese per italiani</span><span>{num}</span></div>
</div></body></html>'''
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,s in enumerate(SL,1):
            open(D+f's{i}.html','w').write(page(*s))
            await pg.goto(f'file://{D}s{i}.html'); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=D+f'mi_manchi_{i}.png')
        await b.close()
asyncio.run(main())
from PIL import Image
W=Image.new('RGB',(5*360,450))
for i in range(5): W.paste(Image.open(D+f'mi_manchi_{i+1}.png').convert('RGB').resize((360,450)),(i*360,0))
W.save('/home/claude/prev.png')
