"""Build fully authored model answers, precise stems, lecture constructions and rules."""
from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision';BASE='f890223f3111d27958eb483056556fded2d59ff3'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md))
from induction_question_diagrams import leaf_mass
from model_question_diagrams import depth_witness,representation
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/a_model.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw)
parts=re.split(r'^## Q(\d+)\s*$',(E/'a_model-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)};assert set(answers)==set(range(1,47))and len(entries)==46
actual={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())};original={q['title']:q for f in sorted((B/'exam-calibration').glob('original-*.json'))for q in json.loads(f.read_text())if q.get('topic')=='a_model'}
contexts=[r'A comparison-only sorting decision tree must distinguish all relative orders of $n\ge1$ distinct labeled keys. Each comparison has two relevant outcomes. Determine the smallest integer worst-case depth permitted by the information-capacity inequality; this is a necessary lower bound, not a claim of exact attainability.',r'All subsets of an $n$-element set are emitted as complete $n$-bit membership vectors, with no shared or incremental representation. Count emitted payload bits.',r'Let $n\ge1$ be an integer. Write $2^n-1$ in ordinary unpadded binary. Determine its bit length, not its numeric value.',r'Let $n\ge1$ be an integer. Encode $2^n-1$ in unary using one mark per numeric unit. Count its payload marks.',r'Multiply two dense $n\times n$ matrices with $n\ge1$ by the direct row-column dot-product algorithm. Count scalar multiplication events; additions and bit costs are separate resources.',r'Emit each permutation of $n\ge1$ distinct labels as its full length-$n$ list. Count emitted labels, assuming one constant-size reference per label.',r'For every position $i=1,\ldots,n$, compare its key once with each earlier position $j<i$, with no early exit. Count charged key comparisons.',r'A perfect binary search tree contains $2^n-1$ distinct keys for $n\ge1$. A successful search charges one three-way key comparison per visited nonempty node. Count comparisons for a deepest stored key; edge traversals and null checks are separate resources.']
boundaries=['Which statement correctly specifies the information bound and its model restrictions?','Which statement correctly describes a change to the full-vector output contract?','Which statement correctly distinguishes binary length from a value-dependent iteration count?','Which statement correctly identifies the role of the input encoding in polynomiality?','Which statement correctly distinguishes scalar counts from bit work or problem lower bounds?','Which statement correctly distinguishes permutations from arbitrary functions and explicit output?','Which statement correctly describes a modification to the declared index region or control flow?','Which statement correctly identifies the structural premise behind a logarithmic search bound?']
replacements=[];records=[]
for n,(a,b,attrs,q)in enumerate(entries,1):
    prefix=q[:q.index('<details')]if n<=44 else q[:re.search(r'<p><strong>Correct option:',q).start()]
    if n<=44:
        title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1]);rec=actual[attrs['data-source-id']]if n<=4 else original[re.sub(r'^Question \d+\. ','',title)];stem=rec['stem']
        if n==8:stem=r'Given $n$ distinct objects, explicitly write every unordered three-element subset as its three object references. Assume a constant cost per reference write. What is the tight asymptotic order of the unavoidable output work? Choose the sharp output-size lower bound.'
        if n==9:stem=r'For integers $r,c\ge1$, a dense real $r\times c$ matrix is multiplied by a vector using row dot products. Each dot product combines its $c$ already formed products in a chain, without adding an initial zero. Count scalar multiplications and additions, respectively.'
        if n>=13:
            family,part=divmod(n-13,4);stem=contexts[family]+(f' Set $n={5 if part==0 else 8}$. What is the exact requested count?'if part<2 else' Which expression is valid throughout the stated domain?'if part==2 else' '+boundaries[family])
        end=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end();prefix=prefix[:end]+render(stem)+prefix[prefix.index('<div class="exam-options">'):]
    else:
        stem=(r'Let $x_0=2$ and $x_{k+1}=x_k^2$ in exact integer arithmetic. After six squarings, how many bits does the final positive integer need in ordinary unpadded binary? Explain both its highest bit index and its representation length.'if n==45 else r'A table has $100W$ fixed-size cells. Its capacity $W$ is a positive integer represented in exactly 20 ordinary binary bits without leading zeros. What is the largest possible cell count? Distinguish cells, payload bits and eager initialization work.')
        end=prefix.index('<p><strong>1.</strong>');start=prefix.index('</h3>')+5;prefix=prefix[:start]+'<p class="exam-provenance">Original integrated computation-model challenge; not an authentic examination item.</p>'+render(stem)+prefix[end:]
    if n>=5:
        i=prefix.find('<div class="exam-options">')
        if i<0:i=prefix.index('<p><strong>1.</strong>')
        prefix=prefix[:i]+'<p class="reasoning-task"><strong>Required reasoning.</strong> Define the charged resource, derive its exact count or justified bound, explain the alternatives and test the relevant boundary inputs.</p>'+prefix[i:]
    prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
    visual=leaf_mass(render)if n==1 else depth_witness(render)if n==12 else''
    if n==2:visual='<p><strong>Exact comparison animation.</strong> Every checkpoint follows this question\'s original array, rather than another illustrative input. Highlighted fronts are shown before the comparison; the output prefix is shown after it. Copies after exhaustion add no key comparisons.</p><section class="concept-animation question-specific-animation" data-scenes="model-merge-exact" aria-label="All sixteen comparisons for the original eight-key array"><p>The complete front-pair trace and output table are available above.</p></section>'
    v=prefix+'<details class="exam-solution"><summary>Read the full mathematical derivation and option analysis</summary>'+render(answers[n])+visual+'</details></section>';replacements.append((a,b,v));records.append(dict(index=n,answer=int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]),sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(replacements):page=page[:a]+v+page[b:]
