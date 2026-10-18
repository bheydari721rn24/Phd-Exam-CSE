"""Register the single current author-reviewed game-search chapter after its gates."""
from pathlib import Path
from markdown_it import MarkdownIt
import hashlib, json, re, tempfile

R=Path(__file__).resolve().parents[1];B=R/'research'
def read(p):return json.loads((R/p).read_text(encoding='utf8'))
def write(p,d):(R/p).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
m=read('research/i_games-mathematics.json');b=read('research/i_games-evidence/browser.json')
printed=read('research/i_games-printed-code-exhaustive.json')
assert m['state']=='passed_current_manuscript_numeric_and_notation_checks'
assert b['status']=='passed_actual_browser_checks' and len(b['frames'])==815
assert all(not f['issues'] for f in b['frames']) and all(p['moved'] and p['stopped'] for p in b['playback'])
assert b['windowRoles']['classification']>0 and printed['assertions']==46560
assert m['nativeMathExpressions']==533 and m['modelBoundCertificates']==121
assert all(hashlib.sha256((B/p).read_bytes()).hexdigest()==sha for p,sha in m['inputSha256'].items()), 'Mathematical inputs changed after verification'
assert all(hashlib.sha256((R/p).read_bytes()).hexdigest()==sha for p,sha in b['inputSha256'].items()), 'Teaching page or simulation changed after browser verification'

p=B/'i_games-source-audit.md';s=p.read_text(encoding='utf8')
s=s.replace('Date: 17 October 2026. Authoring state: in progress. This is evidence for a chapter, not a delivered or student-approved chapter.',
            'Written scopes reviewed during 17 October 2026; final author review completed 18 October 2026. This edition remains a student-unapproved review draft.')
start=s.find('Before delivery: finish the complete original explanation')
if start>=0:
    end=s.index('\n\n## Exact references',start)
    s=s[:start]+'The delivered author-review edition contains eighteen teaching sections, fifty original/course problems, two inspected authentic MS reconstructions and sixty final decisions. The current mathematics, code, model and browser results are recorded in the [quality review](i_games-quality.html). The bounded source-reading and exercise-access limits above remain in force.'+s[end:]
p.write_text(s,encoding='utf8')

# Preserve acquisition history, but distinguish actual read scopes from fetched-only files.
cache=Path(tempfile.gettempdir())/'phd-game-sources-20261017'
records=[]
for file in cache.glob('*acquisition.json'):
    for d in json.loads(file.read_text(encoding='utf8')):
        if d.get('sha256'):records.append({k:d[k] for k in ['id','url','sha256','bytes'] if k in d})
selected={'stanford-modeling','stanford-minimax','stanford-alpha-beta-pruning','stanford-evaluation-functions','stanford-expectimax','stanford-expectiminimax','mit-transcript','cornell','cmu-adversarial','berkeley-expectimax','berkeley-mcts'}
unique={d['id']:d for d in records}
for key,d in unique.items():d['readingState']='documented_in_scope_written_body_read' if key in selected else 'acquisition_only_unless_separately_identified_in_audit'
write('research/i_games-source-ledger.json',{'date':'2026-10-18','candidateUniversities':7,
    'primaryUniversities':['Stanford','UC Berkeley','MIT','Cornell'],'additionalContribution':'CMU',
    'comparisonOnly':['Harvard','Yale-hosted AIMA'], 'documents':list(unique.values()),
    'webReaderScopesWithoutLocalFingerprint':['Berkeley minimax/evaluation and general-games full textbook bodies; Harvard adversarial-search section'],
    'exactScopeAuthority':'research/i_games-source-audit.md',
    'limits':'Fetched combined Stanford games1/games2 and indices are not counted as additional substantive readings. Local acquisition failures are retained in historical ledgers; an official written body read through the web reader need not have a local-byte fingerprint.'})
