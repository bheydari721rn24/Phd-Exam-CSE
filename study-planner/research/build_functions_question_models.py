"""Construct exact, question-specific finite functions and counting states."""
from pathlib import Path
import sys,math,json,html,itertools,re
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True});S={}
def native(s):return mathml.render(str(s),False)
def math_prose(s):
 slots=[]
 def hold(value):slots.append(mathml.render(value,False));return '\ue000'+str(len(slots)-1)+'\ue001'
 if 'f∘g=id'in s:s=s.replace('f∘g=id',hold(r'f\circ g=\operatorname{id}'))
 if '2−sqrt(y−3)'in s:s=s.replace('2−sqrt(y−3)',hold(r'2-\sqrt{y-3}'))
 s=re.sub(r'\{([A-Za-z0-9, ]+)\}',lambda m:hold(r'\{'+m[1]+r'\}'),s)
 s=re.sub(r'\b[a-d](?:,\s*[a-d])+',lambda m:hold(m[0]),s)
 s=re.sub(r'\ba(?=-fiber)',lambda m:hold('a'),s)
 for expression in['g(f(a))','f(g(b))','f(f(x))']:
  if expression in s:s=s.replace(expression,hold(expression))
 s=re.sub(r'\b([fg])=(\([^)]*\))',lambda m:hold(m[1]+'='+m[2]),s)
 s=re.sub(r'\(-?\d+(?:,\s*-?\d+)+\)',lambda m:hold(m[0]),s)
 s=re.sub(r'\b[fg]\([^()]+\)',lambda m:hold(m[0]),s)
 s=re.sub(r'\b[xy][≤≥=][-0-9]+',lambda m:hold(m[0]),s)
 s=re.sub(r'\d+(?:→\d+)+',lambda m:hold(m[0]),s)
 s=re.sub(r'\b[bcdfghkmnxy]\b',lambda m:hold(m[0]),s)
 result=md.render(s).strip()
 if result.startswith('<p>')and result.endswith('</p>'):result=result[3:-4]
 for i,value in enumerate(slots):result=result.replace('\ue000'+str(i)+'\ue001',value)
 return result
def frame(kind,formula,caption,why=None,**v):
 return dict(nodes=[],edges=[],snapshot=dict(kind=kind,**v),caption=caption,captionHtml='<p>'+html.escape(caption)+'</p>',formula=formula,formulaHtml='<div class="formula-block">'+mathml.render(formula,True).replace('<mo>-</mo>','<mo>−</mo>')+'</div>',line=0,metrics={},teaching=dict(operation=caption,why=why or caption,currentState=v,initial=False,activeLine=0,changes=[],checks=[],reading='Read the displayed domain, codomain and fixed choices. Prefix states are partial constructions; counts and final assignments are exact. A finite excerpt of an infinite map is identified explicitly.'))
