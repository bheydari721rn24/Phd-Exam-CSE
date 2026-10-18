"""Register only a completed, evidenced author-review edition."""
from pathlib import Path
import json,re,shutil
from markdown_it import MarkdownIt
from teaching_prose_spacing import fix
R=Path(__file__).resolve().parents[1];B=R/'research';D=R/'dist';E=B/'deep-library-revision'
def load(p):return json.loads(p.read_text(encoding='utf8'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
qa=load(E/'l_functions-current-evidence/browser.json');assert qa['status']=='passed_functions_current_revision_browser_checks'
assert load(E/'p_functions-current-mathematics.json')['status'].startswith('passed')
p=D/'chapters/p_functions.html';s=p.read_text(encoding='utf8')
if 'href="#proof-method"'not in s:s=s.replace('<a href="#problems">Problems</a>','<a href="#proof-method">Proof method</a> <a href="#problems">Problems</a>')
s=s.replace('p_functions.css"','p_functions.css?v=review-20261018"');p.write_text(fix(s),encoding='utf8')
p=E/'progress.json';v=load(p);chapter=next(x for x in v['chapters']if x['topicId']=='p_functions');chapter.update(state='revised_checked_review_draft',revisionEvidence='research/deep-library-revision/p_functions-current-review.md');v.update(revisedChapters=28,pendingChapters=32,currentTopicId='p_arrays',nextIndividualReview='p_arrays');save(p,v)
p=D/'lessons.json';v=load(p);chapter=next(c for w in v for c in w['chapters']if c['topicId']=='p_functions');chapter.update(status='draft',statusLabel='Individually reviewed edition · awaiting student approval',revisionState='revised_checked_review_draft',studentApproved=False,qualityAuditUrl='reviews/p_functions-current-review.html',animationWalkthroughCount=27,problemAnimationCount=27,visualRevisionState='author_review_complete_student_approval_pending',animationReviewState='author_review_complete_student_approval_pending',libraryDecisionRevisionState='author_review_complete_student_approval_pending');save(p,v)
p=B/'chapter-gate.json';v=load(p);v.update(currentTopicId='p_arrays',state='in_progress',currentIndividualReviewComplete=False,currentReviewedAnswerBlocks=0,lastCompletedReview='p_functions: all 91 answers, 80 rules, 27 exact question aids and editable-lab/source/math/browser gates passed.',nextReview='p_arrays',lastCompletedReviewEvidence='research/deep-library-revision/p_functions-current-review.md',currentDraftPath='research/p_arrays.en.md',currentAnswerEvidence='research/deep-library-revision/p_functions-current-mathematics.json',activeWork='28 of 60 baseline reviews complete; 32 remain. 64 of 119 technical drafts exist; 55 new remain. Functions author review complete; next Arrays. CSP and Functions await confirmed Site upload. Three IELTS lessons exist; mastery unconfirmed.');save(p,v)
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def report(name,source):
    markup=md.render(source)
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Functions chapter review</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/p_functions.html">Functions chapter</a></p><article class="lesson">'+markup+'</article></main></body></html>'
    (D/'reviews'/name).write_text(fix(page),encoding='utf8')
review=(E/'p_functions-current-review.md').read_text(encoding='utf8')
report('p_functions-current-review.html',review);report('p_functions-quality.html',review)
sources=(B/'p_functions-source-audit.md').read_text(encoding='utf8')+'\n\n## Current source-reading refresh\n\n'+(E/'p_functions-source-revalidation-20261018.md').read_text(encoding='utf8')+'\n\n'+(E/'p_functions-supplementary-source-refresh.en.md').read_text(encoding='utf8')
report('p_functions-sources.html',sources)
public=D/'evidence/p_functions';public.mkdir(exist_ok=True)
for src,dest in [(E/'p_functions-current-mathematics.json','current-mathematics.json'),(E/'l_functions-current-evidence/browser.json','current-browser.json'),(E/'p_functions-answer-integration.json','answer-integration.json')]:shutil.copyfile(src,public/dest)
p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf8');s+='\n\n## Functions individual review — 18 October 2026\n\nCompleted the English author review of all 91 solutions, 80 decision rules and 27 actual-input question aids. Source, original-PDF, numerical and browser checks are recorded in research/deep-library-revision/p_functions-current-review.md. This edition awaits student approval. Baseline progress is 28/60 reviewed; technical inventory remains 64/119. Next existing review is p_arrays; next new authoring is i_informed. CSP and this revision require a confirmed private Site upload; latest confirmed online version remains 110 until a successful deployment result is recorded.\n';p.write_text(s,encoding='utf8')
print('Registered Functions author review; 28 baseline reviews complete, 32 remain.')