register=read('dist/course-audit-week1.en.json')
courses=[]
for key,university,course,url,evidence,advantage in [
    ('stanford','Stanford','CS221 Spring 2026 Games modules','https://stanford-cs221.github.io/spring2026/','https://stanford-cs221.github.io/spring2026/modules/games/minimax.js','Six complete written module bodies: model, minimax, evaluation, alpha-beta, expectimax and expectiminimax; precise policy and bound semantics.'),
    ('berkeley','UC Berkeley','CS188 Games textbook sections 3.2–3.5','https://inst.eecs.berkeley.edu/~cs188/textbook/games/minimax.html','https://inst.eecs.berkeley.edu/~cs188/textbook/games/monte-carlo.html','Full in-scope textbook prose for minimax/evaluation, expectation, general games and MCTS; unread source images are not copied.'),
    ('mit','MIT','6.034 Fall 2010, Patrick H. Winston','https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/','https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/7524b662aa86938e45c10c74d3a1ad41_STjW3eH0Cik.pdf','Complete 26-page Lecture 6 transcript: pruning explanations, distant-ancestor thresholds, progressive deepening and extensions.'),
    ('cornell','Cornell','CS4700 Fall 2018, Bart Selman','https://www.cs.cornell.edu/courses/cs4700/2018fa/','https://www.cs.cornell.edu/courses/cs4700/2018fa/lectures/pdf/CS4700-06-Search_adversarial_v2.pdf','All 56 extracted text pages and five named original page renders; independent minimax and cardinal-utility comparison.'),
    ('cmu','CMU','15-281 Fall 2025, Pat Virtue','https://www.cs.cmu.edu/~15281-f25/','https://www.cs.cmu.edu/~15281-f25/lectures/15281_F25_Lec4_Adversarial_Search.pdf','Fifth contribution: all 61 extracted text pages and named original diagrams; pruning polls, unequal chance weights and a known opponent.')]:
    courses.append(dict(id='i-games-'+key,subject='ai',university=university,course=course,url=url,evidence=evidence,topics=['i_games'],advantage=advantage,limit='Only the exact chapter-relevant written scope is claimed. See the seven-candidate source audit for image, exercise-access and attribution limits.',access='official_written_course_material',reviewLevel='reviewed_in_scope_written_sections'))
ids={c['id']for c in courses};register['courses']=[c for c in register['courses']if c['id']not in ids]+courses
register['reviewedAt']='2026-10-18';write('dist/course-audit-week1.en.json',register)

lessons=read('dist/lessons.json');week=next(w for w in lessons if w['week']==5)
entry=dict(topicId='i_games',title='Adversarial Search and Pruning',status='draft',statusLabel='New chapter: author review complete',
    revisionState='new_chapter_draft',url='chapters/i_games.html',questionCount=52,authenticQuestionCount=2,
    originalQuestionCount=50,examNotesCount=60,animationCount=19,animationWalkthroughCount=17,
    animationReviewState='reviewed_draft',sourceAuditUrl='reviews/i_games-sources.html',
    qualityAuditUrl='reviews/i_games-quality.html',studentApproved=False)
week['chapters']=[x for x in week['chapters'] if x['topicId']!='i_games']+[entry];write('dist/lessons.json',lessons)
available=[x for w in lessons for x in w.get('chapters',[])];assert len(available)==len({x['topicId']for x in available})==63
assert all((R/'dist'/x['url']).is_file()for x in available)
planned=len(read('dist/schedule.en.json')['topics']);assert planned==119
progress=read('research/deep-library-revision/progress.json')
progress.update(availableTechnicalChapters=63,plannedTechnicalChapters=119,newTechnicalChaptersRemaining=56,
    currentLibraryChapterCount=63,lastCompletedNewTechnicalChapter='i_games',nextNewTechnicalTopicId='i_csp',
    nextNewTechnicalTopic='i_csp',currentTopicId='l_rank')
