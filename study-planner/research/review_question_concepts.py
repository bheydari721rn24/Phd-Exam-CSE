"""Map remaining visual reasoning needs to explicit, bounded concept models.

Exact question-data models take precedence. Reused teaching models are disclosed
as separate illustrations, never represented as the question's numeric solution.
"""
from pathlib import Path
import json,re,html,collections
R=Path(__file__).resolve().parents[1];O=R/'research/library-visual-question-review';rows=json.loads((O/'input.json').read_text());exact=json.loads((O/'problem-models.json').read_text());scenes=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes']
# Rules are local to each chapter and inspect the stem, not competing options.
rules={
'd_logic':[(r'quantif|witness|domain|relation|row constraint','quantifier-dependent'),(r'cnf|maxterm|clause|parity|truth|implication|assignment|entail|countermodel','implication')],
'd_sets':[(r'symmetric difference','set-symmetric'),(r'complement|outside|none|union','set-union'),(r'intersection|overlap','set-intersection'),(r'cartesian|product','cartesian'),(r'power.?set|subset|family|inclusion|transitive','powerset')],
'd_proof':[(r'witness|quantifier|existential','quantifier-dependent'),(r'counterexample|converse|implication|inconsisten','contrapositive'),(r'occupancy|pair.selection','selection-unordered')],
'd_induction':[(r'coin','strong-coins'),(r'tree|constructor','recursion-tree'),(r'recurrence|prefix|two.step|base','induction-gap'),(r'polynomial|square','induction-square'),(r'weighted|sum|telescop|binomial','induction-triangular')],
'a_model':[(r'merg|comparison','merge'),(r'recurs|tree|depth|stack','recursion-tree'),(r'bit|binary|doubl|encoded|encoding|numeric','word-bit-cost'),(r'matrix','matrix-product')],
'a_asym':[(r'recurren|recurs|split|level|toll','recurrence-levels'),(r'log|exponen|encoding|polynomial|growth|ratio|asymptotic|upper bound|tight','growth-threshold')],
'a_loop':[(r'merg','merge'),(r'doubl|squar|geometric','loop-doubling'),(r'ordered|triple|nested|inner|triangular|region|sum|guard|loop','loop-triangle'),(r'search|boundary','lower-bound')],
's_axioms':[(r'independent|pairwise','pairwise-independence'),(r'union|outside|overlap|event|cardinal','probability-union'),(r'weight|atom|sample|uniform','probability-atoms'),(r'limit|infinite','probability-limit')],
's_counting':[(r'onto|surject|weakly|increasing|nonnegative|allocation|bound|stars','stars-bars'),(r'without replacement|card|draw|selection','draw-without-replacement'),(r'order|arrang|word|position|code|symbol|permut','selection-ordered'),(r'group|team|subset|committee','selection-unordered')],
'l_vectors':[(r'projection|orthogonal|distance','projection'),(r'gram|orthonormal','gram-schmidt'),(r'norm|inequality','vector-norms'),(r'affine|origin','affine-origin'),(r'cross|orientation','cross-orientation'),(r'linear|subspace|basis|dimension|vector','vector-addition')],
'l_matrices':[(r'compos|commut|order','matrix-composition'),(r'transpos','matrix-transpose'),(r'inverse|elimin|nilpot|cancel','row-elimination'),(r'product|multiply|matrix|rank','matrix-product')],
'p_types':[(r'float|round|precision|binary32|large.integer','float-rounding'),(r'short.?circuit|invalid evaluation','short-circuit'),(r'unsigned|signed|wrap|complement|width|bit|shift','finite-representation'),(r'assignment|sequen|increment|macro','assignment-sequential')],
'p_flow':[(r'unsigned|orbit|wrap','wraparound-loop'),(r'continue|break|transfer|nested loop','loop-transfers'),(r'recurs|stride','fn-recursion'),(r'condition|else|switch|branch','branch-0'),(r'guard|accumul|assignment','assignment-sequential')],
'g_number':[(r'gray','gray-code'),(r'hamming|parity|error','hamming-code'),(r'float|bias|round|trunc|exponent|precision','float-rounding'),(r'sign|overflow|carry|word|complement|fixed.point','finite-representation'),(r'base|binary|expansion|radix|digit','base-conversion')],
'g_boolean':[(r'cofactor|shannon|mux|multiplexer|select','shannon'),(r'xor|parity','xor'),(r'consensus|hazard','consensus'),(r'nand|nor|complete','nand-only'),(r'canonical|cnf|equivalent|boolean|truth|simplif','de-morgan')],
'g_gates':[(r'cmos|transistor','cmos-nand'),(r'hazard|glitch','hazard-consensus'),(r'delay|timing|arrival|path','static-hazard'),(r'nand|mux|multiplexer|mapping|network','nand-mapping')],
'd_relations':[(r'composition|transitive|closure|reach','transitive-closure'),(r'equivalence|class|partition','equivalence-classes'),(r'partial order|hasse|bound|poset|divisib','hasse'),(r'reflexiv|antisym|symmetr','reflexive-closure'),(r'schedul|topolog','topological')],
'd_functions':[(r'preimage|image|inverse image','function-preimages'),(r'composition','function-composition'),(r'right inverse|section|representative','right-inverse'),(r'inject|surject|fiber|cardinal|onto|bijection','function-fibers'),(r'increas|monoton|count','function-count')],
'd_invariants':[(r'sort|insert','insertion'),(r'search|binary|interval','lower-bound'),(r'power|exponent','power'),(r'divis|quotient','division'),(r'gcd|euclid','euclid'),(r'recurs','merge-recursion'),(r'assignment|sequen|accumul|state','assignment-sequential')],
'd_number':[(r'chinese|congruen|crt|residue','crt-intersection'),(r'power|exponent|fermat','modular-power'),(r'gcd|euclid|bezout','euclid'),(r'diophant|equation|integer.solution','integer-family')],
'a_recurrence':[(r'rounded|floor|ceiling|unbalanced|split','rounded-splits'),(r'tree|leaf|stack|depth','recursion-tree'),(r'recurren|master|toll|level|unroll','recurrence-levels')],
'a_divide':[(r'closest|planar|distance|strip|point','closest-pair'),(r'karatsuba|digit|integer product','karatsuba'),(r'strassen|matrix','strassen'),(r'fft|fourier|convol|root|transform','fft-butterfly'),(r'subarray|prefix|suffix','max-subarray'),(r'merg|invers|stable','merge')],
'a_correct':[(r'partition|pivot','partition3'),(r'merge','merge'),(r'sort|stable|insertion','insertion'),(r'search|interval|binary','lower-bound'),(r'euclid|gcd','euclid'),(r'power|exponent','power'),(r'quotient|divis','division'),(r'certificate|shortest','shortest-path-certificate')],
's_conditional':[(r'simpson|stratum|strata|aggregate','conditional-simpson'),(r'mixture|hidden type','conditional-mixture'),(r'collider|selection|retained','conditional-selection'),(r'urn|draw|replacement','conditional-urn'),(r'bridge|reliab','conditional-bridge'),(r'report|informant|lie','conditional-report'),(r'continu|density|strip','conditional-strip'),(r'atom|joint|cell|reverse|independen|weight','conditional-atoms'),(r'history|prefix|sequence','conditional-history')],
's_bayes':[(r'host|door','bayes-host'),(r'copied|copy|correlat','bayes-copy'),(r'predict|future','bayes-predict'),(r'loss|decision|cost','bayes-loss'),(r'likelihood|evidence|prior|posterior|source','bayes-normalize'),(r'density|continu','bayes-density')],
'l_gauss':[(r'parameter|exceptional|compatib','gauss-parameters'),(r'lu|multiplier|permutation|pivot','gauss-plu'),(r'inverse','gauss-inverse'),(r'finite.field|binary','gauss-binary'),(r'round|numeric|tolerance','gauss-rounding'),(r'column|coordinate','gauss-coordinate'),(r'inconsisten|contradict','gauss-inconsistent'),(r'geometry|plane|solution|free','gauss-affine')],
'l_rank':[(r'factorization','rank-factorization'),(r'composition|product|sylvester|intersection','rank-composition'),(r'projection|idempotent','rank-projection'),(r'power|kernel chain','rank-powers'),(r'update|perturb|outer','rank-update'),(r'parameter','rank-parameters'),(r'fiber|solution|load|compatib','rank-fibers'),(r'null|kernel|rank|dimension|basis','rank-pivots')],
'p_functions':[(r'alias|pointer|reference|redirect|swap','fn-alias'),(r'static|persist','fn-static'),(r'closure|capture','fn-closure'),(r'lexical|scope|shadow|lookup','fn-lookup'),(r'order|unsequenc|argument|comma','fn-orders'),(r'recurs|depth|nested|halv','fn-recursion'),(r'copy|value|return|helper','fn-copy')],
'p_arrays':[(r'overlap|copy|move','arr-copy-right'),(r'growth|allocation|doubl|tripl|realloc','arr-growth'),(r'prefix|range|weighted','arr-prefix'),(r'difference|rectangle','arr-difference'),(r'transpos','arr-transpose'),(r'packed|triangle','arr-packed'),(r'row.major|column.major|offset|address|stride','arr-row'),(r'reverse','arr-reverse'),(r'rotat|ring','arr-rotate'),(r'insert','arr-insert'),(r'compact|filter','arr-compact'),(r'alias|sharing|slice','arr-sharing'),(r'bound|pointer|index|one.past','arr-boundary'),(r'search|lower.bound','arr-search')],
'g_kmap':[(r'hazard|edge.cover|glitch','km-hazard-cover'),(r'prime|essential|chart|dominan|irredund','km-chart'),(r'petrick|cover|cost|optimal','km-petrick'),(r'don.t.care|dc','km-dc'),(r'cube|group|canonical|merge','km-qm')],
'g_combin':[(r'priority','comb-priority'),(r'rom|decoder','comb-rom'),(r'nand','comb-nand'),(r'latch|feedback|combinational','comb-feedback'),(r'active.low|enable','comb-active-low'),(r'arrival|timing|path|delay','comb-arrival'),(r'fault|stuck','comb-fault'),(r'miter|equivalence|counterexample','comb-miter'),(r'shared|dag|depth','comb-dag')],
'd_counting':[(r'weak|increasing|nonnegative|allocation|lower bound|upper bound|stars|integer solution','stars-bars'),(r'ordered|word|symbol|code|permut|position|block|adjacent','selection-ordered'),(r'group|subset|team|committee|binomial|marked','selection-unordered'),(r'repet|alphabet','selection-repeated'),(r'loop|triple','loop-triangle')],
'd_inclusion':[(r'map|onto|image|output','function-fibers'),(r'atom|event|overlap|union|survey|outside','probability-union'),(r'permut|fixed|derang','selection-ordered'),(r'occupancy|bound|ball|box','stars-bars')],
'd_pigeonhole':[],
}
array_models=json.loads((R/'dist/chapters/a_arrays-models.json').read_text())['models']
array_rules=[(r'sparse|orthogonal|outer.product','orthogonal'),(r'floyd|cycle|fast.speed|meeting','floyd'),(r'splic','splice'),(r'sentinel|doubly|four.*write','dll'),(r'reversal|reverse|recursive','reverse'),(r'compact|dedup|filter','compact'),(r'merge|comparison','merge'),(r'rotation','rotate'),(r'shrink|contraction|thrash','quarter-shrink'),(r'growth|resiz|append|amortiz|memory|capacity','resize'),(r'insert|delet|shift|copy|movement','insert'),(r'tail|predecessor|destruction','tail-search'),(r'travers|search|indexed|prefix|kth|middle','scan-cost')]
out=[];counts=collections.Counter()
for r in rows:
 qs=[]
 for q in r['questions']:
  stem=q['html'].split('<details')[0].split('<div class="exam-options"')[0];stem=html.unescape(re.sub('<[^>]*>',' ',stem)).lower();ids=[]
  if q['id'] not in exact and not q['existingFigures'] and r['topicId']=='a_arrays':
   match=next((id for pattern,id in array_rules if re.search(pattern,stem)),None)
   if match:
    src=next(m for m in array_models if m['id']==match)
    exact[q['id']]=dict(kind='supporting-array-concept',frames=[dict(html=f['svg'],caption=f['caption']) for f in src['frames']],reading='Use this separately labeled teaching example to inspect the '+src['kind']+'. Apply its invariant to the data and cost convention of this question.',scope='The numbers and node labels belong to the teaching example, not the question. The written solution gives the actual answer. '+src['invariant'])
  if q['id'] not in exact and not q['existingFigures']:
   for pattern,id in rules.get(r['topicId'],[]):
    if re.search(pattern,stem):ids=[id];break
   # A transitive-set membership argument is not a powerset enumeration.
   # A monotone-subsequence proof is not a count of monotone functions.
   if r['topicId'] in ['d_sets','d_proof'] and re.search(r'transitive|transitivity|occupancy|pair.selection',stem):ids=[]
   if r['topicId']=='d_logic' and re.search(r'canonical|cnf|maxterm|parity',stem) and ids==['implication']:ids=[]
  for id in ids:assert id in scenes,id;counts[id]+=1
  qs.append(dict(id=q['id'],number=q['number'],title=q['title'],conceptModels=ids,exactModel=q['id'] if q['id'] in exact else None,reviewState='needs_rendered_review',decision='Exact question-data aid' if q['id'] in exact else 'Explicitly scoped teaching illustration' if ids else 'Existing visual retained' if q['existingFigures'] else 'No additional model: symbolic/conceptual derivation retained'))
 out.append(dict(topicId=r['topicId'],questions=qs))
(O/'concept-review.json').write_text(json.dumps(dict(chapters=out,counts=dict(counts)),indent=2)+'\n')
(O/'problem-models.json').write_text(json.dumps(exact,separators=(',',':'))+'\n');(R/'dist/chapters/problem-visual-models.json').write_text(json.dumps(exact,separators=(',',':'))+'\n')
print(dict(exact=len(exact),conceptPlacements=sum(counts.values()),distinctSupportingModels=len(counts),unmatched=sum(not q['conceptModels'] and not q['exactModel'] for r in out for q in r['questions'])))
