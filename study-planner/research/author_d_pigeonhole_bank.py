"""Original mathematical tasks and independently worded course reconstructions."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent;Q=[]
def add(title,stem,steps,expected,check,wrong=None,origin='Original examination-style problem',difficulty='Hard'):
 row=dict(id=f'DPH_{len(Q)+1:02}',title=title,stem=stem,solution='\n\n'.join(f'{i}. {s}' for i,s in enumerate(steps,1))+f'\n\n**Conclusion.** {expected}.',expected=str(expected),check=check,origin=origin,difficulty=difficulty)
 if wrong:
  opts=[str(expected)]+list(wrong);shift=len(Q)%4;opts=opts[shift:]+opts[:shift];row.update(options=opts,answer=opts.index(str(expected))+1)
 Q.append(row)
MIT='Independent reconstruction of MIT 6.042J §14.8 / related class problems'
MIT18='Independent reconstruction of MIT 18.310 Pigeonhole Principle lecture'
OX='Independent reconstruction of Oxford Discrete Mathematics §6.5 / Exercises 6.7–6.8'
ST='Independent reconstruction of Stanford CS103 Winter 2026 Lecture 11'
TO='Independent reconstruction of Toronto MAT344 Lecture 7 §4'
CO='Independent reconstruction of Cornell CS2800 §4.5'
add('What the finite-function theorem actually forces',r'A total function maps seven distinct objects to five labels. Which property is forced for every such function?',[
 r'If the function were injective, its seven images would be distinct elements of a five-element set, which is impossible.',
 'Surjectivity is not forced: a constant function uses only one label. It is not ruled out either: send the first five objects to distinct labels and repeat two labels afterwards.',
 'The forced conclusion is a repeated image, hence noninjectivity. Equal output labels do not make the original objects identical.'], 'Noninjective',{'kind':'function','n':7,'k':5},['Injective','Surjective','Not surjective'],ST,'Medium')
add('An inclusive calendar model',r'Assume 366 possible birthday dates. Among 800 people, what is the largest occupancy guaranteed independently of their birthdays?',[
 r'The 800 people are objects and the 366 dates are labels. Since $800=2\cdot366+68$, the ceiling of $800/366$ is 3.',
 'A distribution with 68 dates containing three people and 298 containing two has total 800 and maximum three, so four cannot be universally required.',
 'The answer is a deterministic bound. No assumption of uniform birthday probabilities is needed.'],3,{'kind':'maxmin','n':800,'k':366},['2','4','800'],CO,'Medium')
add('ID sums with a fixed first digit',r'Each of 75 nine-digit ID strings begins with digit 9. Digits may repeat, and each student sums all nine digits. How many sum labels are possible, and what repeated-sum occupancy is guaranteed?',[
 r'The remaining eight digits range from 0 to 9, so the sum lies between 9 and $9+8\cdot9=81$ inclusive. This gives $81-9+1=73$ labels.',
 'Every integer sum in this range is realizable: distribute the desired increment among eight slots, each holding at most nine. The digits being ordered does not introduce extra sum labels.',
 r'There are 75 objects and 73 labels, so two sums coincide. Three are not forced because a vector with two doubled labels and 71 single labels has total 75.',
 'Counting 81 labels by omitting the minimum, or counting 72 by omitting an endpoint, changes the guarantee.'], '73 labels; occupancy 2',{'kind':'ids','students':75,'digits':9,'first':9},origin=MIT)
add('A stronger residue occupancy',r'Among 100 integers, how many are guaranteed to have the same remainder modulo 37?',[
 r'There are exactly 37 canonical remainder labels. Division gives $100=2\cdot37+26$, so some remainder class contains at least 3 positions.',
 'Two members in this class have a difference divisible by 37. Three equal residue labels do not require three equal numerical values.',
 'The balanced residue occupancies are 26 classes of size three and eleven of size two. Distinct integers with those residues can be chosen by adding multiples of 37, so the guarantee three is sharp.'],3,{'kind':'maxmin','n':100,'k':37},['2','4','37'],MIT)
add('Thirty bounded positive values',r'Thirty positive integers are all less than $10^7$. Use an exact image-size comparison to show that disjoint nonempty equal-sum index subsets exist.',[
 r'The total is at most $30(10^7-1)=299999970$. Including the empty subset, sum labels number at most 299999971.',
 r'There are $2^{30}=1073741824$ index subsets, strictly more than the labels. Therefore two distinct subsets have equal sums.',
 'Remove common indices from the two subsets. Their sums remain equal; distinctness leaves at least one nonempty side, and positivity then forces the other side to be nonempty too.',
 'The argument establishes existence even when a search through all subsets would be expensive. It does not identify the subsets by counting alone.'],'Guaranteed',{'kind':'subset-bound','n':30,'maximum':9999999},origin=MIT18)
add('A symmetric monotone guarantee',r'A sequence contains 37 distinct real values. What is the largest universally guaranteed length of an increasing or decreasing subsequence?',[
 r'The product-label theorem forces a monotone subsequence of length $\lceil\sqrt{37}\rceil=7$. Equivalently, 37 is one more than $6^2$.',
 'To exclude a guarantee of eight, use seven descending blocks with at most seven elements each and keep 37 values. Each increasing subsequence uses at most seven blocks and each decreasing subsequence stays within a block of at most seven.',
 'The theorem supplies either direction. A completely decreasing input shows why it cannot force increasing length seven specifically.'],7,{'kind':'symmetric-es','n':37},['6','8','37'],MIT18)
add('Divisibility among 101 selections',r'Choose 101 distinct integers from $\{1,\ldots,200\}$. Prove that one divides another, and show that 100 selections need not have this property.',[
 'Write each selected integer as a power of two times its odd part. The possible odd parts are the 100 odd integers from 1 through 199.',
 'Two distinct selections share an odd part. Their powers of two differ, so the smaller divides the larger.',
 'The 100 integers from 101 through 200 form a counterexample: a proper multiple of any of them exceeds 200. Hence the threshold 101 is exact.',
 'Grouping by parity alone would only prove matching parity, not divisibility.'],101,{'kind':'divisibility-threshold','n':100},origin=TO)
add('Triangle proximity and a counterexample',r'What is the minimum number of points in a closed unit equilateral triangle that forces two at distance at most $1/2$?',[
 'Joining the side midpoints partitions the triangle into four equilateral cells of side one-half. Assign any shared boundary point to the first containing cell in a fixed ordering.',
 'Five points place two in one cell, whose diameter is one-half. Therefore five suffice.',
 r'The three vertices and the centroid give four points with smallest pair distance $1/\sqrt3>1/2$. Thus four do not suffice.',
 'A strict distance smaller than one-half is not what the cell-diameter proof establishes.'],5,{'kind':'triangle-threshold'},['4','6','8'],OX)
add('Saturated workshop attendance',r'Twenty people attend at most three of four workshops. The four attendance totals are 18,16,14,12. How many people necessarily attend at least one of any two specified workshops?',[
 r'The total number of attendance incidences is $18+16+14+12=60$. The sum of personal capacities is $20\cdot3=60$.',
 'Every person must therefore reach the capacity three: if one attended fewer, no other person could compensate by attending more than three.',
 'A person missing both specified workshops could attend at most the other two, contradicting exactly three. Thus all twenty satisfy the conclusion.',
 'This does not imply everyone attends both specified workshops; some can miss one of them.'],20,{'kind':'saturation','capacities':[3]*20,'total':60},origin=ST)
add('The friends-and-strangers threshold',r'Find the least party size forcing either three mutual acquaintances or three mutual strangers. Every pair has exactly one of the two relationships.',[
 'At a person in a six-person party, the five incident relationships have two labels, so at least three share a label. Suppose these are acquaintance relationships to three people.',
 'If any pair among those three are acquaintances, that pair and the chosen person form a mutual-acquaintance triple. Otherwise the three are mutual strangers.',
 'For five people, let acquaintance edges form a five-cycle. Its complement is another five-cycle; neither contains a triangle. Thus five fail and six suffice.'],6,{'kind':'ramsey-threshold'},['5','7','8'],ST)
add('Sevens followed by zeros',r'Construct a positive multiple of 8 consisting of one or more decimal digits 7 followed by one or more zeros. Explain the residue collision.',[
 r'The numbers 777 and 7777 both have remainder 1 modulo 8. Their difference is $7777-777=7000$.',
 r'The quotient is $7000/8=875$. Removing a common suffix of three sevens produces one seven followed by three zeros, so the requested form is satisfied.',
 'An all-sevens multiple of 8 is impossible because its last digit is odd. The zeros cannot be discarded without checking coprimality with the decimal base.'],7000,{'kind':'seven-multiple','m':8,'value':7000},origin=MIT)
add('Products as modular labels',r'A set has ten positive indexed elements. Show that two distinct index subsets have congruent products modulo 512. Must common factors be cancelable?',[
 r'There are $2^{10}=1024$ index subsets, including the empty subset whose product is 1. Product remainders have only 512 labels.',
 'A repeated label is unavoidable, irrespective of whether the values are coprime to 512. The subsets are distinct even if some numerical values repeat.',
 r'Cancellation is a separate issue. If the common product has a factor 2, it is not invertible modulo 512; a congruence $cu\equiv cv$ does not then imply $u\equiv v$.',
 'The proof asserts a pair of subset products, not necessarily a single nonempty subset with product zero modulo 512.'],'Collision guaranteed; cancellation not guaranteed',{'kind':'subset-residue-bound','n':10,'m':512},origin=OX)
add('Two directions of the average bound',r'Forty-three objects occupy eight bins. Give the largest guaranteed lower bound on a maximum and the smallest guaranteed upper bound on a minimum.',[
 r'Write $43=5\cdot8+3$. The maximum is at least 6 and the minimum is at most 5.',
 'A vector with three sixes and five fives attains these endpoints. It proves no stronger universal maximum lower bound or minimum upper bound is possible.',
 'The class meeting the large-occupancy conclusion and the class meeting the small-occupancy conclusion need not be the same.'],'Maximum at least 6; minimum at most 5',{'kind':'average','n':43,'k':8},difficulty='Medium')
add('Forcing five in any bin',r'What is the smallest number of objects that forces at least five in one of seven unrestricted bins?',[
 r'Avoiding the target allows at most four per bin, so at most $7\cdot4=28$ objects. The twenty-ninth forces a violation.',
 'Four in every bin realizes the avoiding total 28, proving minimality. Empty bins do not invalidate the upper-capacity argument.',
 'The alternative 35 imposes five everywhere in a balanced picture rather than five somewhere under every placement.'],29,{'kind':'threshold','k':7,'r':5},['28','35','12'])
add('The target one boundary',r'With five available bins and empty bins allowed, what total first guarantees that some bin contains at least one object?',[
 'A total of zero permits all five bins to be empty, so it fails.',
 'A total of one places its only object into one bin, satisfying the existential target. The formula five times zero plus one agrees.',
 'This says nothing about all bins being occupied; surjectivity is a different property.'],1,{'kind':'threshold','k':5,'r':1},['0','5','6'],difficulty='Medium')
add('Finite inventory defeats uniform capacities',r'Tokens have color inventories $(2,7,9)$. How many draws without replacement guarantee four of some color?',[
 r'Avoidance uses at most $\min(2,3)+\min(7,3)+\min(9,3)=8$ tokens.',
 'The selection with color counts two, three, three avoids the target and is available. A ninth draw cannot remain within all three avoidance caps.',
 'Red cannot reach four, so the witness must be blue or green. Applying three equal avoidance capacities would overestimate the threshold.'],9,{'kind':'inventory','stocks':[2,7,9],'targets':[4,4,4]},['8','10','12'])
add('A specified color is a different target',r'With inventories red 2, blue 7, green 9, how many draws guarantee at least four blue tokens?',[
 'An adversary first draws every nonblue token, eleven in total, and then three blue tokens. These fourteen draws still avoid four blue.',
 'The next draw is blue because only blue tokens remain, so fifteen suffice and are necessary.',
 'The threshold nine for four of any color does not answer this specified-color question.'],15,{'kind':'specified','stocks':[2,7,9],'index':1,'r':4},['9','14','18'])
add('Forcing three distinct colors',r'With positive inventories $(2,7,9)$, find the first draw count forcing all three colors to appear.',[
 'To avoid three colors, draw from at most two. The two largest inventories are nine and seven, so an avoiding selection can have sixteen tokens.',
 'Seventeen draws require a token of the remaining color. Drawing all blue and green tokens shows sixteen are insufficient.',
 'Capping each color at one or two would answer repeated occupancy, not the number of distinct colors represented.'],17,{'kind':'distinct-colors','stocks':[2,7,9],'t':3},['3','16','18'])
add('An unavailable goal',r'Can any feasible draw count from inventories $(2,7,9)$ force ten tokens of one color?',[
 'Every inventory is less than ten, so even drawing the entire stock yields no color with ten.',
 r'The avoiding maximum is $2+7+9=18$, equal to the physical total. The formal next integer 19 cannot be drawn.',
 'Report the guarantee as infeasible; do not report 19 as a minimum legal number of draws.'],'Infeasible',{'kind':'inventory','stocks':[2,7,9],'targets':[10,10,10]},['18','19','30'])
add('Different targets for different bins',r'Inventories are $(2,7,9)$ and the targets are respectively $(3,5,4)$. Find the first feasible total forcing at least one target to be reached.',[
 r'The avoidance capacities are $(2,4,3)$, because each cap is the minimum of inventory and one less than its target. Their total is 9.',
 'The vector two, four, three is a legal nine-draw counterexample. Ten draws are feasible because the physical stock is eighteen and some target remains attainable.',
 'The first target three is impossible in inventory two, but the second and third targets can still force the disjunction.'],10,{'kind':'inventory','stocks':[2,7,9],'targets':[3,5,4]},['9','12','13'])
add('How many bins must be heavy?',r'Eight bins each have capacity six. Place 31 objects. A bin is heavy when it contains at least three. Find the minimum possible number of heavy bins.',[
 r'If $h$ bins are heavy, the total is at most $6h+2(8-h)=16+4h$. Hence $31\le16+4h$, giving $h\ge4$.',
 'The vector six, six, six, five, two, two, two, two totals 31 and has exactly four heavy bins. All capacities are respected.',
 'A simple ceiling of 31 divided by eight only forces one large bin; it does not determine the number of heavy bins.'],4,{'kind':'heavy','n':31,'k':8,'capacity':6,'r':3},['1','3','5'])
add('Full capacity implies every bin is heavy',r'Place twenty objects in five bins of capacity four. How many bins contain at least three?',[
 'The total equals the sum of the capacities. Every deficit from four is nonnegative and the deficits sum to zero.',
 'All five bins therefore contain exactly four objects, and all are heavy.',
 r'The general heavy-bin bound also gives $\lceil(20-5\cdot2)/(4-2)\rceil=5$, consistent with saturation.'],5,{'kind':'heavy','n':20,'k':5,'capacity':4,'r':3},['1','3','4'])
add('No heavy bin at the boundary',r'Place ten objects in five bins of capacity four. A heavy bin means at least three objects. What is the minimum heavy-bin count?',[
 'The vector two, two, two, two, two has total ten and no heavy bin.',
 'A heavy-bin count is nonnegative, so this construction attains the minimum zero.',
 'The strict excess condition matters: ten equals five times the largest allowed nonheavy occupancy, rather than exceeding it.'],0,{'kind':'heavy','n':10,'k':5,'capacity':4,'r':3},['1','2','3'])
add('Unequal saturation',r'Three bins have capacities $(2,3,5)$ and jointly contain ten objects. Determine their occupancies.',[
 'Write the three deficits from capacity. They are nonnegative integers whose sum is two plus three plus five minus ten, namely zero.',
 'Every deficit is zero, giving occupancy two, three, five. The conclusion does not require equal capacities or a uniform average.',
 'The balanced unrestricted vector would violate the first capacity, so unrestricted balancing is not the relevant construction.'],'2,3,5',{'kind':'saturation','capacities':[2,3,5],'total':10})
add('Strictness when the mean is an integer',r'Twenty-one objects occupy seven unrestricted bins. Is a bin with more than three objects forced?',[
 'The mean is three. The distribution with exactly three in every bin is allowed and has no occupancy strictly above the mean.',
 'Therefore the strict claim is false, although the weak claim at least three is true.',
 'In any particular distribution, a value above the mean exists if and only if one below it exists. The equal vector has neither.'],'Not forced',{'kind':'strict-average','n':21,'k':7},['Forced in every distribution','Every bin is above the mean','Every bin is below the mean'])
add('Nonintegral mean forces both strict directions',r'Twenty-two objects occupy seven bins. Must some bin be above the mean and another below it?',[
 r'The mean is $22/7$, which is not an integer. Integer occupancies cannot all equal this value.',
 'If no occupancy were above the mean, every occupancy would be at most three and the total at most twenty-one, a contradiction. Thus an above-average occupancy exists.',
 'If none were below the mean, every occupancy would be at least four and the total at least twenty-eight. A below-average occupancy also exists.'],'Both are forced',{'kind':'strict-average','n':22,'k':7},['Only the above direction is forced','Only the below direction is forced','Neither is forced'])
add('Fractional loads cannot be rounded into objects',r'Two servers carry total real load 0.8. Does the pigeonhole average prove a server carries at least one unit?',[
 'A server must carry at least the mean 0.4, but the loads need not be integers.',
 'The vector 0.4,0.4 meets the total and has no load of one. Thus rounding the mean upward to one is invalid.',
 'The ceiling bound applies to discrete counts; real weights retain the unrounded average inequality.'],'No; 0.4 is the sharp lower bound',{'kind':'real-load'},['Yes, by taking the ceiling','Yes, if the loads are equal','No server can reach 0.4'])
add('Capacity-weighted utilization',r'Bins have positive capacities $(2,4,6)$ and nonnegative loads totaling nine. What maximum-utilization lower bound follows, where utilization is load divided by capacity?',[
 r'If every utilization were less than $9/(2+4+6)=3/4$, multiply each inequality by its positive capacity and add. The total load would be less than nine.',
 'Thus some utilization is at least three-quarters. Loads one-and-a-half, three, four-and-a-half attain equality if real loads are permitted.',
 'An unweighted mean of the three utilizations does not equal nine divided by total capacity unless extra relations are assumed.'],'3/4',{'kind':'utilization','loads':9,'capacities':[2,4,6]},['1/2','9/3','1'])
add('Twenty-one unavoidable pairs',r'Seventeen distinct objects map to five labels. Find the minimum number of unordered pairs with equal labels.',[
 r'Write $17=3\cdot5+2$. Convex exchange balances the occupancies, yielding two bins of size four and three of size three.',
 r'The pair total is $2\binom42+3\binom32=12+9=21$. Any transfer from a bin at least two larger to a smaller bin lowers the total, proving minimality.',
 'The answer counts pairs, not bins or the largest fiber. A largest fiber of four alone would prove only six pairs.'],21,{'kind':'pairs','n':17,'k':5},['6','5','20'])
add('Actual pairs in an unbalanced vector',r'Occupancies are $(5,4,1)$. Count equal-label unordered pairs.',[
 r'A pair must come from one fiber, so the count is $\binom52+\binom42+\binom12=10+6+0=16$.',
 'Products such as five times four count cross-label pairs and are irrelevant to equality of labels.',
 'The total ten objects alone does not determine the actual pair count; the distribution must be used.'],16,{'kind':'actual-tuples','occupancies':[5,4,1],'t':2},['10','20','45'])
add('The opposite extremum for pairs',r'What is the maximum equal-label pair count for twenty objects in seven unrestricted bins?',[
 r'There are only $\binom{20}{2}=190$ unordered object pairs in total, giving an absolute upper bound.',
 'Placing every object in one bin makes every pair share its label, attaining that bound.',
 'Balanced placement minimizes the pair count; using it to maximize would reverse the exchange argument.'],190,{'kind':'max-pairs','n':20,'k':7},['19','21','140'])
add('The minimum number of monochromatic triples',r'Seventeen objects map to five labels. Find the minimum number of three-element object subsets with a common label.',[
 'Balancing does not increase the sum of triple counts: the marginal cost of adding to a bin of size x is the number of its two-element subsets, which is nondecreasing in x.',
 r'The balanced occupancies four, four, three, three, three contribute $2\binom43+3\binom33=8+3=11$.',
 'This is an attaining construction. For triples, marginal ties at small occupancies can make other minimizers possible, so uniqueness is not implied.'],11,{'kind':'tuples','n':17,'k':5,'t':3},['5','6','21'])
add('Balanced pairs with a nonzero remainder',r'Eighteen objects map to four labels. Find the smallest collision-pair count.',[
 r'Division gives $18=4\cdot4+2$. Two occupancies are five and two are four in a balanced minimizing vector.',
 r'The total is $2\binom52+2\binom42=20+12=32$, equivalently $4\binom42+2\cdot4$.',
 'Rounding the average to five and pretending all four bins have five objects changes the total to twenty and overcounts.'],32,{'kind':'pairs','n':18,'k':4},['24','30','40'])
add('A capacity changes the pair minimum',r'Six objects occupy two bins with capacities one and nine. Find the minimum pair count.',[
 'The first occupancy can only be zero or one. If it is zero, the second is six and contributes fifteen pairs.',
 'If it is one, the second is five and contributes ten pairs. This is feasible and is the smaller value.',
 'The unrestricted balanced vector three,three would give six pairs but violates the first capacity. A legal extremal witness is indispensable.'],10,{'kind':'bounded-pairs','n':6,'capacities':[1,9]},['6','9','15'])
add('A fixed-width hash range',r'What is the least number of distinct keys that forces a collision for every function returning a 12-bit hash?',[
 r'There are $2^{12}=4096$ possible output words. An injection from 4097 keys into these outputs is impossible.',
 'With 4096 keys, a function can assign each a different output. Thus 4097 is the exact universal threshold.',
 'This does not claim a particular hash function first collides at that input count; it may collide much earlier.'],4097,{'kind':'hash','bits':12},['4096','4095','2049'])
add('Many keys and few outputs',r'Six distinct keys map to four output labels. Find the minimum number of collision pairs.',[
 r'The balanced vector is $(2,2,1,1)$, giving one pair from each doubleton and none from the singletons.',
 'The minimum is two. A distribution with one triple would instead have three pairs, showing that counting only repeated bins can be misleading.',
 'This is a guarantee over all functions with that codomain, not a random-output expected value.'],2,{'kind':'pairs','n':6,'k':4},['1','3','15'])
add('A small domain can be collision free',r'Five distinct keys map to eight labels. Which deterministic collision claim follows from sizes alone?',[
 'There are enough labels to assign distinct outputs to all five keys, so collision is not forced.',
 'A constant function also causes many collisions, so collision is not impossible. Both types of functions satisfy the stated sizes.',
 'A birthday-model probability would require a random-function or random-output assumption that is absent here.'],'Neither collision nor collision-freedom is forced',{'kind':'function','n':5,'k':8},['A collision is forced','Collision is impossible','Every label is used'])
add('Four equal birthdays',r'Under 366 possible birthday dates, what is the least group size forcing four people with a common birthday?',[
 r'To avoid four, each date can have at most three people. The avoiding total is $366\cdot3=1098$.',
 'One more person forces a date with four, while exactly three per date is a counterexample at 1098.',
 'The leap-day convention changes the number of labels; replacing 366 by 365 answers a different model.'],1099,{'kind':'threshold','k':366,'r':4},['1098','1464','1100'])
add('Strictly shorter binary codes',r'How many distinct ten-bit messages can at most be assigned injectively to binary strings of length strictly less than ten, when the empty string is permitted?',[
 r'The available output count is $1+2+\cdots+2^9=2^{10}-1=1023$. Injectivity cannot assign more messages than that.',
 'This bound is attained for a chosen restricted set of 1023 messages by matching them bijectively to the 1023 short outputs.',
 'All 1024 ten-bit messages cannot be shortened at once. Counting only outputs of length nine would miss the shorter permitted outputs; counting length ten would violate strict shortening.'],1023,{'kind':'short-codes','n':10},['512','1024','1022'])
add('Convert a prefix collision into indices',r'For modulus five and values $(3,4,2,7,1)$, scan prefixes from the start and use the first repeated remainder. Give the resulting one-based block and its sum.',[
 'Prefix remainders including the empty prefix are zero,three,two,four,one,two. The first collision pairs prefix indices two and five.',
 'Subtracting these prefixes retains entries three through five, not entry two. Their sum is two plus seven plus one, namely ten.',
'The endpoints are ordered and different, so the block is nonempty. Ten is divisible by five, providing a verifiable certificate.'],'Positions 3–5; sum 10',{'kind':'prefix','values':[3,4,2,7,1],'m':5})

add('Difference versus sum',r'Eight integers are selected. What is forced modulo seven: a divisible difference or a divisible sum?',[
'The eight positions have only seven remainder labels. Two different positions therefore have equal remainders.',
r'Subtracting their values gives remainder zero. Adding their values instead gives twice their common remainder, which need not be zero.',
'For a counterexample to the sum claim, choose eight distinct integers all congruent to one modulo seven. Every two-element sum has remainder two.'],'A divisible difference, not necessarily a divisible sum',{'kind':'difference','n':8,'m':7})
add('Equal remainders need not sum to zero',r'The numbers 1 and 6 have the same remainder modulo five. Does their sum or their difference give a zero remainder?',[
'Both remainder labels are one. The difference six minus one is five and is divisible by five.',
'The sum is seven and has remainder two. The equality of labels supports subtraction, not arbitrary combination.',
'For a sum argument one instead groups complementary remainders, taking care with remainder zero and a possible self-complementary class.'],'Difference only',{'kind':'remainder-counterexample'})
add('Too few prefix objects',r'For modulus five, do the four values $(1,1,1,1)$ contain a nonempty contiguous block with sum divisible by five?',[
'Their five prefix remainders, including the empty prefix, are zero,one,two,three,four. No remainder repeats.',
'Every nonempty block has length between one and four and, because all entries are one, has the same sum as its length. None is divisible by five.',
'The usual universal theorem needs five input values and hence six prefix objects. Having five objects in five classes does not force collision.'],'No',{'kind':'no-prefix','values':[1,1,1,1],'m':5},['Yes','Only the full block','Only singletons'])
add('The first all-ones multiple',r'Find the shortest positive decimal all-ones multiple of seven.',[
'Compute the remainders of repunits recursively: one,four,six,five,two,zero for lengths one through six.',
r'The first zero occurs at length six, giving $111111=7\cdot15873$. The nonzero earlier remainders prove shortest length.',
'A repeated nonzero remainder would also yield an all-ones multiple after subtraction and valid cancellation of a power of ten. The direct zero remainder here already supplies the shortest witness.'],'111111',{'kind':'repunit','m':7},['11111','1111111','1110'])
add('A zero-one multiple without decimal invertibility',r'Use a repeated repunit remainder to construct a decimal zero-one multiple of six.',[
'The repunits of lengths one and four have equal remainder one modulo six. Their difference is 1111 minus 1, namely 1110.',
r'This difference is $6\cdot185$. It has only zero and one digits and is positive.',
'An all-ones multiple cannot exist because every repunit is odd. Multiplication by ten cannot be canceled modulo six; that obstruction is compatible with the zero-one construction.'],'1110',{'kind':'zeroone','m':6,'value':1110})
add('A base obstruction',r'Can a positive decimal repunit be divisible by ten?',[
'Its final digit is one, so its remainder modulo ten is one, irrespective of length.',
'Therefore no positive length works. The existence theorem for all-ones multiples requires the modulus to be coprime with ten.',
'The broader zero-one theorem remains true: ten itself is a zero-one multiple. The two statements have different hypotheses.'],'Impossible',{'kind':'repunit-obstruction','m':10},['Length ten works','Length eleven works','Every length works'])
add('Modular cancellation needs a unit',r'Modulo six, $2\cdot1\equiv2\cdot4$. May the factor two be canceled?',[
'Both products have remainder two, but one and four have different remainders. Thus cancellation would assert a false congruence.',
r'The factor has $\gcd(2,6)=2$ and has no multiplicative inverse modulo six. Cancellation would only yield equality modulo three here.',
'In a prime modulus every nonzero factor is a unit; in a composite modulus nonzero alone is insufficient.'],'No',{'kind':'cancellation','m':6,'a':1,'b':4,'c':2},['Yes, because two is nonzero','Yes, in any modulus','Only if both products are positive'])
add('Overlapping square images',r'How many residues occur as $x^2$ modulo eleven, and why does $x^2+y^2\equiv-1\pmod{11}$ have a solution?',[
'The square image is zero,one,three,four,five,nine: six values. Pairing each nonzero x with its negative explains the image size six.',
'The second image minus one minus a square also has six values in an eleven-element universe. Two six-element subsets must intersect.',
'One certificate is x equals one and y equals three: their squares sum to ten, which equals minus one modulo eleven. This is an existence proof plus a checked witness.'],'6 residues; a solution exists',{'kind':'square-prime','p':11},origin=OX)
add('The exceptional prime two',r'For modulus two, verify the square-sum statement and explain why $(p+1)/2$ is not the right image-size argument.',[
'Both residues zero and one are their own squares. The square image has two elements, whereas the odd-prime formula would give a noninteger three-halves.',
'Choose x equals one and y equals zero. Their square sum is one, which is minus one modulo two.',
'The theorem includes prime two through a separate direct case. An argument pairing distinct nonzero opposites cannot be used because one equals its negative here.'],'x=1, y=0',{'kind':'square-two'})
add('A composite counterexample',r'Does $x^2+y^2\equiv-1\pmod8$ have an integer solution?',[
'The square residues modulo eight are zero,one,four. Adding two members gives only zero,one,two,four,five as possible remainders.',
'The required remainder seven is missing, so no pair solves the congruence.',
'The prime-image proof fails: the square image is not large enough and nonzero residues need not have just two square roots. This counterexample prevents extending the prime result to arbitrary moduli.'],'No solution',{'kind':'square-composite','m':8},['A solution exists','Only x=y works','Only odd x and odd y work'])
add('Equal sums with an explicit cancellation',r'For indexed values $(1,2,3,4)$, give two disjoint nonempty equal-sum subsets and explain the counting proof.',[
r'The sixteen index subsets have sums in the eleven labels zero through ten. A collision follows from $16>11$.',
'The subsets containing values one and four, and values two and three, both sum to five and are disjoint.',
'If a counting collision initially shared indices, subtract their common contribution from both sides. Positivity ensures neither residual side is empty when the original subsets are distinct.'],'1+4=2+3',{'kind':'equal-subsets','values':[1,2,3,4]})
add('Equality at the image-size bound',r'For values $(1,2,4,8)$, do two distinct index subsets have equal sums?',[
'Their sixteen subset sums are exactly the integers zero through fifteen. Binary expansion supplies a different sum for every subset.',
'The number of objects equals the number of possible labels, so collision is not forced, and in this example it does not occur.',
'A non-strict comparison cannot replace the strict image-size inequality. The empty subset is still a legitimate object with sum zero.'],'No',{'kind':'unique-subsets','values':[1,2,4,8]},['Yes, because sixteen labels exist','Only with empty subsets','Every two subsets collide'])
add('Fixed-cardinality subset sums',r'Among four-element subsets of $\{1,\ldots,8\}$, show that at least two have equal sum.',[
r'There are $\binom84=70$ objects. Their sums range from ten to twenty-six inclusive, so there are at most seventeen sum labels.',
'Seventy exceeds seventeen; therefore two distinct four-element subsets have the same sum. For example one,two,seven,eight and one,three,six,eight both sum to eighteen.',
'Canceling the common values one and eight yields two plus seven equals three plus six. Equal size survives cancellation, although the residual size need not remain four.'],'Guaranteed',{'kind':'fixed-subsets','n':8,'t':4})
add('A subset collision is not a zero sum',r'For indexed values $(2,2)$ modulo three, two singleton subset sums coincide. Must a nonempty subset have sum zero?',[
'The two singleton index subsets are distinct and each has remainder two, so a collision exists.',
'The nonempty sums are two,two,four, whose remainders are two,two,one. None is zero.',
'Subtracting collided sums gives equality between two disjoint subsets, not a positive sum of selected entries. The contiguous-prefix theorem has an additional nesting property that arbitrary subsets lack.'],'No',{'kind':'no-zero-subset','values':[2,2],'m':3},['Yes, by subtracting labels','Yes, the pair works','Only a singleton works'])
add('Cancelable product images',r'Take indexed values $(2,3,4,5,6)$ modulo seventeen. Show that two distinct subsets have equal product remainder and state what cancellation preserves.',[
'There are thirty-two subsets and seventeen remainder labels, so distinct subsets collide. The empty product is one.',
'Every chosen value is nonzero modulo the prime seventeen and hence invertible. The product of common indices is also invertible and may be canceled.',
'The residual subsets are disjoint and remain distinct. One side can be empty, since positivity of ordinary products does not exclude a nonempty modular product of one.'],'Collision with valid cancellation',{'kind':'unit-subsets','values':[2,3,4,5,6],'m':17})
add('Why positivity was stated',r'The indexed list consists only of the value zero. Two subset sums coincide. Does this yield two disjoint nonempty equal-sum subsets?',[
'The empty subset and the singleton both sum to zero. These are the only subsets.',
'Two disjoint nonempty subsets are impossible because there is only one index. The collision therefore cannot meet the strengthened conclusion.',
'Strictly positive entries rule out an empty residual side with sum equal to a nonempty side; nonnegative entries alone do not.'],'No',{'kind':'zero-subset-counterexample'})
add('Complementary pairs without a fixed point',r'What is the least number of distinct selections from 1 through 20 that forces a pair summing to 21?',[
'Partition the twenty values into ten disjoint complement pairs: one with twenty through ten with eleven.',
'Eleven distinct selections force two in one pair. Ten can avoid the target by taking exactly one member per pair, for example one through ten.',
'The bins contain two distinct complementary values; choosing repeated copies of one value would not provide the same proof.'],11,{'kind':'complement','H':20,'sum':21},['10','12','20'])
add('A self-complementary value changes the count',r'What is the least number of distinct selections from 1 through 21 forcing two distinct selected values summing to 22?',[
'There are ten two-element complement pairs and the singleton eleven. The singleton cannot supply a pair of distinct values.',
'An avoiding selection may take one value from each pair and also eleven, giving eleven selected values. Twelve force a completed pair.',
'The values one through eleven give an attaining counterexample at eleven. Treating the singleton as an ordinary two-element pair would create a false answer.'],12,{'kind':'complement','H':21,'sum':22},['11','10','21'])
add('Construct the actual divisibility witness',r'Find a divisibility pair in $(4,5,6,7,8,10,11,12)$ by grouping odd parts.',[
'The odd parts are respectively one,five,three,seven,one,five,eleven,three.',
'The first repeated odd part is one at values four and eight. The smaller divides the larger, with quotient two.',
'There are other witnesses: five divides ten, and six divides twelve. Equal parity by itself would not identify these divisibility chains.'],'4 divides 8',{'kind':'odd-witness','values':[4,5,6,7,8,10,11,12]})
add('The sharp avoiding half interval',r'Why do the twenty values 21 through 40 contain no pair of distinct values where one divides the other?',[
'A proper positive multiple of a selected value is at least twice that value, hence at least forty-two.',
'Every selected value is at most forty, so such a multiple cannot lie in the selection.',
'The full interval one through forty has twenty odd-part chains. This example attains one value from each without a divisibility pair, proving the twenty-one threshold sharp.'],'No proper multiple remains in the interval',{'kind':'divfree','L':21,'H':40})
add('Consecutive integers with an odd endpoint',r'Find the smallest number of distinct selections from 1 through 15 forcing two consecutive integers.',[
'An avoiding set can contain the eight odd values one,three through fifteen. Thus eight are insufficient.',
'Group the interval into seven adjacent pairs and the singleton fifteen. At most one selection from each of these eight groups avoids completing an adjacent pair.',
'Nine force a completed pair. Other consecutive pairs cross group boundaries, but ignoring them cannot invalidate this sufficient bound, and the odd set proves sharpness.'],9,{'kind':'consecutive','H':15},['8','10','15'])
add('Consecutiveness supplies a coprime witness',r'Show that eleven distinct selections from 1 through 20 force a coprime pair, and show ten may fail.',[
'The ten adjacent pairs one,two through nineteen,twenty force a completed pair under eleven selections.',
'Consecutive integers have greatest common divisor one, so the pair is a coprime witness.',
'The ten even values have pairwise greatest common divisor at least two. They prove that ten cannot give the universal coprime guarantee.'],11,{'kind':'coprime-threshold','H':20},origin=OX)
add('Chains by powers of three',r'Choose 201 distinct positive integers less than 300. Show that the quotient of two is a positive integral power of three.',[
'Write each value uniquely as a power of three times a core not divisible by three.',
'Among one through 299, there are 299 minus ninety-nine, namely two hundred possible cores. Two hundred and one selections force equal cores.',
'Distinct values with one core have different exponents. Dividing the larger by the smaller gives three raised to a positive exponent. This establishes sufficiency without claiming the selected number is the unique sharp threshold for every variant.'],200,{'kind':'base-cores','H':299,'base':3},origin=MIT)
add('A sufficient grid threshold is not an optimum theorem',r'Use a square grid to force two points in a closed unit square at distance at most one-quarter. What is the best threshold from this equal-grid method?',[
r'With r divisions along each axis, the cell diameter is $\sqrt2/r$. To make it at most one-quarter, r must be at least six.',
'The six-by-six grid has thirty-six cells. Thirty-seven points force two in one cell, whose distance meets the requested bound.',
'This is the least threshold among these equal axis-aligned grids. It is not a proof that thirty-seven is the smallest threshold among all geometric arguments or all point configurations.'],37,{'kind':'grid','distance':0.25},['36','33','17'])
add('A rectangular partition',r'A closed rectangle has side lengths six and four. Divide it into three columns and two rows. How many points suffice to force distance at most $2\sqrt2$?',[
'The partition has six cells, each a square of side two and diameter two times the square root of two.',
'Assign shared-boundary points to a fixed containing cell. Seven points force two in the same cell and hence the stated distance bound.',
'Six points need not collide in a cell, but that observation alone does not prove the global geometric threshold is seven. The claim is sufficient, tied to this partition.'],7,{'kind':'rectangle-grid','cols':3,'rows':2},['6','8','12'])
add('A numerical approximation certificate',r'For $\alpha=\sqrt2$ and m equals five, exhibit integers q,p with one at most q at most five and $|q\alpha-p|<1/5$.',[
'The fractional parts of zero through five multiples of the square root of two share one of five half-open interval labels. In particular the fractional parts at indices zero and five are close.',
r'Take q equal to five and p equal to seven. The error is $5\sqrt2-7$, about 0.071068, which is positive and less than 0.2.',
r'Dividing by q gives $|\sqrt2-7/5|<1/25$. The theorem bounds this rational error by $1/(mq)$, not by the original unscaled $1/m$.'],'q=5, p=7',{'kind':'approximation','m':5,'q':5,'p':7})
add('A rational boundary case',r'Use m equals two and $\alpha=1/2$ to find a prefix-fraction collision and its approximation witness.',[
'The fractional parts at indices zero,one,two are zero,one-half,zero. In two half-open intervals, zero belongs to the first and one-half to the second.',
'The equal first and third fractional parts give q equals two and p equals one. Their approximation error is exactly zero.',
'This remains a valid strict error less than one-half. Half-open intervals eliminate boundary ambiguity without excluding repeated fractional values.'],'q=2, p=1',{'kind':'rational-approximation','m':2,'q':2,'p':1})
add('An asymmetric monotone threshold',r'Find the least length forcing a strictly increasing subsequence of length five or a strictly decreasing subsequence of length seven, when all entries are distinct.',[
'Avoidance requires increasing ending length at most four and decreasing ending length at most six. Each distinct entry receives a different ordered pair of these labels.',
'The twenty-four possible pairs permit at most twenty-four entries. Twenty-five force the desired conclusion.',
'Four descending blocks of six values, with every block larger than the preceding block, attain twenty-four without either target. This proves necessity as well as sufficiency.'],25,{'kind':'es','r':5,'s':7},['24','35','36'],TO)
add('A sharp short monotone construction',r'For the sequence $(2,1,4,3,6,5)$, compute the longest increasing and decreasing subsequence lengths.',[
'An increasing subsequence takes at most one value from each descending two-element block. Taking one,two-block representative values one,three,five attains length three.',
'A decreasing subsequence cannot cross into a later block, because every later value is larger. Inside a block its length is at most two, attained by two,one.',
'Thus LIS is three and LDS is two. Six is the sharp avoiding length for targets increasing four or decreasing three.'],'LIS 3; LDS 2',{'kind':'lis','values':[2,1,4,3,6,5]},['LIS 4; LDS 2','LIS 3; LDS 3','LIS 2; LDS 3'])
add('The square boundary',r'For one hundred distinct real values, what monotone subsequence length is forced? At what first length is eleven forced?',[
'The largest integer guarantee at length one hundred is ten: the ceiling of the square root is ten.',
'Ten descending blocks of ten values avoid length eleven in either direction. At length one hundred and one, one hundred available label pairs are insufficient, so eleven is forced.',
'Using the floor of the square root works at perfect squares but fails immediately after them.'],'10 at 100; 11 first at 101',{'kind':'es-square','n':100})
add('Duplicate values break the strict theorem',r'A sequence has twenty equal values. Does the distinct-entry monotone theorem force a strictly monotone subsequence of length five?',[
'Every strict increasing or strict decreasing subsequence has length one, because every comparison is equality.',
'Its weakly nondecreasing subsequence has length twenty. The weak conclusion differs from the strict one.',
'With duplicates one can use a mixed nondecreasing/decreasing theorem, or explicitly specify tie handling. The distinctness hypothesis cannot simply be deleted.'],'No; strict maximum is one',{'kind':'duplicate-es','n':20},['Yes, strict length five','Yes, strict length twenty','No weak subsequence exists'])
add('Audit ending-length labels',r'For $(5,1,4,2,3)$, calculate increasing and decreasing lengths ending at each position.',[
'Increasing ending lengths are one,one,two,two,three. Each is one plus the greatest earlier length whose value is strictly smaller.',
'Decreasing ending lengths are one,two,two,three,three, using strictly larger predecessors instead.',
'The five ordered labels are distinct and the maxima are both three. A label proof uses ending lengths consistently; mixing starting and ending conventions without proof can destroy its implication.'],'LIS 3; LDS 3',{'kind':'lis','values':[5,1,4,2,3]})
add('Subsequence does not mean contiguous',r'For $(1,4,2,5,3,6)$, compare the longest increasing subsequence and the longest increasing contiguous block.',[
'The values one,two,three,six give an increasing subsequence of length four. Dynamic programming confirms no longer increasing subsequence exists.',
'Each drop from four to two and from five to three breaks a contiguous run. The runs one,four; two,five; three,six have maximum length two.',
'Pigeonhole monotone theorems concern subsequences and permit skipped positions. They cannot be read as contiguous-block guarantees.'],'Subsequence 4; contiguous block 2',{'kind':'lis-contiguous','values':[1,4,2,5,3,6]})
add('Degree labels and their forbidden coexistence',r'Why do nine vertices in a simple undirected graph force repeated degree, while a directed tournament can have all distinct outdegrees?',[
'The undirected degree labels are zero through eight, but zero and eight cannot coexist: a degree-eight vertex would connect to the supposedly isolated one.',
'At most eight labels are usable simultaneously for nine vertices, so a repeated degree follows.',
'Orient a nine-vertex complete graph from the lower ordered vertex to the higher. Its outdegrees are eight,seven through zero, all distinct. The undirected exclusion does not apply to outdegree.'],'Repeated undirected degree; distinct tournament outdegrees possible',{'kind':'degree','n':9},origin=ST)
add('The five-cycle Ramsey counterexample',r'Color a complete graph on five vertices red on a cycle and blue on its complement. How many monochromatic triangles occur?',[
'A five-cycle contains no triangle, so no triple has all three edges red.',
'Its complement is also a five-cycle and likewise has no triangle. Thus no triple has all edges blue.',
'The count is zero. This is an actual lower-bound certificate for the six-vertex Ramsey theorem, not merely a failure of the star argument at five.'],0,{'kind':'ramsey-cycle','n':5},['1','2','5'])
add('A sharp three-color rectangle threshold',r'A grid has four columns, arbitrary rows, and three colors. Find the least row count forcing a rectangle whose four corners have one color.',[
'Each row has four entries and only three colors, so it contains a same-color pair of columns. Choose one such pair and its color as a certificate.',
'There are six column pairs times three colors, namely eighteen certificates. Nineteen rows repeat one, producing the rectangle.',
'For each of the eighteen certificates, construct a row with its chosen pair in its chosen color and the other two cells in the other two colors. It has exactly that one same-color pair, so different rows never repeat a certificate. Eighteen avoid the rectangle, proving sharpness.'],19,{'kind':'rectangle','cols':4,'colors':3},origin=MIT)
add('The smaller rectangle construction',r'With three columns and two colors, find the sharp row threshold forcing a monochromatic rectangle.',[
'Every row has a same-color pair. Three column pairs times two colors give six possible certificates.',
'Seven rows repeat a certificate. Six avoiding rows can be formed by taking each certificate once and coloring the remaining singleton with the other color.',
'This construction works because columns equal colors plus one. For more columns, a row may realize multiple certificates, so one cannot automatically claim the same sharp construction.'],7,{'kind':'rectangle','cols':3,'colors':2},['6','8','9'])
add('Binary decision-tree information',r'At least how many arbitrary truthful yes-no answers are required in the worst case to identify one of one thousand possibilities?',[
'A binary decision tree of worst-case depth q has at most two to the q leaves. Each possibility needs a distinct leaf.',
'Nine answers support at most 512 leaves, whereas ten support 1024. Thus the minimum is ten if arbitrary subset questions are allowed.',
'A balanced identification strategy realizes this minimum. Restrictions on the permitted questions, or lies, can raise the requirement.'],10,{'kind':'binary-identification','N':1000},['9','11','1000'])
add('One lie: a necessary packing bound',r'With twenty adaptive yes-no questions and at most one lie, what possibility-count upper bound follows from transcript packing?',[
'For a fixed hidden possibility, the truthful run and each choice of one lie position yield twenty-one distinct transcripts. Distinctness follows at the first position where the lie schedules differ.',
'Transcripts belonging to different hidden possibilities must be disjoint for unique decoding. Thus the number of possibilities times twenty-one is at most two raised to twenty.',
'The integer upper bound is 49932. This is a necessary condition; no strategy attaining it has been constructed here. Adaptive transcript sets are not automatically ordinary Hamming balls around a fixed truthful word.'],49932,{'kind':'one-lie','q':20},['52428','49933','1048576'],MIT18)
add('The card channel and the impossible variant',r'From five cards in a thirteen-rank four-suit deck, one is hidden and four are ordered visibly. Explain the six-way rank code and why hiding one of only four cards cannot always work in a 52-card deck.',[
'Among five cards, two have the same suit. Their distinct ranks have one directed cyclic gap between one and six. Show the first as an anchor and hide the second.',
'The other three visible cards can be placed in six permutations under an agreed total ordering. Their order encodes the gap; the anchor supplies suit and initial rank, permitting exact decoding.',
'For the four-card variant, an ordered visible triple has at most 52 times 51 times 50 states, while hidden hands number the binomial coefficient of 52 choose 4. The latter is larger: 270725 exceeds 132600. Thus no protocol can uniquely decode every hand.',
'For the five-card variant in an arbitrary n-card deck, a necessary state-count condition gives n at most 124. That upper bound alone does not provide a construction for every such deck.'],'Six rank codes; four-card variant impossible',{'kind':'card-channel','deck':52},origin=MIT)

assert len(Q)==80,len(Q)
assert len({q['id'] for q in Q})==80
(B/'d_pigeonhole-questions.json').write_text(json.dumps(Q,indent=2)+'\n',encoding='utf-8')
actual=json.loads((B/'exam-calibration/actual-items.json').read_text())
x=next(x for x in actual if x['id']=='Phd_CS_1404_Q25').copy()
x['solution']=r'''There are $\binom{10}{4}=210$ four-element subsets. A pair has odd sum exactly when its values have opposite parity. The only failures are all-even and all-odd selections. Each parity class has five elements, so failures number $2\binom54=10$. The answer is $210-10=200$, printed option 1. Four selections do not universally force opposite parity: four even values are a counterexample. Six distinct selections would force it because either single parity class has capacity five. This authentic problem counts successful subsets; it does not ask for the universal pigeonhole threshold.'''
x['check']={'kind':'authentic-parity','H':10,'t':4};x['expected']='200';x['answer']=1
y=dict(id='MS_CS_1405_Q116',title='Worst-case search for an odd three-digit password',stem='A combination lock has an unknown odd three-digit password whose digits are chosen from 1 through 9. Each trial takes two minutes. What is the maximum time required, in hours?',options=['12','12.5','13','13.5'],answer=4,expected='13.5',origin='Authentic MSc Computer Science examination, 1405, question 116; checked English adaptation',repoPath='Exams/MS/CS/1405/Q257A-Arshad1405-[www.konkur.in].pdf',sourceSha256='198f75f9f9d195adc5c09ab14d17029e63a3cd11030d62cffcdfcb5df7627527',physicalPage=25,repositoryCommit='bdadf6e2c9cadc4772ae137a96a3da753c7cfd08',difficulty='Medium',check={'kind':'authentic-password'},solution=r'''The first two digits each have nine choices. Oddness restricts only the final digit, which has five choices: 1, 3, 5, 7, 9. Repetition is permitted because distinctness is not stated. Thus there are $9\cdot9\cdot5=405$ candidate passwords. In the worst case the correct password is the last candidate tried, and the successful final trial also takes two minutes. The time is $405\cdot2=810$ minutes, or $810/60=13.5$ hours, printed option 4. This is a finite worst-case search bridge problem, not a direct repeated-class pigeonhole question. The conclusion assumes a systematic search without repeated trials and no additional feedback eliminating candidates.''')
(B/'d_pigeonhole-authentic.json').write_text(json.dumps([x,y],indent=2)+'\n',encoding='utf-8')
print('Authored 80 original/course reconstructions and two checked authentic questions.')
