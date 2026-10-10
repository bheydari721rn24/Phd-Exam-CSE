from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json,hashlib,fitz
from html.parser import HTMLParser
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[]
 def handle_data(self,s):self.out.append(s)
P=Path('C:/Users/bheydari/AppData/Local/Temp/a-balanced-sources');P.mkdir(exist_ok=True)
sources={
 'stanford6.pdf':'https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/lectures/06/Condensed%20Slides.pdf',
 'stanford7.pdf':'https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/lectures/07/Condensed%20Slides.pdf',
 'mit.pdf':'https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/83cdd705cd418d10d9769b741e34a2b8_MIT6_006F11_lec06.pdf',
 'cmu.pdf':'https://www.cs.cmu.edu/~15122/handouts/lectures/16-avl.pdf',
 'berkeley27.txt':'https://people.eecs.berkeley.edu/~jrs/61b/lec/27',
 'princeton.pdf':'https://www.cs.princeton.edu/courses/archive/spring23/cos226/lectures/33BalancedSearchTrees.pdf',
 'princeton.html':'https://algs4.cs.princeton.edu/33balanced/',
 'stanford6.html':'https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/lectures/06/',
 'stanford7.html':'https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/lectures/07/',
 'eth.html':'https://lec.inf.ethz.ch/DA/2020/'
}
def one(it):
 name,url=it
 try:
  r=requests.get(url,timeout=(10,45));r.raise_for_status();data=r.content;(P/name).write_bytes(data)
  out={'file':name,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
  if name.endswith('.pdf'):
   d=fitz.open(stream=data,filetype='pdf');out['pages']=len(d);s='\n\n'.join('PAGE '+str(i+1)+'\n'+p.get_text()for i,p in enumerate(d))
  elif name.endswith('.html'):
   parser=Text();parser.feed(r.text);s='\n'.join(parser.out)
  else:s=r.text
  (P/(name+'.read.txt')).write_text(s,encoding='utf-8');out['status']='acquired';return out
 except Exception as e:return {'file':name,'url':url,'status':'unavailable','error':str(e)}
rows=list(ThreadPoolExecutor(max_workers=7).map(one,sources.items()));(P/'acquisition.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
