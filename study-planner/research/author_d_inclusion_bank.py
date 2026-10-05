"""One chapter bank: independently worded course reconstructions and new exam models."""
from pathlib import Path
from math import comb,factorial,lcm,gcd
from fractions import Fraction
from itertools import product,permutations,combinations
import json
B=Path(__file__).resolve().parent;Q=[]
def onto(n,m):return sum((-1)**j*comb(m,j)*(m-j)**n for j in range(m+1))
def der(n):return sum((-1)**j*comb(n,j)*factorial(n-j) for j in range(n+1))
def partial(n,q):return sum((-1)**j*comb(q,j)*factorial(n-j) for j in range(q+1))
def caps(total,c):
 m=len(c);h=lambda t:comb(t+m-1,m-1) if t>=0 else 0
 return sum((-1)**len(I)*h(total-sum(c[i]+1 for i in I)) for k in range(m+1) for I in combinations(range(m),k))
def add(title,stem,solution,expected,category,check,origin='Original examination-style problem',difficulty='Hard'):
 Q.append(dict(id=f'DINCL_{len(Q)+1:02}',title=title,stem=stem,solution=solution,expected=str(expected),category=category,check=check,origin=origin,difficulty=difficulty))
def a(title,stem,steps,expected,category,check,origin='Original examination-style problem',difficulty='Hard'):
 add(title,stem,'\n\n'.join(f'{i}. {s}' for i,s in enumerate(steps,1))+f'\n\n**Result.** {expected}.',expected,category,check,origin,difficulty)

# Independently written reconstructions of every relevant numerical course example.
a('Correct an original survey arithmetic error','A class has 32 students. Twenty-one study mathematics, fourteen are seniors, and three meet both descriptions. Count students in neither group and assess a reported answer of two.',[
 'The universe is the 32 students. Membership in both groups is an inclusive overlap, not an extra disjoint group.',
 r'The union is $21+14-3=32$. Therefore its complement has $32-32=0$ members.',
 'An attaining atom table has eighteen math-only students, eleven senior-only students, three in both and none outside. Its total is 32.',
 'The answer two printed in the source example is an arithmetic error, not an alternative interpretation.'],0,'sets',{'kind':'atoms','atoms':[0,18,11,3],'target':'none'},'Independent corrected reconstruction of CMU 21-301 §2.5 opening example')
a('Inclusive overlaps from pair-only reports','Three subject sets have sizes 60, 200 and 40. Pair-only groups have sizes 4, 3 and 11, and the triple group has size 2. Count the union.',[
 'Pair-only data must be converted to inclusive intersections before using the standard union formula. The inclusive pair counts are six, five and thirteen.',
 r'The union is $60+200+40-6-5-13+2=278$. Subtracting four, three and eleven directly would count the triple group three times.',
 'The single-only groups have sizes 51, 183 and 24. Add these to the pair-only and triple groups to obtain the same union count.',
 'Each atom is nonnegative, so the data are feasible; no outside-universe total was supplied or needed for a union.'],278,'sets',{'kind':'atoms','atoms':[0,51,183,4,24,3,11,2],'target':'union'},'Independent reconstruction of MIT 6.042J §14.9.2')
a('Both required decimal digits','Count positive six-digit integers that contain at least one 7 and at least one 9.',[
 r'The universe has $9\cdot10^5$ integers. Its first digit is nonzero, so it must not be treated as an unrestricted digit code.',
 r'Forbidding 7 gives $8\cdot9^5$ integers; forbidding 9 gives the same number. Forbidding both leaves $7\cdot8^5$.',
 r'The valid count is $9\cdot10^5-2\cdot8\cdot9^5+7\cdot8^5=184592$. The missing-digit events may overlap, so the final addition is essential.',
 'A digit dynamic program tracking whether 7 and 9 have appeared supplies an independent exact count.'],184592,'digits',{'kind':'digits','length':6,'required':[7,9],'positive':True},'Independent reconstruction of Oxford §3.3 Example 3.10')
a('Two divisibility events','Among the positive integers at most 100, count those divisible by 2 or 5.',[
 'There are fifty multiples of two and twenty multiples of five. The universe includes 100.',
 r'The intersection consists of multiples of $\operatorname{lcm}(2,5)=10$, so it has ten members.',
 'The union count is fifty plus twenty minus ten, giving sixty. The integer 100 belongs to both sets but contributes once.',
 'A direct residue check across the ten blocks of length ten gives six qualifying residues in each block.'],60,'sieve',{'kind':'divisible','L':1,'H':100,'divisors':[2,5],'target':'union'},'Independent reconstruction of Cornell §4.4 Example 4.24',difficulty='Medium')
a('Repeated rank, not poker-hand strength','From a standard 52-card deck, count unordered five-card hands containing at least two cards of the same rank.',[
 r'The universe is $\binom{52}{5}$ unordered hands. Count the complement, whose five ranks are all distinct.',
 r'Choose those ranks in $\binom{13}{5}$ ways and choose one of four suits for each selected rank, giving $\binom{13}{5}4^5$ complement hands.',
 r'The difference is $\binom{52}{5}-\binom{13}{5}4^5=1281072$. These include pairs, triples, full houses and other repeated-rank patterns.',
 'A straight with five distinct ranks belongs to the complement, even though its poker value may exceed a pair. The predicate concerns repeated rank, not hand ranking.'],1281072,'complement',{'kind':'poker'},'Independent reconstruction of Cornell §4.4 Example 4.27')
