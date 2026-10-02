from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'research/g_gates.en.md';s=p.read_text(encoding='utf-8')
old='<circle cx="395" cy="215" r="5"/>';assert old in s;s=s.replace(old,'').replace('M400 215H420','M390 215H420');p.write_text(s,encoding='utf-8')
p=ROOT/'research/s_counting.en.md';s=p.read_text(encoding='utf-8')
s=s.replace('The six unordered multisets are <span class="math-inline">{1,1},{2,2},{3,3},{1,2},{1,3},{2,3}</span>.','We write multisets with doubled brackets to retain multiplicity: ⟦1,1⟧ has two copies of 1, whereas the ordinary set {1,1} equals {1}. The six unordered multisets are <span class="math-inline">⟦1,1⟧,⟦2,2⟧,⟦3,3⟧,⟦1,2⟧,⟦1,3⟧,⟦2,3⟧</span>.')
s=s.replace('{1,1}: mass 1/9','⟦1,1⟧: mass 1/9').replace('{1,2}: mass 2/9','⟦1,2⟧: mass 2/9')
s=s.replace('Ordered uniform draws → unordered report','Ordered uniform draws → multiset report')
s=s.replace('Forgetting order changes the mass of a report according to the number of detailed outcomes it combines.', 'The doubled brackets denote multisets, so repeated labels remain repeated. Forgetting order changes the mass of a report according to the number of detailed outcomes it combines.')
p.write_text(s,encoding='utf-8')
for name in ('build_induction_chapter.py','build_model_chapter.py','build_asym_chapter.py','build_loop_chapter.py'):
 p=ROOT/'research'/name;s=p.read_text(encoding='utf-8').replace('Review draft ·','Student-approved chapter ·');p.write_text(s,encoding='utf-8')
