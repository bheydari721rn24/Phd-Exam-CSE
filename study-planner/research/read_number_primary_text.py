from pathlib import Path
from html.parser import HTMLParser
import sys,tempfile
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ['script','style']:self.skip+=1
  if tag in ['p','h1','h2','h3','h4','li','tr','br']:self.out.append('\n')
 def handle_endtag(self,tag):
  if tag in ['script','style']:self.skip-=1
 def handle_data(self,data):
  if not self.skip:self.out.append(data)
t=Path(tempfile.gettempdir());name=sys.argv[1]
if name=='stanford':
 import fitz
 d=fitz.open(t/'g-number-review-b/stanford.pdf');pages=list(range(8,51))+list(range(53,85))+list(range(109,115));s='\n'.join('PDF PAGE '+str(i)+'\n'+d[i-1].get_text() for i in pages)
else:
 p=Text();p.feed((t/'deep-number-sources'/(name+'.html')).read_text(encoding='utf-8'));s='\n'.join(' '.join(x.split()) for x in ''.join(p.out).splitlines() if x.strip())
print('TOTAL CHARACTERS',len(s));a=int(sys.argv[2]) if len(sys.argv)>2 else 0;b=int(sys.argv[3]) if len(sys.argv)>3 else len(s);print(s[a:b])
