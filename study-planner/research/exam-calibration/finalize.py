"""Publishable review, explicit provenance, and approval gate for this revision."""
import sys,json,re,html,shutil,collections
from pathlib import Path
BASE=Path(__file__).resolve().parent; ROOT=BASE.parents[1]
sys.path.insert(0,str(BASE))
from build import text,source_link
e=html.escape
m=json.loads((BASE/'manifest.json').read_text())
actual=json.loads((BASE/'actual-items.json').read_text())
valid=[q for q in actual if q['answer'] is not None]
excluded=[q for q in actual if q['answer'] is None]
checks=json.loads((BASE/'answer-validation.json').read_text())
expansion=json.loads((BASE/'expansion-validation.json').read_text())
out=Path('C:/Users/bheydari/AppData/Local/Temp/chapter-library-review')
browser=json.loads((out/'browser-review.json').read_text())
assert len(browser)==22 and all(x['mobile']['document']<=390 and not x['mobile']['formulaOverflow'] for x in browser)
assert all(x['mobile']['problems']==next(c['totalQuestions'] for c in m['chapters'] if c['topicId']==x['topicId']) for x in browser), 'Browser evidence must reflect the expanded bank counts.'
import hashlib
assert all(hashlib.sha256((BASE/name).read_bytes()).hexdigest()==value for name,value in expansion['inputHashes'].items()), 'Answer evidence must match the current authored inputs.'
assert all(not f['outside'] and not f['overlap'] for x in browser for f in x['figures'])
assert all(x['printStyle']['diagramOverflow']==0 for x in browser)
assert sum(len(x['figures']) for x in browser)==m['figures']
evidence=BASE/'evidence'; evidence.mkdir(exist_ok=True)
shutil.copy2(out/'browser-review.json',evidence/'browser-review.json')
for screenshot in out.glob('*.png'):shutil.copy2(screenshot,evidence/screenshot.name)
if (out/'report-review.json').exists():shutil.copy2(out/'report-review.json',evidence/'report-review.json')
public=ROOT/'dist/evidence/exam-calibration'; public.mkdir(parents=True,exist_ok=True)
for name in ('manifest.json','answer-validation.json','expansion-validation.json','tripling-baseline.json'):
 shutil.copy2(BASE/name,public/name)
shutil.copy2(out/'browser-review.json',public/'browser-review.json')

def page(title,body):
 return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+e(title)+' · Doctoral CSE 1406</title><link rel="stylesheet" href="chapters/chapter.en.css"><link rel="stylesheet" href="chapters/exam-calibration.css"></head><body><main class="chapter"><p class="top-link"><a href="index.html#library">← Chapter library</a></p><header class="hero"><p class="eyebrow">Exam-grounded revision · 3 October 2026 · awaiting approval</p><h1>'+e(title)+'</h1></header><article class="lesson">'+body+'</article><script src="chapters/exam-calibration.js"></script></main></body></html>\n'

