"""Record the completed individual review without inferring student approval."""
from pathlib import Path
import json,re
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1];B=R/'research';D=R/'dist';E=B/'deep-library-revision'
def load(p):return json.loads(p.read_text(encoding='utf8'))
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
assert load(E/'p_arrays-current-mathematics.json')['status']=='passed_arrays_current_revision_integrated_checks'
md=MarkdownIt('commonmark',{'html':True}).enable('table')
note=(E/'p_arrays-current-review.md').read_text(encoding='utf8');(B/'p_arrays-quality-audit.md').write_text(note,encoding='utf8')
def page(text,title):return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><a href="../chapters/p_arrays.html">Arrays and Indexing</a><article class="lesson">'+md.render(text)+'</article></main></body></html>'
for name in ['current-review','quality']:(D/f'reviews/p_arrays-{name}.html').write_text(page(note,'Arrays: current individual review'),encoding='utf8')
source=B/'p_arrays-source-audit.md';s=source.read_text(encoding='utf8')
heading='# Current individual review: 20 October 2026'
if heading not in s:
    s+='\n\n'+heading+'\n\n'+note.split('## Written source selection and actual reading\n\n')[1].split('## Authentic problems')[0]
source.write_text(s,encoding='utf8');(D/'reviews/p_arrays-sources.html').write_text(page(s,'Arrays: written-source selection and current scope'),encoding='utf8')
p=load(E/'progress.json')
for c in p['chapters']:
    if c['topicId']=='p_arrays':c.update(state='revised_checked_review_draft',revisionEvidence='research/deep-library-revision/p_arrays-current-review.md')
n=sum(c['state']=='revised_checked_review_draft'for c in p['chapters']);assert n==29
p.update(revisedChapters=n,pendingChapters=60-n,currentTopicId='g_kmap',nextIndividualReview='g_kmap')
save(E/'progress.json',p)
lessons=load(D/'lessons.json')
for w in lessons:
    for c in w['chapters']:
        if c['topicId']=='p_arrays':
            if c.get('approvedVersion'):c['historicalApprovedVersion']=c.pop('approvedVersion')
            c.update(status='draft',statusLabel='Revised and checked · review draft',revisionState='deep_revision_checked_draft',studentApproved=False,questionCount=83,originalQuestionCount=81,authenticQuestionCount=2,examNotesCount=80,animationCount=38,animationWalkthroughCount=56,qualityAuditUrl='reviews/p_arrays-current-review.html')
assert sum(len(w['chapters'])for w in lessons)==64;save(D/'lessons.json',lessons)
gate=load(B/'chapter-gate.json');gate.update(currentTopicId='g_kmap',nextReview='g_kmap',state='in_progress',status='in_progress',lastCompletedReview='p_arrays',lastCompletedReviewEvidence='research/deep-library-revision/p_arrays-current-review.md',sourceAuditPath='research/g_kmap-source-audit.md',currentDraftPath='research/g_kmap.en.md',currentIndividualReviewComplete=False,currentReviewedAnswerBlocks=0,currentChapterPublicationState='arrays_functions_csp_checked_pending_site',pendingCurrentRevisionPublication='research/p_arrays-publication-20261020.json',activeWork='29 of 60 baseline editions individually reviewed; 31 remain. 64 of 119 technical chapters exist; 55 new remain. Next baseline review g_kmap; next new chapter i_informed. Three IELTS lessons prepared; learner mastery unconfirmed. Continue under standing authorization; revisions remain student-unapproved drafts.')
gate['completedArraysReview']={'date':'2026-10-20','solutions':83,'rules':80,'studentApproved':False,'evidence':'research/deep-library-revision/p_arrays-current-review.md'}
save(B/'chapter-gate.json',gate)
a=load(E/'p_arrays-answer-integration.json');a.update(status='author_review_complete_student_approval_pending',individualReviewComplete=True,studentApproved=False,qualityEvidence='research/deep-library-revision/p_arrays-current-review.md');save(E/'p_arrays-answer-integration.json',a)
snapshot={'date':'2026-10-20','availableTechnicalChapters':64,'plannedTechnicalChapters':119,'newTechnicalChaptersRemaining':55,'individuallyRevisedBaselineChapters':29,'baselineReviewsRemaining':31,'preparedIELTSAcademicLessons':3,'learnerMastery':'unconfirmed','nextExistingReview':'g_kmap','nextNewTechnicalChapter':'i_informed','publicationState':'pending_site_publication','lastConfirmedPublishedVersion':110,'reviewEvidence':'research/deep-library-revision/p_arrays-current-review.md'};save(B/'continuation-status-20261020.json',snapshot)
# Reuse only the inventory presentation, with this edition's real counts and cards.
s=(B/'build_functions_library_inventory.py').read_text(encoding='utf8').replace("v['revisedChapters']==28 and v['pendingChapters']==32","v['revisedChapters']==29 and v['pendingChapters']==31").replace('28 of 60','29 of 60').replace('32 reviews remain','31 reviews remain').replace('28 reviewed','29 reviewed').replace('32 pending','31 pending').replace('28 baseline reviews complete, 32 remain','29 baseline reviews complete, 31 remain').replace('Next existing review: Arrays and Indexing.','Next existing review: Minterms, Maxterms and Logic Minimization.')
s=s.replace('<h2>Functions, Scope and Parameter Passing</h2><p>Latest individual revision: 91 complete worked solutions, 80 final decision rules and 27 exact-input visual aids with 101 checkpoints. The six-course source audit distinguishes four primary universities and two supplementary courses.</p>','<h2>Arrays and Indexing</h2><p>Latest individual revision: all 83 solutions rewritten, 80 final rules and 38 exact-input visual aids with 143 checkpoints. The six-course source audit distinguishes current reading from historical supplementary reading.</p>').replace('chapters/p_functions.html','chapters/p_arrays.html').replace('reviews/p_functions-current-review.html','reviews/p_arrays-current-review.html')
exec(compile(s,str(B/'build_functions_library_inventory.py'),'exec'),{'__file__':str(B/'build_functions_library_inventory.py'),'__name__':'current_arrays_inventory'})
log=R/'WEEKLY_DELIVERY.md';s=log.read_text(encoding='utf8');h='## Arrays individual review completed: 20 October 2026'
if h not in s:log.write_text(s+'\n\n'+h+'\n\nAll 83 worked solutions rewritten and checked; 80 final rules retained and strengthened. Four primary university reading scopes documented, with two historical supplementary courses. Two original PDF pages and hashes rechecked. 38 exact-input visual aids, 143 frames, 121 teaching placement/states, 180 laboratory cases and native mathematical layout passed. The 63 other chapter bodies and 421 previous shared model entries are preserved. 29 of 60 baseline editions reviewed; 31 remain. 64 of 119 technical chapters exist; 55 new remain. Three IELTS Academic lessons prepared; mastery unconfirmed. Next existing review g_kmap; next new chapter i_informed. Student approval is pending. Latest confirmed hosted version is 110; combined Arrays/Functions/CSP publication and GitHub backup are recorded separately.\n',encoding='utf8')
print(snapshot)
