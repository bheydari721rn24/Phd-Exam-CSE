"""Update only this chapter's instruction, rules and evidence links."""
from pathlib import Path
import re,sys
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1];B=R/'research';D=R/'dist/chapters'
sys.path.insert(0,str(B/'exam-rewrite'))
import mathml
mathml.wrap_display=lambda s:s
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def text(s):return mathml.markdown_math(s,md)
p=B/'p_functions.en.md';s=p.read_text(encoding='utf8')
s=s.replace('x += 1 produces a new integer and rebinds the local name','x += 1 computes an integer value and rebinds the local name without promising a fresh allocation')
addition=(B/'deep-library-revision/p_functions-method-additions.en.md').read_text(encoding='utf8')
if '## From a language model to an examination proof'not in s:s=s.replace('## Worked mathematical, conceptual, and archive problems',addition+'\n\n## Worked mathematical, conceptual, and archive problems')
p.write_text(s,encoding='utf8')
p=B/'p_functions-review.en.md';rules=p.read_text(encoding='utf8')
rules=rules.replace('59. Mathematical representability of the final result is insufficient. Check every executed intermediate, including an unnecessary final square whose value is later discarded.','59. Mathematical representability of the final result is insufficient. With an explicitly assumed int32, 50000 raised to exponent one fits, but an unused square of 50000 is 2500000000 and overflows. Check every executed intermediate and avoid a final square that the algorithm never needs.')
rules=rules.replace('67. A specification promising “a positive common divisor” does not promise “the greatest common divisor.” The constant-one implementation refutes that inference.','67. A specification promising a positive common divisor does not promise the greatest common divisor. For inputs twelve and eighteen, returning one meets the weaker contract but misses the gcd six. A descending search proves greatestness by maintaining that every larger candidate has already failed, not merely by testing that the current candidate divides both inputs.')
rules=rules.replace('79. Loop-created Python closures can share a late-read binding; per-definition defaults can instead save each current value. Explain binding identity and evaluation time rather than saying merely “captured.”','79. Loop-created Python closures can share a late-read binding: saved functions reading i after range(3) can all return two. A definition lambda i=i: i instead saves defaults zero, one and two at the respective definitions. Its parameter can still be overridden by an explicit call argument; saving a mutable default would not create a deep copy.')
p.write_text(rules,encoding='utf8')
p=D/'p_functions.html';page=p.read_text(encoding='utf8')
if 'id="proof-method"'not in page:page=page.replace('<h2 id="problems">',text(addition).replace('<h2>','<h2 id="proof-method">',1)+'<h2 id="problems">')
page=page.replace('x += 1 produces a new integer','x += 1 computes an integer value without promising a fresh allocation')
blocks=[]
for block in rules.split('\n\n'):
    m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
    if m:blocks.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>')
assert len(blocks)==80
it=iter(blocks);page,n=re.subn(r'<section class="review-rule">[\s\S]*?</section>',lambda _:next(it),page);assert n==80
if 'Lifetime references for PF86'not in page:
    reference='<p><strong>Lifetime references for PF86.</strong> The C++ working draft <a href="https://eel.is/c++draft/basic.life">basic.life</a> distinguishes an object lifetime from a reference lifetime. <a href="https://eel.is/c++draft/class.temporary">class.temporary</a> describes temporary-binding lifetime rules; those rules do not preserve an ordinary automatic local returned by reference. These are supplementary language references, not additional university courses.</p>'
    page=page.replace('<p><strong>Audit boundary.</strong>',reference+'<p><strong>Audit boundary.</strong>')
page=page.replace('Student-approved chapter','Author-reviewed revision · awaiting student approval')
p.write_text(page,encoding='utf8')
print('Added full proof method and strengthened three of the 80 decision rules.')
