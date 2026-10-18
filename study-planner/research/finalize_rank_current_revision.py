"""Record completion only after current mathematical and rendered gates pass."""
from pathlib import Path
import hashlib,json,subprocess
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision'
def load(p):return json.loads((R/p).read_text(encoding='utf8'))
def save(p,d):(R/p).write_text(json.dumps(d,indent=2)+'\n',encoding='utf8')
m=load('research/deep-library-revision/l_rank-current-mathematics.json')
b=load('research/deep-library-revision/l_rank-current-evidence/browser.json')
assert m['state']=='passed_current_rank_mathematical_review'
assert b['status']=='passed_rank_current_revision_browser_checks'
assert m['pageSha256']==hashlib.sha256((R/'dist/chapters/l_rank.html').read_bytes()).hexdigest()
assert len(b['problemFrames'])==81 and len(b['conceptFrames'])==75
assert all(not f['issues']for f in b['problemFrames']+b['conceptFrames'])
assert all(f['ok']for f in b['controls'])and all(f['moved']for f in b['playback'])
assert len(b['labCases'])==31 and b['independentTraceChecks']==240 and not b['errors']
note='''# Rank, invertibility and solution sets: current individual review

## Instruction and every answer

The complete main lesson was read and preserved. Two substantial sections were added: a complete rank-and-fiber examination decision sequence, and the distinction between right-kernel row-membership tests and left-kernel output-membership tests. All 88 original and course-derived answers were individually read and extended with question-specific coordinate calculations, missing proof steps, complete compatibility equations, independent-parameter checks or actual attaining constructions. Both authentic answers were rewritten as complete teaching solutions. The bank has 90 question placements, not 90 new questions; its solutions contain 14,535 whitespace-separated words, including mathematical notation.

The misleading left-annihilator wording in LR88 was corrected: the three-by-four full-row-rank matrix has a one-dimensional right kernel, which supplies its row-space hyperplane equation. Its left kernel is zero. The authentic norm-bound solution now also proves the complex-eigenvalue conclusion for an arbitrary real norm using a justified complex extension, while retaining the simpler Euclidean proof. A visual inspection caught single-bar rendering in newly authored norm expressions; those expressions now explicitly use double norm bars. Eighty complete final rules remain, with six rules sharpened and the full decision sequence added.

## Sources and authentic examinations

Four primary written university scopes were genuinely reread: MIT 18.700 PDF pages 13–20; Oxford M1 pages 42–51, 57–61 and 68–69; Stanford EE263 Lecture 3 pages 1–19; and both handwritten Berkeley Math 54 pages, visually inspected. This is 46 scoped pages from four universities. The bounded historical candidate comparison contains a fifth CMU course, which was not freshly reread in this task. Acquisition, actual reading, attribution and source fingerprints are recorded separately.

The current source reconciliation identifies MIT's erroneous rank-two yz-plane basis and its tall-matrix pivot wording, and Oxford's undefined symbol and invalid claim that one deletion must immediately make a dependent spanning list independent. These errors are not adopted. Both authentic source PDF pages were visually rechecked: MS CS 1405 Q41 has dimension nine, option two; PhD CS 1404 Q30 has positive definiteness as the false assertion, option two. Original hashes match the pinned repository records. Answers are independently proved, not represented as official keys.

## Mathematics, diagrams and exact interaction

The retained independent rank oracle passed 2,524 assertions; the newly explicit affine formulas, basis calculations, interpolation witnesses and sharp cube-zero constructions passed 73 additional exact assertions. These overlapping finite scopes are not counts of distinct examination questions. All 1,551 native MathML expressions passed structural, fence and script-base inspection.

Sixty-two old question-animation aliases were removed. Six retained question walkthroughs now match the actual question inputs. Thirteen generic matrix galleries were replaced with mathematical derivations using the exact problem data; twelve row traces were checked operation by operation and redrawn with original/current coefficient matrices; two authentic aids were added. The chapter now has 27 question-specific visual aids with 81 finite frames, plus twelve main teaching-model families. Every one of the 81 problem frames and 75 teaching-scene placement/states passed browser geometry checks. Twenty-four multistep controls and four actual playbacks passed. The five-column teaching scene no longer mislabels its coefficient matrix as augmented.

The four-space laboratory passed six presets and one independent input for each of the 25 allowed matrix shapes, from one-by-one through five-by-five. Rank, RREF, original pivot columns and complete independent right/left-kernel bases were compared with exact symbolic results. All 240 emitted row checkpoints preserved the independently calculated row space. Eight invalid inputs were rejected. These row-space checks are not described as explicit tracked transformation-matrix checks; the laboratory does not emit those matrices.

Mathematical and coding fonts loaded. Desktop, tablet and narrow-screen documents stayed within viewport width. Long inline mathematics can scroll locally without cutting a formula or expanding the whole document. A real print-state restoration failure was repaired with an early state snapshot and final restoration. Print exposes all 90 solutions and all 81 question-model frames, then restores the reader's prior answer state. Three rendered views were visually inspected; the post-correction norm view was checked separately.

## Status and limits

Individual author review is complete. This revised edition remains a student-unapproved review draft. Finite source scopes, exact examples, formal proofs and browser checks support the chapter but do not establish literal universal accuracy, exhaustive worldwide course reading or guaranteed performance on every unseen examination. The source pool, scalar fields, parameter branches and original-examination provenance are explicit. Browser evidence covers portable Edge and finite interactions; print DOM/CSS was inspected without claiming every final PDF page break. Publication and GitHub backup are recorded separately.
'''
(E/'l_rank-current-review.md').write_text(note,encoding='utf8')
(R/'research/l_rank-quality-audit.md').write_text(note,encoding='utf8')
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def audit_page(content,title):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/l_rank.html">Rank, invertibility and solution sets</a></p><article class="lesson">'+md.render(content)+'</article></main></body></html>'
for name in['current-review','quality']:(R/f'dist/reviews/l_rank-{name}.html').write_text(audit_page(note,'Rank: current individual review'),encoding='utf8')
historical=subprocess.check_output(['git','show','ce272ad83079d4e95f6e009fd89c603240a8a708:research/l_rank-source-audit.md'],cwd=R).decode('utf8')
fresh=(E/'l_rank-source-revalidation-20261018.md').read_text(encoding='utf8')
source=historical+'\n\n# Current source revalidation\n\n'+fresh.split('\n',1)[1]
(R/'research/l_rank-source-audit.md').write_text(source,encoding='utf8')
(R/'dist/reviews/l_rank-sources.html').write_text(audit_page(source,'Rank: source evaluation and fresh revalidation'),encoding='utf8')
p=load('research/deep-library-revision/progress.json')
for c in p['chapters']:
    if c['topicId']=='l_rank':c.update(state='revised_checked_review_draft',revisionEvidence='research/deep-library-revision/l_rank-current-review.md')
