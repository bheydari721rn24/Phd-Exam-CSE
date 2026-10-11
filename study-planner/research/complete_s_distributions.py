"""Finish only the reviewed distribution draft, then hand off to linear maps."""
from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_distributions-evidence'
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
math=json.loads((E/'mathematics.json').read_text());browser=json.loads((E/'browser.json').read_text());assert math['status']==browser['status']=='passed'
assert not browser['geometry']['issues']and not browser['runtimeErrors']
prior=json.loads((E/'prior-library.json').read_text())['chapters'];assert len(prior)==57
for c in prior:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256'],c['topicId']
chapters=[c for w in json.loads((R/'dist/lessons.json').read_text())for c in w['chapters']]
assert len(chapters)==58 and sum(c['questionCount']for c in chapters)==4001
save(E/'retention.json',dict(status='passed',unchangedChapterPages=57,libraryCards=58,workedQuestionEntries=4001))
save(E/'lesson-and-retention.json',dict(status='quality_review_complete',sections=28,workedQuestions=88,originalQuestions=85,authenticRevisitedQuestions=3,finalRules=84,coreUniversities=4,universitiesRead=5,models=26,checkpoints=358,placements=66,staticMathMLChecks=math['staticMathMLChecks'],mountedMath=browser['counts']['math'],studentApproved=False))
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='s_distributions'
g['completedReviewDrafts']=[c for c in g['completedReviewDrafts']if c['topicId']!='s_distributions']+[dict(topicId='s_distributions',state='quality_review_complete',studentApproved=False,url='chapters/s_distributions.html',qualityAudit='research/s_distributions-quality-audit.md',evidence=['research/s_distributions-evidence/'+k+'.json'for k in['reading','mathematics','browser']],publicationState='pending_upload')]
g.update(currentTopicId='l_linear',state='in_progress',nextTopicRequiresExplicitApproval=False,activeWork='Evaluate written courses and author linear transformations under standing continuous authorization.',reviewScope='Linear maps, kernels and images, matrix representations, composition and changes of basis; exact geometric and computational models.',sourceAuditPath='research/l_linear-source-audit.md',sourceAudit='research/l_linear-source-audit.md',qualityAuditPath='research/l_linear-quality-audit.md',qualityAudit='research/l_linear-quality-audit.md',lastCompletedReview='s_distributions: 88 worked entries, 84 rules, five read universities, 26 models / 358 checkpoints; 594 independently enumerated experiments and 105 editable calculator cases.',nextReview='Complete l_linear source, scientific and visual audits.',reviewEvidence=['research/s_distributions-evidence/'+k+'.json'for k in['reading','mathematics','browser']],currentChapterPublicationState='in_authoring')
save(B/'chapter-gate.json',g)
N=B/'l_linear-evidence';N.mkdir(exist_ok=True);save(N/'prior-library.json',dict(chapters=[dict(topicId=c['topicId'],url=c['url'],questions=c['questionCount'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest())for c in chapters]))
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:
 f.write('\n\n## Discrete distributions review draft\n\nCompleted s_distributions with 28 sections, 88 worked entries (85 original/reconstructed and three explicitly revisited authenticated items), 84 complete final rules, four core written university courses plus Stanford. Twenty-six mechanism-specific models provide 358 checkpoints and 66 teaching/problem placements. Independent review passed 594 enumerated experiments, 105 actual editable-calculator cases and 921 native MathML fence checks. Edge inspected all models, 987 mounted formulas, fonts, geometry, pause/resume, comparison, reduced motion, print, mobile containment and library links. All 57 earlier chapter pages are unchanged. Library: 58 chapters / 4001 worked entries. The chapter stays an unapproved review draft. Continue sequentially with l_linear under the standing authorization; publication is recorded separately.\n')
print('Distribution review complete; retained all 57 prior pages; next l_linear.')
