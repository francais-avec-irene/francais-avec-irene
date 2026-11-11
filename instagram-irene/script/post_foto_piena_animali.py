import asyncio
from playwright.async_api import async_playwright
D='/home/claude/render/'
F="'Bricolage Grotesque', system-ui, sans-serif"; PX="'Silkscreen', monospace"
LIME,MINT,YEL,INK='#E5FF3D','#3DFFB0','#FFD23F','#062A1D'
HL=f"background: linear-gradient(90deg,{LIME},{MINT}); -webkit-background-clip: text; background-clip: text; color: transparent;"
hl=lambda t:f'<span style="{HL}">{t}</span>'
def pill(t,c,rot,fs=46): return f'<span style="display:inline-block;padding:18px 38px;border-radius:40px;background:{c};color:{INK};font-family:{F};font-weight:800;font-size:{fs}px;transform:rotate({rot}deg);box-shadow:0 14px 30px rgba(0,0,0,.35)">{t}</span>'
def h(t,fs=96): return f'<h2 style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.03;letter-spacing:-2px;color:#fff">{t}</h2>'
def num(t): return f'<span style="font-family:{PX};font-size:44px;color:{LIME};text-shadow:0 0 16px rgba(229,255,61,.8)">{t}</span>'
def eq(t,fs=58): return f'<p style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.1;color:#fff">= <span style="color:{YEL}">{t}</span></p>'
def quote(t): return f'<p style="margin:0;padding-left:30px;border-left:8px solid {MINT};font-family:{F};font-weight:500;font-size:40px;line-height:1.3;color:rgba(255,255,255,.93)">{t}</p>'
def p(t): return f'<p style="margin:0;font-family:{F};font-weight:500;font-size:40px;line-height:1.3;color:rgba(255,255,255,.93)">{t}</p>'
SL=[
 ('a_coq.jpg','top:0;height:820px;object-position:40% 50%',[h('5 espressioni<br>'+hl('francesi')+' con<br>gli animali',96),f'<span style="align-self:flex-start;padding:14px 28px;border-radius:12px;background:{MINT};color:{INK};font-family:{F};font-weight:800;font-size:32px;letter-spacing:2px;transform:rotate(-2deg)">CHE FANNO RIDERE GLI ITALIANI</span>','<div style="display:flex;gap:24px;flex-wrap:wrap;margin-top:8px">'+pill('le chat',LIME,-4)+pill('le lapin',MINT,3)+pill('la poule',YEL,-2)+'</div>'],'1/7 · scorri →'),
 ('a_chat.jpg','top:-40px;height:1707px;object-position:center 20%',[num('1/5'),h(hl('Avoir un chat<br>dans la gorge'),96),eq('avere la raucedine'),quote('Letteralmente: «avere un gatto in gola».')],'2/7 · scorri →'),
 ('a_lapin.jpg','top:-330px;height:1620px;object-position:62% 50%',[num('2/5'),h(hl('Poser un lapin'),104),eq('dare buca'),quote('Letteralmente: «posare un coniglio».')],'3/7 · scorri →'),
 ('a_canard.jpg','top:0;height:1350px;object-position:22% 30%',[num('3/5'),h(hl('Il fait un froid<br>de canard'),96),eq('fa un freddo cane'),quote('Letteralmente: «un freddo da anatra».')],'4/7 · scorri →'),
 ('a_poule.jpg','top:-30px;height:1600px;object-position:12% 30%',[num('4/5'),h(hl('Quand les poules<br>auront des dents'),84),eq('quando gli asini voleranno',52),quote('Letteralmente: «quando le galline avranno i denti».')],'5/7 · scorri →'),
 ('a_poule2.jpg','top:-380px;height:1650px;object-position:62% 50%',[num('5/5'),h(hl('Avoir la chair<br>de poule'),96),eq('avere la pelle d\'oca'),quote('Qui francesi e italiani sono d\'accordo… quasi: è una gallina!')],'6/7 · scorri →'),
 ('a_gens.jpg','top:-60px;height:1440px;object-position:center 30%',[h('Qual è la tua<br>'+hl('preferita')+'?',104),'<div style="margin-top:4px">'+pill('Scrivilo nei commenti!',YEL,-3,48)+'</div>',p('Salva il post per usarle al momento giusto.')],None),
]
def page(img,css,parts,n):
    right = f'<span>{n}</span>' if n else f'<span style="padding:14px 34px;border-radius:40px;background:{LIME};color:{INK};font-weight:800">Salva ★</span>'
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Silkscreen&display=swap">
<style>body{{margin:0}}</style></head><body>
<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background:#04261A;color:#fff">
<img src="{img}" style="position:absolute;left:0;width:1080px;object-fit:cover;{css}">
<div style="position:absolute;inset:0;background:radial-gradient(circle at 92% 4%,rgba(229,255,61,.45),rgba(229,255,61,0) 28%),radial-gradient(circle at 4% 98%,rgba(61,255,176,.4),rgba(61,255,176,0) 28%),linear-gradient(180deg,rgba(4,60,40,.45) 0%,rgba(10,90,60,.15) 30%,rgba(6,70,46,.55) 55%,rgba(3,34,22,.94) 100%)"></div>
<div style="position:absolute;left:60px;right:60px;top:50px;display:flex;align-items:center;justify-content:space-between">
<img src="logo.png" style="width:150px;height:150px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 6px #fff,0 12px 30px rgba(0,0,0,.45)">
<span style="font-family:{PX};font-size:38px;letter-spacing:2px;color:{LIME};text-shadow:0 0 20px rgba(229,255,61,.9),0 2px 6px rgba(3,34,22,.9)">ESPRESSIONI BUFFE</span></div>
<div style="position:absolute;left:46px;right:46px;bottom:126px;padding:50px 50px 56px;border-radius:48px;background:rgba(6,70,46,.5);border:2px solid rgba(255,255,255,.28);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);display:flex;flex-direction:column;gap:26px">{''.join(parts)}</div>
<div style="position:absolute;left:70px;right:70px;bottom:44px;height:70px;display:flex;align-items:center;justify-content:space-between;font-family:{F};font-weight:500;font-size:36px;color:rgba(255,255,255,.92)"><span>Irene · Francese per italiani</span>{right}</div>
</div></body></html>'''
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,s in enumerate(SL,1):
            open(D+f'an{i}.html','w').write(page(*s))
            await pg.goto(f'file://{D}an{i}.html'); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=D+f'espressioni_animali_{i}.png')
        await b.close()
asyncio.run(main())
from PIL import Image
W=Image.new('RGB',(7*300,375))
for i in range(7): W.paste(Image.open(D+f'espressioni_animali_{i+1}.png').convert('RGB').resize((300,375)),(i*300,0))
W.save('/home/claude/prev2.png')
