**Summary.** An array problem connects a logical index domain, a storage representation and an exact sequence of reads and writes. First normalize the indices and derive strides from the representation. Then establish that every requested access names a live initialized element. Finally derive the output from original values or from explicitly evolving values. These steps distinguish address calculation from C pointer legality, capacity from logical length, copied values from shared references and per-operation work from amortized totals.

**Examination procedure.** Identify the language and arithmetic model. Write every lower bound, extent and exclusive boundary. Count offsets in elements before converting to bytes. State the identities and lifetimes of all arrays and aliases. Express visited indices as a function of the iteration number. For a mutation, decide which source values have already changed. Prove initialization, preservation, exit and termination for every relevant invariant. Check zero, one, last-element and one-past cases. For a cost question, state precisely whether you count comparisons, successful updates, element assignments, allocated slots or cache fills.

1. A length n array has n element positions but n+1 boundaries. Its valid normalized element domain is $0\le i<n$; boundary n is not an element.

2. Inclusive declaration bounds L through U contain U-L+1 positions. Subtract the declared lower bound before using a zero-based stride formula.

3. A half-open segment [l:r) has r-l elements when $0\le l\le r\le n$. An empty segment remains a valid boundary-based operation.

4. The mathematical empty-array case does not justify a fixed C declaration with bound zero. Use an appropriate pointer/length or container representation.

5. C array elements have a uniform element type and are contiguous. A structure element's own padding is already included in its stride.

6. A pointer object is not the array it selects. Pointer size cannot determine the number of pointed-to elements.

7. Python lists contain object references under the language model. A C numeric element-address formula cannot be applied directly to their contents.

8. For stated byte width w, element address is $B+w(i-L)$. Compute i-L before multiplying.

9. The last element start and last occupied byte are different. A length-n array's final occupied byte is $B+wn-1$ in the flat model.

10. The byte address $B+wn$ marks one-past storage. It does not hold the array's last value or an implicit terminator.

11. Row-major offset is $(i-L_r)C+(j-L_c)$. Its row stride uses the number of columns.

12. Column-major offset is $(j-L_c)R+(i-L_r)$. Its column stride uses the number of rows.

13. Equal addresses at some indices do not make two layouts equivalent. The first and final positions can agree while intermediate positions differ.

14. Row-major inversion divides the element offset by the column extent. Quotient recovers the row and remainder recovers the column.

15. A byte-address inverse must check divisibility by element width. An address inside an element is not automatically its starting address.

16. Every recovered coordinate must satisfy its own bound. A plausible flat offset formula does not excuse an invalid row or column.

17. Three-dimensional row-major strides are the products of later extents. The last index has stride one.

18. Mixed-radix inversion uses successive remainder and quotient operations. It gives a unique coordinate within a positive rectangular shape.

19. An affine view can have gaps or negative strides. Use its stated strides instead of silently assuming dense storage.

20. A true C rectangular array and an array of row pointers have different stored objects. Casting between them does not construct the missing representation.

21. C's first array conversion removes only the outermost array level. A converted rectangular array therefore gives a pointer to a row.

22. A pointer to a row advances by the complete row size. A pointer to one integer advances by one integer size.

23. Physical adjacency across row subarrays does not authorize arbitrary flat C pointer traversal. Use legal row and column accesses or a genuine flat backing array.

24. A copied transpose changes both coordinate order and destination shape. The destination flat map is $jR+i$ for an original R-by-C matrix.

25. A transpose view can exchange strides without rearranging the backing values. A physical copied transpose instead creates a different order in storage.

26. Square in-place transpose swaps only i<j pairs. Including both orientations swaps each pair twice and undoes the result.

27. Rectangular transpose can have longer permutation cycles. A square-only diagonal-swap loop is not a general rectangular algorithm.

28. A C array expression usually converts to its first-element pointer. Important exceptions include sizeof, unary & and string-literal array initialization.

29. sizeof a counts full array storage only where a really has array type. An adjusted array parameter has pointer type.

30. A written bound in a C array parameter does not automatically supply a runtime length. Pass length or establish an explicit usable contract.

31. For a real array, sizeof a / sizeof a[0] yields its extent. Reusing the expression on a pointer yields a pointer-size quotient, not a length.

32. a and &a can begin at the same storage while selecting different types. Their increments use different element sizes.

33. A pointer's negative subscript is relative to its current position. It is not Python's end-relative indexing convention.

34. For a pointer at array position r, legal dereference offsets satisfy $-r\le k\le n-1-r$. Prove the transformed index r+k.

35. Pointer formation also permits one-past, with upper offset n-r. The extra endpoint cannot be dereferenced as an element.

36. C pointer subtraction requires one array relation and a representable ptrdiff_t result. Numerical closeness of unrelated allocations is insufficient.

