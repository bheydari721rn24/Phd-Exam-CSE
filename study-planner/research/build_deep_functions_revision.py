from pathlib import Path
import ast,json,re,hashlib,subprocess,sys
from markdown_it import MarkdownIt
from read_functions_bank import rows
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='162799857108eb67965f6d2a54526a9da82bb3e7'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'pure_read_helpers','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):
 return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
parts=re.split(r'^## Q(\d+)\s*$',(E/'d_functions-solutions.md').read_text(encoding='utf-8'),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/d_functions.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==len(answers)==47
scenes={1:'cardinality-counter',2:'quantified-cycle',3:'monotone-five-five',4:'onto-six-four',5:'integer-shift-excerpt',6:'image-three',7:'sections-two-three-four',8:'endpoints-six-four',9:'idempotent-two-5',10:'composite-counter',11:'prescribed-fiber',12:'image-collision',13:'involution-two-5',46:'idempotents-four',47:'split-two-three'}
for a,name in[(14,'injection'),(18,'onto-three'),(22,'idempotent-two'),(26,'involution-two'),(30,'monotone-three'),(34,'sections-three'),(38,'one-cycle'),(42,'fixed-two')]:
 for j,n in enumerate([5,8]):scenes[a+j]=name+'-'+str(n)
edits=[];records=[]
for n,(a,b,attrs,q)in enumerate(entries,1):
 end=q.find('<details');end=end if end>=0 else q.index('<p><strong>Correct option:');prefix=q[:end];c=rows[n-1];anchor='exam-provenance'if n<=45 else'exam-label';match=re.search(r'<p class="'+anchor+r'">[\s\S]*?</p>',prefix);assert match,(n,anchor);retained=prefix[:match.end()];stem=c['stem'];options=c['options']
 if n==46:stem=r'How many total functions on a four-element labelled set satisfy $f\circ f=f$?';options=['$24$','$36$','$41$','$64$']
 if n==47:stem=r'A has two labelled elements and B three. How many ordered function pairs $f:A\to B$, $g:B\to A$ satisfy $g\circ f=\operatorname{id}_A$?';options=['$6$','$8$','$12$','$18$']
 stem=stem.replace('in the positive-integer parameter domain, subject to the additional conditions stated above','for all positive integers satisfying the stated conditions')
 if 22<=n<=25 or 42<=n<=45:stem+=r' Assume $n\ge2$.'
 if 26<=n<=29:stem+=r' Assume $n\ge4$.'
 if n>=6:retained=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.','Independently authored function question; no specific authentic source item is claimed for this mechanism.',retained)
 prefix=retained+render(stem)+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(v)+'</div></div>'for i,v in enumerate(options,1))+'</div>'
 key=c['answer'];prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 visual='<section class="concept-animation question-specific-animation" data-scenes="functions-question-'+scenes[n]+'"><p>This model uses this question’s finite types, fixed constraints or explicitly named counterexample. Representative cases are distinguished from exhaustive enumerations.</p></section>'if n in scenes else''
 answer='Correct option: '+str(key)+'.\n\n'+answers[n]
 edits.append((a,b,prefix+'<details class="exam-solution"><summary>Read the full derivation, conceptual proof and individual option diagnoses</summary>'+render(answer)+visual+'</details></section>'))
 records.append(dict(index=n,answer=key,sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(edits):page=page[:a]+v+page[b:]
bridge=(E/'d_functions-method-instruction.md').read_text()+'\n\n'+(E/'d_functions-transfer-challenges.md').read_text();needle='<h2 id="proof-tutorials">';assert needle in page;page=page.replace(needle,render(bridge).replace('<h2>','<h2 id="mathematical-bridge">',1)+needle,1)
for n,names in{1:'bounded-fibers-six',2:'split-two-four',3:'powerset-roundtrips',4:'endpoints-eight-five',5:'affine-quotient',6:'involutions-eight',7:'power-seven',8:'cycles-three-four',9:'weighted-composite',10:'restricted-parabola'}.items():
 a=page.index('<h3>Challenge '+str(n)+'.');z=page.index('</h3>',a)+5;visual='<section class="concept-animation transfer-specific-animation" data-scenes="functions-question-'+names+'"><p>The displayed data belong to this solved challenge. The explanation identifies which finite cases are exhaustive and which illustrate a general proof.</p></section>';page=page[:z]+visual+page[z:]
a=page.index('<h2 id="review">');z=page.index('<h2 id="laboratory">',a);page=page[:a]+render((E/'d_functions-exam-rules.md').read_text()).replace('<h2>','<h2 id="review">',1)+page[z:]
for anchor,names in{'fibers':'powerset-roundtrips','composition':'composite-counter,weighted-composite','inverses':'sections-two-three-four','images':'powerset-roundtrips','counting':'onto-six-four,onto-three-5'}.items():page=re.sub(r'(<section id="animation-'+anchor+r'"[^>]*data-scenes=")[^"]+',lambda m:m[1]+','.join('functions-question-'+v for v in names.split(',')),page)
page=page.replace('Student-approved chapter','Revised English review draft').replace('18 examination notes','38 detailed examination decisions').replace('No archived Iranian entrance-examination question is used in this chapter.','Five authentic examination items are identified and their original scanned pages have been reread for this revision.').replace('This chapter has been approved by the student.','This rewritten edition remains a review draft; approval of an earlier edition is not transferred to the revision.')
a=page.index('<p>This chapter synthesizes four principal written');z=page.index('</p>',a)+4;page=page[:a]+render('This revision freshly combines the written functions scopes of Cambridge, Stanford, MIT and Cornell, with all seven CMU assignment families as an additional independently reviewed contribution. The extensive Oxford reading remains a historical source within its recorded bounds, rather than being counted as a fresh retrieval. The nine-university candidate comparison, exact read scopes and scientific qualifications are recorded in the [source audit](../reviews/d_functions-sources.html).')+page[z:]
notice='<aside class="deep-review-notice"><strong>Functions revision · 13 October 2026.</strong> All 47 bank answers are rewritten, with eight further mathematical constructions, ten solved synthesis challenges and 38 detailed examination decisions. The full lesson and all 42 tutorials remain. Mathematical and rendered checks are pending.</aside>';page=page.replace('<article',notice+'<article',1)
page=page.replace('</nav>','<a href="#mathematical-bridge">Deeper constructions</a></nav>',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
page=re.sub(r'(semantic-diagrams\.js|concept-unified\.js)(?:\?[^"\s>]*)?',r'\1?v=deep-functions-18-20261013',page)
page=re.sub(r'(advanced-simulations\.js|concept-animation\.js|teaching-transitions\.js)(?:\?[^"\s>]*)?',r'\1?v=deep-functions-18-20261013',page)
from space_number_prose import fix
page=fix(page)
for letter in ['A','B','S','T','E']:old='<mo>|</mo><mi>'+letter+'</mi><mo>|</mo>';page=page.replace(old,'<mrow>'+old+'</mrow>')
(R/'dist/chapters/d_functions.html').write_text(page,encoding='utf-8')
(E/'d_functions-revision.json').write_text(json.dumps(dict(topicId='d_functions',baselineCommit=BASE,status='rewritten_pending_mathematical_and_rendered_checks',studentApproval=False,questionCount=47,retainedFullTutorials=42,lectureAdditionSections=8,addedSolvedTransferChallenges=10,finalDetailedDecisions=38,records=records,questionModelPlacements=len(scenes),sourceReview='research/deep-library-revision/d_functions-course-recheck.json'),indent=2)+'\n',encoding='utf-8')
print({'answers':47,'words':sum(v['words']for v in records),'questionModelPlacements':len(scenes),'math':page.count('<math')})
