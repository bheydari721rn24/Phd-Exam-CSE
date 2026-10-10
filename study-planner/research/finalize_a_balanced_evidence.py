from pathlib import Path
import json,hashlib,shutil,re
B=Path(__file__).resolve().parent;R=B.parent;E=B/'a_balanced-evidence';cache=Path('C:/Users/bheydari/AppData/Local/Temp/a-balanced-sources')
p=R/'dist/chapters/a_balanced.js';s=p.read_text(encoding='utf-8')
s=s.replace("b+=txt(601,265,'Labels use true')+txt(601,290,'subtree heights.')+txt(601,330,'B = left - right','bl-meta');", "const colorLabels=s.operation.startsWith('llrb')||s.operation==='classical-demo'||z.kind==='encoding';b+=txt(601,265,colorLabels?'Color labels: R/B':'Labels use true')+txt(601,290,colorLabels?'b: black count.':'subtree heights.')+txt(601,330,colorLabels?'b=-1: unequal':'B = left - right','bl-meta');")
s=s.replace("{mathHtml:'Completed update checkpoint',result:String(!!z.complete)}]", "...(spec.operation.startsWith('llrb')?[{mathHtml:'Completed 2–3 LLRB validity',result:String(rb(z.tree,true))}]:[]),{mathHtml:'Completed update checkpoint',result:String(!!z.complete)}]")
p.write_text(s,encoding='utf-8')
acq=json.loads((E/'acquisition.json').read_text(encoding='utf-8'));java=cache/'princeton-java.html'
reading=dict(coreUniversities=['CMU','MIT','Princeton','Stanford'],additionalReviewedUniversity='UC Berkeley',nativeAcquisition=acq,readScopes={'CMU':'All 29 PDF pages including 11 exercises and sample answers; page 27 rendered and inspected.','MIT':'All eight PDF pages; page 3 rendered and inspected.','Princeton':'All 45 PDF pages, complete written §3.3 booksite and full linked Java listing.','Stanford':'All 58 and 66 condensed slides for Lectures 6 and 7; lecture/course pages used to establish instructor and year.','Berkeley':'All 195 official web-text lines; web reader succeeded after native TLS retrieval failed.'},additionalNativeJava=dict(url='https://algs4.cs.princeton.edu/33balanced/RedBlackBST.java.html',sha256=hashlib.sha256(java.read_bytes()).hexdigest(),bytes=java.stat().st_size),limits='Eight bounded candidate offerings evaluated; schedule/link inventories and search-index-only alternatives are distinguished from genuinely read lecture texts. No claim of exhaustive worldwide source review or wholesale exercise reproduction.')
(E/'reading.json').write_text(json.dumps(reading,indent=2)+'\n',encoding='utf-8')
for p in cache.glob('*.png'):shutil.copy2(p,E/('source-'+p.name))
audit='''# Balanced search trees: scientific and visual review

## Delivery status

This is a quality-reviewed English chapter draft, available for student review. It is not marked student-approved. Continuous sequential authoring is authorized; publication is recorded separately only after a native deployment succeeds.

## Sources and scientific scope

Four core courses from CMU, MIT, Princeton and Stanford were genuinely read, plus Berkeley as a fifth comparison. Eight accessible course candidates were screened with actual reading scope stated in the source audit. The exposition includes exact AVL thresholds, attainable-size and shape-counting proofs, insertion/deletion height propagation, complete independently written AVL update code, augmentation, multiway occupancy/repair, precise general red-black conventions, classical repair cases and the distinct completed 2–3 LLRB algorithm.

Source discrepancies are reconciled rather than copied: empty-height shifts, MIT's Fibonacci index, CMU's insufficient generic rotation contract, the deletion equality case, Stanford's discrete degree minimization and classical versus LLRB rotation counts. Source hashes, page counts and reading scope are in the reading ledger.

## Questions and final rules

The chapter contains 80 original or independently reconstructed course-pattern problems and two authenticated Iranian examination questions, with complete reasoning. Both original PDF pages were rendered and read; archive hashes and repository source commit accompany each adaptation. Correct options are independently derived, not attributed to an official key. The final 80 rules state assumptions, formulas, exception cases and practical exam traps in full sentences. Some boundary-recognition problems are introductory diagnostics; the bank also includes exact extremal/counting, cascade, augmentation, multiway and color-resource problems. Full copyrighted course banks are not reproduced.

## Independent mathematics and model checks

An immutable AVL reference computes true heights without the production cache and independently checks exact outputs and primitive counts. The audit covers all five-key insertion permutations with corresponding deletion orders, plus fifty distinct twelve-key AVL and LLRB deletion sequences: 340 input specifications and 13,142 generated checkpoints. Every completed stored tree checkpoint is independently certified for inherited order, actual size/height agreement and the named AVL/general-red-black/LLRB invariant. Multiway checkpoints are checked for strict intervals, key capacity, child count and uniform leaf depth. The general-red-black midpoint construction is separately certified for every size from one through 1,024. All 80 question audit entries distinguish computed checks from manual proof reviews; finite success is not misrepresented as a universal proof.

## Specialized visual teaching

There are 26 exact models and 294 saved checkpoints: four AVL insertion cases, actual middle-subtree transfer, deletion equality/outer/inner/cascade/successor, top-down multiway split, exact question-specific borrow and root merge, red-cluster collapse, classical insertion cases, and separately implemented LLRB updates. Models are domain-specific; the chapter does not pretend to animate every possible classical red-black deletion input. Binary node labels show true AVL height/balance or explicitly named color/black count. A black-count value of minus one signals unequal temporary routes, not a valid negative black height. Cached ancestor fields can be pending until the recursive return; displayed heights are independently computed from actual links.

Real Edge inspected every stored model checkpoint for label boundaries, spacing and compact viewport geometry. All 867 binary edge endpoints were checked against their actual node ports. A real seven-pair moving transition was checked for attached arrows, pause freezing and resumed progress. Before/result/compare, seek, previous, restart, reduced motion, checkpoint printing and all five editable operation modes were exercised. Ten invalid input cases retained the preceding valid model. At 390 pixels wide, page containment passed. MathML uses STIX Two Math; prose, headings and code use the established separate font families. Formula scripts and closing fences were checked, and links are not underlined.

## Retention and limits

All 52 preceding chapter pages and their question counts remain byte-identical. The library now contains 53 chapter cards and 3,575 worked questions. The source ledger, mathematical audit, real-browser evidence and screenshots support the named checks. Source access is bounded; finite tests do not establish literal 100% infallibility, mastery after reading alone or guaranteed performance on every unseen examination question.
'''
(B/'a_balanced-quality-audit.md').write_text(audit,encoding='utf-8')
print('Prepared reading ledger, source images, precise visual labels and quality audit.')
