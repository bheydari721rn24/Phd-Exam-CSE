from pathlib import Path
import ast,hashlib,json,re,subprocess,sys,runpy
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='77bb96d8943bae3480a2f90cde622447d29587d4'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
def option(v):return render('$'+v+'$' if re.fullmatch(r'-?\d+(?:\.\d+)?',v.strip()) else v)
parts=re.split(r'^## Q(\d+)\s*$',(E/'g_number-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip() for i in range(1,len(parts),2)}
data=runpy.run_path(str(B/'read_number_question_bank.py'),run_name='bank_data')['rows']
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/g_number.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==len(answers)==45
scene_map={1:'original-overflow',2:'chop',3:'associativity',4:'carry',5:'product',6:'normal',7:'binary-tie',8:'extension',9:'decimal',10:'termination',11:'bytes',12:'bias',16:'scale',20:'negative',24:'max-sum',28:'zero',32:'finite',36:'spacing',40:'hex',44:'signed-product',45:'nearest'}
edits=[];records=[]
for n,(a,b,attrs,q) in enumerate(entries,1):
 end=q.find('<details');end=end if end>=0 else q.index('<p><strong>Correct option:');prefix=q[:end];c=data[n-1]
 if n<=43:
  stop=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end();prefix=prefix[:stop]+render(c['stem'].replace("two\\'s","two's"))+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+option(v)+'</div></div>' for i,v in enumerate(c['options'],1))+'</div>'
 else:
  stop=re.search(r'<p class="exam-label">[\s\S]*?</p>',prefix).end()
  stem=r'A signed eight-bit two\'s-complement fixed-point format has two fractional bits. Raw signed integer inputs are $-6$ and $5$. Multiply their represented real values and round back to the same scale using nearest, ties to even. What real value is stored?' if n==44 else r'Quantize $1.625$ to an unsigned fixed-point format with two fractional bits, nearest-even rounding, and enough integer range. What real value is stored?'
  values=['-1.75','-1.875','-2.0','-7.5'] if n==44 else ['1.25','1.5','1.625','1.75'];prefix=prefix[:stop]+render(stem.replace("\\'","'"))+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+option(v)+'</div></div>' for i,v in enumerate(values,1))+'</div>'
 if n>=4:prefix=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.', 'Original authored representation question; no specific authentic source item is asserted for this mechanism.',prefix)
 if n in [16,17,18,19]:
  pos=prefix.index('<div class="exam-options">');prefix=prefix[:pos]+'<aside class="source-ambiguity">The unsigned format has enough total bits for the stated raw integer; '+render('$n+2$ bits suffice for positive $n$.')+'</aside>'+prefix[pos:]
 key=int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]);assert key==c['answer'];prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 if 'data-answer=' not in prefix:prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-answer="{key}"',1)
 visual='<section class="concept-animation question-specific-animation" data-scenes="number-question-'+scene_map[n]+'" aria-label="Actual representation mechanism for question '+str(n)+'"><p>The model uses the named input, width, scale and rounding or coding contract from this question.</p></section>' if n in scene_map else ''
 edits.append((a,b,prefix+'<details class="exam-solution"><summary>Read the complete mathematical derivation, trace, and alternatives</summary>'+render(answers[n])+visual+'</details></section>'));records.append(dict(index=n,answer=key,sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(edits):page=page[:a]+v+page[b:]
page=page.replace('<h2 id="worked-problems">',render((E/'g_number-method-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1)+'<h2 id="worked-problems">',1)
rules=(E/'g_number-exam-rules.md').read_text();rules=re.sub(r'^(### )(\d+)(\.)',lambda m:m[1]+str(int(m[2])+1)+m[3],rules,flags=re.M);page=page.replace('<h2 id="references">',render(rules)+'<h2 id="references">',1)
page=page.replace('Student-approved chapter','Revised English review draft').replace('16 examination notes','36 detailed examination decisions')
page=page.replace('Archived Iranian entrance-exam questions remain reserved for the final month. The examination guidance here is mathematical problem-solving guidance, not a statistical analysis of those deferred papers.','Three authentic source questions are used under the later instruction to analyze the repository. Their original page images were inspected; their solutions are independently derived.')
page=page.replace('None uses the deferred Iranian examination archive.','These retained authored tutorials use no archived Iranian question; the authentic questions are identified separately in the examination bank below.').replace('The stated chapter boundary and deferred archive are explicit;','The chapter boundary and authentic-source distinctions are explicit;')
page=re.sub(r'<p>This chapter was explicitly approved by the student on [\s\S]*?</p>','<p>The earlier edition received approval; this rewritten edition remains a review draft under the continuous individual-library review.</p>',page)
page=page.replace('An all-zero exponent uses subnormal or zero rules; an all-one exponent selects infinity or NaN.','In a declared IEEE-style format, an all-zero exponent uses subnormal or zero rules and an all-one exponent selects infinity or NaN; other custom formats require their own reserved-field definitions.')
page=page.replace('Subnormals use the minimum normal exponent without the hidden leading one','In the declared IEEE-style convention, subnormals use the minimum normal exponent without the hidden leading one')
notice='<aside class="deep-review-notice"><strong>Number representation revision · 13 October 2026.</strong> All 45 answers are individually rewritten. Seven construction sections, ten fully solved transfer challenges and twenty additional final decisions supplement the retained full lesson and all 36 tutorials. Four university written bodies were actually reread, plus the Princeton Gray supplement. Diagram and rendered checks remain pending; this is an integration draft.</aside>'
page=page.replace('<article',notice+'<article',1);style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
mapping={'conversion':'division','fractions':'fraction-conversion','signed':'multi-decode,extension,zero','arithmetic':'carry','gray':'gray','errors':'hamming,secded'}
for anchor,names in mapping.items():page=re.sub(r'(<section id="animation-'+anchor+r'"[^>]*data-scenes=")[^"]+',lambda m:m[1]+','.join('number-question-'+n for n in names.split(',')),page)
# The decade-code mechanism belongs beside its complete original teaching.
page=page.replace('<h2 id="gray">','<section class="concept-animation" data-scenes="number-question-bcd" aria-label="BCD correction for the exact98+76+1 example"></section><h2 id="gray">',1)
page=page.replace('<mo>-</mo>','<mo>−</mo>');from space_number_prose import fix;page=fix(page);(R/'dist/chapters/g_number.html').write_text(page,encoding='utf-8')
(E/'g_number-revision.json').write_text(json.dumps(dict(topicId='g_number',baselineCommit=BASE,status='rewritten_pending_model_and_rendered_checks',questionCount=45,studentApproval=False,finalRules=36,lectureAdditionSections=7,addedSolvedTransferChallenges=10,retainedFullTutorials=36,records=records,sourceReview='research/deep-library-revision/g_number-course-recheck.json'),indent=2)+'\n',encoding='utf-8')
print({'questions':45,'answerWords':sum(x['words'] for x in records),'math':page.count('<math'),'status':'integration_draft'})
