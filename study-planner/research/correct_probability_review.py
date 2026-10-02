from pathlib import Path

def change(path,old,new):
 p=Path(path);s=p.read_text(encoding='utf-8')
 if new in s: return
 assert old in s,(path,old);p.write_text(s.replace(old,new),encoding='utf-8')

change('research/s_axioms.en.md',
 'The limsup is the entire interval.',
 'The limsup is [0,1), an event of probability one; if the ambient space is [0,1], the endpoint 1 is still excluded. This is almost-sure occurrence, not equality with the entire closed sample space.')
change('research/s_counting.en.md','encoded by <span class="math-inline">**||*|**</span>.','encoded by <code>**||*|**</code>.')
change('research/a_loop.en.md',
 'Since <span class="math-inline">2<sup>m</sup>≤n&lt;2<sup>m+1</sup></span>, the count is greater than or equal to <span class="math-inline">n</span>? When <span class="math-inline">n=6</span>, it is seven, but when <span class="math-inline">n=7</span>, it is seven. Indeed',
 'Since <span class="math-inline">2<sup>m</sup>≤n&lt;2<sup>m+1</sup></span> and <span class="math-inline">n</span> is integral,')
for name in ['a_loop','a_asym']:
 change(f'research/{name}.en.md','English review draft','Approved English chapter')
print('Corrected endpoint, stars-and-bars representation, geometric-sum prose and approval labels.')
