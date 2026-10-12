from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='44c760435cb24a1f7eaafac9bfb15905c818e305'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):
 s=re.sub(r'\\mathord\{\\sim\}(15|128|u|v)',r'\\operatorname{bitnot}(\1)',s)
 return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
parts=re.split(r'^## Q(\d+)\s*$',(E/'p_types-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip() for i in range(1,len(parts),2)}
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/p_types.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==45
scene_map={1:'adder',2:'chop-positive',3:'decimal',4:'promotion15',5:'casts',6:'conditional',7:'short',8:'wrap',9:'binary64',10:'chop-negative',11:'macro',12:'width',16:'register',20:'signed',24:'layout',28:'array',32:'packed',36:'precision',40:'division',44:'promotion128',45:'conditional-zero'}
actualpath=B/'exam-calibration/actual-items.json';actual=json.loads(actualpath.read_text());old_actual={q['id']:q for q in actual}
original={q['title']:q for f in (B/'exam-calibration').glob('original-*.json') for q in json.loads(f.read_text()) if q.get('topic')=='p_types'}
records=[];edits=[]
for n,(a,b,attrs,q) in enumerate(entries,1):
 end=q.index('<details') if '<details' in q else re.search(r'<p><strong>Correct option:',q).start();prefix=q[:end]
 if n<=43:
  title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1]);c=old_actual[attrs['data-source-id']] if n<=3 else original[re.sub(r'^Question \d+\. ','',title)]
  stop=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end();oldopts=prefix[prefix.index('<div class="exam-options">'):];stem=c['stem']
  if n==11:stem=stem.replace('#define SQR(x) x*x','`#define SQR(x) x*x`') if '`#define' not in stem else stem
  prefix=prefix[:stop]+render(stem)+oldopts
 if 24<=n<=27:
  pos=prefix.index('<div class="exam-options">');prefix=prefix[:pos]+render('Use the minimum-layout ABI: place the first member at offset zero and every subsequent member at its earliest aligned offset, insert no discretionary padding, and round the final size to record alignment. Alignment constraints alone would not make the answer unique.')+prefix[pos:]
 if 40<=n<=43:
  pos=prefix.index('<div class="exam-options">');prefix=prefix[:pos]+render(r"The representability premise includes every evaluated intermediate. Under the chapter's int32 model, the positive parameter obeys $n\le715827882$.")+prefix[pos:]
 if n>=4:prefix=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.', 'Original authored typed-expression or representation question; no specific authentic source item is asserted for this mechanism.',prefix)
 key=int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]);prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 if 'data-answer=' not in prefix:prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-answer="{key}"',1)
 else:assert int(attrs['data-answer'])==key
 visual=('<section class="concept-animation question-specific-animation" data-scenes="types-question-'+scene_map[n]+'" aria-label="Actual mechanism for question '+str(n)+'"><p>This model declares its language or representation contract and uses the actual question data.</p></section>') if n in scene_map else ''
 edits.append((a,b,prefix+'<details class="exam-solution"><summary>Read the full typed derivation, checks, and option analysis</summary>'+render(answers[n])+visual+'</details></section>'));records.append(dict(index=n,answer=key,sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(edits):page=page[:a]+v+page[b:]
for n,(_,_,attrs,_) in enumerate(entries[:3],1):old_actual[attrs['data-source-id']]['solution']=answers[n]
actualpath.write_text(json.dumps(actual,ensure_ascii=False,indent=2)+'\n')
page=page.replace('<h2 id="worked-problems">',render((E/'p_types-method-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1)+'<h2 id="worked-problems">',1)
page=page.replace('<h2 id="references">',render((E/'p_types-exam-rules.md').read_text())+'<h2 id="references">',1)
for a,b in [('Student-approved chapter','Revised English review draft'),('Approved English chapter','Revised English review draft'),('15 examination notes','40 examination decisions')]:page=page.replace(a,b)
page=page.replace('Five written university course bodies were reviewed for this boundary.','Four university course bodies were freshly reviewed for this edition; Stanford\'s earlier reading is retained as historical evidence because renewal access failed.')
page=page.replace('Signedness, range, conversions, and comparison pitfalls. Machine assumptions in the slides are made explicit here.','Historical reading: signedness, range, conversions and comparison pitfalls. Fresh renewal was unavailable; it is not counted among the four fresh university bodies.')
page=page.replace('The student explicitly approved this chapter','The student approved the earlier edition of this chapter')
page=page.replace('The student approved this chapter on 2026-10-02; it is promoted to the finished library.','The earlier edition was approved on 2026-10-02. This individually rewritten edition remains a review draft; the earlier approval does not approve the new text.')
page=re.sub(r'<p>Student approved this chapter on 2026-10-02[\s\S]*?</p>','<p>This revision is part of the continuously authorized whole-library review. The next existing chapter is control flow.</p>',page)
page=page.replace('This supplemental course prevents inappropriate transfer of','This freshly selected fourth university role prevents inappropriate transfer of')
notice='<aside class="deep-review-notice"><strong>Typed expression revision · 12 October 2026.</strong> All 45 answers were individually rewritten; seven construction sections, ten fully solved transfer challenges and 25 detailed decisions supplement the retained complete lesson, 36 tutorials and fifteen foundational notes. Four university bodies were freshly read within documented bounds. Layout questions now declare a minimum ABI policy. Dedicated diagrams separate typed computation, memory and rounding. This edition is a review draft.</aside>'
page=page.replace('<article',notice+'<article',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
# Replace the five repeated body mechanisms with relevant question-specific constructions.
mapping={'animation-values':'promotion15','animation-conversions':'promotion128','animation-operators':'macro','animation-sequencing':'short','animation-floating':'decimal'}
for anchor,name in mapping.items():
 page=re.sub(r'(<section id="'+anchor+r'"[^>]*data-scenes=")[^"]+',r'\g<1>types-question-'+name,page)
# Correct the scalar truth explanation directly; the bit representation need not be all zero.
needle='<h3>Equality, comparisons, and truth</h3>'
page=page.replace(needle,needle+render('Scalar truth tests the value against zero, not whether every stored bit is zero. Under IEEE floating semantics, negative zero is false despite its sign bit, and NaN is true in scalar truth conversion. A null pointer need not have an all-zero representation. Logical comparison and truth results in C have int value zero or one.'))
page=page.replace('<mo>-</mo>','<mo>−</mo>')
from types_diagrams import figure
figs=list(re.finditer(r'<figure class="type-diagram">[\s\S]*?</figure>',page));assert len(figs)==2
for match,kind in reversed(list(zip(figs,['pipeline','tree']))):page=page[:match.start()]+figure(kind)+page[match.end():]
(R/'dist/chapters/p_types.html').write_text(page,encoding='utf-8');(E/'p_types-revision.json').write_text(json.dumps(dict(topicId='p_types',baselineCommit=BASE,status='rewritten_pending_checks',questionCount=45,studentApproval=False,records=records),indent=2)+'\n')
print({'questions':45,'answerWords':sum(q['words'] for q in records),'constructionWords':len((E/'p_types-method-instruction.md').read_text().split()),'math':page.count('<math')})
