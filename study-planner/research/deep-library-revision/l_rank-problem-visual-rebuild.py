"""Replace every referenced rank gallery with actual-input derivation states."""
from pathlib import Path
import ast,copy,html,json,re,subprocess
import sympy as S
ROOT=Path(__file__).resolve().parents[2]; PATH=ROOT/'dist/chapters/problem-visual-models.json'
OLD=json.loads(PATH.read_text(encoding='utf8')); MODELS=copy.deepcopy(OLD); CHECKS=[]
BASE_MODELS=json.loads(subprocess.check_output(['git','show','ce272ad83079d4e95f6e009fd89c603240a8a708:dist/chapters/problem-visual-models.json'],cwd=ROOT))
M=S.Matrix
# Reuse only the already-reviewed rendering functions, never the Gaussian mutations.
helper=ROOT/'research/deep-library-revision/l_gauss-problem-visual-rebuild.py'
names={'check','plain','txt','cell','matrix','frame','setmodel'}
for node in ast.parse(helper.read_text(encoding='utf8')).body:
    if isinstance(node,ast.FunctionDef)and node.name in names:
        exec(compile(ast.Module(body=[node],type_ignores=[]),str(helper),'exec'))

def figure(title,panels,lines=(),extra=''):
    out=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-label="{html.escape(title,quote=True)}"><title>{html.escape(title)}</title>'
    out+=txt(380,25,title,21,True)
    positions={0:[],1:[380],2:[205,555],3:[130,380,630]}[len(panels)]
    for cx,p in zip(positions,panels):
        role,data,*aug=p;cols=len(data[0])if isinstance(data,list)else data.cols
        out+=matrix(cx,76,data,role,aug[0]if aug else None,min(48,(190 if len(panels)==3 else 260)/cols),36)
    for i,line in enumerate(lines):out+=txt(380,281+28*i,line,19)
    return out+extra+'</svg>'

def model(key,kind,reading,frames,scope):
    setmodel(key,kind,reading,frames,scope)
    MODELS[key]['audit']['builder']='research/deep-library-revision/l_rank-problem-visual-rebuild.py'

def exactrow(a,b):
    if a==b:return True
    changed=[i for i in range(a.rows)if a.row(i)!=b.row(i)]
    if len(changed)==2:
        i,j=changed
        return a.row(i)==b.row(j)and a.row(j)==b.row(i)
    if len(changed)!=1:return False
    i=changed[0];old=a.row(i);new=b.row(i)
    if any(old):
        c=next(j for j in range(a.cols)if old[j]);q=new[c]/old[c]
        if q!=0 and new==q*old:return True
    diff=new-old
    for j in range(a.rows):
        if j==i or not any(a.row(j)):continue
        c=next(k for k in range(a.cols)if a[j,k]);q=diff[c]/a[j,c]
        if diff==q*a.row(j):return True
    return False

qs=json.loads((ROOT/'research/l_rank-questions.json').read_text(encoding='utf8'))
for index,q in enumerate(qs[:12],3):
    key='l_rank-q'+str(index);a=M(q['certificate']['input']);r=a.rank();previous=a;frames=[]
    for k,f in enumerate(BASE_MODELS[key]['frames']):
        current=M(f['matrix']);check(key+' elementary checkpoint '+str(k),exactrow(previous,current))
        check(key+' invariant row space '+str(k),current.rref()[0]==a.rref()[0])
        caption=f['caption'].replace('Original matrix.','Original coefficient matrix.')
        frames.append(frame('Exact coefficient reduction: '+q['id'],[('Original A',a),('Current matrix',current)],
            [f'{a.rows} output coordinates; {a.cols} input coordinates',f'Rank = {r}; right nullity = {a.cols-r}',f'Left nullity = {a.rows-r}; no load column is present'],
            caption,'This reversible operation preserves row space and every right-kernel vector. Original pivot indices still select original columns.',
            {'input':a,'matrix':current,'rank':r,'question':q['id']}))
        previous=current
    check(key+' exact endpoint',previous==M(q['certificate']['rref']))
    model(key,'exact-four-space-reduction','Compare original and current coefficient matrices. Every column is an input coordinate; no last column is treated as a load.',frames,
        'Actual input '+q['id']+'. Exact rational operation checkpoints; written solutions give all four bases and explicit load restrictions.')

