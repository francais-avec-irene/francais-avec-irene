import asyncio
from playwright.async_api import async_playwright
D='/home/claude/brin/'
F="'Bricolage Grotesque', system-ui, sans-serif"; PX="'Silkscreen', monospace"
LIME,MINT,YEL,INK='#FFD6E8','#FF7A3D','#FFD23F','#2A0620'
HL=f"background: linear-gradient(90deg,{YEL},{MINT}); -webkit-background-clip: text; background-clip: text; color: transparent;"
hl=lambda t:f'<span style="{HL}">{t}</span>'
def pill(t,c,rot,fs=46): return f'<span style="display:inline-block;padding:18px 38px;border-radius:40px;background:{c};color:{INK};font-family:{F};font-weight:800;font-size:{fs}px;transform:rotate({rot}deg);box-shadow:0 14px 30px rgba(0,0,0,.35)">{t}</span>'
def h(t,fs=96): return f'<h2 style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.03;letter-spacing:-2px;color:#fff">{t}</h2>'
def num(t): return f'<span style="font-family:{PX};font-size:44px;color:{YEL};text-shadow:0 0 16px rgba(255,210,63,.8)">{t}</span>'
def eq(t,fs=58): return f'<p style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.1;color:#fff">= <span style="color:{LIME}">{t}</span></p>'
def quote(t): return f'<p style="margin:0;padding-left:30px;border-left:8px solid {MINT};font-family:{F};font-weight:500;font-size:40px;line-height:1.3;color:rgba(255,255,255,.93)">{t}</p>'
def p(t): return f'<p style="margin:0;font-family:{F};font-weight:500;font-size:40px;line-height:1.3;color:rgba(255,255,255,.93)">{t}</p>'
SL=[
 ('k_coupe3.jpg','top:0;height:900px;object-position:55% 40%',[h('Come si brinda<br>'+hl('in francese')+'?',100),f'<span style="align-self:flex-start;padding:14px 28px;border-radius:12px;background:{MINT};color:{INK};font-family:{F};font-weight:800;font-size:32px;letter-spacing:2px;transform:rotate(-2deg)">5 FRASI PER LA FESTA</span>','<div style="display:flex;gap:22px;flex-wrap:wrap;margin-top:6px">'+pill('Santé !',YEL,-4)+pill('Tchin-tchin !',MINT,3)+pill('À nous !',LIME,-2)+'</div>'],'1/7 · scorri →'),
 ('k_coupe1.jpg','top:0;height:950px;object-position:40% 40%',[num('1/5'),h(hl('Santé !'),130),eq('salute!'),quote('Il brindisi più comune.')],'2/7 · scorri →'),
 ('k_festival.jpg','top:-60px;height:1250px;object-position:50% 40%',[num('2/5'),h(hl('Tchin-tchin !'),118),eq('cin cin!'),quote('Come in italiano, ma si scrive così.')],'3/7 · scorri →'),
 ('k_parisdiner.jpg','top:0;height:1000px;object-position:58% 40%',[num('3/5'),h(hl('À la tienne !'),118),eq('alla tua!'),quote('A una persona a cui dai del tu.')],'4/7 · scorri →'),
 ('k_vignes.jpg','top:0;height:1050px;object-position:40% 50%',[num('4/5'),h(hl('À la vôtre !'),118),eq('alla vostra! / alla Sua!',52),quote('A un gruppo, o a chi dai del Lei.')],'5/7 · scorri →'),
 ('k_bastille.jpg','top:0;height:1050px;object-position:45% 35%',[num('5/5'),h(hl('À nous !'),130),eq('a noi!'),quote('Per brindare tutti insieme.')],'6/7 · scorri →'),
 ('k_wine2.jpg','top:0;height:950px;object-position:60% 50%',[h('Il segreto<br>francese:',100),f'<p style="margin:0;font-family:{F};font-weight:800;font-style:italic;font-size:60px;line-height:1.15;color:{LIME};transform:rotate(-2deg)">quando brindi,<br>guarda negli occhi! ♥</p>',p('Manda questo post a chi festeggerà con te ★')],None),
]
def page(img,css,parts,n):
    right = f'<span>{n}</span>' if n else f'<span style="padding:14px 34px;border-radius:40px;background:{YEL};color:{INK};font-weight:800">Salva ★</span>'
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Silkscreen&display=swap">
<style>body{{margin:0}}</style></head><body>
<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background:#2A0620;color:#fff">
<img src="{img}" style="position:absolute;left:0;width:1080px;object-fit:cover;{css}">
<div style="position:absolute;inset:0;background:radial-gradient(circle at 92% 4%,rgba(255,200,80,.5),rgba(255,200,80,0) 28%),radial-gradient(circle at 4% 98%,rgba(255,122,61,.5),rgba(255,122,61,0) 28%),linear-gradient(180deg,rgba(214,40,118,.35) 0%,rgba(214,40,118,0) 22%,rgba(180,30,100,.35) 48%,rgba(50,6,36,.96) 92%)"></div>
<div style="position:absolute;left:60px;right:60px;top:50px;display:flex;align-items:center;justify-content:space-between">
<img src="logo.png" style="width:150px;height:150px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 6px #fff,0 12px 30px rgba(0,0,0,.45)">
<span style="font-family:{PX};font-size:38px;letter-spacing:2px;color:{YEL};text-shadow:0 0 20px rgba(255,210,63,.9),0 2px 6px rgba(0,0,0,.8),0 2px 6px rgba(3,34,22,.9)">BRINDISI ★</span></div>
<div style="position:absolute;left:46px;right:46px;bottom:126px;padding:50px 50px 56px;border-radius:48px;background:rgba(170,30,100,.5);border:2px solid rgba(255,255,255,.28);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);display:flex;flex-direction:column;gap:26px">{''.join(parts)}</div>
<div style="position:absolute;left:70px;right:70px;bottom:44px;height:70px;display:flex;align-items:center;justify-content:space-between;font-family:{F};font-weight:500;font-size:36px;color:rgba(255,255,255,.92)"><span>Irene · Francese per italiani</span>{right}</div>
</div></body></html>'''
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,s in enumerate(SL,1):
            open(D+f'brin{i}.html','w').write(page(*s))
            await pg.goto(f'file://{D}brin{i}.html'); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=D+f'brindisi_{i}.png')
        await b.close()
asyncio.run(main())
from PIL import Image
W=Image.new('RGB',(7*300,375))
for i in range(7): W.paste(Image.open(D+f'brindisi_{i+1}.png').convert('RGB').resize((300,375)),(i*300,0))
W.save('/home/claude/prev2.png')
