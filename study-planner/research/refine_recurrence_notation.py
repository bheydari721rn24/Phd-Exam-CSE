"""Replace letter sigma by the summation operator in mathematical prose."""
from pathlib import Path
root=Path(__file__).resolve().parent
for name in ('a_recurrence.en.md','a_recurrence-problems.en.md','a_recurrence-review.en.md'):
 p=root/name
 p.write_text(p.read_text(encoding='utf-8').replace('Σ','∑'),encoding='utf-8')
