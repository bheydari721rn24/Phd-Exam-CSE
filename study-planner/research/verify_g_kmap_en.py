"""Independent truth-row and exact-cover certification, archive provenance and preservation."""
from pathlib import Path
from itertools import product,combinations
import json,hashlib,re,subprocess
from kmap_model import cells,primes,optimum,qm,petrick,cost
B=Path(__file__).resolve().parent;R=B.parent;checks=[]
def ck(label,value):assert value,label;checks.append(label)
# Independent enumeration uses bit masks rather than the authoring model's cube matching.
def independent(n,on,dc=()):
 allowed=sum(1<<i for i in set(on)|set(dc));target=sum(1<<i for i in set(on));valid=[]
 for fixed in range(1<<n):
  for values in range(1<<n):
   if values&~fixed:continue
   mask=sum(1<<i for i in range(1<<n) if i&fixed==values)
   if mask&target and not mask&~allowed:
    pattern=''.join('-' if not fixed&(1<<(n-1-j)) else str((values>>(n-1-j))&1) for j in range(n))
    valid.append((pattern,mask,fixed.bit_count()))
 ps=sorted([p for p in valid if not any(p[1]!=q[1] and p[1]&q[1]==p[1] for q in valid)])
 if not target:return [],[()],(0,0)
 best=None;sol=[]
 for r in range(1,len(ps)+1):
  for inds in combinations(range(len(ps)),r):
   union=0
   for j in inds:union|=ps[j][1]
   if union&target==target:
    c=(r,sum(ps[j][2] for j in inds));s=tuple(ps[j][0] for j in inds)
    if best is None or c<best:best=c;sol=[s]
    elif c==best:sol.append(s)
  if best:break
 return [p[0] for p in ps],sorted(sol),best
Q=json.loads((B/'g_kmap-questions.json').read_text());ck('81 distinct tasks',len(Q)==len({q['id'] for q in Q})==81)
for q in Q:
 ck(q['id']+' complete explanatory solution',len(q['solution'].split())>=70)
 k=q['certificate']['kind'];d=q['certificate']['data']
 if k=='cover':
  n,on,dc=d['n'],d['on'],d['dc'];req=sorted(set(range(1<<n))-set(on)-set(dc)) if d['pos'] else on
  ps,sol,c=independent(n,req,dc);ck(q['id']+' all exact candidates/covers/cost',(ps,sol,c)==(d['primes'],sorted(tuple(x) for x in d['covers']),tuple(d['cost'])))
  qp,lev=qm(n,req,dc);ck(q['id']+' independent QM set',sorted(qp)==ps)
  p=petrick(primes(n,req,dc),req);best=min(map(cost,p));ck(q['id']+' exact Petrick ties',sorted(s for s in p if cost(s)==best)==sol)
 elif k=='canonical':
  c=d['cube'];rows=[i for i in range(1<<len(c)) if all(x=='-' or (i>>(len(c)-j-1))&1==int(x) for j,x in enumerate(c))]
  ck(q['id']+' canonical expansion',rows==d['ones'] and sorted(set(range(1<<len(c)))-set(rows))==d['zeros'])
  ck(q['id']+' reverse significance',sorted(int(format(i,f'0{len(c)}b')[::-1],2) for i in rows)==d['reversed'])
  ck(q['id']+' literal count',len(c)*len(rows)==d['literals'])
 else:ck(q['id']+' written proof family',k in {'irredundant','cycle','petrick3','dominance','obligation','diagonal','shape','greedy','dc','empty','merge','counts','parity','threshold','majority','hazard','timing','hazard0','edgecover','sharing','factoring','shannon','consensus','bound','allcovers','contract'})
for mask in range(256):
 on=[i for i in range(8) if mask&(1<<i)];ip,sol,c=independent(3,on);p,ss,cc=optimum(3,on)
 ck('all 3-input functions '+str(mask),(ip,sol,c)==(sorted(p),sorted(ss),cc));ck('QM all 3-input '+str(mask),sorted(qm(3,on)[0])==ip)
for assignment in product(range(3),repeat=4):
 on=[i for i,x in enumerate(assignment) if x==1];dc=[i for i,x in enumerate(assignment) if x==2]
 ck('all incomplete 2-input contracts '+str(assignment),independent(2,on,dc)==(sorted(primes(2,on,dc)),sorted(optimum(2,on,dc)[1]),optimum(2,on,dc)[2]))
# Explicit mathematical identities and lower-bound witnesses.
for A,Bb,C,D,E in product([0,1],repeat=5):
 ck(f'consensus {A}{Bb}{C}{D}{E}',bool(A and Bb or not A and C or Bb and C)==bool(A and Bb or not A and C))
 ck(f'factored {A}{Bb}{C}{D}{E}',bool(A and (Bb or C) and (D or E))==bool(A and Bb and D or A and Bb and E or A and C and D or A and C and E))
 ck(f'majority dual {A}{Bb}{C}{D}{E}',bool(A*Bb+A*C+Bb*C)==bool((A or Bb) and (A or C) and (Bb or C)))
for n in range(1,7):
 for t in range(1,n+1):
  for row in range(1<<n):ck(f'threshold {n},{t},{row}',(row.bit_count()>=t)==any(all(row&(1<<j) for j in chosen) for chosen in combinations(range(n),t)))
