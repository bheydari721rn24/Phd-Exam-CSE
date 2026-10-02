"""Record performed review only; do not infer semantic review from tests."""
from pathlib import Path
import json, hashlib

findings = {
 'd_logic':['Corrected free-variable count and fresh-bound-name condition.', 'Added four quantifier movement laws with empty-domain cases and precise distribution laws.', 'Corrected formal-calculus scope; split diagram arrows to retain every arrowhead.'],
 'd_sets':['Corrected the alternating/decreasing-tail exercise title.', 'Distinguished legitimate ordered-pair membership from product-condition errors.', 'Named the outside Venn region relative to U.'],
 'd_proof':['Corrected contradiction and unused-assumption guidance.', 'Clarified the square-root domain and equality characterization.', 'Restored each proof-route arrowhead.'],
 'd_induction':['Corrected central L-tile quadrant placement and induced-gap explanation.', 'Made the zero-base geometric-sum polynomial convention explicit.', 'Restored dependency arrowheads.'],
 'a_model':['Corrected empty-size supremum and input-sensitivity lower-bound qualifications.', 'Specified distinct index-pair answer semantics and decision-tree b>=2,q>=1 assumptions.', 'Restored encoding-layer arrowheads.'],
 'a_asym':['Corrected signed residual in asymptotic equivalence under the nonnegative little-oh convention.'],
 'a_loop':['Checked all twenty exact-count solutions, including powers of two, short-circuit comparisons, inversions, and zero-size cases.', 'Removed rhetorical ambiguity in the geometric-sum solution.'],
 's_axioms':['Corrected the dyadic-cell limsup endpoint: probability one does not mean the whole closed interval.', 'Reviewed both manuscripts, all twenty-four solutions, limits, feasibility and laboratory model.'],
 's_counting':['Defined multiset brackets preserving repetitions instead of ordinary set braces.', 'Preserved all five stars in the stars-and-bars text using code formatting.', 'Reviewed all three manuscripts, thirty-four solutions, parity law, and review rules.'],
 'l_vectors':['Reviewed all three manuscripts, thirty-four complete solutions, complex conjugation, projection coefficients, equality cases, and numerical caveats.', 'Corrected a grammatical error in Problem 7.'],
 'l_matrices':['Reviewed all three manuscripts, thirty-six solutions, rectangular/square distinctions, Hermitian identities, matrix norms, and conditioning.', 'Replaced an unsupported backward reference with a self-contained exchange proof that n independent vectors in R^n span.'],
 'p_types':['Reviewed all three manuscripts, thirty-six solutions, C17 conversion/overflow contracts, and fifty end rules. No substantive mathematical correction identified.'],
 'p_flow':['Reviewed all three manuscripts, thirty-six solutions, break/continue paths, termination clauses, loop checkpoints, and sixty end rules. No substantive correction identified.'],
 'g_number':['Reviewed all three manuscripts, thirty-six solutions, arithmetic flags, signed ranges, fixed-point bounds, decimal/Gray/Hamming codes, and sixty end rules.', 'Added the extended-Hamming minimum-distance proof and clarified capacity, radix-termination, word-width, and absolute-error assumptions.'],
 'g_boolean':['Reviewed all three manuscripts, forty solutions, Boolean derivatives, quantification, ANF, unateness, source boundaries, and sixty end rules. No substantive mathematical correction identified.'],
 'g_gates':['Reviewed all three manuscripts, thirty-six solutions, constant assumptions, gate mappings, CMOS conduction, timing contracts, and sixty end rules.', 'Removed the incorrect XOR output-inversion bubble and corrected the equivalent-POS/duality distinction in the voter solution.'],
}

p=Path('research/library-review.json'); data=json.loads(p.read_text(encoding='utf-8'))
for chapter in data['chapters']:
    topic=chapter['topicId']
    chapter['diagramReview']='baseline_visual_and_semantic_review_complete; final_render_pending'
    if topic in findings:
        chapter['semanticReview']='complete; final_render_pending'
        chapter['findings']=findings[topic]
        for source in chapter['manuscripts']:
            content=Path(source['path']).read_bytes()
            source['reviewedSha256']=hashlib.sha256(content).hexdigest()
data['semanticChaptersReviewed']=len(findings)
data['lastCheckpoint']='All sixteen existing chapters fully read, including all source manuscripts, worked solutions and end rules. All twenty-nine figures visually and semantically inspected; final rebuilt rendering is pending.'
p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(data['lastCheckpoint'])
