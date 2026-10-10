from pathlib import Path
import re
B=Path(__file__).resolve().parent;R=B.parent
s=(B/'render_a_balanced.py').read_text().replace('a_balanced','a_heap').replace('bl-','hp-').replace('#bl','#hp').replace('data-bl','data-hp')
s=s.replace('balanced-tree','heap').replace('Balanced search tree','Heap and priority queue').replace('Balanced Search Trees: Exact Heights, Repair Proofs, and Ordered Updates','Heaps and Priority Queues: Exact Structure, Repair Proofs, and Amortized Design')
start=s.index("lab='<section");stop=s.index('\n\nsource=',start)
lab='''<section class="lab"><form id="hp-form"><label>Operation<select name="operation"><option>build</option><option>insert</option><option>extract</option><option>change</option><option>delete</option><option>sort</option><option>multiway</option><option>topk</option><option>frontier</option><option>binomial</option><option>fibonacci</option></select></label><label>Orientation<select name="orientation"><option>min</option><option>max</option></select></label><label>Input keys<input name="keys" value="9,4,7,1,0,3,2"></label><label>Arity<select name="arity"><option>2</option><option>3</option><option>4</option></select></label><label>New key<input name="value" value="1"></label><label>Target zero-based position<input name="index" value="0"></label><label>Rank or retained count<input name="k" value="3"></label><button type="submit">Build the exact heap trace</button></form><p id="hp-error" role="alert"></p><p>The compact editable laboratory accepts one through fifteen integer keys between minus 999 and 999, including duplicates; insertion accepts at most fourteen initial keys. Insert, extraction, key change, deletion and frontier selection require an already heap-ordered input. Build repairs arbitrary input. Sort uses a max heap for ascending output. Top-k uses a retained min heap. Binomial insertion uses canonical equal-rank carries. Fibonacci replays the stated four-record first-loss/second-loss case; its controls do not promise an arbitrary Fibonacci implementation. Stable E identifiers refer to original input positions, so E0, E1 and E2 correspond to A, B and C in the tie example. Every trace starts paused; invalid input preserves the previous valid trace.</p><div id="hp-output"></div></section>'''
s=s[:start]+'lab='+repr(lab)+s[stop:]
s=s.replace('<!-- LAB: balanced -->','<!-- LAB: heap -->')
s=s.replace("psi='ψ',phi='φ'","psi='ψ',phi='φ',Phi='Φ'")
start=s.index('anchors=');stop=s.index(';it=iter(anchors)',start)
s=s[:start]+"anchors=['sources','interface','shape','order','upward','downward','construction','counters','indexed','aggregate','heapsort','counting','multiway','applications','binomial','potential','fibonacci','degree-proof','alternatives','exam-reasoning','summary','problems','review','laboratory','references']"+s[stop:]
s=s.replace('26 exact balanced-tree models','21 specialized exact heap models').replace('26 exact heap models','21 specialized exact heap models')
s=s.replace('80 final rules, 26 exact heap models','80 final rules, 21 specialized heap models')
s=s.replace('animationCount=26,animationWalkthroughCount=26','animationCount=21,animationWalkthroughCount=21')
(B/'render_a_heap.py').write_text(s,encoding='utf-8')
# Scientific identity labels are visible, not merely hidden data attributes.
p=R/'dist/chapters/a_heap.js';s=p.read_text().replace('radius=19','radius=22').replace("label:'i='+i","label:e.id+' @ '+i").replace("label:'d='+t.children.length","label:t.id+' d='+t.children.length")
p.write_text(s,encoding='utf-8')
print('Prepared heap renderer and compact visible record identities.')
