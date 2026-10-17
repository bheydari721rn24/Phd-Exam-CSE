"""Replace unrelated example aliases with eleven actual-input question scenes."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/l_gauss.html';s=p.read_text(encoding='utf8');removed=0
while m:=re.search(r'<div class="question-concept-aid">',s):
 depth=1
 for t in re.finditer(r'<div\b[^>]*>|</div>',s[m.end():]):
  depth+=-1 if t[0]=='</div>'else 1
  if depth==0:end=m.end()+t.end();break
 else:raise ValueError('Unclosed question aid')
 s=s[:m.start()]+s[end:];removed+=1
mapping={'LG01':'gauss-swap','LG02':'gauss-skip','LG03':'gauss-affine','LG04':'gauss-inconsistent','LG13':'gauss-parameters','LG30':'gauss-coordinate','LG31':'gauss-inverse','LG34':'gauss-lu','LG36':'gauss-plu','LG45':'gauss-rounding','LG49':'gauss-binary'}
for id,scene in mapping.items():
 a=s.index('data-source-id="'+id+'"');z=s.index('</details>',a)
 note='This walkthrough uses the actual matrix or equations in this problem. Its checkpoints expose the stated row operations, coordinate map or declared arithmetic model.'
 if id=='LG13':note='The finite checkpoints use selected values of this problem\'s own alpha parameter. The written symbolic proof supplies all real branches; the animation does not replace that proof.'
 aid='<div class="question-concept-aid"><h4>Walk through this problem\'s actual model</h4><p>'+note+'</p><div class="concept-animation" data-scenes="'+scene+'"></div></div>'
 s=s[:z]+aid+s[z:]
p.write_text(s,encoding='utf8')
out=R/'research/deep-library-revision/l_gauss-targeted-errata.json';d=json.loads(out.read_text(encoding='utf8'));d.update(unrelatedQuestionAliasesRemoved=removed,matchedQuestionScenes=mapping,visualScope='Targeted replacement of unrelated aliases. Existing problem-specific aids remain; the entire chapter individual review is still in progress.');out.write_text(json.dumps(d,indent=2)+'\n',encoding='utf8')
print({'removed':removed,'matched':len(mapping)})