a('Three directed blocks with shared symbols','Permute the ten distinct digits, allowing an initial zero. Count arrangements containing at least one of the directed consecutive blocks 42, 04 and 60.',[
 r'Each single block contracts two symbols into one, leaving $9!$ permutations. Reverse blocks do not satisfy the event.',
 r'Any pair leaves eight contracted objects. In particular 60 and 04 concatenate to 604, and 04 with 42 concatenates to 042; the intersections are compatible.',
 r'All three concatenate to 6042, leaving $7!$ arrangements. Inclusion-exclusion gives $3\cdot9!-3\cdot8!+7!=972720$.',
 'The shared symbols do not make the intersections empty. Their predecessor and successor requirements agree and form a path.'],972720,'adjacency',{'kind':'edges','n':10,'edges':[[4,2],[0,4],[6,0]],'target':'union'},'Independent reconstruction of MIT 6.042J §14.9.3')
a('Strictly below the endpoint','Count positive integers strictly less than 1000 divisible by at least one of 2, 3 and 5.',[
 'The endpoint is 999. Singles contribute 499, 333 and 199; pair intersections use divisors six, ten and fifteen.',
 'Those pair counts are 166, 99 and 66. The triple count uses thirty and is 33.',
 r'The alternating total is $$499+333+199-166-99-66+33=733.$$ The seven terms include every specified nonempty divisor intersection.',
 'The complementary count is 266. Using 1000 changes the universe and includes an additional qualifying integer.'],733,'sieve',{'kind':'divisible','L':1,'H':999,'divisors':[2,3,5],'target':'union'},'Independent reconstruction of Oxford §3.4 Example 3.12')
a('The dice union error','Roll three independent fair six-sided dice. Find the probability that at least one shows a specified face, and assess the claim that it equals one half.',[
 r'Each hit event has probability $1/6$. Every specified pair has probability $1/36$, and the triple has probability $1/216$ by mutual independence.',
 r'The union is $3/6-3/36+1/216=91/216$. One half is only the first-order upper bound.',
 r'Alternatively all three dice miss with probability $(5/6)^3=125/216$, whose complement is $91/216$.',
 'The two descriptions count the same event. The independence assumption computes intersections; inclusion-exclusion itself does not require it.'],Fraction(91,216),'probability',{'kind':'dice','dice':3,'faces':6,'face':1},'Independent reconstruction of Berkeley EECS70 Note 14 §4.3')
a('Totient from actual prime events','How many integers in the closed interval from 1 to 360 are coprime to 360?',[
 r'The distinct prime divisors are two, three and five. An integer is coprime precisely when it avoids all three divisibility events.',
 r'The complementary sum factors as $360(1-1/2)(1-1/3)(1-1/5)=96$. Exponents of the prime factors are already included in 360.',
 'Equivalently subtract the union of multiples of two, three and five from 360; all selected prime products divide 360 exactly.',
 'Repeating a factor for every exponent would incorrectly exclude the same event several times.'],96,'sieve',{'kind':'coprime','n':360},'Independent numerical application of the MIT §14.9.5 and CMU §2.5 totient derivations')
a('Onto maps with no extra relabeling','Count functions from a five-element labeled domain onto a three-element labeled codomain.',[
 r'Start with $3^5$ maps. Missing a specified codomain value leaves $2^5$ maps; missing a specified pair leaves one map.',
 r'The count is $3^5-3\cdot2^5+3\cdot1^5=150$. Missing all three yields zero because the domain is nonempty.',
 'The codomain values were labeled throughout. Multiplying the result by three factorial would overcount.',
 'Dividing by three factorial instead gives twenty-five partitions of the five inputs into three nonempty unlabeled fibers.'],150,'maps',{'kind':'map','n':5,'m':3,'target':'onto'},'Independent numerical application of Cornell Example 4.26 and CMU §2.5 surjections')

# Exact atoms, inversion, extremal constraints and nonuniqueness.
atoms=[22,22,18,8,15,6,5,4]
for title,target,expected,formula in [
 ('Exactly two properties','exact2',19,r'$S_2-3S_3=31-12=19$'),
 ('Exactly one property','exact1',55,r'$S_1-2S_2+3S_3=105-62+12=55$'),
 ('At least two properties','atleast2',23,r'$S_2-2S_3=31-8=23$'),
 ('An exclusive triple alternative','odd',59,r'$N_1+N_3=55+4=59$')]:
 a(title,'A universe has 100 objects. Three sets have sizes 40, 35 and 30, inclusive pair sizes 12, 10 and 9, and triple size 4. '+{'exact2':'Count objects in exactly two sets.','exact1':'Count objects in exactly one set.','atleast2':'Count objects in at least two sets.','odd':'Count objects in an odd number of sets.'}[target],[
 'First reconstruct the disjoint atoms. The single-only sizes are 22, 18 and 15; pair-only sizes are eight, six and five; the triple size is four.',
 'The requested multiplicities select the corresponding disjoint atoms. Equivalently use '+formula+'.',
 'The outside size is 22, and all eight atoms are nonnegative and total 100. This confirms feasibility before interpreting the count.',
 'An inclusive pair includes triple members, so a direct sum of reported pair counts cannot be used as an exact-two count.'],expected,'sets',{'kind':'atoms','atoms':atoms,'target':target})
a('A hidden inconsistency','Sets A, B and C each have size ten. Every inclusive pair intersection has size eight and the triple intersection has size one. Can these data come from finite sets?',[
 r'The only-$A$ atom would have size $10-8-8+1=-5$. The same holds for the other single-only atoms.',
 'A cardinality cannot be negative. Therefore the data are impossible, even though each pair size individually is no larger than either participating set.',
 'The contradiction does not depend on an outside-universe size. Increasing the universe cannot repair a negative internal atom.',
 'The missing feasibility check is the joint overlap geometry encoded by the atom equations.'],'Infeasible: each single-only atom is -5','concept',{'kind':'proof','claim':'negative_single_atom'})
