"""Deliver the existing-library revision after independent and browser checks."""
from pathlib import Path
import json,re,html,shutil,datetime
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'research/exam-rewrite'
m=json.loads((BASE/'manifest.json').read_text())
answers=json.loads((BASE/'answer-checks.json').read_text())
browser_source=Path('C:/Users/bheydari/AppData/Local/Temp/chapter-library-review')
browser=json.loads((browser_source/'browser-review.json').read_text())
assert {x['topicId'] for x in browser}=={x['topicId'] for x in m['chapters']}
assert len(browser)==22
assert all(x['mobile']['document']<=390 and not x['mobile']['formulaOverflow'] for x in browser)
assert all(not f['outside'] and not f['overlap'] for x in browser for f in x['figures'])
assert all(x['printStyle']['diagramOverflow']==0 for x in browser)
figures=sum(len(x['figures']) for x in browser)
assert figures==66 and answers['questions']==320 and answers['examinationNotes']==339
evidence=BASE/'evidence';evidence.mkdir(exist_ok=True)
for name in ['browser-review.json']+[f['screenshot'] for x in browser for f in x['figures']]+[p.name for p in browser_source.glob('*-questions.png')]+[p.name for p in browser_source.glob('*-notes.png')]+[p.name for p in browser_source.glob('*-exam-mobile.png')]:
 shutil.copy2(browser_source/name,evidence/name)
for name in ('report-review.json','report-1280.png','report-390.png','library-390.png'):
 if (browser_source/name).exists():shutil.copy2(browser_source/name,evidence/name)