progress.setdefault('newTechnicalDrafts',{})['i_games']={'state':'completed_author_review_draft','countedAsCompleted':True,'studentApproved':False}
progress['newChaptersCompletedSinceBaseline']=[{'topicId':k,'status':'author_review_complete_student_approval_pending','questions':v}for k,v in [('l_projection',52),('l_leastsquares',51),('i_games',52)]]
write('research/deep-library-revision/progress.json',progress)
gate=read('research/chapter-gate.json');gate.update(currentTopicId='l_rank',state='in_progress',nextReview='l_rank',
    lastCompletedNewTechnicalChapter='i_games',nextNewTechnicalTopicId='i_csp',currentDraftPath='research/l_rank.en.md',
    sourceAuditPath='research/i_games-source-audit.md',qualityAuditPath='research/i_games-quality-audit.md',
    activeWork='26 of 60 baseline reviews checked;34 remain.63 of 119 technical drafts exist;56 new chapters remain. Continue individual l_rank review, then i_csp authoring. Three IELTS lessons exist; learner mastery remains unconfirmed.',
    currentChapterPublicationState='games_and_complete_gauss_publication_pending')
gate['latestNewChapterReview']={'topicId':'i_games','manuscript':'research/i_games.en.md','evidence':'research/i_games-final-author-review.json','studentApproved':False}
write('research/chapter-gate.json',gate)
snapshot=read('research/continuation-status-20261017.json');snapshot.update(date='2026-10-18',availableTechnicalChapters=63,
    newTechnicalChaptersRemaining=56,nextExistingReview='l_rank',nextNewTechnicalChapter='i_csp',
    completedNewChaptersSinceBaseline=['l_projection','l_leastsquares','i_games'],
    sitePublication='games_and_complete_gauss_local_github_and_site_delivery_pending')
write('research/continuation-status-20261018.json',snapshot)

sys_path=B/'exam-rewrite'
import sys
sys.path.insert(0,str(sys_path));import mathml
mathml.wrap_display=lambda s:s
md=MarkdownIt('commonmark',{'html':True}).enable('table')
for source,target in [('i_games-source-audit.md','i_games-sources.html'),('i_games-quality-audit.md','i_games-quality.html')]:
    text=(B/source).read_text(encoding='utf8')
    body=mathml.markdown_math(text,md)
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Adversarial search review</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p><a href="../chapters/i_games.html">Read the chapter</a></p><article class="lesson">'+body+'</article></main></body></html>'
    (R/'dist/reviews'/target).write_text(page,encoding='utf8')
write('research/i_games-final-author-review.json',{'date':'2026-10-18','state':'author_review_complete_student_approval_pending',
    'questions':52,'teachingSections':18,'finalDecisions':60,'nativeMathExpressions':533,
    'treeModels':27,'treePlacements':17,'renderedCheckpoints':815,'numericAssertions':181,
    'printedAlgorithmAssertions':46560,'studentApproved':False,
    'pageSha256':hashlib.sha256((R/'dist/chapters/i_games.html').read_bytes()).hexdigest(),
    'evidence':['research/i_games-source-audit.md','research/i_games-source-ledger.json','research/i_games-mathematics.json','research/i_games-printed-code-exhaustive.json','research/i_games-evidence/browser.json'],
    'baselineReviewsComplete':26,'baselineReviewsRemaining':34,'technicalChaptersAvailable':63,'newTechnicalChaptersRemaining':56})
if '## Adversarial search author review completed: 18 October 2026'not in (R/'WEEKLY_DELIVERY.md').read_text(encoding='utf8'):
  with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf8')as f:
    f.write('\n\n## Adversarial search author review completed: 18 October 2026\n\nEighteen teaching sections, fifty original/course mathematical and conceptual problems, two inspected original MS trees and sixty final decisions. Seven university candidates compared; four primary written scopes and a fifth contribution used. The actual printed algorithm passed 46,560 bounded assertions; 181 problem/notation checks and 121 model certificates passed. All 815 rendered tree states, seventeen players, dedicated UCT/chance controls, fonts, mobile overview navigation and print presentation passed actual browser checks. Incoming, current and original classification windows are now explicitly distinguished.\n\nThe library contains63 actual technical chapters of119, leaving56 new chapters. The original60-chapter revision baseline remains26 reviewed and34 pending. IELTS still has three prepared lessons and unconfirmed student mastery. Next individual review:l_rank; next technical authoring:i_csp. No claim of new Site publication is made until a native success response is recorded.\n')
print({'state':'author_review_complete','available':63,'remainingNew':56,'baselineReviewed':26,'baselinePending':34})
