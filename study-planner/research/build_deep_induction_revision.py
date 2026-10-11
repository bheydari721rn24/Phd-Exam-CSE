"""Build individual induction answers while retaining reviewed full teaching."""
from pathlib import Path
import ast,hashlib,html,json,re,subprocess,sys
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision';BASE='f890223f3111d27958eb483056556fded2d59ff3'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):
    v=mathml.markdown_math(s,md)
    return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',v)
from induction_question_diagrams import leaf_mass,full_shapes
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/d_induction.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw)
parts=re.split(r'^## Q(\d+)\s*$',(E/'d_induction-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
assert set(answers)==set(range(1,47))and len(entries)==46
actual={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
original={q['title']:q for f in sorted((B/'exam-calibration').glob('original-*.json'))for q in json.loads(f.read_text())if q.get('topic')=='d_induction'}
contexts=[
    r'Let $n\ge1$ be an integer and let $S_n=\sum_{k=1}^{n}k2^{k-1}$. Determine this exact finite sum.',
    r'Let $n\ge1$ be an integer and let $S_n=\sum_{k=1}^{n}k^2$. Determine this exact finite sum.',
    r'Let $n\ge1$ be the size of a finite universe. Evaluate $\sum_{k=0}^{n}k\binom nk$, interpreting the weight as a choice of a distinguished member of the selected subset.',
    r'Let $n\ge0$ be an integer. A finite nonempty rooted full binary tree has $n$ internal nodes; every internal node has exactly two children. Determine its total number of nodes, counting both internal nodes and leaves.',
    r'Let $n\ge1$ be an integer. Evaluate the finite sum $\sum_{k=1}^{n}1/[k(k+1)]$.',
    r'Let $H_0=0$ and $H_n=2H_{n-1}+1$ for integers $n\ge1$. Determine the exact recurrence value $H_n$. The separate question about minimum Hanoi moves requires the declared puzzle rules as well as a lower bound.',
    r'Let $n\ge0$ be an integer. A finite nonempty rooted full ternary tree has $n$ internal nodes; every internal node has exactly three children. Determine the number of leaves.',
    r'Let $a_0=1$ and $a_n=2+\sum_{j=0}^{n-1}a_j$ for integers $n\ge1$. Determine $a_n$ on the positive-index domain while retaining the separate initial value.'
]
boundaries=[
    'Which statement correctly identifies an obligation or boundary change in this exact-sum proof?',
    'Which statement correctly describes a valid way to prove the identity, with the necessary initial-value check?',
    'Which statement correctly treats the zero-size boundary and the marked-subset counting construction?',
    'Which statement correctly distinguishes fullness from perfection, balance and height?',
    'Which statement correctly justifies the finite telescoping calculation and its possible limit?',
    'Which statement correctly distinguishes the cost of a legal construction from a proof of minimum cost?',
    'Which statement correctly describes the branching hypotheses and the structural base?',
    'Which statement correctly describes the range of the transformed recurrence and the permitted induction hypothesis?'
]
replacements=[];records=[]
for n,(a,b,attrs,q)in enumerate(entries,1):
    prefix=q[:q.index('<details')]if n<=44 else q[:re.search(r'<p><strong>Correct option:',q).start()]
    if n<=44:
        title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1]);record=actual[attrs['data-source-id']]if n<=4 else original[re.sub(r'^Question \d+\. ','',title)]
        stem=record['stem']
        if n>=13:
            family,part=divmod(n-13,4)
            if part<2:stem=contexts[family]+f' Set $n={5 if part==0 else 8}$. What is the exact answer?'
            elif part==2:stem=contexts[family]+' Which expression gives the result for every eligible parameter?'
            else:stem=contexts[family]+' '+boundaries[family]
            if family in [3,6]:prefix=prefix.replace('Pattern reference: MS_CS_1405_Q121; MS_CS_1405_Q130.','Pattern reference: Phd_CE_1405_Q3.')
            if n==36:stem=r'In the standard three-peg Hanoi puzzle, move $n$ distinct-size disks from one peg to another, one disk at a time, without ever placing a larger disk on a smaller one. A legal recursive construction has cost $H_0=0$, $H_n=2H_{n-1}+1$. Which statement correctly describes what is needed to prove that this construction is optimal among all legal procedures?'
        end=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end()
        prefix=prefix[:end]+render(stem)+prefix[prefix.index('<div class="exam-options">'):]
    else:
        stem=(r'For a six-element universe, evaluate $\sum_{j=0}^{6}j^2\binom6j$. Derive the result by distinguishing repeated and distinct ordered markings, and check the individual summands.'if n==45 else r'Let $P(k)$ be a statement for each integer $k\ge0$. The only provided base is $P(0)$, and a proved rule gives $P(k)\Rightarrow P(k+2)$ for every $k\ge0$. Which index class is established by these premises alone? Distinguish what this scheme proves from what might independently be true.')
        begin=prefix.index('</h3>')+5;end=prefix.index('<p><strong>1.</strong>');prefix=prefix[:begin]+'<p class="exam-provenance">Original integrated induction challenge; not an authentic examination item.</p>'+render(stem)+prefix[end:]
    if n>=5:
        option=prefix.find('<div class="exam-options">')
        if option<0:option=prefix.index('<p><strong>1.</strong>')
        task='Derive the answer with explicit base and successor calculations, or a justified counting or structural proof. Explain the alternatives and the relevant boundary conditions.'
        prefix=prefix[:option]+'<p class="reasoning-task"><strong>Required reasoning.</strong> '+task+'</p>'+prefix[option:]
    prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
    visual=leaf_mass(render)if n==3 else full_shapes(render)if n==28 else ''
    if n==46:
        visual='<p><strong>Exact proof-scheme animation.</strong> The following finite prefix shows only indices justified from the supplied zero base and two-step rule. The written induction above proves the complete even chain; the animation does not assert falsehood at the odd indices.</p><section class="concept-animation question-specific-animation" data-scenes="induction-gap" aria-label="The zero base reaches only the even chain"><p>The finite prefix has established index zero; odd indices have no provided base. Use the controls to advance the justified even chain.</p><noscript>The full written derivation remains available immediately above.</noscript></section>'
    v=prefix+'<details class="exam-solution"><summary>Read the full derivation, induction and option analysis</summary>'+render(answers[n])+visual+'</details></section>'
    replacements.append((a,b,v));records.append(dict(index=n,answer=int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]),sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(replacements):page=page[:a]+v+page[b:]
bridge=render((E/'d_induction-method-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1);page=page.replace('<h2 id="worked-problems">',bridge+'<h2 id="worked-problems">',1)
rules=render((E/'d_induction-final-rules.md').read_text()).replace('<h2>','<h2 id="quick-reference">',1)
page=re.sub(r'<h2 id="quick-reference">[\s\S]*?(?=<h2 id="references">)',lambda m:rules,page,count=1)
page=page.replace('<a href="#worked-problems">','<a href="#mathematical-bridge">Mathematical constructions</a> <a href="#worked-problems">',1)
page=page.replace('Student-approved chapter','Revised review draft').replace('13 examination notes','30 examination notes')
notice='<aside class="deep-review-notice"><strong>Induction revision · 11 October 2026.</strong> All 46 solutions are rewritten individually with exact algebra, counting constructions, bases, transitions, boundary checks and option analysis. Seven added mathematical teaching sections and thirty final rules complement the retained full lesson and 24 derivation tutorials. Four authentic source meanings and option orders are retained. The five prior university-course readings are reused within their documented bounds. This is a review draft.</aside>'
page=page.replace('<article',notice+'<article',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
# Accurate ports and semantic labels for the base/successor diagram.
diagram='<figure class="logic-diagram"><svg viewBox="0 0 800 195" role="img" aria-label="A proved induction base reaches successive indices through a valid arbitrary-index implication"><defs><marker id="induction-route-tip" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#47768a"/></marker></defs>'
for j in range(4):
    x=20+j*200;formula=r'P(n_0'+('+'+str(j)if j else'')+')'
    label=render('$'+formula+'$').removeprefix('<p>').removesuffix('</p>\n')
    diagram+=f'<rect x="{x}" y="60" width="150" height="62" rx="9" fill="#f2f8fa" stroke="#a2bac6"/><foreignObject x="{x+10}" y="68" width="130" height="46"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:19px">{label}</div></foreignObject>'
    if j<3:diagram+=f'<path d="M{x+150} 91H{x+200}" fill="none" stroke="#47768a" stroke-width="2" marker-end="url(#induction-route-tip)"/>'
diagram+='<text x="95" y="40" text-anchor="middle" font-size="17">Proved base</text><text x="400" y="160" text-anchor="middle" font-size="17">Each arrow applies the same proved rule at the current eligible index.</text></svg><figcaption>The first box is independently established. Every later box depends on the valid successor implication; the diagram cannot repair a missing base or an invalid transition.</figcaption></figure>'
page,count=re.subn(r'<figure class="logic-diagram">[\s\S]*?</figure>',lambda m:diagram,page,count=1);assert count==1
# Give the existing deficient-board labels enough room in their viewBox.
page=page.replace('viewBox="0 0 510 280"','viewBox="0 0 720 280"')
coin_proof=render(r'''### The exact 3-and-5-unit construction animated below

This example uses coin values 3 and 5, separately from the 4-and-5-unit postage example above. We prove that every integer $n\ge8$ has a representation $n=3a+5b$ with integers $a,b\ge0$. Establish the three bases $8=3+5$, $9=3+3+3$ and $10=5+5$. For $n\ge11$, assume the claim for every integer from 8 through $n-1$. Since $8\le n-3<n$, write $n-3=3a+5b$ and append one 3-unit coin: $n=3(a+1)+5b$. This proves the entire tail. The three bases cover the three residue classes modulo 3, so none can be silently omitted from this particular proof scheme. The threshold is sharp: $7=3a+5b$ would force $b\in\{0,1\}$, leaving either 7 or 2 to be divisible by 3, which is impossible.

In the animation, each displayed multiset is an actual representation, not merely a claim that the amount is obtainable. The dependency card names the already established amount $n-3$; the highlighted final 3-unit coin is the constructive successor step. Bases are independently established before any such dependency is used.
''')
page=page.replace('<section id="animation-strong-induction"',coin_proof+'<section id="animation-strong-induction"',1)
euclid_proof=render(r'''### A stronger arithmetic invariant and a decreasing induction measure

The Euclidean animation below illustrates a strengthened correctness assertion for an algorithm. It is a separate application of induction and invariants, rather than a simulation of the deficient-board construction. Let the immutable inputs be $A=84$ and $B=30$. At each state maintain both $\gcd(a,b)=\gcd(A,B)$ and the coefficient equations $a=Ax_0+By_0$, $b=Ax_1+By_1$. Initially $(a,b)=(A,B)$ and the coefficient rows are $(1,0)$ and $(0,1)$.

For $b>0$, set $q=\lfloor a/b\rfloor$ and $r=a-qb$. Replace $(a,b)$ simultaneously by $(b,r)$ and the coefficient rows simultaneously by $(x_1,y_1)$ and $(x_0-qx_1,y_0-qy_1)$. The equations remain true by substitution. A number divides both $a,b$ if and only if it divides both $b,a-qb$, so the gcd invariant is also preserved. Because $0\le r<b$, the second operand is a strictly decreasing nonnegative integer until it reaches zero; this gives a well-founded termination argument. At the zero base, $\gcd(a,0)=a$ for the nonnegative operands in this demonstration.

The exact operand sequence is $(84,30)\to(30,24)\to(24,6)\to(6,0)$. The final first coefficient row is $(-1,3)$, giving the certificate $6=-84+90$. Tracking only the gcd would establish the numerical result; the stronger coefficient invariant additionally explains the linear-combination certificate. The finite animation checks this particular execution; the preceding symbolic update proves preservation for every eligible state.
''')
page=page.replace('<section id="animation-strengthening"',euclid_proof+'<section id="animation-strengthening"',1)
page=page.replace('The chapter covers the named induction patterns and the 24 independently solved problems. It does not contain all exercises in the source courses, archived Iranian examination items, or an exhaustive census of global university courses.','The retained lesson includes 24 derivation tutorials; the revised bank adds 46 individually explained authentic and original questions. This is not a reproduction of complete source-course exercise banks or an exhaustive census of global university courses.')
page=re.sub(r'<p>Each problem below is independently written[\s\S]*?</p>','<p>The revised bank combines four authentic examination translations with original mathematical and conceptual problems. The retained full lesson and its derivation tutorials synthesize the five documented university readings; complete university problem banks are not reproduced.</p>',page,count=1)
(R/'dist/chapters/d_induction.html').write_text(page,encoding='utf-8')
report=dict(topicId='d_induction',baselineCommit=BASE,status='rewritten_pending_checks',questionCount=46,authenticSourceMeaningsRetained=4,studentApproval=False,records=records)
(E/'d_induction-revision.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(questions=46,solutionWords=sum(q['words']for q in records),questionTables=sum('<table>'in v for a,b,v in replacements),nativeMathExpressions=page.count('<math'),finalRules=30),indent=2))
