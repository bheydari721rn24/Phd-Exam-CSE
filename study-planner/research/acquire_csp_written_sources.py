"""Cache written CSP candidates; acquisition is explicitly not a reading claim."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import hashlib,json,requests,fitz
CACHE=Path('C:/Users/bheydari/AppData/Local/Temp/phd-csp-sources-20261018');CACHE.mkdir(exist_ok=True)
class Prose(HTMLParser):
    def __init__(self):super().__init__();self.parts=[];self.skip=0
    def handle_starttag(self,t,a):
        if t in['script','style']:self.skip+=1
    def handle_endtag(self,t):
        if t in['script','style']:self.skip=max(0,self.skip-1)
    def handle_data(self,s):
        if not self.skip and s.strip():self.parts.append(s.strip())
def acquire(item):
    name,url=item
    try:
        r=requests.get(url,timeout=45);r.raise_for_status();suffix='.pdf'if r.content.startswith(b'%PDF')else'.js'if'.js'in url else'.html'
        p=CACHE/(name+suffix);p.write_bytes(r.content)
        row={'id':name,'url':r.url,'path':str(p),'sha256':hashlib.sha256(r.content).hexdigest(),'bytes':len(r.content),'readingState':'acquired_not_read'}
        if suffix=='.pdf':
            doc=fitz.open(p);row['pages']=len(doc);body='\n'.join('--- PDF page '+str(i+1)+' ---\n'+x.get_text()for i,x in enumerate(doc))
        elif suffix=='.js':body=r.content.decode('utf8')
        else:
            raw=r.content.decode('utf8');start=raw.find('<main');end=raw.find('</main>')
            parser=Prose();parser.feed(raw[start:end]if start>=0 and end>start else raw);body='\n'.join(parser.parts)
        (CACHE/(name+'.txt')).write_text(body,encoding='utf8');return row
    except Exception as e:return {'id':name,'url':url,'readingState':'direct_download_failed_reading_evidence_separate','error':str(e)}
if __name__=='__main__':
    items=[
        ('berkeley-filtering','https://inst.eecs.berkeley.edu/~cs188/textbook/csp/filtering.html'),
        ('berkeley-ordering','https://inst.eecs.berkeley.edu/~cs188/textbook/csp/ordering.html'),
        ('cmu-constraints','https://www.cs.cmu.edu/~15281-f25/coursenotes/constraints/index.html'),
        ('harvard-optimization','https://cs50.harvard.edu/ai/notes/3/'),
        ('stanford-course-data','https://stanford-cs221.github.io/spring2026/modules/course-data.js?v=1'),
        ('mit-autonomy-index','https://ocw.mit.edu/courses/16-410-principles-of-autonomy-and-decision-making-fall-2010/pages/lecture-notes/'),
        ('cornell-csp','https://www.cs.cornell.edu/courses/cs4700/2013fa/slides/CS4700-CSP_v6.pdf')]
    with ThreadPoolExecutor(max_workers=4)as pool:rows=list(pool.map(acquire,items))
    (CACHE/'acquisition.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf8')
    print(json.dumps(rows,indent=2))
