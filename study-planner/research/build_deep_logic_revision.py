"""Rebuild only the logic bank from an immutable Git baseline and authored solutions.

No historical builder is imported or run. Non-question lesson prose and scientific
laboratories remain byte-for-byte unchanged, apart from an explicit review notice.
"""
from pathlib import Path
import ast, hashlib, html, json, re, subprocess, sys
from markdown_it import MarkdownIt

B=Path(__file__).resolve().parent; R=B.parent; E=B/'deep-library-revision'
BASE='f890223f3111d27958eb483056556fded2d59ff3'
ns={}; tree=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'inventory helpers','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'))
import mathml
mathml.wrap_display=lambda s:s
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):
 s=re.sub(r'\\big\b','',s)
 s=s.replace(r'\Gamma','Γ').replace(r'\models','⊨')
 value=mathml.markdown_math(s,md)
 return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',value)
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/d_logic.html']).decode('utf-8').replace('\r\n','\n')
entries=ns['questions'](raw)
source=(E/'d_logic-solutions.md').read_text(encoding='utf-8')
actual={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
original={q['title']:q for f in sorted((B/'exam-calibration').glob('original-*.json'))for q in json.loads(f.read_text())if q.get('topic')=='d_logic'}
contexts=[
 r'There are $n+2$ distinct labelled Boolean variables. The formula requires $x_1\Leftrightarrow x_2$ and $x_2\Rightarrow x_3$; all other variables are unconstrained.',
 r'A unary predicate $P$ on a fixed labelled $n$-object domain must satisfy both $\exists xP(x)$ and $\neg\forall xP(x)$.',
 r'A binary relation $R$ on a fixed labelled $n$-object domain must satisfy $\forall x\exists yR(x,y)$. There are no symmetry, column, or uniqueness conditions.',
 r'A binary relation $R$ on a fixed labelled $n$-object domain must satisfy $\forall x\exists!yR(x,y)$. Different inputs may share a target.',
 r'The Boolean function on $n$ distinct atoms is true exactly when an odd number of its input bits are one. Its canonical CNF must use only those original atoms.',
 r'The $2n$ atoms $p_1,q_1,\ldots,p_n,q_n$ are all distinct. The premises are $p_i\Rightarrow q_i$ for every $i$, and the conclusion is the conjunction of all converses $q_i\Rightarrow p_i$.',
 r'The $2n$ atoms $p_1,q_1,\ldots,p_n,q_n$ are all distinct. Consider the inclusive disjunction $\bigvee_{i=1}^{n}(p_i\land q_i)$.',
 r'A fixed equivalence relation partitions a labelled domain into $n$ nonempty classes. A unary predicate is constant on each class and is true on at least one object.',
 r'A binary relation $R$ on a fixed labelled $n$-object domain must satisfy $\neg\forall x\exists yR(x,y)$. No other relation property is required.'
]
objects=['satisfying complete assignments','predicate interpretations','relation interpretations','relation interpretations','clauses in the canonical CNF','complete premise-true, conclusion-false assignments','satisfying complete assignments','predicate interpretations','relation interpretations']
boundary=[
 r'Assume $n\ge3$, so two distinct unconstrained variables exist. Which statement correctly describes the effect of adding constraints?',
 'For this boundary question only, explicitly permit an empty domain and ignore languages with object-denoting constants. Which statement correctly evaluates existential and universal quantification on that domain?',
 'Which statement correctly distinguishes row totality from unique existence and column conditions?',
 'Which statement correctly describes the additional requirement that distinct inputs have distinct targets on a finite square domain?',
 'Which statement correctly compares canonical normal-form size with the size of a circuit computing the same function?',
 'Which statement gives the correct criterion for refuting or proving entailment?',
 'Which statement correctly describes the independence assumptions needed for the product count?',
 'Which statement correctly identifies whether class sizes affect the unrestricted count of class-constant predicates?',
 'Which statement correctly describes negating the quantified condition and counting its relation models?'
]
pieces=re.split(r'^## Q(\d+)\s*$',source,flags=re.M)
solutions={int(pieces[i]):pieces[i+1].strip()for i in range(1,len(pieces),2)}
assert set(solutions)==set(range(1,54)) and len(entries)==53
records=[]; replacements=[]
for n,(a,b,attrs,question)in enumerate(entries,1):
 if n<=51:
  prefix=question[:question.index('<details')]
 else:
  cut=re.search(r'<p><strong>Correct option:',question)
  assert cut, n
  prefix=question[:cut.start()]
 # Restore complete grammatical sentences from the written source, rather than
 # retaining the legacy automatic display conversion's orphan punctuation.
 if n<=51:
  title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',question)[1])
  record=actual[attrs['data-source-id']]if n<=7 else original[re.sub(r'^Question \d+\. ','',title)]
  stem=record['stem']
  if 16<=n<=51:
   family,part=divmod(n-16,4)
   if part<=1:
    parameter=5 if part==0 else 8
    stem=contexts[family]+f' Set $n={parameter}$. How many '+objects[family]+' satisfy the stated requirements?'
   elif part==2:stem=contexts[family]+r' Assume $n\ge1$. Which expression counts '+objects[family]+' for every permitted value of $n$?'
   else:stem=contexts[family]+' '+boundary[family]
  if n==2:
   stem=r'''Let the domain be $D=\{0,1,2\}$ and let $c=0$. The function is specified by $f(0)=1$, $f(1)=2$ and $f(2)=0$. The binary relation contains exactly the pairs $(0,1)$, $(1,2)$ and $(2,0)$. Consider the open formula

$$\phi(x)=\forall y(R(x,y)\Rightarrow R(f(y),c)).$$

The assignments $v_1$ and $v_2$ give $x$ the values 0 and 2, respectively. Under which of these assignments is $\phi(x)$ true?'''
  if n==6:stem='In variable order $p,q,r$, a formula is true exactly at the four bit strings 111, 110, 101 and 011, and false at all other bit strings. Which displayed expression is its canonical CNF?'
  end=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end()
  prefix=prefix[:end]+render(stem)+prefix[prefix.index('<div class="exam-options">'):]
 if n==19:
  prefix=prefix.replace('generally halves the count.','halves the count under the stated independence assumptions.')
 if n==6:
  corrected=[r'$(p\land q\land r)\lor(p\land q\land\neg r)\lor(p\land\neg q\land r)\lor(\neg p\land q\land r)$',r'$(p\lor q\lor r)\land(\neg p\lor q\lor r)\land(p\lor\neg q\lor r)\land(p\lor q\lor\neg r)$',r'$(\neg p\lor\neg q\lor\neg r)\land(p\lor\neg q\lor r)\land(\neg p\lor q\lor\neg r)\land(\neg p\lor\neg q\lor r)$',r'$(\neg p\land\neg q\land r)\lor(\neg p\land\neg q\land\neg r)\lor(\neg p\land q\land\neg r)\lor(p\land\neg q\land\neg r)$']
  prefix=prefix[:prefix.index('<div class="exam-options">')]+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(x)+'</div></div>'for i,x in enumerate(corrected,1))+'</div><p class="exam-provenance">Editorial correction: options 3 and 4 have been retranscribed from the original booklet image, physical page 7, on 11 October 2026. Option order and the original question are retained.</p>'
 # The raw contract is retained for authentic translations. Original stems receive
 # a precise task statement identifying what an answer must explain.
 tasks={8:'List the surviving assignments in the order p,q,r,s and explain why there are no others.',9:'Use p as the most significant bit and distinguish semantic equivalence from the requested normal-form syntax.',10:'Derive the forced path for each statement before evaluating its outer quantifier.',11:'Check separately the existence clause, the uniqueness clause, and the direction of the relation.',12:'Evaluate both formulas at every possible predicate value; do not assume that a universal conditional implies an existential witness.',13:'Prove the entailed option and give complete premise-satisfying countervaluations for the others.',14:'State the value of each implication for every assignment or give an equivalent complete argument.',15:'State both possible failures of unique existence, using distinct witnesses in the multiple-solution case.',52:'Count possible output tables of F, rather than input assignments satisfying one formula. Identify forced-zero, forced-one and free rows.',53:'Treat the two quantified requirements as properties of one labelled relation. Account for overlaps between possible common witnesses.'}
 if 16<=n<=51:
  if (n-16)%4 in (0,1):task='Derive the count from a partition or a bijection, explain every factor and excluded case, and identify the condition represented by each incorrect count.'
  elif (n-16)%4==2:task='Prove the parameterized count, state its domain of applicability, and check the smallest admissible domain.'
  else:task='Justify the correct claim and refute each false claim with a specific valuation, relation matrix, or boundary model.'
 elif n in tasks:task=tasks[n]
 else:task=None
 if task:
  optionstart=prefix.find('<div class="exam-options">')
  if optionstart<0:
   optionstart=prefix.find('<p><strong>1.</strong>')
  assert optionstart>=0,n
  prefix=prefix[:optionstart]+'<p class="reasoning-task"><strong>Required reasoning.</strong> '+html.escape(task)+'</p>'+prefix[optionstart:]
 answer=int(re.search(r'Correct option:\s*(\d+)',solutions[n])[1])
 # This replaces the old generic animation with the actual table, model or
 # derivation authored for this question. The main concept laboratories remain.
 prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 replacement=prefix+'<details class="exam-solution"><summary>Read the complete derivation and option analysis</summary>'+render(solutions[n])+'</details></section>'
 replacements.append((a,b,replacement))
 records.append(dict(index=n,answer=answer,kind=attrs.get('data-kind'),sourceId=attrs.get('data-source-id'),words=len(solutions[n].split()),solutionSha256=hashlib.sha256(solutions[n].encode()).hexdigest(),state='rewritten_pending_mathematical_and_browser_checks'))
