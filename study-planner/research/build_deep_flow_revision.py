from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='b786d491f7285f3ab2154d958988641fd43c3ee1'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):
 s=s.replace(r'\mathbin{\&}',r'\operatorname{bitand}')
 return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
parts=re.split(r'^## Q(\d+)\s*$',(E/'p_flow-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip() for i in range(1,len(parts),2)}
authpath=B/'exam-calibration/actual-items.json';actual=json.loads(authpath.read_text());auth={q['id']:q for q in actual};copy=auth['MS_CS_1393_Q167'];copy['options'][3]=copy['options'][3].replace('store(n-1,i+2)','store(n-2,i+2)');assert 'store(n-2,i+2)' in copy['options'][3]
copy['translationStatus']='Original option4 freshly rechecked on PDFpage34,12October2026: source stride2, destinationoffset1/stride2.'
original={q['title']:q for f in (B/'exam-calibration').glob('original-*.json') for q in json.loads(f.read_text()) if q.get('topic')=='p_flow'}
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/p_flow.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==len(answers)==45
def options(vals):return '<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(v)+'</div></div>' for i,v in enumerate(vals,1))+'</div>'
scene_map={1:'triples',2:'split',3:'copy-source',4:'dangling',5:'filter-odd',6:'switch',7:'orbit-unreachable',8:'copy10',9:'postfix',10:'ranking',11:'nested',12:'sum-before',16:'stateful',20:'filter-third',24:'threshold',28:'binary-tree',32:'toll',36:'swap',40:'posttest',44:'priorities',45:'orbit-target'}
edits=[];records=[]
for n,(a,b,attrs,q) in enumerate(entries,1):
 end=q.index('<details') if '<details' in q else re.search(r'<p><strong>Correct option:',q).start();prefix=q[:end]
 if n<=43:
  title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1]);c=auth[attrs['data-source-id']] if n<=3 else original[re.sub(r'^Question \d+\. ','',title)]
  stop=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end();prefix=prefix[:stop]+render(c['stem'])+options(c['options'])
 if n>=4:prefix=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.', 'Original authored control-flow question; no specific authentic source item is asserted for this mechanism.',prefix)
 if n==3:
  pos=prefix.index('<div class="exam-options">');prefix=prefix[:pos]+'<aside class="source-ambiguity"><strong>Source transcription repair.</strong> All four printed alternatives use source decrement two. The fourth differs through destination offset one and stride two. Concrete copying assumes separate logical arrays or an independently proved overlap-safe implementation.</aside>'+prefix[pos:]
 key=int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]);prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 if 'data-answer=' not in prefix:prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-answer="{key}"',1)
 else:assert int(attrs['data-answer'])==key,(n,attrs['data-answer'],key)
 visual='<section class="concept-animation question-specific-animation" data-scenes="flow-question-'+scene_map[n]+'" aria-label="Actual control mechanism for question '+str(n)+'"><p>This bounded model records the actual path, values and counted event rather than substituting a generic algorithm.</p></section>' if n in scene_map else ''
 edits.append((a,b,prefix+'<details class="exam-solution"><summary>Read the full execution trace, mathematical proof, and alternatives</summary>'+render(answers[n])+visual+'</details></section>'));records.append(dict(index=n,answer=key,sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(edits):page=page[:a]+v+page[b:]
for n,(_,_,attrs,_) in enumerate(entries[:3],1):auth[attrs['data-source-id']]['solution']=answers[n]
authpath.write_text(json.dumps(actual,ensure_ascii=False,indent=2)+'\n')
page=page.replace('<h2 id="worked-problems">',render((E/'p_flow-method-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1)+'<h2 id="worked-problems">',1)
page=page.replace('<h2 id="references">',render((E/'p_flow-exam-rules.md').read_text())+'<h2 id="references">',1)
page=page.replace('No Iranian entrance-exam paper is used in this chapter, consistent with the final-month reservation.','Three authentic entrance-exam items are included and freshly checked against original PDF pages under the later archive-analysis instruction.')
page=page.replace('Student-approved chapter','Revised English review draft').replace('Approved English chapter','Revised English review draft').replace('15 examination notes','35 detailed examination decisions')
page=re.sub(r'The student approved this chapter on [^<]*?finished library\.', 'The earlier edition received approval; this individually rewritten edition remains a review draft.',page)
page=re.sub(r'<p>Student approved this chapter[^<]*?[\s\S]*?</p>','<p>The continuously authorized individual library review continues after this edition.</p>',page)
notice='<aside class="deep-review-notice"><strong>Control-flow revision · 12 October 2026.</strong> All45 answers are individually rewritten, with seven construction sections, eight solved transfer extensions and twenty additional final decisions. The original full lesson and all36 tutorials remain. SourceQ167 option4 and Q44 condition-priority analysis are corrected. Scoped readings distinguish fresh evidence from inaccessible material. Diagram and browser checks are still pending; this is an integration draft.</aside>'
page=page.replace('<article',notice+'<article',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
page=page.replace('<mo>-</mo>','<mo>−</mo>')
mapping={'animation-state':'swap','animation-conditionals':'dangling','animation-transfers':'filter-odd,switch,nested,priorities','animation-termination':'orbit-unreachable,ranking,posttest'}
for anchor,names in mapping.items():
 value=','.join('flow-question-'+n for n in names.split(','));page=re.sub(r'(<section id="'+anchor+r'"[^>]*data-scenes=")[^"]+',lambda m:m[1]+value,page)
(R/'dist/chapters/p_flow.html').write_text(page,encoding='utf-8')
# Reconcile the corrected original across placements without claiming their wider review complete.
related=[]
for path in (R/'dist/chapters').glob('*.html'):
 if path.stem=='p_flow':continue
 s=path.read_text(encoding='utf-8');changes=[]
 for a,b,attrs,q in ns['questions'](s):
  if attrs.get('data-source-id')!='MS_CS_1393_Q167':continue
  end=q.index('<details') if '<details' in q else re.search(r'<p><strong>Correct option:',q).start();prefix=q[:end];pos=prefix.index('<div class="exam-options">');prefix=prefix[:pos]+options(copy['options'])
  new=prefix+'<details class="exam-solution"><summary>Read the source-corrected complete copying derivation</summary>'+render(answers[3])+'</details></section>';changes.append((a,b,new))
 for a,b,v in reversed(changes):s=s[:a]+v+s[b:]
 if changes:path.write_text(s,encoding='utf-8');related.append(dict(topicId=path.stem,sourceId=copy['id'],scope='Only original option4 and its source-specific explanation reconciled. The wider chapter review is not claimed complete.'))
(E/'p_flow-revision.json').write_text(json.dumps(dict(topicId='p_flow',baselineCommit=BASE,status='rewritten_pending_diagrams_and_checks',questionCount=45,studentApproval=False,records=records,relatedSourceCorrections=related),indent=2)+'\n')
print({'questions':45,'answerWords':sum(x['words'] for x in records),'math':page.count('<math'),'relatedCorrections':related})
