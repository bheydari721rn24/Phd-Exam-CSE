"""Add native MathML for central product and factorial-valuation limits."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1];p=root/'research/d_number.en.md'
s=p.read_text(encoding='utf-8').replace('Every nonzero pair has integer coefficients','Every pair that is not both zero has integer coefficients')
product='<div class="formula-block"><math display="block" aria-label="phi of n equals n times the product over distinct primes dividing n of one minus one over p"><mrow><mi>φ</mi><mo>(</mo><mi>n</mi><mo>)</mo><mo>=</mo><mi>n</mi><munder><mo>∏</mo><mrow><mi>p</mi><mo>∣</mo><mi>n</mi></mrow></munder><mo>(</mo><mn>1</mn><mo>−</mo><mfrac><mn>1</mn><mi>p</mi></mfrac><mo>)</mo></mrow></math></div>'
s=s.replace('$φ(n)=n∏_{p∣n}(1−1/p)$.',product)
legendre='<div class="formula-block"><math display="block" aria-label="the p valuation of N factorial equals the sum over j from one through infinity of floor N over p to the j"><mrow><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>N</mi><mo>!</mo><mo>)</mo><mo>=</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mo>∞</mo></munderover><mo>⌊</mo><mfrac><mi>N</mi><msup><mi>p</mi><mi>j</mi></msup></mfrac><mo>⌋</mo></mrow></math></div>'
needle='### Squares, Wilson\'s theorem, and primality evidence'
if legendre not in s:s=s.replace(needle,legendre+'\n\n'+needle)
p.write_text(s,encoding='utf-8')
p=root/'research/d_number-source-downloads.json';rows=json.loads(p.read_text())
old=json.loads((root/'research/d_invariants-source-downloads.json').read_text())
mit=next(r for r in old if r['id']=='mit')
if not any(r['id']=='mit' for r in rows):rows.append(mit);p.write_text(json.dumps(rows,indent=2)+'\n')
print('Central product and summation limits use native MathML; MIT reference fingerprint retained.')
