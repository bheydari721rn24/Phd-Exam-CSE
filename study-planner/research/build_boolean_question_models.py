from pathlib import Path
import sys,json,math,re,html
from itertools import product
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s
S={};md=MarkdownIt('commonmark',{'html':True})
def frame(kind,formula,caption,**v):
 return dict(nodes=[],edges=[],snapshot=dict(kind=kind,**v),caption=caption,captionHtml='<p>'+caption+'</p>',formula=formula,formulaHtml='<div class="formula-block">'+mathml.render(formula,True).replace('<mo>-</mo>','<mo>−</mo>')+'</div>',line=0,metrics={},teaching=dict(operation=caption,why=caption,currentState=v,initial=False,activeLine=0,changes=[],checks=[],reading='Read the named inputs, current operation and exact table or connected net. A pending value is not an established output.'))
def scene(name,title,description,frames):
 frames[0]['teaching']['initial']=True
 S['boolean-question-'+name]=dict(id='boolean-question-'+name,title=title,description=description,descriptionHtml=mathml.markdown_math(description,md),invariant=description,visual=dict(type='enumeration',claim=description),code=['Read the declared input domain; execute the actual restriction or gate operation; compare the derived result and its boundary'],frames=frames)
def table(name,title,description,headings,rows,formula,captions=None):
 def cell(v):
  text=str(v)
  if re.fullmatch(r'[01]+|\d+|[abcFpqr]|a\d+',text)or re.search(r'x\d|[∨∧¬]|F\(e',text):
   formula=re.sub(r'([xa])([0-9]+)',r'\1_{\2}',text).replace('∨',r'\lor ').replace('∧',r'\land ').replace('¬',r'\neg ').replace(' XOR ',r'\oplus ')
   formula=re.sub(r'e([0-9]+)',r'e_{\1}',formula)
   return mathml.render(formula,False)
  return html.escape(text)
 rendered=[[cell(v)for v in r]for r in rows]
 caps=captions or ['Establish all column meanings and the complete input domain.','Derive the intermediate columns or independent decisions.','Read the result and cross-check the stated conclusion.']
 scene(name,title,description,[frame('table',formula,cap,headings=headings,rows=rows,rowsHtml=rendered,stage=i) for i,cap in enumerate(caps)])
bits=list(product((0,1),repeat=3))
table('sets','The four actual set-membership regions','Every row is a possible membership region of an arbitrary element. The bracket collapses to not-B, so its intersection with B-minus-A is empty.',['a','b','bracket','second term','output'],[[a,b,1-b,0,(1-a)*b]for a,b in product((0,1),repeat=2)],r'F=(\neg a)b')
for name,on,names in [('cnf',[1,3,4,6],'ABC'),('majority',[3,5,6,7],'pqr'),('implication',[0,1,7],'pqr')]:
 rows=[]
 for i,b in enumerate(bits):
  clause=' ∨ '.join(('¬'if z else'')+x for x,z in zip(names,b));rows.append([''.join(map(str,b)),i,int(i in on),'none: true row'if i in on else clause])
 table(name,'Actual source truth table and false-row clauses','The complete original three-input domain is enumerated. Only false rows supply canonical maxterms; each literal is false on its designated row.',['word','index','F','required maxterm'],rows,r'F=\prod_{i:F(i)=0}M_i')
table('weighted-parity','The source zero-count cases carry unequal weights','Original length-four strings are grouped by their number of zeros, retaining the three choices for every nonzero position.',['zeros','position choices','nonzero fills','strings'],[[0,1,81,81],[2,6,9,54],[4,1,1,1]],r'A=81+54+1=136,\quad A/4=34')
for name,kind in [('nand','nand'),('mux','mux')]:
 frames=[]
 for x,y in product((0,1),repeat=2):
  if kind=='nand':
   t=1-x*y;u=1-x*t;v=1-y*t;f1=1-u*v;f2=1-v
   caps=['Apply one original input assignment to both primary wires.','Evaluate the first NAND; its output feeds both middle gates.','Evaluate the two middle NAND gates using the same shared net.','Evaluate both output NAND gates, including the tied-input inverter.']
   frames.extend(frame(kind,rf'{x}-{y}={f1}-2\cdot{f2}',cap,x=x,y=y,t=t,u=u,v=v,f1=f1,f2=f2,stage=i) for i,cap in enumerate(caps))
  else:
   t=1-y;out=(1-x)*t
   frames.extend(frame(kind,r'F=(\neg a)(\neg b)',cap,a=x,b=y,t=t,out=out,stage=i) for i,cap in enumerate(['Set the two actual select pins and the three constant data wires.','The first multiplexer selects 1 or 0 according to b.','The second multiplexer selects the first output or zero according to a.']))
 scene(name,'Five-NAND difference and borrow'if kind=='nand'else'Two original cascaded multiplexers','All four original input assignments are traced through the source pin connections. Checkpoints show logical evaluation, not measured propagation timing.',frames)
