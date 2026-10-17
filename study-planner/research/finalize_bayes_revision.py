"""Record only the chapter whose current mathematics and browser audits passed."""
from pathlib import Path
from markdown_it import MarkdownIt
import hashlib,json,re
from teaching_prose_spacing import fix
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision'
def read(p):return json.loads((R/p).read_text(encoding='utf8'))
def write(p,x):(R/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
m=read('research/deep-library-revision/s_bayes-mathematics.json');b=read('research/deep-library-revision/s_bayes-evidence/browser.json')
assert m['status']=='passed_independent_mathematical_checks'and b['status']=='passed_bayes_revision_browser_checks'
assert all(x['moved']for x in b['playback'])
p=R/'research/author_bayes_problems.py';s=p.read_text(encoding='utf8')
qs=read('research/s_bayes-questions.json')
for qid,old in [('SB33','Families have sizes one, two, and three with prior probabilities $(1/2,1/3,1/6)$. Select a child uniformly from all children in the population. What are the family-size probabilities of that selected child?'),('SB36','Two heavy and eight light coins lie in a bag. An unordered pair is selected uniformly. The selected pair has equal weights. What is the probability both are heavy?')]:
 new=next(x['stem']for x in qs if x['id']==qid);s=s.replace(old,new.replace("'","\\'"))
p.write_text(s,encoding='utf8')
p=R/'research/s_bayes.en.md';s=p.read_text(encoding='utf8');old='If the family-size prior is $\\pi_n$ and an individual is drawn uniformly from a large population of all children, the corresponding family-size weights are proportional to $n\\pi_n$, subject to finite positive mean.'
new='If the fixed family proportions are $\\pi_n$, uniform child selection weights them by $n\\pi_n$ and normalizes by the positive mean. A limiting population law requires finite positive mean. For a small random finite population, the expected ratio of random counts need not equal the ratio of their expectations.'
s=s.replace(old,new);p.write_text(s,encoding='utf8')
p=R/'dist/chapters/s_bayes.html';s=p.read_text(encoding='utf8').replace('../reviews/s_bayes-quality.html','../reviews/s_bayes-current-review.html');p.write_text(s,encoding='utf8')
progress=read('research/deep-library-revision/progress.json')
for x in progress['chapters']:
 if x['topicId']=='s_bayes':x.update(state='revised_checked_review_draft',revisionEvidence='research/deep-library-revision/s_bayes-current-review.md')
n=sum(x['state']=='revised_checked_review_draft'for x in progress['chapters']);assert n==25
progress.update(revisedChapters=n,pendingChapters=60-n,currentTopicId='l_gauss',nextIndividualReview='l_gauss');write('research/deep-library-revision/progress.json',progress)
gate=read('research/chapter-gate.json');gate.update(currentTopicId='l_leastsquares',state='in_progress',nextReview='l_gauss',lastCompletedReview='s_bayes: all65answers individually reviewed;63expanded derivations;80final decisions;31exact question figures;13players and all76finitecheckpoints checked.',nextNewTechnicalTopicId='l_leastsquares',sourceAuditPath='research/deep-library-revision/s_bayes-current-review.md',qualityAuditPath='research/deep-library-revision/s_bayes-mathematics.json',activeWork='25of60baseline chapters individually reviewed;35remain.61technical drafts exist,58newtechnical chapters remain.Continue least-squares authoring and Gauss review under standing authorization.');write('research/chapter-gate.json',gate)
snap=read('research/continuation-status-20261015.json');snap.update(date='2026-10-17',individuallyRevisedBaselineChapters=25,baselineReviewsRemaining=35,nextExistingReview='l_gauss',nextNewTechnicalChapter='l_leastsquares',sitePublication='official_source_open_succeeded_packaging_pending');write('research/continuation-status-20261017.json',snap)
lessons=read('dist/lessons.json')
for w in lessons:
 for x in w['chapters']:
  if x['topicId']=='s_bayes':x.update(status='draft',statusLabel='Revised and checked · review draft',revisionState='deep_revision_checked_draft',qualityAuditUrl='reviews/s_bayes-current-review.html',questionCount=65,examNotesCount=80,problemFigureCount=31,studentApproved=False)
write('dist/lessons.json',lessons)
md=MarkdownIt('commonmark',{'html':True}).enable('table');html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bayes: current individual review</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p><a href="../chapters/s_bayes.html">Bayes chapter</a></p>'+md.render((E/'s_bayes-current-review.md').read_text(encoding='utf8'))+'</main></body></html>'
(R/'dist/reviews/s_bayes-current-review.html').write_text(fix(html),encoding='utf8')
record=read('research/deep-library-revision/s_bayes-answer-revision.json');record.update(state='revised_checked_review_draft',studentApproved=False,questionFigures=31,finiteScenePlacements=len(b['finiteScenes']),finiteCheckpoints=sum(x['frames']for x in b['finiteScenes']),pageSha256=hashlib.sha256(p.read_bytes()).hexdigest());write('research/deep-library-revision/s_bayes-answer-revision.json',record)
p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf8');marker='## Bayes individual review completed: 17 October 2026'
if marker not in s:p.write_text(s+'\n\n'+marker+'\n\n65answers reviewed;63newderivations;80final decisions;31actual-input vector figures. Fixed finite-population and common-coin-weight assumptions;all76finitecheckpoints and actual playback checked.25of60baseline reviews checked;35remain.61technical drafts;58newtechnical chapters remain. IELTS has two actual prepared lessons;mastery remains unconfirmed. Next new chapter:l_leastsquares;next existing review:l_gauss. Official Site source opening now succeeds;publication awaits completed packaging.\n',encoding='utf8')
print({'baselineReviewed':n,'remaining':60-n})
