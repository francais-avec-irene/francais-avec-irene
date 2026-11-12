import asyncio, sys, json
from playwright.async_api import async_playwright
D='/home/claude/w/ph/'; O='/home/claude/w/out/'
F="'Bricolage Grotesque', system-ui, sans-serif"; PX="'Silkscreen', monospace"

def kit(P):
    A1,A2,A3,INK=P['a1'],P['a2'],P['a3'],P['ink']
    HL=f"background:linear-gradient(90deg,{A1},{A2});-webkit-background-clip:text;background-clip:text;color:transparent;"
    k={}
    k['hl']=lambda t:f'<span style="{HL}">{t}</span>'
    k['c']=lambda t,col=None:f'<span style="color:{col or A1}">{t}</span>'
    k['pill']=lambda t,c,rot=0,fs=44:f'<span style="display:inline-block;padding:16px 34px;border-radius:40px;background:{c};color:{INK};font-family:{F};font-weight:800;font-size:{fs}px;transform:rotate({rot}deg);box-shadow:0 12px 26px rgba(0,0,0,.3)">{t}</span>'
    k['pills']=lambda *ps:'<div style="display:flex;gap:20px;flex-wrap:wrap;align-items:center">'+''.join(ps)+'</div>'
    k['tag']=lambda t,c=None:f'<span style="align-self:flex-start;padding:12px 26px;border-radius:12px;background:{c or A2};color:{INK};font-family:{F};font-weight:800;font-size:30px;letter-spacing:2px;transform:rotate(-2deg)">{t}</span>'
    k['h']=lambda t,fs=92:f'<h2 style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.04;letter-spacing:-2px;color:#fff">{t}</h2>'
    k['num']=lambda t:f'<span style="font-family:{PX};font-size:40px;color:{A1};text-shadow:0 0 14px {A1}aa">{t}</span>'
    k['p']=lambda t,fs=38:f'<p style="margin:0;font-family:{F};font-weight:500;font-size:{fs}px;line-height:1.3;color:rgba(255,255,255,.94)">{t}</p>'
    k['ex']=lambda fr,it=None,fs=44:f'<div style="padding-left:28px;border-left:8px solid {A2}"><p style="margin:0;font-family:{F};font-weight:800;font-size:{fs}px;line-height:1.2;color:#fff">{fr}</p>'+(f'<p style="margin:6px 0 0;font-family:{F};font-weight:500;font-style:italic;font-size:32px;color:rgba(255,255,255,.8)">{it}</p>' if it else '')+'</div>'
    k['row']=lambda a,b:f'<div style="display:flex;gap:22px;align-items:baseline"><span style="flex:0 0 auto;min-width:96px;font-family:{PX};font-size:34px;color:{A1}">{a}</span><span style="font-family:{F};font-weight:800;font-size:42px;color:#fff;line-height:1.15">{b}</span></div>'
    k['bubble']=lambda t,c,side='left',rot=0:f'<div style="align-self:{"flex-start" if side=="left" else "flex-end"};padding:20px 34px;border-radius:34px;border-{"bottom-left" if side=="left" else "bottom-right"}-radius:6px;background:{c};color:{INK};font-family:{F};font-weight:800;font-size:46px;transform:rotate({rot}deg);box-shadow:0 12px 26px rgba(0,0,0,.3)">{t}</div>'
    return k

def page(P,s,label):
    img,css,parts,n,veil=s
    A1,INK=P['a1'],P['ink']
    right=f'<span>{n}</span>' if n else f'<span style="padding:12px 32px;border-radius:40px;background:{A1};color:{INK};font-weight:800">Salvate ★</span>'
    v1,v2,glass=veil
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Silkscreen&display=swap">
<style>body{{margin:0}} s{{text-decoration-thickness:7px;text-decoration-color:#FF3B3B}}</style></head><body>
<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background:{v2};color:#fff">
<img src="{img}" style="position:absolute;left:0;width:1080px;object-fit:cover;{css}">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,{v1}55 0%,{v1}00 20%,{v1}00 34%,{v1}cc 62%,{v2}f5 90%)"></div>
<div style="position:absolute;left:60px;right:60px;top:50px;display:flex;align-items:center;justify-content:space-between">
<img src="logo.png" style="width:150px;height:150px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 6px #fff,0 12px 30px rgba(0,0,0,.45)">
<span style="max-width:620px;text-align:right;padding:12px 22px;border-radius:14px;background:{v2}cc;font-family:{PX};font-size:30px;line-height:1.25;letter-spacing:1px;color:{A1}">{label}</span></div>
<div style="position:absolute;left:46px;right:46px;bottom:126px;padding:46px 48px 52px;border-radius:46px;background:{glass};border:2px solid rgba(255,255,255,.3);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);display:flex;flex-direction:column;gap:24px">{''.join(parts)}</div>
<div style="position:absolute;left:70px;right:70px;bottom:42px;height:70px;display:flex;align-items:center;justify-content:space-between;font-family:{F};font-weight:500;font-size:34px;color:rgba(255,255,255,.92)"><span>Irene · Francese per italiani</span>{right}</div>
</div></body></html>'''

async def render(name,P,SL,label):
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,s in enumerate(SL,1):
            f=D+f'{name}{i}.html'; open(f,'w').write(page(P,s,label))
            await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=O+f'{name}_{i}.png')
        await b.close()
    from PIL import Image
    n=len(SL); W=Image.new('RGB',(n*360,450))
    for i in range(n): W.paste(Image.open(O+f'{name}_{i+1}.png').convert('RGB').resize((360,450)),(i*360,0))
    W.save(f'/home/claude/w/prev_{name}.png')
