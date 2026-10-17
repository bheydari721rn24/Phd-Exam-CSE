"""Rebuild only the 32 Gaussian problem aids actually referenced by the chapter.

All states use this chapter's actual inputs. SymPy assertions below are independent
of rendered strings. Other chapters and the unused Gaussian gallery stay unchanged.
"""
from pathlib import Path
import copy, hashlib, html, json, re
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'dist/chapters/problem-visual-models.json'
OLD = json.loads(PATH.read_text(encoding='utf-8'))
MODELS = copy.deepcopy(OLD)
CHAPTER = (ROOT / 'dist/chapters/l_gauss.html').read_text(encoding='utf-8')
USED = [k for k in re.findall(r'data-problem-visual="(l_gauss-q\d+)"', CHAPTER) if k!='l_gauss-q2']
Q = json.loads((ROOT / 'research/l_gauss-questions.json').read_text(encoding='utf-8'))
AUTH = json.loads((ROOT / 'research/l_gauss-authentic.json').read_text(encoding='utf-8'))
CHECKS = []
M = S.Matrix
R = S.Rational

def check(label, truth):
    assert truth, label
    CHECKS.append(label)

def plain(x):
    if isinstance(x, S.MatrixBase):
        return [[str(v) for v in row] for row in x.tolist()]
    if isinstance(x, dict): return {k: plain(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [plain(v) for v in x]
    if isinstance(x, (S.Basic,)): return str(x)
    return x

def txt(x, y, value, size=19, prose=False, anchor='middle', fill='#18384a'):
    font = 'Source Sans 3' if prose else 'STIX Two Math'
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font}" font-size="{size}" fill="{fill}">{html.escape(str(value))}</text>'

def cell(x, y, value, size=23):
    value = str(value)
    if re.fullmatch(r'-?\d+/\d+', value):
        a,b=value.split('/')
        # A real stacked fraction rather than a prose slash or substituted glyph.
        w=max(len(a),len(b))*9+12
        return txt(x,y-8,a,17)+f'<line x1="{x-w/2}" y1="{y-2}" x2="{x+w/2}" y2="{y-2}" stroke="#18384a" stroke-width="1"/>'+txt(x,y+16,b,17)
    return txt(x,y+7,value,size)

def matrix(cx, top, data, role, aug=None, step=48, rowheight=42):
    data=plain(data); n=len(data); cols=len(data[0]); width=cols*step
    left=cx-width/2; bottom=top+n*rowheight
    out=txt(cx,top-21,role,18,True)
    for i,row in enumerate(data):
        for j,v in enumerate(row):
            if aug is not None and j>=aug:
                out+=f'<rect x="{left+j*step+2}" y="{top+i*rowheight+2}" width="{step-4}" height="{rowheight-4}" rx="4" fill="#fff1d8"/>'
            out+=cell(left+(j+.5)*step,top+(i+.5)*rowheight,v)
    out+=f'<path d="M{left-2},{top}h-9v{n*rowheight}h9 M{left+width+2},{top}h9v{n*rowheight}h-9" fill="none" stroke="#557e91" stroke-width="1.5"/>'
    if aug is not None:
        x=left+aug*step
        out+=f'<line x1="{x}" y1="{top+2}" x2="{x}" y2="{bottom-2}" stroke="#b28337" stroke-width="1.4"/>'
    return out

def figure(title, panels, lines=(), extra=''):
    out=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-label="{html.escape(title,quote=True)}"><title>{html.escape(title)}</title>'
    out+=txt(380,30,title,21,True)
    positions={1:[380],2:[205,555],3:[135,380,625]}[len(panels)] if panels else []
    for cx,p in zip(positions,panels):
        role,data,*aug=p
        cols=len(data[0]) if isinstance(data,list) else data.cols
        step=min(48,190/cols) if len(panels)==3 else min(52,260/cols)
        out+=matrix(cx,91,data,role,aug[0] if aug else None,step)
    for i,line in enumerate(lines): out+=txt(380,254+29*i,line,19)
    return out+extra+'</svg>'

def frame(title, panels, lines, caption, why, state, **kw):
    return {'html':figure(title,panels,lines,kw.pop('extra','')), 'caption':caption,
            'state':plain(state), 'teaching':{'operation':caption,'why':why,
            'reading':'Inspect the named objects and exact calculation at this checkpoint. Different matrix roles are stated explicitly.',
            'guide':[], 'activeLine':None,'checks':[], 'changes':[],
            'currentState':plain(state), 'initial':False,'mode':kw.pop('mode','exact-question-derivation'),
            'counterexample':kw.pop('counterexample',False)}, **kw}

def setmodel(key, mechanism, reading, frames, scope):
    for i,f in enumerate(frames):
        f['teaching']['initial']=i==0
        f['teaching']['scope']=scope
        if i:
            a=frames[i-1]['state']; b=f['state']
            f['teaching']['changes']=[{'field':k,'before':a.get(k),'after':b.get(k)} for k in sorted(a.keys()|b.keys()) if a.get(k)!=b.get(k)]
    MODELS[key]={'kind':mechanism,'reading':reading,'frames':frames,'scope':scope,
                 'audit':{'builder':'research/deep-library-revision/l_gauss-problem-visual-rebuild.py','actualInput':True}}

# The authentic LU question: necessity, actual factors, and admissible diagonal scaling.
A=M([[3,-2,4],[0,5,1],[6,2,3]])
L=M([[1,0,0],[0,1,0],[2,R(6,5),1]])
U=M([[3,-2,4],[0,5,1],[0,0,R(-31,5)]])
D=S.diag(-1,1,1); LD=L*D; DU=D.inv()*U
check('Authentic Q33 Doolittle product',L*U==A)
check('Authentic Q33 scaled factors',LD*DU==A and LD[:,0]==M([-1,0,-2]))
setmodel('l_gauss-q1','lu-column-scaling',
 'The first column of a triangular product has one contributing term. Follow that necessity check before the actual existence construction.',[
 frame('Why the first column fixes a ratio',[('Product A',A)],['A[:,1] = u₁₁ L[:,1] = (3, 0, 6)ᵀ','L₃₁ = 2L₁₁;  L₂₁ = 0;  u₁₁ ≠ 0'],
       'Use triangularity: only u₁₁ contributes to the product’s first column.',
       'No unit diagonal was assumed. The first column is proportional to (3,0,6), rather than equal to it.',{'A':A,'firstColumn':A[:,0]}),
 frame('Construct one exact factorization',[('Unit-diagonal L₀',L),('Upper-triangular U₀',U)],['L₀U₀ = A','Row 3, column 2: 2(−2) + (6/5)5 = 2'],
       'Check an actual pair of factors before changing their normalization.',
       'The off-diagonal product checks that these are factors of the specified A, not merely matrices with the right column ratio.',{'L0':L,'U0':U,'product':A}),
 frame('Change normalization without changing the product',[('L = L₀D',LD),('U = D⁻¹U₀',DU)],['D = diag(−1, 1, 1);  DD⁻¹ = I','L[:,1] = (−1, 0, −2)ᵀ;  u₁₁ = −3'],
       'Scale column one of L and inversely scale row one of U.',
       'The inserted diagonal factors cancel. This verifies existence of the third option as well as its necessary ratio.',{'L':LD,'U':DU,'product':A})],
 'Original examination input; independently derived option 3. The permitted factors are triangular, without a unit-diagonal restriction.')

# Coefficient/load compatibility: exact zero rows retain the transformed load.
for key,A,elim,lines,why in [
 ('l_gauss-q20',M([[1,2,-1],[2,4,-2],[3,6,-3]]),M([[1,0,0],[-2,1,0],[-3,0,1]]),
 ['Eb = (b₁, b₂ − 2b₁, b₃ − 3b₁)ᵀ','Consistent ⇔ b₂ = 2b₁ and b₃ = 3b₁','x = (b₁ − 2s + t, s, t)ᵀ;  s,t ∈ ℝ'],
 'Two zero coefficient rows impose two independent load compatibility conditions. The coefficient rank is one, not three.'),
 ('l_gauss-q22',M([[1,0],[0,1],[1,1]]),M([[1,0,0],[0,1,0],[-1,-1,1]]),
 ['Eb = (b₁, b₂, b₃ − b₁ − b₂)ᵀ','Consistent ⇔ b₃ = b₁ + b₂','Compatible load ⇒ unique x = (b₁, b₂)ᵀ'],
 'The bottom zero coefficient row tests existence; the two coefficient pivots test uniqueness when that condition holds.')]:
 B=elim*A;check(key+' exact elimination',B.rref()[0]==A.rref()[0] and elim.det()!=0)
 setmodel(key,'load-compatibility', 'Keep the arbitrary load symbolic while applying exactly the same equation operations to A and b.',[
  frame('Separate coefficient structure from load conditions',[('Coefficient A',A)],['Rows are equations; b is an arbitrary load.','Changing row order or combinations must also transform b.'],
        'Identify the coefficient matrix and the separate load vector.',why,{'A':A}),
  frame('The zero coefficient rows still constrain the load',[('Invertible row map E',elim),('Transformed EA',B)],lines,
        'Apply the invertible row map, then interpret each zero coefficient row.',why,{'E':elim,'EA':B,'loadConditions':lines})],
 'The coefficient matrices are fixed and the load is symbolic. No numerical sample is substituted for the all-load argument.')

# Noncanonical echelon matrices; the arrows are exact reversible row operations.
A=M([[1,1],[1,2]]);B=M([[1,1],[0,1]]);C=M([[1,1],[0,2]])
check('LG24 both REF share RREF',A.rref()[0]==B.rref()[0]==C.rref()[0]==S.eye(2))
setmodel('l_gauss-q26','echelon-versus-rref','Compare the actual legal operations with the form they produce. REF permits non-unit pivots; RREF fixes their normalization.',[
 frame('One matrix, two legal echelon forms',[('Original A',A),('REF B',B),('REF C',C)],['B: R₂ ← R₂ − R₁','C: start with B, then R₂ ← 2R₂'],
       'Produce distinct REF matrices using reversible operations.', 'Multiplication of a row by 2 is reversible and keeps echelon structure. Therefore REF is not unique.',{'A':A,'B':B,'C':C}),
 frame('Both forms reduce to the same canonical matrix',[('RREF(B) = RREF(C)',S.eye(2))],['Normalize the second pivot, then R₁ ← R₁ − R₂.','Unique RREF does not imply a unique elimination trace.'],
       'Normalize and clear above each coefficient pivot.', 'Both routes give I₂. Their different non-unit second pivots do not represent different row spaces.',{'rref':S.eye(2)})],
 'Both displayed forms are row-equivalent to this exact input. The comparison is REF nonuniqueness, not nonuniqueness of RREF.')

# Singular row map: two duplicated equations lose an independent constraint.
A=M([[1,1],[1,-1]]); b=M([1,3]); E=M([[1,1],[1,1]])
check('LG26 singular map loses rank',E.det()==0 and A.rank()==2 and (E*A).rank()==1 and E*b==M([4,4]))
setmodel('l_gauss-q28','singular-equation-map','Track the information removed by replacing both equations with their sum. A singular map is a deliberately incorrect transformation here.',[
 frame('Original equations determine one point',[('Original [A | b]',A.row_join(b),2)],['x + y = 1;  x − y = 3','Subtract: 2y = −2, so (x,y) = (2,−1)'],
       'Solve the two independent original equations.', 'Both independent constraints must survive any equivalent rewrite.',{'A':A,'b':b,'solution':[2,-1]}),
 frame('The duplicate sum erases the difference equation',[('Singular E',E),('Changed [EA | Eb]',(E*A).row_join(E*b),2)],['det(E) = 0;  both rows now say 2x = 4','Changed solutions: (2,t), t ∈ ℝ; only t = −1 is original.'],
       'Compare the original point with the enlarged line of false solutions.', 'The forward implication holds, but no inverse row transformation exists. Copying the same sum twice loses information.',{'E':E,'EA':E*A,'Eb':E*b,'solutions':'(2,t)'},counterexample=True)],
 'This animation illustrates an invalid simultaneous row replacement. It does not authorize singular equation maps as elementary row operations.')

# Synchronized and unsynchronized right-side updates side by side.
A=M([[1,1],[1,-1]]); b=M([3,1]); E=M([[1,0],[-1,1]]); B=E*A
xc=A.inv()*b; wrong=B.inv()*b
check('LG27 synchronized and incorrect solves',xc==M([2,1]) and wrong==M([R(7,2),R(-1,2)]) and A*wrong==M([3,4]))
setmodel('l_gauss-q29','synchronized-load-counterexample','A coefficient row operation is only equivalent when its right side changes with it. Compare both actual computed answers in the original equations.',[
 frame('Start with the complete augmented matrix',[('Original [A | b]',A.row_join(b),2)],['R₂ ← R₂ − R₁ must act on the full row.'],
       'Mark the load column before eliminating.', 'The right column is not decoration: it is part of each equation.',{'augmented':A.row_join(b)}),
 frame('The correct and corrupted systems differ only in the load',[('Correct [EA | Eb]',B.row_join(E*b),2),('Incorrect [EA | b]',B.row_join(b),2)],['Correct load: (3, −2)ᵀ ⇒ x = (2, 1)ᵀ','Unchanged load: (3, 1)ᵀ ⇒ x = (7/2, −1/2)ᵀ'],
       'Apply the row map to b in the correct branch only.', 'The coefficient matrices match, but their loads and solution sets do not.',{'correctAugmented':B.row_join(E*b),'wrongAugmented':B.row_join(b)},counterexample=True),
 frame('Substitution detects the corrupted answer',[('Original A',A),('Incorrect candidate',wrong),('Original A times it',A*wrong)],['A(7/2, −1/2)ᵀ = (3, 4)ᵀ ≠ (3, 1)ᵀ','Correct candidate: A(2,1)ᵀ = (3,1)ᵀ'],
       'Test answers in the original equations, not only the altered array.', 'The second equation exposes the failed synchronization immediately.',{'wrongCandidate':wrong,'originalResidual':A*wrong-b},counterexample=True)],
 'The incorrect branch is intentional and explicitly labeled. The correct branch uses one invertible equation map on both blocks.')

# Composition order, coordinate recovery, and inverse blocks are separate mechanisms.
Swap=M([[0,1],[1,0]]); T=M([[1,0],[3,1]]); E=T*Swap
check('LG28 inverse composition',E==M([[0,1],[1,3]]) and E.inv()==M([[-3,1],[1,0]]))
setmodel('l_gauss-q30','row-operation-composition','Read chronological operations from the rightmost factor acting first, and undo them in reverse order.',[
 frame('Swap first, then add three times the new first row',[('Swap S',Swap),('Row addition T',T),('Combined E = TS',E)],['A → SA → TSA','E = TS, not ST'], 'Compose the two actual elementary row maps.',
       'Left multiplication places the later operation to the left of the earlier one.',{'S':Swap,'T':T,'E':E}),
 frame('Reverse the order when undoing the operations',[('E',E),('E⁻¹ = ST⁻¹',E.inv())],['EE⁻¹ = TSST⁻¹ = I','E⁻¹E = ST⁻¹TS = I'],
       'Undo the row addition before undoing the swap.', 'S is its own inverse. Exact multiplication checks the resulting inverse in both orders.',{'E':E,'inverse':E.inv()})], 'The input A is arbitrary; these exact elementary matrices act on every two-row array.')

A=M([[1,2],[3,4]]); Qp=Swap; b=M([5,11]); y=(A*Qp).inv()*b; x=Qp*y
check('LG29 column permutation coordinates',y==M([2,1]) and x==M([1,2]) and A*y==M([4,10]) and A*x==b)
setmodel('l_gauss-q31','column-permutation-recovery','A right-side coefficient permutation changes the coordinate vector. Follow the map from new coordinates back to original coordinates.',[
 frame('Permute coefficient columns, retain the given load',[('Original A',A),('Coordinate map Q',Qp),('New coefficient AQ',A*Qp)],['AQy = b with b = (5,11)ᵀ','New variable y is not the original variable x.'],
       'Introduce the coordinate change x = Qy.', 'The load is unchanged because columns, rather than equations, were transformed.',{'A':A,'Q':Qp,'AQ':A*Qp}),
 frame('Recover and verify the original coordinates',[('New y',y),('Recovered x = Qy',x),('Original Ax',A*x)],['AQ(2,1)ᵀ = (5,11)ᵀ','A(2,1)ᵀ = (4,10)ᵀ;  A(1,2)ᵀ = (5,11)ᵀ'],
       'Apply Q before returning an answer in the original coordinates.', 'The recovered vector passes both original equations; returning y directly fails both.',{'y':y,'x':x,'Ax':A*x})], 'This is a column permutation, not an equation operation. Coordinate recovery is essential.')

A=M([[1,2],[0,1]]);Qp=M([[1,-2],[0,1]]);b=M([5,2]);x=Qp*b
check('LG30 column addition coordinates',A*Qp==S.eye(2) and x==M([1,2]) and A*x==b)
setmodel('l_gauss-q32','column-addition-recovery','Column addition simplifies the coefficient array by a right transformation. Keep the new and original coordinate vectors distinct.',[
 frame('Subtract twice column one from column two',[('Original A',A),('Coordinate map Q',Qp),('Simplified AQ',A*Qp)],['C₂ ← C₂ − 2C₁ gives AQ = I','AQy = b ⇒ y = (5,2)ᵀ'],
       'Represent the actual column addition by right multiplication.', 'The resulting identity has new variable y. It does not make b the original answer.',{'A':A,'Q':Qp,'AQ':A*Qp,'y':b}),
 frame('The coordinate map restores the original answer',[('Q',Qp),('New y',b),('Original x = Qy',x)],['x₁ = 5 − 2(2) = 1;  x₂ = 2','Ax = (1 + 2(2), 2)ᵀ = (5,2)ᵀ'],
       'Multiply the new coordinates by Q.', 'Only coefficient columns were transformed. Mixing the load column into this map would be a different operation.',{'Q':Qp,'y':b,'x':x})], 'The original and new coordinate vectors are shown separately and exact substitution verifies the original system.')

A=M([[2,1],[1,1]]); aug=A.row_join(S.eye(2)); states=[aug,Swap*aug]; states.append(M([[1,0],[-2,1]])*states[-1]);states.append(S.diag(1,-1)*states[-1]);states.append(M([[1,-1],[0,1]])*states[-1])
check('LG31 synchronized inverse blocks',states[-1][:,:2]==S.eye(2) and states[-1][:,2:]==A.inv())
captions=['Start with the original coefficients and two identity loads.','Swap the two entire rows, including both right-side columns.','Subtract twice row one from row two in both blocks.','Multiply row two by minus one in both blocks.','Clear above pivot two and read the inverse from the right block.']
setmodel('l_gauss-q33','synchronized-inverse-blocks','The right identity block records the same invertible row map that turns A into I. It is not an independent list of matrices.',[
 frame('An inverse from synchronized block reduction',[('[coefficient block | identity loads]',v,2)],
       ['Final check: AB = BA = I' if i==4 else 'Every row operation acts on all four columns.'],caption,
       'At the final checkpoint the left block is I and the right block is the accumulated inverse transformation.',{'augmented':v},mode='synchronized-block-reduction')
 for i,(v,caption) in enumerate(zip(states,captions))], 'Exact Gauss–Jordan block states for this A; both inverse products are independently checked.')

A=M([[1,2],[2,4]]);E=M([[1,0],[-2,1]])
check('LG32 singular inverse obstruction',E*A==M([[1,2],[0,0]]) and E.det()==1)
setmodel('l_gauss-q34','singular-inverse-compatibility','An invertible row transformation exists, but the singular coefficient block cannot become I. The surviving right row supplies the load test.',[
 frame('Begin the inverse attempt',[('[A | I]',A.row_join(S.eye(2)),2)],['R₂ ← R₂ − 2R₁'], 'Start with two identity loads attached to the coefficient matrix.',
       'The coefficient rows are dependent before reduction.',{'augmented':A.row_join(S.eye(2))}),
 frame('A zero coefficient row prevents an inverse',[('[EA | E]',(E*A).row_join(E),2)],['EA has zero row, while E remains invertible.','Applied to arbitrary b: 0 = b₂ − 2b₁'],
       'Interpret the nonzero right row as a compatibility certificate.', 'E is a row-operation matrix, not an inverse of A. Its second row annihilates A and tests each proposed load.',{'EA':E*A,'E':E})], 'The failed inverse construction is informative: it exposes inconsistent loads. No inverse of the singular coefficient matrix is asserted.')

A=M([[1,0],[0,1],[1,1]]); B=M([[1,0,0],[0,1,0]])
check('LG33 one-sided inverse',B*A==S.eye(2) and A*B!=S.eye(3) and (A*B)**2==A*B)
setmodel('l_gauss-q35','rectangular-left-inverse','Compare dimensions and the two product orders. A left inverse recovers compatible coordinates without making every load attainable.',[
 frame('A 2-by-3 map can undo A on its domain',[('A: 3 × 2',A),('B: 2 × 3',B),('BA = I₂',B*A)],['For compatible b = Ax: Bb = BAx = x'],
       'Multiply in the order that acts on the original two coordinates.', 'A has independent coefficient columns. B recovers x from a compatible load.',{'A':A,'B':B,'BA':B*A}),
 frame('The reverse product is not the 3-by-3 identity',[('AB: 3 × 3',A*B)],['ABb = (b₁, b₂, b₁ + b₂)ᵀ','ABb = b ⇔ b₃ = b₁ + b₂'],
       'Test which three-dimensional loads survive the reverse product.', 'A left inverse does not imply surjectivity onto the three-dimensional load space.',{'AB':A*B,'compatibility':'b3=b1+b2'})], 'The comparison uses exact rectangular products. The drawing does not represent AB as an orthogonal projection.')

# LU factorization, actual elimination multipliers, and load-specific triangular solves.
A=M([[2,1,1],[4,-6,0],[-2,7,2]]);L=M([[1,0,0],[2,1,0],[-1,-1,1]]);U=M([[2,1,1],[0,-8,-2],[0,0,1]]);b=M([5,-2,9]);y=L.inv()*b;x=U.inv()*y
check('LG34 factors and triangular solves',L*U==A and y==M([5,-12,2]) and x==M([1,1,2]) and A*x==b)
stage=M([[2,1,1],[0,-8,-2],[0,8,3]])
setmodel('l_gauss-q36','lu-elimination-and-solves','First derive the multipliers from their correct elimination stages. Then use the fixed factors in forward and backward substitution.',[
 frame('The second multiplier uses the updated row',[('Original A',A),('After column-one elimination',stage)],['l₂₁ = 4/2 = 2;  l₃₁ = −2/2 = −1','l₃₂ = 8/(−8) = −1;  not 7/(−6)'],
       'Recompute the stage-two multiplier from the updated entries.', 'The original 7 and −6 are not the entries used at the second elimination stage.',{'A':A,'stageAfterFirstPivot':stage,'multipliers':[2,-1,-1]}),
 frame('Store multipliers and certify the factors',[('Unit-lower L',L),('Upper U',U)],['LU = A','Row 3: −U₁ − U₂ + U₃ = (−2,7,2)'],
       'Place the actual stage multipliers in L.', 'The product verifies the stored multipliers, including the second-stage value −1.',{'L':L,'U':U,'product':L*U}),
 frame('Forward solve Ly = b, then backward solve Ux = y',[('Given b',b),('Intermediate y',y),('Original x',x)],['y₁ = 5;  y₂ = −2 − 2(5) = −12;  y₃ = 9 + 5 − 12 = 2','x₃ = 2;  x₂ = (−12 + 4)/(−8) = 1;  x₁ = (5 − 1 − 2)/2 = 1'],
       'Carry the actual load through both triangular systems.', 'L and U act in different steps. Direct substitution also gives Ax=(5,−2,9).',{'b':b,'y':y,'x':x})], 'The exact factors and load match LG34. Multipliers are computed from updated matrices, never interpolated between elimination states.')

A=Swap
check('LG35 pivoted factorization',A*A==S.eye(2))
setmodel('l_gauss-q37','zero-pivot-ordering-obstruction','A zero first entry can obstruct a fixed triangular factorization while a row permutation produces a valid pivoted one.',[
 frame('Invertible does not imply this unpivoted ordering works',[('Invertible A',A)],['det(A) = −1, but a₁₁ = 0','If A = LU were invertible: l₁₁u₁₁ ≠ 0, a contradiction.'],
       'Use the nonzero diagonal requirement of invertible triangular factors.', 'The top-left product in a lower-times-upper factorization contains only l₁₁u₁₁.',{'A':A,'determinant':A.det()}),
 frame('A row swap repairs the pivot ordering',[('Permutation P = A',A),('PA = I',A*A)],['PA = LU with L = U = I','The obstruction belongs to the ordering, not to invertibility.'],
       'Pivot the rows before constructing triangular factors.', 'The permuted coefficient matrix is exactly I, so the pivoted factorization is explicit.',{'P':A,'PA':A*A,'L':S.eye(2),'U':S.eye(2)})], 'The impossibility claim concerns square triangular factors in the original row order. A pivoted factorization is shown separately.')

A=M([[4,2,0],[2,1,1],[1,3,1]]);P=M([[1,0,0],[0,0,1],[0,1,0]]);L=M([[1,0,0],[R(1,4),1,0],[R(1,2),0,1]]);U=M([[4,2,0],[0,R(5,2),1],[0,0,1]])
stage=M([[4,2,0],[0,0,1],[0,R(5,2),1]])
bad=M([[1,0,0],[R(1,2),1,0],[R(1,4),0,1]])
check('LG36 later swap factors',L*U==P*A and bad*U!=P*A)
setmodel('l_gauss-q38','later-pivot-multiplier-permutation','At a later pivot, swap the active rows and the already stored multiplier entries. Both changes are needed for PA=LU.',[
 frame('A later zero pivot appears after valid first elimination',[('After first pivot',stage)],['Stored multipliers before swapping: l₂₁ = 1/2, l₃₁ = 1/4','Stage two: swap rows 2 and 3 to use pivot 5/2.'],
       'Detect the second-stage zero pivot using the updated array.', 'The first pivot is already valid. Its multiplier records still follow their original equation rows.',{'stage':stage,'storedMultipliers':[R(1,2),R(1,4)]}),
 frame('Move the old multipliers with their equations',[('Permutation P',P),('Correct L',L),('Upper U',U)],['After swapping: l₂₁ = 1/4, l₃₁ = 1/2','LU = PA, whose first column is (4,1,2)ᵀ'],
       'Swap the first-column entries already stored in L.', 'The factors reconstruct the permuted equations. The diagonal ones remain in their triangular positions.',{'P':P,'L':L,'U':U,'product':L*U}),
 frame('Keeping the old multipliers reconstructs the wrong rows',[('Incorrect old-order L',bad),('Wrong product',bad*U),('Required PA',P*A)],['Wrong product first column: (4,2,1)ᵀ','Required first column: (4,1,2)ᵀ'],
       'Compare the failed reconstruction with the required permuted matrix.', 'Triangular shape alone does not prove a correct factorization.',{'wrongL':bad,'wrongProduct':bad*U,'required':P*A},counterexample=True)],
 'The permutation and factors are exact for LG36. The final intentionally incorrect branch isolates the multiplier-ordering error.')

L=M([[1,0],[2,1]]);U=M([[3,1],[0,2]]);A=L*U;loads=[M([4,10]),M([1,0])]; ys=[L.inv()*b for b in loads];xs=[U.inv()*y for y in ys]
check('LG42 reused exact factors',A==M([[3,1],[6,4]]) and xs==[M([1,1]),M([R(2,3),-1])] and all(A*x==b for x,b in zip(xs,loads)))
setmodel('l_gauss-q44','reuse-factor-two-loads','The factors stay fixed; each load has its own intermediate y and solution x. Compare both forward/backward chains.',[
 frame('Factor once, solve multiple loads',[('Fixed L',L),('Fixed U',U),('Common A = LU',A)],['A is unchanged when the requested load changes.'],
       'Check the common coefficient matrix reconstructed by the factors.', 'There is no need to form a full inverse for these two solves.',{'L':L,'U':U,'A':A}),
 *[frame('Load '+str(i+1)+': forward and backward substitution',[('Given b',b),('Ly = b gives y',y),('Ux = y gives x',x)],
       ['y₂ = b₂ − 2b₁;  x₂ = y₂/2;  x₁ = (y₁ − x₂)/3',
        f'Ax = ({b[0]}, {b[1]})ᵀ = b'],
       'Use the same L and U with this load’s own triangular solves.', 'An intermediate vector belongs to its load; it must not be reused as the intermediate vector for the other load.',{'b':b,'y':y,'x':x}) for i,(b,y,x) in enumerate(zip(loads,ys,xs))]],
 'Both fixed factors and both actual loads match LG42. Each arithmetic chain is independently substituted into the original coefficient matrix.')

A=M([[2,1],[4,3]]);b=M([3,7]);aug=A.row_join(b);good=M([[1,0],[-2,1]])*aug;bad=M([[2,1,3],[0,3,7]])
check('LG52 overwrite invariant',good==M([[2,1,3],[0,1,1]]) and A.inv()*b==M([1,1]) and bad[:,:2].inv()*bad[:,2]==M([R(1,3),R(7,3)]))
setmodel('l_gauss-q54','in-place-overwrite-data-dependency','The multiplier depends on the old pivot-column entry. Save that value before writing the known zero.',[
 frame('Read the multiplier before overwriting its input',[('Original augmented array',aug,2)],['Save m = old a₂₁/a₁₁ = 4/2 = 2','Then update trailing entries using this saved m.'],
       'Read the old entry 4 and retain multiplier 2.', 'The pivot row must also remain unchanged during this row update.',{'augmented':aug,'savedMultiplier':2}),
 frame('Correct saved value versus overwritten value',[('Correct update',good,2),('Corrupted update',bad,2)],['Saved m=2: (3,7) − 2(1,3) = (1,1)','Recomputed m=0 after overwrite: trailing (3,7) is unchanged.'],
       'Compare the actual trailing entries in the two execution orders.', 'The corrupted row says 3y=7 rather than y=1. It is not the original system under a reversible row map.',{'correct':good,'corrupted':bad},counterexample=True)],
 'The bad branch is a deliberately incorrect in-place implementation. The state records expose the exact read-before-write dependency.')

A=M([[1,0],[1,0]]);E=M([[1,0],[-1,1]]);B=E*A
check('LG55 invariant and moving spaces',A.rowspace()==B.rowspace() and A.nullspace()==B.nullspace() and A.columnspace()!=B.columnspace())
# Two actual column lines in the same coordinate axes, not unrelated matrix cards.
geometry='<g><line x1="70" y1="182" x2="690" y2="182" stroke="#a1b7c1"/><line x1="380" y1="69" x2="380" y2="282" stroke="#a1b7c1"/><line x1="285" y1="277" x2="475" y2="87" stroke="#477c99" stroke-width="3"/><line x1="130" y1="182" x2="630" y2="182" stroke="#be8129" stroke-width="3"/>'+txt(495,85,'Col(A): y = x',18,True)+txt(596,163,'Col(EA): y = 0',18,True)+txt(397,204,'0',17)+'</g>'
setmodel('l_gauss-q57','row-versus-column-subspaces','Compare the row vectors, null equation, and column vectors separately. Only the column subspace moves in this example.',[
 frame('One row operation, three different subspace questions',[('Original A',A),('Row-reduced EA',B)],['Row(A) = Row(EA) = span{(1,0)}','Ker(A) = Ker(EA) = span{(0,1)ᵀ}'],
       'Inspect the unchanged row span and unchanged homogeneous equation.', 'Both matrices impose x₁=0 in the homogeneous system; a row map changes equations without changing that solution set.',{'A':A,'EA':B,'rowBasis':[[1,0]],'kernelBasis':[[0],[1]]}),
 frame('Equal column rank does not mean the same column line',[],['E(1,1)ᵀ = (1,0)ᵀ','Both column spaces have dimension 1, but are distinct.'],
       'Draw the actual original and transformed column lines in one load plane.', 'The invertible left map carries one line to the other. It preserves dimension, not equality of the two embedded subspaces.',{'originalColumnBasis':[[1],[1]],'changedColumnBasis':[[1],[0]],'rank':1},extra=geometry)],
 'The common-coordinate line drawing shows these exact column spaces. It makes no claim that general row maps preserve Euclidean angles or lengths.')

A=M([[1,1],[2,2]]);E=M([[1,0],[-2,1]]);b1=M([1,2]);b2=M([1,3])
check('LG61 identical singular coefficients different consistency',A.det()==0 and E*b1==M([1,0]) and E*b2==M([1,1]))
setmodel('l_gauss-q63','same-coefficients-different-loads','Hold the singular coefficient matrix fixed and change only the load. A determinant cannot distinguish these two consistency outcomes.',[
 frame('Same singular A, two different augmented systems',[('Compatible load',A.row_join(b1),2),('Incompatible load',A.row_join(b2),2)],['det(A) = 0 in both cases','Apply R₂ ← R₂ − 2R₁ to each complete system.'],
       'Keep the identical coefficient arrays visually aligned.', 'The determinant belongs to A alone and is identical for both requested solves.',{'A':A,'firstLoad':b1,'secondLoad':b2}),
 frame('The transformed load decides the outcome',[('Zero row gives 0 = 0',(E*A).row_join(E*b1),2),('Zero row gives 0 = 1',(E*A).row_join(E*b2),2)],['Left: (x,y) = (1−t,t), t ∈ ℝ','Right: contradiction, so no solution'],
       'Read both augmented zero rows as equations.', 'The same deficient coefficient rank permits infinitely many solutions when compatible and no solution when incompatible.',{'firstReduced':(E*A).row_join(E*b1),'secondReduced':(E*A).row_join(E*b2)})],
 'This is an exact comparison of two loads for one fixed A. The failure of invertibility alone does not decide consistency.')

L=M([[1,0,0],[2,1,0],[-1,3,1]]);N=L-S.eye(3);N2=N*N;inv=S.eye(3)-N+N2
check('LG63 nilpotent inverse and cross term',N**3==S.zeros(3) and N2[2,0]==6 and L*inv==S.eye(3) and inv*L==S.eye(3))
setmodel('l_gauss-q65','nilpotent-path-correction','The indirect lower-triangular path contributes an extra term. Follow the exact N² entry before checking the finite inverse series.',[
 frame('Split the unit-lower matrix into I + N',[('Strictly lower N',N),('Path-product N²',N2)],['(N²)₃₁ = N₃₂N₂₁ = 3(2) = 6','N³ = 0; all paths of length three vanish.'],
       'Compute the indirect contribution through index two.', 'Only the (3,1) entry of N² survives. Merely changing signs cannot include that two-step contribution.',{'N':N,'N2':N2,'N3':N**3}),
 frame('Terminate the inverse series and certify it',[('L = I + N',L),('L⁻¹ = I − N + N²',inv)],['(L⁻¹)₃₁ = 1 + 6 = 7','Third-row first-column product: −1 − 6 + 7 = 0'],
       'Add the N² correction before checking the inverse.', 'The product (I+N)(I−N+N²)=I+N³ equals I; both exact multiplication orders are also verified.',{'L':L,'inverse':inv,'product':L*inv})],
 'The finite series is exact because this strictly lower three-by-three N has N³=0. The indirect contribution is computed from the actual entries.')

# Retain all exact row traces, verify each elementary step, add semantic roles.
TRACE_REPORT=[]
for key in USED:
    if OLD[key]['kind']!='exact-row-reduction': continue
    entry=copy.deepcopy(OLD[key]); number=int(key.split('q')[1])-2
    question=Q[number-1]; original=M(question['certificate']['input'])
    check(key+' trace input matches certificate',M(entry['frames'][0]['matrix'])==original)
    prev=None
    for i,f in enumerate(entry['frames']):
        current=M(f['matrix']); operation=f['caption']
        if prev is not None:
            expected=prev.copy()
            match=re.fullmatch(r'Swap rows (\d+) and (\d+)\. The solution set is unchanged\.',operation)
            div=re.fullmatch(r'Divide row (\d+) by the nonzero pivot (.+)\. Apply the operation to the entire row\.',operation)
            sub=re.fullmatch(r'Row (\d+) ← row (\d+) − \((.+)\) × row (\d+)\. Only this row is replaced\.',operation)
            if match: expected.row_swap(int(match[1])-1,int(match[2])-1)
            elif div:
                j=int(div[1])-1; factor=S.Rational(div[2]);check(key+f' nonzero divisor {i}',factor!=0);expected[j,:]=expected[j,:]/factor
            elif sub:
                j=int(sub[1])-1;check(key+f' same destination {i}',sub[1]==sub[2]);expected[j,:]=expected[j,:]-S.Rational(sub[3])*expected[int(sub[4])-1,:]
            else: raise AssertionError((key,operation))
            check(key+f' exact elementary transition {i}',current==expected)
        prev=current
        n=current.cols-1; coeff=current[:,:n]; load=current[:,n:]
        f['html']=figure('Actual augmented system: '+question['id'],[('[coefficients | load]',current,n)],
                         ['Amber cells are the transformed load, not coefficient variables.',
                          'Coefficient pivots determine free coordinates; a contradictory load decides consistency.'])
        # Four-row traces need a narrower row height to leave the footer clear.
        if current.rows==4:
            f['html']=f['html'].replace(matrix(380,91,current,'[coefficients | load]',n,min(52,260/current.cols)),
                                                   matrix(380,73,current,'[coefficients | load]',n,min(52,260/current.cols),40))
        f['teaching']['reading']='The load column is amber and separated by a vertical rule. Coefficient columns keep their original variable meanings throughout every legal row operation.'
        f['teaching']['why']=operation+' '+('The final coefficient equations describe the complete original solution set; inspect any zero coefficient row together with its load.' if i==len(entry['frames'])-1 else 'Apply the operation to every coefficient and to the load in the same row.')
        f['teaching']['currentState']={'augmented':plain(current),'coefficientColumns':n,'loadColumns':1}
        f['teaching']['scope']='Actual question '+question['id']+'; exact elementary-operation checkpoints, not interpolated arrays.'
    expected=original.rref()[0]
    # Contradictory traces stop when a zero coefficient row has nonzero load.
    certificate=M(question['certificate']['rref'])
    check(key+' recorded endpoint matches certificate',prev==certificate)
    check(key+' final row space equals original',prev.rref()[0]==expected)
    entry['reading']='Follow this question’s exact row operations. The amber right-side column is a load, never an extra coefficient variable.'
    entry['scope']='Exact rational arithmetic for '+question['id']+'. The trace endpoint is checked against its certificate and its RREF against an independent symbolic reduction.'
    MODELS[key]=entry
    TRACE_REPORT.append({'key':key,'question':question['id'],'frames':len(entry['frames'])})

check('32 referenced Gaussian models',len(USED)==32 and len(set(USED))==32)
check('all used galleries replaced',all(MODELS[k]['kind']!='matrix-objects' for k in USED))
UNCHANGED=[k for k in OLD if k not in USED]
check('all non-target entries unchanged',all(MODELS[k]==OLD[k] for k in UNCHANGED))
for key in USED:
    for f in MODELS[key]['frames']:
        check(key+' SVG compact and font explicit '+str(MODELS[key]['frames'].index(f)),
              'viewBox="0 0 760 360"' in f['html'] and 'font-family="STIX Two Math"' in f['html'] and '<svg' in f['html'])

PATH.write_text(json.dumps(MODELS,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
REPORT={'state':'exact_model_arithmetic_passed_browser_review_required','scope':'32 referenced Gaussian problem models only',
        'referenceModels':len(USED),'retainedExactRowTraces':len(TRACE_REPORT),'rewrittenMatrixGalleries':len(USED)-len(TRACE_REPORT),
        'frames':sum(len(MODELS[k]['frames']) for k in USED),'assertions':len(CHECKS),'checks':CHECKS,'traces':TRACE_REPORT,
        'nonTargetEntriesUnchanged':len(UNCHANGED),'unusedGaussianModel':'l_gauss-q58 retained without edits',
        'questionBankSha256':hashlib.sha256((ROOT/'research/l_gauss-questions.json').read_bytes()).hexdigest(),
        'authenticBankSha256':hashlib.sha256((ROOT/'research/l_gauss-authentic.json').read_bytes()).hexdigest(),
        'limits':['Browser font, overlap, all-frame control, playback and print checks are a separate root-agent task.',
                  'Finite checkpoints supplement the written mathematical proofs; they do not themselves prove symbolic all-input claims.',
                  'The authentic nonnegative-integer counting question has no referenced problem aid on this page and is not inserted by this bounded asset task.',
                  'Only the 32 currently referenced Gaussian entries were revised. The unused Gaussian gallery and all other chapters remain unchanged.']}
(ROOT/'research/deep-library-revision/l_gauss-problem-visual-audit.json').write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in REPORT.items() if k not in ['checks','traces']},ensure_ascii=False,indent=2))
