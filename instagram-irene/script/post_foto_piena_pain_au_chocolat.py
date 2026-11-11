import asyncio
from playwright.async_api import async_playwright
D='/home/claude/pac/'
F="'Bricolage Grotesque', system-ui, sans-serif"; PX="'Silkscreen', monospace"
LIME,MINT,YEL,INK='#B8FF3D','#3FF0FF','#FFD93D','#06123A'
HL=f"background: linear-gradient(90deg,{MINT},{LIME}); -webkit-background-clip: text; background-clip: text; color: transparent;"
hl=lambda t:f'<span style="{HL}">{t}</span>'
def pill(t,c,rot,fs=46): return f'<span style="display:inline-block;padding:18px 38px;border-radius:40px;background:{c};color:{INK};font-family:{F};font-weight:800;font-size:{fs}px;transform:rotate({rot}deg);box-shadow:0 14px 30px rgba(0,0,0,.35)">{t}</span>'
def h(t,fs=96): return f'<h2 style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.03;letter-spacing:-2px;color:#fff">{t}</h2>'
def num(t): return f'<span style="font-family:{PX};font-size:44px;color:{MINT};text-shadow:0 0 16px rgba(63,240,255,.8)">{t}</span>'
def eq(t,fs=58): return f'<p style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.1;color:#fff">= <span style="color:{YEL}">{t}</span></p>'
def quote(t): return f'<p style="margin:0;padding-left:30px;border-left:8px solid {MINT};font-family:{F};font-weight:500;font-size:40px;line-height:1.3;color:rgba(255,255,255,.93)">{t}</p>'
def p(t): return f'<p style="margin:0;font-family:{F};font-weight:500;font-size:40px;line-height:1.3;color:rgba(255,255,255,.93)">{t}</p>'
def opt(l,t,c): return f'<div style="display:flex;align-items:center;gap:28px;padding:26px 34px;border-radius:30px;background:{c};color:{INK};box-shadow:0 12px 26px rgba(0,0,0,.3)"><span style="width:84px;height:84px;border-radius:50%;background:rgba(6,18,58,.18);display:flex;align-items:center;justify-content:center;font-family:{PX};font-size:40px">{l}</span><span style="font-family:{F};font-weight:800;font-size:66px;line-height:1">{t}</span></div>'
SL=[
 ('c_tray.jpg','top:-40px;height:900px;object-position:40% 55%',[h('In francese si dice<br>'+hl('pain au chocolat')+'<br>o '+hl('chocolatine')+'?',84),f'<span style="align-self:flex-start;padding:14px 28px;border-radius:12px;background:{LIME};color:{INK};font-family:{F};font-weight:800;font-size:32px;letter-spacing:2px;transform:rotate(-2deg)">LA DOMANDA CHE DIVIDE LA FRANCIA</span>','<div style="margin-top:6px">'+pill('A ou B ?',YEL,-3)+'</div>'],'1/5 · scorri →'),
 ('p_rosiers.jpg','top:0;height:1100px;object-position:60% 40%',[num('A PARIGI E AL NORD'),h(hl('Pain au chocolat'),100),eq('il cornetto al cioccolato',54),quote('È la parola che trovi nella maggior parte delle boulangeries.')],'2/5 · scorri →'),
 ('b_miroir.jpg','top:0;height:1150px;object-position:50% 50%',[num('NEL SUD-OVEST'),h(hl('Chocolatine'),112),eq('la stessa cosa!'),quote('A Bordeaux e Tolosa, se dici «pain au chocolat», ti guardano storto.')],'3/5 · scorri →'),
 ('be_gp2.jpg','top:0;height:1150px;object-position:50% 50%',[num('E IN BELGIO?'),h(hl('Couque au<br>chocolat'),104),quote('Tre nomi per un solo dolce. I francesi ci litigano davvero!')],'4/5 · scorri →'),
 ('c_viatour.jpg','top:-120px;height:950px;object-position:50% 50%',[h('E tu da che<br>parte stai?',100),opt('A','Pain au chocolat',MINT),opt('B','Chocolatine',LIME),p('Vota nei commenti: A o B?')],None),
]
def page(img,css,parts,n):
    right = f'<span>{n}</span>' if n else f'<span style="padding:14px 34px;border-radius:40px;background:{MINT};color:{INK};font-weight:800">Salva ★</span>'
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Silkscreen&display=swap">
<style>body{{margin:0}}</style></head><body>
<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background:#06123A;color:#fff">
<img src="{img}" style="position:absolute;left:0;width:1080px;object-fit:cover;{css}">
<div style="position:absolute;inset:0;background:radial-gradient(circle at 92% 4%,rgba(63,240,255,.45),rgba(63,240,255,0) 28%),radial-gradient(circle at 4% 98%,rgba(184,255,61,.4),rgba(184,255,61,0) 28%),linear-gradient(180deg,rgba(8,40,140,.30) 0%,rgba(20,80,220,0) 22%,rgba(10,50,160,.25) 48%,rgba(6,18,58,.95) 92%)"></div>
<div style="position:absolute;left:60px;right:60px;top:50px;display:flex;align-items:center;justify-content:space-between">
<img src="logo.png" style="width:150px;height:150px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 6px #fff,0 12px 30px rgba(0,0,0,.45)">
<span style="font-family:{PX};font-size:38px;letter-spacing:2px;color:{MINT};text-shadow:0 0 20px rgba(63,240,255,.9),0 2px 6px rgba(3,34,22,.9)">IL GRANDE DIBATTITO</span></div>
<div style="position:absolute;left:46px;right:46px;bottom:126px;padding:50px 50px 56px;border-radius:48px;background:rgba(12,50,160,.5);border:2px solid rgba(255,255,255,.28);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);display:flex;flex-direction:column;gap:26px">{''.join(parts)}</div>
<div style="position:absolute;left:70px;right:70px;bottom:44px;height:70px;display:flex;align-items:center;justify-content:space-between;font-family:{F};font-weight:500;font-size:36px;color:rgba(255,255,255,.92)"><span>Irene · Francese per italiani</span>{right}</div>
</div></body></html>'''
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,s in enumerate(SL,1):
            open(D+f'pac{i}.html','w').write(page(*s))
            await pg.goto(f'file://{D}pac{i}.html'); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=D+f'pain_au_chocolat_{i}.png')
        await b.close()
asyncio.run(main())
from PIL import Image
W=Image.new('RGB',(5*300,375))
for i in range(5): W.paste(Image.open(D+f'pain_au_chocolat_{i+1}.png').convert('RGB').resize((300,375)),(i*300,0))
W.save('/home/claude/prev2.png')
