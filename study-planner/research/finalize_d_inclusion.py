"""Finalize only the new inclusion-exclusion chapter from observed receipts."""
from pathlib import Path
import json, hashlib, shutil
B=Path(__file__).resolve().parent
R=B.parent
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def write(p,a): p.write_text(json.dumps(a,indent=2)+'\n',encoding='utf-8')
v=read(B/'d_inclusion-verification.json')
b=read(B/'d_inclusion-browser-audit.json')
assert v['state']==b['state']=='passed'
assert v['retainedQuestions']==1835 and v['retainedChapters']==32
assert b['counts']['questions']==82 and b['counts']['rules']==80
assert len(b['labReferenceChecks'])==308 and all(x['actual']==x['expected'] for x in b['labReferenceChecks'])
assert len(b['invalidCalls'])==7 and all(b['invalidCalls'])
assert b['print']['checkpoints']==56 and not b['errors']
assert not b['mobile']['mathOverflow'] and b['mobile']['badAnchors']==0
assert b['realMotion']>0 and b['reducedMotion']
p=B/'d_inclusion-quality-audit.md';s=p.read_text(encoding='utf-8')
start=s.index('## Verification in progress') if '## Verification in progress' in s else s.index('## Observed verification')
end=s.index('## Authentic archive boundary',start)
s=s[:start]+'''## Observed verification

The independent mathematical verifier passed 1,267 assertions. Every numerical question-bank answer is checked by separately implemented map/permutation enumeration, integer predicate evaluation, a digit-mask dynamic program, bounded occupancy convolution, rank-occupancy dynamic programming or compatible-adjacency state counting. Symbolic identities have general written proofs and finite identity checks. All 32 earlier chapter bodies and their 1,835 question entries are retained. The earlier counting header alone records the student's explicit approval.

The actual Edge browser audit passed on this chapter. It inspected 82 solved tasks, 80 complete examination rules, 13 distinct models and all 56 checkpoints, including measured text bounds and overlaps. It checked 308 lab cases against independent Python reference counts and seven rejected invalid inputs. Actual moving animations, restart, previous/next, seeking, speed and playback controls were exercised. Reduced-motion mode had no motion animations. Source Sans 3, Newsreader, STIX Two Math and JetBrains Mono actually loaded; 610 native MathML instances include the printable model checkpoints.

At a 390-pixel viewport, the measured document and body width were both 375 pixels, with no overflowing mathematical expressions or underlined links. Wide diagrams have an explicit internal horizontal pan and the pan was exercised. Print mode opened all 82 complete solutions and exposed all 56 checkpoint drawings; interactive controls were hidden, and solution states were restored afterwards. The real application Library link, draft label and approved-library notice were reachable. No runtime or resource errors were observed. These are finite observed checks, not a certification of every possible browser or mathematical input.

Machine-readable evidence: [mathematical verification](../evidence/d_inclusion/verification.json), [browser interactions](../evidence/d_inclusion/browser.json), [model contracts](../evidence/d_inclusion/models.json), and [reviewed courses](../evidence/d_inclusion/courses.json).

'''+s[end:]
p.write_text(s,encoding='utf-8')
p=B/'d_inclusion-model-audit.json';a=read(p)
a.update(state='passed',verificationPath='research/d_inclusion-verification.json',browserAuditPath='research/d_inclusion-browser-audit.json',observedAssertions=v['checks'],labReferenceCases=308,limitations='Finite checks supplement general proofs; the model contracts and bounded input ranges delimit the claims.')
write(p,a)
p=B/'chapter-gate.json';g=read(p)
g.update(currentTopicId='d_inclusion',state='awaiting_user_approval',approvedTopicId='d_counting',nextTopicId='d_pigeonhole',proposedNextTopicId='d_pigeonhole',nextTopicRequiresExplicitApproval=True,sourceAuditPath='research/d_inclusion-source-audit.md',sourceAudit='research/d_inclusion-source-audit.md',qualityAuditPath='research/d_inclusion-quality-audit.md',qualityAudit='research/d_inclusion-quality-audit.md',activeWork='Delivered the sole new inclusion-exclusion review draft: 82 worked tasks, 80 examination rules, 13 dedicated concept traces and four editable labs.',reviewScope='Only d_inclusion; all 32 prior chapters explicitly approved.',lastCompletedReview='d_inclusion: 1267 independent mathematical assertions, 308 browser lab reference cases, all 56 checkpoint label layouts, mobile, font, motion and print checks passed.',nextReview='Wait for explicit student approval of d_inclusion. Do not start d_pigeonhole or any other chapter.',reviewEvidence=['research/d_inclusion-verification.json','research/d_inclusion-browser-audit.json','research/d_inclusion-model-audit.json'])
write(p,g)
p=B/'animation-manifest.json';a=read(p)
for c in a['chapters']:
 if c['topicId']!='d_inclusion':
  c['visualRevisionState']='student_approved'
  c['htmlSha256']=hashlib.sha256((R/'dist/chapters'/(c['topicId']+'.html')).read_bytes()).hexdigest()