scene('hazard','A declared single-input handoff and its consensus bridge','Stable b=c=1. The illustrative delay contract has a falling at time 1, product ab falling at time 3, inverted-a product rising at time 5, and OR responses one time unit later. The added bc path is stable at one. This is a specified possible timing trace, not a transistor measurement.',[frame('hazard',r'ab+(\neg a)c+bc=ab+(\neg a)c',cap,stage=i,times=[0,1,3,4,5,6,7],signals=[[1,0,0,0,0,0,0],[1,1,0,0,0,0,0],[0,0,0,0,1,1,1],[1,1,1,0,0,1,1],[1,1,1,1,1,1,1]]) for i,cap in enumerate(['Read the declared input and delay contract.','The old product falls before the inverter-dependent new product rises.','The original OR output can briefly fall on the uncovered interval.','The consensus product stays one and blocks this single-input static-one glitch.'])])
table('free-pairs','Two free complementary pairs in the actual partial table','Unknown indices 0,1,6,7 form two independent opposite-output pairs; fixed pairs are already consistent.',['F(0)','F(7)','F(1)','F(6)'],[[a,1-a,b,1-b]for a,b in product((0,1),repeat=2)],r'N=2^2=4')
table('quantifier','Exact two cofactor choices for the selector','The zero-x cofactor is z, the one-x cofactor is y. Existential output accepts either successful witness.',['y','z','F0','F1','exists x','forall x'],[[y,z,z,y,y|z,y*z]for y,z in product((0,1),repeat=2)],r'\exists xF=y+z,\quad\forall xF=yz')
table('majority-anf','Parity of the actual three pair products','The same three pair products are ORed and XORed on all eight inputs. Their odd threefold overlap explains agreement at 111.',['abc','ab','ac','bc','OR','XOR'],[[''.join(map(str,b)),b[0]*b[1],b[0]*b[2],b[1]*b[2],int(sum(b)>=2),(b[0]*b[1])^(b[0]*b[2])^(b[1]*b[2])]for b in bits],r'F=ab\oplus ac\oplus bc')
table('derivative','Four contexts, eight starting assignments','Both starting values of x lie on each sensitive edge. The context count and directed-start count remain separate.',['yz','F0=yz','F1=not yz','difference','starting rows'],[[''.join(map(str,b)),b[0]*b[1],1-b[0]*b[1],1,2]for b in product((0,1),repeat=2)],r'D_x(x\oplus yz)=1,\quad N=2\cdot4=8')
table('cofactor','The actual three-factor expression restricted on a','Restricting a to zero gives b; restricting a to one gives c. The extra b+c factor is already implied on each accepted branch.',['abc','original','a c + not-a b','mismatch'],[[''.join(map(str,b)),(b[0]|b[1])*((1-b[0])|b[2])*(b[1]|b[2]),(b[0]*b[2])|((1-b[0])*b[1]),0]for b in bits],r'F=(\neg a)b+ac')
table('monotone-two','Incomparable middle rows are independent','Endpoints 00 and 11 are fixed; the two middle rows are incomparable in the componentwise order.',['F00','F01','F10','F11','function'],[[0,a,b,1,['AND','a','b','OR'][2*a+b]]for a,b in product((0,1),repeat=2)],r'N=2^2=4')
# In the table index above: 01=0,10=1 is a; 01=1,10=0 is b.
for row in S['boolean-question-monotone-two']['frames'][0]['snapshot']['rows']:assert row[-1] in ['AND','a','b','OR']
for n in [5,8]:
 table('chain-'+str(n),'Every accepted '+str(n)+'-bit implication-chain row','The zero-prefix length is the unique choice. Including both endpoints gives n+1 rows.',['zero prefix','accepted word'],[[k,'0'*k+'1'*(n-k)]for k in range(n+1)],rf'N={n}+1={n+1}')
 table('parity-'+str(n),'Actual parity pairing on '+str(n)+' inputs','Choose the remaining n−1 bits freely. Exactly one leading bit gives odd parity; representative contexts show the bijection.',['tail','leading for odd','odd word','paired even word'],[[format(k,f'0{n-1}b'),1-(k.bit_count()%2),str(1-(k.bit_count()%2))+format(k,f'0{n-1}b'),str(k.bit_count()%2)+format(k,f'0{n-1}b')]for k in range(4)],rf'N=2^{{{n}-1}}={2**(n-1)}')
 table('products-'+str(n),'Independent input pairs in the '+str(n)+'-pair problem','The full domain has two bits per pair. Count the all-false-product complement before subtracting.',['pairs processed','all words','all products false','OR true'],[[k,4**k,3**k,4**k-3**k]for k in range(n+1)],rf'N=4^{n}-3^{n}={4**n-3**n}')
 table('weight-'+str(n),'Exactly-two rows and their actual position choices','An unordered pair of distinct positions defines a unique row. The sum of possible partners counts each pair once.',['first one position','second choices','new rows'],[[i,','.join(map(str,range(i+1,n+1))),n-i]for i in range(1,n)],rf'N=\binom{{{n}}}{{2}}={math.comb(n,2)}')
 table('false-'+str(n),'At-most-one table: canonical false-row count','Canonical clauses correspond to all remaining false rows after retaining the weight-zero and weight-one layers.',['object','count'],[['all rows',2**n],['zero-weight true',1],['one-weight true',n],['false rows / maxterms',2**n-n-1]],rf'N=2^{n}-{n}-1={2**n-n-1}')
