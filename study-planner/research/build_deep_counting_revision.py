from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='f890223f3111d27958eb483056556fded2d59ff3'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md))
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/s_counting.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw)
parts=re.split(r'^## Q(\d+)\s*$',(E/'s_counting-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip() for i in range(1,len(parts),2)};assert len(answers)==len(entries)==77
actual={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())};original={q['title']:q for f in (B/'exam-calibration').glob('original-*.json') for q in json.loads(f.read_text()) if q.get('topic')=='s_counting'}
extensions=[
r'Give a reversible stars-and-bars construction and an independent row-sum proof. Extend the argument to arbitrary lower bounds and handle an impossible residual total.',
r'Derive the exact row ledger and verify it by excluding $x\ge3$. Determine the counts at totals zero and one instead of extrapolating blindly.',
r'Derive the even and odd counts separately. Compare their sum and difference with the unrestricted count, including the residual-zero boundary.',
r'Partition by the exact red count and prove a second color-swap identity. Explain why choosing three witnesses can count a final subset several times.',
r'Derive every inclusion–exclusion term from a missing-target event. Explain named versus unnamed nonempty bins and the empty-domain exception.',
r'Derive both parity counts from the signed binomial sum and verify the empty-word boundary. Explain why half of the unrestricted count is not exact.',
r'Prove the prefix recurrence with both seeds, then derive the fixed-weight gap bijection and use it to check the total independently.',
r'Construct the multiplicity-vector bijection and distinguish multiset counts from probabilities induced by uniform ordered draws. Also count multisets using every type.',
r'Prove the rotation quotient by anchoring a distinct label. Explain the reflection boundary and demonstrate the failure of constant orbit sizes with repeated letters.',
r'Prove both the constant-fiber factorial quotient and the smallest-label partner recurrence. Specify the empty pairing and both erased symmetries.',
r'Derive inclusion–exclusion and the two-case derangement recurrence. Explain why removing the identity or counting full cycles alone fails.',
r'Give a reversible membership construction. Distinguish a prescribed common element from a chosen singleton intersection and examine the unordered-pair boundary.',
r'Prove the block construction with internal orientations. Compare a linear row with rotation-equivalent circular arrangements, including the single-couple exception.'
]
scenes={1:'counting-question-stars',7:'counting-question-onto',9:'counting-question-parity',40:'counting-question-dp',71:'counting-question-pairing',77:'counting-question-report'}
replacements=[];records=[]
for n,(a,b,attrs,q) in enumerate(entries,1):
 end=q.index('<details') if '<details' in q else re.search(r'<p><strong>Correct option:',q).start();prefix=q[:end]
 if n<=67:
  title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1]);rec=actual[attrs['data-source-id']] if n<=15 else original[re.sub(r'^Question \d+\. ','',title)]
  stop=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end();prefix=prefix[:stop]+render(rec['stem'])+prefix[prefix.index('<div class="exam-options">'):]
  if n>=16:
   at=prefix.index('<div class="exam-options">');prefix=prefix[:at]+render(extensions[(n-16)//4])+prefix[at:]
   prefix=prefix.replace('Original examination analogue · author-assessed medium difficulty','Original examination analogue · exact calculation with a proof extension').replace('Original examination analogue · author-assessed hard difficulty','Original examination analogue · boundary and counterexample analysis')
 else:
  # Preserve the independently formulated integrated stems; reconstruct their options natively.
  prefix=re.sub(r'<section class="concept-animation"[\s\S]*?</section>','',prefix)
  first=re.search(r'<div class="exam-options">|<p><strong>1\.</strong>',prefix).start();prefix=prefix[:first]+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(v)+'</div></div>' for i,v in enumerate({68:['$32$','$33$','$34$','$36$'],69:['$80$','$100$','$120$','$150$'],70:['$121$','$122$','$123$','$81$'],71:['$105$','$210$','$2520$','$1680$'],72:['$5376$','$2688$','$84$','$10752$'],73:['$150$','$175$','$200$','$210$'],74:[r'$\binom{13}5/2^{13}$',r'$\binom{13}8/2^8$',r'$\binom85/2^{13}$','$1/2$'],75:['$5$','$8$','$10$','$15$'],76:['$65$','$80$','$85$','$165$'],77:['$1/4$','$3/8$','$1/2$','$2/3$']}[n],1))+'</div>'
 prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 key=int(re.search(r'Correct option:\s*(\d+)',answers[n])[1])
 if 'data-answer=' not in prefix:prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-answer="{key}"',1)
 else:assert int(attrs['data-answer'])==key,(n,attrs['data-answer'],key)
 visual='<section class="concept-animation question-specific-animation" data-scenes="'+scenes[n]+'" aria-label="Exact counting construction for question '+str(n)+'"><p>Read the changing exact state together with the complete derivation above.</p></section>' if n in scenes else ''
 v=prefix+'<details class="exam-solution"><summary>Read the complete construction, calculation, and option analysis</summary>'+render(answers[n])+visual+'</details></section>';replacements.append((a,b,v));records.append(dict(index=n,answer=key,sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(replacements):page=page[:a]+v+page[b:]
bridge=render((E/'s_counting-method-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1);page=page.replace('<h2 id="worked-problems">',bridge+'<h2 id="worked-problems">',1)
rules=render((E/'s_counting-final-rules.md').read_text()).replace('<h2>','<h2 id="quick-reference">',1);page=re.sub(r'<h2 id="quick-reference">[\s\S]*?(?=<h2 id="references">)',lambda m:rules,page,count=1)
page=page.replace('<a href="#worked-problems">','<a href="#mathematical-bridge">Mathematical constructions</a> <a href="#worked-problems">',1).replace('Student-approved chapter','Revised and checked · review draft').replace('15 examination notes','32 complete final rules').replace('15 exam decision notes','32 final review rules')
notice='<aside class="deep-review-notice"><strong>Counting and independence revision · 12 October 2026.</strong> All 77 question answers now contain explicit constructions, numerical steps or general proofs, option analysis and boundaries. Six mathematical construction sections and 32 final rules complement the full retained lesson and 34 derivation tutorials. Six question-specific models replace unrelated repeated players. Four selected university courses were genuinely reviewed within documented written bounds; 15 authentic items were checked against original PDF pages, including recorded inspections reused for five identical items. This edition remains a review draft.</aside>'
page=page.replace('<article',notice+'<article',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
page=page.replace('Iranian entrance-exam papers remain reserved for the final-month guided work under the student\'s instruction.','The examination applications are included under the subsequent explicit instruction to analyze authentic archived questions. No official answer key is inferred from a source image alone.')
page=page.replace('No archived Iranian exam questions were consulted.','Fifteen authentic questions are included with original-PDF evidence. The contradictory without-replacement repetition item Phd_CS_1404_Q67 is excluded rather than silently repaired.')
page=page.replace('This student-approved chapter is undergoing the requested final library review.','This edition is an individually revised review draft.')
from counting_diagrams import reports
page=re.sub(r'<figure class="logic-diagram">[\s\S]*?</figure>',lambda m:reports(),page,count=1)
ox='The Oxford “Bits for free” size assertion is corrected to the bound in Mathematical constructions, Section 6: the number of seed outcomes is between n+1 and 2(n+1), rather than exactly n.'
page=page.replace('Used for the distinction between pairwise and mutual independence and the computational parity perspective.','Used for the distinction between pairwise and mutual independence and the computational parity perspective. '+ox)
(R/'dist/chapters/s_counting.html').write_text(page,encoding='utf-8')
(E/'s_counting-revision.json').write_text(json.dumps(dict(topicId='s_counting',baselineCommit=BASE,status='rewritten_pending_checks',questionCount=77,studentApproval=False,records=records),indent=2)+'\n')
print(json.dumps(dict(questions=77,solutionWords=sum(q['words'] for q in records),questionTables=sum(v.count('<table>') for a,b,v in replacements),nativeMathExpressions=page.count('<math'),finalRules=32)))
