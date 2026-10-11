"""Generate exact finite-law checkpoints and compact subject-specific SVGs."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
from math import comb,sqrt
from html import escape
import json
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_variance-evidence'
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def numeric(x):
 if isinstance(x,F):return float(x)
 if isinstance(x,dict):return{k:numeric(v)for k,v in x.items()}
 if isinstance(x,list):return[numeric(v)for v in x]
 return x
def n(x):return str(round(float(x),5)).removesuffix('.0')
def text(x,y,t,anchor='start',math=False):return f'<text x="{x}" y="{y}" class="sv-{"math"if math else"prose"}" text-anchor="{anchor}">{escape(str(t))}</text>'
def line(x1,y1,x2,y2,gold=False,dash=False):return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{"#b98634"if gold else"#7195a5"}" stroke-width="1.5"'+(' stroke-dasharray="5 4"'if dash else'')+'/>'
def dot(id,x,y,r=7,color='#b98634'):return f'<g data-entity="{id}"><circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="#315b6f"/></g>'
def moments(a):
 mu=sum((p['p']*p['x']for p in a),F(0));m2=sum((p['p']*p['x']**2 for p in a),F(0));v=sum((p['p']*(p['x']-mu)**2 for p in a),F(0));return dict(mean=mu,second=m2,variance=v)
def drawing(z):
 kind=z['kind'];out=''
 if kind=='walk':
  limit=max(1,z['limit']);X=lambda v:80+600*(v+limit)/(2*limit);source=z['source'];dest=z['destination'];out=text(45,35,'Exact mass propagation · probabilities rounded to three decimals')
  out+=text(45,63,'Source law',math=False)+text(45,190,'Incoming mass',math=False)
  out+='<defs><marker id="walk-arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#b98634"/></marker></defs>'
  if z.get('from')is not None:
   x1=X(z['from']);x2=X(z['to']);y1=115;y2=235;distance=sqrt((x2-x1)**2+(y2-y1)**2);dx=(x2-x1)/distance;dy=(y2-y1)/distance
   out+=f'<path d="M{x1+16*dx} {y1+16*dy}L{x2-16*dx} {y2-16*dy}" fill="none" stroke="#b98634" stroke-width="2" marker-end="url(#walk-arrow)" data-route="mass-transfer"/>'
  for row,y in[(source,115),(dest,235)]:
   for p in row:
    x=X(p['x']);active=p['x']==z.get('from')if y==115 else p['x']==z.get('to');out+=f'<circle cx="{x}" cy="{y}" r="16" fill="{"#ffe4ad"if active else"#e1eef1"}" stroke="#7195a5"/>'+text(x,y+5,p['x'],'middle',True)+text(x,y-27 if y==115 else y+35,str(round(float(p['p']),3)),'middle',True)
  out+=text(70,303,'Completed source steps '+str(z['sourceStep'])+' · target step '+str(z['targetStep'])+' · incoming mass '+n(sum(p['p']for p in dest)),math=True)
  out+=text(70,334,('Completed target mean '+n(z['mean'])+' · variance '+n(z['variance']))if z['complete']else'Partial incoming mass is not a normalized probability law.',math=True)
 elif kind in['moments','sampling']:
  a=z['points'];top=max([p['p']for p in a]+[.01]);w=620/len(a);out=text(70,40,'Probability mass · vertical scale follows current maximum')+line(70,260,700,260)
  for i,p in enumerate(a):
   x=80+i*w;h=170*float(p['p'])/float(top);tail=z.get('tail');istail=tail and(p['x']>=tail['threshold']if tail['side']=='one'else abs(p['x']-z['mean'])>=tail['threshold']);color='#dbad95'if istail else '#8cb9ad'if i<=z.get('cursor',-1)else'#b9d2dd'
   out+=f'<rect x="{x}" y="{260-h}" width="{w-20}" height="{h}" fill="{color}" stroke="#537688"/>'+text(x+(w-20)/2,285,n(p['x']),'middle',True)
  if kind=='moments':
   out+=text(70,320,'Weighted squared displacement so far: '+n(z['accumulated']),math=True)+text(70,345,'Center '+n(z['center'])+' · population mean '+n(z['mean']),math=True)
   if z['cursor']>=0:
    p=a[z['cursor']];out+=text(70,65,'Atom '+n(p['x'])+' · probability '+n(p['p'])+' · weighted square '+n(z['terms'][z['cursor']]),math=True)
  else:out+=text(70,320,'Mean '+n(z['mean'])+' · variance '+n(z['variance']),math=True)+text(70,345,('Draws '+str(z['n'])+' of '+str(z['N'])+' without replacement')if kind=='sampling'else'Steps '+str(z['step'])+' · right-step probability '+n(z['rightProbability']),math=True)
 elif kind=='joint':
  a=z['points'];lo=min(p['x']for p in a)-1;hi=max(p['x']for p in a)+1;low=min(p['y']for p in a)-1;high=max(p['y']for p in a)+1;X=lambda v:75+330*float(v-lo)/float(hi-lo);Y=lambda v:260-175*float(v-low)/float(high-low)
  out=text(70,40,'Joint outcomes · marker area follows probability')+line(65,270,425,270)+line(65,75,65,270)+line(X(z['meanX']),75,X(z['meanX']),270,True,True)+line(65,Y(z['meanY']),425,Y(z['meanY']),True,True)
  if z['cursor']>=0:
   p=a[z['cursor']];x=min(X(p['x']),X(z['meanX']));y=min(Y(p['y']),Y(z['meanY']));out+=f'<rect x="{x}" y="{y}" width="{abs(X(p["x"])-X(z["meanX"]))}" height="{abs(Y(p["y"])-Y(z["meanY"]))}" fill="{"#cee5d8"if z["terms"][z["cursor"]]>=0 else"#efd8cb"}" opacity=".7"/>'
  grouped={}
  for p in a:grouped[(p['x'],p['y'])]=grouped.get((p['x'],p['y']),0)+p['p']
  active=(a[z['cursor']]['x'],a[z['cursor']]['y'])if z['cursor']>=0 else None
  for i,((px,py),prob)in enumerate(grouped.items()):
   if prob>0:out+=dot('joint-'+str(i),X(px),Y(py),sqrt(float(prob))*23,'#b98634'if (px,py)==active else'#578c9d')
  out+=text(X(lo+1),285,n(lo+1),'middle',True)+text(X(hi-1),285,n(hi-1),'middle',True)+text(52,Y(low+1)+5,n(low+1),'end',True)+text(52,Y(high-1)+5,n(high-1),'end',True)
  out+=text(245,311,'X coordinate','middle')+text(32,65,'Y',math=True)+text(470,78,'Centered contribution ledger')+line(475,180,715,180);top=max([abs(t)for t in z['terms']]+[.01]);w=230/len(a)
  for i,t in enumerate(z['terms']):
   if i<=z['cursor']:
    h=65*float(abs(t))/float(top);out+=f'<rect x="{480+i*w}" y="{180-h if t>=0 else 180}" width="{max(5,w-8)}" height="{h}" fill="{"#8cb9ad"if t>=0 else"#dbad95"}"/>'
  out+=text(470,280,'Sum '+n(z['accumulated']),math=True)+text(70,335,'Means ('+n(z['meanX'])+', '+n(z['meanY'])+') · gold lines mark the centers',math=True)
 elif kind=='mixture':
  a=z['groups'];lo=min([g['mean']-sqrt(float(g['variance']))for g in a]+[z['mean']])-1;hi=max([g['mean']+sqrt(float(g['variance']))for g in a]+[z['mean']])+1;X=lambda v:100+340*float(v-lo)/float(hi-lo);out=text(40,38,'Group means and one-SD intervals')+text(490,38,'Variance decomposition')
  for i,g in enumerate(a):
   y=95+i*65;out+=text(35,y+6,'G'+str(i),math=True)+line(X(g['mean']-sqrt(float(g['variance']))),y,X(g['mean']+sqrt(float(g['variance']))),y,i==z['cursor'])+dot('group-'+str(i),X(g['mean']),y,color='#b98634'if i==z['cursor']else'#578c9d')+text(100,y+27,'Weight '+n(g['p'])+' · mean '+n(g['mean'])+' · variance '+n(g['variance']),math=True)
  out+=line(X(z['mean']),65,X(z['mean']),270,True,True)+text(90,305,'Global mean '+n(z['mean']),math=True);top=max(float(z['within']+z['between']),.01)
  for i,(name,v,color)in enumerate([('Within',z['partialWithin'],'#8cb9ad'),('Between',z['partialBetween'],'#dbad95')]):
   y=105+i*95;out+=text(490,y-16,name+' = '+n(v),math=True)+f'<rect x="490" y="{y}" width="{210*float(v)/top}" height="25" fill="{color}"/>'
  out+=text(490,295,'Accumulated total')+text(490,321,n(z['partialWithin']+z['partialBetween']),math=True)
 elif kind in['quadratic','projection']:
  a=z['curve'];lo=min([0]+[p['y']for p in a])-1;hi=max([1]+[p['y']for p in a])+1;X=lambda v:335+365*float(v+2)/5;Y=lambda v:265-185*float(v-lo)/float(hi-lo);M=z['matrix'];out=text(35,40,'Covariance candidate')+text(335,40,'Squared prediction risk'if kind=='projection'else'Variance quadratic form')
  for i,row in enumerate(M):
   for j,v in enumerate(row):
    x=40+j*70;y=90+i*58;out+=f'<rect x="{x}" y="{y}" width="62" height="46" rx="5" fill="{"#d5e7e4"if i==j else"#e8eff2"}" stroke="#8ca8b2"/>'+text(x+31,y+29,n(v),'middle',True)
  out+=line(330,Y(0),710,Y(0))+line(330,70,330,270)+f'<polyline points="{" ".join(str(X(p["x"]))+","+str(Y(p["y"]))for p in a)}" fill="none" stroke="#578c9d" stroke-width="2.5"/>'+dot('risk-point',X(z['weight']),Y(z['variance']))+text(335,297,'Coefficient '+n(z['weight']),math=True)+text(335,325,'Current value '+n(z['variance']),math=True)+text(40,315,'Coefficients '+', '.join(n(c)for c in z['coefficients']),math=True)
 elif kind=='averaging':
  a=z['curve'];X=lambda v:80+600*(v-1)/max(1,len(a)-1);top=max([1]+[p['y']for p in a]);Y=lambda v:255-170*float(v)/float(top);out=text(70,40,'Mean variance · reference curve from declared covariance')+line(70,270,710,270)+f'<polyline points="{" ".join(str(X(p["x"]))+","+str(Y(p["y"]))for p in a)}" fill="none" stroke="#578c9d" stroke-width="2.5"/>'+dot('mean-risk',X(z['n']),Y(z['variance']))
  for p in a:out+=text(X(p['x']),295,p['x'],'middle',True)
  out+=text(70,330,'Diagonal '+n(z['diagonal'])+' + cross '+n(z['cross'])+' = '+n(z['variance']),math=True)
 elif kind=='permutations':
  w=600/z['n'];out=text(70,40,'Uniform permutations · enumerate separate possible outcomes')+text(70,73,'Permutation '+str(z['processed'])+' of '+str(z['total']))
  for i,v in enumerate(z['permutation']):
   x=80+i*w;out+=f'<rect x="{x}" y="125" width="{w-20}" height="60" rx="5" fill="{"#cee5d8"if v==i+1 else"#e4edf1"}" stroke="#7195a5"/>'+text(x+(w-20)/2,162,v,'middle',True)+text(x+(w-20)/2,220,'Position '+str(i+1),'middle',True)
  out+=text(70,265,'Fixed points '+str(z['fixed']),math=True)+text(70,305,'Weighted mean so far '+n(z['partialMean']),math=True)+text(70,335,'Weighted second moment so far '+n(z['partialSecond']),math=True)
 return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-label="'+escape(z['action'])+'">'+out+'</svg>'

def evaluate(s):
 states=[];kind=s['kind']
 def emit(action,why,**z):states.append(dict(kind=kind,action=action,why=why,**z))
 if kind=='moments':
  a=s['points'];m=moments(a);center=s.get('center',m['mean']);terms=[p['p']*(p['x']-center)**2 for p in a];acc=F(0);base=dict(points=a,center=center,terms=terms,tail=s.get('tail'),**m)
  emit('Identify the center','The law is fixed. A partial weighted sum is not yet a full variance or prediction error.',cursor=-1,accumulated=acc,**base)
  for i,p in enumerate(a):
   acc+=terms[i];emit('Add atom '+str(i),'Multiply the squared displacement by this probability, then add it to the partial ledger.',cursor=i,accumulated=acc,**base)
  result=dict(**m,center=center,squaredError=sum(terms),tail=sum(p['p']for p in a if(p['x']>=s['tail']['threshold']if s['tail']['side']=='one'else abs(p['x']-m['mean'])>=s['tail']['threshold']))if s.get('tail')else None)
 elif kind=='joint':
  a=s['points'];x=moments(a);y=moments([dict(x=p['y'],p=p['p'])for p in a]);terms=[p['p']*(p['x']-x['mean'])*(p['y']-y['mean'])for p in a];acc=F(0);base=dict(points=a,meanX=x['mean'],meanY=y['mean'],varX=x['variance'],varY=y['variance'],terms=terms)
  emit('Center both coordinates','Scatter locations and probabilities remain fixed; centered products can be signed.',cursor=-1,accumulated=acc,**base)
  for i,p in enumerate(a):acc+=terms[i];emit('Add joint atom '+str(i),'Weight the product of its centered coordinates; the rectangle shows their signs and magnitudes.',cursor=i,accumulated=acc,**base)
  result=dict(meanX=x['mean'],meanY=y['mean'],varX=x['variance'],varY=y['variance'],covariance=sum(terms),mixed=sum(p['p']*p['x']*p['y']for p in a),correlation=float(sum(terms))/sqrt(float(x['variance']*y['variance']))if x['variance']*y['variance']>0 else None)
 elif kind=='mixture':
  gs=s['groups'];mu=sum(g['p']*g['mean']for g in gs);wi=sum(g['p']*g['variance']for g in gs);be=sum(g['p']*(g['mean']-mu)**2 for g in gs);pw=pb=F(0);base=dict(groups=gs,mean=mu,within=wi,between=be)
  emit('Choose the global center','Each horizontal interval is one standard deviation around its group mean, not the complete support.',cursor=-1,partialWithin=pw,partialBetween=pb,**base)
  for i,g in enumerate(gs):pw+=g['p']*g['variance'];pb+=g['p']*(g['mean']-mu)**2;emit('Account for group '+str(i),'Add both its weighted conditional variance and its weighted squared mean displacement.',cursor=i,partialWithin=pw,partialBetween=pb,**base)
  result=dict(mean=mu,within=wi,between=be,variance=wi+be)
 elif kind=='sampling':
  N,K=s['N'],s['K'];p=F(K,N)
  for count in range(s['draws']+1):
   def C(a,b):return comb(a,b)if 0<=b<=a else 0
   a=[dict(x=k,p=F(C(K,k)*C(N-K,count-k),C(N,count)))for k in range(count+1)]
   emit('Sample size '+str(count),'This is the full without-replacement success-count law, including zero-mass impossible counts.',points=a,n=count,N=N,K=K,covariance=-p*(1-p)/(N-1),**moments(a))
  result=moments(a)
 elif kind=='walk':
  p=s['p'];a=[dict(x=0,p=F(1))]
  emit('Zero steps','The initial distribution has all mass at the origin. The two rows show its initial source and result.',points=a,source=a,destination=a,sourceStep=0,targetStep=0,step=0,limit=s['steps'],complete=True,rightProbability=p,**moments(a))
  for step in range(1,s['steps']+1):
   source=a;dest={};base=dict(points=source,source=source,sourceStep=step-1,targetStep=step,step=step-1,limit=s['steps'],rightProbability=p,**moments(source))
   emit('Begin ensemble step '+str(step),'The destination row starts with no incoming mass. Keep the source distribution unchanged while splitting it.',destination=[],complete=False,**base)
   for atom in a:
    for value,weight in[(atom['x']-1,1-p),(atom['x']+1,p)]:
     sent=atom['p']*weight;dest[value]=dest.get(value,F(0))+sent
     state=dict(base);state['from']=atom['x'];state['to']=value;state['sent']=sent
     emit('Send '+n(sent)+' from '+str(atom['x'])+' to '+str(value),'Multiply the source mass by the branch probability. Add the result to any mass already arriving at this destination.',destination=[dict(x=x,p=w)for x,w in sorted(dest.items())],complete=False,**state)
   a=[dict(x=x,p=w)for x,w in sorted(dest.items())]
   emit('Complete ensemble step '+str(step),'All source atoms have sent both branches. Incoming mass now sums to one, so its moments describe a completed probability law.',points=a,source=source,destination=a,sourceStep=step-1,targetStep=step,step=step,limit=s['steps'],complete=True,rightProbability=p,**moments(a))
  result=moments(a)
 elif kind=='permutations':
  all=list(permutations(range(1,s['n']+1)));mu=m2=F(0)
  for i,a in enumerate(all):
   fixed=sum(v==j+1 for j,v in enumerate(a));mu+=F(fixed,len(all));m2+=F(fixed**2,len(all));emit('Inspect permutation '+str(i+1),'A fixed point matches its positional label. These are distinct possible arrangements, not an asserted swapping algorithm.',permutation=list(a),fixed=fixed,processed=i+1,total=len(all),partialMean=mu,partialSecond=m2,n=s['n'])
  result=dict(mean=mu,second=m2,variance=m2-mu**2,total=len(all))
 elif kind=='averaging':
  v,c=s['matrix'][0];curve=[dict(x=i,y=F(v,i)+F((i-1)*c,i))for i in range(1,s['count']+1)]
  for p in curve:emit('Average '+str(p['x'])+' observations','Divide the diagonal and all ordered covariance contributions by squared sample size.',curve=curve,n=p['x'],variance=p['y'],diagonal=F(v,p['x']),cross=F((p['x']-1)*c,p['x']),matrix=s['matrix'])
  result=dict(variance=curve[-1]['y'])
 else:
  M=s['matrix']
  def coeff(w):return[1,-w]if kind=='projection'else[1,w,1]if len(M)==3 else[w,s.get('fixed',-2)]
  def risk(w):
   c=coeff(w);return sum(c[i]*c[j]*M[i][j]for i in range(len(c))for j in range(len(c)))
  curve=[dict(x=F(-2)+F(5*i,80),y=risk(F(-2)+F(5*i,80)))for i in range(81)]
  for w in s['weights']:emit(('Predictor slope 'if kind=='projection'else'Coefficient ')+n(w),'The gold point follows the exact risk quadratic; a negative proposed variance rejects the candidate matrix.',curve=curve,weight=w,variance=risk(w),matrix=M,coefficients=coeff(w))
  result=dict(variance=states[-1]['variance'],matrix=M)
 return states,result
specs=[]
def model(id,title,**s):specs.append(dict(id=id,title=title,spec=s))
def atoms(xs,ps,ys=None):return[dict(x=x,p=F(p),**(dict(y=ys[i])if ys is not None else{}))for i,(x,p)in enumerate(zip(xs,ps))]
model('weighted-three','Values 1,3,5 with masses 1/4,1/4,1/2',kind='moments',points=atoms([1,3,5],[F(1,4),F(1,4),F(1,2)]))
model('center-shift','Squared error about 7: values 8,12 with equal masses',kind='moments',points=atoms([8,12],[F(1,2)]*2),center=7)
model('joint-positive','Fair binary marginals: joint masses 1/3,1/6,1/6,1/3',kind='joint',points=atoms([0,0,1,1],[F(1,3),F(1,6),F(1,6),F(1,3)],[0,1,0,1]))
model('bernoulli-opposite','A fair indicator and its complement',kind='joint',points=atoms([0,1],[F(1,2)]*2,[1,0]))
model('overlap','Shared middle toss in two fair two-toss counts',kind='joint',points=atoms([0,0,1,1,1,1,2,2],[F(1,8)]*8,[0,1,1,2,0,1,1,2]))
model('parabola','X uniform on -1,0,1; Y = X squared',kind='joint',points=atoms([-1,0,1],[F(1,3)]*3,[1,0,1]))
model('without-replacement','Three draws from ten entries with four successes',kind='sampling',N=10,K=4,draws=3)
model('fixed-points','All six permutations of three labels',kind='permutations',n=3)
model('empty-boxes','Empty-box count for three balls and two boxes',kind='moments',points=atoms([0,1],[F(3,4),F(1,4)]))
model('two-group','Group weights 1/4,3/4; means 0,4; variances 1,9',kind='mixture',groups=[dict(p=F(1,4),mean=0,variance=1),dict(p=F(3,4),mean=4,variance=9)])
model('latent-bernoulli','Exact one-outcome marginal under a uniform latent probability',kind='moments',points=atoms([0,1],[F(1,2)]*2))
model('latent-pair','Two conditionally independent Bernoulli outcomes sharing uniform P',kind='joint',points=atoms([0,0,1,1],[F(1,3),F(1,6),F(1,6),F(1,3)],[0,1,0,1]))
model('heteroscedastic','Equal zero-mean groups with variances one and four',kind='mixture',groups=[dict(p=F(1,2),mean=0,variance=1),dict(p=F(1,2),mean=0,variance=4)])
model('cancel-covariance','Overall zero covariance: equal means 0,2 and opposite residuals',kind='joint',points=atoms([-1,1,1,3],[F(1,4)]*4,[1,-1,3,1]))
model('quadratic-weight','Covariance matrix [[4,1],[1,2]]; coefficient vector (w,-2)',kind='quadratic',matrix=[[4,1],[1,2]],weights=[-2,-1,0,F(1,2),1,2,3])
model('psd-failure','Rejected matrix: diagonals one, off-diagonals -3/4',kind='quadratic',matrix=[[1,F(-3,4),F(-3,4)],[F(-3,4),1,F(-3,4)],[F(-3,4),F(-3,4),1]],weights=[-2,-1,0,1,2,3])
model('linear-projection','Predict X by bY: variances 16,9 and covariance six',kind='projection',matrix=[[16,6],[6,9]],weights=[0,F(1,3),F(2,3),1,F(4,3),2,3])
model('averaging','Common variance nine and pair covariance three, n = 1 through 8',kind='averaging',matrix=[[9,3],[3,9]],count=8)
model('same-versus-independent','Independent mean-variance curve: variance five, n = 1 through 8',kind='averaging',matrix=[[5,0],[0,5]],count=8)
model('chebyshev','Mean zero, variance one: mass 1/8 at -2,+2, 3/4 at zero',kind='moments',points=atoms([-2,0,2],[F(1,8),F(3,4),F(1,8)]),tail=dict(side='two',threshold=2))
model('cantelli','Mean zero, variance four: masses 9/13 at -4/3 and 4/13 at 3',kind='moments',points=atoms([F(-4,3),3],[F(9,13),F(4,13)]),tail=dict(side='one',threshold=3))
model('walk-two','Exact fair-sign ensemble from zero through two steps',kind='walk',steps=2,p=F(1,2))
model('walk-biased','Exact six-step ensemble with right-step probability 3/4',kind='walk',steps=6,p=F(3,4))
models=[]
for item in specs:
 states,result=evaluate(item['spec']);frames=[]
 for i,z in enumerate(states):
  formula=r'Cov(X,Y)=E[XY]-E[X]E[Y]'if z['kind']=='joint'else r'Var(X)=E[Var(X\mid Z)]+Var(E[X\mid Z])'if z['kind']=='mixture'else r'Var(X-bY)=Var(X)-2bCov(X,Y)+b^2Var(Y)'if z['kind']=='projection'else r'Var(a^T X)=a^T\Sigma a'if z['kind']=='quadratic'else r'Var(X)=E[X^2]-E[X]^2'
  frames.append(dict(index=i,label=z['action'],caption=z['why'],duration=1000,svg=drawing(z),formula=formula,snapshot=dict(inputs=numeric(item['spec']),state=numeric(z),result=numeric(result)if i==len(states)-1 else None),teaching=dict(currentState=z['action'],operation=z['action'],why=z['why'],reading='The axes, probabilities and declared sample data define this drawing. Signed covariance contributions differ from probability masses. Full precision and all state entries remain inspectable.',checks=[dict(mathHtml='This is the completed result, not a partial accumulator',result=str(i==len(states)-1).lower())])))
 models.append(dict(**numeric(item),invariant='Inspect the declared finite law and its exact checkpoints. Partial sums are labeled; a finite trace is not a universal proof. Geometric plots keep their coordinate meaning.',result=numeric(result),frames=frames))
groups=dict(moments=['weighted-three','center-shift'],joint=['joint-positive','bernoulli-opposite','overlap'],dependence=['parabola'],quadratic=['quadratic-weight','psd-failure'],sampling=['without-replacement','fixed-points','empty-boxes'],averages=['averaging','same-versus-independent'],mixture=['two-group','latent-bernoulli','latent-pair','heteroscedastic','cancel-covariance'],projection=['linear-projection'],bounds=['chebyshev','cantelli'],walk=['walk-two','walk-biased'])
save(E/'model-specs.json',numeric(specs));save(R/'dist/chapters/s_variance-models.json',dict(models=models,groups=groups))
save(E/'reading.json',dict(status='reviewed_written_sources',candidateUniversities=9,coreUniversities=['MIT','CMU','Oxford','Berkeley'],additionalUniversities=['ETH Zurich','Cornell'],readRanges=dict(MIT='Combined PDF46–51,70–76,103–112',CMU='Lecture3 pp7–8; Lecture4 pp1–8',Oxford='PDF1–3,23–29,57,64–68',Berkeley='All five Lecture17 pages',ETH='Title and PDF8,16',Cornell='Entire Lecture9 HTML'),limitations='Stanford, Harvard and Cambridge screened only; no global-all-courses claim; selected sections rather than all downloaded text.'))
print('Prepared',len(models),'models and',sum(len(m['frames'])for m in models),'checkpoints.')
