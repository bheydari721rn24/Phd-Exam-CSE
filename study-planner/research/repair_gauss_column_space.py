"""Targeted mathematical erratum, not completion of the individual chapter review."""
from pathlib import Path
from markdown_it import MarkdownIt
from html import escape
import hashlib,json,re,sys
import sympy as S
from teaching_prose_spacing import fix
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'deep-library-revision'
path=B/'l_gauss-questions.json';qs=json.loads(path.read_text(encoding='utf8'));q=next(q for q in qs if q['id']=='LG56');old=q['solution']
answer=r'''**1. Solve the stated two-row example without asserting a false difference.** Subtract twice row one from row two to obtain $R=\begin{bmatrix}1&2&3\\0&0&1\end{bmatrix}$. Pivot indices are one and three. The corresponding original columns $(1,2)^T$ and $(3,7)^T$ have determinant $7-6=1$, so they form a basis of the original column space. Both this space and the reduced column space are the whole of $\mathbb R^2$. Therefore the reduced columns also happen to form a basis of the same space in this particular full-row-rank example. It would be false to claim that these two spaces differ here.

**2. Exhibit a case where the distinction is real.** Add a dependent third row and use $B=\begin{bmatrix}1&2&3\\2&4&7\\3&6&10\end{bmatrix}$. First subtract twice row one from row two and three times row one from row three. Then subtract the new row two from row three. The result is $S=\begin{bmatrix}1&2&3\\0&0&1\\0&0&0\end{bmatrix}$, with the same pivot indices.

**3. Identify both actual planes.** Every original column satisfies $z=x+y$, and original columns one and three are independent, so $\operatorname{col}(B)=\{(x,y,z):z=x+y\}$. The reduced columns span $\operatorname{col}(S)=\{(x,y,z):z=0\}$. These are distinct planes: $e_1=(1,0,0)^T$ lies in the second but not the first. Their intersection is the line $z=0$, $y=-x$.

**4. State exactly what transfers through elimination.** An invertible row transformation preserves every linear dependence relation among column indices, but it can move the column subspace inside its ambient space. Use reduced pivot indices to select the original columns when a basis of the original space is requested. In a full-row-rank example the two column spaces coincide because both are the whole ambient space; that special coincidence does not invalidate the general warning.'''
q['solution']=answer
for item in qs:
 if item['id']=='LG05':item['title']='Three equations reduced through rational pivots'
 if item['id']=='LG14':item['title']='A repeated singular factor with incompatible loads'
