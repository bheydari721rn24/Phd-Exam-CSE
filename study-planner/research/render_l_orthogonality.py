"""Rebuild only this draft and its library entry."""
from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
s=(B/'render_l_linear_impl.py').read_text(encoding='utf-8').replace('l_linear','l_orthogonality').replace('lt-','og-').replace('data-lt','data-og')
s=s.replace('Linear Transformations, Coordinate Representations, and Changes of Basis','Orthogonality and Orthogonal Decompositions')
s=s.replace('Linear transformations chapter','Orthogonality chapter').replace('Authentic examinations: explicit linear-map revisits','Authentic examinations: explicit orthogonality revisits')
a=s.index('lab=');b=s.index('\nsource=',a)
lab='<section class="lab"><form id="og-form"><label>Generator columns<input name="matrix" value="1,1;0,1;1,0"></label><label>Target vector<input name="vector" value="1,2,-1"></label><label>Positive diagonal weights<input name="weights" value="1,1,1"></label><button type="submit">Compute the exact projection and certificates</button></form><p id="og-error" role="alert"></p><p>Use two through four rows and one through four generator columns. Separate matrix rows with semicolons and entries with commas. Target entries are integers from minus ten through ten. Provide one positive integer weight from one through ten for each row; all ones give Euclidean geometry. Dependent and zero generators are accepted by retaining an independent column basis. Invalid input preserves the previous valid result. Every walkthrough starts paused.</p><div id="og-output"></div></section>'
s=s[:a]+'lab='+repr(lab)+s[b:]
s=s.replace('<!-- LAB: linear -->','<!-- LAB: orthogonality -->')
s=s.replace("s=s.replace(r'\\bigl'", "s=s.replace(r'\\rm new',r'\\text{new}').replace(r'\\arccos',r'\\operatorname{arccos}');s=s.replace(r'\\bigl'")
s=s.replace('def text(s):', "def text(s):\n s=re.sub(r'\\\\\\|(.+?)\\\\\\|',lambda m:r'{\\Vert '+m[1]+r'\\Vert}',s)")
a=s.index('anchors=');b=s.index(';it=iter(anchors)',a)
anchors=['sources','inner-product','gram-matrices','cauchy-schwarz','norms','orthogonal-sets','complements','four-subspaces','line-projection','closest-point','projectors','basis-formula','plane','bessel','gram-schmidt','three-columns','qr','least-squares','weighted','coordinates','functions','fourier','reflection','products','implementation','summary','problems','review','laboratory','references']
s=s[:a]+'anchors='+repr(anchors)+s[b:]
(B/'render_l_orthogonality_impl.py').write_text(s,encoding='utf-8')
css=(R/'dist/chapters/l_linear.css').read_text(encoding='utf-8').replace('lt-','og-').replace('#lt','#og')
(R/'dist/chapters/l_orthogonality.css').write_text(css,encoding='utf-8')
exec(compile(s,str(B/'render_l_orthogonality_impl.py'),'exec'))
