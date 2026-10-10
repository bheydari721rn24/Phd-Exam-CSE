from pathlib import Path
import json,hashlib,subprocess
B=Path(__file__).resolve().parent;R=B.parent;E=B/'g_mux-evidence'
m=json.loads((E/'mathematics.json').read_text(encoding='utf-8'));v=json.loads((E/'browser.json').read_text(encoding='utf-8'));models=json.loads((R/'dist/chapters/g_mux-models.json').read_text(encoding='utf-8'))
assert m['status']==v['status']=='passed'and not v['geometry']['issues']and m['retainedPages']==48
assert v['geometry']['models']==len(models['models'])==17
count=sum(len(x['frames'])for x in models['models'])
audit=f'''# Scientific and visual quality audit: g_mux

## Delivery status

Complete review draft, not labeled student-approved. The explicit standing instruction authorizes continuing to the next chapter after this chapter's audit. English lesson, references, worked bank and final rules are available together in the chapter page. Online publication is reconciled separately; a local file is not automatically an online deployment.

## Content and provenance

- 29 sections including 24 teaching sections, a complete summary, 82 worked questions, 80 full-sentence reasoning rules, an editable lab, and exact references.
- Four genuinely reviewed written courses from Stanford, MIT, Cambridge and ETH Zurich. The source audit records the bounded candidate pool, actual read scopes, file hashes, and corrected source ambiguities.
- 80 original or explicitly reconstructed mathematical/conceptual problems plus two authentic MSc bridges, Q80 and Q82 from 1404 PDF page 19. The bank progresses from foundational counterexamples to cofactor synthesis, hierarchy, timing, grant proofs, lookup capacity, polarity and mixed arithmetic circuits. Not every entry is described as hard.
- Each solution explains its derivation rather than supplying an answer alone. Visual companions explicitly declare their sample inputs when the problem has different parameters. No fabricated doctoral problem or official-key claim is included.

## Mathematics and executable evidence

Independent integer, set-membership, search, and geometric-segment references passed for {m['cases']:,} input cases and {m['states']:,} generated checkpoints. Checks include every binary-data combination for two-, four-, and eight-input selectors/trees; enabled/disabled decoder and demultiplexer polarity; all request words through eight requests for both fixed priorities and every rotating start; all display codes under both polarities; every bus data/enable combination; sixteen integrated adder/selector inputs; and both cascade input bits.

Both authentic answers were independently rederived. Q82 was enumerated over all sixteen truth rows; the original adder, XOR, inverter and selector connections were checked against the scanned source. Native MathML contains {m['mathExpressions']} expressions in the static page; delimiter and closing-script-base checks passed. These tests do not substitute for electrical timing signoff, HDL compilation, or a proof about all possible custom inputs and all unseen exam questions.

## Diagrams and teaching models

17 distinct concept-specific stored models, {count} checkpoints, and 47 mounted lesson/solution appearances. Models include labeled binary selector trees, a real shared-inverter/four-AND decoder schematic, positive and negative decoder interfaces, two-bank expansion, data-zero demultiplexing, sequential fixed/rotating priority decisions, row/column ROM organization, real seven-segment geometry, tri-state bus classification, authentic cascaded selectors, and the fully connected adder/XOR/inverter/MUX topology.

The input contract and exact outcome are shown independently from the transition replay. The diagrams use marked electrical junctions, connected named ports, and a bounded lesson-column stage; larger diagrams scroll or zoom inside the stage. The integrated diagram was manually revised after screenshots to connect every actual signal branch. Tree value labels were moved off wires. Model check labels were corrected to the shared player's schema, eliminating visible undefined text.

## Real-browser checks

Edge checked all {count} stored frames: no label collision, clipped glyph or insufficient label padding was reported. Source Sans 3, Newsreader, STIX Two Math and JetBrains Mono loaded. Math fences and scripts have visible bounds, and no underlined links remain. The chapter passed paused start, Play/Pause, previous/next, scrubbing, reset, reduced-motion and complete print checkpoints. Eight editable examples and six invalid-input preservation cases passed. Mobile width 390 has no page overflow. The library has 49 chapter cards and the Week 3 link works. No runtime errors or undefined teaching labels were reported.

Screenshots of the real circuits, display, priority states, question, final rules and mobile/print views were retained. They are evidence of the tested samples, not a universal visual proof at every screen size.

## Retention and remaining boundaries

All 48 preceding chapter HTML files remain byte-identical to the snapshot, and their question counts are preserved. No synced sources were edited. The four core courses contribute different parts of the chapter; no claim is made that every course supplies every advanced topic. Complete four-valued HDL behavior, analog contention voltages, device loading, sequential arbitration fairness, and specific commercial memory/PAL architectures need additional stated assumptions. The draft supplies deep instruction and exam-pattern reasoning without guaranteeing a score or literal universal completeness.
'''
(B/'g_mux-quality-audit.md').write_text(audit,encoding='utf-8')
subprocess.run(['python','-X','utf8',str(B/'render_g_mux.py')],cwd=R,check=True)
g=json.loads((B/'chapter-gate.json').read_text(encoding='utf-8'));entry=dict(topicId='g_mux',state='quality_review_complete',studentApproved=False,url='chapters/g_mux.html',qualityAudit='research/g_mux-quality-audit.md',evidence=['research/g_mux-evidence/reading.json','research/g_mux-evidence/mathematics.json','research/g_mux-evidence/browser.json'],publicationState='pending_source_push')
g['completedReviewDrafts']=[x for x in g.get('completedReviewDrafts',[])if x['topicId']!='g_mux']+[entry]
g.update(currentTopicId='d_recurrence',state='in_progress',nextTopicRequiresExplicitApproval=False,activeWork='Evaluate written university treatments of discrete recurrence relations; g_mux has passed its chapter audit.',reviewScope='d_recurrence: sequence recurrences, initial conditions, characteristic roots, forcing, counting recurrences and generating-function bridges',sourceAuditPath='research/d_recurrence-source-audit.md',sourceAudit='research/d_recurrence-source-audit.md',qualityAuditPath='research/d_recurrence-quality-audit.md',qualityAudit='research/d_recurrence-quality-audit.md',lastCompletedReview=f'g_mux: 82 solved entries, 80 rules, four written university courses, 17 models / {count} checkpoints; {m["cases"]} independently referenced cases.',nextReview='Complete d_recurrence before advancing; standing sequential authorization remains active.')
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write(f'\n\n## Selector/decoder/encoder review draft — 10 October 2026\n\nCompleted g_mux: four read written university courses, 82 complete solutions, 80 final rules, 17 domain-specific models / {count} saved checkpoints. Independent references passed for {m["cases"]} cases / {m["states"]} generated checkpoints. All 48 preceding pages retained byte for byte. Browser font, geometry, control, lab, mobile and print checks passed. Review complete, not yet student-approved. Publication tracked separately. Standing authorization advances work to d_recurrence without another start-permission request.\n')
F=B/'d_recurrence-evidence';F.mkdir(exist_ok=True);chapters=[c for w in json.loads((R/'dist/lessons.json').read_text(encoding='utf-8'))for c in w['chapters']]
(F/'prior-library.json').write_text(json.dumps(dict(chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount'])for c in chapters]),indent=2)+'\n',encoding='utf-8')
print('Completed audited g_mux review draft; d_recurrence is the current chapter.')