for n in [3,4]:
 table('self-dual-'+str(n),'Complementary row decisions for '+str(n)+' inputs','Each pair has one independent output bit; the other member is forced opposite.',['pair representative','partner','free outputs'],[[format(i,f'0{n}b'),format(2**n-1-i,f'0{n}b'),'0/1; partner forced']for i in range(2**(n-1))],rf'N=2^{{2^{{{n}-1}}}}={2**(2**(n-1))}')
 table('affine-'+str(n),'Recoverable affine coefficients in '+str(n)+' inputs','The origin fixes the constant; each singleton row recovers one input coefficient.',['coefficient','recovery'],[['c','F(0)']]+[['a'+str(i),'F(e'+str(i)+') XOR F(0)']for i in range(1,n+1)],rf'N=2^{{{n}+1}}={2**(n+1)}')
 table('quadratic-'+str(n),'Actual square-free monomial inventory','Independent binary coefficients are attached to each displayed monomial class. Distinctness follows from subset inversion.',['degree','monomials','count'],[[0,'1',1],[1,', '.join('x'+str(i)for i in range(1,n+1)),n],[2,', '.join('x'+str(i)+'x'+str(j)for i in range(1,n)for j in range(i+1,n+1)),math.comb(n,2)]],rf'N=2^{{1+{n}+\binom{{{n}}}{{2}}}}={2**(1+n+math.comb(n,2))}')
 table('symmetric-'+str(n),'All nonempty weight layers for '+str(n)+' inputs','Layer sizes count rows. One freely chosen output per layer counts symmetric functions; those are different quantities.',['weight','layer size','output freedom'],[[k,math.comb(n,k),'one independent bit']for k in range(n+1)],rf'N=2^{{{n}+1}}={2**(n+1)}')
table('antichains','Complete three-input monotone classification','Minimal true sets are an antichain. All possible sizes and subtypes are counted without overlap.',['antichain size','classification','count'],[[0,'empty',1],[1,'one of eight subsets',8],[2,'3 singleton pairs + 3 pair pairs + 3 mixed',9],[3,'two complete middle layers',2]],r'N=1+8+9+2=20')
table('fixed-self-dual','The fixed endpoint pair leaves three free pairs','The actual fixed 000/111 pair is consistent. Each other pair contributes one independent bit.',['pair','constraint','choices'],[['000/111','fixed 0/1',1],['001/110','choose one; force partner',2],['010/101','choose one; force partner',2],['011/100','choose one; force partner',2]],r'N=1\cdot2\cdot2\cdot2=8')
# Dedicated lesson mechanisms use actual identities rather than unrelated examples.
table('de-morgan','Scope-preserving complement evaluation','Both columns evaluate the same binary input; the composite complement includes the entire AND node.',['ab','not(ab)','not a OR not b'],[[''.join(map(str,b)),1-b[0]*b[1],(1-b[0])|(1-b[1])]for b in product((0,1),repeat=2)],r'\neg(ab)=\neg a+\neg b')
table('absorption','Whole-product coverage by its simpler term','When a is one it already covers every row accepted by ab; when a is zero both vanish.',['ab','ab','a OR ab','a'],[[''.join(map(str,b)),b[0]*b[1],b[0]|(b[0]*b[1]),b[0]]for b in product((0,1),repeat=2)],r'a+ab=a')
table('selector','Shannon restriction and exact sensitivity','The actual selector is not-x times y plus x times z. Compare ordered cofactors to distinguish change from its direction.',['yz','F0=y','F1=z','D_x F'],[[''.join(map(str,b)),b[0],b[1],b[0]^b[1]]for b in product((0,1),repeat=2)],r'F=(\neg x)y+xz,\quad D_xF=y\oplus z')
table('xor','Binary XOR has cancellable, reversible inputs','A fixed input bit either preserves or complements the other bit. XOR and OR differ on the both-one row.',['ab','XOR','OR','XNOR'],[[''.join(map(str,b)),b[0]^b[1],b[0]|b[1],1-(b[0]^b[1])]for b in product((0,1),repeat=2)],r'a+b=a\oplus b\oplus ab')
(E/'g_boolean-models.json').write_text(json.dumps(S,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=R/'dist/chapters/concept-animations.json';all=json.loads(p.read_text());all['scenes'].update(S)
for key in list(all):
 if key.startswith('boolean-question-'):all.pop(key)
p.write_text(json.dumps(all,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
print({'uniqueModels':len(S),'frames':sum(len(v['frames'])for v in S.values())})
