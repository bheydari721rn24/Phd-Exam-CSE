1. **One array, three string views.** Determine the first terminator relative to the given starting address; capacity and total zero count do not determine that view's length.

2. **Exact-size initialization.** Separate initialization constraints from the later library contract; a valid declaration can create a nonstring array.

3. **Embedded escape and size.** Expand escapes, retain explicit embedded zeros, and then add the literal's implicit final zero before counting storage.

4. **Suffix identity and one-past.** The empty-string pointer designates the terminator itself; a pointer one past the complete array does not.

5. **Array size inside a function.** Array parameter syntax does not transmit the array extent; pass capacity before array-to-pointer conversion loses that information.

6. **Two pointers and an independent copy.** Draw object identity before tracing mutation; pointer assignment preserves aliasing, whereas a disjoint byte copy creates separate content storage.

7. **Equal content and unequal objects.** Use a string comparison for string equality; equal literal spelling does not establish a required object identity.

8. **Bounded scan failure.** A bounded scan returning its bound means no terminator was found; represent that status separately from a successful length.

9. **Short-circuit order.** Put the range guard before the indexed access in a short-circuit conjunction; the guard must be established before the read occurs.

10. **Exact scalar length cost.** Include the final failing sentinel test and sum repeated suffix costs instead of counting distinct stored bytes only.

11. **A copy that just fits.** For a nontruncating string copy, require source length strictly less than destination capacity and retain the terminator in the write count.

12. **Bounded copy padding.** When the source ends before the `strncpy` bound, count zero padding through the entire bound and preserve bytes beyond it.

13. **Bounded copy without a terminator.** A `strncpy` bound limits writes but does not guarantee termination; inspect the resulting complete accessible array before using string functions.

14. **Forced termination and zero capacity.** Guard positive capacity before subtracting one, and separate guaranteed termination from a guarantee that no content was truncated.

15. **The exact append bound.** Compute append space as capacity minus current length minus one; a `strncat` bound limits new content, not total storage.

16. **Short source and a large bound.** Use the actual minimum of source length and append limit when both are known; a worst-case sufficient bound need not be necessary.

17. **Safe arithmetic without forming an overflowing sum.** Establish the existing terminator lies within capacity before using subtraction to validate an append.

18. **Right-overlap propagation.** Distinguish a defined faulty handwritten algorithm from an undefined overlapping library call; use original-source semantics for `memmove`.

19. **Left-overlap movement.** An overlapping left shift can copy forward, but the moved range must include the original terminator when moving a whole suffix.

20. **Insertion at all boundary positions.** For one nonzero insertion at position $p$, move $n-p+1$ bytes, reserve $n+2$ storage bytes, and count the insertion separately.

21. **Deletion count includes zero.** Delete by moving the following suffix through its terminator; omitting zero often duplicates the old last character.

22. **Lexicographic comparison count.** Find the first mismatch before considering length; only the sign of a standard string-comparison return is portable.

23. **A proper prefix compares smaller.** A comparison bound ending at a common prefix can hide the terminator mismatch that distinguishes complete strings.

24. **Unsigned byte order.** Standard string ordering uses unsigned character values; signed plain-char arithmetic is not a substitute.

25. **Equal strings and different storage.** String equality ignores bytes after the first zero; fixed-count memory equality does not.

26. **Searching for the terminator.** Character search includes the terminating zero, but a failed search returns null and cannot be converted into an offset by subtraction.

27. **Spans are initial segments.** Span functions measure a maximal qualifying prefix; set membership is different from a full-string frequency count.

28. **Overlapping substring occurrences.** State whether matching returns the first hit, permits overlaps, or advances past a full hit before counting occurrences or work.

29. **Empty and longer patterns.** Resolve empty-pattern semantics and rule out a longer pattern before forming an unsigned candidate-range difference.

30. **A tight naive-search worst case.** To prove a matching worst case is tight, construct inputs that force the maximum comparisons at every feasible alignment.

31. **A matcher that misses the last start.** The last feasible substring start is inclusive; derive it from the last indexed character of the candidate.

32. **Reversal never swaps the terminator.** Reverse only the content interval and leave the terminator fixed; an odd-length middle byte needs no swap.

33. **Empty reversal and unsigned indices.** An expression inside a skipped body is not evaluated; verify guard placement before classifying unsigned-underflow consequences.

34. **Palindrome comparisons.** Distinguish pair comparisons, individual byte observations, and distinct memory locations when deriving exact counts.

35. **Filtering with retained-order proof.** For stable compaction, preserve the retained subsequence behind the read head and write a fresh terminator after the last retained byte.

36. **All removed, none removed.** Count the operations actually present in the algorithm, including self-writes and final termination, even when the string value is unchanged.

37. **Why repeated deletion is quadratic.** Sum suffix lengths for repeated shifting; a single retained-subsequence pass avoids revisiting the remaining input.

38. **Token count and empty fields.** Choose whether empty fields carry meaning before choosing a tokenizer; delimiter count plus one applies to the preserving policy.

39. **Nested tokenization state.** Independent tokenization traversals need independent continuation state; a null argument to `strtok` does not identify which previous sequence to resume.

40. **Line input at exact capacity.** A full `fgets` buffer without newline may be only a prefix of the line; preserve real data until stream status and policy are resolved.

