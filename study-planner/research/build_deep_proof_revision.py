"""Build the proof chapter from its preserved lesson and individually authored bank."""
from pathlib import Path
import ast,hashlib,html,json,re,subprocess,sys
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
BASE='f890223f3111d27958eb483056556fded2d59ff3'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'helpers','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):
 s=s.replace(r'\prec','≺')
 value=mathml.markdown_math(s,md)
 return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',value)
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/d_proof.html']).decode('utf-8').replace('\r\n','\n')
entries=ns['questions'](raw)
parts=re.split(r'^## Q(\d+)\s*$',(E/'d_proof-solutions.md').read_text(encoding='utf-8'),flags=re.M)
solutions={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
assert set(solutions)==set(range(1,49))and len(entries)==48
actual={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
original={q['title']:q for f in sorted((B/'exam-calibration').glob('original-*.json'))for q in json.loads(f.read_text())if q.get('topic')=='d_proof'}
contexts=[
 r'Let $n\ge1$ be an integer. Count integers $x$ in the inclusive interval $1\le x\le6n$ satisfying $6\mid x^2$.',
 r'Let $n\ge1$ be an integer. Distribute distinct objects into $n$ labelled boxes without any restriction that every box be nonempty. Find the smallest number of objects that forces some box to contain at least four objects, regardless of the distribution.',
 r'Let $n\ge1$ be an integer. Choose a subset of $\{1,\ldots,2n\}$, with no repeated values. Find the smallest subset size forcing two different selected values whose sum is $2n+1$.',
 r'Let $n\ge1$ be an integer. Count integers $x$ in $1\le x\le6n$ that are divisible by two or three but not by six.',
 r'Let $n\ge1$ be an integer. Consider the universal claim that every ordered pair $(x,y)$ with $x,y\in\{1,\ldots,n\}$ satisfies $x\le y$. Count all its counterexample pairs.',
 r'Let $n\ge1$ be an integer. Count input residue classes modulo $2n$ whose integer representatives have odd squares. Count input classes, not distinct square outputs.',
 r'Let $p_1,q_1,\ldots,p_n,q_n$ be $2n$ distinct Boolean atoms, with $n\ge1$. Count complete assignments making every implication $p_i\Rightarrow q_i$ true and at least one antecedent $p_i$ false.',
 r'Let $n\ge1$ be an integer. Count ordered triples $(a,b,c)$ of positive integers with $a+b+c=n+4$.'
]
boundaries=[
 'Which statement correctly characterizes the extension from modulus six to other integer moduli?',
 'Which statement correctly describes the proof obligations for a sharp forcing threshold?',
 'Which statement correctly identifies a necessary modelling assumption of the complementary-pair proof?',
 'Which statement correctly distinguishes the counting calculation from additive closure?',
 'Which statement correctly interprets negation and counterexamples to this bounded universal inequality?',
 'Which statement correctly distinguishes a necessary residue obstruction from a sufficient existence proof?',
 'Which statement correctly explains material implication and the inference of a consequent?',
 'Which statement correctly describes what exhaustive checking on the bounded triple domain can prove?'
]
replacements=[];records=[]
for n,(a,b,attrs,q)in enumerate(entries,1):
 prefix=q[:q.index('<details')]if n<=46 else q[:re.search(r'<p><strong>Correct option:',q).start()]
 if n<=46:
  title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1])
  record=actual[attrs['data-source-id']]if n<=6 else original[re.sub(r'^Question \d+\. ','',title)]
  stem=record['stem']
  if n==6:
   prefix=prefix.replace('data-answer="3"','data-answer="2"').replace('Strict order and injectivity','Order preservation versus identity')
  if n==3:stem=r'A set $A$ is transitive when $x\in y\in A$ implies $x\in A$. Consider (a) $\bigcup A\subseteq A$ and (b) $A\subseteq\mathcal P(A)$. Which of these conditions is equivalent to transitivity of $A$?'
  if n>=15:
   family,part=divmod(n-15,4)
   if part in(0,1):stem=contexts[family]+f' Set $n={5 if part==0 else 8}$. What is the exact answer?'
   elif part==2:stem=contexts[family]+' Which expression gives the answer for every such parameter?'
   else:stem=contexts[family]+' '+boundaries[family]
  end=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end()
  prefix=prefix[:end]+render(stem)+prefix[prefix.index('<div class="exam-options">'):]
 else:
  stem=(r'The claim is that $n^2+n+41$ is prime for every integer $n\ge0$. Which listed input is a counterexample? Verify the factorization that refutes the claim.'if n==47 else r'For real $x>0$, which statement about $x+1/x$ is correct? Prove the bound and equality condition, and check how allowing negative inputs changes it.')
  begin=prefix.index('</h3>')+5;option=prefix.index('<p><strong>1.</strong>')
  prefix=prefix[:begin]+'<p class="exam-provenance">Original integrated proof problem; not an authentic examination item.</p>'+render(stem)+prefix[option:]
 if n>=7:
  option=prefix.find('<div class="exam-options">')
  if option<0:option=prefix.index('<p><strong>1.</strong>')
  task=('Justify the true statement and refute each false alternative by an admissible model or mathematical counterexample.'if 15<=n<=46 and(n-15)%4==3 else 'Give the mathematical derivation and its proof obligations. Explain the alternatives and test the relevant domain or equality boundaries.')
  prefix=prefix[:option]+'<p class="reasoning-task"><strong>Required reasoning.</strong> '+task+'</p>'+prefix[option:]
 prefix=prefix.replace('Testing an existential claim by its witnesses','Counting failures of a universal inequality').replace('Counting the failure of an implication','Counting vacuous implication models')
 prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 replacements.append((a,b,prefix+'<details class="exam-solution"><summary>Read the complete proof and option analysis</summary>'+render(solutions[n])+'</details></section>'))
 records.append(dict(index=n,answer=int(re.search(r'Correct option:\s*(\d+)',solutions[n])[1]),sourceId=attrs.get('data-source-id'),words=len(solutions[n].split()),solutionSha256=hashlib.sha256(solutions[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(replacements):page=page[:a]+v+page[b:]
bridge=render((E/'d_proof-method-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1)
page=page.replace('<h2 id="worked-problems">',bridge+'<h2 id="worked-problems">',1)
rules=render((E/'d_proof-final-rules.md').read_text()).replace('<h2>','<h2 id="quick-reference">',1)
assert 'id="references"'in page
page=re.sub(r'<h2 id="quick-reference">[\s\S]*?(?=<h2 id="references">)',lambda m:rules,page,count=1)
page=page.replace('<a href="#worked-problems">','<a href="#mathematical-bridge">Mathematical constructions</a> <a href="#worked-problems">',1)
notice='<aside class="deep-review-notice"><strong>Proof revision · 11 October 2026.</strong> All 48 answers have been rewritten individually, with explicit derivations, witnesses, proof side conditions and boundary checks. Seven additional construction sections and eighteen final rules connect the full lesson to the questions. Original option orders are retained. The PhD 1405 Q19 translation is corrected from injectivity to identity, changing its independently derived answer to option 2. This is a review draft. The five prior university-course readings are reused within their documented bounds.</aside>'
page=page.replace('<article',notice+'<article',1)
page=page.replace('<section id="animation-contrapositive"',render(r'**Animation predicates.** Here $P(n)$ means that the integer $n^2$ is odd and $Q(n)$ means that $n$ is odd. The target is $P(n)\Rightarrow Q(n)$; its contrapositive says that an even input has an even square. The letters keep this meaning throughout the walkthrough.')+'<section id="animation-contrapositive"',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0]
page=page.replace('</head>',style+'</head>').replace('Student-approved chapter','Revised review draft').replace('13 examination notes','18 examination notes')
# Replace the old diagonal, disconnected strategy arrows with exact ports.
cards=[('Direct','Assume P','Derive Q',False),('Contrapositive','Assume ¬Q','Derive ¬P',False),('Contradiction','Assume P ∧ ¬Q','Derive a contradiction',False),('Refutation','Select an admissible input','Verify P and ¬Q',True)]
svg='<figure class="logic-diagram"><svg viewBox="0 0 840 320" role="img" aria-label="Three routes that prove an implication and the separate route that refutes it"><defs><marker id="proof-route-arrow" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#47768a"/></marker></defs>'
for i,(label,left,right,refutation)in enumerate(cards):
 y=12+i*76;fill='#fff6f0'if refutation else'#f2f8fa'
 svg+=f'<g><text x="18" y="{y+34}" font-family="Source Sans 3,sans-serif" font-size="17">{label}</text><rect x="170" y="{y}" width="275" height="60" rx="9" fill="{fill}" stroke="#a2bac6"/><rect x="530" y="{y}" width="285" height="60" rx="9" fill="{fill}" stroke="#a2bac6"/><text x="307" y="{y+35}" text-anchor="middle" font-family="STIX Two Math,serif" font-size="18">{html.escape(left)}</text><text x="672" y="{y+35}" text-anchor="middle" font-family="STIX Two Math,serif" font-size="18">{html.escape(right)}</text><path d="M445 {y+30}H530" fill="none" stroke="#47768a" stroke-width="2" marker-end="url(#proof-route-arrow)"/></g>'
svg+='</svg><figcaption>The first three rows prove the implication. The last row refutes it by a premise-true, conclusion-false input; it is a separate task.</figcaption></figure>'
page,count=re.subn(r'<figure class="logic-diagram">[\s\S]*?</figure>',lambda m:svg,page,count=1);assert count==1
obsolete='No archived Iranian entrance-exam question is used here. Those booklets are reserved for joint study in the final month.'
page=page.replace(obsolete,'Six original Iranian examination items are included under the later instruction to use authentic questions. The older final-month deferral is superseded for this chapter.')
page=page.replace('The Iranian entrance-exam archive is intentionally deferred to the final month.','The authentic examination questions below follow the later instruction to integrate original examination items with independently derived solutions.')
(R/'dist/chapters/d_proof.html').write_text(page,encoding='utf-8')
report=dict(topicId='d_proof',baselineCommit=BASE,status='rewritten_pending_checks',questionCount=48,authenticOriginalOptionOrdersRetained=6,sourceCorrections=[dict(sourceId='Phd_CS_1405_Q19',previousMeaning='injective',originalMeaning='identity function',previousAnswer=3,correctedAnswer=2)],studentApproval=False,records=records)
(E/'d_proof-revision.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(questions=48,solutionWords=sum(x['words']for x in records),nativeMathExpressions=page.count('<math'),questionTables=sum('<table>'in v for a,b,v in replacements),finalRules=18),indent=2))