old=ROOT/'dist/library-review.html';archived=BASE/'baseline/library-review.html'
if not archived.exists():shutil.copy2(old,archived)
lessons={c['topicId']:c for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']}
plan=json.loads((ROOT/'dist/schedule.en.json').read_text())
for t,c in lessons.items():c.setdefault('title',plan['topics'][t]['title'])
rows=[];chapter_log=[]
for c in m['chapters']:
 t=c['topicId'];s=(ROOT/'dist/chapters'/(t+'.html')).read_text(encoding='utf-8')
 headings=[(re.search(r'id="([^"]+)"',x)[1] if re.search(r'id="([^"]+)"',x) else '',re.sub('<[^>]+>','',x)) for x in re.findall(r'<h2\b[\s\S]*?</h2>',s)]
 bank=next(a for a,b in headings if b=='Formula and conceptual problem bank')
 notes=next(a for a,b in headings if b=='Applicable formulas and examination notes')
 source=next((a for a,b in headings if a and re.search('source|course',b,re.I)), 'references')
 methods=(BASE/(t+'.md')).read_text(encoding='utf-8').split('## Formula and conceptual problem bank')[0]
 names=re.findall(r'^### (.+)',methods,re.M)
 focus='; '.join(names)
 title=html.escape(lessons[t]['title']);url='chapters/'+t+'.html'
 count=len(next(x for x in browser if x['topicId']==t)['figures'])
 rows.append(f'<tr><td><a href="{url}">{title}</a><p>{html.escape(focus)}</p></td><td><a href="{url}#{bank}">{c["questionCount"]} questions</a><br><a href="{url}#{notes}">{c["notesCount"]} notes</a><br>{count} figures<br><a href="{url}#{source}">Sources and reading scope</a></td></tr>')
 chapter_log.append(f'- {lessons[t]["title"]}: {c["questionCount"]} new questions, {c["notesCount"]} examination notes, {count} figures. New solution methods: {focus}.')
report='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Examination Practice Revision · Doctoral CSE 1406</title><link rel="stylesheet" href="chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="index.html#library">← Chapter library</a></p><header class="hero"><p class="eyebrow">Whole-library revision · 3 October 2026</p><h1>Formula-solving instruction, conceptual questions and examination notes</h1><p>22 revised chapters · 320 new original questions · 339 applicable notes · 66 figures</p></header><article class="lesson">
<h2 id="changes">What changed in every chapter</h2>
<p>The previous examination banks and review sheets were rejected. Every existing chapter now has a newly written section that teaches how to recognize a question, translate its conditions into a calculation or logical decision, and derive the result. The new four-option question bank includes explicit assumptions, a justified answer and discussion of incorrect approaches. Forty-four of the 320 questions combine multiple steps or distinguish easily confused models.</p>
<p>The replacement notes state usable formulas, theorem conditions, boundary cases and concrete mistakes. They are chapter-specific, rather than a checklist of general study advice. Correct deep explanations, proofs, implementations and university exercise derivations remain available as detailed tutorials. This revision replaces the rejected banks and notes and extends the teaching; it does not claim that every correct sentence in the existing lessons needed replacement.</p>
<h2 id="chapters">Open the revised material</h2>
<p>Each question and notes link opens the relevant section directly. The full chapter contains the definitions, proofs, worked derivations, diagrams, laboratory where available and references.</p><table><thead><tr><th>Chapter and new solution methods</th><th>Revised sections and evidence</th></tr></thead><tbody>'''+''.join(rows)+'''</tbody></table>
<h2 id="visuals">Figures and mathematical presentation</h2>
<p>Twelve new numerical vector figures connect question data with the solution: three-set membership, probability masses, isolated-symbol gaps, vector projection, matrix multiplication cost, signed encodings, gate hazards, divisor orders, idempotent functions, congruences, recursion levels and convolution aliasing. The existing 54 useful figures are retained. All 66 SVG figures were captured in the browser and checked for labels outside the drawing or overlapping one another; no such findings remained.</p>
<p>Mathematics uses the bundled STIX Two Math font with native fractions, roots, subscripts, superscripts and summation limits. Body text uses Source Sans 3, headings use Newsreader, and code uses JetBrains Mono. Long display formulas break at meaningful operators; long inline expressions can scroll within their own line on narrow screens. Checks at a 390-pixel viewport found no page-wide or display-formula overflow. Print styles were checked for diagram fit; a paginated printed document was not produced.</p>
<h2 id="verification">What the checks establish</h2>
<p>All 22 revised banks passed structural checks for four distinct alternatives, an answer declaration and an explanation. Internal section links and unique figure identifiers were checked. Every native MathML expression passed XML and argument-arity checks. Independent enumerations, exact rational arithmetic, integer computations and execution models supplied 194 answer or property checks, including combinatorial counts, truth tables, projections, modular arithmetic and recurrence instances.</p>
<p>The 194 checks are not 320 independent proofs. They corroborate exact instances and expose inconsistencies; they do not establish universal theorems or asymptotic bounds by enumeration. Those statements require their stated mathematical derivations. C-language questions use explicit platform assumptions and the specified language rules; no C compiler execution is claimed. Browser geometry checks do not establish mathematical truth.</p>
<h2 id="sources">University sources and problem provenance</h2>
<p>The existing chapter source comparisons and recorded reading scopes are preserved. The lessons use at least four genuinely reviewed written university courses from four universities; additional reviewed sources remain where needed. This revision reuses those documented readings and does not claim a new exhaustive search of every university course. The 320 replacement questions are original, university-concept practice. Source exercise derivations retained as tutorials keep their original references; they are not relabeled as new original questions.</p>
<p>The <a href="https://web.stanford.edu/class/archive/cs/cs103/cs103.1198/handouts/extra-practice.html">Stanford CS103 extra-practice topic catalogue</a> was inspected for question families. Its linked exercise collections were not all read. The recurrence examples in <a href="https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/b06b8a8baf9b15f98947e75bae55b8bf_MIT6_006S20_ps2-solutions.pdf">MIT 6.006 Problem Set 2 solutions</a>, PDF pages 1–3, informed the comparison of exact, critical and boundary cases. Selected clauses 6.5, 6.5.3.3, 6.5.7 and 6.5.15 of the <a href="https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf">WG14 N1570 C draft</a> were checked for sequencing, promotions, shifts and conditional-expression typing. These are targeted reading statements, not claims that those complete documents were reread.</p>
<h2 id="limits">Remaining calibration and approval</h2>
<p>Under your earlier instruction, Iranian master's and doctoral examination archives remain deferred until the final month. These original questions are therefore not labeled as authentic past-exam items or empirically calibrated to the national examination's difficulty. The course-based range includes foundational, intermediate and integrative work, but success on every unseen question cannot be guaranteed.</p>
<p><strong>All 22 chapters remain examination revision drafts.</strong> Earlier approval does not approve the replacement sections. New chapters remain paused until you explicitly approve the revised material. Study progress checkmarks have been preserved.</p></article></main></body></html>'''
old.write_text(report,encoding='utf-8')
summary='# Whole-Library Examination Revision\n\n'+ '\n'.join(chapter_log)+'\n\n320 new original questions; 339 new applicable notes; 44 multi-step challenges; 12 new numerical figures; 66 figures checked. Independent answer/property checks: 194. All 22 revision drafts await explicit approval. Iranian exam archives remain deferred. See dist/library-review.html for evidence and limitations.\n'
(BASE/'DELIVERY.en.md').write_text(summary,encoding='utf-8')
m.update(state='awaiting_user_approval',completed='2026-10-03',questions=320,examinationNotes=339,figures=66,newFigures=12,independentAnswerChecks=194,browserAuditPath='research/exam-rewrite/evidence/browser-review.json',answerAuditPath='research/exam-rewrite/answer-checks.json',reportPath='dist/library-review.html')
(BASE/'manifest.json').write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
gate=json.loads((ROOT/'research/chapter-gate.json').read_text())
gate.update(state='awaiting_user_approval',nextTopicId=None,proposedNextTopicId=None,reviewScope='All 22 existing chapters: revised formula-solving instruction, problem banks and examination notes.',lastCompletedReview='All 22 existing chapters revised; 320 original questions, 339 examination notes, 66 figures; 194 independent finite answer/property checks; mobile, diagram labels and print-style geometry passed.',nextReview='Wait for explicit student approval of the whole-library examination revision; do not start a new topic.',libraryReviewReportPath='research/exam-rewrite/DELIVERY.en.md',revisionTracker='research/exam-rewrite/manifest.json',approvedLibraryReview=False)
(ROOT/'research/chapter-gate.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
weekly=ROOT/'WEEKLY_DELIVERY.md';text=weekly.read_text(encoding='utf-8')
marker='\n## Authoritative whole-library examination revision\n'
text=text.split(marker)[0]+marker+'\n2026-10-03: The explicit whole-library rewrite supersedes older delivery counts and approval states below. All 22 existing chapters remain revision drafts. No new topic may start until explicit approval of this revision. Current evidence and delivery: research/exam-rewrite/manifest.json, DELIVERY.en.md, answer-checks.json and evidence/browser-review.json. App report: dist/library-review.html. Previous Iranian exam-archive deferral remains active. Do not reset study progress.\n\nThe authoritative rebuild is research/rebuild_exam_library.py using research/exam-rewrite/baseline and the new authored chapter files. Run it after any legacy builder. Never publish a legacy builder’s output alone. See research/exam-rewrite/README.md for the complete generation and validation sequence.\n'
weekly.write_text(text,encoding='utf-8')
print('Finalized 22 revision drafts and the current report; approval gate closed to new topics.')
