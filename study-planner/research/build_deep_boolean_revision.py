from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
from read_boolean_bank import rows
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='0ef53d08d354001a3dc205711dceafecd0e277f9'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
parts=re.split(r'^## Q(\d+)\s*$',(E/'g_boolean-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/g_boolean.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==len(answers)==53
scenes={1:'sets',2:'cnf',3:'weighted-parity',4:'majority',5:'implication',6:'nand',7:'mux',8:'implication',9:'hazard',10:'free-pairs',11:'quantifier',12:'majority-anf',13:'derivative',14:'cofactor',15:'monotone-two',52:'antichains',53:'fixed-self-dual'}
for i,name in [(16,'chain-5'),(17,'chain-8'),(20,'parity-5'),(21,'parity-8'),(24,'self-dual-3'),(25,'self-dual-4'),(28,'products-5'),(29,'products-8'),(32,'weight-5'),(33,'weight-8'),(36,'affine-3'),(37,'affine-4'),(40,'false-5'),(41,'false-8'),(44,'quadratic-3'),(45,'quadratic-4'),(48,'symmetric-3'),(49,'symmetric-4')]:scenes[i]=name
edits=[];records=[]
for n,(a,b,attrs,q)in enumerate(entries,1):
 end=q.find('<details');end=end if end>=0 else q.index('<p><strong>Correct option:');prefix=q[:end];c=rows[n-1]
 anchor='exam-provenance'if n<=51 else'exam-label';stop=re.search(r'<p class="'+anchor+r'">[\s\S]*?</p>',prefix).end();retained=prefix[:stop]
 # Preserve faithful original circuit schematics in authentic stems as well as new dynamic traces.
 figures=''.join(re.findall(r'<figure\b[\s\S]*?</figure>',prefix))if n in [6,7]else''
 stem=c['stem'];options=c['options']
 if n==52:stem='How many Boolean functions of three inputs are nondecreasing in every input? Count distinct truth functions, including constants.';options=['$8$','$16$','$20$','$256$']
 if n==53:stem='A self-dual function on three inputs has $F(000)=0$ and $F(111)=1$ fixed. No other rows are specified. How many distinct completions exist?';options=['$4$','$8$','$16$','$64$']
 if n==19:stem+=r' Assume $n\ge2$ when comparing strict strength with the equivalence chain.'
 if 28<=n<=31:retained=retained.replace('disjoint two-input products','products on disjoint input pairs')
 stem=stem.replace('in the positive-integer parameter domain, subject to the additional conditions stated above','for all positive integers $n$ satisfying the stated conditions')
 if n>=8:retained=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.','Original authored Boolean-function question; no specific authentic source item is asserted for this mechanism.',retained)
 prefix=retained+render(stem)+figures+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(v)+'</div></div>'for i,v in enumerate(options,1))+'</div>'
 key=int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]);assert key==c['answer'];prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 visual='<section class="concept-animation question-specific-animation" data-scenes="boolean-question-'+scenes[n]+'" aria-label="Actual Boolean mechanism for question '+str(n)+'"><p>This model uses the input function, circuit connections or exact counting domain specified in this question.</p></section>'if n in scenes else''
 edits.append((a,b,prefix+'<details class="exam-solution"><summary>Read the full derivation, conceptual explanation and exact alternatives</summary>'+render(answers[n])+visual+'</details></section>'))
 records.append(dict(index=n,answer=key,sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(edits):page=page[:a]+v+page[b:]
# Retain the full original lesson; add the bridge before the forty existing tutorials.
needle='<h2 id="proof-tutorials">'
if needle not in page:
 candidates=re.findall(r'<h2[^>]*>[^<]*',page);print(candidates);raise AssertionError('Inspect the actual tutorial anchor before inserting')
bridge=(E/'g_boolean-method-instruction.md').read_text()+'\n\n'+(E/'g_boolean-transfer-challenges.md').read_text();page=page.replace(needle,render(bridge).replace('<h2>','<h2 id="mathematical-bridge">',1)+needle,1)
page=page.replace('<h2 id="references">',render((E/'g_boolean-exam-rules.md').read_text())+'<h2 id="references">',1)
for anchor,names in {'laws':'de-morgan,absorption','simplification':'hazard','xor':'xor','selectors':'implication','cofactors':'selector,quantifier'}.items():page=re.sub(r'(<section id="animation-'+anchor+r'"[^>]*data-scenes=")[^"]+',lambda m:m[1]+','.join('boolean-question-'+v for v in names.split(',')),page)
page=page.replace('Student-approved chapter','Revised English review draft').replace('16 examination notes','36 detailed final decisions')
page=re.sub(r'<p>The student (?:explicitly )?approved[\s\S]*?</p>','<p>This rewritten edition remains a review draft; approval of an earlier edition is not approval of these new revisions.</p>',page)
page=page.replace('No archived Iranian exam has been mined for this chapter','The seven authentic source page images were reread for this revision').replace('No Iranian examination archive was read or mined','Seven authentic source questions were reread under the later examination-analysis instruction')
page=page.replace('Archived Iranian entrance-exam questions remain reserved for the final month.','The later examination-analysis instruction applies; the authentic bank is identified separately.')
notice='<aside class="deep-review-notice"><strong>Boolean algebra revision · 13 October 2026.</strong> All 53 bank answers are rewritten, with corrected original CNF options, seven teaching constructions, ten distinct solved challenges and twenty additional detailed decisions. The full lesson and all forty tutorials remain. Mathematical and rendered checks are pending; this is an integration draft.</aside>'
page=page.replace('<article',notice+'<article',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
page=re.sub(r'(semantic-diagrams\.js|concept-unified\.js)(?:\?[^"\s>]*)?',r'\1?v=deep-boolean-15-20261013',page)
from space_number_prose import fix
page=fix(page);(R/'dist/chapters/g_boolean.html').write_text(page,encoding='utf-8')
(E/'g_boolean-revision.json').write_text(json.dumps(dict(topicId='g_boolean',baselineCommit=BASE,status='rewritten_pending_model_and_rendered_checks',questionCount=53,studentApproval=False,retainedFullTutorials=40,lectureAdditionSections=7,addedSolvedTransferChallenges=10,finalDetailedDecisions=36,records=records,questionModelPlacements=len(scenes),sourceReview='research/deep-library-revision/g_boolean-course-recheck.json',authenticOptionCorrections={'Phd_CS_1405_Q15':[3,4]}),indent=2)+'\n',encoding='utf-8')
print({'answers':53,'words':sum(x['words']for x in records),'questionModelPlacements':len(scenes),'math':page.count('<math')})
