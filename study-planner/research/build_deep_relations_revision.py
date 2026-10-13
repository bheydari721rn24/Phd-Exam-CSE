from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
from read_relations_bank import rows
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='9628d13bd1f5417e4144c95b1be84e18782294bc'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'helpers','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
parts=re.split(r'^## Q(\d+)\s*$',(E/'d_relations-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/d_relations.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==len(answers)==45
scenes={1:'difference',2:'girls-boys',3:'equivalence-intersection',4:'mod-six',5:'union-closure',6:'diagonal-only',7:'exact-powers',8:'block-profile',9:'induced-divisors',10:'bounded-difference',11:'refinement',44:'grid72-covers',45:'grid72-height'}
for a,name in [(12,'equal-blocks'),(16,'reflexive-symmetric'),(20,'antisymmetric'),(24,'irreflexive-symmetric'),(28,'residues'),(32,'nonstrict-order'),(36,'chain-closure'),(40,'triples')]:
 for j,n in enumerate([5,8]):scenes[a+j]=name+'-'+str(n)
edits=[];records=[]
for n,(a,b,attrs,q)in enumerate(entries,1):
 end=q.find('<details');end=end if end>=0 else q.index('<p><strong>Correct option:');prefix=q[:end];c=rows[n-1];anchor='exam-provenance'if n<=43 else'exam-label';stop=re.search(r'<p class="'+anchor+r'">[\s\S]*?</p>',prefix).end();retained=prefix[:stop];stem=c['stem'];options=c['options']
 if n==44:stem=r'The divisors of $72=2^3 3^2$ are ordered by divisibility. How many vertices and cover edges does their Hasse diagram have?';options=[r'$(12,17)$',r'$(12,24)$',r'$(6,17)$',r'$(12,29)$']
 if n==45:stem=r'The divisors of $72=2^3 3^2$ are ordered by divisibility. What is their longest-chain length measured in vertices?';options=[r'$3$',r'$4$',r'$5$',r'$6$']
 stem=stem.replace('in the positive-integer parameter domain, subject to the additional conditions stated above','for positive integers satisfying the stated conditions')
 if n>=4:retained=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.','Original authored relation or order question; no specific authentic source item is asserted for this mechanism.',retained)
 prefix=retained+render(stem)+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(v)+'</div></div>'for i,v in enumerate(options,1))+'</div>'
 key=int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]);assert key==c['answer'];prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 visual='<section class="concept-animation question-specific-animation" data-scenes="relations-question-'+scenes[n]+'" aria-label="Relation mechanism for question '+str(n)+'"><p>This model uses the stated carrier and relation, or the explicitly named countermodel in the proof of a general statement.</p></section>'if n in scenes else''
 edits.append((a,b,prefix+'<details class="exam-solution"><summary>Read the derivation, conceptual proof and exact option diagnoses</summary>'+render(answers[n])+visual+'</details></section>'))
 records.append(dict(index=n,answer=key,sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(edits):page=page[:a]+v+page[b:]
bridge=(E/'d_relations-method-instruction.md').read_text()+'\n\n'+(E/'d_relations-transfer-challenges.md').read_text();needle='<h2 id="proof-tutorials">';assert needle in page
page=page.replace(needle,render(bridge).replace('<h2>','<h2 id="mathematical-bridge">',1)+needle,1)
for n,names in {1:'mod10-interval30',2:'partition-profiles',3:'symmetric-serial',4:'closure-intersection',5:'closure-operations',6:'grid72-covers,grid72-height,linear-extensions',7:'cross-partitions',8:'composition-witnesses',9:'lexicographic-branch',10:'pentagon'}.items():
 needle='<h3>Challenge '+str(n)+'.';a=page.index(needle);z=page.index('</h3>',a)+5
 visual='<section class="concept-animation transfer-specific-animation" data-scenes="'+','.join('relations-question-'+v for v in names.split(','))+'"><p>This model uses this solved challenge’s own carrier, parameters and construction.</p></section>'
 page=page[:z]+visual+page[z:]
page=page.replace('<h2 id="references">',render((E/'d_relations-exam-rules.md').read_text()).replace('<h2>','<h2 id="final-decisions">',1)+'<h2 id="references">',1)
for anchor,names in {'closures':'chain-closure-5,closure-operations','equivalence':'union-closure,cross-partitions','orders':'grid12','bounds':'induced-divisors,pentagon','scheduling':'linear-extensions'}.items():page=re.sub(r'(<section id="animation-'+anchor+r'"[^>]*data-scenes=")[^"]+',lambda m:m[1]+','.join('relations-question-'+v for v in names.split(',')),page)
page=page.replace('Student-approved chapter','Revised English review draft').replace('17 examination notes','37 detailed final decisions')
page=page.replace('and no archived Iranian entrance-exam questions are included at this stage.','and authentic entrance-examination items are identified separately under the later examination-analysis instruction.').replace('Archived Iranian examination papers remain reserved for the final month.','Three authentic original examination pages have been reread for this revision.')
page=page.replace('This is a complete review draft awaiting the student\'s approval for promotion to the approved library.','This rewritten edition is a review draft; earlier approval is not transferred to these revisions.')
page=re.sub(r'<p>The student (?:explicitly )?approved[\s\S]*?</p>','<p>The rewritten edition remains a review draft under the standing authorization for continuous revision.</p>',page)
a=page.index('<p>Four principal written university courses were selected');z=page.index('</p>',a)+4;page=page[:a]+render('Four written university scopes were freshly read for this revision: MIT, Stanford, Cambridge and Cornell. Their complementary contributions are typed relations and scheduling, definition-based proofs, closures and well-foundedness, and quotient/representative reasoning. Oxford’s substantial previously audited scope is retained as a historical supplement; its fresh local retrieval timed out and was not counted as a fifth fresh reading. The documented nine-university candidate pool and exact access/reading bounds are retained in the source audit, rather than claiming a complete worldwide census.')+page[z:]
page=page.replace('<table>','<p>The following table retains the original scoped inventory. The fresh four-course selection above supersedes its earlier ranking; historical readings are distinguished from the current rereading.</p><table>',1)
note=render('### Fresh source qualifications\n\nStanford’s extracted text drops relation negation strokes; physical page 69 was reread visually. Cambridge’s finite-irreflexivity claim is corrected by the two-cycle counterexample, and its composition symbol order is reconciled with the explicit witness definition. MIT’s minimum-element argument requires a nonempty finite carrier, and its scheduling statement is expressed with strict predecessors. Cornell’s quotient examples require representative independence, an admissible target and any necessary existence/uniqueness assumptions. The source audit records these scopes and the fresh Oxford access failure.')
page=page.replace('<h2 id="references">',note+'<h2 id="references">',1)
notice='<aside class="deep-review-notice"><strong>Relations revision · 13 October 2026.</strong> All 45 bank answers are rewritten, with seven deeper mathematical constructions, ten distinct solved synthesis challenges and twenty additional detailed final decisions. The complete lesson and all 46 tutorials remain. Mathematical and rendered checks are pending.</aside>'
page=page.replace('<article',notice+'<article',1);page=page.replace('</nav>','<a href="#mathematical-bridge">Mathematical constructions</a> <a href="#final-decisions">Detailed final decisions</a></nav>',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
page=re.sub(r'(semantic-diagrams\.js|concept-unified\.js)(?:\?[^"\s>]*)?',r'\1?v=deep-relations-17-20261013',page)
from space_number_prose import fix
page=fix(page);page=page.replace('<mo>|</mo><mi>E</mi><mo>|</mo>','<mrow><mo>|</mo><mi>E</mi><mo>|</mo></mrow>');(R/'dist/chapters/d_relations.html').write_text(page,encoding='utf-8')
(E/'d_relations-revision.json').write_text(json.dumps(dict(topicId='d_relations',baselineCommit=BASE,status='rewritten_pending_model_and_rendered_checks',questionCount=45,studentApproval=False,retainedFullTutorials=46,lectureAdditionSections=7,addedSolvedTransferChallenges=10,finalDetailedDecisions=37,records=records,questionModelPlacements=len(scenes),sourceReview='research/deep-library-revision/d_relations-course-recheck.json'),indent=2)+'\n',encoding='utf-8')
print({'answers':45,'words':sum(x['words']for x in records),'questionModelPlacements':len(scenes),'math':page.count('<math')})
