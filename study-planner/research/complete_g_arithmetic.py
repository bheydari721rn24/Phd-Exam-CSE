"""Record a completed audited draft and continue under the explicit standing instruction."""
from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'g_arithmetic-evidence'
math=json.loads((E/'mathematics.json').read_text(encoding='utf-8'));browser=json.loads((E/'browser.json').read_text(encoding='utf-8'))
assert math['status']==browser['status']=='passed'
assert math['retainedPages']==47 and browser['geometry']['models']==15 and not browser['geometry']['issues']
gate=json.loads((B/'chapter-gate.json').read_text(encoding='utf-8'))
gate.setdefault('completedReviewDrafts',[])
entry=dict(topicId='g_arithmetic',state='quality_review_complete',studentApproved=False,url='chapters/g_arithmetic.html',qualityAudit='research/g_arithmetic-quality-audit.md',evidence=['research/g_arithmetic-evidence/reading.json','research/g_arithmetic-evidence/mathematics.json','research/g_arithmetic-evidence/browser.json'],publicationState='pending_network')
gate['completedReviewDrafts']=[x for x in gate['completedReviewDrafts']if x['topicId']!='g_arithmetic']+[entry]
gate.update(currentTopicId='g_mux',state='in_progress',sourceAudit='research/g_mux-source-audit.md',qualityAudit='research/g_mux-quality-audit.md',sourceAuditPath='research/g_mux-source-audit.md',qualityAuditPath='research/g_mux-quality-audit.md',activeWork='Evaluate and read written courses for g_mux; arithmetic chapter is a completed audited review draft.',reviewScope='g_mux: multiplexers, decoders, encoders and combinational function realization',publicationState='pending_network',pendingPriorPublication='Arithmetic review draft and preceding simulation corrections are preserved locally; Sites backend transport currently fails. No new online version is claimed.')
(B/'chapter-gate.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Arithmetic-circuit review draft — 10 October 2026\n\nCompleted g_arithmetic with four reviewed written university courses, 82 fully worked problems, 80 final reasoning rules and 15 concept-specific models / 71 checkpoints. Independent reference checks passed for 16,648 cases / 84,808 states. All 47 prior chapter bodies remain byte-identical. Browser checks passed for fonts, glyph bounds, controls, reduced motion, print, invalid inputs and mobile containment. The draft is review-complete but not labeled student-approved. Native Sites transport currently fails, so online publication remains pending; retain the prepared source and archive. Continuous sequential authorization advances work to g_mux without requesting another start permission.\n')
prior=json.loads((R/'dist/lessons.json').read_text(encoding='utf-8'));chapters=[c for w in prior for c in w['chapters']]
F=B/'g_mux-evidence';F.mkdir(exist_ok=True)
(F/'prior-library.json').write_text(json.dumps(dict(chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount'])for c in chapters]),indent=2)+'\n',encoding='utf-8')
print('Completed audited arithmetic draft; current writing gate is g_mux.')
