"""Exact mass-flow, absorbing waits, population depletion and law transformations."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from math import comb,exp,factorial,sqrt
from html import escape as h
import json
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_distributions-evidence'
E.mkdir(exist_ok=True)
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def clean(x):
 if isinstance(x,F):return float(x)
 if isinstance(x,dict):return {str(k):clean(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [clean(v)for v in x]
 return x
def fmt(x):return str(round(float(x),5)).removesuffix('.0')
def tx(x,y,t,anchor='start',math=False):return f'<text x="{x}" y="{y}" class="sd-{"math"if math else"prose"}" text-anchor="{anchor}">{h(str(t))}</text>'
def node(x,y,label,id,fill='#e1eef1'):
 return f'<g data-entity="{h(id)}"><circle cx="{x}" cy="{y}" r="15" fill="{fill}" stroke="#658899"/>{tx(x,y+5,label,"middle",True)}</g>'
def arrow(x1,y1,x2,y2):
 d=sqrt((x2-x1)**2+(y2-y1)**2);dx=(x2-x1)/d;dy=(y2-y1)/d
 return f'<path d="M{x1+15*dx} {y1+15*dy}L{x2-15*dx} {y2-15*dy}" fill="none" stroke="#b98634" stroke-width="2" marker-end="url(#sd-arrow)"/>'
def svg(z):
 out='<defs><marker id="sd-arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#b98634"/></marker></defs>'
 kind=z['kind']
 if kind=='flow':
  n=z['n'];X=lambda k:95+580*k/max(1,n)
  out+=tx(40,35,''+z['experiment'])+tx(40,66,'Upper: completed step '+str(z['step']-1)+' · lower: incoming step '+str(z['step']))
  if z.get('from')is not None:out+=arrow(X(z['from']),125,X(z['to']),260)
  for row,y,prefix in [(z['source'],125,'s'),(z['destination'],260,'d')]:
   for k,v in enumerate(row):
    out+=node(X(k),y,k,prefix+str(k),'#ffe4ad'if k==z.get('to')and prefix=='d'else'#e1eef1')+tx(X(k),y-29 if y==125 else y+39,fmt(v),'middle',True)
  out+=tx(40,335,'Transferred mass '+fmt(z['transferred'])+' · destination total '+fmt(sum(z['destination'])),math=True)
 elif kind=='wait':
  r=z['r'];X=lambda k:120+490*k/r
  out+=tx(45,35,'State = successes already observed · final state absorbs mass')
  for k,v in enumerate(z['mass']):
   x=X(k);out+=node(x,145,str(k),str(k),'#cee5d8'if k==r else'#e1eef1')+tx(x,110,fmt(v),'middle',True)
   if k<r:out+=arrow(x,145,X(k+1),145)+tx((x+X(k+1))/2,179,'success','middle')
  out+=tx(45,228,'Completed trials '+str(z['step'])+' · new finishing mass '+fmt(z['newFinish']),math=True)
  out+=tx(45,265,'Finished by now '+fmt(z['mass'][-1])+' · still waiting '+fmt(sum(z['mass'][:-1])),math=True)
  out+=tx(45,310,'The unresolved tail stays visible; this finite horizon is not a truncated law.')
 elif kind=='transform':
  X=lambda k:110+105*k
  out+=tx(45,35,z['operation'])+tx(45,72,'Original wait atoms; the last source represents all waits above four.')
  if z.get('from')is not None:out+=arrow(X(z['from']),130,X(z['to']),270)
  for k,v in enumerate(z['source']):
   out+=node(X(k),130,['1','2','3','4','>4'][k],'s'+str(k))+tx(X(k),100,fmt(v),'middle',True)
  for k,v in enumerate(z['destination']):
   out+=node(X(k),270,['0','1','2','3','4'][k],'d'+str(k),'#cee5d8')+tx(X(k),310,fmt(v),'middle',True)
  out+=tx(45,344,'Accumulated retained mass '+fmt(sum(z['destination']))+(' · normalized after filtering'if z['normalized']else' · completed recorded law'if z.get('complete')else' · partial recorded mass'),math=True)
 elif kind=='subsets':
  a=z['positions'];N=z['N'];w=600/N
  out+=tx(40,35,'Uniform marked-position subsets · each is a distinct possible ordering')
  for i in range(N):
   x=80+i*w;out+=f'<rect x="{x}" y="90" width="{w-10}" height="47" rx="4" fill="{"#d5e7d9"if i+1 in a else"#e8eff2"}" stroke="#7093a2"/>'+tx(x+(w-10)/2,119,i+1,'middle',True)
  out+=tx(40,175,'Subset '+str(z['processed'])+' of '+str(z['total'])+' · stopping position '+str(z['stop']),math=True)
  top=max([1]+z['counts']);xs=list(range(z['r'],z['N']-z['K']+z['r']+1));w=620/len(xs)
  for i,k in enumerate(xs):
   height=110*z['counts'][k]/top
   out+=f'<rect x="{65+i*w}" y="{305-height}" width="{w-15}" height="{height}" fill="#8cb9ad"/>'+tx(65+i*w+(w-15)/2,332,k,'middle',True)
  out+=tx(40,64,'Histogram is enumeration counts, not a single stochastic trajectory.')
 elif kind=='classification':
  a=z['law'];extent=z['n'];w=330/(extent+1);height=210/(extent+1);out+=tx(45,35,z['experiment'])+tx(440,100,('Poisson exposure step 'if z.get('poisson')else'Completed trials ')+str(z['step']))+tx(440,138,'Cell = (A count, B count)')+tx(440,176,'Displayed mass '+fmt(sum(v for _,_,v in a)),math=True)+tx(440,214,'Omitted tail '+fmt(z.get('tail',0)),math=True)
  for i in range(extent+1):
   for j in range(extent+1):
    x=70+i*w;y=75+(extent-j)*height;p=next((v for u,vv,v in a if u==i and vv==j),0)
    out+=f'<rect x="{x}" y="{y}" width="{w-5}" height="{height-5}" fill="{"#cee5d8"if p else"#f2f5f6"}" stroke="#b7cbd2"/>'+tx(x+(w-5)/2,y+(height-5)/2+5,fmt(p),'middle',True)
  for i in range(extent+1):out+=tx(70+i*w+(w-5)/2,308,i,'middle',True)+tx(54,75+(extent-i)*height+height/2+5,i,'end',True)
  out+=tx(440,263,'Horizontal A · vertical B')+tx(440,300,'Each cell is a joint probability.')
 elif kind=='uniform':
  xs=z['x'];ys=z['y'];w=600/len(xs)
  out+=tx(45,35,'Uniform atoms under an affine map · spacing belongs to the support')
  for i,(x,y)in enumerate(zip(xs,ys)):
   xx=85+i*w;out+=node(xx,105,x,'x'+str(i))+node(xx,260,y,'y'+str(i),'#cee5d8')
   if i<=z['cursor']:out+=arrow(xx,105,xx,260)
  out+=tx(45,66,'Map: '+str(z['a'])+'X + '+str(z['b'])+' · equal probability per image '+fmt(1/len(xs)),math=True)+tx(45,325,'Missing lattice values have zero probability; they are not hidden atoms.')
 else:
  a=z['law'];b=z.get('comparison');xs=[k for k,_ in a];count=len(a);w=620/count
  out+=tx(40,35,z['experiment'])+tx(40,66,z['detail'])
  for i,(k,p)in enumerate(a):
   width=(w-10)/2 if b else w-10;x=70+i*w;hi=190*float(p)
   out+=f'<rect x="{x}" y="{285-hi}" width="{width}" height="{hi}" fill="{"#b98634"if i==z.get("cursor")else"#8cb9ad"}" data-entity="mass-{k}"/>'+tx(x+(w-10)/2,309,k,'middle',True)
   if b:
    pp=dict(b).get(k,0);out+=f'<rect x="{x+width}" y="{285-190*pp}" width="{width}" height="{190*pp}" fill="#b7cfdd"/>'
  out+=f'<path d="M65 285H710M65 90V285" stroke="#658899" fill="none"/>'+tx(40,345,'Probabilities use fixed vertical scale 0 through 1 · '+z.get('footer',''),math=False)
 return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-label="'+h(z['action'])+'">'+out+'</svg>'

MODELS=[]
def add(id,title,spec,states,formula):
 frames=[]
 for i,z in enumerate(states):
  frames.append(dict(index=i,label=z['action'],caption=z['why'],duration=950,svg=svg(z),formula=formula,snapshot=dict(inputs=clean(spec),state=clean(z)),teaching=dict(currentState=z['action'],operation=z['action'],why=z['why'],reading='Read the declared parameters, probability scale and checkpoint meaning. Partial incoming mass or an enumeration histogram is explicitly labeled; it is not silently normalized.',checks=[dict(mathHtml='The displayed checkpoint is the final one',result=str(i==len(states)-1).lower())])))
 MODELS.append(dict(id=id,title=title,spec=clean(spec),invariant='This is an exact probability-law mechanism with declared sample inputs, not a random demonstration or a universal proof. Finite displays retain or label unresolved tail mass.',frames=frames))
def flow(id,ps,kind='independent',N=None,K=None):
 n=len(ps);src=[F(1)];states=[]
 for t,p in enumerate(ps,1):
  dst=[F(0)]*(t+1)
  def emit(action,why,**kw):states.append(dict(kind='flow',n=n,step=t,source=src+[F(0)]*(n+1-len(src)),destination=dst+[F(0)]*(n+1-len(dst)),transferred=kw.pop('transferred',0),experiment='Without-replacement depletion'if kind=='hyper'else'Independent count dynamic programming',action=action,why=why,**kw))
  emit('Prepare destination for draw '+str(t),'Keep the previous normalized law fixed while receiving its branches.')
  for k,mass in enumerate(src):
   prob=F(K-k,N-t+1)if kind=='hyper'else p
   if not mass:continue
   for target,factor in[(k,1-prob),(k+1,prob)]:
    if not factor:continue
    v=mass*factor;dst[target]+=v
    emit('Transfer '+('success'if target>k else'failure')+' mass from count '+str(k),'Multiply the source mass by the conditional branch probability. In depletion, the remaining population depends on the count and draw index.',**{'from':k,'to':target,'transferred':v,'branchProbability':prob if target>k else 1-prob})
  src=dst
 add(id,('Marked draws: N='+str(N)+', K='+str(K)+', n='+str(n))if kind=='hyper'else'Count propagation with probabilities '+', '.join(fmt(p)for p in ps),dict(kind=kind,probabilities=ps,N=N,K=K,n=n),states,r'P_{t+1}(k)=P_t(k)(1-p_{t+1})+P_t(k-1)p_{t+1}'if kind!='hyper'else r'P(B_{t+1}=1\mid S_t=k)=(K-k)/(N-t)')
def wait(id,r,p,steps):
 m=[F(1)]+[F(0)]*r;states=[]
 for t in range(steps+1):
  newFinish=0 if t==0 else old[r-1]*p
  states.append(dict(kind='wait',r=r,mass=m.copy(),step=t,newFinish=newFinish,action='After '+str(t)+' trials',why='Unfinished mass moves according to failure and success. Already finished mass remains absorbed; no later outcome changes the stopping time.'))
  old=m.copy();m=[F(0)]*(r+1);m[r]=old[r]
  for k in range(r):m[k]+=old[k]*(1-p);m[k+1]+=old[k]*p
 add(id,'Absorbing wait: '+str(r)+' successes, p='+fmt(p)+', horizon '+str(steps),dict(kind='wait',r=r,p=p,steps=steps),states,r'P(T_r\le t)=P(S_t\ge r)')
def masses(id,title,law,detail='',footer='',comparison=None,parameters=None):
 states=[]
 for i,(k,p)in enumerate(law):
  states.append(dict(kind='pmf',law=law,comparison=comparison,cursor=i,experiment=title,detail=detail,footer=footer,action='Inspect count '+str(k),why='The full displayed law stays fixed; the highlighted atom checks its adjacent-ratio or support interpretation. Omitted tail mass is labeled explicitly.'))
 add(id,title,parameters or dict(kind='pmf',law=law),states,r'P(X=k+1)/P(X=k)=\lambda/(k+1)'if 'Poisson'in title else r'\sum_k P(X=k)=1')
def finite(id,N,K,r):
 subsets=list(combinations(range(1,N+1),K));counts=[0]*(N+1);states=[]
 for i,a in enumerate(subsets,1):
  stop=a[r-1];counts[stop]+=1;states.append(dict(kind='subsets',positions=a,N=N,K=K,r=r,counts=counts.copy(),processed=i,total=len(subsets),stop=stop,action='Enumerate marked positions '+','.join(map(str,a)),why='Each mark-position subset has equal probability. The rth marked position increments the appropriate histogram cell; intermediate counts represent only processed outcomes.'))
 add(id,'Finite wait: N='+str(N)+', K='+str(K)+', r='+str(r),dict(kind='subsets',N=N,K=K,r=r),states,r'P(T_r=t)=\binom{t-1}{r-1}\binom{N-t}{K-r}/\binom NK')
flow('binomial-eight',[F(1,2)]*8)
flow('binomial-thinning',[F(1,3)]*6)
flow('heterogeneous',[F(1,2),F(1,3),F(1,4)])
flow('hypergeometric-small',[0]*3,'hyper',10,4)
flow('hypergeometric-dense',[0]*5,'hyper',8,6)
wait('geometric-six',1,F(1,6),8)
wait('negative-two',2,F(1,4),8)
wait('negative-convolution',5,F(1,2),8)
for kind in ['censored','truncated','failure-code']:
 source=[F(1,2),F(1,4),F(1,8),F(1,16),F(1,16)];dest=[F(0)]*5;states=[]
 for i,mass in enumerate(source):
  target=4 if kind=='censored'and i==4 else 0 if kind=='failure-code'and i==4 else i+1
  if kind=='truncated'and i==4:continue
  dest[target]+=mass
  states.append(dict(kind='transform',source=source,destination=dest.copy(),normalized=False,operation=kind+' observation at horizon four',**{'from':i,'to':target},action='Map original waiting atom '+(['1','2','3','4','>4'][i])+' to recorded value '+str(target),why='Filtering retains a subprobability law until normalization.'if kind=='truncated'else'Preserve the original probability mass and move it to the value specified by the recording map. No outcomes are discarded.'))
 if kind=='truncated':
  total=sum(dest);dest=[p/total for p in dest];states.append(dict(kind='transform',source=source,destination=dest.copy(),normalized=True,operation='Normalize successful records by 15/16',action='Normalize the retained outcomes',why='Discarded attempts are absent from the recorded population; dividing by the retained probability completes its law.'))
 states[-1]['complete']=True
 add(kind,kind.capitalize()+': positive geometric p=1/2, horizon four',dict(kind=kind,p=F(1,2),horizon=4),states,r'P(T=t\mid T\le c)=P(T=t)/P(T\le c)'if kind=='truncated'else r'C=\min(T,c)'if kind=='censored'else r'R=T1_{\{T\le c\}}')
finite('finite-wait',7,3,2);finite('finite-one-mark',6,1,1)
law={(0,0):F(1)};states=[]
for t in range(5):
 states.append(dict(kind='classification',n=4,step=t,law=[(a,b,v)for(a,b),v in law.items()],experiment='Four competing-label trials: A=1/4, B=1/2, neither=1/4',action='Joint counts after '+str(t)+' trials',why='Each trial adds one A, one B or neither. Joint convolution preserves the triangular feasible support and the normalization.'))
 nxt={}
 for(a,b),v in law.items():
  for da,db,p in[(1,0,F(1,4)),(0,1,F(1,2)),(0,0,F(1,4))]:nxt[(a+da,b+db)]=nxt.get((a+da,b+db),0)+v*p
 law=nxt
add('classification','Competing label joint-count grid',dict(kind='classification',n=4,a=F(1,4),b=F(1,2)),states,r'Cov(A,B)=-nab')
states=[]
for step in range(4):
 a=step/3;b=2*step/3;law=[(i,j,exp(-a-b)*a**i*b**j/(factorial(i)*factorial(j)))for i in range(5)for j in range(5)]
 states.append(dict(kind='classification',n=4,step=step,law=law,poisson=True,tail=1-sum(p for i,j,p in law),experiment='Independent Poisson labeling · category means t/3 and 2t/3',action='Increase expected total count to '+str(step),why='The joint PGF factors into independent Poisson category laws. The visible grid includes counts zero through four and labels the probability outside that grid.'))
add('poisson-splitting','Poisson splitting: independent joint-count grid',dict(kind='poisson-splitting',probability=F(1,3),exposures=[0,1,2,3],limit=4),states,r'G_{A,B}(z,w)=\exp(\lambda a(z-1))\exp(\lambda(1-a)(w-1))')
for id,lam in [('poisson-one',1),('poisson-mode',3),('poisson-small-interval',F(1,10))]:
 law=[(k,exp(-float(lam))*float(lam)**k/factorial(k))for k in range(9)];tail=1-sum(p for k,p in law)
 masses(id,'Poisson parameter '+fmt(lam),law,'Highlight each mass; adjacent ratios locate the modes.','Tail beyond eight = '+fmt(tail),parameters=dict(kind='poisson',lam=lam,limit=8))
law=[(k,F(comb(4,k))*F(2,5)**k*F(3,5)**(4-k))for k in range(5)]
masses('poisson-conditional','Conditional Poisson allocation: total four, proportion 2/5',law,'Conditional count is binomial; the original counts were independent.',parameters=dict(kind='binomial',n=4,p=F(2,5)))
for id,ps in [('latent-count',[F(1,4),F(3,4)])]:
 law=[(k,sum(F(comb(6,k))*p**k*(1-p)**(6-k)for p in ps)/2)for k in range(7)]
 masses(id,'Shared latent binomial count: six trials',law,'One parameter is chosen per experiment, not afresh per trial.',parameters=dict(kind='latent-binomial',n=6,ps=ps))
law=[(k,(exp(-1)+exp(-3)*3**k)/factorial(k)/2)for k in range(9)]
masses('mixed-poisson','Mixed Poisson parameters one and three',law,'Equal prior weights; mean two, variance three.','Tail beyond eight = '+fmt(1-sum(p for k,p in law)),parameters=dict(kind='mixed-poisson',parameters=[1,3],limit=8))
law=[(k,F(3,4)*F(1,4)**k)for k in range(9)]
masses('family-posterior','Posterior family-size count after no boys',law,'Prior weights times observation likelihood; include the zero-size case.','Tail beyond eight = '+fmt(F(1,4)**9),parameters=dict(kind='geometric-failures',p=F(3,4),limit=8))
states=[]
for n in [2,4,8,16,32,64,128]:
 lam=1;law=[(k,comb(n,k)*(1/n)**k*(1-1/n)**(n-k)if k<=n else 0)for k in range(9)];other=[(k,exp(-1)/factorial(k))for k in range(9)]
 states.append(dict(kind='pmf',law=law,comparison=other,cursor=-1,experiment='Binomial rare-count limit · lambda fixed at one',detail='Green Bin('+str(n)+',1/'+str(n)+') · blue Pois(1)',footer='Omitted tails: '+fmt(1-sum(p for k,p in law))+' and '+fmt(1-sum(p for k,p in other)),n=n,bound=1/n,action='Increase n to '+str(n),why='Keep the expected count fixed while decreasing each success probability. Both laws use a fixed probability scale; the finite and infinite supports remain distinct.'))
add('poisson-approximation','Rare-count limit with an explicit absolute bound',dict(kind='approximation',lam=1,ns=[2,4,8,16,32,64,128]),states,r'\operatorname{sup}_A|P(S_n\in A)-P(Pois(1)\in A)|\le1/n')
law=[(k,F(comb(5,k)*comb(7,5-k),comb(12,5)))for k in range(6)]
masses('hypergeometric-mode','Hypergeometric mode: N=12, K=5, n=5',law,'The neighboring ratio changes from above to below one at mode two.',parameters=dict(kind='hypergeometric',N=12,K=5,n=5))
states=[]
for m in range(7):
 q1=F(2,3);q2=F(1,2)
 states.append(dict(kind='pmf',law=[(0,1-q1**m),(1,1-q2**m),(2,1-(q1*q2)**m),(3,(1-q1**m)*(1-q2**m))],cursor=-1,experiment='Independent clocks: first, second, minimum and maximum CDFs',detail='Clock parameters 1/3 and 1/2 · elapsed trials '+str(m),footer='Bars are four CDF values, not masses of a single law.',step=m,action='Compare completion by trial '+str(m),why='The minimum completes if either clock completes; the maximum needs both. Independence gives the product of survival or completion probabilities.'))
add('race','Two-clock completion and discrete ties',dict(kind='race',p1=F(1,3),p2=F(1,2)),states,r'P(T_1=T_2)=p_1p_2/(1-q_1q_2)')
states=[dict(kind='uniform',x=list(range(1,6)),y=list(range(-1,8,2)),a=2,b=-3,cursor=i,action='Map atom '+str(i+1),why='Each source atom maps to exactly one image with its original mass. The affine scale changes the lattice spacing, not the atom weights.')for i in range(5)]
add('uniform-lattice','Uniform lattice under Y = 2X - 3',dict(kind='uniform',m=5,a=2,b=-3),states,r'E[aX+b]=aE[X]+b,\quad Var(aX+b)=a^2Var(X)')
groups=dict(binomial=['binomial-eight','binomial-thinning'],splitting=['classification','poisson-conditional','poisson-splitting'],heterogeneous=['heterogeneous','latent-count'],geometric=['geometric-six','race'],censoring=['censored','truncated','failure-code'],negative=['negative-two','negative-convolution'],hypergeometric=['hypergeometric-small','hypergeometric-dense','hypergeometric-mode'],**{'finite-wait':['finite-wait','finite-one-mark']},poisson=['poisson-one','poisson-mode','poisson-small-interval','mixed-poisson'],approximation=['poisson-approximation'],uniform=['uniform-lattice'])
save(R/'dist/chapters/s_distributions-models.json',dict(models=clean(MODELS),groups=groups))
save(E/'model-specs.json',[dict(id=m['id'],spec=m['spec'])for m in MODELS])
auth=json.loads((B/'s_discrete-authentic.json').read_text(encoding='utf-8'))
for a in auth:
 a.update(topics=['s_distributions'],revisited=True,verification='Original PDF visually rechecked for this chapter, including the family-size base-two prior. Previously delivered item revisited for deeper named-law reasoning.',modelId={'MS_CE_1405_Q35':'binomial-thinning','Phd_CS_1404_Q68':'poisson-approximation','Phd_CS_1404_Q69':'family-posterior'}[a['id']])
save(B/'s_distributions-authentic.json',auth)
save(E/'reading.json',dict(status='reviewed_written_sources',candidateUniversities=9,coreUniversities=['Oxford','Cambridge','Berkeley','MIT'],additionalUniversities=['Stanford'],readRanges=dict(Oxford='Native PDF18–26 and39–44',Cambridge='All23 native pages',Berkeley='All8 pages',MIT='Native combined PDF34–51; reread42–43 untruncated',Stanford='All66 textual slides, including progressive duplicates'),limitations='Four more candidate universities screened; no exhaustive-global or all-materials-read claim.'))
save(E/'problem-visual-decisions.json',[dict(id=q['id'],model=q.get('modelId'),reason=q['visualDecision'])for q in json.loads((B/'s_distributions-questions.json').read_text(encoding='utf-8'))])
print('Prepared',len(MODELS),'mechanism-specific models /',sum(len(m['frames'])for m in MODELS),'checkpoints.')