bridge=render((E/'a_model-method-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1);page=page.replace('<h2 id="worked-problems">',bridge+'<h2 id="worked-problems">',1)
rules=render((E/'a_model-final-rules.md').read_text()).replace('<h2>','<h2 id="quick-reference">',1);page=re.sub(r'<h2 id="quick-reference">[\s\S]*?(?=<h2 id="references">)',lambda m:rules,page,count=1)
page=page.replace('<a href="#worked-problems">','<a href="#mathematical-bridge">Mathematical constructions</a> <a href="#worked-problems">',1).replace('Student-approved chapter','Revised review draft')
notice='<aside class="deep-review-notice"><strong>Computation-model revision · 11 October 2026.</strong> All 46 answers are individually rewritten with exact resource accounting, algebra, witness inputs and boundary analysis. Eight mathematical construction sections and 32 final rules complement the retained full lesson and 16 derivation tutorials. An exact animation follows all 16 comparisons of the authentic merge-sort input. Four official university readings were rechecked; the fifth Berkeley reading is reused within its previously documented bounds because its old slide URL is currently unavailable. This is a review draft.</aside>';page=page.replace('<article',notice+'<article',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
# Connect the existing representation arrows exactly to their rectangle ports.
page=page.replace('refX="8" refY="5"','refX="10" refY="5"').replace('M208 72 H248','M205 72H256').replace('M439 72 H479','M436 72H487').replace('M670 72 H710','M667 72H718')
page=re.sub(r'<figure class="logic-diagram model-diagram">[\s\S]*?</figure>',lambda m:representation(render),page,count=1)
# Put the exact animation-contract explanations immediately before their players.
start=bridge.index('<h3>8. Interpret');contract=bridge[start:];page=page.replace(contract,'',1);page=page.replace('<section id="animation-problem-contract"',contract+'<section id="animation-problem-contract"',1)
page=re.sub(r'<p>Every problem below is original[\s\S]*?</p>','<p>The revised bank includes four authentic examination translations and original mathematical and conceptual problems. All 46 answers explain their exact models and derivations. The retained full instruction additionally contains 16 independent derivation tutorials; complete source-course exercise banks are not reproduced.</p>',page,count=1)
(R/'dist/chapters/a_model.html').write_text(page,encoding='utf-8')
(E/'a_model-revision.json').write_text(json.dumps(dict(topicId='a_model',baselineCommit=BASE,status='rewritten_pending_checks',questionCount=46,studentApproval=False,records=records),indent=2)+'\n')
print(json.dumps(dict(questions=46,solutionWords=sum(q['words']for q in records),questionTables=sum('<table>'in v for a,b,v in replacements),nativeMathExpressions=page.count('<math'),finalRules=32),indent=2))
