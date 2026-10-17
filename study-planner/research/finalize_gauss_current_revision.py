"""Advance the individual-review inventory only after the actual chapter gates pass."""
from pathlib import Path
import hashlib,json,subprocess
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision'
def load(path):return json.loads((R/path).read_text(encoding='utf8'))
def save(path,data):(R/path).write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
m=load('research/deep-library-revision/l_gauss-current-mathematics.json')
b=load('research/deep-library-revision/l_gauss-current-evidence/browser.json')
assert m['status']=='passed_gauss_current_revision_mathematics' and b['status']=='passed_gauss_current_revision_browser_checks'
assert m['pageSha256']==hashlib.sha256((R/'dist/chapters/l_gauss.html').read_bytes()).hexdigest()
assert all(not f['issues']for f in b['problemFrames']+b['conceptFrames'])
assert all(x['moved']for x in b['playback'])and len(b['labCases'])==54
note='''# Gaussian elimination: current individual review

## Completed scope

The complete earlier lesson is preserved and three substantial explanations added: column-space transport with the original-pivot-column proof, the restricted conjugation argument for later LU pivoting, and a complete examination decision sequence. All 69 original/course solutions were individually expanded; both authentic examination answers were also expanded. The bank still has 71 question placements, not 71 new questions. Its solutions contain 13,291 whitespace-separated words, including mathematical notation. Eighty complete final rules remain, with four sharpened hypotheses.

## Sources and original examinations

Four primary written courses were genuinely reread: MIT 18.700 all 21 PDF pages; Oxford M1 printed pages 3–8 and 16–20; Berkeley Math 54 all seven handwritten pages visually; Stanford CME108/MATH114 all eleven Gaussian/LU/Permuted-LU bodies. Their individual strengths and the bounded five-course historical candidate comparison are documented in the source audit. CMU remains an earlier fifth comparison, not a newly reread source. Public instructor attribution is retained only where documented.

Both authentic source pages were rechecked against original PDF images and pinned Git blobs. The Gaussian copied JSON record for MS CS 1405 Q113 still had option one as 32; it is now 37. The already-correct HTML option and canonical archive record remain 37. The answer remains 336, option four. PhD CS 1404 Q33 remains option three, with an actual scaled LU construction. No independently derived answer is described as an official key.

## Mathematics and visuals

The retained exact models passed 1,035 assertions, the parameter/proof manuscript 861, the advanced manuscript 612, and an independent peer check of the earlier/root scopes 105. These are separate overlapping audit scopes, not counts of different examination problems. All 1,698 native MathML expressions passed structural, fence and script-base checks.

Twenty generic matrix galleries were replaced with actual-input mathematical derivations. Twelve exact row traces were retained and checked operation by operation. An additional Cartesian-choice model explains the authentic integer count. The chapter has 33 question-specific visual aids with 121 finite frames, plus twelve teaching-model families placed in the lesson and eleven matched questions. All 118 selectable teaching-scene placements/states were checked for geometry. The 31 multistep question players passed controls; four real playback runs advanced.

The exact interactive laboratory passed six presets and 48 independent input-grid cases, including 360 invertible transformation checkpoints checked against original input and symbolic classifications. Eight invalid inputs were rejected. Mathematical and coding fonts loaded; three viewport widths stayed within the document width. An observed four-row cell-padding failure and long-inline-formula mobile overflow were repaired. Print exposes all 71 solutions and 121 question-model frames, and restores the reader's prior open-answer state afterward. Three representative rendered screenshots were visually inspected.

## Status and boundaries

The individual author review is complete. This revised edition remains a review draft; student approval is not inferred from approval of an earlier edition. The finite source pool, worked bank, model states and tests cannot establish literal universal correctness or guaranteed performance on every unseen examination question. Restricted homework was not claimed as read. Browser checks cover portable Edge and finite interactions; print DOM/CSS was inspected without a claim about every PDF page break or every browser. Publication is recorded separately from local review completion.
'''
(E/'l_gauss-current-review.md').write_text(note,encoding='utf8')
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def audit_page(content,title):return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/l_gauss.html">Gaussian elimination chapter</a></p><article class="lesson">'+md.render(content)+'</article></main></body></html>'
(R/'dist/reviews/l_gauss-current-review.html').write_text(audit_page(note,'Gaussian elimination: current review'),encoding='utf8')
(R/'dist/reviews/l_gauss-quality.html').write_text(audit_page(note,'Gaussian elimination: current review'),encoding='utf8')
historical=subprocess.check_output(['git','show','ed4a4c486cba3a388a32384faa68a916bfda9399:research/l_gauss-source-audit.md'],cwd=R).decode('utf8')
fresh=(E/'l_gauss-source-revalidation-20261017.md').read_text(encoding='utf8')
source=historical+'\n\n# Current primary-source revalidation\n\n'+fresh.split('\n',1)[1]
(R/'research/l_gauss-source-audit.md').write_text(source,encoding='utf8')
(R/'dist/reviews/l_gauss-sources.html').write_text(audit_page(source,'Gaussian elimination: written source evaluation'),encoding='utf8')
p=load('research/deep-library-revision/progress.json')
for c in p['chapters']:
    if c['topicId']=='l_gauss':c.update(state='revised_checked_review_draft',revisionEvidence='research/deep-library-revision/l_gauss-current-review.md')
