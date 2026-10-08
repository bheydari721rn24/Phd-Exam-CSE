from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
s=(B/'render_l_det_impl.py').read_text(encoding='utf-8').replace('l_det','l_spaces').replace('det-','vs-').replace('data-det','data-vs').replace('#det','#vs').replace('Determinants, Orientation, and Structured Computation','Vector Spaces, Subspaces, Bases, and Dimension').replace('Determinants chapter audit','Vector spaces chapter audit').replace('Expectation chapter','Vector spaces chapter').replace('Authentic examinations: positivity and a triangular polynomial map','Authentic examinations: structured dimension and basis-defined projection')
s=s.replace("mathml.SYMBOLS.update(Phi=", "mathml.SYMBOLS.update(star='⋆',odot='⊙',varnothing='∅',subsetneq='⊊',setminus='∖');mathml.SYMBOLS.update(Phi=")
s=s.replace("'<h3>Question '+str(n)","'<h3>'+('Authentic Question 'if auth else'Question ')+str(n)")
a=s.index('lab=');b=s.index('\nsource=',a)
lab='''<section class="lab"><form id="vs-form"><label>Generator matrix<input name="matrix" value="1,2,0,3;2,4,1,4;3,6,2,5"></label><label>Target vector<input name="target" value="1,3,5"></label><button type="submit">Compute bases, dependencies and membership</button></form><p id="vs-error" role="alert"></p><p>Enter generators as columns: separate columns with commas and rows with semicolons. Use 2–4 rows, 1–5 columns and integer entries from −20 to 20. The target has one entry per row. Exact rational arithmetic handles every row operation, including fractions. The original generators are retained; an independently tracked row operator checks every intermediate matrix. Invalid input preserves the previous result. Every walkthrough starts paused.</p><div id="vs-output"></div></section>'''
s=s[:a]+'lab='+repr(lab)+s[b:];s=s.replace('<!-- LAB: determinant -->','<!-- LAB: spaces -->')
a=s.index('anchors=');b=s.index(';it=iter(anchors)',a)
anchors=['sources','axioms','consequences','subspace','constraints','span','independence','basis','exchange','dimension','computation','functions','interpolation','matrix-spaces','sum-intersection','dimension-formula','direct-sums','complements','coordinate-change','quotients','fields','parameters','infinite-boundaries','workflow','summary','problems','review','laboratory','references']
s=s[:a]+'anchors='+repr(anchors)+s[b:]
(B/'render_l_spaces_impl.py').write_text(s,encoding='utf-8')
css=(R/'dist/chapters/l_det.css').read_text(encoding='utf-8').replace('det-','vs-').replace('#det','#vs')
css+='\n#vs-form {display:grid;grid-template-columns:1fr;gap:1rem} #vs-form input {width:100%;max-width:100%;font-family:"JetBrains Mono",monospace} .vs-model svg{display:block;width:100%;height:auto} .lab-results{padding:1rem;border:1px solid #b0c4c5;border-radius:12px} a,a:hover,a:focus{text-decoration:none!important}\n'
(R/'dist/chapters/l_spaces.css').write_text(css,encoding='utf-8')
exec(compile(s,'render_l_spaces_impl.py','exec'))