body='<h2>What is now in the problem banks</h2><p>All 22 existing chapters have been revised. Each bank separates authentic examination questions, original formula and conceptual analogues, and two retained integrated challenges. Every chapter now has at least three times its version-55 question count. Each item states its assumptions, gives four alternatives, and explains the calculation or conceptual decision. Worked solutions identify mistaken approaches and conditions that change the answer.</p>'
body+=f'<p><strong>{m["authenticUniqueItems"]} distinct authentic questions</strong> appear {m["authenticChapterOccurrences"]} times across related chapters. Reuse is identified by the same source question number; these are not {m["authenticChapterOccurrences"]} different past-exam questions. The banks also contain <strong>{m["newOriginalItems"]} original analogues</strong> (176 from version 55 and 736 added in this revision) and <strong>{m["retainedOriginalChallenges"]} retained original challenges</strong>. This gives <strong>{m["totalQuestions"]} chapter-level problem entries</strong>. The 339 examination notes, deep university instruction, proofs, laboratory activities and course-source comparisons remain available.</p>'
body+='<p>The 736 added questions form 184 explicitly related families: two numerical instances, one symbolic generalization and one applicability or counterexample question per family. They are not 736 unrelated concepts. Chapter family menus let you choose a model without searching a long page. Difficulty is qualitative; many exact calculations provide medium-level preparation and scope questions develop conceptual discrimination.</p>'
body+='<p>Read the theory and derivation tutorials first. Then open the problem bank, attempt a question on paper, and expand its complete solution. Compare the method with the stated transfer rule or distractor analysis. Printing opens the solutions automatically and restores their previous states afterward. No learner test is requested as part of this delivery.</p>'
body+='<h2>Read the revised banks</h2><p>The source items are English translations with the original option numbering. Each link identifies the year, field, question number, PDF page and immutable repository revision.</p><table><thead><tr><th>Chapter</th><th>Before → now / minimum</th><th>Problem bank and sources</th></tr></thead><tbody>'
for c in m['chapters']:
 link='chapters/'+c['topicId']+'.html'
 body+='<tr><td><a href="'+link+'">'+e(c['title'])+'</a></td><td>'+str(c['baselineQuestions'])+' → <strong>'+str(c['totalQuestions'])+'</strong><br>Required minimum: '+str(c['minimumQuestions'])+'</td><td><a href="'+link+'#authentic-questions">'+str(c['authenticQuestions'])+' authentic questions</a><br><a href="'+link+'#original-analogues">'+str(c['newOriginalQuestions'])+' original analogues</a><br><a href="'+link+'#integrated-challenges">2 integrated challenges</a><br><a href="'+link+'#'+c['notesId']+'">'+str(c['notes'])+' examination notes</a><br><a href="'+link+'#exam-references">Exam references</a><br>'+str(c['figures'])+' figures</td></tr>'
body+='</tbody></table><h2>How the examination patterns shaped the revision</h2><ul><li><strong>Discrete mathematics:</strong> model counts, quantifier order, restrictions in counting, equivalence classes, periodic recurrences and modular constraints.</li><li><strong>Algorithms:</strong> exact comparison counts, loop regions, unequal or nonlinear recurrence arguments, boundary conditions of asymptotic theorems, and combine costs.</li><li><strong>Probability:</strong> precisely stated events, conditional denominators, sampling models, and counting under multiple restrictions.</li><li><strong>Linear algebra:</strong> independence at exceptional parameter values, rank, coordinate conventions, projection and nilpotent matrix powers.</li><li><strong>Programming and digital logic:</strong> numeric representation, intermediate rounding, defined language behavior, Boolean equivalence and circuit connectivity. Cross-topic placements are disclosed rather than relabeled as exact language-rule matches.</li></ul>'
body+='<h2>Source scope and exclusions</h2><p>The repository inventory contains 84 PDFs. This revision is a question-level selection from eight practice-bearing booklets, including additional records examined for source defects. It is not a claim that all 84 PDFs or every question in those booklets has been read. Selected source pages were rendered and compared with the translations, options and diagrams. The <a href="exam-source-audit.html">source-ambiguity audit</a> documents three records excluded from the single-answer practice banks.</p><p>Solutions are independently derived; they are not represented as verified official answer keys. Original-question difficulty labels are author-assessed medium or hard, without student-response statistics. Authentic questions preserve the source difficulty, including prerequisite checks. The latest instruction authorizes using past examination questions now and supersedes the earlier final-month deferral.</p>'
body+='<h2>Scientific and presentation checks</h2><p>'+str(checks['independentChecks'])+' existing finite, exact-arithmetic and output-consistency checks support the calculations and record counts. The expanded bank additionally passed 368 numeric-answer recomputations using separate finite models, state transitions and exact algebra; each recomputed value is bound to its selected alternative. All 22 individual count targets passed. Symbolic derivations and scope statements received editorial review; neither count checks nor numeric recomputation prove all general statements or difficulty labels. The 22 chapter pages were reviewed with all worked solutions open at a 390-pixel viewport: no page-wide or display-formula overflow remained. All 70 figure instances passed label-boundary, label-overlap and print-style fit checks. Two authentic circuit topologies were redrawn as four English SVG instances across their relevant chapters.</p><p>Body text uses Source Sans 3, headings use Newsreader, mathematics uses STIX Two Math, and code uses JetBrains Mono. Long mathematical expressions keep their complete scope and break at meaningful operators. Print-style fit checks are not verification of every possible printer or paginated PDF layout.</p><p><a href="evidence/exam-calibration/manifest.json">Chapter counts and source IDs</a> · <a href="evidence/exam-calibration/answer-validation.json">Existing checks</a> · <a href="evidence/exam-calibration/expansion-validation.json">Expanded-answer and count checks</a> · <a href="evidence/exam-calibration/tripling-baseline.json">Frozen version-55 baseline</a> · <a href="evidence/exam-calibration/browser-review.json">Browser and figure checks</a></p>'
body+='<h2>Approval and remaining limits</h2><p><strong>All 22 chapters remain revision drafts pending explicit approval.</strong> No new chapter has been started. Study-progress checkmarks are preserved. University teaching retains the existing recorded comparisons of at least four reviewed written courses from four universities per chapter; this bank revision does not claim a fresh exhaustive review of all university courses worldwide. A finite collection of lessons and problems cannot guarantee answers to every unseen examination question.</p>'
(ROOT/'dist/library-review.html').write_text(page('Expanded formula and conceptual examination banks',body),encoding='utf-8')

