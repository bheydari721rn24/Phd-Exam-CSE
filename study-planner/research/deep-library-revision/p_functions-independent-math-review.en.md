# Independent semantic and numerical review of PF37–PF89

Date: 2026-10-18. Scope: current `research/p_functions-questions.json`, the existing PF01–PF36 replacement manuscript, and the lesson's explicit C17/Python/C++ contract. The checkout was read only. No C or C++ compiler was invoked, and this report must not be described as a C compilation certificate.

## Result

No incorrect numeric result was found in PF37–PF89. The oracle passes 53 grouped assertions. This includes 20 *actual stated* Python blocks PF64–PF83, run separately in fresh `python -I` subprocesses, rather than merely executing the question certificates. Calls requested only in prose or comments were appended explicitly and are retained in `oracle-results.json`. No execution was allowed to contaminate the next question's module state.

PF85 contains no executable block. Its factory reconstruction is explicitly labelled as a reconstruction. Its result `[1, 2, 1, 3]` and distinct retained cells agree with the natural-language procedure. Likewise, the complete guarded binary exponentiation implementation in the oracle is an explicitly specified reconstruction, not a claim that the incomplete PF52 stem supplies all its statements.

## Findings to incorporate in the expanded solutions

1. **PF49: initialize and maintain maximality explicitly.** Assume positive integer inputs and initialize `d=min(a,b)`. Every integer common divisor is at most that initial bound. The loop invariant rules out every candidate in `(d,min(a,b)]`; initialization makes that range empty. Decrement only after the divisibility test has failed. At a successful return, the test establishes that d is a common divisor and the invariant excludes every larger candidate. The decreasing positive candidate supplies termination because one divides both positive inputs. The old answer has the right idea, but initialization, transition, and termination should be visible in its teaching proof.

2. **PF51–PF53: mathematical output safety and executed operation safety differ.** The geometric sum is `2**n-1`. On the explicitly chosen signed int32 model, n=31 produces a representable result 2147483647, but a helper maintaining a power and unconditionally doubling it after its last addition still executes the unrepresentable next power 2147483648. A helper using `p=2*p+1` has a different operation-level contract. PF53's stated n=1/x=50000 example is correct: the requested result is 50000, whereas the unused square is 2500000000. When repairing PF52, supply all exponent/base/accumulator updates and avoid a last unused square. Saying only “loop while e>0, return r” does not specify the whole repaired implementation.

3. **PF55: retain language and quotient-domain qualifications.** C's mathematical truncation model gives q=-4 and r=-3 for -23/5. Python `//` and `%` give a different negative-numerator decomposition. For positive d, when r<0, use q-1 and r+d to obtain the nonnegative Euclidean remainder. General C division still requires a nonzero divisor and representable quotient; do not evaluate `abs(INT_MIN)` in int merely to express a mathematical magnitude condition.

4. **PF57: distinguish portable bounds from the int32 example.** The symbolic interval and the stated numerical endpoints are correct. The original stem says C17 int, while the int32 representation appears only in the old answer. Explicitly introduce that model before presenting the numerical interval; retain actual `INT_MIN`/`INT_MAX` as the portable statement. Both the intermediate addition and multiplication were checked. Neighbors immediately outside the numerical interval overflow the multiplication.

5. **PF64: avoid a fresh-allocation promise.** `x += 3` on the integer binding obtains the value seven and rebinds the local parameter. “Creates integer 7” must not be read as a guarantee of fresh allocation or distinct integer identity: Python implementations may reuse integer objects. No identity test on immutable cached integer values is needed for the caller-preservation proof.

6. **PF84: separate persistent-state, accumulated-output and closed-form-expression bounds.** Under the explicit signed int32 model and a fresh static zero, the triangular counter itself fits through n=65535. The sequential caller sum of returns fits only through n=2343, with total2146453540; n=2344 gives2149201880, above INT_MAX. A literal evaluation `n*(n+1)*(n+2)/6` in int can overflow its numerator already above n=1289 even when the final mathematical quotient fits. These are three different contracts. This supplements the universal mathematical induction; it does not replace it.

## Executable Python observations

- PF64: caller/result `[4,14]`.
- PF65–PF67: mutation then rebind yields `[[2,7],[99],false]`; returned alias yields two names for `[1,5,9]`; shallow outer copy yields distinct `[2,3]` and `[2,3,8]`.
- PF68: `[4,9]`, definition-time default versus explicit call-time argument.
- PF69: snapshots `[2]` and `[2,5]` are distinct, while the persistent default ends at `[2,5]`.
- PF70: `[1]`, `[9,7]`, `[1,2]`; all result snapshots are distinct, default ends `[1,2]`.
- PF71: distinct returned `[1]` and `[2]` objects.
- PF72: `UnboundLocalError`; captured stdout is empty, so no global eight is printed first.
- PF73: module x/result `[11,11]`.
- PF74: `[7,12]`; two functions and two retained cells are distinct.
- PF75: lexical lookup gives13.
- PF76: `[2,4,6]`.
- PF77: `[2,2,2]`; three function identities share one retained cell.
- PF78: `[0,1,2]`; defaults are separately saved tuples `(0,)`, `(1,)`, `(2,)`; these lambdas have no closure cells.
- PF79: result/counter `[-1,2]`.
- PF80: `TypeError`, duplicate binding of a; empty stdout.
- PF81:127.
- PF82:`None`.
- PF83:25.
- All20 actual blocks have no unsolicited stdout. PF47's separate printed-output example is semantically `5\n8\n`, not a claim that any of these20 blocks prints that output.

## Bounded mathematical checks

| Topic | Checks and scope |
|---|---|
| Descending divisor proof |10000 positive input pairs a,b=1..100;317270 visited candidate states, each with the exclusion invariant checked and final equality to independent `math.gcd` |
| Triangular helper |101 n values,0..100; live counter at most101, total at most5050 |
| Geometric sum |151 n values,0..150, unbounded integer invariant |
| Explicit guarded binary power |1616 pairs x=-50..50,y=0..15;842 final int32-fit cases also have every recorded executed product in int32 range |
| Quotient/remainder |5050 input pairs n=0..100,d=1..50, plus515100 alternative quotient checks; separate universal subtraction proof remains necessary |
| Signed division |8040 mathematical truncation cases n=-100..100,d=-20..-1 or1..20; positive-d Euclidean adjustment checked |
| Composite interval |131056 exhaustive x values across illustrative two's-complement widths4..16, plus int32 endpoints and their outside neighbors |
| Persistent callback |100 sequential `apply(step,5)` invocations; result at invocation m is4m+4; first two8 and12 |
| Value-result copy-out |Both stipulated orders yield20 and10 respectively |
| By-name versus by-value |Read pairs `(4,5)` and `(4,4)` under explicit access to caller i |
| Sum of persistent returns |301 n values0..300; tetrahedral closed form and each triangular return checked |

## Limitations

The bounded oracle supports the proofs but is not a proof for every integer or every conforming implementation. The C/C++ answers were checked as language-model reasoning, not executable C behavior. No undefined C fragment was assigned a numerical result or “validated” by a compiler run. The existing PF01–PF36 manuscript was read; its separation of object identity, mathematical recurrence, language contract, activation-body depth and machine safety is consistent with these later answers. The report does not certify browser rendering, figures, code typography, source-reading coverage, future rewritten prose, or any examination score.
