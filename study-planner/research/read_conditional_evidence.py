from pathlib import Path
from html.parser import HTMLParser
import json
P=Path('C:/Users/bheydari/AppData/Local/Temp/phd-conditional-sources')
class Body(HTMLParser):
    def __init__(self):super().__init__();self.skip=0;self.out=[]
    def handle_starttag(self,t,a):
        if t in ('script','style'):self.skip+=1
    def handle_endtag(self,t):
        if t in ('script','style'):self.skip-=1
    def handle_data(self,d):
        if not self.skip and d.strip():self.out.append(d.strip())
for name in ['stanford-chain','stanford-independence','stanford-conditional']:
    b=Body();b.feed((P/(name+'.html')).read_text());s='\n'.join(b.out);s=s[s.find('Ⓒ Chris Piech'):];print('\n'+name+'\n'+s)
a=json.loads(Path('research/exam-calibration/actual-items.json').read_text())
for q in a:
    if q['id'] in ['MS_CE_1405_Q35','Phd_CS_1404_Q68','Phd_CS_1404_Q69','Phd_CS_1404_Q70']:print(json.dumps(q,indent=2))
