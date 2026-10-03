r"""Individually authored calculation, proof and counterexample questions."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parent
questions=[]
def add(title,stem,options,answer,solution,origin=r'Original problem',difficulty=r'Medium'):
    assert len(options)==4 and 1<=answer<=4
    questions.append(dict(id=f'AC{len(questions)+1:02}',title=title,stem=stem,options=options,answer=answer,solution=solution,origin=origin,difficulty=difficulty))

add(r'Backward substitution through a quadratic',
    r'Over exact integers, execute `x = x + 3`. What is the weakest precondition for final $x^2=25$?',
    [r'$x=5$ or $x=-5$',r'$x=2$ or $x=-8$',r'$x=8$ or $x=-2$',r'$x=2$'],2,
    r'Substitute the old expression into the final predicate: $(x+3)^2=25$. Therefore $x+3=5$ or $x+3=-5$, giving $x=2$ or $x=-8$. Both inputs produce an allowed final square. Option 1 confuses final and initial values; option 3 reverses the shift; option 4 loses the negative branch. The word weakest requires every admitted solution, not one sufficient input. This calculation assumes exact arithmetic and a defined assignment.')
add(r'Sequence order changes the precondition',
    r'Execute `x=x+1; y=2*x; x=y-3` over integers. Which initial condition is weakest for final $x=7$?',
    [r'$x=4$',r'$x=5$',r'$y=10$',r'$x=10$'],1,
    r'Work backward. The final assignment requires old $y-3=7$, hence $y=10$. The middle assignment requires $2x=10$. The first assignment then requires $2(x+1)=10$, so initial $x=4$. Initial $y$ is unconstrained because the middle statement overwrites it. A forward trace from four gives five, ten and seven, confirming the derivation. Option 2 omits the increment; option 3 constrains an overwritten value; option 4 mistakes an intermediate value for the input.')
add(r'Simultaneous versus sequential assignment',
    r'Initially $(x,y)=(5,8)$. Compare simultaneous `(x,y)=(y,x+y)` with sequential `x=y; y=x+y`. What are their respective results?',
    [r'$(8,13)$ and $(8,13)$',r'$(8,16)$ and $(8,13)$',r'$(8,13)$ and $(8,16)$',r'$(5,13)$ and $(8,16)$'],3,
    r'Simultaneous assignment evaluates both right sides in the old state, producing $(8,5+8)=(8,13)$. Sequential execution first makes $x=8$; the second statement then uses that updated value and gives $y=8+8=16$. Option 1 ignores state change; option 2 exchanges the models; option 4 fails to assign the first coordinate. A temporary old value repairs the sequential Fibonacci update.')
add(r'Conditional weakest precondition',
    r'For integer `x`, execute `if x<0: x=-x; else: x=x+2`. Which condition is weakest for final $x\ge3$?',
    [r'$x\ne0$',r'$x\ge1$',r'$x\le-3$',r'$x\le-3$ or $x\ge1$'],4,
    r'In the negative branch, $-x\ge3$ means $x\le-3$, which already implies the branch guard. In the nonnegative branch, $x+2\ge3$ means $x\ge1$. Combine the guarded branches by disjunction to obtain $x\le-3$ or $x\ge1$. Inputs negative one and negative two refute option 1. Options 2 and 3 each omit one valid branch. The postcondition must be proved on both paths, including the otherwise branch.', r'Course-derived analogue: Cambridge conditional verification, PDF pages 52–53')
add(r'Which consequence direction is sound?',
    r'A known triple has precondition $x\ge0$ and postcondition $r=x^2$. Which replacement is always justified by consequence alone?',
    [r'Precondition true; postcondition $r=x^2$',r'Precondition $x\ge2$; postcondition $r\ge0$',r'Precondition $x\ge0$; postcondition $r>x$',r'Precondition $x<0$; postcondition $r\ge0$'],2,
    r'The stronger precondition $x\ge2$ implies $x\ge0$, and the exact square postcondition implies $r\ge0$ over real or integer values. Therefore option 2 follows. Option 1 expands the input domain; option 4 changes it to an unproved domain. Option 3 strengthens the output assertion and fails at $x=0$ or $x=1$. Consequence moves assumptions toward greater restriction and conclusions toward weaker requirements.')
add(r'Array aliasing is a logical condition',
    r'Both indices are valid. Execute `A[i]=1; A[j]=2`. Which is the weakest condition on indices for final $A[i]=1$ and $A[j]=2$?',
    [r'$i<j$',r'$i>j$',r'$i\ne j$',r'No condition'],3,
    r'If indices differ, the second write cannot change the first cell, so both desired values hold. If they coincide, the last write leaves that single cell equal to two, contradicting its required equality to one. Thus inequality is both necessary and sufficient. Either strict-order alternative is sufficient but not weakest because it excludes the opposite order. The no-condition alternative assumes separate array syntax means separate memory.', r'Course-derived analogue: Cambridge array updates, PDF pages 19–22')
add(r'Invariant strength can fail at an unreachable state',
    r'Start at $(x,y)=(0,0)$ and repeatedly assign both coordinates simultaneously to $(x+1,y+1)$. Is $I:x\ge0$ by itself inductive under the transition, and is it sufficient to prove final $x=y$?',
    [r'Inductive and sufficient',r'Inductive but insufficient',r'Not inductive but sufficient',r'Neither'],2,
    r'Every state with nonnegative $x$ produces nonnegative $x+1$, so the predicate is inductive. However, it admits $(3,8)$ and gives no relationship between the coordinates. Adding $x=y$ yields a useful invariant and proves the equality at any termination checkpoint. Truth of a weak invariant does not supply an unrelated postcondition. The reachable states happen to satisfy equality, but the annotation must express it.', r'Original state-machine analogue informed by MIT §5.4')
add(r'Reachable truth need not be inductive',
    r'Start at $x=0$. The transition maps zero to zero and maps every positive $x$ to $-1$. Which describes $I:x\ge0$?',
    [r'False on a reachable state',r'True on every reachable state but not inductive',r'Inductive but false initially',r'A proof that every state is reachable'],2,
    r'The only reachable value is zero, because zero maps to itself. Thus the predicate holds on every reachable state. Yet the state $x=1$ satisfies the predicate and its successor $-1$ does not; this refutes preservation over all invariant states. Strengthening to $x=0$ removes the unreachable counterexample. Option 1 confuses possible integers with reachable ones, and option 3 reverses the failed obligation.', r'Original state-machine analogue informed by MIT §5.4', r'Hard')
add(r'A defective annotation does not condemn a program',
    r'Annotate `while False: x=0` with invariant `False`, initial assertion `True`, and final assertion `True`. Which claim is correct?',
    [r'The program diverges',r'The final assertion is false',r'Initialization of the chosen invariant fails, although the program is correct',r'Every chosen invariant proves every loop'],3,
    r'The loop executes zero bodies and terminates with the state unchanged, so the stated partial and total result is true. Nevertheless, initialization asks whether true implies false, which is invalid. A failed annotation can be repaired by using invariant true. This separates a proof artifact from program behavior. The preservation implication is vacuous here, but it cannot repair failed initialization.', r'Course-derived analogue: Cambridge Exercise 45, PDF page 58')
add(r'A loop with exact iteration count',
    r'For positive integer $n$, initialize $x=n$ and execute `while x>0: x=max(0,x-3)`. How many body executions occur?',
    [r'$\lfloor n/3\rfloor$',r'$\lceil n/3\rceil$',r'$n$',r'$\lceil(n-1)/3\rceil$'],2,
    r'After $t$ bodies, $x=\max(0,n-3t)$. Termination first occurs when $3t\ge n$, whose smallest integer solution is $\lceil n/3\rceil$. For $n=1$ the result is one, ruling out both floor and the fourth expression. The variant decreases by at least one at a true guard, but its initial value only gives a coarse upper bound; the exact state formula gives the precise count.')
add(r'Strict decrease over reals is insufficient',
    r'Start $x=1$ and repeat `while x>0: x=x/2` in exact real arithmetic. Which is correct?',
    [r'The loop terminates after one step',r'It terminates after finitely many steps because $x$ decreases',r'It does not terminate; nonnegative real strict descent is not well-founded',r'It violates $x\ge0$'],3,
    r'After $t$ steps, $x=2^{-t}>0$ for every finite integer $t$, so the guard never becomes false. Strict decrease and nonnegativity hold throughout. A real measure therefore does not justify termination without an additional well-founded ordering or a fixed minimum decrease. Floating-point underflow would create a different execution model and must not be inserted into the exact-real problem.', r'Original termination analogue informed by MIT §5.4')
add(r'Lexicographic descent and step bounds',
    r'A nonnegative pair starts at $(1,0)$. A step may replace it by $(0,B)$ for any finite nonnegative integer $B$, after which the second coordinate decreases to zero. Which is true?',
    [r'Every execution terminates, but there is no uniform step bound from the initial pair alone',r'Some execution has infinitely many decrements after the reset',r'Every execution has at most one step',r'The pair does not decrease lexicographically'],1,
    r'The first step strictly decreases the first coordinate, so any finite reset is permitted by lexicographic descent. Thereafter exactly $B$ unit decrements reach zero, making total length $B+1$. Each particular execution is finite, but choosing arbitrarily large finite $B$ defeats any uniform bound depending only on the initial pair. Infinite reset values are not admitted. Option 4 wrongly applies componentwise ordering rather than lexicographic ordering.', r'Original termination analogue informed by MIT §5.4', r'Hard')
add(r'Exact lower-bound trace with duplicates',
    r'Apply the displayed lower-bound algorithm to $[1,3,3,3,8,9]$ with target three. What are the visited midpoint indices and returned index?',
    [r'Midpoints $(3,1,0)$; result one',r'Midpoints $(3,1)$; result three',r'Midpoints $(2,1,0)$; result one',r'Midpoints $(3,4)$; result four'],1,
    r'Start $[0,6)$: midpoint three has value three, so set the upper boundary to three. In $[0,3)$, midpoint one has value three, so set the upper boundary to one. In $[0,1)$, midpoint zero has value one, so set the lower boundary to one. The empty interval $[1,1)$ returns one, the first equal position. Option 2 stops on equality, which would solve a different search specification; option 3 uses another midpoint convention.')
add(r'Maximum iterations for this implementation',
    r'What is the maximum number of loop bodies for lower bound on a sorted array of length 31?',
    [r'Four',r'Five',r'Six',r'Thirty-one'],2,
    r'The interval lengths on a longest path are $31,15,7,3,1,0$, giving five bodies. Formally $\lfloor\log_2 31\rfloor+1=5$. The bound includes the final one-element interval; treating its test as free gives option 1. The expression $\lceil\log_2 n\rceil+1$ is not the exact bound for this implementation and would overcount here. The empty-array case has zero bodies and must be handled separately.')
add(r'A monotone invariant can coexist with nontermination',
    r'Replace `lo=mid+1` by `lo=mid` in half-open lower bound. Which smallest array/target pair demonstrates failure?',
    [r'$[2]$, target three',r'$[2]$, target one',r'$[]$, target three',r'$[2,4]$, target one'],1,
    r'On the one-element interval $[0,1)$, midpoint zero has value two below target three. The defective update leaves the lower boundary at zero, so the state repeats forever. Its classification invariant remains true; the decreasing-width obligation fails. The target-one case moves the upper boundary to zero and terminates, and an empty array executes no body. A minimal counterexample isolates the faulty branch rather than relying on a large random test.')
add(r'Lower bound requires sortedness',
    r'Run correct lower-bound code on the unsorted array $[4,1,3]$ with target three. Which result and conclusion are correct?',
    [r'It returns zero and is correct',r'It returns two; sortedness was needed to discard earlier positions',r'It returns one; the duplicate rule failed',r'It raises an index error'],2,
    r'The first midpoint is one, whose value is one, so the lower boundary becomes two. The next midpoint two has value three, so the upper boundary becomes two and the result is two. However, index zero already has value at least three. The step that discarded the left region relied on sortedness and is invalid for this input. Bounds and termination remain correct even though the functional specification fails.')
add(r'Array lower bound versus upper bound',
    r'For $[1,2,2,2,5]$ and target two, the leftmost index satisfying $A[i]\ge2$ and the leftmost satisfying $A[i]>2$ are respectively what?',
    [r'One and one',r'Three and four',r'One and four',r'Zero and three'],3,
    r'The first eligible index for the non-strict comparison is one. Strictly greater elements begin at index four. Changing the branch test from `A[mid]<target` to `A[mid]<=target` changes the contract to upper bound. The duplicate block length is the difference, $4-1=3$. Returning an arbitrary equality position cannot replace either boundary in a counting formula.')
add(r'A conditional interval bound',
    r'At a true lower-bound guard, let interval length be $L$. Which is the tightest listed common upper bound on new length in both branches with the floor midpoint?',
    [r'$L-1$ only; no tighter bound is valid',r'$\lfloor L/2\rfloor$',r'$\lceil L/2\rceil+1$',r'$L$ and no strict decrease'],2,
    r'The left-keeping branch has length $\lfloor L/2\rfloor$. The right-keeping branch has length $L-\lfloor L/2\rfloor-1=\lceil L/2\rceil-1$, at most $\lfloor L/2\rfloor$. For $L=1$ both new lengths are zero. Option 1 gives a true but weaker bound rather than the requested common halving bound; option 3 is loose; option 4 misses strict progress.')
add(r'Insertion shifts and inversions',
    r'Sort $[4,2,3,1]$ by the displayed insertion sort. How many assignments of the form `a[j+1]=a[j]` execute?',
    [r'Three',r'Four',r'Five',r'Six'],3,
    r'Key two shifts four once. Key three shifts four once. Key one shifts four, three and two three times. Total shifts are $1+1+3=5$. Independently, the strict inversions are $(4,2),(4,3),(4,1),(2,1),(3,1)$, also five. Placements of the saved key are different assignments and are not counted. The sorted output is $[1,2,3,4]$.', r'Course-derived insertion analogue: Stanford Lecture 2, PDF pages 1–2')
add(r'The temporary array is not a permutation',
    r'During insertion of key two into $[1,4,2]$, after shifting four right and before restoring the key, the physical array is $[1,4,4]$. Which conservation statement is correct?',
    [r'The physical array alone preserves the input multiset',r'Ignore the hole at index one and include the saved key two',r'Ignore the last element and discard the key',r'Only the sum of physical array values is preserved'],2,
    r'After the shift, the logical hole is index one: that old value has moved right and its stale duplicate must not count twice. The other positions contain one and four; the external saved key is two. Their multiset is exactly the original prefix multiset. Filling the hole restores physical permutation. The physical sum changes from seven to nine, refuting option 4. A correct inner invariant accounts for temporary storage instead of demanding an assertion that the code does not preserve.', r'Original refinement of Stanford insertion-sort proof')
add(r'Stability is independent of sortedness',
    r'Insertion sort compares keys and moves entire records. If its inner comparison becomes `a[j].key >= key.key`, what happens to records $(2,a),(2,b)$?',
    [r'They remain in order $(a,b)$',r'Their order becomes $(b,a)$; sortedness and multiplicity still hold',r'The keys become unsorted',r'A record is lost'],2,
    r'When inserting the second record, the equal first key satisfies the modified guard. The first record shifts right, and the saved second record fills index zero. The result is $(2,b),(2,a)$, sorted by key and a permutation of the input but unstable. The example shows why proving only key order and multiset preservation does not establish stability. A strict greater-than shift preserves equal-key order.')
add(r'Exact stable-merge comparisons',
    r'Merge sorted lists $[1,4,7]$ and $[2,3,8]$, comparing heads while both lists are nonempty and taking the left on a tie. How many head comparisons occur?',
    [r'Three',r'Four',r'Five',r'Six'],3,
    r'The compared head pairs are $(1,2),(4,2),(4,3),(4,8),(7,8)$. The emissions are one, two, three, four and seven; the left list is then exhausted and eight is appended without a head comparison. Thus five comparisons occur. Six counts tail copying as another comparison; three assumes each list element pair aligns by index. The merge proof must cover the unpaired tail explicitly.', r'Course-derived merge analogue: Stanford Lecture 2, PDF pages 3–4')
add(r'Sorted output without preservation',
    r'A routine replaces every input entry by zero. Which verifier incorrectly accepts it as a sorting algorithm for arbitrary integer inputs?',
    [r'Check nondecreasing output only',r'Check output multiset equals input multiset only',r'Check both order and multiset',r'Check a bijection of record indices and ordered keys'],1,
    r'A zero-filled array is nondecreasing, so an order-only verifier accepts every such output. For input $[3,1]$, the multiset differs, and the other listed checks reject it. A permutation-only check is also insufficient in general, but it rejects this particular corrupting routine unless the input already consists entirely of zeros. This question distinguishes what the verifier tests from the complete contract it ought to establish.')
add(r'Recursive size must strictly decrease',
    r'A purported merge sort stops only at length one and splits length $n$ into $\lfloor n/2\rfloor$ and $\lceil n/2\rceil$. What happens on an empty input?',
    [r'It terminates with an empty list automatically',r'Both child sizes are zero, so the recursion has no decreasing measure',r'It calls a child of size one',r'It produces a sorted nonempty list'],2,
    r'At length zero the stated base case does not apply. Both children again have length zero, so recursive calls reproduce the same unhandled size indefinitely. Correcting the base condition to length at most one covers empty input and makes both children strictly smaller for every remaining length. Runtime formulas derived only for positive sizes cannot repair a missing functional base case.', r'Original boundary completion of Stanford recursive proof')
add(r'Three-way partition trace',
    r'Run the displayed three-way partition on $[3,1,2,3,0]$ with pivot two. What final boundary pair $(lt,gt)$ is returned?',
    [r'$(1,2)$',r'$(2,3)$',r'$(3,4)$',r'$(0,5)$'],2,
    r'There are two values below two (one and zero), one equal value and two greater values. Preservation plus the final region invariant requires less region length two and equal region length one, giving boundaries $(2,3)$. A concrete trace produces $[0,1,2,3,3]$ with these boundaries, though the order within outer regions is not promised. Counting only distinct keys instead of records would give the wrong lengths.')
add(r'Skipping an incoming unknown value',
    r'Modify the greater-than branch of three-way partition to increment `i` after the swap. Which two-element input with pivot two exposes failure?',
    [r'$[1,3]$',r'$[2,3]$',r'$[3,1]$',r'$[1,2]$'],3,
    r'On $[3,1]$, decrement the upper boundary from two to one and swap index zero with index one, producing $[1,3]$. The defective increment makes the scan index one, ending the loop with less boundary zero. It therefore classifies the first value as equal even though one is less than two. The incoming unknown value needed inspection. The correct code keeps the scan index zero and moves that value into the less region on the next iteration.')
add(r'An exact partition work count',
    r'For the displayed three-way partition on an array of length $n$, how many loop bodies execute regardless of key distribution?',
    [r'$n$',r'$n-1$',r'$2n$',r'The count depends on the number of distinct keys'],1,
    r'Initially the unknown-region length is $gt-i=n$. In each branch exactly one boundary moves by one in the direction that reduces this length, and no branch changes it by another amount. The loop stops precisely at unknown length zero. Hence there are exactly $n$ body executions, including zero for empty input. This does not mean equal numbers of key comparisons or swaps: those depend on which branches execute.')
add(r'Conservation does not imply stability',
    r'Partition tagged records $(3,a),(3,b),(1,c)$ around pivot two using swaps. Which complete claim is valid?',
    [r'Every partition is stable',r'Only keys, not records, are preserved',r'The algorithm preserves the record multiset but may reverse equal-key records',r'The algorithm sorts each outer region'],3,
    r'The first greater-than swap exchanges $(3,a)$ with $(1,c)$, yielding $(1,c),(3,b),(3,a)$. The two equal-key three records now appear in reverse original order. Swaps preserve whole records, so multiplicity and payloads survive. Region membership is established, but stability and internal sorting are not part of the contract. The trace provides a precise counterexample to option 1.')
add(r'Quotient and remainder as a certificate',
    r'Repeated subtraction divides 47 by six with initial $(q,r)=(0,47)$. What final pair and body count result?',
    [r'$(7,5)$ and seven',r'$(8,-1)$ and eight',r'$(6,11)$ and six',r'$(7,6)$ and seven'],1,
    r'The remainder sequence is $47,41,35,29,23,17,11,5$. Seven subtractions occur, and the quotient reaches seven. Conservation gives $47=7\cdot6+5$, and the exit range $0\le5<6$ proves this is the unique division result. The negative-remainder option performs one extra subtraction after the guard is false; the third option stops too early; the fourth violates conservation.', r'Course-derived division analogue: Cambridge verification examples and Exercise 53')
add(r'A valid identity with an invalid termination proof',
    r'Use repeated subtraction with $X=5,Y=0$. Which statement explains the defect?',
    [r'The conservation identity fails initially',r'The remainder becomes negative',r'The invariant remains true, but the guard remains true and the remainder does not decrease',r'The algorithm returns quotient zero and remainder five'],3,
    r'Initialization gives $5=0\cdot0+5$. Every body leaves the remainder five while increasing the quotient, so conservation continues to hold. The guard tests $5\ge0$ forever. A nonnegative remainder that is merely constant is not a decreasing variant. This is precisely why total correctness needs a positive divisor even though the algebraic partial-correctness equations can still be written.', r'Course-derived domain repair: Cambridge Exercise 53, PDF page 72')
add(r'Sequential updates in Euclid',
    r'With input $(21,15)$, what does defective code `while b!=0: a=b; b=a%b` return, and what should correct Euclid return?',
    [r'Fifteen and three',r'Three and three',r'Six and fifteen',r'Zero and three'],1,
    r'The first statement overwrites the dividend with fifteen. The second uses the new dividend and computes $15\bmod15=0$, so the defective loop returns fifteen. Correct simultaneous steps are $(21,15)\to(15,6)\to(6,3)\to(3,0)$, returning three. The gcd invariant fails on the defective first step, because the old gcd is three but the new gcd is fifteen. Preserving old operands is essential.')
add(r'Euclid exact trace length',
    r'How many body executions does Euclid perform from $(34,21)$ with simultaneous updates?',
    [r'Five',r'Six',r'Seven',r'Eight'],3,
    r'The states after each body are $(21,13),(13,8),(8,5),(5,3),(3,2),(2,1),(1,0)$. There are seven bodies; the initial state is not a body execution. The decreasing second components are $21,13,8,5,3,2,1,0$. This Fibonacci-like input illustrates many remainder steps, but a single trace is not a general worst-case bit-complexity proof.')
add(r'Power algorithm intermediate state',
    r'For exact `power(3,13)`, what is $(r,b,e)$ after two complete loop bodies?',
    [r'$(3,81,3)$',r'$(9,81,3)$',r'$(3,9,6)$',r'$(81,3,3)$'],1,
    r'Initially $(1,3,13)$. The odd first body multiplies the accumulator by three, squares the base to nine and halves the exponent to six: $(3,9,6)$. The even second body leaves the accumulator three, squares nine to 81 and halves six to three. The invariant checks $3\cdot81^3=3^{13}$. Option 3 is only the first checkpoint; option 2 incorrectly multiplies the accumulator on an even exponent.', r'Course-derived exponentiation analogue: CMU Contracts')
add(r'Two multiplication counts',
    r'For exponent 45, count accumulator multiplications and base squarings in the displayed exact power implementation.',
    [r'Six and four',r'Four and six',r'Five and five',r'Four and five'],2,
    r'Binary 45 is 101101, with six bits and four one bits. The loop executes six bodies, squaring once per body; the accumulator multiplication executes only on the four odd-exponent checkpoints. The exact counts are therefore four and six. Avoid silently deleting the final square when analyzing this displayed code. An optimized version could have five squarings, corresponding to option 4 but not to this implementation.')
add(r'The old base matters',
    r'Move `b=b*b` before the odd-exponent accumulator update in `power`. What does the resulting code return for $(x,y)=(2,1)$?',
    [r'One',r'Two',r'Four',r'Eight'],3,
    r'The loop begins with base two and exponent one. Squaring first makes the base four. The odd branch then multiplies the accumulator one by four, and halving the exponent ends the loop. The result four differs from the required two. The even/odd invariant derivation uses the old base in the accumulator factor; changing execution order invalidates that derivation.')
add(r'Exponent zero and modulus one',
    r'A correct modular power routine allows $M\ge1$ and exponent zero. For modulus one, which initialization yields the canonical final residue?',
    [r'Accumulator one, without reduction',r'Accumulator $1\bmod M$',r'Accumulator equal to the base',r'Reject every exponent-zero input'],2,
    r'The canonical residues modulo one contain only zero. With exponent zero no bodies execute, so the accumulator itself is returned. Initialization $1\bmod1=0$ yields the correct residue; unnormalized one is congruent to zero but is not the canonical value required by the contract. This distinguishes congruence from normalized output range.', r'Course-derived modular extension: CMU Exercise 1')
add(r'Reduction after overflow is too late',
    r'For eight-bit unsigned wrapping arithmetic, compute `(200*200)%251` using an eight-bit wrapped product. Compare it with exact modular multiplication.',
    [r'Both are 91',r'Wrapped result 64; exact result 91',r'Wrapped result 91; exact result 64',r'Both are 64'],2,
    r'Exact product is 40000. Modulo 256 it becomes 64 because $40000=156\cdot256+64$. Reducing that wrapped value modulo 251 still gives 64. Exact reduction gives $40000=159\cdot251+91$, hence 91. Wrapping modulo a power of two before reducing modulo a different modulus changes the arithmetic. A wide intermediate or an overflow-safe multiplication algorithm is required.', r'Course-derived overflow extension: CMU Exercises 1–2', r'Hard')
add(r'Permutation index certificate',
    r'Input records have keys $[5,1,5]$ and claimed sorted output keys $[1,5,5]$. Which zero-based source-index certificate additionally establishes stability?',
    [r'$[1,0,2]$',r'$[1,2,0]$',r'$[1,0,0]$',r'$[0,1,2]$'],1,
    r'Indices one, zero and two form a bijection and map the output to keys one, five and five. The equal-five records keep original index order zero before two, proving stability. Option 2 is a bijection and preserves keys but reverses equal records. Option 3 duplicates a source record; option 4 gives the wrong output ordering. A certificate must check index range, uniqueness, key consistency and the additional tie rule.')
add(r'Meeting witness and bound proves optimum',
    r'In a minimization problem, a feasible solution has value 17, while a proved lower bound for every feasible solution is 17. What follows?',
    [r'The optimum is at most 17 only',r'The optimum is at least 17 only',r'The optimum equals 17',r'The result depends on the search algorithm runtime'],3,
    r'The feasible witness establishes optimum at most 17. The universal lower bound establishes optimum at least 17. Together they force equality. Feasibility alone would not exclude a cheaper solution, and the lower bound alone would not supply an attaining solution. Runtime is irrelevant to this logical certificate, although finding or checking the witness may have a cost.')
add(r'Distance edge inequalities are necessary',
    r'Graph edges are $s\to a$ of weight two, $a\to b$ of weight three, and $s\to b$ of weight four. Claimed distances are $(0,2,5)$ with parent path through $a$. Which check detects failure?',
    [r'Parent path existence',r'Root distance zero',r'The edge inequality on $s\to b$',r'Nonnegative distances'],3,
    r'The supplied parents give a real root-to-$b$ path of weight five, so feasibility succeeds. But the direct edge gives $d(b)\le d(s)+4$, requiring $5\le4$, which is false. There is a shorter path of weight four. Thus parent paths alone certify reachable distances, not shortest distances. This example isolates the optimality-bound component of the certificate.', r'Original certificate problem', r'Hard')
add(r'Parent cycles can pass local equalities',
    r'Graph edges are $s\to a$ of weight five, $a\to b$ of weight zero and $b\to a$ of weight zero. A certificate sets $d(s)=d(a)=d(b)=0$, and chooses parents $parent(a)=b$, $parent(b)=a$. What is missing?',
    [r'All edge inequalities already fail',r'A requirement that parent chains reach the root',r'The root distance must be five',r'A requirement that weights be positive'],2,
    r'All edge inequalities hold: zero is at most five on the root edge, and equal zero distances satisfy both zero edges. Both parent equalities also hold. Yet the parent cycle provides no path from the root attaining distance zero; the actual distances to the other vertices are five. Requiring every parent chain to end at the root excludes this false certificate. Strictly positive weights would be an unnecessary domain restriction rather than the general repair.', r'Original certificate counterexample', r'Hard')
add(r'Negative weights do not automatically defeat a certificate',
    r'Graph edges are $s\to a$ of weight four, $s\to b$ of weight five and $a\to b$ of weight negative three. Which distance assignment is certified by root-reaching parents and all edge inequalities?',
    [r'$(0,4,5)$',r'$(0,4,1)$',r'$(0,1,4)$',r'No finite assignment because an edge is negative'],2,
    r'Choose parents of $a$ and $b$ as $s$ and $a$. Parent sums give distances four and one. Edge checks are $4\le4$, $1\le5$ and $1\le4-3$. Every parent chain reaches the root. Hence the certificate proves exact distances despite a negative edge. Option 1 violates the edge through $a$; option 3 cannot match its parent-path witness. Negative cycles, rather than every negative edge, are the relevant obstruction to finite shortest-path values in the reachable domain.', r'Original certificate problem', r'Hard')
add(r'A negative cycle contradicts finite labels',
    r'A reachable directed cycle has edge weights two, negative five and one. What do shortest-path edge inequalities imply when summed around the cycle?',
    [r'$0\le-2$, a contradiction',r'$0\le2$, a proof of optimality',r'$d(s)=0$ only',r'A cycle is allowed whenever one edge is positive'],1,
    r'Each inequality bounds the next distance by the previous distance plus its edge weight. Summing cancels every distance from both sides and requires zero at most total cycle weight $2-5+1=-2$. This is impossible, so no finite assignment satisfying all cycle-edge inequalities exists. The contradiction depends on the negative total, not on which individual edges have which sign.', r'Original certificate problem', r'Hard')
add(r'Greedy feasibility is not optimality',
    r'For unweighted interval scheduling, choosing the earliest-start interval selects $[0,10)$ and rejects $[1,2),[2,3),[3,4)$. Which conclusion is justified?',
    [r'It is optimal because chosen intervals never overlap',r'The output is feasible but may be suboptimal',r'No greedy algorithm can be correct',r'Endpoint conventions do not matter'],2,
    r'The chosen singleton is feasible. Under half-open intervals, the three short intervals are mutually compatible and yield three selections instead of one. Therefore a non-overlap invariant proves feasibility but not maximal cardinality. An optimality proof needs an exchange or dominance argument for the chosen rule. This counterexample does not refute every greedy rule; earliest finish is a different rule. Endpoint conventions matter to whether adjacent intervals are compatible.')
add(r'Structural mass with missing children',
    r'A binary tree has leaves at depths one, two and three, with no other leaves. What is the leaf mass $\sum 2^{-d}$, and does it alone prove fullness?',
    [r'$7/8$; it does not prove fullness',r'$1$; it proves fullness',r'$3/8$; it proves fullness',r'$7/8$; it proves fullness'],1,
    r'The mass is $1/2+1/4+1/8=7/8$. In a finite full binary tree root mass splits completely and all mass reaches leaves, so total mass is one. A mass below one means some possible child branches are missing. The given depths can occur in a tree with a chain containing missing branches. This certificate argument distinguishes a universal bound from its equality condition.')
add(r'An accumulator formula for dependent loops',
    r'For integer $n\ge1$, increment an accumulator once for each $1\le i\le j\le k\le n$, starting from $c_0$. What final formula follows?',
    [r'$c_0+\binom n3$',r'$c_0+n^3$',r'$c_0+\binom{n+2}3$',r'$\binom{n+2}3$'],3,
    r'Each weakly increasing triple corresponds to a multiset of size three drawn from $n$ values. The count is $\binom{n+3-1}3=\binom{n+2}3$. The accumulator invariant is initial value plus the number of already visited triples, yielding the displayed final formula. Strict-combination counting omits repeated indices; a cube ignores dependent bounds; the fourth option discards initialization. For $n=1$, exactly one body executes, an immediate boundary check.')
add(r'Recursion depth as an index invariant',
    r'Copy indices $N-1,N-3,\ldots$ from an input into consecutive output cells starting at zero. For $N=10$, what final copied source index and output length occur?',
    [r'Source zero; length five',r'Source one; length five',r'Source one; length six',r'Source zero; length ten'],2,
    r'The source indices are nine, seven, five, three and one. At depth $t$, the source is $N-1-2t$ and destination is $t$. After five writes, the next source is negative one and recursion stops. Generally the output length is $\lceil N/2\rceil$ and the last source is one for even positive lengths, zero for odd lengths. This state formula proves indexing and termination together.')
add(r'An exact invariant determines a nonlinear sum',
    r'Initialize `s=0, k=1`. While `k<=n`, execute `s += 2*k-1; k += 1`, with exact integers and $n\ge0$. Which invariant at the checkpoint just before the guard is correct?',
    [r'$s=k^2$',r'$s=(k-1)^2$',r'$s=2k-1$',r'$s=n^2$'],2,
    r'Before iteration one, the sum is zero, equal to $(1-1)^2$. If the invariant holds before $k$, adding $2k-1$ gives $(k-1)^2+2k-1=k^2$, which is the required assertion before iteration $k+1$. At exit $k=n+1$, it yields $s=n^2$. The empty range for $n=0$ leaves zero, agreeing with the formula. Option 1 places the assertion after the body rather than before it.', r'Course-derived summation analogue: Cambridge for-loop verification, PDF pages 57–58')
add(r'An induction hypothesis must include preservation',
    r'For a recursive sorting proof, the induction hypothesis says only that each child output is sorted. Which additional assertion is essential to establish the complete parent sorting contract?',
    [r'The child runtime is linear',r'Each child output preserves its input multiset',r'The recursion tree is balanced',r'Every input key is positive'],2,
    r'Sorted child outputs could both be empty, satisfying the weak induction hypothesis while destroying all input records. Preservation of each child multiset plus preservation by merge proves preservation for the parent. Balance affects cost and strict size reduction affects termination, but neither implies value preservation. Positive keys are unnecessary because ordering works over any totally ordered key domain.', r'Original strengthening of Stanford recursive proof', r'Hard')
add(r'A smallest counterexample to a weakened contract',
    r'A claimed maximum routine initializes `best=0` and scans a nonempty integer array using `best=max(best,a[i])`. Which input refutes its contract, and what invariant does the code actually maintain?',
    [r'$[-2]$; best is the maximum of zero and the processed values',r'$[2]$; best is the minimum of processed values',r'$[0]$; best is undefined',r'$[]$; the input satisfies the nonempty precondition'],1,
    r'For the admitted singleton negative two, the routine returns zero, which is not even an input value. Its genuine invariant is $best=\max(0,A[0],\ldots,A[i-1])$, so its logic solves a different problem unless inputs are constrained appropriately. Initializing with the first input value repairs the arbitrary-nonempty-integer contract. The empty array is outside that contract, so it cannot serve as the requested admitted counterexample. Writing the exact maintained invariant exposes the hidden assumption.')

assert len(questions)==50, len(questions)
(BASE/r'a_correct-questions.json').write_text(json.dumps(questions,indent=2)+chr(10),encoding=r'utf-8')
print(r'Authored 50 distinct original/course-derived problems with complete solutions.')
