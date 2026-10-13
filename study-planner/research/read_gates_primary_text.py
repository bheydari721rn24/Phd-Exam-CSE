from pathlib import Path
from html.parser import HTMLParser
import sys,fitz
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ['script','style']:self.skip+=1
  if tag in ['p','h1','h2','h3','h4','li','tr','br']:self.out.append('\n')
 def handle_endtag(self,tag):
  if tag in ['script','style']:self.skip-=1
 def handle_data(self,data):
  if not self.skip:self.out.append(data)
S=Path('C:/Users/bheydari/AppData/Local/Temp/deep-gates-recheck');name=sys.argv[1]
if name=='stanford':
 d=fitz.open(S/'stanford.pdf');pages=list(range(39,43))+[45]+list(range(58,66))+[66]+list(range(67,77))+[79]+list(range(83,86))+[100,101]
 s='\n'.join('PHYSICAL PDF PAGE '+str(i)+'\n'+d[i-1].get_text()for i in pages)
else:
 p=Text();p.feed((S/(name+'.html')).read_text(encoding='utf-8'));s='\n'.join(' '.join(x.split())for x in ''.join(p.out).splitlines()if x.strip())
print('TOTAL CHARACTERS',len(s));a=int(sys.argv[2])if len(sys.argv)>2 else 0;b=int(sys.argv[3])if len(sys.argv)>3 else len(s);print(s[a:b])