A=M([[1,0],[0,0],[0,0]]);B=M([[0,0],[1,0],[0,1]])
check('block load ranks',(A.rank(),A.row_join(B).rank())==(1,3))
model('l_rank-q24','multiple-load-compatibility','Compare the original image with each separate required output.',[
 frame('Two loads outside the original image',[('Coefficient A',A),('Required columns B',B)],['A(u,v)ᵀ = (u,0,0)ᵀ','b₁ = e₂ and b₂ = e₃ are both unattainable'],
 'The two load columns are two different output demands.','Neither can be produced by the only nonzero output direction.',{'A':A,'B':B}),
 frame('Augmentation adds two independent directions',[('Concatenation [A | B]',A.row_join(B))],['rank A = 1; rank [A | B] = 3','Rank increase = 2; AX = B has no solution'],
 'Keep both load columns when computing the augmented span.','The zero second coefficient column does not erase either independent load direction.',{'augmented':A.row_join(B),'rank':3})],
 'LR22 actual two-load matrices; a block of two loads can raise rank by two.')

At=M([[1,0],[0,1],[1,1]]);L=M([[1,0,0],[0,1,0]]); y=M([[-1,-1,1]])
check('left inverse',L*At==S.eye(2)and y*At==S.zeros(1,2))
model('l_rank-q26','left-inverse-family','The inverse recovers two input coordinates; correction rows must annihilate the three-coordinate output image.',[
 frame('A left inverse acts on the input identity',[('Tall A',At),('Left inverse L₀',L)],['L₀A = I₂','The other product is 3 × 3 and need not be I₃.'],
 'Read the product order and identity size.','Left inversion recovers the original two-coordinate input.',{'A':At,'L0':L}),
 frame('All correction rows lie in one left-kernel line',[('One annihilating row',y),('Its product with A',y*At)],['L = L₀ + [s; t](−1,−1,1)','(L − L₀)A = 0 for every s,t'],
 'Add one independent multiple to each inverse row.','Both row corrections vanish on every attainable output.',{'annihilator':y,'zeroProduct':y*At})],
 'LR24 actual tall matrix; the two arbitrary coefficients give the complete family.')

Aw=M([[1,0,1],[0,1,1]]);R=M([[1,0],[0,1],[0,0]]);v=M([-1,-1,1])
check('right inverse',Aw*R==S.eye(2)and Aw*v==S.zeros(2,1))
model('l_rank-q27','right-inverse-family','Each right-inverse column chooses one preimage of a different standard output.',[
 frame('A right inverse selects preimages',[('Wide A',Aw),('Right inverse R₀',R)],['AR₀ = I₂','Three input coordinates recover every two-coordinate load.'],
 'Multiply A by each selected inverse column.','The resulting columns are the two standard output vectors.',{'A':Aw,'R0':R}),
 frame('Kernel corrections change choices, not outputs',[('Kernel direction v',v),('Av',Aw*v)],['R = R₀ + v(s,t)','AR = I₂ for all s,t; no left inverse exists.'],
 'Change either inverse column independently along the same kernel.','The correction is annihilated, but its nonzero direction prevents input uniqueness.',{'v':v,'Av':Aw*v})],
 'LR25 actual wide matrix; two independent correction coordinates.')

Ai=M([[1,0],[0,1],[0,0]]);Li=M([[1,0,0],[0,1,0]])
check('norm bound example',Ai.T*Ai==S.eye(2)and Li*Ai==S.eye(2))
model('l_rank-q29','rectangular-norm-bound','Separate perfect input recovery from the missing third output direction.',[
 frame('A lower norm bound does not give every output',[('Isometric embedding A',Ai)],['A(x₁,x₂)ᵀ = (x₁,x₂,0)ᵀ','‖Ax‖₂ = ‖x‖₂, but e₃ is not attained.'],
 'Inspect the always-zero output coordinate.','The lower bound is compatible with a proper output plane.',{'A':Ai,'Gram':Ai.T*Ai}),
 frame('The products have different sizes',[('LA',Li*Ai),('AL',Ai*Li)],['LA = I₂; AL = diag(1,1,0)','Left inverse exists; right inverse is impossible.'],
 'Compare the two actual products.','The second product projects outputs onto the attainable plane.',{'LA':Li*Ai,'AL':Ai*Li})],
 'LR27 actual isometric embedding and explicit inverse products.')