a('Recover an unknown triple range','Three sets have sizes 12, 11 and 10 in a universe of 25. Inclusive pair sizes are five, four and three. Determine the attainable integer range of the unspecified triple size t.',[
 r'The pair-only atoms are $5-t,4-t,3-t$, requiring $0\le t\le3$. The single-only atoms are $3+t,3+t,3+t$ and remain nonnegative.',
 r'The union is $12+11+10-5-4-3+t=21+t$, leaving $4-t$ outside. This also requires $t\le4$.',
 'Combining every constraint gives t equal to zero, one, two or three. Each value is attainable by constructing the eight disjoint atoms.',
 'The data do not determine a unique union: its size can range from 21 through 24.'],'0 <= t <= 3, integer','concept',{'kind':'proof','claim':'triple_range'})
a('An attainable minimum outside','In a universe of 50, three sets have sizes 24, 18 and 12, with exactly three objects in all three. Find the minimum possible number outside the union.',[
 'Total memberships are 54. Every triple member creates two duplicate memberships, forcing six duplications in total.',
 'The union can contain at most 48 objects, so at least two are outside. Additional pair-only atoms would reduce the union further.',
 'The bound is attained with single-only groups of sizes 21, 15 and nine, three triple members, and two outside. Every marginal is correct.',
 'The construction is necessary: a lower bound without an arrangement attaining it would not establish the exact minimum.'],2,'sets',{'kind':'atoms','atoms':[2,21,15,0,9,0,0,3],'target':'none'})
a('Invert four-event aggregate data','Four events on 50 objects have intersection sums S1 = 70, S2 = 40, S3 = 10, S4 = 1. Find the counts N0 through N4 for exactly each membership multiplicity.',[
 r'Use the triangular system from the largest index: $N_4=1$, $N_3=10-4=6$, and $N_2=40-3\cdot6-6=16$.',
 r'Then $N_1=70-2\cdot16-3\cdot6-4=16$ and $N_0=50-16-16-6-1=11$.',
 'The vector is nonnegative and totals fifty. Objects of each multiplicity can be assigned to arbitrary masks of that size, establishing aggregate feasibility.',
 'These aggregate counts do not prescribe individual intersection sizes. In particular S2 is a sum of six inclusive pair counts, not the exact-two count.'],'[11, 16, 16, 6, 1]','inverse',{'kind':'inverse','S':[50,70,40,10,1]})
a('A symmetric difference is not a union','A and B have sizes 30 and 25, with ten objects in both. Count objects in exactly one of the two sets.',[
 'The two disjoint single-only groups have sizes twenty and fifteen.',
 r'The symmetric difference has $|A|+|B|-2|A\cap B|=30+25-20=35$ objects.',
 'Subtracting the overlap only once yields the union size 45, which still contains the ten shared objects.',
 'The correct coefficient of each shared object is two minus two, so it disappears from the exact-one event.'],35,'sets',{'kind':'atoms','atoms':[0,20,15,10],'target':'exact1'})
a('Equal margins, different triple overlap','Construct two three-event systems with marginal probabilities one half and pair intersections one quarter, but different triple intersections.',[
 'For three mutually independent fair bits, the all-one outcome has probability one eighth.',
 'For independent fair bits X and Y, let Z be their exclusive-or. The four equally likely triples are 000, 011, 101 and 110. Each bit is fair and each pair is independent.',
 'In the second system 111 is absent, so the triple intersection has probability zero. Pairwise data therefore do not determine the triple.',
 'The probability of the union is seven eighths in the first system and three quarters in the second, despite matching singles and pairs.'],'Triple 1/8 versus 0; union 7/8 versus 3/4','concept',{'kind':'proof','claim':'pairwise_not_mutual'})

# Fixed points and forbidden cycles.
a('Eight-label derangements','Count permutations of eight distinct labels with no fixed points.',[
 r'For a specified j fixed positions, the intersection has $(8-j)!$ completions. Group these by j using $\binom8j$.',
 r'The count is $\sum_{j=0}^8(-1)^j\binom8j(8-j)!=14833$. All eight positions are restricted.',
 r'The recurrence gives $D_8=7(D_7+D_6)=7(1854+265)=14833$. This is independent of direct evaluation of the alternating formula.',
 'The full permutation universe has 40320 outcomes, so the count is within range and is not exactly 40320 divided by e.'],der(8),'permutation',{'kind':'permutation','n':8,'target':'fixed','r':0})
a('Exactly three fixed positions','Count permutations of eight labels with exactly three fixed points, whose locations are not specified.',[
 r'Choose the three fixed positions in $\binom83=56$ ways. Each such choice forces the corresponding three labels.',
 'The remaining five positions must contain a derangement on their own labels, otherwise the permutation has additional fixed points.',
 r'There are $56D_5=56\cdot44=2464$ permutations. Using $5!$ instead counts at least the selected three positions as fixed.',
 'Each qualifying permutation has one unique set of fixed positions, so the choice stage introduces no duplicate representation.'],2464,'permutation',{'kind':'permutation','n':8,'target':'fixed','r':3})
a('Restrict only the named positions','For a seven-label permutation, require that positions one, two and three are not fixed; other positions are unrestricted.',[
 'There are three forbidden-fixed events, not seven. A specified j-event intersection leaves seven minus j freely permuted labels.',
 r'The count is $7!-3\cdot6!+3\cdot5!-4!=3216$.',
 'The count exceeds D7, because fixed points outside the first three positions are allowed.',
 'Changing the event family to all seven positions would solve a stricter question.'],partial(7,3),'permutation',{'kind':'permutation','n':7,'target':'partial','q':3})
a('Forced and forbidden fixed positions','A permutation of seven labels must fix position seven and must not fix positions one, two or three. Count the permutations.',[
 'First remove the forced position and its symbol. There are six remaining labels and three specified forbidden-fixed positions.',
 r'The count is $6!-3\cdot5!+3\cdot4!-3!=426$.',
 'The two sets of positional conditions are disjoint. If position seven also appeared in the forbidden list, the count would be zero.',
 'The required-fixed position is specified, so there is no factor choosing which position remains fixed.'],426,'permutation',{'kind':'permutation','n':7,'target':'forcedpartial','forced':[6],'forbidden':[0,1,2]})
