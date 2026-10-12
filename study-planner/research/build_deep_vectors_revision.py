from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='f890223f3111d27958eb483056556fded2d59ff3'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md))
parts=re.split(r'^## Q(\d+)\s*$',(E/'l_vectors-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip() for i in range(1,len(parts),2)}
authpath=B/'exam-calibration/actual-items.json';actual=json.loads(authpath.read_text());rec=next(q for q in actual if q['id']=='Phd_CS_1404_Q31')
rec.update(stem=rec['stem'].replace('An orthonormal basis','An orthogonal basis'),answer=None,intendedAnswer=3,sourceAmbiguity='The Persian page states orthogonal without explicitly requiring unit lengths, but its formula omits nonunit denominators. Literal hypotheses can invalidate both options 1 and 3. With an added orthonormal interpretation, option 3 fails as a general theorem; the allowed full-space case has equality.',translationStatus='literal orthogonal wording rechecked against original page image, 12 October 2026',solution=answers[3],answerProvenance='No unique literal answer asserted; option 3 is an independently derived intended normalized interpretation, not an official key.')
authpath.write_text(json.dumps(actual,ensure_ascii=False,indent=2)+'\n');actual={q['id']:q for q in actual}
original={q['title']:q for f in (B/'exam-calibration').glob('original-*.json') for q in json.loads(f.read_text()) if q.get('topic')=='l_vectors'}
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/l_vectors.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==len(answers)==46
extensions=[r'Construct an explicit basis, prove spanning and independence, and explain rank versus the number of displayed equations. Handle the dimension-one boundary.',r'Prove the sum/intersection dimension identity and construct subspaces attaining the supplied dimensions. Explain the distinction between union, sum, ambient feasibility and a fixed embedding.',r'Prove rank–nullity from a kernel-basis extension. Construct a witness matrix and compare the kernel of its transpose, including the smallest feasible parameter.',r'Calculate the coefficient, signed unit component, projected vector and squared length separately. Check the residual and invariance under a nonzero rescaling of the generator.',r'Compute all residual coordinates and verify orthogonality before using Pythagorean subtraction. Give a counterexample for an oblique decomposition.',r'Derive the parameter equation from the actual inner product and check every competing value. Compare the answer under a positive weighted inner product.',r'Reconstruct both basis coordinates, verify uniqueness, and compute the induced coordinate norm from the Gram matrix. Explain the effect of swapping basis order.',r'Construct a kernel basis and prove unique free-coordinate parameterization. Compare homogeneous and nonzero constant-sum conditions, including the zero-dimensional kernel boundary.']
scenes={3:'vectors-question-source',4:'vectors-question-positivity',37:'vectors-question-gram37',41:'vectors-question-coordinates',45:'vectors-question-gram45',46:'vectors-question-minimum'}
def options(values):return '<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(v)+'</div></div>' for i,v in enumerate(values,1))+'</div>'
records=[];replacements=[]
for n,(a,b,attrs,q) in enumerate(entries,1):
 end=q.index('<details') if '<details' in q else re.search(r'<p><strong>Correct option:',q).start();prefix=q[:end]
 if n<=44:
  title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1]);c=actual[attrs['data-source-id']] if n<=4 else original[re.sub(r'^Question \d+\. ','',title)]
  stop=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end();prefix=prefix[:stop]+render(c['stem'])+prefix[prefix.index('<div class="exam-options">'):]
  if 5<=n<=36:
   pos=prefix.index('<div class="exam-options">');prefix=prefix[:pos]+render(extensions[(n-5)//4])+prefix[pos:]
   prefix=prefix.replace('Original examination analogue · author-assessed medium difficulty','Original examination analogue · exact calculation and proof extension').replace('Original examination analogue · author-assessed hard difficulty','Original examination analogue · conditions and counterexample analysis')
  if n==12:
   vals=list(c['options']);vals[3]='The individual dimensions determine the intersection dimension regardless of the relative positions of the two subspaces.';prefix=prefix[:prefix.index('<div class="exam-options">')]+options(vals)
  if n==3:
   pos=prefix.index('<div class="exam-options">');prefix=prefix[:pos]+'<aside class="source-ambiguity"><strong>Original-source ambiguity.</strong> The original says orthogonal, without explicit unit lengths. Its displayed sum is a true orthogonal projection only with normalization or squared-norm denominators. No unique literal key is asserted. The complete answer below separates the literal wording from the intended normalized interpretation and also handles the full-space exception.</aside>'+prefix[pos:]
 else:
  pos=re.search(r'<p><strong>1\.</strong>|<div class="exam-options">',prefix).start();prefix=prefix[:pos]+options([r'$(1,1,1)$',r'$(2/3,1/3,1/3)$',r'$(0,1/2,1/2)$',r'$(1/2,1/2,1/2)$'] if n==45 else ['$1/3$','$2/3$','$1$','$2$'])
 key=3 if n==3 else int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]);prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 if n==3:prefix=prefix.replace('data-answer="3"','data-source-ambiguous="true" data-intended-answer="3"')
 elif 'data-answer=' not in prefix:prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-answer="{key}"',1)
 else:assert int(attrs['data-answer'])==key
 visual='<section class="concept-animation question-specific-animation" data-scenes="'+scenes[n]+'" aria-label="Exact construction for question '+str(n)+'"><p>The visual model uses the actual problem data and the assumptions explained above.</p></section>' if n in scenes else ''
 value=prefix+'<details class="exam-solution"><summary>Read the complete derivation, checks, and option analysis</summary>'+render(answers[n])+visual+'</details></section>';replacements.append((a,b,value));records.append(dict(index=n,answer=None if n==3 else key,intendedAnswer=3 if n==3 else None,sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(replacements):page=page[:a]+v+page[b:]
bridge=render((E/'l_vectors-method-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1);page=page.replace('<h2 id="worked-problems">',bridge+'<h2 id="worked-problems">',1)
rules=render((E/'l_vectors-final-rules.md').read_text()).replace('<h2>','<h2 id="quick-reference">',1);page=re.sub(r'<h2 id="quick-reference">[\s\S]*?(?=<h2 id="references">)',lambda m:rules,page,count=1)
page=page.replace('<a href="#worked-problems">','<a href="#mathematical-bridge">Mathematical constructions</a> <a href="#worked-problems">',1).replace('Student-approved chapter','Revised review draft').replace('15 examination notes','32 complete final rules').replace('15 exam decision notes','32 final review rules')
page=page.replace('Approved English chapter','Revised English review draft')
page=page.replace('data-scenes="gram-schmidt"','data-scenes="vectors-question-gram-schmidt"')
notice='<aside class="deep-review-notice"><strong>Vector geometry revision · 12 October 2026.</strong> All 46 answers are individually rewritten, with exact calculations, explicit bases, complete optimality proofs, Gram equations, norm conventions and diagnosed alternatives. Six construction sections and 32 final rules complement the full lesson and all 34 retained tutorials. Six specific question models replace unrelated repeated players. Four written university selections were freshly rechecked within documented bounds. The authentic Q31 source ambiguity is preserved and explained rather than assigned a fabricated unique key. This edition is a review draft.</aside>'
page=page.replace('<article',notice+'<article',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];style=style.replace('</style>','.source-ambiguity{margin:1rem 0;padding:1rem;border-left:3px solid #aa8641;background:#fcf8ef;line-height:1.65}</style>');page=page.replace('</head>',style+'</head>')
page=page.replace('No archived Iranian entrance-exam question was used.','Four separately labeled authentic items were checked against their original PDF images; Q31 has a documented wording ambiguity.')
page=page.replace('Archived Iranian entrance-exam booklets remain reserved for joint study in the final month. No claim of empirical calibration to those untouched papers is made here.','Authentic examination applications are now included under the later explicit instruction to analyze the archives. The independently derived keys are not official keys, and the Q31 literal source has no asserted unique answer.')
page=page.replace('This chapter was explicitly approved by the student and is ready for study.','This newly revised edition remains a review draft; approval of the earlier edition does not label the new edition student-approved.')
from vectors_diagrams import plot
figs=list(re.finditer(r'<figure class="logic-diagram(?: exam-figure)?">[\s\S]*?</figure>',page));assert len(figs)==3
for match,kind in reversed(list(zip(figs,['addition','projection','nonunit']))):page=page[:match.start()]+plot(kind)+page[match.end():]
page=page.replace('General matrix elimination, determinant theory, rank–nullity, eigenvalues, full least-squares algorithms, and infinite-dimensional convergence are reserved for later chapters.','General matrix elimination, full determinant/eigenvalue theory, numerical least-squares algorithms and infinite-dimensional convergence have later chapters. The examination constructions section below derives the kernel/dimension, induced-norm and structured-quadratic-form tools needed by this bank.')
page=page.replace('Structural matrix theory, general basis-exchange arguments, infinite Fourier convergence, advanced numerical rank estimation, and other later-chapter topics are deliberately outside this boundary.','The new construction sections prove the basis-extension, dimension and Gram-system claims used by this bank. Full matrix factorization, infinite Fourier convergence and advanced numerical rank estimation remain later-chapter topics.')
page=page.replace('The 34 problems are an instructional selection, not every exercise published in the surveyed courses.','The 34 retained derivation tutorials and 46 separately labeled examination questions are an instructional selection, not every exercise published in the surveyed courses.')
page=page.replace('No claim of empirical calibration to those untouched papers is made here.','The four authentic items were checked against the recorded original PDF images; original analogues are not represented as empirical performance calibration.')
page=re.sub(r'Large candidate[^<]*window[^<]*\.', 'The camera adapts to keep all candidate endpoints visible with equal axis scales.', page)
page=page.replace('</style>','.vector-lab svg{display:block;width:100%;max-height:360px}.vector-lab [id="vector-result"] p{margin:.35rem 0}</style>',1)
# Minimal original-source correction in the four pending chapters: their wider review is not claimed.
corrections=[]
for target in ['l_matrices','l_linear','l_orthogonality','l_spaces']:
 path=R/f'dist/chapters/{target}.html';s=path.read_text();items=ns['questions'](s);edits=[]
 for a,b,attrs,q in items:
  if attrs.get('data-source-id')!='Phd_CS_1404_Q31':continue
  head=q[:q.index('<details')];head=re.sub(r'<aside class="source-ambiguity">[\s\S]*?</aside>','',head);head=head.replace('An orthonormal basis','An orthogonal basis').replace('data-answer="3"','data-source-ambiguous="true" data-intended-answer="3"');pos=head.index('<div class="exam-options">');head=head[:pos]+'<aside class="source-ambiguity"><strong>Source correction, 12 October 2026.</strong> The original says orthogonal without an explicit unit-length condition. The literal formula may invalidate more than one option. The answer below explains both the literal wording and the added orthonormal interpretation; no official unique key is asserted.</aside>'+head[pos:];value=head+'<details class="exam-solution"><summary>Read the source ambiguity and complete mathematical analysis</summary>'+render(answers[3])+'</details></section>';edits.append((a,b,value))
 for a,b,v in reversed(edits):s=s[:a]+v+s[b:]
 if edits:path.write_text(s,encoding='utf-8');corrections.append(dict(topicId=target,sourceId='Phd_CS_1404_Q31',correctedPlacements=len(edits),scope='Only this source item corrected; full chapter revision remains pending.'))
(R/'dist/chapters/l_vectors.html').write_text(page,encoding='utf-8');(E/'l_vectors-revision.json').write_text(json.dumps(dict(topicId='l_vectors',baselineCommit=BASE,status='rewritten_pending_checks',questionCount=46,studentApproval=False,records=records,relatedSourceCorrections=corrections),indent=2)+'\n')
print({'questions':46,'words':sum(q['words'] for q in records),'relatedSourceCorrections':corrections,'math':page.count('<math')})
