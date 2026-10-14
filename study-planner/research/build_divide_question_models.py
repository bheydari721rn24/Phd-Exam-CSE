from pathlib import Path
import json,math,sys,copy
from fractions import Fraction
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True});S={}
def prose(s):return mathml.markdown_math(s,md).strip().removeprefix('<p>').removesuffix('</p>')
def frame(kind,formula,caption,why,**data):return dict(nodes=[],edges=[],snapshot=dict(kind=kind,**data),caption=caption,captionMathHtml=prose(caption),formula=formula,formulaHtml=mathml.render(formula,True),metrics={},line=0,teaching=dict(operation=caption,operationHtml=prose(caption),why=why,whyHtml=prose(why),currentState={},changes=[],checks=[]))
def scene(name,title,description,frames):
 guide=['Read the declared input and measured object.','Apply the highlighted valid combination operation.','Check the result against the invariant and exact formula.']
 for i,f in enumerate(frames):
  f['line']=0 if i==0 else 2 if i==len(frames)-1 else 1;f['teaching'].update(initial=i==0,activeLine=f['line'],guide=guide,currentState={'Checkpoint':i,'Checkpoints':len(frames)})
  if i:f['teaching']['changes']=[dict(field='Checkpoint',before=i-1,after=i)]
 key='divide-question-'+name;S[key]=dict(id=key,title=title,description=description,descriptionHtml='<p>'+prose(description)+'</p>',invariant=description,visual=dict(type='enumeration',claim=description),code=guide,frames=frames,useAuthoredTeachingChanges=True)
def merge(name,a,title):
 events=[];allComparisons=0
 def rec(a,offset):
  nonlocal allComparisons
  if len(a)<2:return a
  m=len(a)//2;l=rec(a[:m],offset);r=rec(a[m:],offset+m);i=j=0;o=[];charge=0;comp=0
  events.append(frame('merge',r'C_{\text{merge}}=0','Start one actual merge.','Both children are already sorted. The output is the consumed multiset in order.',left=l,right=r,i=i,j=j,output=[],charge=0,comparisons=0,totalComparisons=allComparisons,offset=offset))
  while i<len(l)and j<len(r):
   comp+=1;allComparisons+=1
   if l[i]<=r[j]:o.append(l[i]);i+=1
   else:charge+=len(l)-i;o.append(r[j]);j+=1
   events.append(frame('merge',r'C_{\text{merge}}='+str(comp)+r',\quad C_{\text{total}}='+str(allComparisons),'Select one smaller head; ties go left.','A strict right selection charges every remaining left key; equal keys charge none.',left=l,right=r,i=i,j=j,output=o.copy(),charge=charge,comparisons=comp,totalComparisons=allComparisons,offset=offset))
  o+=l[i:]+r[j:];events.append(frame('merge',r'C_{\text{merge}}='+str(comp)+r',\quad C_{\text{total}}='+str(allComparisons),'Copy the unconsumed tail without new head comparisons.','Every record is written exactly once in this merge; comparisons stop on exhaustion.',left=l,right=r,i=len(l),j=len(r),output=o.copy(),charge=charge,comparisons=comp,totalComparisons=allComparisons,offset=offset));return o
 result=rec(a,0);scene(name,title,'Actual recursive trace for input '+str(a)+'. Every merge is shown. The current-merge count and cumulative count over all merges are separately displayed.',events);S['divide-question-'+name]['audit']=dict(kind='merge',input=a,result=result,totalComparisons=allComparisons)
def direct_merge(name,l,r,title):
 i=j=0;c=inv=0;o=[];fs=[]
 while True:
  fs.append(frame('merge',r'C='+str(c)+r',\quad I_{\text{cross}}='+str(inv),'Inspect the current heads and completed output.','Consumed equal keys retain left-before-right order. Only strictly smaller right keys create cross charges.',left=l,right=r,i=i,j=j,output=o.copy(),charge=inv,comparisons=c,offset=0))
  if i==len(l)or j==len(r):break
  c+=1
  if l[i]<=r[j]:o.append(l[i]);i+=1
  else:inv+=len(l)-i;o.append(r[j]);j+=1
 o+=l[i:]+r[j:];fs.append(frame('merge',r'W='+str(len(o))+r',\quad I_{\text{cross}}='+str(inv),'The tail is copied; all output records remain.','The strict inversion count is complete and excludes equal pairs.',left=l,right=r,i=len(l),j=len(r),output=o.copy(),charge=inv,comparisons=c,offset=0));scene(name,title,'Two exact sorted runs; pointers, output and strict charges are displayed.',fs)
