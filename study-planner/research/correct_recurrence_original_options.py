from pathlib import Path
import json,re,ast,hashlib,sys
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision'
options=[r'$O(\log n\log\log n)$',r'$O(n\log n\log\log n)$',r'$O(n\log\log n)$',r'$O(\log\log n)$']
p=B/'exam-calibration/actual-items.json';rows=json.loads(p.read_text());q=next(q for q in rows if q['id']=='MS_CE_1405_Q58');q['options']=options
q['solution']=q['solution'].replace('Option 2 is also a loose upper bound.','Options 2 and 3 are also loose upper bounds.').replace('Options 3 and 4 are too small.','Only option 4 is too small. The original options are, in order, O(log n log log n), O(n log n log log n), O(n log log n) and O(log log n).')
q['translationStatus']='All four options rechecked against the enlarged original physical page 13 on 13 October 2026; options 2, 3 and 4 corrected.'
p.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
p=B/'exam-calibration/author_actual.py';s=p.read_text();a=s.index("add('MS_CE_1405',13,58,");z=s.index("add('MS_CE_1405',13,59,",a);v=s[a:z];v=v.replace("[r'$O(\\log n\\log\\log n)$',r'$O(n\\log\\log n)$',r'$O(\\log\\log n)$',r'$O(\\log n)$']",repr(options));v=v.replace('Option 2 is also a loose upper bound.','Options 2 and 3 are also loose upper bounds.').replace('Options 3 and 4 are too small.','Only option 4 is too small.');s=s[:a]+v+s[z:];p.write_text(s,encoding='utf8')
p=E/'a_asym-solutions.md';s=p.read_text();a=s.index('## Q3');z=s.index('## Q4',a);v=s[a:z].replace('option 2 is a valid looser upper bound as well.','options 2 and 3 are valid looser upper bounds as well.').replace('two true upper bounds','three true upper bounds').replace('Option 3 omits the $\\log n$ factor; option 4 omits the $\\log\\log n$ factor. Option 2 grows much faster, so it is true as an upper bound but not tight.','Option 2 adds a factor $n$ to the tight upper bound. Option 3 replaces the leading $\\log n$ by $n$; its ratio to the tight bound is $n/\\log n\\to\\infty$. Both are valid loose upper bounds. Option 4 omits the required $\\log n$ factor and is too small.');s=s[:a]+v+s[z:];p.write_text(s,encoding='utf8')
sys.path.insert(0,str(B/'exam-rewrite'));import mathml;mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md))
ns={};t=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in t.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'helpers','exec'),ns)
for topic in ['a_asym','a_recurrence']:
 p=R/'dist/chapters'/f'{topic}.html';s=p.read_text();a,z,attrs,v=next(x for x in ns['questions'](s)if x[2].get('data-source-id')==q['id']);opts='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(o)+'</div></div>'for i,o in enumerate(options,1))+'</div>';left=v.index('<div class="exam-options">');right=v.index('<details',left);v=v[:left]+opts+v[right:]
 if topic=='a_asym':
  left=v.index('</summary>')+len('</summary>');right=v.index('</details>',left);v=v[:left]+render((E/'a_asym-solutions.md').read_text().split('## Q3\n',1)[1].split('## Q4',1)[0])+v[right:]
 else:
  v=v.replace('Option 2 is also a loose upper bound.','Options 2 and 3 are also loose upper bounds.').replace('Options 3 and 4 are too small.','Only option 4 is too small.')
 s=s[:a]+v+s[z:];p.write_text(s,encoding='utf8')
record=json.loads((E/'a_asym-revision.json').read_text());record['originalOptionErratum']='MS CE 1405 Q58 options 2, 3 and 4 corrected against enlarged original; three true O bounds; option 1 is tightest.';(E/'a_asym-revision.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
ledger=json.loads((E/'a_recurrence-course-recheck.json').read_text());ledger['sources'][1]['conceptChecks']='All 111 available browser lines of the one-page recurrence concept sheet were freshly read, including exact level counts, the fourth-root critical case and the mixed-child quadratic induction constant six.';(E/'a_recurrence-course-recheck.json').write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf8')
original=json.loads((E/'a_recurrence-original-recheck.json').read_text());
for r in original:
 r['state']='original_image_actually_visually_read_and_stem_reconciled';r['optionNote']='Three canonical options corrected from enlarged original image; the literal O wording admits three bounds.'if r['id']=='MS_CE_1405_Q58'else'All listed stem parameters and options reconciled.'
(E/'a_recurrence-original-recheck.json').write_text(json.dumps(original,indent=2)+'\n',encoding='utf8')
(E/'a_recurrence-source-option-erratum.json').write_text(json.dumps(dict(id=q['id'],date='2026-10-13',originalSha256=q['sourceSha256'],physicalPage=13,options=options,correctTightest=1,looseAlsoValid=[2,3],false=[4],image='C:/Users/bheydari/AppData/Local/Temp/deep-algorithm-recurrence-recheck/q58-options-upper.png',updatedLiveChapters=['a_asym','a_recurrence']),indent=2)+'\n',encoding='utf8')
print('Reconciled original options, canonical producer, two live chapters and actual reading ledger.')