n=sum(c['state']=='revised_checked_review_draft'for c in p['chapters'])
assert n==26
p.update(revisedChapters=n,pendingChapters=len(p['chapters'])-n,currentTopicId='l_rank',nextIndividualReview='l_rank')
save('research/deep-library-revision/progress.json',p)
lessons=load('dist/lessons.json')
for w in lessons:
    for c in w.get('chapters',[]):
        if c['topicId']=='l_gauss':
            if c.get('approvedVersion'):c['historicalApprovedVersion']=c.pop('approvedVersion')
            c.update(status='draft',statusLabel='Revised and checked · review draft',revisionState='deep_revision_checked_draft',studentApproved=False,questionCount=71,originalQuestionCount=69,authenticQuestionCount=2,examNotesCount=80,animationCount=33,animationWalkthroughCount=54,qualityAuditUrl='reviews/l_gauss-current-review.html')
save('dist/lessons.json',lessons)
gate=load('research/chapter-gate.json');gate.update(currentTopicId='i_games',state='in_progress',status='in_progress',nextReview='l_rank',lastCompletedReview='l_gauss: complete 71-answer individual revision,80rules,33actual-input problem aids,source/math/browser gates passed.',sourceAuditPath='research/l_gauss-source-audit.md',qualityAuditPath='research/deep-library-revision/l_gauss-current-mathematics.json',currentDraftEvidence='research/deep-library-revision/l_gauss-answer-revision.json',activeWork='26of60baseline reviews checked;34remain.62of119technical chapters exist;57newremain. Continue i_games authoring; next existing review l_rank. Three IELTS lessons exist; learner mastery unconfirmed.',publicationState='gauss_complete_revision_pending_publication')
save('research/chapter-gate.json',gate)
snapshot=load('research/continuation-status-20261017.json');snapshot.update(individuallyRevisedBaselineChapters=26,baselineReviewsRemaining=34,nextExistingReview='l_rank',nextNewTechnicalChapter='i_games',currentReviewEvidence='research/deep-library-revision/l_gauss-current-review.md',sitePublication='gauss_complete_revision_pending_publication');save('research/continuation-status-20261017.json',snapshot)
revision=load('research/deep-library-revision/l_gauss-answer-revision.json');revision.update(state='revised_checked_review_draft',individualChapterReviewComplete=True,studentApproved=False,correctedAuthenticOption={**revision['correctedAuthenticOption'],'scope':'stale JSON copy; published HTML was already correct'});save('research/deep-library-revision/l_gauss-answer-revision.json',revision)
log=R/'WEEKLY_DELIVERY.md';log.write_text(log.read_text(encoding='utf8')+'\n\n## Gaussian elimination individual review complete: 17 October 2026\n\nAll71answers integrated;69original/course solutions rewritten;80rules;three deeper instruction sections;four primary written university scopes reread;two original archive items rechecked.33actual-input problem aids with121frames and118teaching-scene placement/states passed geometry.31multistep controls,4realplaybacks,54exactlabinputs and360transformation checkpoints passed. Repaired actual padding, mobile math overflow and print-state restoration.26of60baseline reviews checked;34remain. Technical inventory remains62/119;57newchapters remain. ThreeIELTS lessons exist;mastery unconfirmed. New-authoring task nowi_games;nextbaseline reviewl_rank. The revised chapter remains student-unapproved. Cloud publication follows separately.\n',encoding='utf8')
print({'baselineReviewsCompleted':n,'remainingBaselineReviews':60-n,'nextAuthoring':'i_games'})
