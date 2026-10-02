"""Repair delimiters and replace two identified preliminary mathematical claims."""
from pathlib import Path
p=Path(__file__).resolve().parent/'a_recurrence.en.md';s=p.read_text(encoding='utf-8').replace('`','$').replace('define a independently solvable','define an independently solvable')
a=s.index('Regularity is not decorative.');b=s.index('\n\nWhen a theorem does not apply',a)
s=s[:a]+'''Regularity is not decorative. On the dyadic grid $n=2^h$, let the toll be $n^2$ for even $h$ and $n^3$ for odd $h$, in the recurrence $T(n)=2T(n/2)+f(n)$. This toll is always at least quadratic, giving a polynomial gap above the critical exponent one. For even $h$, however, the immediate child has cubic toll, so the child contribution alone is $2(n/2)^3=n^3/4$. The solution-to-root-toll ratio is therefore at least $n/4$, unbounded along those even levels. The claimed $Θ(f(n))$ conclusion fails. The regularity ratio also grows without bound there, exposing the missing condition.''' +s[b:]
s=s.replace('With a threshold at one, stopping occurs after','With the fixed base range zero through $b−1$, stopping occurs after')
s=s.replace('their numbers are $2^h−n$ and $2n−2^h$.','their numbers are $2^h−n$ and $2n−2^h$. If these counts are $u,v$, then $u+v=n$ and $2u+v=2^h$: each shallower leaf occupies two slots at depth $h$, while each deeper leaf occupies one. Solving these equations gives the stated counts.')
p.write_text(s,encoding='utf-8');assert all(line.count('$')%2==0 for line in s.splitlines())
print('Delimiter parity and the regularity/floor-depth statements corrected.')
