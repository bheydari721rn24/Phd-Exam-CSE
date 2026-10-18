"""Generate exact, problem-specific tree traces; labels distinguish bounds from values."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import math,json
R=Path(__file__).resolve().parents[1]
def MAX(*c):return ('MAX',c)
def MIN(*c):return ('MIN',c)
def CH(*c):return ('CHANCE',c)
def display(x):
 if x==math.inf:return '∞'
 if x==-math.inf:return '−∞'
 return str(x).replace('-','−')
def build(key,title,raw,alpha=-math.inf,beta=math.inf,labels=None):
 nodes=[];edges=[];leaves=[]; labels=labels or {}
 def visit(raw,depth,path):
  id='n'+str(len(nodes));terminal=not isinstance(raw,tuple)
  n={'id':id,'kind':'LEAF'if terminal else raw[0],'depth':depth,'path':path,'label':labels.get(path,''),'children':[]}
  nodes.append(n)
  if terminal:n['input']=display(F(raw));n['exact']=F(raw);n['span']=(len(leaves),len(leaves));leaves.append(n)
  else:
   for i,child in enumerate(raw[1]):
    prob=None
    if raw[0]=='CHANCE':prob,child=child;prob=F(prob)
    c=visit(child,depth+1,path+str(i));n['children'].append((c,prob));edges.append({'from':id,'to':c['id'],'probability':display(prob)if prob is not None else None})
   n['span']=(n['children'][0][0]['span'][0],n['children'][-1][0]['span'][1])
   if raw[0]=='CHANCE':
    assert all(p>=0 for _,p in n['children'])and sum(p for _,p in n['children'])==1
    n['exact']=sum(p*c['exact']for c,p in n['children'])
   else:n['exact']=(max if raw[0]=='MAX'else min)(c['exact']for c,p in n['children'])
  return n
 root=visit(raw,0,'');width=max(430,82*len(leaves)+48);height=118+84*max(n['depth']for n in nodes)
 for n in nodes:n['x']=(n['span'][0]+n['span'][1]+1)*41+24+(width-(82*len(leaves)+48))/2;n['y']=32+84*n['depth']
 state={n['id']:{'status':'unread','score':None,'flag':None}for n in nodes};frames=[];checks=[];visits=[]
 def frame(active,caption,why,window=None,windowRole=None):frames.append({'active':active,'caption':caption,'why':why,'window':window,'windowRole':windowRole,'nodes':deepcopy(state),'evaluatedLeaves':len(visits)})
 def mark(n):
  state[n['id']]['status']='pruned'
  for c,p in n['children']:mark(c)
 def search(n,a,b):
  a0,b0=a,b;state[n['id']]['status']='active';frame(n['id'],'Enter '+(n['label']or n['kind'])+'.','Incoming thresholds restrict which further information can affect an ancestor. They do not necessarily enclose this subtree’s value.',[display(a),display(b)],'incoming')
  if n['kind']=='LEAF':
   value=n['exact'];visits.append(n['id']);state[n['id']].update(status='returned',score=display(value),flag='exact');frame(n['id'],'Evaluate terminal input '+display(value)+'.','This leaf is an exact terminal utility in MAX’s coordinates.');return value
  vals=[];value=-math.inf if n['kind']=='MAX'else math.inf
  if n['kind']=='CHANCE':value=F(0)
  for i,(c,p)in enumerate(n['children']):
   v=search(c,-math.inf,math.inf)if n['kind']=='CHANCE'else search(c,a,b)
   if n['kind']=='CHANCE':value+=p*v
   elif n['kind']=='MAX':value=max(value,v);a=max(a,value)
   else:value=min(value,v);b=min(b,value)
   vals.append(v);state[n['id']].update(status='working',score=display(value),flag='partial sum'if n['kind']=='CHANCE'else'working score')
   frame(n['id'],'Update '+n['kind']+' after child '+str(i+1)+'.',('Add probability '+display(p)+' times exact child value '+display(v)+'. This is a partial weighted sum until all outcomes are processed.'if n['kind']=='CHANCE'else'Update the working score and thresholds using the child return. Its flag matters; a working score is not automatically an exact minimax value.'),[display(a),display(b)],'current')
   if n['kind']!='CHANCE'and a>=b:
    remaining=n['children'][i+1:]
    for child,prob in remaining:mark(child)
    if remaining:frame(n['id'],'Cut '+str(len(remaining))+' remaining child branch'+('es.'if len(remaining)>1 else'.'),'Alpha has reached beta. These inputs remain visible as supplied problem data, but the grey branches are not evaluated by this trace.',[display(a),display(b)],'current')
    break
  flag='exact'if n['kind']=='CHANCE'else'upper bound'if value<=a0 else'lower bound'if value>=b0 else'exact'
  truth=n['exact'];assert (truth==value if flag=='exact'else truth<=value if flag=='upper bound'else truth>=value),(key,n['id'],value,truth,flag)
  checks.append({'node':n['id'],'returned':display(value),'flag':flag,'independentFullBackup':display(truth)})
  state[n['id']].update(status='returned',score=display(value),flag=flag)
  frame(n['id'],'Return '+display(value)+' as '+flag+'.',('All required continuation information establishes this exact value.'if flag=='exact'else'The return is a one-sided certificate, not a claim that the pruned subtree was completely evaluated.'),[display(a0),display(b0)],'classification')
  return value
 frame(None,'Read the complete ordered input tree.','Blue nodes maximize MAX’s utility; red nodes minimize it; teal nodes take the displayed probability-weighted expectation. Terminal numbers are input data, not evidence that a branch has been searched.')
 result=search(root,alpha,beta)
 flat=[{k:v for k,v in n.items()if k not in ['children','span','exact']}for n in nodes]
 return {'id':key,'title':title,'type':'tree','width':width,'height':height,'nodes':flat,'edges':edges,'frames':frames,'result':display(result),'exactRoot':display(root['exact']),'checks':checks,'visitedLeaves':visits}

models=[]
def add(*args,**kwargs):models.append(build(*args,**kwargs))
add('intro','An enforceable payoff rather than the largest leaf',MAX(MIN(4,11,-2),MIN(6,3,9),MIN(5,8,7)))
add('q1','Problem1: MIT two-ply reconstruction',MAX(MIN(2,7),MIN(1,8)))
add('bins-min','Problem2: an adversarial opponent',MAX(MIN(-50,50),MIN(1,3),MIN(-5,15)))
add('bins-chance','Problem2: the same inputs under a uniform opponent',MAX(CH(('1/2',-50),('1/2',50)),CH(('1/2',1),('1/2',3)),CH(('1/2',-5),('1/2',15))))
bins=[(-50,50),(1,3),(-5,15)]
add('bins-coin','Problem3: coin outcome observed before MIN acts',MAX(*(CH(('1/2',MIN(*bins[i])),('1/2',MIN(*bins[(i-1)%3])))for i in range(3))))
add('q4','Problem4: reject the right MIN branch',MAX(MIN(10,8),MIN(4,50)))
add('q5','Problem5: two directions of pruning',MAX(MIN(MAX(10,6),MAX(100,8)),MIN(MAX(1,2),MAX(20,4))))
add('q6','Problem6: preserve the exact edge probabilities',MAX(CH(('1/4',12),('1/4',8),('1/2',4)),CH(('1/2',8),('1/2',6)),CH(('1/3',12),('2/3',6))))
for x in [2,4,6,10]:add('q9-x'+str(x),'Problem9: x='+str(x),MAX(MIN(x,8),MIN(4,12)))
for x in [5,6,8]:add('q10-x'+str(x),'Problem10: x='+str(x),MAX(MIN(MAX(4,7),MAX(x,3)),MIN(MAX(6,1),MAX(9,2))))
add('q11','Problem11: the equality return is only a bound',MAX(5,MIN(5,0)))
add('q12','Problem12: a fail-low MAX working score',MAX(MIN(6,-5),MIN(7,-8)),alpha=F(8),beta=F(10))
add('q13','Problem13: fail-high leaves an exact value undiscovered',MAX(9,20),alpha=F(0),beta=F(8))
add('q16','Problem16: count visits separately from leaves',MAX(MIN(MAX(0,0),MAX(0,0)),MIN(MAX(0,0),MAX(0,0))))
add('q24','Problem24: deterministic and weighted backups',MAX(MIN(1,5),CH(('1/4',8),('3/4',0))))
add('q40','Problem40: repeated successor probability is retained',CH(('1/4',8),('1/4',8),('1/2',0)),labels={'0':'s (1)','1':'s (2)','2':'t'})
add('authentic-1403','Original MS CE1403 Question68: no branch is pruned',MAX(MIN(MAX(8,2),MAX(5,3)),MIN(15,MAX(4,7))),labels={'01':'A','010':'B','011':'C','1':'D','11':'E','110':'F','111':'G'})
for name,x,y in [('original',4,15),('lower-x',-2,20),('y-equality',4,10),('x-too-large',11,15),('y-too-large',4,21)]:
 add('authentic-1404-'+name,'Original MS CE1404 Question69: x='+str(x)+', y='+str(y),MAX(10,MIN(MAX(x,3,2),MAX(7,1)),MIN(MAX(y,6),MAX(20,23))))
out=R/'research/i_games-tree-models.json';out.write_text(json.dumps({'state':'generated_exact_frames_browser_review_pending','models':models},indent=2)+'\n',encoding='utf8')
print({'models':len(models),'frames':sum(len(m['frames'])for m in models),'boundContracts':sum(len(m['checks'])for m in models),'path':str(out)})