on={5,6,7,8,9,15};ps=primes(4,on,{0,1});edges=[(a,b) for a,b in combinations(sorted(on),2) if (a^b).bit_count()==1]
ck('authentic four required edges',edges==[(5,7),(6,7),(7,15),(8,9)])
owners={edge:sorted(c for c,s in ps.items() if set(edge)<=s) for edge in edges};ck('hazard edge owners force minimum',all(len(v)==1 for v in owners.values()) and set(v[0] for v in owners.values())=={'01-1','011-','-111','-00-'} and cost(tuple(v[0] for v in owners.values()))==(4,11))
selected=['01-1','011-','-111','-00-'];realized=set().union(*(cells(c) for c in selected));full_edges=[(a,b) for a,b in combinations(sorted(realized),2) if (a^b).bit_count()==1]
ck('DC completion exposes missing bridge',[(a,b) for a,b in full_edges if not any({a,b}<=cells(c) for c in selected)]==[(1,5)])
fixed=selected+['0-01'];ck('added consensus bridges completed graph',all(any({a,b}<=cells(c) for c in fixed) for a,b in full_edges))
alternative=['01-1','011-','-111','100-'];ck('zero DC completion removes all edges',set().union(*(cells(c) for c in alternative))==on and all(any({a,b}<=cells(c) for c in alternative) for a,b in edges) and cost(alternative)==(4,12))
data=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes'];new={k:v for k,v in data.items() if k.startswith('km-')};ck('14 new models',len(new)==14)
checkpoint_count=0
for id,s in new.items():
 for j,f in enumerate(s['frames']):
  checkpoint_count+=1;v=f['snapshot'];ck(id+' caption '+str(j),len(f['caption'].split())>=14)
  if 'cover' in v:
   union=set().union(*(cells(c) for c in v['cover'])) if v['cover'] else set();ck(id+' exact cube union '+str(j),sorted(union)==v['covered'] and sorted(union&set(v['on']))==v['requiredCovered'] and union<=set(v['on'])|set(v['dc']))
  if id=='km-gray':ck(id+str(j),v['label']==[0,1,3,2,0][j])
  if id=='km-merge':ck(id+str(j),v['rows']==sorted(cells(v['pattern'])))
  if id=='km-qm':ck(id+str(j),v['patterns']==qm(4,v['on'])[1][v['level']])
  if id=='km-hazard-time':t=v['time'];ck(id+str(j),v['signals']=={'A':0,'AB':int(t<1),'not A':int(t>=3),'not A C':int(t>=4),'F':int(t<2 or t>=5)})
  if id=='km-chart':ck(id+str(j),v['owners']=={str(m):sorted(c for c,s in primes(3,[2,3,5,7]).items() if m in s) for m in [2,3,5,7]})
  if id=='km-petrick':ck(id+str(j),v['satisfied']==[bool(set(v['selection'])&set(z)) for z in [['P','Q'],['Q','R'],['P','R']]] and v['cost']==[len(v['selection']),sum({'P':2,'Q':3,'R':5}[x] for x in v['selection'])])
  if id=='km-pos':ck(id+str(j),v['zero'] in [0,1,2,4])
  if id=='km-sharing':ck(id+str(j),v['outputs']=={'AB':['F','G'],'AC':['F'],'BC':['G']}[v['product']])
  if id=='km-planes':ck(id+str(j),v['rows']==sorted(cells(v['pattern'])))
auth=json.loads((B/'g_kmap-authentic.json').read_text());cache=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')
for a in auth:ck(a['id']+' original PDF fingerprint',hashlib.sha256((cache/a['repoPath']).read_bytes()).hexdigest()==a['sourceSha256'])
old='88e1179f6f076477a499f8b455ca429c2b2bcf63';total=0
approved=json.loads((B/'library-approval.json').read_text())['approvedTopics'];ck('29 approved chapters remain',len(approved)==29)
for topic in approved:
 path='dist/chapters/'+topic+'.html';before=subprocess.check_output(['git','show',old+':'+path],cwd=R).decode();after=(R/path).read_text(encoding='utf-8')
 regex=r'<section class="exam-question"[\s\S]*?</section>';a=re.findall(regex,before);b=re.findall(regex,after);ck(topic+' complete approved banks preserved',a==b);total+=len(a)
ck('1581 prior entries preserved',total==1581)
h=(R/'dist/chapters/g_kmap.html').read_text(encoding='utf-8');ck('84 printable solutions',h.count('class="exam-question"')==h.count('class="exam-solution"')==84);ck('80 rules',h.count('class="review-rule"')==80);ck('seven original SVG figures',h.count('class="logic-diagram kmap-diagram"')==7);ck('no raw TeX markers','$' not in h);ck('chapter English only',not re.search(r'[\u0600-\u06ff]',h))
import sys,html,xml.etree.ElementTree as ET
sys.path.insert(0,str(B/'exam-rewrite'))
import mathml
def leaves(root):return [(e.tag.split('}')[-1],e.text or '') for e in root.iter() if not len(e) and e.tag.split('}')[-1] in ['mi','mn','mo'] and e.text!='·']
for j,m in enumerate(re.findall(r'<math\b[\s\S]*?</math>',h)):
 root=ET.fromstring(m);expected=ET.fromstring(mathml.render(root.attrib['aria-label']));ck('responsive formula tokens preserved '+str(j),leaves(root)==leaves(expected))
report=dict(status='passed',checks=len(checks),questions=84,originalQuestions=81,authenticRevisits=3,ambiguityTutorials=1,reviewRules=80,figures=7,models=14,checkpoints=checkpoint_count,preservedApprovedChapters=29,preservedPriorEntries=total,methods=['Independent bit-mask cube/cover enumeration','Independent Petrick and iterative QM comparison','All 256 three-input Boolean functions','All 81 two-input incomplete specifications','Explicit identities and threshold families through six inputs','DC completion transition audit','Responsive formula token preservation','Original archive PDF fingerprints','Exact approved-bank preservation'])
(B/'g_kmap-validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