a('A specified two-cycle inside a derangement','Count derangements of seven labels satisfying pi(1) = 2 and pi(2) = 1.',[
 'The named labels form a forced two-cycle. Their positions and symbols can be removed together.',
 'All remaining five labels must still avoid their own positions. There are D5 = 44 completions.',
 'No factor of six is present because the partner of label one was specified as label two.',
 'Replacing the derangement remainder by five factorial would permit forbidden fixed points among labels three through seven.'],44,'permutation',{'kind':'permutation','n':7,'target':'two_cycle','a':0,'b':1})
a('The non-two-cycle branch','Count derangements of seven labels with pi(1) = 2 but pi(2) not equal to 1.',[
 'Remove label one from its directed cycle by joining its predecessor directly to label two. Since the predecessor is not two, this creates no fixed point.',
 'The operation gives a derangement of the remaining six labels. Conversely insert one into the unique arrow entering two.',
 'This bijection gives D6 = 265 outcomes. The two-cycle branch gives D5 separately, so for the fixed partner two there are D6 + D5 total.',
 'The bijection explains the recurrence rather than merely reusing its numerical output.'],265,'permutation',{'kind':'permutation','n':7,'target':'not_two_cycle','a':0,'b':1})
a('Exclude every two-cycle','How many permutations of six labels contain no two-cycle? Fixed points are allowed.',[
 'A bad event fixes a particular unordered pair as a two-cycle. Two such events intersect only if their pairs are disjoint.',
 r'The number of j disjoint unordered pairs is $6!/(2^j j!(6-2j)!)$, with $(6-2j)!$ unrestricted completions.',
 r'The count is $6!\sum_{j=0}^3(-1)^j/(2^j j!)=720-360+90-15=435$.',
 'This is not the derangement count: a fixed point is permitted and a cycle of length three or more is also permitted.'],435,'permutation',{'kind':'permutation','n':6,'target':'no_two_cycles'})
a('Specified fixed set versus fixed count','In an eight-label permutation, exactly positions one and two must be fixed. Count the outcomes.',[
 'The fixed set is specified, so no binomial choice is required.',
 'All remaining six positions must avoid their own labels, giving D6 = 265 outcomes.',
 'If the question instead asked for exactly two fixed positions anywhere, the count would be the result multiplied by twenty-eight.',
 'If it asked merely to fix positions one and two without the word exactly, the count would instead be six factorial.'],265,'permutation',{'kind':'permutation','n':8,'target':'specified_fixed','positions':[0,1]})
a('Impossible fixed-point multiplicity','Can a permutation of nine labels have exactly eight fixed points? Prove the answer.',[
 'If eight positions contain their own distinct labels, the unused label is the label of the remaining position.',
 'The final position is forced to contain that label and is therefore fixed too. A permutation cannot have exactly n minus one fixed points.',
 r'The exact-count formula agrees: $\binom98D_1=9\cdot0=0$.',
 'The obstruction is bijectivity, not a lack of arrangements of eight chosen positions.'],0,'permutation',{'kind':'permutation','n':9,'target':'fixed','r':8})
a('The empty permutation exception','Evaluate D0 and determine whether nearest-integer rounding of 0!/e gives it.',[
 'There is one empty permutation, and no position violates a fixed-point restriction. Thus D0 = 1.',
 'The nearest integer to one divided by e is zero. The nearest-integer rule therefore does not hold at n equal to zero.',
 r'For $n\ge1$ the alternating-series error is strictly less than $1/(n+1)\le1/2$, making the nearest integer unique.',
 'This is a boundary-domain exception, not a contradiction of the exact finite alternating sum.'],'D0 = 1; rounding gives 0','concept',{'kind':'proof','claim':'empty_derangement'})

# Map predicates and labeled/unlabeled distinctions.
for n,m,target,extra in [(6,4,'onto',None),(7,4,'required',2),(6,5,'image',3),(7,5,'missing',2),(6,4,'specified_missing',2)]:
 if target=='onto': val=onto(n,m);pred='onto all four codomain labels';form=rf'$O({n},{m})=\sum_j(-1)^j\binom{{{m}}}j({m}-j)^{{{n}}}$';reason='All missing-label intersections have the same size for a fixed order.'
 elif target=='required':val=sum((-1)**j*comb(extra,j)*(m-j)**n for j in range(extra+1));pred='with each of two specified codomain labels present, while the other labels are optional';form=rf'$\sum_{{j=0}}^{{{extra}}}(-1)^j\binom{{{extra}}}j({m}-j)^{{{n}}}$';reason='Only the required labels define bad events; optional labels remain available in every surviving alphabet.'
 elif target=='image':val=comb(m,extra)*onto(n,extra);pred='with image size exactly three';form=rf'$\binom{{{m}}}{{{extra}}}O({n},{extra})$';reason='Choose the actual image set once, then require an onto map to that set.'
 elif target=='missing':val=comb(m,extra)*onto(n,m-extra);pred='missing exactly two unspecified codomain labels';form=rf'$\binom{{{m}}}{{{extra}}}O({n},{m-extra})$';reason='Choose the missing set, then require every nonmissing output label to appear.'
 else:val=(m-extra)**n;pred='missing two specified codomain labels, with any additional omissions permitted';form=rf'$({m}-{extra})^{{{n}}}$';reason='The two prohibited labels are simply deleted from each input alphabet; no onto condition remains.'
 a('Map predicate: '+target,f'Count functions from a {n}-element labeled set to a {m}-element labeled set '+pred+'.',[
 f'The universe distinguishes every input and output label. {reason}',
 'The corresponding exact expression is '+form+'. This formulation preserves whether missing labels are specified and whether other labels must occur.',
 f'Exact evaluation gives {val}. A multinomial occupancy sum over qualifying fiber sizes is an independent check.',
 'No output-label factorial is introduced after this calculation; the labels are already part of each function.'],val,'maps',{'kind':'map','n':n,'m':m,'target':target,'q':extra})