page=raw
for a,b,value in reversed(replacements):page=page[:a]+value+page[b:]
bridge=render((E/'d_logic-counting-instruction.md').read_text())
bridge=bridge.replace('<h2>','<h2 id="mathematical-bridge">',1)
page=page.replace('<h2 id="worked-problems">',bridge+'<h2 id="worked-problems">',1)
rules=render((E/'d_logic-final-rules.md').read_text()).replace('<h2>','<h2 id="quick-reference">',1)
page=re.sub(r'<h2 id="quick-reference">[\s\S]*?(?=<h2 id="laboratory">)',lambda m:rules,page,count=1)
page=page.replace('<a href="#worked-problems">','<a href="#mathematical-bridge">Counting derivations</a> <a href="#worked-problems">',1)
notice='<aside class="deep-review-notice"><strong>Logic revision · 11 October 2026.</strong> All 53 answers have been rewritten with question-specific mathematical derivations, countermodels, boundary checks and option analysis. Two mistranscribed options of PhD 1405 Q15 and the missing hypothesis of Question 19 have been corrected. The original examination meanings and option order are retained. This is a review draft; historical approval does not certify this new revision. The wider 60-chapter review is in progress.</aside>'
page=page.replace('<article',notice+'<article',1)
style='''<style id="deep-review-layout">.deep-review-notice{margin:1.5rem 0;padding:1rem 1.2rem;border-left:3px solid #47768a;background:#f1f7f8;line-height:1.65}.reasoning-task{color:#37586a}.exam-solution p{margin:.9rem 0}.exam-solution table{margin:1.25rem 0;border-collapse:collapse;min-width:0;width:100%}.exam-solution th,.exam-solution td{padding:.65rem .85rem;vertical-align:top;line-height:1.55}.exam-solution math{font-family:'STIX Two Math',serif}.exam-solution .formula-block{overflow-x:auto;white-space:nowrap}.exam-solution .formula-block math{white-space:nowrap}.exam-solution summary{padding:.8rem 0;cursor:pointer}@media(max-width:600px){.exam-solution table{font-size:.86rem}.exam-solution th,.exam-solution td{padding:.4rem .45rem}}@media print{.exam-solution{display:block}.exam-solution summary{display:none}.deep-review-notice{break-inside:avoid}}</style>'''
page=page.replace('</head>',style+'</head>')
page=page.replace('Student-approved chapter · 7 authentic questions','Revised review draft · 7 authentic questions')
(R/'dist/chapters/d_logic.html').write_text(page,encoding='utf-8')
report=dict(topicId='d_logic',baselineCommit=BASE,status='rewritten_pending_checks',questionCount=53,authenticQuestionMeaningsRetained=7,authenticOptionTranscriptionCorrections={'Phd_CS_1405_Q15':[3,4]},studentApproval=False,records=records)
(E/'d_logic-revision.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(questions=53,solutionWords=sum(q['words']for q in records),nativeMathExpressions=page.count('<math'),questionTables=page[page.index('Question 1.') :].count('<table>')),indent=2))