path.write_text(json.dumps(qs,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
gen=B/'author_gauss_problems.py';source=gen.read_text(encoding='utf8').replace('Three equations with a unit pivot after swapping','Three equations reduced through rational pivots').replace('Two exceptional parameters with different right sides','A repeated singular factor with incompatible loads')
a=source.index("add('Original pivot columns versus reduced pivot columns'");z=source.index('\nadd(',a)
source=source[:a]+"add('Original pivot columns versus reduced pivot columns',"+repr(q['stem'])+','+repr(answer)+')'+source[z:]
gen.write_text(source,encoding='utf8')
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
page=(R/'dist/chapters/l_gauss.html').read_text(encoding='utf8');start=page.index('<section class="exam-question"',page.index('data-source-id="LG55"'))
assert 'data-source-id="LG56"'in page[start:start+200]
depth=1;opening=page.index('>',start)+1
for token in re.finditer(r'<section\b[^>]*>|</section>',page[opening:]):
 depth+=-1 if token[0]=='</section>'else 1
 if depth==0:end=opening+token.end();break
old_section=page[start:end];prefix=old_section[:old_section.index('<details')]
def point(x,y,z):return 165+50*x-40*y,180+22*x+15*y-40*z
def polygon(zfunc):return' '.join(','.join(map(str,point(x,y,zfunc(x,y))))for x,y in[(-1,-1),(1,-1),(1,1),(-1,1)])
figure='<figure class="gauss-column-erratum"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" role="img" aria-label="Two distinct column-space planes intersect in a line"><polygon points="'+polygon(lambda x,y:0)+'" fill="#8fc3c2" fill-opacity=".55" stroke="#17636a" stroke-width="2"/><polygon points="'+polygon(lambda x,y:x+y)+'" fill="#e0b58a" fill-opacity=".55" stroke="#9d6438" stroke-width="2"/>'
p1=point(-1,1,0);p2=point(1,-1,0);figure+='<path d="M'+str(p1[0])+' '+str(p1[1])+'L'+str(p2[0])+' '+str(p2[1])+'" stroke="#233d59" stroke-width="3"/>'
for y,t in[(55,'Actual three-coordinate comparison'),(100,'Original plane: z = x + y'),(145,'Reduced plane: z = 0'),(190,'Intersection: z = 0, y = −x'),(235,'e₁ belongs only to the reduced plane')]:figure+='<text x="325" y="'+str(y)+'" style="font:17px '+('&quot;STIX Two Math&quot;,serif'if y!=55 else'&quot;Source Sans 3&quot;,sans-serif')+';fill:#264653">'+escape(t)+'</text>'
figure+='</svg><figcaption>Two-dimensional drawing of the exact planes in the added three-row example. The viewing map is oblique and does not represent Euclidean angles. The original two-row question has both column spaces equal to the whole two-dimensional ambient space.</figcaption></figure>'
new=prefix+'<details class="exam-solution"><summary>Read the corrected derivation and the distinct-plane counterexample</summary>'+mathml.markdown_math(answer,md)+figure+'</details></section>'
page=page[:start]+new+page[end:]
page=page.replace('Three equations with a unit pivot after swapping','Three equations reduced through rational pivots').replace('Two exceptional parameters with different right sides','A repeated singular factor with incompatible loads')
page=page.replace('</head>','<style>.gauss-column-erratum{border:1px solid #bed6d0;border-radius:10px;padding:1rem;overflow-x:auto}.gauss-column-erratum svg{width:100%;min-width:700px;max-height:330px;height:auto;display:block}.gauss-column-erratum figcaption{font-size:.9rem}@media print{.gauss-column-erratum svg{min-width:0}}</style></head>',1)
(R/'dist/chapters/l_gauss.html').write_text(fix(page),encoding='utf8')
A=S.Matrix([[1,2,3],[2,4,7]]);RR=S.Matrix([[1,2,3],[0,0,1]]);BB=S.Matrix([[1,2,3],[2,4,7],[3,6,10]]);SS=S.Matrix([[1,2,3],[0,0,1],[0,0,0]])
checks={'old_spaces_are_both_R2':A.rank()==RR.rank()==2,'new_pivot_indices':BB.rref()[1]==SS.rref()[1]==(0,2),'original_plane':S.Matrix([[-1,-1,1]])*BB==S.zeros(1,3),'reduced_plane':S.Matrix([[0,0,1]])*SS==S.zeros(1,3),'distinct_spaces':BB.row_join(S.Matrix([1,0,0])).rank()==3 and SS.row_join(S.Matrix([1,0,0])).rank()==2}
assert all(checks.values())
(E/'l_gauss-targeted-errata.json').write_text(json.dumps({'state':'targeted_erratum_individual_review_in_progress','date':'2026-10-17','baseline':'f4195fd9c5a874cf3f032b4724f293a94168e5f1','changes':['LG56: original full-row-rank example does not demonstrate unequal column spaces; corrected and added an actual distinct-plane example','LG05: title no longer claims a swap absent from the displayed trace','LG14: title no longer claims two exceptional values when there is only lambda=1'],'exactChecks':checks,'individualChapterReviewComplete':False,'studentApproved':False,'pageSha256':hashlib.sha256((R/'dist/chapters/l_gauss.html').read_bytes()).hexdigest()},indent=2)+'\n',encoding='utf8')
print(checks)