Ac=M([[1,2,1],[2,4,0],[0,0,1]]);C=Ac[:,[0,2]];F=M([[1,2,0],[0,0,1]])
check('rank factorization',C*F==Ac and C.rank()==F.rank()==2)
model('l_rank-q32','rank-factorization','Follow the independent column coordinates through an exact two-coordinate bottleneck.',[
 frame('Choose actual independent columns',[('Original A',Ac)],['a₂ = 2a₁; a₁ and a₃ are independent.','rank A = 2, so one intermediate coordinate cannot suffice.'],
 'Locate dependencies before choosing factors.','The first and third columns form a basis of the image.',{'A':Ac,'rank':2}),
 frame('Separate the image basis and coordinate map',[('Image basis C',C),('Coordinate map F',F)],['A = CF','Fx = (x₁ + 2x₂, x₃)ᵀ'],
 'Read each column of F as coordinates in C.','Multiplication reconstructs each original column exactly.',{'C':C,'F':F,'product':C*F})],
 'LR30 exact matrices and their minimal rank bottleneck.')

X=M([[1,2,0],[0,0,1]])
model('l_rank-q50','selected-minor-counterexample','A zero selected minor must be compared with the other column pairs.',[
 frame('The first column pair is dependent',[('Actual A',X)],['det A[:,{1,2}] = 0','A zero selected minor does not establish rank ≤ 1.'],
 'Inspect the first two proportional columns.','Their dependence says nothing about the independent third column.',{'A':X,'selectedMinor':0}),
 frame('A different minor certifies maximal row rank',[('Columns 1 and 3',X[:,[0,2]])],['det A[:,{1,3}] = 1','rank A ≥ 2 and rank A ≤ 2, so rank A = 2.'],
 'Use a nonzero minor for the missing lower bound.','Two rows already give the matching upper bound.',{'minor':X[:,[0,2]],'determinant':1})],
 'LR48 actual matrix; the nonzero minor remains valid in characteristic two.')

H=M([[1,1],[1,-1]]);H2=M([[1,1],[1,1]])
check('field-dependent ranks',H.rank()==2 and H2.rank()==1)
model('l_rank-q52','scalar-field-rank','Interpret coefficients in the declared field before deciding whether a pivot is zero.',[
 frame('Real subtraction retains a second pivot',[('Real A',H),('Real echelon form',M([[1,1],[0,-2]]))],['Over ℝ: −2 ≠ 0, so rank = 2.','Kernel = {0}.'],
 'Subtract the first row from the second.','The nonzero second pivot makes the real matrix invertible.',{'field':'R','A':H,'rank':2}),
 frame('Characteristic two makes the rows identical',[('A reduced modulo 2',H2),('Echelon form over F₂',M([[1,1],[0,0]]))],['Over F₂: −1 = 1 and −2 = 0.','rank = 1; kernel = span(1,1)ᵀ'],
 'Reduce integer coefficients modulo two.','The surviving row supplies only one independent restriction.',{'field':'F2','A':H2,'rank':1})],
 'LR50 real versus field-of-two-elements computation; displayed echelon claims use the stated field.')

S0=M([[2,1,3],[0,1,1],[2,2,4]]);E=M([[1,0,0],[0,1,0],[-1,-1,1]])
check('Schur exceptional',E*S0==M([[2,1,3],[0,1,1],[0,0,0]])and S0.rank()==2)
model('l_rank-q55','schur-parameter-branch','Use a legal parameter-independent row operation before dividing by the Schur scalar.',[
 frame('A fixed invertible leading block',[('A at the exceptional t = 4',S0)],['R₃ ← R₃ − R₁ − R₂','For general t, the new bottom entry is t − 4.'],
 'Use the actual leading rows to clear the bottom-left block.','The leading two-by-two determinant is 2 and never vanishes.',{'A4':S0,'E':E}),
 frame('The exceptional scalar removes exactly one pivot',[('EA at t = 4',E*S0)],['t = 4 ⇒ rank 2; t ≠ 4 ⇒ rank 3','At t = 4: kernel = span(−1,−1,1)ᵀ'],
 'Separate the zero and nonzero scalar branches.','The first two pivots remain nonzero on both branches.',{'EA4':E*S0,'rankAt4':2})],
 'LR53 actual Schur example; finite exceptional checkpoint plus exact symbolic t−4 argument.')