audit='<p>These records are retained for source criticism, not counted as practice questions. Ambiguous assumptions, missing correct alternatives and alternative valid implementations must not be silently repaired. No official-key verification is claimed.</p>'
for q in excluded:
 audit+='<section class="exam-question"><h2>'+e(q['id'].replace('_',' '))+' — '+e(q['title'])+'</h2><p><a href="'+e(source_link(q))+'">Original PDF · page '+str(q['pdfPage'])+' · Q'+str(q['questionNumber'])+'</a></p>'+text(q['stem'])+'<ol>'+''.join('<li>'+text(x)+'</li>' for x in q['options'])+'</ol><h3>Independent audit and practice decision</h3>'+text(q['solution'])+'</section>'
audit+='<p><a href="library-review.html">Return to the revised chapter banks</a></p>'
(ROOT/'dist/exam-source-audit.html').write_text(page('Excluded and assumption-sensitive source questions',audit),encoding='utf-8')
(ROOT/'dist/exam-audit.html').write_text(page('Entrance-examination archive and question provenance','<p>Past MSc and PhD examination questions are included now under the instruction of 3 October 2026. The earlier final-month deferral is superseded. A repository inventory is distinct from a record of pages actually read.</p><p><a href="library-review.html">Open the 22 revised banks and verification report</a> · <a href="exam-source-audit.html">Read the source-defect audit</a></p>'),encoding='utf-8')

# Remove only stale examination-deferral sentences, not unrelated study-calendar language.
for p in (ROOT/'dist').rglob('*'):
 if not p.is_file() or p.suffix not in ('.html','.js','.json'):continue
 s=p.read_text(encoding='utf-8')
 s=re.sub(r'[^<>.\n"\x27]*?(?:Iranian|entrance-exam|entrance-examination)[^<>.\n"\x27]*?(?:final month|final-month|final study month)[^<>.\n"\x27]*\.', ' Original MSc and PhD examination questions are included in the revised chapter banks.',s,flags=re.I)
 s=s.replace('Do not use entrance-exam booklets before the final month.', 'Use the attributed examination questions in the current chapter banks after reading the theory.')
 if p.name=='app.en.js':
  s=s.replace('${chapter.questionCount || 0} original questions with explanations', '${chapter.authenticQuestionCount || 0} authentic questions · ${chapter.originalQuestionCount || 0} original problems with explanations')
 p.write_text(s,encoding='utf-8')

log='# Source reading log — question-level review\n\nRepository revision: '+m['archiveCommit']+'. Inventory: 84 PDFs. This is not an exhaustive reading claim.\n\n'
for book in sorted({q['booklet'] for q in actual}):
 qs=[q for q in actual if q['booklet']==book]
 log+='## '+book+'\n\nRendered PDF pages checked: '+', '.join(str(n) for n in sorted({q['pdfPage'] for q in qs}))+'.\n\n'
 log+='Question records: '+', '.join(str(q['questionNumber'])+(' (excluded)' if q['answer'] is None else '') for q in qs)+'.\n\n'
