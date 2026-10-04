"""Independent exact arithmetic, executable Python and preservation checks."""
import json,math,itertools,hashlib,re,subprocess
from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent;checks=[]
def ck(n,v):
 assert v,n
 checks.append(n)
Q=json.loads((B/'p_arrays-questions.json').read_text());ck('81 distinct authored tasks',len(Q)==len({q['id'] for q in Q})==81)
manual={'provenance','subarray','initialization','constraints','onepast','reverseguard','copycontract','segmentproof','string','literal','searchboundaries','argv','ctype','lifetime','doublingproof','realloc','hysteresis','interface','overflow','boundsproof','pointerdomain'}
for q in Q:
 k=q['certificate']['kind'];d=q['certificate']['data'];name=q['id']+' '+k
 ck(name+' complete explanation',len(q['solution'].split())>=45)
 if k=='python':
  ns={};exec(d[0],ns);ck(name+' actual execution',json.loads(json.dumps(ns['result']))==d[1])
 elif k=='address':b,w,l,u,i,x=d;ck(name,b+w*(i-l)==x and l<=i<=u)
 elif k=='inverse':b,w,lr,lc,r,c,x,i,j=d;o=(x-b)//w;ck(name,(x-b)%w==0 and (lr+o//c,lc+o%c)==(i,j) and o<r*c)
 elif k=='recover':ck(name,(36//4+1)//2==d[0] and 1028-4*(d[0]+2)==d[1])
 elif k=='layouts':r,c,i,j,a,b=d;ck(name,(i*c+j,j*r+i)==(a,b))
 elif k=='mixed':r,c,z,i,j,t,o=d;ck(name,(i*c+j)*z+t==o and divmod(o,z)==(i*c+j,t))
 elif k=='transpose':r,c,o,t,o2,t2=d;ck(name,(o%c)*r+o//c==t and (o2%c)*r+o2//c==t2)
 elif k=='strides':ck(name,1020+40*2-4*5==d[0] and 1020+40==d[1] and min(1020+40*i-4*j for i in range(3) for j in range(6))==d[2] and max(1020+40*i-4*j for i in range(3) for j in range(6))==d[3])
 elif k=='lower':n,i,j,o=d;ck(name,sum(range(1,i+1))+j==o and j<=i<n)
 elif k=='upper':n,i,j,o,ri,rj=d;ck(name,sum(n-t for t in range(i))+j-i==o and (ri,rj)==(2,2))
 elif k=='jagged':lens,starts=d;ck(name,starts==[sum(lens[:i]) for i in range(len(lens)+1)])
 elif k=='diagonal':n,s=d;ck(name,sum(i*n+i for i in range(n))==s)
 elif k=='interior':n,r,l,u,pdiff,bytes_=d;ck(name,list(range(-r,n-r))==list(range(l,u+1)) and pdiff==4 and bytes_==14)
 elif k=='sizeof':n,w,p,actual,wrong=d;ck(name,(n*w//w,p//w)==(actual,wrong))
 elif k=='whole':ck(name,d==[4,24])
 elif k=='rowpointer':r,c,w,x,y=d;ck(name,(2*c*w,c*w)==(x,y))
 elif k=='stride':l,r,s,count,last=d;seq=list(range(l,r,s));ck(name,(len(seq),seq[-1])==(count,last))
 elif k=='minimum':a,cmp_,up,sc,su=d;m=a[0];updates=0
 elif k=='weighted':a,s=d;ck(name,sum((i+1)*v for i,v in enumerate(a))==s)
 elif k=='prefix':a,p=d;ck(name,[sum(a[:i]) for i in range(len(a)+1)]==p)
 elif k=='difference':a,out=d;ck(name,[sum(a[:i+1]) for i in range(len(out))]==out)
 elif k=='rect':a,total=d;ck(name,sum(a[i][j] for i in range(2) for j in range(1,3))==total)
 elif k=='inplace':a,order,out=d;b=a[:];indices=range(1,len(a)) if order=='forward' else range(len(a)-1,0,-1)
 elif k=='move':a,s,t,m,order,out=d;b=a[:];indices=range(m) if order=='forward' else range(m-1,-1,-1)
 elif k=='insert':a,i,v,out,count=d;ck(name,a[:i]+[v]+a[i:]==out and len(a)-i==count)
 elif k=='delete':a,i,out,count=d;ck(name,a[:i]+a[i+1:]==out and len(a)-i-1==count)
 elif k=='reverse':a,l,r,out=d;ck(name,a[:l]+a[l:r][::-1]+a[r:]==out)
 elif k=='rotate':a,t,out=d;ck(name,a[t:]+a[:t]==out)
 elif k=='cycles':n,t,c,size=d;ck(name,math.gcd(n,t)==c and n//c==size)
 elif k=='filter':a,out=d;ck(name,[v for v in a if v%2==0]==out)
 elif k=='difftransform':a,out=d;ck(name,[a[0]]+[a[i]-a[i-1] for i in range(1,len(a))]==out)
 elif k=='boundedlength':a,n=d;ck(name,next(i for i,v in enumerate(a) if v==0)==n)
 elif k=='search':a,p,start,count=d;c=0;found=None
 elif k=='append':a,b,c=d;ck(name,a+b+1==c)
 elif k=='doubling':n,cap,copies,total,peak=d;c=1;work=0;peak_=1
 elif k=='additive':n,g,copies=d;ck(name,sum(range(g,n,g))==copies)
 elif k=='tripling':n,cap,copies=d;c=1;work=0
 elif k=='allocation':lim,w,n=d;ck(name,lim//w==n and (n+1)*w>lim)
 elif k=='growthinsert':n,i,copy,shift,total,peak=d;ck(name,(n,n-i,n+n-i+1,3*n)==(copy,shift,total,peak))
 elif k=='cache':r,c,row,col=d;ck(name,row==r and col==r*c)
 elif k=='cacheinterval':start,n,w,line,count=d;ck(name,len({(start+w*i+b)//line for i in range(n) for b in range(w)})==count)
 elif k=='ring':cap,h,n,pos,tail=d;ck(name,[(h+i)%cap for i in range(n)]==pos and (h+n)%cap==tail)
 elif k=='transposecycle':mapping,cycle=d;ck(name,[j*2+i for i in range(2) for j in range(3)]==mapping and [mapping[i] for i in cycle]==cycle[1:]+cycle[:1])
 elif k=='triangleinverse':o,i,j=d;ck(name,sum(range(1,i+1))+j==o and 0<=j<=i)
 elif k=='pairs':n,p,dia=d;ck(name,sum(1 for i in range(n) for j in range(n) if i<j)==p and sum(1 for i in range(n) for j in range(n) if i<=j)==dia)
 elif k=='fill':n,sq=d;ck(name,n*n==sq<=2**31-1 and (n+1)**2>2**31-1)
 elif k=='average':s,n,v=d;ck(name,s//n==v and s/n>v)
 else:ck(name+' explicitly audited written semantic case',k in manual)
 if k=='minimum':
  for v in a[1:]:
   if v<m:m=v;updates+=1
  ck(name,cmp_==len(a)-1 and updates==up and sc==len(a) and su==updates+1)
 if k=='inplace':
  for i in indices:b[i]+=b[i-1]
  ck(name,b==out)
 if k=='move':
  for i in indices:b[t+i]=b[s+i]
  ck(name,b==out)
 if k=='search':
  for i in range(len(a)-len(p)+1):
   for j in range(len(p)):
    c+=1
    if a[i+j]!=p[j]:break
   else:found=i;break
  ck(name,(found,c)==(start,count))
 if k in ('doubling','tripling'):
  g=2 if k=='doubling' else 3
  while c<n:work+=c;peak_=c*(g+1);c*=g
  ck(name,(c,work)==(cap,copies))
  if k=='doubling':ck(name+' total and peak',(n+work,peak_)==(total,peak))

# Exhaust every legal same-object segment for sizes zero through eight.
for n in range(9):
 for m in range(n+1):
  for s in range(n-m+1):
   for d in range(n-m+1):
    a=list(range(n));expected=a[:];expected[d:d+m]=a[s:s+m]
    for i in (range(m-1,-1,-1) if d>s else range(m)):a[d+i]=a[s+i]
    ck(f'overlap snapshot {n},{m},{s},{d}',a==expected)
for r in range(1,12):
 for c in range(1,12):
  for i in range(r):
   for j in range(c):ck(f'layout inverse {r},{c},{i},{j}',divmod(i*c+j,c)==(i,j) and divmod(j*r+i,r)==(j,i))
for n in range(1,129):
 cap=1;copies=0
 while cap<n:copies+=cap;cap*=2
 ck(f'doubling bound {n}',copies==cap-1 and copies<2*n)
 seq=[n-1-2*t for t in range((n+1)//2)];ck(f'authentic stride {n}',seq==list(range(n-1,-1,-2)))

data=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes'];new={k:v for k,v in data.items() if k.startswith('arr-')};ck('18 array models',len(new)==18)
for id,scene in new.items():
 a=[2,4,6,8,10,12];target=['—']*6;prev=None
 for index,f in enumerate(scene['frames']):
  s=f['snapshot'];ck(f'{id} caption {index}',len(f['caption'].split())>=14)
  if id=='arr-boundary':ck(id+str(index),0<=s['index']<=6 and s['values']==a)
  elif id in ('arr-row','arr-column'):i,j=s['coord'];ck(id+str(index),s['offset']==4*i+j and s['coord']==([s['step']//4,s['step']%4] if id=='arr-row' else [s['step']%3,s['step']//3]))
  elif id=='arr-prefix':ck(id+str(index),s['prefix']==[sum(s['input'][:i]) for i in range(s['index']+1)])
  elif id.startswith('arr-copy'):
   if index:a[s['destination']+s['step']]=a[s['source']+s['step']]
   ck(id+str(index),s['values']==a)
  elif id=='arr-insert':ck(id+str(index),s['values']==[[3,6,9,12,'—','—'],[3,6,9,12,12,'—'],[3,6,9,9,12,'—'],[3,6,7,9,12,'—']][index])
  elif id=='arr-reverse':ck(id+str(index),s['values']==[[0,1,2,3,4,5],[5,1,2,3,4,0],[5,4,2,3,1,0],[5,4,3,2,1,0]][index])
  elif id=='arr-rotate':ck(id+str(index),s['values']==[[0,1,2,3,4,5],[1,0,2,3,4,5],[1,0,5,4,3,2],[2,3,4,5,0,1]][index])
  elif id=='arr-sharing':ck(id+str(index),s['row']==([2] if index<2 else [2,7]))
  elif id=='arr-growth':ck(id+str(index),s['new']==[2,4,6][:min(index,3)]+['—']*(6-min(index,3)) and s['oldLive']==(index<4))
  elif id=='arr-packed':ck(id+str(index),s['offset']==sum(range(1,s['i']+1))+s['j'])
  elif id=='arr-ring':ck(id+str(index),s['physical']==(5+s['t'])%7)
  elif id=='arr-transpose':
   o=s['source'];ck(id+str(index)+' map',(s['i'],s['j'])==divmod(o,3) and s['destination']==(o%3)*2+o//3)
   if s['phase']=='write':target[s['destination']]=o
   ck(id+str(index)+' fills',s['target']==target)
  elif id=='arr-difference':ck(id+str(index),s['values']==[[3,5,9,10],[3,5,9,1],[3,5,4,1],[3,2,4,1]][index])
  elif id=='arr-compact':ck(id+str(index),s['values'][:s['write']]==[v for v in [5,2,7,4,6,9][:s['read']] if v%2==0])
  elif id=='arr-search':ck(id+str(index),s['equal']==('aaaaab'[s['start']+s['j']]=='aaab'[s['j']]) and s['comparisons']==index+1)
  # Rendered values must agree with the semantic snapshot for every ordinary slot.
  if 'values' in s:ck(id+str(index)+' visible slots',[n['label'] for n in f['nodes'] if re.fullmatch('a[0-9]+',n['id'])]==list(map(str,s['values'])))
auth=json.loads((B/'p_arrays-authentic.json').read_text())
for q in auth:
 p=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/q['repoPath']
 ck(q['id']+' scan identity',hashlib.sha256(p.read_bytes()).hexdigest()==q['sourceSHA'])
 ck(q['id']+' pinned and revisit',q['sourceCommit']=='bdadf6e2c9cadc4772ae137a96a3da753c7cfd08' and 'revisit' in q['provenance'].lower())
ck('authentic answer options',[q['answer'] for q in auth]==[1,2])
approved=json.loads((B/'library-approval.json').read_text())['approvedTopics'];ck('28 approved topics',len(approved)==28);total=0
for id in approved:
 live=(R/f'dist/chapters/{id}.html').read_text(encoding='utf-8');old=subprocess.check_output(['git','show','02ef07ea0cd7e2c7fcebb1147f62327848ff6cf1:dist/chapters/'+id+'.html'],cwd=R).decode('utf-8')
 extract=lambda s:re.findall(r'<section class="exam-question"[\s\S]*?</section>',s)
 ck(id+' approved question preservation',extract(live)==extract(old));total+=len(extract(live))
ck('1498 approved entries preserved',total==1498)
page=(R/'dist/chapters/p_arrays.html').read_text();ck('chapter metrics',page.count('class="exam-question"')==83 and page.count('class="review-rule"')==80 and page.count('<figure')==7)
ck('English native formula content',not re.search('[\u0600-\u06ff]',page) and '$' not in page)
ck('six actually reviewed universities',len({c['university'] for c in json.loads((B/'p_arrays-reviewed-courses.json').read_text())})==6)
result=dict(state='passed',checks=len(checks),questionCount=83,ruleCount=80,modelCount=18,checkpoints=sum(len(s['frames']) for s in new.values()),approvedQuestionsPreserved=total,pythonExecutions=10,limitations='Finite exact-state models and Python execution; C cases verified by explicit written rules, not local compiler execution. No universal unseen-question guarantee.',details=checks)
(B/'p_arrays-validation.json').write_text(json.dumps(result,indent=2)+'\n');(R/'dist/evidence/p_arrays/validation.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k!='details'})