a('Unlabeled nonempty blocks','Partition six labeled elements into three nonempty unlabeled blocks. Count partitions.',[
 'Map the elements onto three labeled outputs, producing a nonempty fiber partition with named blocks.',
 r'The onto count is $3^6-3\cdot2^6+3=540$. Every unlabeled partition has exactly $3!=6$ block labelings.',
 'Dividing by six gives ninety partitions. Equal-sized blocks do not change this factor because the blocks contain different labeled elements.',
 'The Stirling recurrence independently gives S(6,3) = 90.'],90,'maps',{'kind':'partition','n':6,'m':3})
a('Every box receives at least two labeled balls','Distribute six distinct balls among three labeled boxes, requiring at least two balls per box.',[
 'The total forces occupancy exactly two in each box. This is not a weak-composition problem with unit weight per occupancy.',
 r'The count is the multinomial $6!/(2!2!2!)=90$. Choose the first pair, then the second pair, and the last pair is forced.',
 'The boxes are labeled; dividing by three factorial would answer a different partition question.',
 'Simple missing-box inclusion-exclusion only enforces at least one ball per box and would not impose the stated lower bound of two.'],90,'maps',{'kind':'map','n':6,'m':3,'target':'minoccupancy','q':2})
a('Image size after a forced equality','Count onto maps from six inputs to three labeled outputs if the first two inputs must have equal images.',[
 'Contract the two equal-image inputs into one labeled choice unit. The remaining four inputs form four other units.',
 'The equality changes six independent choices to five, while the onto condition still requires all three outputs.',
 r'The count is $O(5,3)=3^5-3\cdot2^5+3=150$. There is no separate factor choosing the common image: that choice is already one of the five map decisions.',
 'Enumeration of five-unit maps and expansion of the contracted unit gives a bijection.'],150,'maps',{'kind':'map','n':6,'m':3,'target':'equalonto'})
a('Empty domain and empty output set','Give the onto counts for size pairs (0,0), (0,3) and (3,0). Explain the zero-power convention.',[
 'The empty domain has one function into any set, but that function is onto only when the codomain is empty.',
 'A nonempty domain has no function to the empty codomain, because even one input would need an output value.',
 'The counts are one, zero and zero respectively. In the finite sum, zero to the zero power is interpreted as one to count the empty function.',
 'This is a combinatorial convention for a discrete count, not a limit of a real-valued expression.'],'[1, 0, 0]','concept',{'kind':'proof','claim':'empty_maps'})
a('Subset-required outputs versus exact image','A seven-input map to four outputs must contain output labels one and two. Is its count the same as the count of maps with image exactly {1,2}? Give both counts.',[
 r'Requiring labels one and two but allowing three and four gives $4^7-2\cdot3^7+2^7=12138$.',
 r'Requiring the image to equal the specified pair removes outputs three and four and requires both remaining labels, giving $2^7-2=126$.',
 'The first predicate allows image size two, three or four; the second fixes both the size and the actual labels.',
 'There is no factor choosing the pair in either expression because the pair was specified.'],'12138 versus 126','concept',{'kind':'proof','claim':'required_vs_exact'})

# Bounded allocations, unequal caps and positional alphabets.
for total,c in [(8,[3,3,3,3]),(7,[1,2,4,5]),(5,[0,2,3,5]),(10,[2,3,4,5]),(9,[4,4,4]),(0,[2,2,2])]:
 val=caps(total,c);thresholds=[x+1 for x in c]
 a('Bounded occupancy: '+','.join(map(str,c)),f'Count nonnegative integer vectors of sum {total} in {len(c)} labeled coordinates with respective upper caps '+', '.join(map(str,c))+'.',[
 f'The objects are occupancy vectors of identical tokens. The first forbidden coordinate values are {thresholds}, one above each allowed cap.',
 r'For a specified violating subset I, subtract its threshold sum. The residual unrestricted count is $H_m(T-\sum_{i\in I}(c_i+1))$, with zero for a negative residual.',
 f'Add these residual counts with subset-parity signs. Exact evaluation gives {val}; unequal caps are retained separately rather than replaced by an average.',
 'The coefficient of the same total in the product of finite coordinate polynomials independently checks every allowed vector.'],val,'caps',{'kind':'caps','total':total,'caps':c})
a('Lower bounds before upper violations','Count integer triples of sum eight satisfying 0 <= x1 <= 2, 1 <= x2 <= 4 and 2 <= x3 <= 6.',[
 'Subtract lower bounds zero, one and two. The new total is five and the residual caps are two, three and four.',
 r'The unrestricted count is $H_3(5)=21$. The single violations leave totals two, one and zero, contributing six, three and one.',
 'No pair of threshold violations is feasible, so the result is 21 − 6 − 3 − 1 = 11.',
 'Using original upper bounds as residual caps would ignore tokens already committed to satisfy the lower bounds.'],11,'caps',{'kind':'caps','total':5,'caps':[2,3,4]})
a('A code may start with zero','Count length-six decimal codes containing at least one 7 and at least one 9. Compare the model to positive six-digit integers.',[
 r'All six positions allow ten digits, so the universe has $10^6$ codes. Missing either specified digit leaves $9^6$ codes, and missing both leaves $8^6$.',
 r'The count is $10^6-2\cdot9^6+8^6=199262$.',
 'This exceeds the positive-integer count 184592 because valid codes beginning with zero are included.',
 'The difference is exactly the count of length-five unrestricted suffixes containing both required digits.'],199262,'digits',{'kind':'digits','length':6,'required':[7,9],'positive':False})
