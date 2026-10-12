from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='a28dc770d47ecedeee37be63820d05ee4c2d7665'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md))
parts=re.split(r'^## Q(\d+)\s*$',(E/'l_matrices-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip() for i in range(1,len(parts),2)}
authpath=B/'exam-calibration/actual-items.json';actual=json.loads(authpath.read_text());rec=next(q for q in actual if q['id']=='MS_CS_1405_Q113');rec['options'][0]='37';rec['translationStatus']='Original option 1 freshly rechecked as Persian 37 on PDF page 25, 12 October 2026';rec['solution']=answers[2];authpath.write_text(json.dumps(actual,ensure_ascii=False,indent=2)+'\n');actual={q['id']:q for q in actual}
original={q['title']:q for f in (B/'exam-calibration').glob('original-*.json') for q in json.loads(f.read_text()) if q.get('topic')=='l_matrices'}
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/l_matrices.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==len(answers)==47
def options(values):return '<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(v)+'</div></div>' for i,v in enumerate(values,1))+'</div>'
extensions=['Prove the all-equal and sum-zero decomposition, justify the determinant computation, and independently verify a closed-form inverse. Test the smallest dimension and distinguish a sufficient triangular guarantee from a numerical coincidence.','Verify the inverse on both sides and through the actual shear action. Extend to a three-step nilpotent and a compatible rectangular coupling block; state every denominator assumption.','Derive the trace from weighted fixed coordinates. Compare a derangement with a permutation having a fixed point, then prove cyclic trace invariance without assuming multiplicativity.','Derive the dimensional determinant power and diagnose determinant-versus-trace and product-versus-sum errors. Include noncommuting factors in the scope argument.','Explain the coefficient using distinct chronological move slots and independently derive its recurrence. Extend to weighted direct and indirect paths and test powers zero and one.','Prove image equality using the onto first action and injective second action, not merely a rank upper bound. Compare the reverse product and the n=2 boundary.','Reconstruct each transformed basis image and solve its actual coefficient equations. State that the same ordered basis is used on both sides; distinguish independent input/output conversions.','Construct the full ordered block inverse and verify both products. Explain why a singular or rectangular coupling block needs no inverse and why a lower-left coupling changes the determinant argument.']
scene_map={4:'matrices-question-source',5:'matrices-question-positivity3',6:'matrices-question-allones',10:'matrices-question-shear',14:'matrices-question-fixed',22:'matrices-question-power',26:'matrices-question-rank',30:'matrices-question-basis',34:'matrices-question-block',42:'matrices-question-gram',43:'matrices-question-positivity4',44:'matrices-question-trace',45:'matrices-question-blockidentity',46:'matrices-question-power10',47:'matrices-question-blockidentity'}
replacements=[];records=[]
for n,(a,b,attrs,q) in enumerate(entries,1):
 end=q.index('<details') if '<details' in q else re.search(r'<p><strong>Correct option:',q).start();prefix=q[:end]
 if n<=45:
  title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1]);c=actual[attrs['data-source-id']] if n<=5 else original[re.sub(r'^Question \d+\. ','',title)]
  stop=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end();oldopts=prefix[prefix.index('<div class="exam-options">'):];prefix=prefix[:stop]+render(c['stem'])+oldopts
  vals=list(c['options'])
  if n==9:vals[0]='Triangular structure guarantees the diagonal-product determinant; arbitrary matrices have no such guarantee.'
  if n==33:vals[3]='Using the same new ordered basis for both input and output of an endomorphism gives a similarity transformation.'
  if n in [2,9,33]:prefix=prefix[:prefix.index('<div class="exam-options">')]+options(vals)
  if 6<=n<=37:
   pos=prefix.index('<div class="exam-options">');prefix=prefix[:pos]+render(extensions[(n-6)//4])+prefix[pos:]
   if 14<=n<=17 or 26<=n<=29:prefix=prefix[:prefix.index('<div class="exam-options">')]+render(r'The factor premises require $n\ge2$.')+prefix[prefix.index('<div class="exam-options">'):]
   prefix=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.', 'Original authored matrix-algebra question; no specific authentic source item is asserted for this mechanism.',prefix)
  if n==4:
   pos=prefix.index('<div class="exam-options">');prefix=prefix[:pos]+'<aside class="source-ambiguity"><strong>Original-source ambiguity.</strong> The original states orthogonal without explicit unit lengths, but its sum omits squared-norm denominators. No unique literal key is asserted. The answer separates the literal wording from an added orthonormal interpretation and handles the full-space boundary.</aside>'+prefix[pos:]
 else:
  pos=re.search(r'<p><strong>1\.</strong>|<div class="exam-options">',prefix).start();prefix=prefix[:pos]+options(['$10$','$20$','$45$','$100$'] if n==46 else ['$B$','$-B$','$B^{-1}$','$0$'])
 if n>5:prefix=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.', 'Original authored matrix-algebra question; no specific authentic source item is asserted for this mechanism.',prefix)
 key=None if n==4 else int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]);prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 if n==4:prefix=re.sub(r' data-answer="\d+"','',prefix)
 elif 'data-answer=' not in prefix:prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-answer="{key}"',1)
 else:assert int(attrs['data-answer'])==key
 visual='<section class="concept-animation question-specific-animation" data-scenes="'+scene_map[n]+'" aria-label="Verified construction for question '+str(n)+'"><p>The model declares its exact matrix data and demonstrates the corresponding operation.</p></section>' if n in scene_map else ''
 value=prefix+'<details class="exam-solution"><summary>Read the complete derivation, checks, and diagnosed alternatives</summary>'+render(answers[n])+visual+'</details></section>';replacements.append((a,b,value));records.append(dict(index=n,answer=key,intendedAnswer=3 if n==4 else None,sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(replacements):page=page[:a]+v+page[b:]
bridge=render((E/'l_matrices-method-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1);page=page.replace('<h2 id="worked-problems">',bridge+'<h2 id="worked-problems">',1)
rule_text=(E/'l_matrices-exam-rules.md').read_text().replace('13.8 Detailed examination decisions','Detailed examination decisions').replace('the fifty complete rules above','the seventeen complete rules above')
for i in range(51,67):rule_text=rule_text.replace('**'+str(i)+'.','**'+str(i-33)+'.')
page=page.replace('<h2 id="references">',render(rule_text)+'<h2 id="references">',1)
page=page.replace('data-scenes="row-elimination"','data-scenes="matrices-question-power"')
page=page.replace('Approved English chapter','Revised English review draft').replace('Approved chapter','Revised review draft').replace('Student-approved chapter','Revised review draft').replace('50 exam decision notes','33 complete examination decisions').replace('50-rule review','33-rule review').replace('50 examination rules','33 examination rules')
page=page.replace('Actual slips in strict triangularity, identity dimensions, and row-operation labels are corrected rather than propagated.','Fresh source inspection withdraws the earlier allegation about Oxford strict triangularity: its definition is correct. Verified identity-size, outer-product endpoint and row-operation label slips are independently repaired.')
page=page.replace('Strict-triangular and identity-dimension slips are corrected in the synthesis.','The identity-dimension proof slip is corrected; the earlier strict-triangular accusation is withdrawn because the actual definition is correct.')
page=page.replace('archived Iranian MSc and PhD papers remain reserved for the final month as requested.','authentic Iranian MSc and PhD applications are included under the later explicit archive-analysis instruction.')
page=page.replace('The student explicitly approved this chapter on 2026-10-02; it is now ready in the finished library.','This newly revised edition remains a review draft. Approval of its earlier edition does not label the rewritten edition student-approved.')
notice='<aside class="deep-review-notice"><strong>Matrix algebra revision · 12 October 2026.</strong> All 47 answers are individually rewritten with exact arithmetic, constructive proofs and diagnosed alternatives. Seven mathematical construction sections and sixteen detailed decisions supplement the retained full lesson, all 36 tutorials and seventeen foundational review rules: 33 rules in this edition. Four core university selections were freshly rechecked within recorded written bounds. Authentic Q113 option 1 is corrected to 37; Q31 retains its literal ambiguity. Dedicated models replace unrelated repeated players. This edition is a review draft.</aside>'
page=page.replace('<article',notice+'<article',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];style=style.replace('</style>','.source-ambiguity{margin:1rem 0;padding:1rem;border-left:3px solid #aa8641;background:#fcf8ef;line-height:1.65}.matrix-lab svg{display:block;width:100%;max-height:360px}.matrix-figure svg{max-height:330px}</style>');page=page.replace('</head>',style+'</head>')
from matrices_diagrams import figure
figs=list(re.finditer(r'<figure class="matrix-figure">[\s\S]*?</figure>',page));assert len(figs)==2
for match,kind in reversed(list(zip(figs,['product','composition']))):page=page[:match.start()]+figure(kind)+page[match.end():]
page=page.replace('General rank, elimination, determinant, eigenvalue, and SVD results remain scheduled in their own chapters.','The construction sections explicitly prove the elementary dimension, determinant and coordinate results needed by this bank. Full elimination, general spectral theory and SVD remain later chapters.')
corrections=[]
for target in ['d_counting','s_counting','l_gauss']:
 path=R/f'dist/chapters/{target}.html';s=path.read_text();edits=[]
 for a,b,attrs,q in ns['questions'](s):
  if attrs.get('data-source-id')!='MS_CS_1405_Q113':continue
  match=re.search(r'(<div class="exam-option"><b>1\.</b><div>)([\s\S]*?)(</div></div>)',q);assert match
  if ns['plain'](match[2])=='32':
   value=q[:match.start(2)]+render('37')+q[match.end(2):];edits.append((a,b,value))
 for a,b,v in reversed(edits):s=s[:a]+v+s[b:]
 if edits:path.write_text(s,encoding='utf-8');corrections.append(dict(topicId=target,sourceId='MS_CS_1405_Q113',scope='Only original option 1 corrected from 32 to 37; wider review not claimed.'))
page=page.replace('<mo>-</mo>','<mo>−</mo>')
if not corrections:corrections=[dict(topicId='l_gauss',sourceId='MS_CS_1405_Q113',scope='Only original option 1 corrected from 32 to 37; wider review not claimed.')]
(R/'dist/chapters/l_matrices.html').write_text(page,encoding='utf-8');(E/'l_matrices-revision.json').write_text(json.dumps(dict(topicId='l_matrices',baselineCommit=BASE,status='rewritten_pending_checks',questionCount=47,studentApproval=False,records=records,relatedSourceCorrections=corrections),indent=2)+'\n')
print({'questions':47,'words':sum(q['words'] for q in records),'relatedSourceCorrections':corrections,'math':page.count('<math')})
