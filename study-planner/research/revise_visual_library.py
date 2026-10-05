"""Reproducible whole-library visual revision; no new chapter or lost question."""
from pathlib import Path
import json,re,sys,html,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'research/exam-rewrite'))
import mathml
GROUPS={
'bars':'insertion insertion-unstable merge selection bubble partition3 partition-skip max-subarray',
'search':'lower-bound search-stall',
'venn':'set-union set-intersection set-difference set-symmetric set-complement set-set-demorgan',
'truth':'implication de-morgan absorption xor shannon selectors nand-only consensus',
'graph':'quantifier-dependent quantifier-fixed cartesian transitive-closure reflexive-closure equivalence-classes hasse topological function-fibers function-preimages right-inverse function-composition function-count image-collapse shortest-path-certificate induction-gap',
'tiles':'induction-triangular induction-square strong-coins',
'derivation':'direct-even contrapositive sqrt-contradiction weakest-precondition karatsuba strassen',
'tree':'recursion-tree merge-recursion recurrence-levels rounded-splits fft-butterfly',
'geometry':'vector-addition projection gram-schmidt affine-origin matrix-composition cross-orientation closest-pair vector-norms gauss-geometry rank-fibers rank-collapse rank-cancellation rank-update rank-projection integer-family',
'matrices':'matrix-product matrix-transpose row-elimination matrix-summaries gauss-swap gauss-skip gauss-affine gauss-inconsistent gauss-inverse gauss-parameters gauss-lu gauss-plu gauss-binary gauss-coordinate gauss-rounding rank-pivots rank-column-transform rank-composition rank-parameters rank-factorization rank-witness rank-powers',
'enumeration':'selection-ordered selection-unordered selection-repeated powerset loop-triangle stars-bars',
'numeric':'euclid division power modular-power word-bit-cost crt-intersection finite-representation float-rounding base-conversion fraction-conversion gray-code hamming-code comb-word',
'memory':'assignment-sequential assignment-simultaneous short-circuit branch-m1 branch-0 branch-2 loop-transfers wraparound-loop fn-copy fn-pointer fn-alias fn-nested fn-static fn-lookup fn-orders fn-recursion fn-sharing fn-closure fn-default fn-output',
'array':'arr-boundary arr-row arr-column arr-prefix arr-copy-bad arr-copy-right arr-copy-left arr-insert arr-reverse arr-rotate arr-sharing arr-growth arr-packed arr-ring arr-transpose arr-difference arr-compact arr-search',
'probability':'probability-atoms probability-union pairwise-independence draw-without-replacement conditional-atoms conditional-history conditional-urn conditional-mixture conditional-selection conditional-simpson conditional-report conditional-bridge conditional-strip bayes-partition bayes-normalize bayes-frequencies bayes-density',
'plot':'growth-threshold encoding-length loop-doubling probability-limit bayes-sensitivity bayes-repeat bayes-copy bayes-predict bayes-host bayes-loss',
'cmos':'cmos-nand',
'circuit':'nand-mapping static-hazard hazard-consensus comb-dag comb-priority comb-cofactor comb-rom comb-nand comb-miter comb-fault comb-feedback comb-latch comb-arrival comb-interval comb-falsepath comb-active-low',
'waveform':'km-hazard-time',
'kmap':'km-gray km-corners km-cycle km-greedy km-dc km-hazard-cover km-merge km-qm km-pos km-chart km-petrick km-sharing km-planes',
}
CLAIMS={
'bars':'Bar height is value magnitude; stable labels identify records during moves and swaps.',
'search':'An indexed sorted strip exposes both half-open boundaries and their shrinking distance.',
'venn':'Overlapping sets retain explicit universe membership and the inspected result set.',
'truth':'The complete finite truth table highlights one valuation without claiming electrical timing.',
'graph':'Vertices, arrows and relation edges show actual membership, dependence or reachability.',
'tiles':'Unit tiles and coin witnesses encode exact constructive counts.',
'derivation':'A proof or arithmetic derivation advances through justified dependencies; formulas are native MathML.',
'tree':'Explicit subproblem/dependency edges expose splitting, evaluation and aggregation.',
'geometry':'Equal-scale coordinate axes expose vectors, solution sets and their actual transformations.',
'matrices':'Bracketed entry arrays retain dimensions, pivot positions and the current exact transformation.',
'enumeration':'Concrete outcome objects or occupied index pairs exhibit the exact counting convention.',
'numeric':'Place-value bits, quotient groups and arithmetic certificates expose the numeric representation.',
'memory':'Call frames, value transfers and references distinguish store, object identity and control.',
'array':'Indexed storage, address mappings and moving read/write positions retain logical versus physical boundaries.',
'probability':'Mass-proportional regions, bars, distributions or reliability edges expose the conditioning model.',
'plot':'Labeled, fixed-scale axes retain the actual quantitative dependence across checkpoints.',
'cmos':'Parallel pMOS and series nMOS channels explicitly connect VDD, output and ground.',
'circuit':'Named nets connect declared input/output ports of distinctive-shape gates or standard functional blocks.',
'waveform':'Step waveforms encode exact binary transport-delay events against a common time axis.',
'kmap':'Gray-ordered cells, Boolean cubes and exact cover tables encode minimization obligations.',
}
PAT=re.compile(r'<math\b[^>]*>[\s\S]*?</math>')
def canonical_math(block):
    m=re.search(r'aria-label="([^"]*)"',block)
    if not m:return block
    source=html.unescape(m[1]);p=mathml.Parser(source);value=p.seq()
    assert p.i==len(source),(p.i,source)
    display='display="block"' in block
    return '<math xmlns="http://www.w3.org/1998/Math/MathML" display="'+('block' if display else 'inline')+'" aria-label="'+html.escape(source,quote=True)+'">'+value+'</math>'
