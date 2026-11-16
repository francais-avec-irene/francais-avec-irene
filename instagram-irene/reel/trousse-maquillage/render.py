import asyncio,subprocess,json
from playwright.async_api import async_playwright
FPS=30
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file:///home/claude/tr/reel_built.html');await pg.wait_for_load_state('networkidle');await pg.evaluate('document.fonts.ready')
        dur=await pg.evaluate('DUR');n=int(dur*FPS)
        ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-i','voice_final.m4a','-map','0:v','-map','1:a','-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-c:a','copy','-shortest','-movflags','+faststart','reel_trousse.mp4'],stdin=subprocess.PIPE)
        for i in range(n):
            await pg.evaluate(f'render({i/FPS})')
            ff.stdin.write(await pg.screenshot(type='jpeg',quality=90))
            if i%300==0: print(i,n,flush=True)
        ff.stdin.close();ff.wait();await b.close();print('done')
asyncio.run(main())
