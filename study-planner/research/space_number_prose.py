"""Repair prose word/number spacing while preserving code, mathematics and SVG."""
from html.parser import HTMLParser
import re
def clean(s):
 s=re.sub(r'(?<![0-9])([A-Za-z]{2,})(?=\d)',r'\1 ',s)
 s=re.sub(r'(?<!\d)([.;:])(?=[A-Za-z0-9])',r'\1 ',s)
 return re.sub(r'(?<=[A-Za-z])-(?=\d)',' -',s)
class Prose(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=False);self.out=[];self.stack=[]
 def handle_starttag(self,tag,attrs):
  self.out.append(self.get_starttag_text());d=dict(attrs)
  if tag not in ['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']:
   self.stack.append((tag,tag in ['script','style','math','svg','code','pre'] or 'math-inline' in d.get('class','').split()))
 def handle_startendtag(self,tag,attrs):self.out.append(self.get_starttag_text())
 def handle_endtag(self,tag):
  self.out.append('</'+tag+'>')
  if self.stack and self.stack[-1][0]==tag:self.stack.pop()
 def handle_data(self,s):self.out.append(s if any(v for _,v in self.stack) else clean(s))
 def handle_entityref(self,s):self.out.append('&'+s+';')
 def handle_charref(self,s):self.out.append('&#'+s+';')
 def handle_comment(self,s):self.out.append('<!--'+s+'-->')
 def handle_decl(self,s):self.out.append('<!'+s+'>')
def fix(s):
 p=Prose();p.feed(s);p.close();return ''.join(p.out)
