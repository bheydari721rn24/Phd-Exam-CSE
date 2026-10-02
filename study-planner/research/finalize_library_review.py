"""Record the completed reading and successful rebuilt checks, preserving evidence."""
from pathlib import Path
import hashlib,json,shutil,tempfile
root=Path(__file__).resolve().parents[1]
qa=Path(tempfile.gettempdir())/'chapter-library-review'
p=root/'research/library-review.json';d=json.loads(p.read_text(encoding='utf-8'))
checks=json.loads((root/'research/library-review-checks.json').read_text())
browser=json.loads((qa/'browser-review.json').read_text())
assert len(d['chapters'])==len(browser)==16
assert d['semanticChaptersReviewed']==16
assert len(checks)==20 and all(c['exitCode']==0 for c in checks)
assert sum(len(x['figures']) for x in browser)==29
assert sum(x['mobile']['problems'] for x in browser)==446
for row in browser:
 assert row['mobile']['document']<=390 and not row['mobile']['formulaOverflow']
 assert row['printStyle']['diagramOverflow']==0
 assert 'STIX Two Math' in row['fonts']['loaded']
 assert all(not f['outside'] and not f['overlap'] for f in row['figures'])
for chapter in d['chapters']:
 assert chapter['semanticReview'].startswith('complete')
 for s in chapter['manuscripts']:
  assert hashlib.sha256((root/s['path']).read_bytes()).hexdigest()==s['reviewedSha256']
 chapter['semanticReview']='complete'
 chapter['diagramReview']='complete: baseline visual/semantic reading; rebuilt geometry checks; corrected figures visually reinspected'
 chapter['renderedSha256']=hashlib.sha256((root/'dist'/chapter['renderedPath']).read_bytes()).hexdigest()
 audit=root/'research'/f"{chapter['topicId']}-quality-audit.md"
 if not audit.exists():audit=root/'research'/f"{chapter['topicId']}-en-quality-audit.md"
 assert audit.exists(),audit
 addition='\n\n## Final existing-library revision — 2026-10-02\n\nThe full authored manuscripts, every worked answer, final rules, and diagram context were reread during the sixteen-chapter revision. Findings: '+ ' '.join(chapter['findings']) +' All identified findings were corrected before rebuilding. The rebuilt chapter passed the recorded finite checks, desktop/mobile geometry, font loading, and print-style diagram-width checks. This is evidence of the performed review, not a universal correctness guarantee or a new full reading of every source course. See `LIBRARY_FINAL_REVIEW.en.md` and `library-review.json`.\n'
 if '## Final existing-library revision' not in audit.read_text(encoding='utf-8'):
  with audit.open('a',encoding='utf-8') as f:f.write(addition)
evidence=root/'research/library-review-evidence';evidence.mkdir(exist_ok=True)
for file in qa.glob('*.png'):shutil.copy2(file,evidence/file.name)
for name in ('browser-review.json','report-review.json'):shutil.copy2(qa/name,evidence/name)
d.update(state='complete',completed='2026-10-02',workedProblemsReviewed=446,figuresReviewed=29,
 manuscriptFilesReviewed=sum(len(c['manuscripts']) for c in d['chapters']),
 reportPath='research/LIBRARY_FINAL_REVIEW.en.md',reportUrl='library-review.html',
 verificationScriptsPassed=20,evidenceDirectory='research/library-review-evidence',
 lastCheckpoint='All sixteen existing chapters fully read and revised; 446 worked solutions and 29 figures reviewed. All identified findings corrected, rebuilt, checked, and recorded.')
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
gate=root/'research/chapter-gate.json';g=json.loads(gate.read_text(encoding='utf-8'))
g.update(state='awaiting_user_approval',activeWork='Final existing-library revision completed and delivered; no new chapter in progress.',
 lastCompletedReview=d['lastCheckpoint'],nextReview='Await explicit student approval of the revised library and direction to begin the next chapter.',
 libraryReviewReportPath='research/LIBRARY_FINAL_REVIEW.en.md',nextTopicId=None)
gate.write_text(json.dumps(g,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
handoff=root/'WEEKLY_DELIVERY.md';text=handoff.read_text(encoding='utf-8');heading='## Current chapter handoff'
assert heading in text
text=text.split(heading)[0]+heading+'''\n\n2026-10-02: The student approved g_gates and requested a final review of all existing chapters. That review is complete: all 16 chapters, 33 authored manuscript files, 446 worked solutions, end rules, and 29 figures were read and audited. Identified mathematical, explanatory, diagram, and typography findings were corrected. All chapters were rebuilt; 20 verification scripts, local-link/math-typography checks, and desktop/mobile/print-style browser checks passed. Exact findings and source hashes are recorded in research/library-review.json; the readable report is research/LIBRARY_FINAL_REVIEW.en.md and dist/library-review.html. Final evidence is in research/library-review-evidence.\n\nThe existing chapters remain approved and available. The gate is awaiting_user_approval for the revised-library handoff; no new chapter is in progress. Wait for explicit approval/direction before beginning the next chapter. Archived Iranian examinations remain deferred until the final month. Do not infer universal correctness or a complete new reading of all source courses from this revision.\n'''
handoff.write_text(text,encoding='utf-8')
print(json.dumps({k:d[k] for k in ('state','semanticChaptersReviewed','manuscriptFilesReviewed','workedProblemsReviewed','figuresReviewed','verificationScriptsPassed')}))