N=M([[0,1],[0,0]])
model('l_rank-q56','off-diagonal-rank-counterexample','The upper off-diagonal block can transfer an independent input even when both diagonal blocks vanish.',[
 frame('Zero diagonal does not imply zero rank',[('Actual triangular M',N)],['M(x₁,x₂)ᵀ = (x₂,0)ᵀ','rank M = 1; diagonal-block rank sum = 0'],
 'Trace the second input coordinate to the first output.','The nonzero off-diagonal column generates a line.',{'M':N,'rank':N.rank()}),
 frame('The nonzero column is the rank certificate',[('Second column',N[:,1])],['Image = span e₁; kernel = span e₁','An inverse of the zero leading block does not exist.'],
 'Use an actual nonzero image generator.','Block-diagonal additivity does not apply to this triangular matrix.',{'imageBasis':N[:,1],'kernelBasis':M([1,0])})],
 'LR54 actual nilpotent triangular counterexample, not a generic matrix gallery.')

u=M([1,2,0]);v=M([-1,0,0]);U=S.eye(3)+u*v.T
check('rank-one loss',U*u==S.zeros(3,1)and U.rank()==2)
model('l_rank-q58','rank-one-kernel-creation','The scalar 1+vᵀu determines whether this actual identity update acquires a kernel.',[
 frame('Insert the actual outer product',[('Original I₃',S.eye(3)),('Update uvᵀ',u*v.T)],['vᵀu = −1, so 1 + vᵀu = 0.','(I₃ + uvᵀ)u = 0'],
 'Test the exceptional scalar before using an inverse formula.','The nonzero vector u becomes an annihilated input.',{'u':u,'v':v,'update':u*v.T}),
 frame('Solve the resulting kernel exactly',[('Updated matrix',U),('Kernel generator',u)],['−2x₁ + x₂ = 0; x₃ = 0','Kernel = span u; rank = 3 − 1 = 2'],
 'Every kernel vector is a multiple of u.','This upper bound on kernel dimension rules out a larger rank loss.',{'matrix':U,'kernel':u,'rank':2})],
 'LR56 actual three-by-three update; the general teaching update scene has different dimensions and is not attached here.')

P=M([[1,2],[0,0]]);x=M([1,1]);px=P*x;qx=x-px
check('oblique exact decomposition',P*P==P and P*qx==S.zeros(2,1)and px+qx==x)
model('l_rank-q61','oblique-direct-decomposition','Separate repeated-action idempotence from Euclidean orthogonality.',[
 frame('A projection with a slanted kernel',[('Actual P',P),('Kernel generator',M([-2,1]))],['P² = P; image = span e₁','e₁ · (−2,1) = −2 ≠ 0'],
 'Compare the actual image and kernel directions.','They are complementary but not perpendicular.',{'P':P,'kernel':M([-2,1])}),
 frame('One vector splits into two nonorthogonal parts',[('Px for x = (1,1)ᵀ',px),('(I−P)x',qx)],['(1,1)ᵀ = (3,0)ᵀ + (−2,1)ᵀ','P fixes the first part and kills the second.'],
 'Verify both summands and their sum.','The example illustrates the full arbitrary-vector formula in the written solution.',{'x':x,'Px':px,'complement':qx})],
 'LR59 actual projection; x=(1,1) is an explicit illustration of its universal decomposition.')

T=M([[0,1],[0,0]])
model('l_rank-q80','rank-with-zero-trace','One nonzero image direction need not appear as a nonzero diagonal entry.',[
 frame('Rank one, trace zero',[('Actual A',T)],['Ae₂ = e₁ and Ae₁ = 0','rank A = 1; trace A = 0'],
 'Use the nonzero second column to certify rank.','The diagonal alone does not count independent columns.',{'A':T,'rank':1,'trace':0}),
 frame('The missing projection hypothesis',[('A²',T*T),('A',T)],['A² = 0 ≠ A','The idempotent rank–trace theorem does not apply.'],
 'Check the theorem’s algebraic hypothesis.','A square-zero map is not a nonzero idempotent map.',{'square':T*T,'A':T})],
 'LR78 actual rank-one nilpotent example and failed projection hypothesis.')

