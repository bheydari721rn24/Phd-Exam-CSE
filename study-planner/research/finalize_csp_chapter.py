"""Register only the source-read, exact-checked and browser-checked CSP edition."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1];B=R/'research'
def read(p):return json.loads((R/p).read_text(encoding='utf8'))
def write(p,d):(R/p).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
math=read('research/i_csp-mathematics.json');browser=read('research/i_csp-evidence/browser.json')
assert math['status']=='passed'and browser['status']=='passed_actual_browser_checks'
assert math['exhaustiveSystems']==browser['labExact']['checked']==4096
assert len(browser['frames'])==335 and all(not f['issues']for f in browser['frames'])
for report in [math,browser]:
 for p,sha in report['inputSha256'].items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==sha,p+' changed after verification'
readings=read('research/i_csp-source-evaluation-start.json')['actualReading']
readings+=[dict(university='Stanford',scope='Seven complete Spring2026 written CSP modules: Overview, Definitions, Examples, Dynamic Ordering, Arc Consistency, Beam Search, Local Search',method='Fresh official file acquisition and actual written-body reading',imagesVisuallyReviewed=False)]
peer=read('research/i_csp-evidence/i_csp-written-source-review.json')
for s in peer['sources']:
 readings.append(dict(university=s['university'],scope=s,method='Scoped official PDF text reading through web reader',imagesVisuallyReviewed=False,localByteFingerprint=None))
documents=read('research/i_csp-evidence/stanford-acquisition.json')
for d in documents:d['readingState']='in_scope_written_body_read';d['visualScope']='Drawing source declarations read; external rendered images not claimed inspected'
ledger=dict(date='2026-10-18',candidateOfferings=7,candidateUniversities=6,primaryUniversities=['Stanford','UC Berkeley','CMU','MIT'],additionalWrittenComparisons=['Cornell','Harvard'],actualReading=readings,documents=documents,discoveredNotRead=['MIT6.034 CSP offering'],fourUniversityGateMet=True,scopeAuthority='research/i_csp-source-audit.md',limits='Bounded written scope, not all courses worldwide; unread university images/protected pseudocode explicitly excluded. Source acquisition history remains separate from actual reading.')
write('research/i_csp-source-ledger.json',ledger)
note='''# Constraint satisfaction: final author review

Date:18 October2026. The complete new English chapter remains a student-unapproved author-review draft.

## Instruction and question-by-question reasoning

Twenty-five teaching sections develop finite relations, modeling, assignment counts, backtracking proofs, deterministic heuristics, directed supports, queue invariants, exact rollback, tree construction/counting, cutsets, global constraints, stronger consistency, conflicts, repair and weighted bounds. Fifty original/attributed problems include numeric calculations, proof obligations, asymptotic assumptions and counterexamples. Four additional authentic MS placements preserve exact original choices and explain every decisive inference. The cycle-coloring solution now derives its closed form through an explicit induction step rather than asserting it. Sixty-four final decisions use complete sentences and identify the assumption behind each rule.

Six actual written university scopes were synthesized. Stanford, Berkeley, CMU and MIT are complementary primaries; Cornell and Harvard provide substantive additional checks. Seven candidate offerings were evaluated. Exact reading ranges, local acquisition failures, omitted protected material, source errors and the bounded prompt inventory are recorded in the source audit and ledger. This is not a worldwide exhaustive-course claim.

The original numeric and map questions were checked against source-page images and pinned PDF fingerprints. No official answer key was verified, and no doctoral CSP item was verified in the bounded archive pass. The1402 edge/arc wording and1405 omitted tree premise are preserved as explicit source qualifications. The map's three-color interactive example is labeled as a teaching assumption.

## Mathematics and executable reference

The actual Python listing was extracted from the rendered HTML and executed, with byte-level source agreement. It was compared against independent direct enumeration on all4096 three-variable Boolean binary-table systems, including empty relations. Plain search, forward checking, MAC, complete enumeration and first-solution mode agreed with the independent solution sets. Propagation preserved all genuine solutions and every successful closure had the required support witnesses.

The reference now uses a separate queued set for expected constant-time queue-membership checks and avoids making before-state snapshots when recording is disabled. Its teaching-output memory is excluded from the lean solver-state bound. Reversed duplicate constraints are conjoined; initially empty isolated domains and the empty variable set are handled correctly. General mathematical correctness relies on the stated invariants/proofs in addition to finite tests.

The mathematics report records39399 assertions, including319 exact serialized support-witness checks, all720 initial queue permutations of the authentic numeric problem, queen attacks, cycle counts and notation structure. Queue order changed that problem's revision count from6 through8 while preserving the successful closure. All749 native MathML expressions passed delimiter, closing-script-base and arity inspection. Explicit raw mathematical expressions in prose were converted to native notation rather than left as unformatted subscripts or Unicode exponent strings.

## Diagrams, interaction and presentation

Twenty-six exact finite domain/queue cases occur in28 player placements. All335 displayed placement/checkpoints passed actual Edge text-padding, connector-endpoint and support-table checks. Five additional interactive board/matching placements use distinct concept mechanisms: actual queen coordinates/attacking pairs and all-different bipartite matchings. A higher-arity factor diagram, original map reconstruction and actual-input tables explain structure, counting, weighted factors, beams and conflict merging.

The editable binary-table laboratory independently implements support filtering in JavaScript. All4096 corresponding finite inputs matched the exact Python closure/failure result; endpoint and reversed-conjunction cases passed. Ten invalid-input checks rejected malformed data. Twenty-eight player controls and three real playbacks passed; three queen placements reproduced conflict scores4,2,2,2 and both valid boards, and two Hall placements traversed all declared support claims.

Newsreader headings, Source Sans3 prose, STIX Two Math notation and JetBrains Mono code loaded. The document stayed within390,768and1360pixel viewports. A genuine long-example-selector overflow was repaired with constrained responsive sizing. Compact graph canvases scroll locally on narrow screens. No links or solution summaries are underlined. Print exposes all54solutions and60initial/failure/final graph snapshots, then restores the reader's previous open/closed answer state. Five representative rendered views were visually inspected, including formula and map views. This checks actual Edge behavior and print DOM/CSS, not every browser or every paginated PDF break.

## Status and limits

Source, mathematical, question, model and browser gates are complete for this edition. Finite verification is not literal universal correctness or an unseen-examination score guarantee. The chapter adds one technical draft; it does not count as another revision of the original sixty-chapter baseline. Publication provenance and GitHub synchronization are recorded separately after their actual success.
'''
(B/'i_csp-quality-audit.md').write_text(note,encoding='utf8')
lessons=read('dist/lessons.json');week=next(w for w in lessons if w['week']==5)
entry=dict(topicId='i_csp',title='Constraint Satisfaction, Propagation, and Structured Search',status='draft',statusLabel='New chapter: author review complete',revisionState='new_chapter_draft',url='chapters/i_csp.html',questionCount=54,originalQuestionCount=50,authenticQuestionCount=4,examNotesCount=64,animationCount=28,animationWalkthroughCount=33,animationReviewState='reviewed_draft',sourceAuditUrl='reviews/i_csp-sources.html',qualityAuditUrl='reviews/i_csp-quality.html',studentApproved=False)
week['chapters']=[c for c in week['chapters']if c['topicId']!='i_csp']+[entry];write('dist/lessons.json',lessons)
available=[c for w in lessons for c in w.get('chapters',[])];assert len(available)==len({c['topicId']for c in available})==64
assert all((R/'dist'/c['url']).is_file()for c in available)
schedule=read('dist/schedule.en.json');present={c['topicId']for c in available};nextnew=next(t for w in schedule['weeks']for unit in w['units']for t in unit['topicIds']if t not in present)
progress=read('research/deep-library-revision/progress.json');progress.update(availableTechnicalChapters=64,currentLibraryChapterCount=64,newTechnicalChaptersRemaining=55,currentTopicId='p_functions',lastCompletedNewTechnicalChapter='i_csp',nextNewTechnicalTopicId=nextnew,nextNewTechnicalTopic=nextnew)
progress['newTechnicalDrafts']['i_csp']=dict(state='completed_author_review_draft',countedAsCompleted=True,studentApproved=False)
progress['newChaptersCompletedSinceBaseline']=[c for c in progress['newChaptersCompletedSinceBaseline']if c['topicId']!='i_csp']+[dict(topicId='i_csp',status='author_review_complete_student_approval_pending',questions=54)];write('research/deep-library-revision/progress.json',progress)
gate=read('research/chapter-gate.json');gate.update(currentTopicId='p_functions',currentDraftPath='research/p_functions.en.md',currentDraftEvidence='research/i_csp-final-author-review.json',state='in_progress',status='in_progress',nextReview='p_functions',lastCompletedNewTechnicalChapter='i_csp',nextNewTechnicalTopicId=nextnew,sourceAuditPath='research/i_csp-source-audit.md',qualityAuditPath='research/i_csp-quality-audit.md',currentReadingEvidence='research/i_csp-source-ledger.json',activeWork='64of119technical drafts exist;55newremain.27of60baseline reviews complete;33remain. CSP author review complete;publication follows. Next individual review p_functions. ThreeIELTS lessons exist;learner mastery unconfirmed.',currentChapterPublicationState='csp_checked_pending_publication',pendingCurrentRevisionPublication='research/i_csp-publication-20261018.json')
gate['latestNewChapterReview']=dict(topicId='i_csp',manuscript='research/i_csp.en.md',evidence='research/i_csp-final-author-review.json',studentApproved=False);write('research/chapter-gate.json',gate)
snapshot=read('research/continuation-status-20261018.json');snapshot.update(availableTechnicalChapters=64,newTechnicalChaptersRemaining=55,completedNewChaptersSinceBaseline=['l_projection','l_leastsquares','i_games','i_csp'],nextNewTechnicalChapter=nextnew,nextExistingReview='p_functions',currentReviewEvidence='research/i_csp-final-author-review.json',nextAuthoringEvidence='research/i_csp-source-ledger.json',sitePublication='csp_local_complete_pending_publication');write('research/continuation-status-20261018.json',snapshot)
register=read('dist/course-audit-week1.en.json');courses=[]
for slug,university,course,url in [('stanford','Stanford','CS221 Spring2026;Moses Charikar and Zachary Robertson','https://stanford-cs221.github.io/spring2026/modules/csps/definitions.js'),('berkeley','UC Berkeley','CS188 written textbook:Filtering;Ordering and Structure','https://inst.eecs.berkeley.edu/~cs188/textbook/csp/ordering.html'),('cmu','CMU','15-281 Fall2025;Pat Virtue and course staff','https://www.cs.cmu.edu/~15281-f25/coursenotes/constraints/index.html'),('mit','MIT','16.410 Fall2010;Brian Charles Williams','https://ocw.mit.edu/courses/16-410-principles-of-autonomy-and-decision-making-fall-2010/pages/lecture-notes/'),('cornell','Cornell','CS4700 Fall2013;Bart Selman','https://www.cs.cornell.edu/courses/cs4700/2013fa/slides/CS4700-CSP_v6.pdf'),('harvard','Harvard','CS50AI;Brian Yu and David J.Malan','https://cs50.harvard.edu/ai/notes/3/')]:
 courses.append(dict(id='i-csp-'+slug,university=university,subject='ai',course=course,url=url,evidence=url,topics=['i_csp'],advantage='Chapter-specific written scope genuinely read; exact complementary contribution and source corrections in reviews/i_csp-sources.html.',limit='Only bounded stated written scopes; unread university images and inaccessible material excluded. Four primary offerings plus two substantive comparisons.',access='official_written_course_material',reviewLevel='reviewed_in_scope_written_sections'))
ids={c['id']for c in courses};register['courses']=[c for c in register['courses']if c['id']not in ids]+courses;register['reviewedAt']='2026-10-18';write('dist/course-audit-week1.en.json',register)
write('research/i_csp-final-author-review.json',dict(date='2026-10-18',state='author_review_complete_student_approval_pending',studentApproved=False,teachingSections=25,questions=54,finalDecisions=64,nativeMathExpressions=749,domainModels=26,playerPlacements=28,specialInteractivePlacements=5,renderedDomainPlacementStates=335,numericAssertions=math['assertions'],browserLaboratoryCases=4096,technicalChaptersAvailable=64,newTechnicalChaptersRemaining=55,baselineReviewsComplete=27,baselineReviewsRemaining=33,evidence=['research/i_csp-source-audit.md','research/i_csp-source-ledger.json','research/i_csp-mathematics.json','research/i_csp-evidence/browser.json']))
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf8')as f:f.write('\n\n## Constraint satisfaction author review completed:18October2026\n\n25teaching sections;50original/course problems;4visually verified authentic MS placements with explicit source ambiguities;64final decisions. Six written university scopes compared,with four complementary primary offerings.39399mathematical assertions,all4096printed-code relation systems,720numeric queue orders,749MathML expressions,335domain placement/states,28controls,5separateboard/matching placements,4096independent browserlab cases and threeviewport/print checks passed.64of119technical chapters exist;55newremain. Baseline review remains27of60;33pending. ThreeIELTS lessons exist,mastery unconfirmed. Nextindividual review p_functions;nextnewtechnical '+nextnew+'. The new chapter remains student-unapproved;cloudpublication follows separately.\n')
print(dict(available=64,newRemaining=55,baselineReviewed=27,nextExisting='p_functions',nextNew=nextnew))
