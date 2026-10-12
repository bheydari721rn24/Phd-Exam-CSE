## Detailed examination decisions and final synthesis

The fifteen foundational review notes remain above. These additional decisions supply explicit domains, examples and failure cases. Use them after studying the constructions and solved problems.

**16. Name the mathematical and language model.** A four-bit hardware sum can have a defined stored low pattern while the analogous overflowing signed C expression is undefined. The authentic overflow question asks the former. The expression `INT_MAX+1` asks the latter. Do not substitute one answer model for the other.

**17. Follow each intermediate's type.** An unsigned byte128 promotes to int before complement; its complemented value is negative129. Assigning to unsigned32 yields4294967167, while converting to unsigned8 yields127. Destination width enters at conversion, not at the earlier operator.

**18. Do not equate storage bits with value bits.** An unsigned representation with eight no-padding value bits has256 values and maximum255. A storage width requires `CHAR_BIT` and possible padding information. The type name alone does not prove a numeric endpoint.

**19. Check intermediate overflow before final range.** The mathematical final value of `-(2*n)` can fit when `2*n` cannot. At int32 `n=1073741824`, the product overflows before negation. Widen an operand before the dangerous operator; a wider result variable is too late.

**20. Unsigned sources can promote into signed arithmetic.** Under int32, two uint16 values65535 multiply as signed int and exceed its maximum. Converting one operand to uint32 first changes the expression domain; the product4294836225 then fits unsigned32. Inspect promotion, not the spelling of the source declaration.

**21. Integer and floating casts have different range rules.** Integer negative one converts to unsigned32 maximum modulo its range. Floating negative one does not have a representable unsigned truncated result, so that conversion is undefined. Floating negative0.75 truncates to zero and is valid. The source type is part of the proof.

**22. Common type and chosen branch are separate.** With int negative one and unsigned int one, a conditional's common type is unsigned even when the signed branch is selected. The chosen negative value converts before comparison. An unexecuted branch affects type without producing a runtime value.

**23. Higher rank alone does not finish mixed-signedness analysis.** First ask whether the higher-rank signed type represents all values of the unsigned type. Long64 can contain unsigned32; long32 cannot. The LP64/LLP64 comparison changes for that reason, not because a machine is informally called64-bit.

**24. Precedence does not specify operand order.** It tells which operations form the expression tree. The plus operator does not sequence its operands' side effects. A comma operator or logical short circuit supplies a separate sequencing rule. Diagnose `i++ + i++` before doing numerical addition.

**25. A guard must precede and cover the unsafe operation.** `x!=0 && 10/x>2` skips division at zero. Reversing the operands or replacing logical AND with bitwise AND removes that proof. For a general signed division, also exclude minimum divided by negative one when its quotient cannot fit.

**26. Expand macros before parsing.** Unparenthesized `SQR(1+2)` yields `1+2*1+2`, so the result is five. Parentheses repair grouping, but `((i++)*(i++))` still repeats unsequenced modifications. Distinguish syntax protection from single evaluation.

**27. Signed endpoints are asymmetric.** An n-bit two's-complement word ranges from negative $2^{n-1}$ to $2^{n-1}-1$. The negative endpoint has no same-type positive counterpart. Negation and absolute-value routines need a domain check; do not assume every negative integer can be safely made positive.

**28. Signed division truncates toward zero.** Negative sixteen divided by three yields negative five and remainder negative one in C17. Floor would yield negative six and remainder positive two. Verify $a=qd+r$ with the stated convention and exclude invalid quotient cases before using the identity.

**29. Ceiling division can be evaluated without a dangerous addition.** For nonnegative n and positive d, use `n/d + (n%d != 0)` under a representable integer model. Blindly computing `(n+d-1)/d` can overflow. For eight flags per byte, exact multiples need no extra byte and a nonzero remainder needs exactly one.

**30. A unique record size needs a precise ABI policy.** Alignment constraints permit extra padding. The minimum-layout recurrence uses the earliest aligned offset and final alignment rounding. With widths5 and4 and alignments1 and4, the minimum is twelve, but alignment alone also permits a later second member and size sixteen.

**31. Internal and tail padding are different.** Widths5,4,1 at offsets0,8,12 end at13 and round to size16 under four-byte record alignment. Three bytes are interior and three at the tail. Summing the widths gives ten, neither the object size nor an aligned ending offset.

**32. Arrays retain their total size only in the correct context.** An actual five-by-six array of four-byte elements is120 bytes; a row is24 bytes. An adjusted parameter measures a pointer in `sizeof a`, while `sizeof a[0]` can still measure the row. A pointer's own representation does not include its target allocation.

**33. Serialization does not determine C bit-field allocation.** Nine consecutive packed flags need two eight-bit bytes with seven unused bits. Nine Boolean array objects and a record of nine bit fields obey different storage rules. Count only under the explicitly stated format.

**34. Consecutive exactness is not maximum magnitude.** With p significant binary bits, all integers through $2^p$ are exact, but the next odd integer is missing. Larger powers of two can still be exact. More exponent range does not fill precision gaps.

**35. At a midpoint, inspect retained parity.** Binary64 rounds $2^{53}+1$ to $2^{53}$ and $2^{53}+3$ to $2^{53}+4$ under nearest-even. One goes downward and the other upward. A blanket rule that halves always round down or away from zero is invalid for this model.

**36. Round at every operation node.** The authentic decimal trees produce435.01 and435.00 because their intermediate rounds differ. One final round of their common exact sum answers a different computation. Do not replace decimal significance with binary64 or printed decimal digits.

**37. CHOP and decimal rounding use different formulas.** Exact-real hundredth truncation is `CHOP(100x)/100`; nearest hundredth adds a signed half unit before CHOP. At negative2.376 the negative offset produces negative2.38. A C cast adds a representability constraint absent from abstract CHOP.

**38. Shift count uses the promoted left width.** An unsigned byte promoted to int32 may be shifted by eight. An unsigned32 word cannot be shifted by32, even when its value is zero. Valid-count unsigned shifts, signed left-shift range, and implementation-defined negative right shifts are separate tests.

**39. Truth is a value test, not an all-zero-bit test.** A scalar compares unequal to zero to count as true. IEEE negative zero is false despite its sign bit; a NaN is true in this scalar truth conversion. A null pointer's representation need not be all-zero bits. Logical results are int zero or one in C.

**40. Keep course-language comparisons labeled.** Java integer overflow, Boolean operator types and fixed ranges differ from C17; Python integers, floor division and arbitrary-precision arithmetic differ again. A well-chosen example from another course teaches a distinction, not a replacement C rule.

### Complete closing summary

An expression is a typed, partially defined computation with sequencing rules. Its representation and destination do not alone determine the intermediate type. Parse first, derive promotions and common types, establish reachability, prove intermediate domains, compute, then convert to storage. Mathematical residue proofs explain unsigned conversion; positional weights explain fixed-width signed bounds; quotient/remainder proves truncation and ceiling formulas; aligned-offset recurrences explain minimum ABI layouts; expression trees and binade spacing explain finite-precision behavior. The solved questions apply these constructions to numeric instances, general proofs and failure cases. The review does not assert a literal guarantee about every unseen exam question or a complete worldwide course census.