Ar=M([[3,4],[1,2]]);coeff=M([[S.Rational(1,2),S.Rational(-1,2)]])
check('row-membership coefficients',coeff*Ar==M([[1,1]])and Ar.det()==2)
model('l_rank-q85','row-coefficient-membership','Row coefficients solve a transposed system and combine the actual original rows.',[
 frame('Ask for a combination of the original rows',[('Original row matrix',Ar)],['s(3,4) + t(1,2) = (1,1)','3s + t = 1; 4s + 2t = 1'],
 'Set up the coordinate equations for row coefficients.','The unknowns weight rows, not columns.',{'A':Ar,'target':M([[1,1]])}),
 frame('The exact coefficients certify membership',[('Coefficient row (s,t)',coeff),('Result (s,t)A',coeff*Ar)],['s = 1/2; t = −1/2','det A = 2 ≠ 0, so the row space is all of ℝ².'],
 'Multiply the proposed coefficients by the original matrix.','The result equals the target, verifying membership directly.',{'coefficients':coeff,'result':coeff*Ar})],
 'LR83 actual row-space question; the explicit weighted-row product is the membership certificate.')

diag=M([[1,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,-6]])
check('authentic trace sample',diag==diag.T and S.trace(diag)==0)
model('l_rank-authentic-dimension','symmetric-constraint-coordinates','Count only independent symmetric coordinates, then impose the single nonzero trace functional.',[
 frame('Symmetry leaves ten independent coordinates',[],['4 diagonal entries + 6 mirrored-pair choices = 10','Mirrored entries are not independent new coordinates.'],
 'Choose diagonal entries and one entry from each off-diagonal pair.','Those choices determine the entire symmetric matrix uniquely.',{'ambientDimension':10,'diagonal':4,'pairs':6}),
 frame('Trace zero fixes one diagonal coordinate',[('One admissible diagonal example',diag)],['a₄₄ = −a₁₁ − a₂₂ − a₃₃','3 diagonal + 6 pair coordinates = 9 dimensions'],
 'Use the last diagonal entry to enforce trace zero.','The nine independent basis directions are proved in the written solution.',{'example':diag,'dimension':9,'answer':2})],
 'MS CS 1405 Q41 authentic revisit; displayed example illustrates a constraint, not a substitute for the nine-vector basis proof.')

minus=-S.eye(2)
model('l_rank-authentic-norm','norm-versus-quadratic-sign','A magnitude lower bound controls invertibility, not positivity of a real quadratic form.',[
 frame('No input direction can collapse',[],['‖Ax‖ ≥ θ‖x‖ with θ > 0','Ax = 0 ⇒ x = 0 ⇒ square A is invertible.'],
 'Test a possible kernel vector in the lower inequality.','Positive norm separates zero from every nonzero input.',{'thetaPositive':True,'kernelTrivial':True}),
 frame('Negative identity disproves positivity',[('A = −I₂',minus)],['‖Ax‖ = ‖x‖ for every norm','xᵀAx = −xᵀx < 0 for nonzero real x'],
 'Check the same matrix against both the hypothesis and disputed claim.','It satisfies the norm bound but violates positive definiteness.',{'A':minus,'theta':1,'falseOption':2})],
 'PhD CS 1404 Q30 authentic revisit; the independently constructed counterexample works in every real dimension.')

keys=['l_rank-q'+str(i)for i in range(3,15)]+['l_rank-q'+str(i)for i in[24,26,27,29,32,50,52,55,56,58,61,80,85]]+['l_rank-authentic-dimension','l_rank-authentic-norm']
check('all 25 referenced old models plus 2 authentic aids',len(keys)==27)
check('all other chapter models preserved',all(MODELS[k]==v for k,v in OLD.items()if k not in keys))
PATH.write_text(json.dumps(MODELS,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
report={'state':'exact_model_audit_passed_browser_pending','models':len(keys),'frames':sum(len(MODELS[k]['frames'])for k in keys),'retainedExactTraces':12,'replacedGalleries':13,'newAuthenticAids':2,'checks':CHECKS,'nonTargetModelsUnchanged':sum(k not in keys for k in OLD),'limits':'Finite states supplement complete written proofs. Every generated state must still pass browser geometry and control inspection.'}
(ROOT/'research/deep-library-revision/l_rank-problem-visual-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print({k:v for k,v in report.items()if k!='checks'})
