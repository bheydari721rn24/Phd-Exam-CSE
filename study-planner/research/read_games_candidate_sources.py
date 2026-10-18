"""Acquire written primary material to an external cache, never course videos."""
from pathlib import Path
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,re,requests,fitz
CACHE=Path('C:/Users/bheydari/AppData/Local/Temp/phd-game-sources-20261017')
class Text(HTMLParser):
 def __init__(self): super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']: self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']: self.skip-=1
 def handle_data(self,s):
  if not self.skip and s.strip(): self.out.append(s.strip())
def acquire(item):
 name,url=item
 r=requests.get(url,timeout=60);r.raise_for_status()
 suffix='.pdf' if r.content.startswith(b'%PDF') else '.html'
 p=CACHE/(name+suffix);p.write_bytes(r.content)
 row={'id':name,'url':r.url,'sha256':hashlib.sha256(r.content).hexdigest(),'bytes':len(r.content),'state':'acquired_not_read'}
 if suffix=='.pdf':
  doc=fitz.open(p);row['pages']=len(doc)
  text='\n'.join('---PAGE '+str(i+1)+'---\n'+page.get_text() for i,page in enumerate(doc))
 else:
  raw=r.content.decode('utf8');body=raw
  if name=='harvard':body=raw[raw.index('<h3 id="adversarial-search">'):]
  elif name.startswith('berkeley'):body=raw[raw.index('<main'):raw.index('</main>')]
  parser=Text();parser.feed(body);text='\n'.join(parser.out)
 (CACHE/(name+'.txt')).write_text(text,encoding='utf8')
 return row
if __name__=='__main__':
 items=[('stanford-games1','https://stanford-cs221.github.io/spring2026-extra/modules/games/games1.pdf'),('stanford-games2','https://stanford-cs221.github.io/spring2026-extra/modules/games/games2.pdf'),('harvard','https://cs50.harvard.edu/ai/notes/0/'),('berkeley-minimax','https://inst.eecs.berkeley.edu/~cs188/textbook/games/minimax.html'),('berkeley-expectimax','https://inst.eecs.berkeley.edu/~cs188/textbook/games/expectimax.html'),('berkeley-mcts','https://inst.eecs.berkeley.edu/~cs188/textbook/games/monte-carlo.html')]
 rows=[]
 with ThreadPoolExecutor(4) as pool:
  futures=[(item,pool.submit(acquire,item)) for item in items]
  for item,future in futures:
   try:rows.append(future.result())
   except Exception as e:rows.append({'id':item[0],'url':item[1],'error':str(e),'state':'not_read'})
 (CACHE/'teaching-acquisition.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf8')
 print(json.dumps(rows,indent=2))