n=sum(c['state']=='revised_checked_review_draft'for c in p['chapters']);assert n==27
p.update(revisedChapters=n,pendingChapters=len(p['chapters'])-n,currentTopicId='p_functions',nextIndividualReview='p_functions')
save('research/deep-library-revision/progress.json',p)
lessons=load('dist/lessons.json')
for week in lessons:
    for c in week.get('chapters',[]):
        if c['topicId']=='l_rank':
            if c.get('approvedVersion'):c['historicalApprovedVersion']=c.pop('approvedVersion')
            c.update(status='draft',statusLabel='Revised and checked · review draft',revisionState='deep_revision_checked_draft',studentApproved=False,questionCount=90,originalQuestionCount=88,authenticQuestionCount=2,examNotesCount=80,animationCount=27,animationWalkthroughCount=41,qualityAuditUrl='reviews/l_rank-current-review.html')
save('dist/lessons.json',lessons)
gate=load('research/chapter-gate.json')
gate.update(currentTopicId='i_csp',state='in_progress',status='in_progress',nextReview='p_functions',lastCompletedReview='l_rank: all90answers individually revised,80rules,27actual-input problem aids,source/math/browser gates passed.',sourceAuditPath='research/l_rank-source-audit.md',qualityAuditPath='research/deep-library-revision/l_rank-current-review.md',currentDraftEvidence='research/deep-library-revision/l_rank-answer-revision.json',activeWork='27 of60 baseline reviews checked;33 remain.63 of119 technical drafts exist;56 new remain. Next authoring i_csp;next existing review p_functions. Three IELTS lessons are prepared;learner mastery is unconfirmed.',publicationState='rank_revision_pending_publication',publishedVersion=109,currentChapterPublicationState='rank_revision_checked_local_pending_github_and_site',pendingCurrentRevisionPublication='research/l_rank-publication-20261018.json',currentDraftPath='research/l_rank.en.md')
gate['priorCompletedContentPublication']='research/i_games-publication-20261018.json'
save('research/chapter-gate.json',gate)
snapshot=load('research/continuation-status-20261018.json')
snapshot.update(date='2026-10-18',availableTechnicalChapters=63,newTechnicalChaptersRemaining=56,individuallyRevisedBaselineChapters=27,baselineReviewsRemaining=33,nextExistingReview='p_functions',nextNewTechnicalChapter='i_csp',currentReviewEvidence='research/deep-library-revision/l_rank-current-review.md',currentAnswerManuscript='research/deep-library-revision/l_rank-answer-additions.en.md',currentAnswerManuscriptChecks='research/deep-library-revision/l_rank-current-mathematics.json',sitePublication='rank_revision_pending_publication',lastVerifiedPublishedVersion=109,publicationEvidence='research/i_games-publication-20261018.json')
save('research/continuation-status-20261018.json',snapshot)
revision=load('research/deep-library-revision/l_rank-answer-revision.json');revision.update(state='revised_checked_review_draft',individualChapterReviewComplete=True,studentApproved=False)
save('research/deep-library-revision/l_rank-answer-revision.json',revision)
log=R/'WEEKLY_DELIVERY.md';text=log.read_text(encoding='utf8');heading='## Rank individual review completed: 18 October 2026'
entry='\n\n'+heading+'\n\nAll90solutions individually reviewed;88original/course answers extended,2authentic derivations rewritten;80rules and2deeper instruction sections. Four primary written university scopes reread,46pages;two original examination pages/hash records rechecked.27actual-input problem aids,81frames,75teaching placement/states,24multistep controls,4playbacks,31exactlabinputs and240row-space checkpoints passed. Corrected LR88 annihilator wording, coefficient/augmented label, explicit norm-bar rendering and print restoration.27of60baseline reviews checked;33remain.63of119technical chapters exist;56newremain. ThreeIELTS lessons exist,mastery unconfirmed. Siteversion109 alreadydelivers Games/fullGaussian/tenofflinecopies;Rankpublication followsseparately. Nextauthoring i_csp;nextbaseline reviewp_functions.\n'
if heading not in text:log.write_text(text+entry,encoding='utf8')
print({'reviewed':n,'pending':60-n,'nextAuthoring':'i_csp','nextExistingReview':'p_functions'})