log+='The translated stems and alternatives were compared with the rendered pages. Independent solutions were derived separately. The diagrams for Phd_CE_1405_Q23 and MS_CE_1404_Q80 were redrawn in English with their original connectivity. Unselected questions and unpublished/unavailable course materials are outside this reading claim.\n'
(BASE/'READING_LOG.en.md').write_text(log,encoding='utf-8')
delivery=f'# Exam-grounded library revision — delivery draft\n\n22 chapters; {m["authenticUniqueItems"]} distinct authentic questions, {m["authenticChapterOccurrences"]} authentic placements, {m["newOriginalItems"]} original authored analogues, {m["retainedOriginalChallenges"]} retained challenges; {m["totalQuestions"]} total problem entries; 339 examination notes; 70 figure instances.\n\nThe latest instruction supersedes archive deferral. Every source question has original options, PDF page, year, field, immutable commit and an independent worked solution. Three ambiguous/defective records are excluded and documented. Difficulty for original questions is qualitative.\n\n'+str(checks['independentChecks'])+' existing finite/exact and output checks, plus 368 expanded numeric recomputations, passed. The 22 pages and 70 figures passed mobile and print-style geometry checks. These checks do not prove universal correctness or unseen-exam performance.\n\nUser-facing report: dist/library-review.html. Source audit: dist/exam-source-audit.html. Sources: actual-items.json and READING_LOG.en.md. The 736 additions comprise 184 related four-question families; this is not a claim of 736 independent concepts. Authoring: original-*.json, author_*.py and expand_*.py. Audit: verify_answers.py and verify_expansion.py. Reauthor: clean_authoring.py regenerates both the earlier banks and all five expansion collections. Rebuild: research/rebuild_exam_library.py applies the calibration overlay after the legacy banks.\n\nAll chapters remain drafts. Await explicit approval before promoting this revision or starting another chapter. Preserve study progress.\n'
(BASE/'DELIVERY.en.md').write_text(delivery,encoding='utf-8')
gate=ROOT/'research/chapter-gate.json';g=json.loads(gate.read_text())
g.update(state='awaiting_user_approval',lastCompletedReview=f'Exam-grounded banks in all 22 chapters: {m["authenticUniqueItems"]} unique authentic items, {m["newOriginalItems"]} original analogues, {m["retainedOriginalChallenges"]} retained challenges, {m["totalQuestions"]} problem placements, 184 added families, 368 numeric recomputations, 70 figures; '+str(checks['independentChecks'])+' finite/exact and output checks.',revisionTracker='research/exam-calibration/manifest.json',libraryReviewReportPath='research/exam-calibration/DELIVERY.en.md',libraryRewritePath='research/exam-calibration/manifest.json',nextReview='Await explicit approval of the tripled problem-bank revision. Do not start a new chapter.',reviewScope='At least three times the version-55 question count in every one of the 22 existing problem banks; authentic MSc/PhD items plus original medium/hard formula and conceptual analogues.')
gate.write_text(json.dumps(g,indent=2)+'\n')
weekly=ROOT/'WEEKLY_DELIVERY.md';s=weekly.read_text(encoding='utf-8')
marker='## Completed exam-grounded problem banks'
if marker in s:s=s[:s.index(marker)].rstrip()+'\n'
weekly.write_text(s+'\n'+marker+'\n\n'+delivery.split('\n\n',1)[1],encoding='utf-8')
# Hashes must describe the final pages after policy normalization.
import hashlib
for c in m['chapters']:c['htmlSha256']=hashlib.sha256((ROOT/'dist/chapters'/(c['topicId']+'.html')).read_bytes()).hexdigest()
(BASE/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
shutil.copy2(BASE/'manifest.json',public/'manifest.json')
print('Prepared report, source audit, reading log, evidence and approval gate.')