a('Three required nonzero decimal symbols','Count positive five-digit integers containing each of digits one, two and three at least once.',[
 'For a specified omitted set of j required nonzero digits, the first position has nine minus j choices and later positions have ten minus j choices.',
 r'The count is $\sum_{j=0}^3(-1)^j\binom3j(9-j)(10-j)^4$. The first-digit factor is not ten minus j.',
 'Exact evaluation gives 4146. The subset-sign sum excludes every missing-required-symbol event while allowing repeated symbols.',
 'A position-by-position mask dynamic program verifies the result without using the same alternating expression.'],4146,'digits',{'kind':'digits','length':5,'required':[1,2,3],'positive':True})
a('Unequal alphabets by position','A four-position word has alphabets {A,B}, {A,B,C}, {B,C}, {A,C}. Count words containing each of A, B and C.',[
 'The universe has two times three times two times two = 24 words. Required symbols define missing-symbol events.',
 'Missing A leaves one times two times two times one = four words; missing B leaves one times two times one times two = four; missing C leaves two times two times one times one = four.',
 'Every two-symbol missing intersection is empty because at least one position then has no allowed symbol. Therefore the result is 24 − 4 − 4 − 4 = 12.',
 'A single alphabet-size power cannot express these intersections because the position alphabets differ.'],12,'digits',{'kind':'alphabets','sets':['AB','ABC','BC','AC'],'required':'ABC'})

# Divisibility, residues and endpoint logic.
for L,H,ds,target in [(1,200,[4,6],'union'),(101,500,[6,10,15],'none'),(1,300,[4,6,9],'exact1'),(1,300,[4,6,9],'atleast2'),(-30,30,[4,6],'union')]:
 vals=[x for x in range(L,H+1) if {'union':lambda r:r>=1,'none':lambda r:r==0,'exact1':lambda r:r==1,'atleast2':lambda r:r>=2}[target](sum(x%d==0 for d in ds))];val=len(vals)
 a('Integer interval: '+target,f'In the closed integer interval [{L},{H}], count values for which divisibility by '+', '.join(map(str,ds))+' holds '+{'union':'at least once','none':'for none of the divisors','exact1':'for exactly one divisor','atleast2':'for at least two divisors'}[target]+'.',[
 r'For every specified divisor subset, use its least common multiple d. The inclusive intersection count is $\lfloor H/d\rfloor-\lfloor(L-1)/d\rfloor$.',
 'Aggregate these intersection counts by order, then apply the '+target+' multiplicity formula. Repeated prime factors are not multiplied twice.',
 f'The exact count is {val}. Direct testing of the listed integer interval verifies the divisor predicate independently.',
 'The interval is closed. When negative values or zero are present, mathematical floors remain valid, and zero satisfies every divisibility event.'],val,'sieve',{'kind':'divisible','L':L,'H':H,'divisors':ds,'target':target})
a('Compatible congruences','Count integers from one through one hundred satisfying x congruent to one modulo four and x congruent to three modulo six.',[
 'The residues agree modulo gcd(4,6) = 2, so the intersection is feasible.',
 'The merged class is x congruent to nine modulo twelve: its members in the stated interval are 9, 21, 33, 45, 57, 69, 81 and 93.',
 'The count is eight. Multiplying moduli to get 24 would miss half the solutions.',
 'The intersection consists of one class modulo the least common multiple, not necessarily modulo the product.'],8,'sieve',{'kind':'congruence','L':1,'H':100,'residues':[[1,4],[3,6]]})
a('Incompatible congruences','Count integers from one through one hundred satisfying x congruent to zero modulo four and x congruent to one modulo six.',[
 'The first condition makes x even, while the second condition makes x odd.',
 'Equivalently the two residues disagree modulo gcd(4,6) = 2. The intersection is empty before considering the interval.',
 'The answer is zero. A floor count using any guessed common modulus would not repair incompatible residues.',
 'In a union question, this incompatibility would set the intersection term to zero rather than eliminate either single event.'],0,'sieve',{'kind':'congruence','L':1,'H':100,'residues':[[0,4],[1,6]]})
a('A modular union','Count integers in [1,120] congruent to one modulo four or three modulo six.',[
 'The first residue class has thirty members and the second has twenty.',
 'Their compatible intersection is the class nine modulo twelve, which has ten members.',
 'Inclusion-exclusion gives thirty plus twenty minus ten = forty. Inclusive or retains common values once.',
 'The residues, not just the moduli, determine whether the intersection exists.'],40,'sieve',{'kind':'congruenceunion','L':1,'H':120,'residues':[[1,4],[3,6]]})
a('A non-squarefree totient','Evaluate the number of positive integers at most 864 that are coprime to 864.',[
 r'The prime factorization is $2^5 3^3$. Only the two distinct primes generate bad divisibility events.',
 r'The count is $864(1-1/2)(1-1/3)=288$. Alternatively subtract multiples of two and three and add multiples of six.',
 'The exponents influence the universe size 864 but do not repeat the factors in the product.',
 'Direct gcd evaluation across the closed interval provides an independent check.'],288,'sieve',{'kind':'coprime','n':864})
a('A strict endpoint changes a residue count','Count positive integers strictly below sixty divisible by four or six.',[
 'The effective upper endpoint is 59. Singles have fourteen and nine members; the intersection has four multiples of twelve.',
 'The union has fourteen plus nine minus four = nineteen members.',
 'Including sixty would add one qualifying value, producing twenty for the at-most-sixty question.',
 'Strict endpoint conversion occurs before every floor calculation, not after subtracting an arbitrary one from the final answer.'],19,'sieve',{'kind':'divisible','L':1,'H':59,'divisors':[4,6],'target':'union'})

