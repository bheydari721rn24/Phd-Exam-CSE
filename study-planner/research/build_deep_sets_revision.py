"""Build a question-specific sets revision without running legacy library builders."""
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
 value=mathml.markdown_math(s,md)
 return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',value)
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/d_sets.html']).decode('utf-8').replace('\r\n','\n')
entries=ns['questions'](raw)
parts=re.split(r'^## Q(\d+)\s*$',(E/'d_sets-solutions.md').read_text(encoding='utf-8'),flags=re.M)
solutions={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
assert set(solutions)==set(range(1,47))and len(entries)==46
actual={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
original={q['title']:q for f in sorted((B/'exam-calibration').glob('original-*.json'))for q in json.loads(f.read_text())if q.get('topic')=='d_sets'}
contexts=[
 r'Let $U$ be a fixed labelled universe of size $n$. Count ordered pairs of subsets satisfying $A\subseteq B$; equality and empty sets are permitted.',
 r'Let $U$ be a fixed labelled universe of size $n$. Count ordered pairs of subsets satisfying $A\cup B=U$. No intersection or nonemptiness restriction is imposed.',
 r'Let $U$ be a fixed labelled universe of size $n$. Count ordered triples of subsets satisfying $A\subseteq B\subseteq C$. Containment need not be proper.',
 r'Let $U$ be a fixed labelled universe of size $n$, and let $D\subseteq U$ be a prescribed set. Count ordered pairs satisfying $A\triangle B=D$.',
 r'Let $U$ be a fixed labelled universe of size $n$. Count subsets $A$ that are both nonempty and proper: $\varnothing\ne A\subsetneq U$.',
 r'Let $U$ be a fixed labelled universe of size $n$. Count ordered triples of pairwise-disjoint subsets $A,B,C$. Empty sets and uncovered universe objects are permitted.',
 r'Let $U$ be a fixed labelled universe of size $2n$, and let $I\subseteq U$ be a particular prescribed set of size $n$. Count ordered pairs satisfying $A\cap B=I$. The union is unrestricted.',
 r'Let $U$ be a fixed labelled universe of size $n$. Count ordered pairs satisfying both $A\cap B=\varnothing$ and $A\cup B=U$. Empty coordinates are permitted.'
]
boundaries=[
 'Which statement correctly distinguishes proper from non-strict containment?',
 'Which statement correctly describes coverage, disjointness and exchange of the two set labels?',
 'Which statement gives the correct way to count membership states in a chain of labelled sets?',
 'Which statement correctly describes symmetric difference with a prescribed set?',
 'Which statement correctly handles nonemptiness, properness and the empty-universe boundary?',
 'Which statement correctly distinguishes pairwise disjointness, an empty triple intersection and full coverage?',
 'Which statement correctly identifies the forced memberships of the prescribed intersection?',
 'Which statement correctly characterizes complementary subsets, including the empty-universe boundary?'
]
replacements=[];records=[]
for n,(a,b,attrs,q)in enumerate(entries,1):
 prefix=q[:q.index('<details')]if n<=44 else q[:re.search(r'<p><strong>Correct option:',q).start()]
 if n<=44:
  title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1])
  record=actual[attrs['data-source-id']]if n<=4 else original[re.sub(r'^Question \d+\. ','',title)]
  stem=record['stem']
  if n==2:
   stem=r'A set $A$ is transitive when $x\in y\in A$ implies $x\in A$. Consider (a) $\bigcup A\subseteq A$ and (b) $A\subseteq\mathcal P(A)$. Which of these conditions is equivalent to transitivity of $A$?'
  if n>=13:
   family,part=divmod(n-13,4)
   if part in(0,1):stem=contexts[family]+f' Set $n={5 if part==0 else 8}$. What is the exact count?'
   elif part==2:stem=contexts[family]+r' Assume $n\ge1$. Which formula gives the count for every such $n$?'
   else:stem=contexts[family]+' '+boundaries[family]
  end=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end()
  prefix=prefix[:end]+render(stem)+prefix[prefix.index('<div class="exam-options">'):]
 else:
  stem=(r'Let $U$ be a fixed four-object labelled universe. How many ordered triples of subsets satisfy $A\subsetneq B\subsetneq C$? The smallest set may be empty, and $C$ may equal $U$.'if n==45 else r'Let $U$ be a fixed five-object labelled universe. How many ordered pairs of nonempty disjoint subsets $A,B$ exist? The sets need not cover $U$.')
  begin=prefix.index('</h3>')+5;option=prefix.index('<p><strong>1.</strong>')
  provenance=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix)
  prefix=prefix[:begin]+(provenance[0]if provenance else'<p class="exam-provenance">Original integrated counting problem; not an authentic examination item.</p>')+render(stem)+prefix[option:]
 if n>=5:
  option=prefix.find('<div class="exam-options">')
  if option<0:option=prefix.index('<p><strong>1.</strong>')
  task=('Prove or refute each alternative using precise membership conditions and a counterexample when needed.'if n>=13 and n<=44 and(n-13)%4==3 else 'Derive the answer from the stated regions or a bijection. Explain every choice, subtraction and boundary case, and distinguish the incorrect alternatives.')
  prefix=prefix[:option]+'<p class="reasoning-task"><strong>Required reasoning.</strong> '+task+'</p>'+prefix[option:]
 prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 replacements.append((a,b,prefix+'<details class="exam-solution"><summary>Read the complete derivation and option analysis</summary>'+render(solutions[n])+'</details></section>'))
 records.append(dict(index=n,answer=int(re.search(r'Correct option:\s*(\d+)',solutions[n])[1]),sourceId=attrs.get('data-source-id'),words=len(solutions[n].split()),solutionSha256=hashlib.sha256(solutions[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(replacements):page=page[:a]+v+page[b:]
bridge=render((E/'d_sets-counting-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1)
page=page.replace('<h2 id="worked-problems">',bridge+'<h2 id="worked-problems">',1)
rules=render((E/'d_sets-final-rules.md').read_text()).replace('<h2>','<h2 id="quick-reference">',1)
page=re.sub(r'<h2 id="quick-reference">[\s\S]*?(?=<h2 id="laboratory">)',lambda m:rules,page,count=1)
page=page.replace('<a href="#worked-problems">','<a href="#mathematical-bridge">Counting constructions</a> <a href="#worked-problems">',1)
notice='<aside class="deep-review-notice"><strong>Sets revision · 11 October 2026.</strong> Every one of the 46 problem answers has been rewritten individually. The chapter adds seven detailed counting constructions and twenty final examination rules. Original examination meanings and option order are retained. This new edition is a review draft. The four prior core written-course readings and fifth supplemental reading are reused within the recorded source-audit boundaries; this is not a new exhaustive worldwide course search.</aside>'
page=page.replace('<article',notice+'<article',1)
logic=(R/'dist/chapters/d_logic.html').read_text()
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',logic)[0]
page=page.replace('</head>',style+'</head>')
page=page.replace('Student-approved chapter','Revised review draft')
# The existing interactive lab used prose glyph strings. Its labels now use the
# same professional mathematical font and semantic MathML as the new solutions.
names=[r'$A\cap(B\cup C)$',r'$(A\cap B)\cup(A\cap C)$',r'$A\triangle(B\cap C)$',r'$(A\triangle B)\cap(A\triangle C)$']
oldnames=['A ∩ (B ∪ C)','(A ∩ B) ∪ (A ∩ C)','A △ (B ∩ C)','(A △ B) ∩ (A △ C)']
for old,new in zip(oldnames,names):page=page.replace(json.dumps(old,ensure_ascii=False),json.dumps(render(new).strip().removeprefix('<p>').removesuffix('</p>'),ensure_ascii=False))
(R/'dist/chapters/d_sets.html').write_text(page,encoding='utf-8')
report=dict(topicId='d_sets',baselineCommit=BASE,status='rewritten_pending_checks',questionCount=46,authenticQuestionMeaningsRetained=4,studentApproval=False,records=records)
(E/'d_sets-revision.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(questions=46,solutionWords=sum(x['words']for x in records),nativeMathExpressions=page.count('<math'),questionTables=sum('<table>'in v for a,b,v in replacements),finalRules=20),indent=2))
