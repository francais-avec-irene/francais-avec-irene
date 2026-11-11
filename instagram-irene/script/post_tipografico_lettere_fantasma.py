import asyncio
from playwright.async_api import async_playwright
D='/home/claude/lun/'
F="'Bricolage Grotesque', system-ui, sans-serif"; PX="'Silkscreen', monospace"
PINK,CY,INK,BG='#FF3D9A','#7FE8FF','#0D0B12','#0D0B12'
def g(t): return f'<span style="color:rgba(255,61,154,.38);text-shadow:0 0 24px rgba(255,61,154,.7)">{t}</span>'
def w(word,pr,fs=88): return f'<div style="display:flex;align-items:baseline;justify-content:space-between;padding:14px 0;border-bottom:2px solid rgba(255,255,255,.1)"><span style="font-family:{F};font-weight:800;font-size:{fs}px;letter-spacing:-1px">{word}</span><span style="font-family:{F};font-weight:500;font-size:46px;color:{CY}">[{pr}]</span></div>'
def frame(inner,n,label='A1 · PRONUNCIA'):
    right = f'<span>{n}</span>' if n else f'<span style="padding:14px 34px;border-radius:40px;background:{PINK};color:#fff;font-weight:800">Salva ★</span>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Silkscreen&display=swap"><style>body{{margin:0}}</style></head><body>
