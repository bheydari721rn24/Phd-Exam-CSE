"""Record actual completed checks, preserve evidence and close the one-chapter gate."""
import hashlib,json,re,shutil,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'research'
evidence=base/'a_divide-evidence';evidence.mkdir(exist_ok=True)
captures=Path(tempfile.gettempdir())/'a-divide-browser'
for p in captures.iterdir():
 if p.suffix in ('.png','.json'):shutil.copy2(p,evidence/p.name)
word_counts={}
for key in ('','-problems','-review'):
 p=base/f'a_divide{key}.en.md'
 word_counts[key or 'lesson']=len(re.findall(r'\b[\w]+(?:[’\'-][\w]+)*\b',p.read_text(encoding='utf-8')))
checks=json.loads((base/'a_divide-math-checks.json').read_text())
audit=f"""# Divide-and-Conquer Mathematical and Visual Quality Audit

Date: 2026-10-02. Topic: a_divide. Status: delivered English review draft awaiting explicit student approval.

## Source evidence

Eight universities form the documented screened pool. MIT, Stanford, UC Berkeley and CMU are the four principal genuinely reviewed written courses. ETH is a genuinely reviewed fifth-university supplement for maximum subarrays. Princeton, Oxford and Cornell are screened candidates, not silently counted as read courses. Actual page scopes and source disagreements are in a_divide-source-audit.md; PDF fingerprints are in a_divide-source-downloads.json.

Original-source page images inspected: CMU page 3 for packing; Berkeley pages 3 and 25 for integer shifts and FFT block structure; ETH page 10 for the crossing decomposition and empty-interval policy. PDFs were used as read-only references, and no course deck was copied into the served chapter.

## Teaching and coverage

The chapter contains {sum(word_counts.values())} source-word tokens by the documented simple lexical count, including code identifiers and review headings; this is not a printed page-count claim. There are 48 independently authored worked problems, 88 full-sentence revision rules, five original vector diagrams, twelve native MathML displays, seven executable teaching-code blocks and an exact bounded summary laboratory. Lesson, problems and review counts: {json.dumps(word_counts)}.

The main lesson develops contracts, recursion, work/span/space, lower bound, stable merge and strict inversions, nonempty maximum subarrays and associative summaries, closest pair with tied coordinates and dense-ID membership, signed/odd-width Karatsuba, all four ordered Strassen block proofs, roots of unity, radix-two FFT, inverse orthogonality, norm scaling, zero padding and modular-recovery conditions.

Source issues addressed include unstable merge ties, exhausted runs, queue-run stability, nonempty versus empty subarrays, half-specific geometric separation, odd-width shifts, carry-bit qualifications, noncommuting blocks, unnormalized Fourier norms, numerical precision and spurious reduced-majority candidates. No national entrance-exam archive was opened or classified.

## Independent executable checks

Actual manuscript code is extracted and executed, rather than rewritten inside its verifier. Optimized results are compared against distinct direct methods. Actual served JavaScript is executed through Node and compared to Python interval enumeration.

{json.dumps(checks,indent=2)}

The geometric packing, inductive correctness and algebraic identities remain mathematical proofs. These finite counts check implementation behavior and boundary cases; they are not a proof of arbitrary instances or all possible exam questions.

## Browser and visual evidence

The chapter was rendered locally in Edge at desktop width 1280 and mobile width 390. All five SVGs have zero out-of-view labels and zero label overlaps. The mobile document fits width 390 without page overflow, and native formula blocks have no overflow. Print-media width 794 confirms diagram fit; this does not claim paginated PDF inspection.

Screenshots of every diagram, all twelve MathML displays, the mobile laboratory, code, rules and opening were inspected. Mathematics, HTML indices and SVG index spans use STIX Two Math. Code uses JetBrains Mono; prose and headings use Source Sans 3 and Newsreader. Links have no underline. SVG indices use explicitly positioned spans rather than relying on small Unicode glyph fallback.

The four laboratory presets verify crossing, all-negative, left-only and tied answers. Invalid splits, malformed integer strings and out-of-bound values are rejected and do not present an old result as newly verified.

The site-wide English checker passes local links, chapter status, session data and index typography. The previously approved recurrence chapter verifier also passes after promotion.

## Limits and handoff

The manuscript is complete for its declared boundary, with no known failing mathematical or visual checks. Full quicksort, selection, randomized geometry, precision engineering and broader correctness theory retain their own chapter boundaries. Floating-point FFT remains educational, with no unrestricted integer-rounding guarantee. Course screening is bounded; neither worldwide optimality nor perfect performance on unseen questions is claimed.

a_recurrence is student-approved and ready. a_divide remains draft. The proposed next topic is a_correct and may begin only after explicit approval.
"""
(base/'a_divide-quality-audit.md').write_text(audit,encoding='utf-8')
gate_path=base/'chapter-gate.json';gate=json.loads(gate_path.read_text())
assert gate['currentTopicId']=='a_divide' and gate['state'] in ('in_progress','awaiting_user_approval')
gate.update(state='awaiting_user_approval',nextTopicId=None,proposedNextTopicId='a_correct',
 lastCompletedReview='Five genuinely reviewed universities; deep divide-and-conquer algorithms and proofs; 48 solved problems, 88 rules, five diagrams, twelve MathML displays and independently checked summary laboratory.',
 nextReview='Wait for explicit student approval of a_divide; then promote it and begin a_correct.',
 activeWork='Delivered a_divide review draft; waiting for explicit approval. No later chapter has been started.')
gate_path.write_text(json.dumps(gate,indent=2)+'\n')
handoff=ROOT/'WEEKLY_DELIVERY.md';text=handoff.read_text(encoding='utf-8')
text=text.split('## Current chapter handoff')[0]+"""## Current chapter handoff

2026-10-02: The student explicitly approved a_recurrence. Its chapter index and reproducible builder preserve ready status.

The sole new chapter is a_divide, Week 2 Algorithms: Divide and Conquer: Design and Analysis. Its English review draft covers design contracts, search, stable merging and strict inversions, maximum-subarray sufficient summaries, deterministic planar closest pair, signed and odd-width Karatsuba, all ordered Strassen proofs, FFT and exact-recovery conditions. Four principal university courses and an additional ETH course were genuinely reviewed from an eight-university screened pool. It contains 48 fully worked problems, 88 complete examination rules, five original vector diagrams, twelve native MathML displays and an independently checked exact summary laboratory.

Study page: dist/chapters/a_divide.html. Source comparison: dist/reviews/a_divide-sources.html. Reading scopes: research/a_divide-source-audit.md. Quality evidence: research/a_divide-quality-audit.md, research/a_divide-math-checks.json and research/a_divide-evidence. Deferred entrance-exam archives were not opened or classified.

The gate is awaiting_user_approval. a_divide remains draft until explicit approval. The proposed next topic is a_correct; it has not been started. Prior chapter and library-review evidence remain preserved.
"""
handoff.write_text(text,encoding='utf-8')
paths=list(evidence.glob('*'))+[base/f for f in ['a_divide.en.md','a_divide-problems.en.md','a_divide-review.en.md','a_divide-source-audit.md','a_divide-source-downloads.json','a_divide-quality-audit.md','a_divide-math-checks.json']]
manifest={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()}
(base/'a_divide-evidence-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Closed one-chapter gate; saved reading, mathematical and visual audits with evidence hashes.')
