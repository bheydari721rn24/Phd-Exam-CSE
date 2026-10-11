"""Isolated renderer; earlier delivered pages are never rebuilt."""
from pathlib import Path
import re
B=Path(__file__).resolve().parent;R=B.parent
s=(B/'render_l_spaces_impl.py').read_text(encoding='utf-8')
s=s.replace('l_spaces','l_linear').replace('vs-','lt-').replace('data-vs','data-lt').replace('#vs','#lt')
s=s.replace("mathml.SYMBOLS.update(star=", "mathml.SYMBOLS.update(dagger='†');mathml.SYMBOLS.update(star=")
s=s.replace('Vector Spaces, Subspaces, Bases, and Dimension','Linear Transformations, Coordinate Representations, and Changes of Basis')
s=s.replace('Vector spaces chapter','Linear transformations chapter').replace('Vector spaces chapter audit','Linear transformations chapter audit')
s=s.replace('Authentic examinations: structured dimension and basis-defined projection','Authentic examinations: explicit linear-map revisits')
s=s.replace('==82','==84').replace('==80','==84').replace('82 worked problems','84 worked problems').replace('80 examination rules','84 examination rules')
s=s.replace('questionCount=82','questionCount=84').replace('originalQuestionCount=80','originalQuestionCount=82').replace('examNotesCount=80','examNotesCount=84')
s=s.replace("w['week']==3","w['week']==4").replace('Week 3','Week 4').replace('#week-3','#week-4')
a=s.index('lab=');b=s.index('\nsource=',a)
lab='<section class="lab"><form id="lt-form"><label>Standard operator A<input name="matrix" value="1,2;0,1"></label><label>Input synthesis P<input name="inputBasis" value="1,0;1,1"></label><label>Output synthesis Q<input name="outputBasis" value="1,1;0,1"></label><label>Input coefficients<input name="vector" value="2,-1"></label><button type="submit">Check both coordinate paths</button></form><p id="lt-error" role="alert"></p><p>Use two-by-two integer matrices, rows separated by semicolons, entries separated by commas, and values from minus ten through ten. Both basis matrices must be invertible. All computations use exact rational arithmetic. Invalid input preserves the preceding valid result.</p><div id="lt-output"></div></section>'
s=s[:a]+'lab='+repr(lab)+s[b:]
s=s.replace('<!-- LAB: spaces -->','<!-- LAB: linear -->')
a=s.index('anchors=');b=s.index(';it=iter(anchors)',a)
anchors=['sources','linearity','affine','basis-images','prescriptions','fibers','rank-nullity','representations','two-bases','transitions','composition','inverses','similarity','passive','geometry','projections','polynomials','compression','matrix-spaces','sylvester','product-rank','dual','powers','infinite','workflow','summary','problems','review','laboratory','references']
s=s[:a]+'anchors='+repr(anchors)+s[b:]
s=s.replace('==82','==84').replace('==80','==84')
s=s.replace('Rendered only l_linear: 82 questions, 80 rules','Rendered only l_linear: 84 questions, 84 rules')
# Review pages refer to shared files through their own directory.
s=s.replace('href="advanced-simulations.css?player-behavior-2"','href="../chapters/advanced-simulations.css?player-behavior-2"',1) if False else s
(B/'render_l_linear_impl.py').write_text(s,encoding='utf-8')
css=(R/'dist/chapters/s_distributions.css').read_text(encoding='utf-8').replace('sd-','lt-').replace('#sd','#lt')
css+='\n.lt-model{max-width:100%}.lt-stage{max-width:760px;margin-inline:auto}.lt-stage svg{display:block;width:100%;height:auto;min-width:760px}.lt-stage svg text,.lt-print svg text{font-size:16px;font-family:"Source Sans 3",sans-serif!important}.lt-stage svg .lt-math,.lt-print svg .lt-math{font-family:"STIX Two Math",serif!important}#lt-form{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:1rem}#lt-form label{display:grid;gap:.5rem}#lt-form input{font-family:"JetBrains Mono",monospace;width:100%}.lt-model svg{overflow:visible}.lt-stage{overflow:auto}@media print{.lt-print svg{min-width:0}}\n'
(R/'dist/chapters/l_linear.css').write_text(css,encoding='utf-8')
exec(compile(s,str(B/'render_l_linear_impl.py'),'exec'))
for label in ['sources','quality']:
 p=R/f'dist/reviews/l_linear-{label}.html'
 if p.exists():p.write_text(p.read_text(encoding='utf-8').replace('href="advanced-simulations.css','href="../chapters/advanced-simulations.css'),encoding='utf-8')