# Forbidden boards and adjacency intersections, with genuinely different compatibility patterns.
boards=[(4,[(0,0),(0,1),(1,0)]),(5,[(0,0),(0,1),(1,0),(1,1)]),(5,[(0,0),(1,1),(2,2)]),(4,[(0,0),(0,1),(0,2),(0,3)]),(5,[(0,0),(0,1),(1,1),(1,2),(2,2)])]
for n,board in boards:
 rk=[]
 for k in range(n+1):rk.append(sum(len({a for a,b in I})==k and len({b for a,b in I})==k for I in combinations(board,k)))
 val=sum((-1)**k*rk[k]*factorial(n-k) for k in range(n+1))
 a('Forbidden-board assignment '+str(len(Q)-59),f'Assign {n} distinct labels bijectively to {n} positions. Using one-based coordinates, forbid the cells '+str([(r+1,c+1) for r,c in board])+'. Count allowed permutations.',[
 'A selected forbidden-cell intersection is nonempty only when no two cells share a row or column. Count such compatible selections by size.',
 f'The rook numbers r0 through r{n} are {rk}. Their values exclude conflicting selections even when those cells are individually forbidden.',
 rf'Apply $\sum_k(-1)^k r_k({n}-k)!$, which evaluates to {val}. Each compatible k-cell selection has exactly the stated factorial of completions.',
 'A direct permutation check against every forbidden cell verifies the result. A binomial coefficient based only on the number of cells would ignore their topology.'],val,'rook',{'kind':'board','n':n,'board':board,'rook':rk})
for n,edges in [(5,[(0,1),(0,2)]),(5,[(0,1),(1,2)]),(5,[(0,1),(1,0)]),(6,[(0,1),(2,3),(1,4)])]:
 val=sum(any(any(p[i]==a and p[i+1]==b for i in range(n-1)) for a,b in edges) for p in permutations(range(n)))
 a('Directed adjacency compatibility '+str(len(Q)-64),f'Permute labels one through {n} in a linear row. Count arrangements containing at least one directed adjacency from '+str([(a+1,b+1) for a,b in edges])+'.',[
 'For each specified event subset, check that every symbol has at most one required successor and predecessor and that no directed cycle is forced.',
 r'A compatible subset of k edges forms directed path blocks and has $(n-k)!$ arrangements. An incompatible subset contributes zero, not the same factorial.',
 f'Apply the union alternating sum over actual compatible subsets. The result is {val}. Direct enumeration of permutations independently confirms it.',
 'Two edges sharing a source conflict; a path sharing its middle symbol is valid; a directed two-cycle cannot occur in a linear row. The specific edge topology determines which case applies.'],val,'adjacency',{'kind':'edges','n':n,'edges':edges,'target':'union'})
a('Cell-disjoint is not component-independent','On a three-by-three forbidden board, take one component {(1,1)} and another {(1,2)}. Is multiplying their rook polynomials valid?',[
 r'Each one-cell component has polynomial $1+x$. Their product would be $1+2x+x^2$.',
 'The actual union has two cells in the same row, so both cannot be selected as nonattacking rooks. Its polynomial is one plus two x, with zero x-squared coefficient.',
 'Therefore the product is invalid. The components are cell-disjoint but share a row.',
 'Independent multiplication requires both row sets and column sets to be disjoint.'],'R(x) = 1 + 2x; product invalid','concept',{'kind':'proof','claim':'rook_components'})

# Bounds, inversion proofs, weighted/conditional data, algorithmic reasoning.
a('Certified union interval','A universe has 200 objects with S1 = 150, S2 = 60 and S3 = 15; higher intersections are unknown. Give Bonferroni intervals for the union and its complement.',[
 'Order two gives the lower union bound 150 minus 60 = 90. Order three gives the upper bound 150 minus 60 plus 15 = 105.',
 'Hence the union lies in [90,105]. Subtract the upper and lower bounds from 200 in reverse order to obtain complement interval [95,110].',
 'These are certified inequalities. Without further constraints they must not be advertised as exact attainable ranges.',
 'A first-order upper bound of 150 is valid but weaker than the available third-order bound.'],'union [90,105]; complement [95,110]','concept',{'kind':'proof','claim':'bonferroni_interval'})
a('A closer-truncation counterexample','One object belongs to each of ten events. Compare the first- and second-order union truncations to the true union count.',[
 r'The intersection sums are $S_1=10$ and $S_2=\binom{10}{2}=45$. The true union count is one.',
 'The first truncation is ten with absolute error nine. The second is negative thirty-five with absolute error thirty-six.',
 'The second is farther away but is still a valid lower bound. Taking its maximum with zero gives a more useful lower bound.',
 'This disproves a blanket statement that every consecutive truncation improves absolute accuracy.'],'T1 = 10; T2 = -35','concept',{'kind':'proof','claim':'truncation_error'})
a('Prove the exact-two coefficient','For arbitrary m events, derive the coefficient of Sj in the count of objects satisfying exactly two events.',[
 r'The coefficient is $(-1)^{j-2}\binom j2$ for $j\ge2$. An object with t memberships receives the sum of these coefficients times $\binom tj$.',
 r'Use $\binom tj\binom j2=\binom t2\binom{t-2}{j-2}$. The alternating sum becomes $\binom t2(1-1)^{t-2}$.',
 'It is one for t equal to two, zero for larger t, and zero for t below two because there are no terms.',
 'This indicator proof applies to arbitrary finite sets, including asymmetric intersection sizes.'],'coefficient (-1)^(j-2) C(j,2)','concept',{'kind':'proof','claim':'exact2_coefficient'})