a['chapters']=[c for c in a['chapters'] if c['topicId']!='d_inclusion']
models=read(R/'dist/chapters/d_inclusion-models.json')
a['chapters'].append(dict(topicId='d_inclusion',placements=13,scenarios=13,sections=models['groups'],questionCount=82,htmlSha256=hashlib.sha256((R/'dist/chapters/d_inclusion.html').read_bytes()).hexdigest(),visualRevisionState='awaiting_user_approval',renderer='Dedicated inclusion-exclusion SVG traces and four bounded enumerating labs',dataUrl='chapters/d_inclusion-models.json',modelAuditPath='research/d_inclusion-model-audit.json',browserAuditPath='research/d_inclusion-browser-audit.json'))
a.update(state='32_approved_chapters_and_one_inclusion_review_draft',uniqueScenarios=234,checkpoints=1343,placements=197,scope='206 approved legacy models, 15 approved counting models, and 13 inclusion-exclusion draft models. Mathematical proofs remain authoritative.',inclusionValidationAssertions=v['checks'],checkpointsPrint='Legacy players retain printable current or initial checkpoints; counting prints all 76 and inclusion-exclusion prints all 56 checkpoints.')
assert len(a['chapters'])==33 and sum(c['questionCount'] for c in a['chapters'])==1917
write(p,a)
p=R/'dist/index.html';s=p.read_text(encoding='utf-8')
s=s.replace('The visual and mathematical revision of all 31 existing chapters is student-approved. The new counting chapter is ready for your review.','All 32 earlier chapters are student-approved. The new inclusion-exclusion chapter is ready for your review.')
p.write_text(s,encoding='utf-8')
p=R/'dist/animation-review.html';s=p.read_text(encoding='utf-8')
s=s.replace('31 approved chapters and 1 counting review draft · 221 distinct scenarios · 1287 exact checkpoints · 184 embedded walkthroughs.','32 approved chapters and 1 inclusion-exclusion review draft · 234 distinct scenarios · 1343 exact checkpoints · 197 embedded walkthroughs.')
s=s.replace('Counting chapter: separate review draft','Counting chapter: student-approved in version 68').replace('The counting chapter remains a draft pending explicit approval.','The student explicitly approved the counting chapter in version 68.')
s=s.replace('animated teaching in 31 existing chapters','animated teaching in 32 existing chapters')
if '<!-- INCLUSION REVIEW -->' not in s:
 s=s.replace('<h2>Approval</h2>','<!-- INCLUSION REVIEW --><h2>Inclusion-exclusion chapter: separate review draft</h2><p><a href="chapters/d_inclusion.html">Open 13 dedicated traces, 56 checkpoints and four editable labs →</a>. Exact set atoms, signed multiplicity, onto maps, forbidden assignments, rook boards, bounded allocations, divisibility sieves and directed adjacency have distinct visual models. This chapter remains a draft pending explicit student approval. <a href="reviews/d_inclusion-quality.html">Read the observed verification evidence.</a></p><h2>Approval</h2>')
p.write_text(s,encoding='utf-8')
out=R/'dist/evidence/d_inclusion';out.mkdir(exist_ok=True)
for source,name in [('d_inclusion-verification.json','verification.json'),('d_inclusion-browser-audit.json','browser.json'),('d_inclusion-model-audit.json','models.json'),('d_inclusion-reviewed-courses.json','courses.json')]: shutil.copy2(B/source,out/name)
p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8')
heading='## Current delivery: English inclusion-exclusion chapter, October 5, 2026'
if heading not in s:
 s+='\n\n'+heading+'''

The user explicitly approved d_counting in Site version 68 and requested the next sole chapter. The 32 earlier chapters and their 1,835 question entries are preserved. d_inclusion is now a review draft awaiting explicit approval, with four genuinely reviewed primary written courses from MIT, Oxford, Cornell and CMU and a fifth reviewed Berkeley note. A documented eight-candidate pool supports a bounded selection; no worldwide exhaustive comparison is claimed. The chapter has a deep 16-section lesson, 80 original or independently reconstructed course tasks plus two authentic archive revisits, 80 complete examination rules, 13 distinct animated traces with 56 checkpoints, and four editable exact-enumeration labs.

Read research/chapter-gate.json before further work. Do not start d_pigeonhole or any other chapter before explicit approval. The approval ledgers retain the preceding 32 chapters as approved; this chapter is not promoted by its delivery. Do not ask the student a test before initial reading.

Source audit: research/d_inclusion-source-audit.md. Main lesson: research/d_inclusion.en.md. Task bank and archive provenance: research/d_inclusion-questions.json and d_inclusion-authentic.json. Rules: research/d_inclusion-review.en.md. Build only this chapter with build_d_inclusion_models.py, render_d_inclusion.py and install_d_inclusion_assets.py. Do not run start_d_inclusion.py again: it records the previous approval once. Do not overwrite this independent player or its inventory with the legacy shared model builder. The combined inventory has 33 chapters, 1,917 question entries, 234 models, 1,343 checkpoints and 197 embedded walkthroughs.

Observed evidence: d_inclusion-verification.json passed 1,267 independent mathematical assertions; d_inclusion-browser-audit.json records 308 independently checked lab cases, seven rejected inputs, all 56 measured checkpoint layouts, actual motion/controls, loaded fonts, 390-pixel containment and complete printable solutions/checkpoints. d_inclusion-model-audit.json records each distinct model contract. The quality audit records source errors corrected, finite verification limits and authentic revisits. The two archive questions were visually checked against the original PDFs; their answers are independent derivations rather than official keys.

Publish the exact pushed source to the existing owner-private Site. Mirror only changed files to the GitHub study-planner-1406 branch, preserving unrelated mirror deletions. Keep the gate awaiting_user_approval after delivery.
'''
p.write_text(s,encoding='utf-8')
print('Finalized one inclusion-exclusion review draft; next chapter remains gated.')