def summary(a):return[sum(a),max(sum(a[:j])for j in range(1,len(a)+1)),max(sum(a[i:])for i in range(len(a))),max(sum(a[i:j])for i in range(len(a))for j in range(i+1,len(a)+1))]
def subarray(name,l,r,title):
 a=l+r;L=summary(l);Q=summary(r);v=summary(a);w=min((-sum(a[i:j]),i,j)for i in range(len(a))for j in range(i+1,len(a)+1));fs=[]
 for k in range(5):fs.append(frame('summary',r'B=\max(B_L,B_R,U_L+P_R)='+str(v[3]),'Reveal summary component '+str(k)+'.','The total, prefix and suffix preserve boundary information; the best witness uses earliest start and end on ties.',input=a,split=len(l),left=L,right=Q,combined=v,reveal=k,witness=[w[1],w[2]]))
 scene(name,title,'Nonempty policy; component order is total, prefix, suffix, best. The highlighted best interval uses zero-based half-open endpoints.',fs)
def radix(name,x,y,m,title):
 base=10**m;h,l=divmod(abs(x),base);u,v=divmod(abs(y),base);z2=h*u;z0=l*v;zs=(h+l)*(u+v);z1=zs-z2-z0;fs=[]
 for k in range(5):fs.append(frame('radix',r'xy='+str(x*y),'Reveal radix reconstruction stage '+str(k)+'.','The low-part width determines both shifts. Sign is restored from the original operands; the mixed coefficient is derived by cancellation.',x=x,y=y,m=m,base=base,parts=[h,l,u,v],products=[z2,z0,zs,z1],stage=k))
 scene(name,title,'Exact decimal example. Products and shifts use the actual low width; they are not a bit-complexity measurement.',fs)
def blocks(name):
 M=[65,35,-2,8,24,22,-30];result=[19,22,43,50]
 scene(name,'Seven products and four output blocks','Exact scalar-block example X=[[1,2],[3,4]], Y=[[5,6],[7,8]]. General block cancellation preserves multiplication order.',[frame('blocks',r'C_{11}=M_1+M_4-M_5+M_7=19','Reveal product or recombination stage '+str(k)+'.','All seven products are needed for the displayed convention; all four outputs are verified against direct dot products.',products=M,outputs=result,stage=k)for k in range(9)])
def geometry(name):
 pts=[[-2,0,'L'],[-1,3,'L'],[0,1,'L'],[0,2,'R'],[1,4,'R'],[2,0,'R']];ordered=sorted(range(6),key=lambda i:(pts[i][1],i));pairs=[(i,j)for k,i in enumerate(ordered)for j in ordered[k+1:]if abs(pts[i][1]-pts[j][1])<math.sqrt(5)]
 fs=[];best=5;active=[]
 fs.append(frame('geometry',r'\delta^2=5','Read the rank-based child memberships.','Tied x-coordinates keep distinct identities. Separation is guaranteed within each color.',points=pts,active=[],best=best,order=ordered))
 for i,j in pairs:
  d=(pts[i][0]-pts[j][0])**2+(pts[i][1]-pts[j][1])**2;best=min(best,d);fs.append(frame('geometry',r'\delta_{\text{current}}^2='+str(best),'Compare the displayed strip pair.','This illustrative candidate trace uses the initial strip. The exact within-color packing proof is in the lesson; it is not inferred from six plotted points.',points=pts,active=[i,j],best=best,order=ordered))
 fs.append(frame('geometry',r'\delta_{\text{final}}^2=1','Return the attaining cross pair.','The two differently colored points at x=0 are one unit apart. Distinct integer-coordinate points cannot have a smaller positive squared distance.',points=pts,active=[2,3],best=1,order=ordered))
 scene(name,'Colored recursive halves and the closest cross pair','Six exact integer-coordinate points. Child squared distances are five; the cross pair at x=0 has squared distance one.',fs)
def butterfly(name):
 fs=[]
 for k in range(5):fs.append(frame('butterfly',r'Y=[3,9,16,10]\pmod{17}','Reveal the ordered butterfly stage '+str(k)+'.','Even and odd coefficient positions feed paired output indices. Twiddle signs and the inverse normalizer are explicit.',stage=k,even=[1,1],odd=[2,2],twiddle=[1,4],output=[3,9,16,10],modulus=17,root=4))
 scene(name,'Exact four-point modular butterflies','Input [1,2,0,0], positive-exponent root 4 modulo 17. Wires terminate at actual box ports; output positions are 0,2,1,3.',fs)