def scene(name,title,description,frames):
 frames[0]['teaching']['initial']=True
 S['functions-question-'+name]=dict(id='functions-question-'+name,title=title,description=description,descriptionHtml='<p>'+math_prose(description)+'</p>',invariant=description,visual=dict(type='enumeration',claim=description),code=['Validate the named types and constraints.','Derive the exact fibers, choices or orbit state.','Match the result to the requested object and inspect the boundary.'],frames=frames)
 meanings={
 'table':('Compute contributions for the named labelled objects.','Combine the disjoint cases or signed omission events exactly as stated.','A row contributes the displayed exact number. Partial sums are bookkeeping stages, and different counted objects must remain distinct.'),
 'sequence':('Choose one admissible multiplicity vector.','Expand its repeated outputs in increasing input order.','Each multiplicity vector determines exactly one weakly increasing tuple. No permutation of the input labels is an additional valid choice.'),
 'endofunction':('Follow each actual successor assignment.','Check the stated composition identity on every vertex.','The arrows specify the complete function. Cycle lengths, fixed points and entry distances explain different identities; an unlabelled shape cannot replace those assignments.'),
 'sections':('Select one input from each named fiber.','Apply the forward function to verify every selected representative.','Each selection lies in its own disjoint fiber, so applying the fixed forward function returns its target. Different target choices cannot share an input.'),
 'composition':('Apply the inner map to the original input.','Apply the outer map at that actual middle value.','The composite uses only attained middle points. Unused points can hide an outer collision or leave final targets unreached, as the stated case shows.'),
 'subsets':('Select the stated input or target subset.','Compute its direct image or full preimage under the given map.','Direct images require an antecedent; preimages collect every input with a selected output. The round trip therefore fills touched fibers or removes unused targets.'),
 'parabola':('Check the domain, codomain and the exact plotted rule.','Select the branch permitted by the restricted domain.','The same quadratic has two real branches. Restricting to the stated domain removes the collision and determines the unique valid inverse branch; the plotted window is only an illustration.'),
 'map':('Assign one valid output to the processed input.','Verify the complete declaration and the claimed counterexample.','A prefix is a partial construction. Only the completed displayed assignment is classified; every declared input must then have exactly one output.')}
 kind=frames[0]['snapshot']['kind'];a,b,why=meanings[kind];S['functions-question-'+name]['code']=['Read the exact types and fixed constraints.',a,b]
 def changes(before,after,path=''):
  if before==after:return []
  if isinstance(before,dict)and isinstance(after,dict):return [c for key in sorted(set(before)|set(after))for c in changes(before.get(key),after.get(key),path+'.'+key if path else key)]
  if isinstance(before,list)and isinstance(after,list):return [c for j in range(max(len(before),len(after)))for c in changes(before[j]if j<len(before)else None,after[j]if j<len(after)else None,path+'['+str(j)+']')]
  label=path
  match=re.fullmatch(r'(values|counts|selected|inner|outer)\[(\d+)\]',path)
  if match:
   field,index=match[1],int(match[2]);label={'values':'Displayed output at input position ','counts':'Multiplicity of output value ','selected':'Selected representative for target position ','inner':'Inner output at input position ','outer':'Outer output at middle position '}[field]+str(index+1)
  if path=='stage':label='Processed input count'if kind=='map'else'Construction stage'
  if path=='active':label='Current contribution row';before=before+1 if before is not None else None;after=after+1 if after is not None else None
  return [dict(field=label,before=before,after=after)]
 states=[]
 for i,f in enumerate(frames):
  state={key:value for key,value in f['snapshot'].items()if not key.endswith('Html')and key!='kind'};states.append(state)
  f['line']=f['teaching']['activeLine']=0 if i==0 else 2 if i==len(frames)-1 else 1
  f['captionMathHtml']=math_prose(f['caption'])
  f['teaching'].update(why=why,operationHtml=f['captionMathHtml'],whyHtml=math_prose(why),guide=S['functions-question-'+name]['code'],currentState=state,changes=changes(states[i-1],state)if i else[])
 if len(frames)>12:S['functions-question-'+name]['printFrameIndices']=[0,1,len(frames)//2,len(frames)-1]
 S['functions-question-'+name]['useAuthoredTeachingChanges']=True
def table(name,title,description,headings,rows,formula):
 rendered=[[native(str(v)[1:])if str(v).startswith('$')else native(str(v))if re.fullmatch(r'[-0-9(), ]+',str(v))else html.escape(str(v))for v in row]for row in rows]
 frames=[frame('table',formula,'Read the named objects before accumulating their contributions.',headings=headings,rows=rows,rowsHtml=[],active=-1)]
 for k,row in enumerate(rows):frames.append(frame('table',formula,'Include contribution '+str(k+1)+' of '+str(len(rows))+': '+str(row[0]).lstrip('$')+'.',headings=headings,rows=rows,rowsHtml=rendered[:k+1],active=k))
 scene(name,title,description,frames)
def graph_frame(values,caption,formula,source=None,target=None,mode='typed',stage=None,**kw):
 m=len(values);n=max(values,default=-1)+1 if target is None else len(target)
 return frame('map'if mode=='typed'else'endofunction',formula,caption,values=values,source=source or list(range(m)),target=target or list(range(n)),stage=m if stage is None else stage,**kw)
def mapscene(name,title,description,values,target,formula,source=None):
 scene(name,title,description,[graph_frame(values,('Establish the displayed types; no arrows are assigned yet.'if k==0 else'Assign the first '+str(k)+' displayed inputs; the remaining points are not yet evaluated.'if k<len(values)else'Every displayed input now has its stated output.'),formula,source=source,target=target,stage=k)for k in range(len(values)+1)])

mapscene('cardinality-counter','Equal finite sizes do not classify a specified map','Both carriers have two labelled members. The constant assignment is a counterexample to bijectivity despite equal sizes.',[0,0],[0,1],r'|A|=|B|=2,\quad f(0)=f(1)=0')
rows=[]
for x in[0,2,1]:
 for y in range(3):
  antecedent=y==(x+1)%3;fy=(y+1)%3;consequent=0==(fy+1)%3
  rows.append([f'$x={x}, y={y}','$'+str(int(antecedent)),'$'+str(fy),'$'+str(int(consequent)),'$'+str(int(not antecedent or consequent))])
table('quantified-cycle','All nine implication tests in the stated cycle model','The function and relation both follow 0→1→2→0. Columns separate the antecedent, interpreted f(y), consequent and implication truth. Only x=0 passes its entire row family.',['assignment','antecedent','function output','consequent','implication'],rows,r'\{x:\varphi(x)\}=\{0\}')
logical=S['functions-question-quantified-cycle']
logical['code']=['Fix one candidate input x.','Evaluate the antecedent and consequent for each y.','Accept x only if every implication in its three-row family is true.']
for i,f in enumerate(logical['frames']):
 f['caption']='Read each truth column separately; no column is a count.' if i==0 else 'Evaluate logical test '+str(i)+' of nine: '+rows[i-1][0][1:]+'.'
 f['captionMathHtml']=math_prose(f['caption'])
 why='An implication is false exactly when its antecedent is true and its consequent is false. A universally quantified candidate passes only when all three values of y give true implications. The zero and one entries are truth values, not contributions to a sum.'
 f['teaching'].update(operation=f['caption'],operationHtml=f['captionMathHtml'],why=why,whyHtml=math_prose(why),guide=logical['code'])
 for change in f['teaching']['changes']:
  if change['field']=='Current contribution row':change['field']='Current logical test row'
def monotone(name,m,n,endpoints=False):
 tuples=[v for v in itertools.combinations_with_replacement(range(1,n+1),m)if not endpoints or(v[0]==1 and v[-1]==n)]
 formula=rf'N=\binom{{{m+n-3 if endpoints else m+n-1}}}{{{n-1}}}={len(tuples)}'
 scene(name,f'All {len(tuples)} monotone output tuples for the stated {m}-to-{n} types','Each checkpoint is one complete valid function, with the ordered output tuple and its multiplicities. This enumerates all functions for the declared finite example, not all parameters.',[frame('sequence',formula,f'Function {i+1} of {len(tuples)}; the output multiplicities determine this unique ordered tuple.',values=list(v),counts=[v.count(j)for j in range(1,n+1)],endpointFixed=endpoints)for i,v in enumerate(tuples)])
monotone('monotone-five-five',5,5)
def onto(name,m,n):
 rows=[];total=0
 for j in range(n+1):
  number=math.comb(n,j);available=n-j;count=available**m;term=(-1)**j*number*count;total+=term
  rows.append([str(j),'$'+str(number),'$'+str(count),'$'+str(term),'$'+str(total)])
 table(name,f'Exact omission sum for {m} inputs and {n} labelled targets','Rows group forbidden target subsets by size. The sign restores intersecting omissions. Each column is derived from the declared domain and target sizes.',['forbidden labels','subsets','maps per subset','signed contribution','partial sum'],rows,rf'N={total}')
onto('onto-six-four',6,4)
mapscene('integer-shift-excerpt','Three declared values of the shift on all integers','The full map is k↦k+1 on the integers. This drawing is only the input excerpt −1,0,1 with outputs 0,1,2; it is not a self-map of that three-point excerpt.',[0,1,2],[0,1,2],r'f(k)=k+1,\quad f(0)=1\ne0',source=[-1,0,1])
table('image-three','Choose each three-label image and fill its nonempty fibers','The domain has five labelled inputs and the codomain four labels a,b,c,d. For each selected three-label image there are exactly 150 onto assignments.',['attained labels','onto count','accumulated count'],[[','.join(c),'$150','$'+str(150*(i+1))]for i,c in enumerate(itertools.combinations('abcd',3))],r'N=\binom{4}{3}(3^5-3\cdot2^5+3)=600')
def sections(name,sizes):
 fibers=[];start=0
 for r in sizes:fibers.append(list(range(start,start+r)));start+=r
 selections=list(itertools.product(*fibers));frames=[]
 for i,choice in enumerate(selections):
  # Large equal-size examples show a finite set of declared choices, with a separate product proof.
  if len(selections)>30 and i not in [0,1,len(selections)//2,len(selections)-1]:continue
  frames.append(frame('sections',rf'N=\prod |F_b|={math.prod(sizes)}',f'Choose representatives {choice}; applying f sends each selected input back to its own target.',fibers=fibers,selected=list(choice),sizes=sizes))
 scene(name,'Right-inverse representatives in the exact named fibers','A reverse arrow selects one member of its own target fiber. Every selection satisfies f∘g=id. When only representative selections are displayed, the caption does not claim a complete enumeration.',frames)
sections('sections-two-three-four',[2,3,4])
monotone('endpoints-six-four',6,4,True)
def idempotent_two(n):
 image=[0,1];rest=list(range(2,n));frames=[]
 for i,tail in enumerate(itertools.product(image,repeat=n-2)):
  if n>=8 and i not in[0,1,len(range(2**(n-2)))//2,2**(n-2)-1]:continue
  v=image+list(tail);frames.append(graph_frame(v,f'For the explicitly fixed image {{0,1}}, assignment {i+1} fixes both image points and sends every other point into that image.',rf'N=\binom{{{n}}}{{2}}2^{{{n}-2}}={math.comb(n,2)*2**(n-2)}',mode='endofunction',fixed=[0,1]))
 scene('idempotent-two-'+str(n),f'Idempotent maps on {n} points with the displayed two-point image','The two displayed image labels are fixed. The lesson separately counts all choices of that image; the animation is explicitly one fixed-image example, not an enumeration of every image set.',frames)
scene('composite-counter','Three exact typed composition counterexamples','Each checkpoint declares both functions. Unused middle points, outer collisions and missed final targets are distinct mechanisms; the complete compatible types change explicitly with the named case.',[
 frame('composition',r'g(f(0))=u','A singleton composite is bijective although the inner map misses c and the outer map merges b and c.',inner=[0],outer=[0,0],source=[0],middle=['b','c'],target=['u']),
 frame('composition',r'g(f(0))=g(f(1))=u','The inner map is onto the two-point middle carrier, but the composite merges two inputs.',inner=[0,1],outer=[0,0],source=[0,1],middle=['b','c'],target=['u']),
 frame('composition',r'g[f[A]]=\{u\}\subsetneq C','The outer map is onto {u,v}, but the inner map reaches only b, so the composite misses v.',inner=[0],outer=[0,1],source=[0],middle=['b','c'],target=['u','v'])])
mapscene('prescribed-fiber','The three required antecedents of a distinguished target','The seven-input example uses targets a,b,c. Inputs 0,1,2 are the specified a-fiber in this illustration; the other four inputs avoid a. They need not reach both b and c.',[0,0,0,1,1,1,1],['a','b','c'],r'N=\binom{7}{3}2^4=560')
mapscene('image-collision','Different input witnesses can have one common output','Use X={u}, Y={v}, with u and v distinct and both mapping to b. The two direct images coincide although the input sets are disjoint.',[0,0],['b'],r'f[X\cap Y]=\varnothing,\quad f[X]\cap f[Y]=\{b\}',source=['u','v'])
def involution_two(n):
 frames=[]
 # For each moved quartet, enumerate all three disjoint pairings; show the first quartet's mechanism.
 moved=range(4);patterns=[[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]
 for pairs in patterns:
  v=list(range(n))
  for a,b in pairs:v[a]=b;v[b]=a
  frames.append(graph_frame(v,'One of the three pairings of the displayed moved quartet; all outside labels are fixed.',rf'N=3\binom{{{n}}}{{4}}={3*math.comb(n,4)}',mode='endofunction',cycles=[list(p)for p in pairs]+[[i]for i in range(4,n)]))
 scene('involution-two-'+str(n),f'Two transpositions on {n} labels','The animation displays all three pairings for one explicitly selected moved quartet. The factor choosing the quartet is proved in the solution.',frames)
for n in[5,8]:
 mapscene('injection-'+str(n),'Three labelled inputs and '+str(n+3)+' available outputs','The arrows show one injective assignment in the exact stated codomain. Counts of remaining distinct choices are proved separately; this is not claimed to enumerate all assignments.',[0,3,6],list(range(n+3)),rf'N=({n}+3)({n}+2)({n}+1)={(n+3)*(n+2)*(n+1)}',source=['a','b','c'])
 onto('onto-three-'+str(n),n,3);idempotent_two(n);involution_two(n);monotone('monotone-three-'+str(n),n,3);sections('sections-three-'+str(n),[n,n,n])
 frames=[];v=[(i+1)%n for i in range(n)]
 for k in range(3):frames.append(graph_frame(v,'The same successor function displayed from a rotated start '+str(k)+'. Rotation changes notation, not any output.',rf'N=({n}-1)!={math.factorial(n-1)}',mode='endofunction',cyclic=True,displayStart=k))
 reverse=[(i-1)%n for i in range(n)];frames.append(graph_frame(reverse,'Reversing the orientation changes the successor function; this is a comparison, not a redundant display.',rf'f(0)=1,\quad f^{{-1}}(0)={n-1}',mode='endofunction',cyclic=True,displayStart=0))
 scene('one-cycle-'+str(n),f'Rotations and the reverse of an exact {n}-cycle','The first three checkpoints represent the same permutation. The final checkpoint is its different reverse. Fixing a starting label leaves (n−1)! cyclic arrangements.',frames)
 vals=[list(range(n)),[0,1]+[3,2]+list(range(4,n))]
 scene('fixed-two-'+str(n),'Two specified fixed labels; additional fixed points allowed','Labels 0 and 1 must remain fixed. Both displayed residual permutations are legal, including the identity on all labels.',[graph_frame(v,'The specified points 0 and 1 are fixed; inspect the unrestricted residual permutation.',rf'N=({n}-2)!={math.factorial(n-2)}',mode='endofunction',fixed=[0,1])for v in vals])

valid=[list(v)for v in itertools.product(range(4),repeat=4)if all(v[v[i]]==v[i]for i in range(4))]
scene('idempotents-four','All forty-one idempotents on the exact four-point carrier','Each checkpoint is one complete function whose image is fixed pointwise. Every displayed assignment satisfies f(f(x))=f(x) at every input; the lesson independently proves the four image-size counts.',[graph_frame(v,f'Idempotent {i+1} of {len(valid)}; its fixed image is '+'{'+', '.join(str(x)for x in sorted(set(v)))+'}.',r'N=4+24+12+1=41',mode='endofunction',fixed=sorted(set(v)))for i,v in enumerate(valid)])
def split_pairs(name,m,n):
 frames=[]
 for f in itertools.permutations(range(n),m):
  for g in itertools.product(range(m),repeat=n):
   if all(g[f[a]]==a for a in range(m)):
    frames.append(frame('composition',rf'N={math.factorial(n)//math.factorial(n-m)*m**(n-m)}',f'Actual split pair f={f}, g={g}; every original input is recovered by g(f(a)).',inner=list(f),outer=list(g),source=list(range(m)),middle=list(range(n)),target=list(range(m))))
 scene(name,f'All split inverse pairs on the exact {m}- and {n}-point carriers','Every checkpoint contains both functions, with exact compatible types. The two maps are an ordered pair; free reverse values appear only on unused middle points.',frames)
split_pairs('split-two-three',2,3)
table('bounded-fibers-six','All admissible labelled fiber-size vectors','Six inputs map onto three named targets, and every fiber size is at most three. The six permutations of (3,2,1) and the single vector (2,2,2) are different disjoint cases.',['labelled sizes','input assignments','partial total'],[(str(v),'$'+str(math.factorial(6)//math.prod(math.factorial(x)for x in v)),'$'+str(sum(math.factorial(6)//math.prod(math.factorial(x)for x in w)for w in sorted(set(itertools.permutations([3,2,1])))[:i+1])))for i,v in enumerate(sorted(set(itertools.permutations([3,2,1]))))]+[('(2, 2, 2)','$90','$450')],r'N=6\cdot60+90=450')
split_pairs('split-two-four',2,4)
scene('powerset-roundtrips','Power-set ambiguities of the stated four-input function','Inputs are 0,1,2,3 and targets a,b,c,d. The unused target d does not affect preimages; the a-fiber cannot be separated by a preimage.',[frame('subsets',r'I_f:\,16\to8,\quad P_f:\,16\to8',cap,values=[0,0,1,2],source=[0,1,2,3],target=['a','b','c','d'],selected=sel,targetSelected=ts)for cap,sel,ts in [('Select only input 0; its direct image is {a}.',[0],[0]),('The input round trip fills the other member 1 of the a-fiber.',[0,1],[0]),('Adding unused target d changes no preimage.',[0,1],[0,3])]])
monotone('endpoints-eight-five',8,5,True)
frames=[]
for a in[0,3]:
 for b in range(6):frames.append(graph_frame([(a*x+b)%6 for x in range(4)],f'Allowed slope {a} and offset {b} modulo six; every representative class gives one target class.',r'6\mid4a\ \Longleftrightarrow\ 3\mid a,\quad N=12',source=['[0]','[1]','[2]','[3]'],target=['[0]','[1]','[2]','[3]','[4]','[5]']))
scene('affine-quotient','All twelve induced affine maps from residues mod four to residues mod six','Only slopes 0 and 3 modulo six satisfy representative independence. Every checkpoint is a complete induced function, not a check on a few integer representatives.',frames)
table('involutions-eight','Eight labels: fixed points and transpositions remain different','The five rows correspond to j=0,…,4 transpositions. Fixed points number 8−2j; the counts are disjoint and exhaust all involutions.',['transpositions','fixed labels','maps','partial total'],[[str(j),str(8-2*j),'$'+str(math.factorial(8)//(2**j*math.factorial(j)*math.factorial(8-2*j))),'$'+str(sum(math.factorial(8)//(2**k*math.factorial(k)*math.factorial(8-2*k))for k in range(j+1)))]for j in range(5)],r'N=1+28+210+420+105=764')
v=[1,2,2,4,3,4,5];frames=[];power=list(range(7))
for k in range(1,5):
 power=[v[x]for x in power];fixed=[i for i,x in enumerate(power)if i==x];okay=all(power[power[i]]==power[i]for i in range(7))
 frames.append(graph_frame(power[:],f'Power {k}: the complete output tuple is {tuple(power)}; this power is '+('idempotent.'if okay else'not idempotent.'),rf'k={k},\quad H_f=2,\quad L_f=2',mode='endofunction',fixed=fixed))
scene('power-seven','Four exact powers of the stated seven-point endofunction','Each checkpoint recomputes all seven outputs, including the incoming chains and the two-cycle. The square and fourth power are idempotent; the odd powers retain a nontrivial cycle.',frames)
v=[1,2,0,4,5,6,3];frames=[]
for k in[1,2,6]:
 power=list(range(7))
 for _ in range(k):power=[v[x]for x in power]
 frames.append(graph_frame(power,f'Power {k}: inspect each actual successor and its fixed points.',rf'k={k},\quad\operatorname{{ord}}(f^k)={12//math.gcd(12,k)}',mode='endofunction',fixed=[i for i,x in enumerate(power)if i==x],cycleGroups=[[0,1,2],[3,4,5,6]]))
scene('cycles-three-four','A 3-cycle and a 4-cycle under powers','The original cycles use seven labelled vertices. A fixed point is a loop, not merely a shorter nontrivial cycle. The sixth power fixes exactly the first three vertices.',frames)
scene('weighted-composite','Actual inner and outer maps with outer fibers of sizes 1,2,3','The middle carrier has six points and the final target three. The three-input example chooses one member of each outer fiber; the four-input example doubles the first composite target.',[frame('composition',r'N_3=36,\quad N_4=432',cap,inner=inner,outer=[0,1,1,2,2,2],source=list(range(len(inner))),middle=list(range(6)),target=['a','b','c'])for cap,inner in [('Three inputs give a bijective composite.',[0,1,3]),('Four inputs give an onto composite with a repeated first target.',[0,0,1,3])]])
scene('restricted-parabola','The quadratic branch, collision and valid restricted inverse','The plotted window is x from −1 to 5, with exact quadratic coordinates. The full rule is stated in the proof. Blue highlights x≤2; the grey branch is excluded by that restriction.',[frame('parabola',r'h(y)=2-\sqrt{y-3},\quad y\ge3'if k==2 else r'f(x)=(x-2)^2+3',cap,stage=k)for k,cap in enumerate(['The two real branches have equal outputs at symmetric inputs 0 and 4.','Restrict the domain to x≤2 and codomain to y≥3.','For any target y≥3, the valid antecedent is 2−sqrt(y−3).'])])

all=json.loads((R/'dist/chapters/concept-animations.json').read_text());all['scenes'].update(S)
(R/'dist/chapters/concept-animations.json').write_text(json.dumps(all,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(E/'d_functions-models.json').write_text(json.dumps(dict(models=len(S),uniqueFrames=sum(len(s['frames'])for s in S.values()),sceneIds=list(S),scope='Exact finite functions and declared representative constructions; the chapter supplies all stated general proofs.'),indent=2)+'\n',encoding='utf-8')
print({'models':len(S),'frames':sum(len(s['frames'])for s in S.values())})
