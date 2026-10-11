"""Inventory is triage only, never a claim of semantic review."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
import re,json,hashlib,collections
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision';E.mkdir(exist_ok=True)
class Sections(HTMLParser):
 def __init__(self,s):
  super().__init__(convert_charrefs=False);self.s=s;self.lines=[0];self.stack=[];self.items=[]
  self.lines.extend(m.end()for m in re.finditer('\n',s));self.feed(s)
 def where(self):a,b=self.getpos();return self.lines[a-1]+b
 def handle_starttag(self,tag,attrs):
  if tag=='section':self.stack.append((self.where(),dict(attrs)))
 def handle_endtag(self,tag):
  if tag=='section'and self.stack:
   start,a=self.stack.pop()
   if 'exam-question'in a.get('class','').split():self.items.append((start,self.where()+len('</section>'),a))
def plain(s):
 slots=[]
 def hold(m):
  a=re.search(r'aria-label="([^"]*)"',m[1]);slots.append('$'+unescape(a[1])+'$'if a else'[native mathematics]');return ' MATHKEEP'+str(len(slots)-1)+'END '
 s=re.sub(r'<math\b([^>]*)>[\s\S]*?</math>',hold,s)
 s=re.sub(r'\s+',' ',unescape(re.sub('<[^>]*>',' ',s))).strip()
 for i,m in enumerate(slots):s=s.replace('MATHKEEP'+str(i)+'END',m)
 return s
def questions(s):return [(a,b,c,s[a:b])for a,b,c in sorted(Sections(s).items)]
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
chapters=[c for w in json.loads((R/'dist/lessons.json').read_text())for c in w['chapters']];out=[]
for c in chapters:
 p=R/'dist'/c['url'];s=p.read_text(encoding='utf-8');qs=questions(s);records=[]
 for n,(a,b,attrs,q)in enumerate(qs,1):
  prose=plain(q);records.append(dict(index=n,title=plain(re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1]),kind=attrs.get('data-kind'),words=len(prose.split()),mathCount=q.count('<math'),visualMarkers=len(re.findall(r'<svg\b|data-problem-visual=|data-[a-z]+-model=',q)),sha256=hashlib.sha256(q.encode()).hexdigest()))
 # Early chapters use exam-question, newer renderers sometimes use a second class.
 actual=len(qs);declared=c.get('questionCount',0)
 out.append(dict(topicId=c['topicId'],url=c['url'],title=c.get('title')or plain(re.search(r'<h1[^>]*>([\s\S]*?)</h1>',s)[1]),declaredQuestions=declared,extractedQuestions=actual,extractionNeedsReview=actual!=declared,canonicalLFsha256=hashlib.sha256(s.encode()).hexdigest(),state='not_yet_semantically_reviewed',questions=records))
 (E/(c['topicId']+'-question-reading.txt')).write_text('\n\n'.join(plain(q)for a,b,c,q in qs),encoding='utf-8')
manifest=dict(scope='Full existing library review and A-to-Z rewriting; current user instruction supersedes previous chapter approval for this revision.',chapterCount=len(out),declaredWorkedEntries=sum(x['declaredQuestions']for x in out),extractedWorkedEntries=sum(x['extractedQuestions']for x in out),status='inventory_complete_semantic_review_pending',note='Word/formula counts only support triage. They neither prove explanation quality nor count as source review. Student-approved historical content remains preserved in Git.',chapters=out)
save(E/'inventory.json',manifest)
print(json.dumps(dict(chapters=len(out),declaredWorkedEntries=manifest['declaredWorkedEntries'],extractedWorkedEntries=manifest['extractedWorkedEntries'],extractionMismatches=[c['topicId']for c in out if c['extractionNeedsReview']]),indent=2))
if __name__=='__main__':pass
