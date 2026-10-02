from pathlib import Path

def replace(path, old, new):
    p=Path(path); text=p.read_text(encoding='utf-8')
    assert old in text, (path, old)
    p.write_text(text.replace(old,new),encoding='utf-8')

replace('research/a_asym.en.md',
    'Equivalently, <span class="math-inline">f=g+o(g)</span> for eventually positive <span class="math-inline">g</span>.',
    'Equivalently, <span class="math-inline">|f−g|/g→0</span> for eventually positive <span class="math-inline">g</span>, or <span class="math-inline">f=g+h</span> with <span class="math-inline">|h|∈o(g)</span>. The residual <span class="math-inline">h</span> may be negative: for example, <span class="math-inline">f(n)=n−1</span> and <span class="math-inline">g(n)=n</span> satisfy <span class="math-inline">f∼g</span> although their difference is <span class="math-inline">−1</span>. This absolute-value formulation respects our nonnegative little-oh convention.')
replace('research/a_asym.en.md','This lesson remains a review draft until the student approves it.','This student-approved chapter is undergoing the requested final library review.')
replace('research/a_model.en.md',
    'Here is a small decision-tree argument. Suppose',
    'Here is a small decision-tree argument. Let <span class="math-inline">b≥2</span> and <span class="math-inline">q≥1</span> be integers. Suppose')
replace('research/a_model.en.md',
    'If each test has at most <span class="math-inline">b</span> outcomes, distinguishing',
    'For integers <span class="math-inline">b≥2</span> and <span class="math-inline">q≥1</span>, if each test has at most <span class="math-inline">b</span> outcomes, distinguishing')
replace('research/d_proof.en.md',
    'The nonnegative domain is needed both for √(xy) and for taking square roots of the comparison without a sign ambiguity.',
    'The nonnegative domain ensures that √(xy) is real and both sides of the comparison are nonnegative. Real-valued √(xy) alone would be insufficient: two negative inputs can have positive product while their arithmetic mean is negative.')
replace('research/d_induction.en.md',
    'The base index n=0 matters: the sum then has the one term r⁰=1, including at r=0 under the usual exponent convention 0⁰ in a sum is ambiguous. To avoid that ambiguity, either assume r≠0 or start at n=1 with a separately defined first term. We use r≥2 in the solved geometric example, where no convention is disputed.',
    'The base index n=0 matters: the sum then has one constant term, equal to 1. Treat G(n) as the polynomial 1+r+⋯+rⁿ; its constant term is 1 even at r=0, so G(n)=1 there. This is a stated polynomial convention, not a claim that the expression 0⁰ has a universal value in all mathematical contexts. With that convention the closed form also works at r=0. We use r≥2 in the solved geometric example.')
replace('research/d_sets.en.md','>outside A ∪ B</text>','>U ∖ (A ∪ B)</text>')
print('Corrected signed residual, decision-tree assumptions, square-root reasoning, polynomial convention, and universe label.')
