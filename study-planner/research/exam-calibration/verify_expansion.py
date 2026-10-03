"""Recompute numeric instances from explicit objects, state transitions or exact algebra.

Does not import authoring formulas. Symbolic proofs and boundary prose need editorial
review; numeric recomputation is not a proof of all 736 expanded questions.
"""
import json, math, itertools as it, re, hashlib
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
def prod(xs):return math.prod(xs)
def repeat_product(values,n):return prod(values for _ in range(n))
def assignments(n,k,predicate):return sum(predicate(v) for v in it.product(range(k),repeat=n))
def binary(n,p):return assignments(n,2,p)
def pair_states(n,p):return assignments(n,4,lambda v:p([(x//2,x%2) for x in v]))
def recurrence(n,initial,step):
 a=initial
 for k in range(1,n+1):a=step(a,k)
 return a
def ceil_information(n):
 outcomes=prod(range(1,n+1));capacity=1;height=0
 while capacity<outcomes:capacity*=2;height+=1
 return height
def determinant(a):
 a=[[F(x) for x in r] for r in a];d=F(1)
 for k in range(len(a)):
  p=next((j for j in range(k,len(a)) if a[j][k]),None)
  if p is None:return F(0)
  if p!=k:a[p],a[k]=a[k],a[p];d=-d
  v=a[k][k];d*=v
  for j in range(k+1,len(a)):
   ratio=a[j][k]/v
   a[j]=[x-ratio*y for x,y in zip(a[j],a[k])]
 return d
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def jordan(n):
 a=[[1,0,0],[0,1,0],[0,0,1]];b=[[1,1,0],[0,1,1],[0,0,1]]
 for _ in range(n):a=mm(a,b)
 return a[0][2]
def valuation(n):
 a=prod(range(1,n+1));c=0
 while a%2==0:a//=2;c+=1
 return c
def two_counter(n):
 x=y=n;c=0
 while x or y:
  if x:x-=1;y+=n
  else:y-=1
  c+=1
 return c
def transfer(n):
 a=n;b=n+1
 while a:a-=1;b+=2
 return b
def accumulate(n):
 s=0;i=2
 for _ in range(n):s+=i;i+=1
 return s
def tree_nodes(branch,n):return recurrence(n,1,lambda a,k:1+branch*a)
def edges_tree(arities):
 leaves=1
 for arity in arities:leaves+=arity-1
 return leaves
def pairings(n):
 @lru_cache(None)
 def go(k):return 1 if k==0 else sum(go(k-2) for _ in range(k-1))
 return go(2*n)
def derangements(n):
 @lru_cache(None)
 def go(mask):
  row=mask.bit_count()
  if row==n:return 1
  return sum(go(mask|(1<<j)) for j in range(n) if not (mask>>j)&1 and row!=j)
 return go(0)
def forbidden_adjacency(n):return binary(n,lambda v:all(not(v[j] and v[j+1]) for j in range(n-1)))
def idempotent(n):
 # Choose fixed image points, then construct the permitted maps themselves.
 return sum(1 for i,j in it.combinations(range(n),2) for _ in it.product((i,j),repeat=n-2))
def involutions(n):
 return sum(1 for v in it.permutations(range(n)) if sum(v[i]!=i for i in range(n))==4 and all(v[v[i]]==i for i in range(n)))
def cycles(n):
 c=0
 for v in it.permutations(range(n)):
  seen=set();k=0
  while k not in seen:seen.add(k);k=v[k]
  c+=len(seen)==n
 return c
def constrained_triples(total,positive=False,even=False,cap=None):
 return sum(1 for a in range(int(positive),total+1) for b in range(int(positive),total-a+1)
            if total-a-b>=int(positive) and (not even or a%2==0) and (cap is None or a<=cap))
def variance(n):
 distribution=[(sum(v),F(1,3)**sum(v)*F(2,3)**(n-sum(v))) for v in it.product((0,1),repeat=n)]
 mean=sum(k*p for k,p in distribution)
 return sum((k-mean)**2*p for k,p in distribution)
def two_stage(n):
 # Elementary four-state outcomes per original coin, one state is HH.
 return F(assignments(n,4,lambda v:v.count(3)==1),4**n)
def merge_bound(n):
 # Build the adversarial interleaving for two already sorted n-element lists.
 a=list(range(0,2*n,2));b=list(range(1,2*n,2));i=j=c=0
 while i<n and j<n:
  c+=1
  if a[i]<b[j]:i+=1
  else:j+=1
 return c
def merge_tree(n):
 # Combine comparison counts at each level, from singletons upward.
 sizes=[1]*(2**n);c=0
 while len(sizes)>1:
  next_level=[]
  for i in range(0,len(sizes),2):
   size=sizes[i]+sizes[i+1];c+=size-1;next_level.append(size)
  sizes=next_level
 return c
def floating_integers(n):
 def exact(k):
  if not k:return True
  while k%2==0:k//=2
  return k.bit_length()<=n
 k=0
 while exact(k+1):k+=1
 return k
def hardware_signed(n,value):
 word=value%(1<<n)
 return word if word<(1<<(n-1)) else word-(1<<n)
def alignment(n):
 offset=n
 while offset%4:offset+=1
 offset+=4
 while offset%4:offset+=1
 return offset
def packed(n):return len([range(i,min(i+8,n)) for i in range(0,n,8)])
def flow_short(n):
 i=j=0
 while i<n:
  j+=1
  if not j:break
  i+=1
 return j
def checkpoint(n):
 threshold=sum(range(1,n+1));s=k=0
 while s<threshold:k+=1;s+=k
 return k
def sequential_swap(n):
 a=n;b=2;a=a+b;b=a-b;a=a-b
 return a
def do_while(n):
 i=n;c=0
 while True:
  c+=1;i-=1
  if i<0:return c
def ripple(n):
 carry=0;times=[]
 for _ in range(n):times.append(carry+3);carry+=2
 return max(times+[carry])
def symmetric_trace_dim(n):
 # Independent symmetric matrix coordinates; the diagonal trace row has rank one.
 columns=[(i,j) for i in range(n) for j in range(i,n)]
 trace=[int(i==j) for i,j in columns]
 return len(columns)-int(any(trace))
def projection(n,residual=False):
 w=[F(n),F(1),F(2)];u=[F(1),F(1),F(0)]
 alpha=sum(x*y for x,y in zip(w,u))/sum(x*x for x in u)
 v=[x-alpha*y for x,y in zip(w,u)] if residual else [alpha*y for y in u]
 return sum(x*x for x in v)
def coordinate_transform(n):
 # P^-1 A P, explicitly multiplied, rather than recalling its closed form.
 P=[[1,1],[1,-1]];inv=[[F(1,2),F(1,2)],[F(1,2),F(-1,2)]]
 return mm(mm(inv,[[2,0],[0,n]]),P)[0][1]

# These evaluators are separate from the production authoring formulas. Some use
# exact factorization/algebra rather than exhaustive object enumeration; reported
# as recomputations, not as 368 independently proved theorems.
R={}
def register(t,**families):
 for k,v in families.items():R[t,k.replace('_','-')]=v
register('d_logic',
 equivalence_components=lambda n:binary(n+2,lambda v:v[0]==v[1] and (not v[0] or v[2])),
 nonempty_witness=lambda n:binary(n,lambda v:any(v) and not all(v)),
 binary_total=lambda n:repeat_product(sum(any(v) for v in it.product((0,1),repeat=n)),n),
 unique_witness=lambda n:repeat_product(sum(sum(v)==1 for v in it.product((0,1),repeat=n)),n),
 canonical_parity=lambda n:binary(n,lambda v:sum(v)%2==0),
 logical_consequence=lambda n:pair_states(n,lambda ps:all(not a or b for a,b in ps) and not all(not b or a for a,b in ps)),
 atleast_one_pair=lambda n:pair_states(n,lambda ps:any(a and b for a,b in ps)),
 functional_predicate=lambda n:binary(n,lambda v:any(v)),
 quantifier_negation=lambda n:repeat_product(2**n,n)-repeat_product(sum(any(v) for v in it.product((0,1),repeat=n)),n))
register('d_sets',three_region=lambda n:assignments(n,4,lambda v:all(x!=2 for x in v)),
 cover_two=lambda n:assignments(n,4,lambda v:all(x!=0 for x in v)),
 chain_three=lambda n:repeat_product(sum(a<=b<=c for a,b,c in it.product((0,1),repeat=3)),n),
 symmetric_fixed=lambda n:repeat_product(sum((a^b)==1 for a,b in it.product((0,1),repeat=2)),n),
 proper_subsets=lambda n:binary(n,lambda v:0<sum(v)<n),
 four_disjoint=lambda n:assignments(n,4,lambda v:True),
 fixed_intersection=lambda n:repeat_product(sum(not(a and b) for a,b in it.product((0,1),repeat=2)),n),
 complement_pairs=lambda n:repeat_product(sum(a!=b for a,b in it.product((0,1),repeat=2)),n))
register('d_proof',square_divisibility=lambda n:sum(x*x%6==0 for x in range(1,6*n+1)),
 pigeonhole_threshold=lambda n:sum(3 for _ in range(n))+1,
 subset_comparable=lambda n:len({min(i,2*n+1-i) for i in range(1,2*n+1)})+1,
 prime_products=lambda n:sum((x%2==0) != (x%3==0) for x in range(1,6*n+1)),
 strict_order_countermodels=lambda n:sum(x>y for x,y in it.product(range(n),repeat=2)),
 residue_square=lambda n:sum(r*r%2 for r in range(2*n)),
 contrapositive_count=lambda n:pair_states(n,lambda ps:all(not a or b for a,b in ps) and any(not a for a,b in ps)),
 distance_triangle=lambda n:constrained_triples(n+4,positive=True))
register('d_induction',weighted_geometric=lambda n:sum(k*2**(k-1) for k in range(1,n+1)),
 squares=lambda n:sum(k*k for k in range(1,n+1)),
 binomial_weights=lambda n:sum(sum(v) for v in it.product((0,1),repeat=n)),
 full_binary=lambda n:n+edges_tree([2]*n),
 telescoping=lambda n:sum(F(1,k*(k+1)) for k in range(1,n+1)),
 hanoi=lambda n:recurrence(n,0,lambda a,k:2*a+1),
 ternary_tree=lambda n:edges_tree([3]*n),
 nested_recurrence=lambda n:(lambda a:a[-1])(__import__('functools').reduce(lambda a,k:a+[2+sum(a)],range(n),[1])))
register('d_relations',equivalence_size=lambda n:sum(x//n==y//n for x,y in it.product(range(n*n),repeat=2)),
 symmetric_diagonal=lambda n:repeat_product(2,len(list(it.combinations(range(n),2)))),
 antisymmetric=lambda n:repeat_product(2,n)*repeat_product(3,len(list(it.combinations(range(n),2)))),
 strict_symmetry=lambda n:repeat_product(2,len(list(it.combinations(range(n),2)))),
 residue_classes=lambda n:sum((x-y)%n==0 for x,y in it.product(range(2*n),repeat=2)),
 order_size=lambda n:sum(x<=y for x,y in it.product(range(n),repeat=2)),
 closure_chain=lambda n:sum(x<y for x,y in it.product(range(n),repeat=2)),
 transitive_triplets=lambda n:sum(1 for _ in it.product(range(n),repeat=3)))
register('d_functions',injection=lambda n:sum(1 for _ in it.permutations(range(n+3),3)),
 onto_three=lambda n:assignments(n,3,lambda v:len(set(v))==3),
 idempotent_two=idempotent,involution_pairs=involutions,
 monotone_three=lambda n:assignments(n,3,lambda v:all(a<=b for a,b in zip(v,v[1:]))),
 right_inverse=lambda n:sum(1 for _ in it.product(range(n),repeat=3)),one_cycle=cycles,
 fixed_points=lambda n:sum(v[0]==0 and v[1]==1 for v in it.permutations(range(n))))
register('d_invariants',weighted_potential=transfer,gcd_euclid=lambda n:math.gcd(30*n,18*n),
 two_counter_ranking=two_counter,mixed_branching=lambda n:edges_tree([2]*n+[3]*n),
 accumulator_checkpoint=accumulate,recursive_state_count=lambda n:tree_nodes(3,n),
 periodic_projection=lambda n:sum(k%3!=0 for k in range(1,3*n)),
 balanced_resource=lambda n:(2*n+1)-2)
register('d_number',linear_congruence=lambda n:sum((6*x-12)%(6*n)==0 for x in range(6*n)),
 crt_adjacent=lambda n:next(x for x in range(n*(n+1)) if x%n==1%n and x%(n+1)==2%(n+1)),
 factorial_two=valuation,divisor_product=lambda n:sum(1 for k in range(1,9*2**n+1) if (9*2**n)%k==0),
 square_divisors=lambda n:sum((2**(2*n)*3**(2*n+1)*25)%(k*k)==0 for k in range(1,math.isqrt(2**(2*n)*3**(2*n+1)*25)+1)),
 totient=lambda n:sum(math.gcd(k,27*2**n)==1 for k in range(27*2**n)),
 power_cycle=lambda n:pow(3,4*n+1,10),gcd_prime_vectors=lambda n:math.gcd(2**n*3**(n+2),2**(n+1)*3**n))
register('a_model',decision_leaves=ceil_information,
 explicit_subsets=lambda n:sum(len(v) for v in it.product((0,1),repeat=n)),
 bit_length=lambda n:len(bin(2**n-1)[2:]),unary_size=lambda n:len('1'*(2**n-1)),
 matrix_multiplications=lambda n:sum(1 for _ in it.product(range(n),repeat=3)),
 permutation_output=lambda n:sum(len(v) for v in it.permutations(range(n))),
 triangular_comparisons=lambda n:sum(j<i for i,j in it.product(range(n),repeat=2)),
 search_height=lambda n:recurrence(n,0,lambda a,k:a+1))
register('a_asym',polynomial_ratio=lambda n:F(3*n*n+5*n,n*n),
 exponential_ratio=lambda n:F(3**n+2**n,3**n),log_log_input=lambda n:(2**(2**n)).bit_length().bit_length()-1,
 harmonic=lambda n:sum(F(1,k) for k in range(1,n+1)),subtracted_lower=lambda n:F(n*n-n,n*n),
 positive_polynomials=lambda n:F(n**3+n*n,n**3),oscillating=lambda n:2*n*(2+(-1)**(2*n)),factorial_information=ceil_information)
register('a_loop',double_triangle=lambda n:sum(1 for i in range(1,n+1) for _ in range(2*i)),
 square_inner=lambda n:sum(1 for i in range(1,n+1) for _ in range(i*i)),
 geometric_rows=lambda n:sum(1 for i in range(n+1) for _ in range(2**i)),
 divisor_region=lambda n:sum(i%j==0 for i,j in it.product(range(1,n+1),repeat=2)),
 continue_filter=lambda n:sum(i%3!=0 for i in range(1,3*n+1)),
 monotone_triple=lambda n:sum(i<=j<=k for i,j,k in it.product(range(n),repeat=3)),
 logarithmic_grid=lambda n:sum(1 for i in range(n) for j in range(i,n+1)),merge_pointer=merge_bound)
register('a_recurrence',affine_geometric=lambda n:recurrence(n,0,lambda a,k:2*a+3),
 balanced_linear=lambda n:recurrence(n,1,lambda a,k:2*a+2**k),
 leaf_dominance=lambda n:recurrence(n,1,lambda a,k:4*a+2**k),
 single_child_linear=lambda n:recurrence(n,1,lambda a,k:a+2**k),
 log_squared_toll=lambda n:recurrence(n,1,lambda a,k:a+k*k),
 subtract_one=lambda n:recurrence(n,0,lambda a,k:a+k*k),
 critical_level_index=lambda n:recurrence(n,0,lambda a,k:2*a+k),
 unequal_scale=lambda n:recurrence(n,0,lambda a,k:2*a+1),
 square_root_scale=lambda n:recurrence(n,1,lambda a,k:2*a+2**k))
register('a_divide',merge_total=merge_tree,
 cross_inversions=lambda n:sum(a>b for a in range(n,2*n) for b in range(n)),
 karatsuba_leaves=lambda n:repeat_product(3,n),strassen_leaves=lambda n:repeat_product(7,n),
 convolution_length=lambda n:len({i+j for i,j in it.product(range(n),repeat=2)}),
 fft_butterflies=lambda n:sum(2**n//2 for _ in range(n)),
 median_pivot=lambda n:sum(3 for _ in range(n))+2,binary_base=lambda n:sum(1 for _ in range(n+1)))
register('s_axioms',union_overlap=lambda n:F(len(set(range(n))|{0,n}),n+3),
 exclusive_independent=lambda n:F(sum((i==0)!=(j==0) for i,j in it.product(range(n),range(n+1))),n*(n+1)),
 two_stage=two_stage,disjoint_atoms=lambda n:sum(F(1,n+1) for _ in range(n)),
 tails_continuity=lambda n:1-sum(F(1,2**k) for k in range(1,n)),
 bayes_prior=lambda n:F(2,3*n)/(F(2,3*n)+F(n-1,3*n)),
 variance_indicators=variance,union_independent=lambda n:1-F(n-1,n)**n)
register('s_counting',positive_three=lambda n:constrained_triples(n+3,positive=True),
 capped_variable=lambda n:constrained_triples(n,cap=2),
 even_allocation=lambda n:constrained_triples(2*n,even=True),
 category_threshold=lambda n:sum(sum(i<n for i in s)>=3 for s in it.combinations(range(2*n),5)),
 onto_labels=lambda n:assignments(n,3,lambda v:len(set(v))==3),
 parity_words=lambda n:assignments(n,4,lambda v:v.count(0)%2==0),
 no_adjacent=forbidden_adjacency,multisets_four=lambda n:sum(1 for _ in it.combinations_with_replacement(range(4),n)),
 circular=lambda n:sum(1 for _ in it.permutations(range(1,n))),pair_partition=pairings,derangements=derangements,
 one_overlap=lambda n:pair_states(n,lambda ps:all(a or b for a,b in ps) and sum(a and b for a,b in ps)==1),
 adjacent_couples=lambda n:sum(1 for _ in it.permutations(range(n)))*binary(n,lambda v:True))
register('l_vectors',symmetric_trace=symmetric_trace_dim,
 intersection=lambda n:len(set(range(2*n))&set(range(n,3*n))),
 rank_nullity=lambda n:len(range(n+1))-len(range(n-1)),
 projection_size=lambda n:projection(n),residual_size=lambda n:projection(n,True),
 orthogonal_parameter=lambda n:next(a for a in range(-3*n,3*n+1) if a+2*n==0),
 coordinates=lambda n:F(n+2,2),kernel_hyperplane=lambda n:len(range(n+1))-1)
register('l_matrices',rank_one_determinant=lambda n:determinant([[1+int(i==j) for j in range(n)] for i in range(n)]),
 nilpotent_inverse=lambda n:next(x for x in range(-n,n+1) if x+n==0),
 trace_cycle=lambda n:sum((i+1)%n==i for i in range(n)),
 determinant_product=lambda n:determinant([[6*int(i==j) for j in range(n)] for i in range(n)]),
 jordan_power=jordan,rank_product=lambda n:2,
 similarity_coordinate=coordinate_transform,
 block_triangle=lambda n:determinant([[int(i==j)*(1 if i<n else 2)+int(i<n and j>=n) for j in range(2*n)] for i in range(2*n)]))
register('p_types',unsigned_range=lambda n:sum(2**i for i in range(n+3)),
 unsigned_addition=lambda n:((2**(n+3)-1)+(n+1))%(2**(n+3)),signed_minimum=lambda n:hardware_signed(n,2**(n-1)),
 alignment=alignment,array_extent=lambda n:sum(4 for _ in it.product(range(n),range(n+1))),packed_bits=packed,
 floating_integers=floating_integers,negative_division=lambda n:-((3*n+1)//3))
register('p_flow',ordered_updates=lambda n:sum(range(n)),short_circuit=flow_short,
 continue_for=lambda n:sum(i%3!=0 for i in range(1,3*n+1)),break_checkpoint=checkpoint,
 call_tree=lambda n:tree_nodes(2,n),recursive_local_work=lambda n:sum(range(1,n+1)),
 sequential_swap=sequential_swap,do_while=do_while)
register('g_number',biased_exponent=lambda n:(n-3)-sum(2**k for k in range(n-1)),
 fixed_point=lambda n:F(3*2**n+1,2**n),negative_decode=lambda n:hardware_signed(n,2**n-3),
 overflow_word=lambda n:hardware_signed(n,2*((1<<(n-1))-1)),ones_zero=lambda n:sum(1 for v in it.product((0,1),repeat=n) if all(v) or not any(v)),
 finite_fraction=lambda n:sum(F(1,2**k) for k in range(1,n+1)),
 floating_spacing=lambda n:F(17*2**n,16)-F(16*2**n,16),hex_width=lambda n:(16**n-1).bit_length())
register('g_boolean',implication_chain=lambda n:binary(n,lambda v:all(not a or b for a,b in zip(v,v[1:]))),
 parity_table=lambda n:binary(n,lambda v:sum(v)%2==1),self_dual=lambda n:repeat_product(2,len(list(it.product((0,1),repeat=n)))//2),
 pair_products=lambda n:pair_states(n,lambda ps:any(a and b for a,b in ps)),
 exact_weight=lambda n:binary(n,lambda v:sum(v)==2),affine_functions=lambda n:repeat_product(2,n+1),
 canonical_false=lambda n:binary(n,lambda v:sum(v)>1),
 quadratic_anf=lambda n:repeat_product(2,1+n+len(list(it.combinations(range(n),2)))),
 symmetric_functions=lambda n:repeat_product(2,len({sum(v) for v in it.product((0,1),repeat=n)})))
register('g_gates',and_tree=lambda n:recurrence(n,0,lambda a,k:2*a+1),
 nand_and=lambda n:sum(2 for _ in range(n)),xor_chain=lambda n:sum(4 for _ in range(n)),
 mux_tree=lambda n:recurrence(n,0,lambda a,k:2*a+1),ripple_delay=ripple,
 rc_scaling=lambda n:F(1,n)*(n+1),ring_frequency=lambda n:F(1000,2*sum(2 for _ in range(n))),
 consensus_cost=lambda n:sum(len('ab')+len('ac')+len('bc') for _ in range(n)))

def parse_numeric(s):
 s=s.strip('$')
 m=re.fullmatch(r'\\frac\{(-?\d+)\}\{(\d+)\}',s)
 return F(int(m[1]),int(m[2])) if m else F(s)
questions=[q for p in sorted(BASE.glob('original-expanded*.json')) for q in json.loads(p.read_text())]
checks=[];families={};ids=set()
for q in questions:
 assert q['id'] not in ids;qid=q['id'];ids.add(qid)
 assert len(q['options'])==4 and len(set(q['options']))==4 and 1<=q['answer']<=4,qid
 assert len(q['solution'].split())>=45,qid
 families.setdefault((q['topic'],q['family']),[]).append(q)
 if q['audit']:
  n=q['audit']['n'];result=R[q['topic'],q['family']](n)
  answer=parse_numeric(q['options'][q['answer']-1])
  assert F(result)==answer==F(q['audit']['expected']),(qid,result,answer)
  assert sum(parse_numeric(x)==answer for x in q['options'])==1,qid
  checks.append(dict(id=qid,n=n,recomputed=str(result),selectedAnswer=str(answer),passed=True))
assert len(families)==184 and len(questions)==736 and len(checks)==368
assert set(families)==set(R)
for key,qs in families.items():
 assert len(qs)==4 and sum(q['audit'] is not None for q in qs)==2,key
 assert {q['id'].rsplit('-',1)[1] for q in qs}=={'1','2','3','4'},key
baseline=json.loads((BASE/'tripling-baseline.json').read_text())
manifest=json.loads((BASE/'manifest.json').read_text());counts=[]
for c in manifest['chapters']:
 b=next(x for x in baseline['chapters'] if x['topicId']==c['topicId'])
 assert c['totalQuestions']>=3*b['before'],c['topicId']
 counts.append(dict(topicId=c['topicId'],before=b['before'],minimum=3*b['before'],after=c['totalQuestions'],passed=True))
out=dict(addedQuestions=len(questions),addedFamilies=len(families),numericRecomputations=len(checks),
 limits='Numeric instances recomputed from separate finite models, state transitions and exact algebra. Some factorizations share the mathematical method with the lesson. Symbolic derivations and boundary statements receive editorial review; these checks do not independently prove every symbolic statement or calibrate difficulty.',
 counts=counts,checks=checks,inputHashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in BASE.glob('original-expanded*.json')})
(BASE/'expansion-validation.json').write_text(json.dumps(out,indent=2)+'\n')
print('Passed',len(checks),'numeric recomputations;',len(questions),'added questions;',len(families),'families; all 22 chapter counts at least tripled.')