def convolution(name,a,b,title,N=None,modulus=None):
 values=[sum(a[i]*b[k-i]for i in range(len(a))if 0<=k-i<len(b))for k in range(len(a)+len(b)-1)];N=N or len(values);fs=[]
 for k in range(len(values)+1):
  accum=[sum(values[i]for i in range(k)if i%N==j)for j in range(N)];fs.append(frame('convolution',r'c_k=\sum_i a_i b_{k-i}','Accumulate '+str(k)+' coefficient positions.','Each source coefficient is connected to its destination index. Index wrap and arithmetic reduction are separate operations.',inputA=a,inputB=b,values=values,N=N,stage=k,accum=accum,modulus=modulus))
 scene(name,title,'Explicit integer coefficient positions; source-to-destination connections show whether padding prevents wraparound.',fs)
def groups(name,t,exactGroups=None):
 positive=3;gs=[]
 for i in range(1,t+1):gs.append([-3*i-2,-3*i-1,-3*i,positive,positive+1]);positive+=2
 gs.append([-2,-1,0,1,2])
 for _ in range(t):gs.append(list(range(positive,positive+5)));positive+=5
 if exactGroups is not None:gs=exactGroups
 # Full data remain in the model; the diagram shows a declared five-group window.
 fs=[]
 for k in range(len(gs)+1):fs.append(frame('groups',r'\#\{x<0\}=3t+2='+str(3*t+2),'Inspect '+str(k)+' certified groups.','Each below-pivot group supplies three strict keys; the pivot group supplies two. The exact full guarantee is not inferred from the displayed window.',groups=gs,stage=k,t=t,pivot=0,windowStart=max(0,min(k-2,len(gs)-5)),smaller=sum(v<0 for g in gs[:k]for v in g)))
 scene(name,'Full-five-group strict pivot certificate','All keys are distinct. The pivot is zero. Earlier and later groups are available through checkpoints; the full totals remain explicit.',fs)
def search(name,h):
 N=2**h-1;lo=0;hi=N;fs=[];visits=0
 while True:
  mid=(lo+hi)//2 if lo<hi else None;visits+=1;fs.append(frame('search',r'\text{calls}='+str(visits),'Visit the declared half-open interval.','The target exceeds every stored key. The final empty call reads no key; the path contains only actually visited states.',N=N,lo=lo,hi=hi,mid=mid,calls=visits,inspections=visits if mid is not None else visits-1,target=N+1))
  if mid is None:break
  lo=mid+1
 scene(name,'Unsuccessful search and the empty endpoint','Keys 1 through '+str(N)+'. Target '+str(N+1)+'. Only the actual rightmost search path is displayed.',fs)