a('At least two is a different inversion','Derive the coefficients of S2, S3 and S4 in the count satisfying at least two events. Explain why the exact-two coefficients differ.',[
 r'The at-least-two coefficients are $(-1)^{j-2}(j-1)$, so the first three are one, negative two and positive three.',
 r'They arise by summing exact-r inversions over r at least two. Equivalently apply $\binom{j-1}{1}=j-1$.',
 'Exact-two coefficients are one, negative three and positive six. A triple member must survive in at-least-two but disappear in exactly-two.',
 'For four events the desired expression is S2 minus two S3 plus three S4.'],'S2 - 2 S3 + 3 S4','concept',{'kind':'proof','claim':'atleast2_coefficient'})
a('Recover specified atoms from inclusive counts','For three events, the complete inclusive table in masks 000 through 111 is [20,10,9,4,8,3,2,1]. Recover all exact atoms.',[
 'Start with the triple atom one. The three pair-only atoms are inclusive pair counts minus one: three, two and one.',
 'The only-A atom is ten minus four minus three plus one = four; only-B is nine minus four minus two plus one = four; only-C is eight minus three minus two plus one = four.',
 'The outside atom is twenty minus twenty-seven plus nine minus one = one. Thus the mask-ordered vector is [1,4,4,3,4,2,1,1].',
 'It is nonnegative and totals twenty. Summing each atom over supersets of a specified mask recovers the original inclusive count.'],'[1, 4, 4, 3, 4, 2, 1, 1]','inverse',{'kind':'atoms_inverse','G':[20,10,9,4,8,3,2,1]})
a('Uniform conditional counting','Roll two fair six-sided dice. Given that their sum is even, find the probability that at least one die shows six.',[
 'The conditional universe has eighteen outcomes: both dice even or both odd. All eighteen retain equal conditional weights.',
 'The first-die-six event has three outcomes in this universe, and the second-die-six event also has three. Their shared outcome is (6,6).',
 'The conditional union therefore has five favorable outcomes and probability five eighteenth.',
 'Unconditioned independence cannot be substituted directly after conditioning. Intersect the hit events with the even-sum universe first.'],Fraction(5,18),'probability',{'kind':'conditional_dice'})
a('Nonuniform atomic weights','A two-event system has atom weights 1/10 outside, 2/10 only A, 3/10 only B and 4/10 in both. Find the union and conditional probability of A given B.',[
 'The marginals are P(A) = six tenths and P(B) = seven tenths, with shared weight four tenths.',
 'The union is six tenths plus seven tenths minus four tenths = nine tenths, agreeing with the outside complement.',
 'Conditional probability is shared weight divided by P(B), namely four sevenths. Counting atoms as equally likely would give a different answer.',
 'The model uses probabilities, not uniform cardinality of the four region labels.'],'union 9/10; P(A|B) = 4/7','concept',{'kind':'proof','claim':'weights'})
a('Complete-table feasibility is sufficient','Prove that nonnegative integer atoms reconstructed from a complete inclusive intersection table are sufficient for finite-set realization.',[
 'For each mask, create a disjoint set containing exactly the reconstructed number of objects. These sets are distinct atoms by construction.',
 'Place every object in event i precisely when its mask has bit i set. The intersection at a specified mask is the union of all atom groups at supersets of that mask.',
 'The inverse transform guarantees those superset sums equal the supplied inclusive counts, so every requested cardinality is realized.',
 'This proof certifies arbitrary finite sets, not a requested geometric representation by circles or a separate probabilistic independence property.'],'Construct disjoint objects per mask','concept',{'kind':'proof','claim':'atom_realization'})
a('Subset-transform invariant and cost','Explain why the bitwise subtraction transform recovers exact atoms from inclusive intersections, and state its complexity.',[
 'Before processing a bit, each count includes membership in its mask and already excludes previously processed outside bits. Subtracting the superset with the current bit removes outcomes having that extra membership.',
 'Masks containing the bit are not modified at that stage, so their role as the needed superset count is preserved. After all bits, each count enforces every membership and nonmembership.',
 'There are m stages and half of the 2^m masks are updated at each stage: O(m 2^m) integer arithmetic operations and O(2^m) storage.',
 'The complexity assumes the complete table is already supplied. It does not account for obtaining each intersection from an implicit event description.'],'O(m 2^m) time; O(2^m) space','concept',{'kind':'proof','claim':'transform'})
a('A mixed-model diagnosis','A solution counts bounded distributions of ten distinct balls into three boxes using one stars-and-bars count per occupancy vector. Identify the error and give the correct general expression.',[
 'Distinct balls distinguish assignments even when their occupancy vectors agree. A vector (x1,x2,x3) represents ten factorial divided by the product of the three occupancy factorials assignments.',
 r'The correct count is $\sum_{x_1+x_2+x_3=10,\;0\le x_i\le c_i}10!/(x_1!x_2!x_3!)$, where the caps must be supplied.',
 'A unit weight per vector counts identical-token allocations instead. Inclusion-exclusion on vector counts cannot silently change those unit weights into assignment counts.',
 'Without numerical caps, no single numeric answer is determined. An exact multinomial occupancy sum or labeled-map enumeration preserves the specified universe.'],'Use multinomial weights, not unit vector weights','concept',{'kind':'proof','claim':'labeled_weights'})

assert len(Q)==80,len(Q)
assert len({q['id'] for q in Q})==80
assert all(q['solution'].count('\n\n')>=4 for q in Q)
(B/'d_inclusion-questions.json').write_text(json.dumps(Q,indent=2)+'\n')
actual=json.loads((B/'exam-calibration/actual-items.json').read_text());ids=['MS_CS_1405_Q124','Phd_CS_1405_Q21']
(B/'d_inclusion-authentic.json').write_text(json.dumps([next(x for x in actual if x['id']==k) for k in ids],indent=2)+'\n')
print('Authored 80 fully worked original/course-inspired tasks plus two authentic revisits.')
