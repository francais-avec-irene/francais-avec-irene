import json,sys,time,urllib.parse,urllib.request
UA="FLELessonBuilder/1.0 (https://francais-avec-irene.github.io; educational use) python"
for q in sys.argv[1:]:
  for t in range(4):
    try:
      u="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(dict(action='query',format='json',generator='search',gsrnamespace=6,gsrlimit=10,gsrsearch=q+' filetype:bitmap',prop='imageinfo',iiprop='url|size|mime',iiurlwidth=500))
      d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=30))
      print('##',q)
      for p in d.get('query',{}).get('pages',{}).values():
        ii=p['imageinfo'][0]
        if ii['mime']=='image/jpeg' and ii['width']>=1200: print(ii['width'],ii['height'],ii['thumburl'])
      break
    except Exception as e:
      time.sleep(15)
  time.sleep(8)
