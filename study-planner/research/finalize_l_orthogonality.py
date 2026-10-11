"""Deliver the audited draft and continue the planner without inventing approval."""
from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_orthogonality-evidence'
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
acq={a['id']:a for a in json.loads((E/'acquisition.json').read_text())}
core={'oxford','mit-complements','mit-gs','mit-gs-problems','mit-gs-solutions','eth-gs','berkeley-inner','berkeley-sets','berkeley-projection','berkeley-spaces','berkeley-gs'}
ranges={'oxford':list(range(70,79)),'stanford':[14,15,16],'mit-complements':[1,2],'mit-gs':[1,2,3],'mit-gs-problems':[1],'mit-gs-solutions':[1,2],'eth-gs':list(range(19,24)),'harvard-inner':[12,13],'cmu-inner':[1,2,3],'cmu-sets':[1,2,3,4],'cmu-complements':[1,2,3,4]}
courses=[]
for id,a in acq.items():
 pages=ranges.get(id,list(range(1,a.get('pages',0)+1)))
 method='Every native scanned page visually read'if id.startswith('berkeley')else'Full specified teaching text read from official PDF'
 if id in {'mit-gs','cmu-inner','cmu-sets','oxford'}:method+='; selected native pages visually checked for typography or conjugation'
 if a.get('sha256'):assert hashlib.sha256(Path(a['cachePath']).read_bytes()).hexdigest()==a['sha256']
 courses.append(dict(id=id,url=a['url'],nativePages=pages,method=method,core=id in core,sha256=a.get('sha256'),cacheAvailable=bool(a.get('sha256'))))