<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background:radial-gradient(circle at 85% 12%,rgba(255,61,154,.28),rgba(255,61,154,0) 35%),radial-gradient(circle at 10% 90%,rgba(127,232,255,.16),rgba(127,232,255,0) 35%),{BG};color:#fff;font-family:{F}">
<div style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.035) 2px,transparent 2px);background-size:90px 90px"></div>
<div style="position:absolute;left:60px;right:60px;top:50px;display:flex;align-items:center;justify-content:space-between">
<img src="logo.png" style="width:140px;height:140px;border-radius:50%;box-shadow:0 0 0 6px #fff,0 0 40px rgba(255,61,154,.5)">
<span style="font-family:{PX};font-size:34px;letter-spacing:2px;color:{PINK};text-shadow:0 0 18px rgba(255,61,154,.9)">{label}</span></div>
{inner}
<div style="position:absolute;left:70px;right:70px;bottom:44px;height:70px;display:flex;align-items:center;justify-content:space-between;font-weight:500;font-size:36px;color:rgba(255,255,255,.85)"><span>Irene · Francese per italiani</span>{right}</div>
</div></body></html>'''
def box(inner,top=260): return f'<div style="position:absolute;left:70px;right:70px;top:{top}px;display:flex;flex-direction:column;gap:26px">{inner}</div>'
def h(t,fs=72): return f'<h2 style="margin:0;font-weight:800;font-size:{fs}px;line-height:1.08;letter-spacing:-1px">{t}</h2>'
def p(t,fs=42): return f'<p style="margin:0;font-weight:500;font-size:{fs}px;line-height:1.35;color:rgba(255,255,255,.88)">{t}</p>'
S=[]
S.append(frame(f'''<div style="position:absolute;left:0;right:0;top:250px;text-align:center;font-weight:800;font-size:330px;line-height:1;letter-spacing:-10px">PARI{g('S')}</div>
<div style="position:absolute;left:70px;right:70px;top:640px;display:flex;flex-direction:column;gap:30px">{h('Le lettere <span style="color:'+PINK+';text-shadow:0 0 30px rgba(255,61,154,.8)">fantasma</span>',110)}
{p('Perché « Paris » non si legge <b style="color:#fff">Pa-ris</b>?',50)}
<span style="align-self:flex-start;padding:14px 28px;border-radius:12px;background:{CY};color:{INK};font-weight:800;font-size:32px;letter-spacing:2px;transform:rotate(-2deg)">LA REGOLA + IL TRUCCO CaReFuL</span></div>''','1/6 · scorri →'))
S.append(frame(box(h('In francese la consonante finale <span style="color:'+PINK+'">di solito non si pronuncia.</span>',66)+'<div style="margin-top:10px">'+w('Pari'+g('s'),'parì')+w('peti'+g('t'),'petì')+w('gran'+g('d'),'gràn')+w('beaucou'+g('p'),'bocù')+w('vou'+g('s'),'vu')+'</div>'),'2/6 · scorri →'))
S.append(frame(box(h('La <span style="color:'+PINK+'">-e</span> finale è muta…',80)+p('… ma fa sentire la consonante che sta prima. Ecco come si sente il femminile!',46)+f'''<div style="margin-top:30px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px">
<div style="padding:30px;border-radius:30px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.15)"><div style="font-weight:800;font-size:80px">peti{g('t')}</div><div style="font-size:46px;color:{CY}">[petì]</div></div>
<div style="padding:30px;border-radius:30px;background:rgba(255,61,154,.14);border:3px solid {PINK}"><div style="font-weight:800;font-size:80px">petit{g('e')}</div><div style="font-size:46px;color:{CY}">[petìt]</div></div>
<div style="padding:30px;border-radius:30px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.15)"><div style="font-weight:800;font-size:80px">gran{g('d')}</div><div style="font-size:46px;color:{CY}">[gràn]</div></div>
<div style="padding:30px;border-radius:30px;background:rgba(255,61,154,.14);border:3px solid {PINK}"><div style="font-weight:800;font-size:80px">grand{g('e')}</div><div style="font-size:46px;color:{CY}">[grànd]</div></div></div>'''),'3/6 · scorri →'))
L=lambda c: f'<span style="color:{CY};text-shadow:0 0 26px rgba(127,232,255,.9)">{c}</span>'
S.append(frame(f'''<div style="position:absolute;left:0;right:0;top:250px;text-align:center"><div style="font-family:{PX};font-size:40px;color:{CY}">IL TRUCCO</div>
<div style="font-weight:800;font-size:200px;letter-spacing:-4px;line-height:1.1">{L('C')}a{L('R')}e{L('F')}u{L('L')}</div>
<p style="margin:10px 90px 0;font-weight:500;font-size:46px;line-height:1.35;color:rgba(255,255,255,.88)">C, R, F, L alla fine di una parola <b style="color:#fff">di solito si pronunciano</b>.</p></div>
<div style="position:absolute;left:70px;right:70px;top:820px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px">
{''.join(f'<div style="padding:26px 30px;border-radius:26px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.15);font-weight:800;font-size:70px">{a}{L(b)}</div>' for a,b in [('un sa','c'),('bonjou','r'),('neu','f'),('avri','l')])}</div>''','4/6 · scorri →'))
S.append(frame(box(f'<span style="font-family:{PX};font-size:40px;color:{CY}">ATTENZIONE!</span>'+h('Nei verbi in <span style="color:'+PINK+'">-ER</span> la R è un fantasma.',76)+'<div>'+w('parle'+g('r'),'parlé')+w('mange'+g('r'),'manjé')+w('le dîne'+g('r'),'diné')+'</div>'+p('E qualche eccezione da sapere: le taba'+g('c')+' [tabà] · la cle'+g('f')+' [clé]',44)),'5/6 · scorri →'))
S.append(frame(box(f'<span style="font-family:{PX};font-size:40px;color:{CY}">MINI-TEST</span>'+h('Come si legge?',100)+f'<div style="padding:44px 40px;border-radius:36px;background:rgba(255,61,154,.12);border:3px solid {PINK};font-weight:800;font-size:76px;line-height:1.2">J\'ai un grand sac et un petit chat.</div>'+p('Scrivete nei commenti le lettere che <b style="color:#fff">NON</b> si pronunciano ↓',46),300),None))
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,html in enumerate(S,1):
            open(D+f'l{i}.html','w').write(html)
            await pg.goto(f'file://{D}l{i}.html'); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=D+f'lettere_fantasma_{i}.png')
        await b.close()
asyncio.run(main())
from PIL import Image
W=Image.new('RGB',(6*300,375))
for i in range(6): W.paste(Image.open(D+f'lettere_fantasma_{i+1}.png').convert('RGB').resize((300,375)),(i*300,0))
W.save('/home/claude/prev5.png')
