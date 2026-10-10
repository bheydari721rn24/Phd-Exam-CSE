"""Prepare the chapter-specific renderer; this helper edits only balanced-tree artifacts."""
from pathlib import Path
B=Path(__file__).resolve().parent; R=B.parent
p=R/'dist/chapters/a_balanced.js';s=p.read_text(encoding='utf-8')
s=s.replace("txt(601,330,'B = left - right')","txt(601,330,'B = left - right','bl-meta')")
s=s.replace('Temporary states may intentionally violate the completed invariant.','Temporary states may intentionally violate the completed invariant. A displayed b=-1 flags unequal black routes; it is not a valid black height.')
p.write_text(s,encoding='utf-8')
p=B/'a_balanced.en.md';s=p.read_text(encoding='utf-8')
if '<!-- SIM: classical -->'not in s:s=s.replace('## 17.','<!-- SIM: classical -->\n\n## 17.',1)
p.write_text(s,encoding='utf-8')
s=(B/'render_a_bst.py').read_text(encoding='utf-8').replace('a_bst','a_balanced').replace('bt-','bl-').replace('LAB: bst','LAB: balanced')
s=s.replace("psi='ψ'","psi='ψ',phi='φ'")
a=s.index("lab='");z=s.index("\nsource=",a)
s=s[:a]+'''lab='<section class="lab"><form id="bl-form"><label>Operation<select name="operation"><option>avl-insert</option><option>avl-delete</option><option>llrb-insert</option><option>llrb-delete</option><option>multiway</option></select></label><label>Insertion keys<input name="keys" value="30,10,20"></label><label>Deletion keys<input name="remove" value="10"></label><button type="submit">Build the exact balanced-tree trace</button></form><p id="bl-error" role="alert"></p><p>Supply one through twelve distinct comma-separated integer insertion keys between minus 999 and 999. Deletion accepts one through twelve integer target keys; absent targets preserve the tree. Insertions construct the initial AVL or completed 2–3 LLRB tree before deletions begin. Multiway builds a top-down 2–3–4 tree. Every trace starts paused. Invalid input preserves the previous valid trace.</p><div id="bl-output"></div></section>'
'''+s[z:]
a=s.index("body=text(source);anchors=");z=s.index(';it=iter(anchors)',a)
s=s[:a]+"body=text(source);anchors="+repr(['sources','contracts','height','minimum','counting','rotations','insertion','insertion-proof','deletion','deletion-proof','implementation','augmentation','multiway','multiway-repair','red-black','black-height','classical-insertion','classical-deletion','llrb-insertion','llrb-deletion','exam-reasoning','summary','problems','review','laboratory','references'])+s[z:]
s=s.replace('Binary Search Trees: Correctness, Ordered Queries, and Exact Costs','Balanced Search Trees: Exact Heights, Repair Proofs, and Ordered Updates').replace('Binary search tree chapter','Balanced search tree chapter').replace('Binary search tree chapter audit','Balanced search tree chapter audit')
s=s.replace('27 exact tree models','26 exact balanced-tree models').replace('animationCount=27,animationWalkthroughCount=27','animationCount=26,animationWalkthroughCount=26').replace('27 exact tree models.','26 exact balanced-tree models.')
s=s.replace('Render only the new arithmetic review draft','Render only the new balanced-tree review draft')
(B/'render_a_balanced.py').write_text(s,encoding='utf-8')