save(E/'reading.json',dict(status='completed',boundedUniversityCandidates=7,universitiesRead=7,coreUniversities=['Oxford','MIT','Berkeley','ETH Zurich'],courses=courses,note='Page ranges, not entire university catalogs, were read. Official PDF research-browser reading remains valid when a local cache download fails; no unavailable hash is invented.'))
math=json.loads((E/'mathematics.json').read_text());browser=json.loads((E/'browser.json').read_text())
assert math['status']==browser['status']=='passed'
assert browser['geometry']==dict(models=31,frames=134,issues=[])
assert not browser['runtimeErrors']and not browser['mobileOverflow']
chapters=[c for w in json.loads((R/'dist/lessons.json').read_text())for c in w['chapters']]
assert len(chapters)==60 and sum(c['questionCount']for c in chapters)==4169
save(E/'lesson-and-retention.json',dict(status='quality_review_complete',sections=30,questions=84,originalOrReconstructed=82,authenticRevisited=2,rules=84,models=31,checkpoints=134,placements=38,retainedPriorChapters=59,libraryChapters=60,workedEntryPlacements=4169,studentApproved=False,exactChecks=math['exactChecks'],actualJSOracleCases=120,mountedMath=browser['counts']['math']))
(B/'l_orthogonality-quality-audit.md').write_text('''# Orthogonality: completed review draft

## Content and source synthesis

Thirty sections derive real and complex inner products, positive Gram forms, Cauchy–Schwarz, norm identities, orthogonal sets, finite-dimensional complements, the four fundamental subspaces, projection and closest-point proofs, Bessel and Parseval identities, full Gram–Schmidt induction, reduced QR, weighted and skew-coordinate geometry, polynomial/Fourier examples, Householder reflections, projector products, and numerical qualifications. Eighty-four worked entries comprise82 authored or independently reconstructed problems and two authenticated examination revisits. Eighty-four final rules state conditions, formulas and failure modes.

The bounded comparison reviewed written material from seven universities. Four core courses from Oxford, MIT, Berkeley and ETH Zurich were combined; Stanford, CMU and Harvard provided additional comparisons. The source audit identifies eight concrete corrections or convention issues. The native scanned Berkeley pages and selected printed MIT/CMU/Oxford pages were visually read. Reading ranges and cache availability are explicit in reading.json; a failed local download is not represented as a missing scientific review or a fabricated hash.

## Mathematical verification

Independent symbolic calculations check the specific vector, polynomial, complex, reflection and repeated-projector examples. Every projection checkpoint is checked for membership, exact decomposition, perpendicular residual, idempotence, metric self-adjointness and squared distance. Gram–Schmidt acceptance and normalization and QR reconstruction are independently checked. The actual JavaScript rational calculator was compared against independently computed SymPy results for120 reproducible cases, including dependent and zero generators and nonuniform positive metrics. Mathematics.json records the exact number of implemented checks; the count does not imply exhaustive software verification.

## Visual and behavior review

Thirty-one model instances contain134 exact checkpoints across38 placements. Mechanisms use connected two-dimensional vector decompositions, explicitly labeled higher-dimensional coordinate panels, complete subtraction/acceptance/normalization steps, triangular QR contributions, function curves, and actual angle-based Householder motion. Norms are grouped as complete mathematical bases before powers are applied. STIX Two Math, Newsreader, Source Sans3 and JetBrains Mono were verified in real Edge.

The browser checked every checkpoint for geometric issues, and representative desktop/mobile images were visually read. Compact760-by360 canvases retain legible labels through internal phone scrolling. Controls, before/result/comparison, speed, pause/resume, print, reduced motion, invalid-input preservation, library cards and the scheduled chapter link passed. No page overflow or runtime errors were found.

## Retention and provenance

All59 prior pages match the actual immutable published source03f3c2006ebf7737e2468163a9e8763fd7c183ad after CRLF-to-LF normalization only. The original preliminary handoff manifest is preserved; it preceded the final l_linear render and is not silently treated as the publication baseline. The library contains60 chapters and4169 worked-entry placements.

MS CS1405 Q41 and PhD CS1404 Q31 are explicit revisits, with original-page hashes and option order retained. Their answers are independently derived; no official answer-key authority or new unique archive item is claimed.

## Remaining scope

The scheduled projection and least-squares chapters will expand numerical/projector applications rather than be replaced by this prerequisite chapter. The bank does not contain every question ever issued by the source courses. No literal100% guarantee for unbounded material or unseen examination performance is made. This is a reviewed draft, not a recorded student approval. Publication is confirmed separately.
''',encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='l_orthogonality'
g['completedReviewDrafts']=[c for c in g['completedReviewDrafts']if c['topicId']!='l_orthogonality']+[dict(topicId='l_orthogonality',state='quality_review_complete',studentApproved=False,url='chapters/l_orthogonality.html',qualityAudit='research/l_orthogonality-quality-audit.md',publicationState='pending_upload')]
plan=json.loads((R/'dist/schedule.en.json').read_text());order=list(plan['topics']);next=order[order.index('l_orthogonality')+1];assert next=='l_projection'
g.update(currentTopicId=next,state='in_progress',nextTopicRequiresExplicitApproval=False,activeWork='Evaluate written sources and develop the scheduled orthogonal-projection chapter under continuous authorization.',reviewScope=plan['topics'][next]['title'],sourceAudit='research/'+next+'-source-audit.md',sourceAuditPath='research/'+next+'-source-audit.md',qualityAudit='research/'+next+'-quality-audit.md',qualityAuditPath='research/'+next+'-quality-audit.md',lastCompletedReview='l_orthogonality: 84 worked entries,84 final rules, four core reviewed university courses,31 models /134 checkpoints;120 actual JS oracle cases.',currentChapterPublicationState='in_authoring')
save(B/'chapter-gate.json',g)
N=B/'l_projection-evidence';N.mkdir(exist_ok=True)
save(N/'prior-library.json',dict(chapters=[dict(topicId=c['topicId'],url=c['url'],questions=c['questionCount'],canonicalLFsha256=hashlib.sha256((R/'dist'/c['url']).read_bytes().replace(b'\r\n',b'\n')).hexdigest())for c in chapters],normalization='CRLF to LF only; final reviewed-render baseline'))
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Orthogonality review draft\n\nCompleted l_orthogonality:30 sections,84 worked entries,84 final rules,four core written courses from four universities,31 compact models/134 checkpoints/38 placements. Exact calculations and120 actual JavaScript oracle cases passed; Edge verified fonts, geometry, full Gram–Schmidt steps, controls, print, reduced motion, phone containment and weekly routing. All59 prior pages match the published source after line-ending normalization. Library:60 chapters/4169 worked-entry placements. Continue with l_projection under continuous authorization; publication is recorded separately.\n')
print('Finalized l_orthogonality; next scheduled chapter: l_projection.')
