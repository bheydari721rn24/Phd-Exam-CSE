from pathlib import Path
from html.parser import HTMLParser
import sys
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ['script','style']:self.skip+=1
  if tag in ['p','h1','h2','h3','h4','li','tr','br']:self.out.append('\n')
 def handle_endtag(self,tag):
  if tag in ['script','style']:self.skip-=1
 def handle_data(self,data):
  if not self.skip:self.out.append(data)
p=Text();p.feed((Path('C:/Users/bheydari/AppData/Local/Temp/deep-boolean-recheck')/(sys.argv[1]+'.html')).read_text(encoding='utf-8'))
s='\n'.join(' '.join(x.split()) for x in ''.join(p.out).splitlines() if x.strip())
print('TOTAL CHARACTERS',len(s));a=int(sys.argv[2]) if len(sys.argv)>2 else 0;b=int(sys.argv[3]) if len(sys.argv)>3 else len(s);print(s[a:b])
