import requests,re,json
from pathlib import Path
from urllib.parse import urljoin
from html.parser import HTMLParser
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.href=None;self.label=''
 def handle_starttag(self,t,a):
  if t=='a':self.href=dict(a).get('href');self.label=''
 def handle_data(self,s):
  if self.href:self.label+=s
 def handle_endtag(self,t):
  if t=='a' and self.href:self.links.append((self.label.strip(),self.href));self.href=None
for key,u in [('cmu','https://www.cs.cmu.edu/~15122-archive/s24/handouts.shtml'),('berkeley','https://sp25.datastructur.es/'),('mit','https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/'),('princeton','https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures.php')]:
 try:
  r=requests.get(u,timeout=30);r.raise_for_status();p=Links();p.feed(r.text)
  print(key,[(label,urljoin(u,h)) for label,h in p.links if any(w in (label+' '+h).lower() for w in ['linked','list','array','sequence','02','03','04','05','stack','queue'])][:36])
 except Exception as e:print(key,str(e))