41. **Removing newline without losing data.** Search for the specific delimiter before deleting it; length alone does not establish that the last byte is a newline.

42. **Formatted input width.** For `%s`, reserve an extra byte beyond the width; `%c` does not supply string termination or the same whitespace handling.

43. **Formatting and would-have length.** Interpret a nonnegative `snprintf` return as the untruncated content length; compare it with capacity and add one when allocating a complete result.

44. **The special zero-size formatting query.** Zero work does not automatically permit invalid pointers; rely on the particular interface's explicit null-pointer exception.

45. **Character classification domain.** Convert stored plain-char bytes into the classification domain before the call, and keep stream EOF distinct from character data.

46. **Numeric conversion needs a status.** Distinguish a valid zero, no conversion, trailing data, and range failure using the end pointer and error status.

47. **UTF-8 bytes and displayed characters.** Keep byte length, code-point count, and grapheme count separate; a correct byte transformation can still be an incorrect human-text transformation.

48. **Rows versus pointer tables.** A table's pointer storage does not include its referenced character arrays, and equal total sizes do not imply equal representations or assignment rules.

49. **Arguments and their final sentinel.** An argument-list sentinel is a null pointer, while an empty argument is a non-null pointer to a terminating character.

50. **Quadratic repeated concatenation.** Account for the increasing existing prefix at every append; enough capacity does not prevent quadratic rescanning.

51. **Geometric buffer growth.** A linear sum of geometric growth copies supports amortized cost, not a constant worst-case guarantee for each individual append.

52. **Reallocation and ownership.** Preserve the original owner until positive-size reallocation succeeds, then replace old aliases using the new allocation's pointer.

53. **Count abstract string values.** For capacity $C$, sum alphabet powers over content lengths zero through $C-1$, rather than assigning all slots to content.

54. **Count terminated storage states.** For complete storage states, account for arbitrary bytes after the first zero; abstract string counts deliberately identify those states as the same value.

55. **Probability of finding a terminator.** Use survival probabilities to count expected scan work, and distinguish a probabilistic initialized model from invalid uninitialized program data.

56. **All suffix lengths without rescanning.** Exploit a shared immutable terminator to derive suffix lengths arithmetically after one scan.

57. **Deleting a whole interval.** For interval deletion, move the surviving suffix through zero and reduce content length by the deleted interval length.

58. **Inserting an entire string.** Move the destination suffix including zero, but copy only inserted content into the gap so that the trailing suffix stays visible.

59. **Aliased insertion source.** An internal source can change when the destination shifts; preserve the original source value before applying a disjoint-source insertion algorithm.

60. **Replacing a substring with a different length.** Replacement length is old length minus removed content plus inserted content; preserve the entire trailing suffix including termination.

61. **An idiomatic copy expression.** In a sentinel-copy idiom, the terminating condition still performs the final assignment and both pointer increments.

62. **Precedence does not solve sequencing.** Check sequencing dependencies separately from precedence; a syntactically grouped expression can still contain unsequenced access and modification.

63. **Returning different kinds of storage.** Persistent lifetime does not imply writable or independently owned text; state all three properties in a string-returning interface.

64. **Constness and changing a view.** Const-qualified pointed-to access and a const pointer variable are separate restrictions; other writable aliases may still change a mutable object.

65. **A finite byte alphabet and character classes.** Validate both the byte universe and subscript signedness before using a byte-indexed lookup table.

66. **First mismatch distributions.** Expected first-mismatch work follows common-prefix survival probabilities, while equal strings still realize the linear worst case.

67. **Counting constrained values in a buffer.** Apply constrained sequence counting only to nonzero content positions, then account separately for the terminator and unused storage.

68. **Maximum naive comparison work over pattern length.** When pattern length varies, maximize both factors together; the number of alignments decreases as comparison depth increases.

69. **The last zero after mutation.** Mutation after one view's terminator may still change another view that starts later in the same array.

70. **Appending to a suffix view.** An interior string view inherits the remaining array extent, not the entire base capacity, and appending through it can extend the base view too.

71. **Copying the empty string.** The empty string requires one writable storage byte for copying; zero content length does not mean zero representation size.

72. **Zero append limit versus missing destination terminator.** An append limit constrains source content, not the search for the existing destination terminator.

73. **Course-inspired halving-index copy.** Debug a string routine by separating pointer validity, capacity, initialized indices, and termination from the intended indexing recurrence.

74. **Lowercase counting without encoding shortcuts.** State the character-class policy and argument domain; a familiar alphabetic range is not a language-independent classification guarantee.

75. **A valid bounded prefix need not be a string.** Bounded comparison can operate on a sufficiently readable nonterminated prefix; whole-string comparison requires string objects.

76. **An overlap check itself needs a domain.** Prove the domain of an overlap test itself; flat numerical address reasoning does not authorize arbitrary C pointer ordering.

77. **Storage states conditioned on length.** Conditioning on first-zero position fixes termination but leaves the suffix unrestricted; factor visible value choices from hidden storage choices.

78. **Concatenation versus raw copying.** Embedded zeros separate byte-region copying from string concatenation even when the visible output happens to agree.

79. **A proof of bounded matching safety.** Combine outer and inner index bounds to prove memory safety, then state the post-match advance policy independently.

80. **Combined capacity, mutation, and cost audit.** Recompute the logical length and terminator after each mutation, and derive movement counts from the current representation rather than the original one.