def levels(name,h,a,b,kind,title):
 fs=[];N=b**h;running=0
 for j in range(h+1):
  size=N//b**j;count=a**j
  local=(1 if j==h else 0)if kind=='leaves'else(0 if j==h else(size-1 if kind=='merge'else size//2 if kind in ('sorted','fft')else size*size if kind=='quadratic'else 1))
  running+=count*local
  value=h*N-N+1 if kind=='merge'else h*N//2 if kind=='sorted'else a**h if kind=='leaves'else h*N//2 if kind=='fft'else running
  formula=(r'M(N)=hN-N+1='+str(value)if kind=='merge'else r'C(N)=hN/2='+str(value)if kind=='sorted'else r'\text{leaves}=a^h='+str(value)if kind=='leaves'else r'\text{butterflies}=hN/2='+str(value)if kind=='fft'else r'\text{accumulated toll}='+str(running))
  fs.append(frame('levels',formula,'Inspect full depth '+str(j)+' of '+str(h)+'.','The drawn root split is explicitly illustrative. The ledger counts every node at the current depth; terminal work and internal tolls are distinguished.',N=N,a=a,b=b,h=h,depth=j,count=count,size=size,local=local,running=running,measure=kind,value=value))
 scene(name,title,'Complete fixed-width recursion, with declared input '+str(N)+'. Leaf counts are not asserted for data-dependent pruning or carry-expanded widths.',fs)
def table_scene(name,title,heads,rows,formula,description):
 fs=[frame('table',formula,'Inspect row '+str(i)+'.','The stated formula counts the complete input. A displayed small illustration is identified separately.',headings=heads,rows=rows[:i+1],rowsHtml=[[prose('$'+str(v)+'$')if isinstance(v,(int,float))else str(v)for v in r]for r in rows[max(0,i-5):i+1]],active=min(i,5))for i in range(len(rows))];scene(name,title,description,fs)

table_scene('q1','Unequal-child conserved size',['depth','sum of sizes'],[[j,64]for j in range(5)],r'\sum_{|v|=j}|v|=64','Illustrative positive fixed fractions one-quarter and three-quarters before the base region. The answer proof covers arbitrary admitted alpha and beta; this table is not a full terminated tree.')
table_scene('q2','Median concatenation in descending order',['piece','keys'],[['right','7, 9'],['median','5'],['left','1, 3'],['output','7, 9, 5, 1, 3']],r'R\Vert[m]\Vert L','The child outputs are descending. These five distinct teaching keys instantiate the authentic algorithm; they are not an extra source input.')
merge('q3',[12,7,5,9,3,8,2,6],'Authentic merge-sort comparisons')
table_scene('q4','Admissible sampled-pivot partition sizes',['input','sample','minimum side','maximum side'],[[k,2*math.isqrt(k)+1,math.isqrt(k),k-1-math.isqrt(k)]for k in[25,36,49,64]],r'\sqrt N\le |L|,|R|\le N-1-\sqrt N','Perfect-square illustrative sizes with a sample that fits. Actual selection and input rank conditions are discussed in the authentic solution.')
merge('q5',list(range(1,9)),'Sorted eight-key merge trace');direct_merge('q6',[1,3,3],[2,3,4],'Strict inversion charges with equality');subarray('q7',[3,-6,5,-5,1],[6,-2],'Actual four-summary reconstruction');radix('q8',23,47,1,'Exact Karatsuba reconstruction');levels('q9',5,3,2,'quadratic','Quadratic toll across a three-child recursion');convolution('q10',[1]*5,[1]*4,'Five-by-four coefficient lengths');table_scene('q11','Nine sampled keys and strict pivot ranks',['sample position','relation to median'],[[i,'strictly below'if i<5 else'pivot'if i==5 else'strictly above']for i in range(1,10)],r'5\le\text{global rank}\le N-4','The nine sampled keys are distinct. Four sample keys certify each strict side; global ranks depend on unsampled keys. This is not the five-group selection algorithm.');geometry('q12')
for start,kind in[(13,'merge'),(17,'cross'),(21,'karatsuba'),(25,'strassen'),(29,'length'),(33,'fft'),(37,'pivot'),(41,'search')]:
 for off,h in enumerate([5,8,5,5]):
  name='q'+str(start+off)
  if kind=='merge':levels(name,h,2,2,'merge','Exact maximum comparison levels')
  elif kind=='karatsuba':levels(name,h,3,2,'leaves','Three-child product leaf count')
  elif kind=='strassen':levels(name,h,7,2,'leaves','Seven-child matrix product leaf count')
  elif kind=='fft':levels(name,h,2,2,'fft','Exact two-output butterfly count')
  elif kind=='cross':direct_merge(name,list(range(h,2*h)),list(range(h)),'All cross pairs are strict inversions')
  elif kind=='length':convolution(name,[1]*h,[1]*h,'Complete linear coefficient support')
  elif kind=='pivot':groups(name,h)
  elif kind=='search':search(name,h)
butterfly('q45');table_scene('q46','Integer lifts of one residue',['candidate','residue','in admitted range'],[[-10,7,'yes'],[7,7,'yes'],[24,7,'no']],r'-10\equiv7\pmod{17}','The range is [-10,10]. Two admissible integers share residue seven; extra range information is required.')
direct_merge('challenge1',[2,4,4,7],[1,4,6],'Duplicate-aware strict merge trace');subarray('challenge2',[3,-6,5,-5,1],[6,-2],'Summary order and deterministic witness');radix('challenge3',-123,45,1,'Odd-width signed multiplication');blocks('challenge4');geometry('challenge5');butterfly('challenge6');convolution('challenge7',[1,2,3],[4,5],'Index wrapping versus modulus loss',2,17);groups('challenge8',2,[[-30,-29,-28,1,2],[-27,-26,-25,3,4],[-2,-1,0,5,6],[7,8,9,10,11],[12,13,14,15,16]]);table_scene('challenge9','Interleaved equal-key record identities',['operation','emitted identities'],[['left-first','0,2,1,3'],['original-index comparison','0,1,2,3']],r'\text{stable order}=[0,1,2,3]','Primary keys are all equal. The diagram compares record identities, not numeric primary-key values.');search('challenge10',3)
for k,source in enumerate(['q6','q7','q12','q8','challenge4','q45','challenge7','challenge8'],1):
 scene0=copy.deepcopy(S['divide-question-'+source]);key='divide-question-construction'+str(k);scene0['id']=key;S[key]=scene0
p=R/'dist/chapters/concept-animations.json';data=json.loads(p.read_text());data['scenes'].update(S);p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(E/'a_divide-models.json').write_text(json.dumps(dict(topicId='a_divide',models=len(S),frames=sum(len(s['frames'])for s in S.values()),ids=list(S),state='models_pending_independent_semantic_and_rendered_checks'),indent=2)+'\n');print(len(S),'models;',sum(len(s['frames'])for s in S.values()),'frames')
