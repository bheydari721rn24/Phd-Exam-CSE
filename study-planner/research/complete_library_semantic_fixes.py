"""Apply the final findings from the full sixteen-chapter semantic reading."""
from pathlib import Path

def replace(file, old, new):
    p=Path('research')/file
    s=p.read_text(encoding='utf-8')
    if new in s:
        return
    assert s.count(old)==1, (file,old)
    p.write_text(s.replace(old,new),encoding='utf-8')

replace('g_number.en.md','If M distinct states must have distinct fixed-length codes,',
        'If M is a positive integer and M distinct states must have distinct fixed-length codes,')
replace('g_number.en.md','If q and b have the same prime factors,',
        'If every prime factor of q occurs in b,')
replace('g_number.en.md','For an n-bit word, let U be its ordinary unsigned value and let s be its most significant bit.',
        'For an n-bit word with integer n ≥ 1, let U be its ordinary unsigned value and let s be its most significant bit.')
replace('g_number.en.md',
 'The resulting eight-bit extended code has minimum distance four and supports single-error correction plus double-error detection, abbreviated SECDED.',
 'The resulting eight-bit extended code has minimum distance four and supports single-error correction plus double-error detection, abbreviated SECDED. To prove the distance, take two distinct seven-bit codewords whose distance is w. The preceding argument establishes w ≥ 3. Their appended parity bits differ exactly when w is odd, because parity of the XOR equals XOR of the two parities. Their extended distance is therefore w + (w mod 2): an odd distance increases by one and an even distance stays unchanged. Both cases give a distance at least four. The valid three-position difference at positions one, two, and three attains four after extension, so the minimum is exactly four.')
replace('g_number-review.en.md','Positive truncation error is below one grid step,',
        'For a nonnegative target, truncation has absolute error below one grid step,')
replace('g_gates.en.md','from a unfamiliar outline','from an unfamiliar outline')
replace('g_gates-problems.en.md',
 'The dual POS is f = (x + y)(x + z)(x + w)(y + z)(y + w)(z + w).',
 'An equivalent POS is f = (x + y)(x + z)(x + w)(y + z)(y + w)(z + w). This is not obtained by merely taking the dual of the three-literal SOP: that dual would be one whenever at least two inputs are one and would implement a different function.')
replace('l_matrices.en.md',
 'The previous vector chapter shows that n independent vectors in ℝ<sup>n</sup> form a basis, so Q is onto.',
 '''To see directly why n independent vectors in ℝ<sup>n</sup> form a basis, start with its n standard coordinate vectors as a spanning list. Insert the independent columns one at a time. Express the next column using the current list, which consists of previously inserted columns and unreplaced coordinate vectors. At least one unreplaced coordinate vector must have a nonzero coefficient; otherwise the next column would be a combination of the earlier columns, contradicting independence. Solve that relation for one such coordinate vector and replace it by the new column. The list still spans, retains n vectors, and contains one more column. After n replacements all columns form a spanning list. This exchange argument supplies the needed finite-dimensional fact without assuming that an independent family automatically spans in arbitrary dimensions. Consequently Q is onto.''')
print('Final semantic findings applied.')