def questions(s):return re.findall(r'<section class="exam-question"[\s\S]*?</section>',s)
def semantic_question(s):
    # Rendering may change; question wording, source labels and formula sources must not.
    s=PAT.sub(lambda m:'MATH:'+html.unescape(re.search(r'aria-label="([^"]*)"',m[0])[1]) if 'aria-label=' in m[0] else m[0],s)
    return re.sub(r'\s+',' ',re.sub('<[^>]+>','',s)).strip()

def question_reasoning(s):
    """Compare stems, citations, formulas and solutions while figures are revised.

    Figure nets are separately checked against their declared circuit contracts.
    This comparison does not claim that unchanged prose certifies new artwork.
    """
    return semantic_question(re.sub(r'<figure\b[\s\S]*?</figure>','',s))
def run():
    data_path=ROOT/'dist/chapters/concept-animations.json';data=json.loads(data_path.read_text())
    mapping={id:type for type,ids in GROUPS.items() for id in ids.split()}
    assert len(mapping)==sum(len(ids.split()) for ids in GROUPS.values()),'Duplicate renderer assignments'
    assert set(mapping)==set(data['scenes']),(set(data['scenes'])-set(mapping),set(mapping)-set(data['scenes']))
    for id,s in data['scenes'].items():
        s['visual']={'type':mapping[id],'claim':CLAIMS[mapping[id]],'revision':'subject-specific-v1'}
        for f in s['frames']:
            for key in ['formulaHtml','captionHtml']:
                if f.get(key):f[key]=PAT.sub(lambda m:canonical_math(m[0]),f[key])
    data_path.write_text(json.dumps(data,ensure_ascii=True,separators=(',',':'))+'\n',encoding='utf-8')
    manifest=json.loads((ROOT/'research/animation-manifest.json').read_text())
    rows=[]
    for row in manifest['chapters']:
        topic=row['topicId'];p=ROOT/f'dist/chapters/{topic}.html';s=p.read_text(encoding='utf-8');before=[semantic_question(q) for q in questions(s)]
        changed=0
        def replace(m):
            nonlocal changed
            new=canonical_math(m[0]);changed+=new!=m[0];return new
        s=PAT.sub(replace,s)
        if 'semantic-diagrams.js' not in s:s=s.replace('<script src="concept-animation.js">','<script src="semantic-diagrams.js"></script><script src="concept-animation.js">')
        if 'math-layout.js' not in s:s=s.replace('</body>','<script src="math-layout.js"></script></body>')
        # Replace a uniform instruction with a chapter-specific visual interpretation.
        ids=list(dict.fromkeys(id for values in row['sections'].values() for id in values))
        types=list(dict.fromkeys(mapping[id] for id in ids))
        guide='<section class="visual-reading-guide" id="visual-reading-guide"><h2>How to read the revised diagrams</h2><p>'+ ' '.join(CLAIMS[t] for t in types)+'</p><p>Use the next-step control to inspect a completed transition. The caption states the assumptions and the exact state; a finite trace illustrates, but does not replace, the general proof. Record indices, logical boundaries, time coordinates and electrical polarity have distinct meanings.</p></section>'
        s=re.sub(r'<section class="visual-reading-guide"[\s\S]*?</section>','',s)
        at=s.find('<!-- CONCEPT ANIMATION START');s=s[:at]+guide+s[at:] if at>=0 else s.replace('</article>',guide+'</article>')
        assert [semantic_question(q) for q in questions(s)]==before,topic+' question content changed'
        p.write_text(s,encoding='utf-8')
        row['htmlSha256']=hashlib.sha256(p.read_bytes()).hexdigest()
        rows.append(dict(topicId=topic,questionCount=len(before),mathExpressions=len(PAT.findall(s)),mathLayoutsRebuilt=changed,visualTypes=types,models=ids,state='implementation_pending_browser_audit',lessonScope='Definitions, proofs, worked questions and cited source pool retained; visual explanations, mathematical layout and concept models revised.'))
    review=dict(state='in_progress',request='Review all existing chapters, replace uniform concept cards, supply circuit schematics and organize every mathematical expression.',chapterCount=len(rows),sceneCount=len(mapping),questionCount=sum(r['questionCount'] for r in rows),chapters=rows,rendererClaims=CLAIMS,limits=['Finite scene traces are bounded illustrations, not universal proofs.','The retained written course pool is documented in each chapter source audit; this revision does not assert a new worldwide course search.'])
    (ROOT/'research/subject-visual-review.json').write_text(json.dumps(review,indent=2)+'\n')
    gate_path=ROOT/'research/chapter-gate.json';gate=json.loads(gate_path.read_text());gate.update(state='in_progress',reviewScope='All 31 existing chapters: subject-specific diagrams, circuit schematics and mathematical layout.',activeWork='Whole-library revision explicitly requested by the user. No new chapter is being drafted.',proposedNextTopicId=None,approvedLibraryReview=False,visualReviewPath='research/subject-visual-review.json');gate_path.write_text(json.dumps(gate,indent=2)+'\n')
    (ROOT/'research/animation-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(chapters=len(rows),scenes=len(mapping),questions=review['questionCount'],mathRebuilt=sum(r['mathLayoutsRebuilt'] for r in rows))))
if __name__=='__main__':run()