37. Uninitialized automatic storage and an out-of-bounds access are different errors. Valid indices do not establish usable values.

38. Partial explicit initialization zero-initializes the remaining array elements. Static-storage arrays without initializers also receive zero initialization.

39. Array assignment is not ordinary C pointer rebinding. Copy individual elements or use an appropriate object-copy operation under its contract.

40. Unsigned reverse loops must avoid a condition that is always true. Test a decreasing boundary before decrementing into a valid element index.

41. For positive stride s over [l:r), visit l+ts while l+ts<r. The nonempty count is $\lceil(r-l)/s\rceil$.

42. Derive the final visited index from the progression. It need not be r-1 when the stride skips positions.

43. A source progression and destination progression can use different strides. Their correct stop condition follows the source's valid domain.

44. A sum invariant relates the accumulator to the processed original prefix. Add machine representability obligations when the accumulator has finite range.

45. A final signed sum fitting its type does not prove intermediate sums fit. Cancellation can occur only after an earlier overflow.

46. A minimum initialized from the first value requires nonempty input. It uses n-1 later comparisons.

47. An infinity-initialized mathematical minimum uses n comparisons and includes the first successful update. This changes the update count.

48. Strict minimum comparison preserves the earliest tied minimum. Non-strict comparison can select the last tied occurrence.

49. A fixed number of scan tests can coexist with a random number of successful updates. Do not identify these cost measures.

50. Prefix sums use n+1 boundary values and P[0]=0. The sum of [l:r) is P[r]-P[l], including empty ranges.

51. An element update invalidates subsequent ordinary prefix sums. Static preprocessing does not promise dynamic-query correctness.

52. A difference-array range update adds at its left boundary and subtracts at its right boundary. The signs follow from starting and ending the change.

53. A right-end difference sentinel is not a data element. Reconstruct only the declared logical length.

54. Two-dimensional prefix queries subtract top and left regions and restore their overlap. The final overlap term has a plus sign.

55. Increasing in-place neighbor updates may read modified predecessors. Derive the evolving-state recurrence before claiming an original-value formula.

56. Decreasing order can preserve a lower predecessor while increasing order cannot. Order is part of the transformation specification.

57. A copy contract should name original source values. Equality to final source values can hide destructive aliasing.

58. Bounds prove access safety but not freedom from interference. A copying proof also needs storage separation or an overlap-safe direction.

59. Rightward overlapping moves copy high indices first. This preserves smaller unread source positions.

60. Leftward overlapping moves copy low indices first. This preserves larger unread source positions.

61. memcpy requires nonoverlapping valid regions. memmove supports valid overlap with an as-if temporary-copy contract.

62. Insertion at k shifts n-k values and needs space for a new logical element. Insertion at boundary n needs no shifts.

63. Stable deletion at k shifts n-k-1 values. Old values in spare slots do not belong to the shortened logical sequence.

64. Segment reversal uses $\lfloor(r-l)/2\rfloor$ pair swaps. Its high partner starts at r-1, not r.

65. Three segment reversals turn XY into YX. Normalize rotation only after handling length zero.

66. Rotation by k on positive length n has $\gcd(n,k)$ cycles under the modular step map. Track the direction of value movement explicitly.

67. Stable compaction maintains write≤read. This prevents writes from destroying larger unread positions.

68. Python single indices must select actual elements after negative normalization. Ordinary slice boundaries can instead be clipped to empty intervals.

69. A negative-step slice's omitted stop differs from explicit -1. Normalize the exact slice before counting or predicting output.

70. Extended slice assignment with step other than one requires equal replacement length. Ordinary step-one replacement can resize the list.

71. A shallow outer-list copy retains inner references. Inner mutation and outer-slot rebinding therefore produce different visibility.

72. Repeating one mutable row repeats its reference. Construct independent rows separately when later row mutations should be independent.

73. Deleting during list iteration can skip shifted values. Use a proved compaction loop or a separate filtered output.

74. C strings require an accessible first zero character. Capacity, initialized bytes and string length are three distinct facts.

75. A string terminator is an actual character element; a one-past pointer is not. argv's null pointer sentinel is a further distinct representation level.

76. Bounded pattern search uses candidate starts through n-m inclusive. Handle m>n before unsigned subtraction and state the empty-pattern convention.

77. Dynamic-array capacity and logical length differ. Under doubling from capacity one, total copied elements through capacity c are c-1.

78. Amortized constant append cost does not bound each expansion append by a constant. Peak memory includes simultaneously live old and new blocks.

79. Packed triangular formulas depend on orientation, diagonal inclusion and traversal order. Check those conventions and safe intermediate arithmetic before substituting.

80. Numerical layouts, finite traces and tests supplement general proofs. A correct answer states its language, domain, ownership, arithmetic and cost assumptions before deriving the result.
