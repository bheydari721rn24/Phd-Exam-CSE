# Arrays: individual solution revision, first twelve problems

Status: review manuscript, not integrated into the student chapter. The whole chapter remains under review. Proposed stem clarifications are recorded explicitly instead of silently supplying unstated assumptions.

## PA01 | Normalize the logical index before counting bytes

The inclusive logical interval from minus three through eight contains $8-(-3)+1=12$ elements. The first element is at logical index minus three, so the normalized offset of index five is $5-(-3)=8$. This counts eight complete element widths before the requested element; it does not use the element's stored value.

With base address 1600 and width four, the requested starting address is

$$1600+4\cdot8=1632.$$

All twelve elements occupy $12\cdot4=48$ bytes. Consequently the inclusive final occupied byte is $1600+48-1=1647$, whereas the one-past boundary is 1648. The last element itself begins at $1600+4\cdot11=1644$ and occupies bytes 1644 through 1647. These three endpoints must not be conflated.

As a consistency check, logical index minus three maps to 1600, and index eight maps to 1644. Increasing a valid index by one increases its starting address by exactly four. Computing 1600 plus four times five would incorrectly assume a zero lower bound. This is a numerical flat-storage model with language-independent declaration bounds, not an ordinary C declaration allowing negative array bounds or a claim about portable integer-to-pointer conversion.

## PA02 | Invert the layout only after checking alignment and extent

**Stem clarification required.** Explicitly say row-major in the stem; the title presently supplies this information, but the numerical observations alone do not determine the layout.

There are five rows, from two through six, and seven columns, from minus one through five. The byte displacement is $4312-4096=216$. Because 216 is divisible by the stated element width eight, the requested address can be an element start. Its normalized element offset is $216/8=27$.

For row-major storage, divide by the column extent seven:

$$27=3\cdot7+6.$$

Thus the normalized coordinates are (3,6), and adding the declared lower bounds gives row $2+3=5$ and column $-1+6=5$. Reconstructing verifies the answer: $4096+8(3\cdot7+6)=4312$. Both declared coordinates lie within their respective bounds, and the flat offset is below the total extent $5\cdot7=35$.

If the same declared matrix instead used column-major storage, dividing 27 by five would yield normalized column five and row two, hence logical coordinate (4,4). This distinct valid result explains why stating the layout is necessary. Address 4313 lies inside an element rather than at its start and fails the alignment test before coordinate recovery is attempted.

## PA03 | Eliminate the unknown base by subtraction

Let C denote the unknown positive column count and B the starting byte address. With zero-based row-major indices and four-byte elements, the two observations give

$$1028=B+4(C+2),\qquad1064=B+4(3C+1).$$

Subtracting the equations removes B:

$$36=4(2C-1).$$

Therefore $2C-1=9$, so C is five. Substitution into the first equation gives $B=1028-4\cdot7=1000$. The second observation independently reconstructs as $1000+4(3\cdot5+1)=1064$.

Column indices one and two are legal for a five-column row, and observing row three requires at least four rows. Nothing in either equation states the final row index, so the total number of rows remains undetermined. Every row count at least four is consistent with these observations under the declared flat layout.

This is an inverse problem with a consistency condition, rather than permission to report any algebraic result as a shape. A noninteger or nonpositive solution for C, or a column observation outside the recovered extent, would invalidate the proposed representation. Once C is known, its byte row stride is twenty; the observed displacement thirty-six equals two row strides minus one element width, exactly matching the move from (1,2) to (3,1).

## PA04 | A matching address does not identify a layout

The row-major offset of (2,3) in four rows and six columns is $2\cdot6+3=15$. With base 800 and two-byte elements, its address is 830. In column-major storage, the offset is $3\cdot4+2=14$, giving address 828. These calculations use the same coordinate and different declared storage conventions.

For an arbitrary valid coordinate (i,j), equality of the two offsets requires

$$iC+j=jR+i,\qquad i(C-1)=j(R-1).$$

Here the condition becomes $5i=3j$. Since three and five are coprime, integer solutions have $i=3t$ and $j=5t$. Within $0\le i<4$ and $0\le j<6$, only t equal to zero or one is possible. Thus the two matching coordinates are (0,0) and (3,5), the common first and final positions. The requested (2,3) is neither of them.

More generally, for both dimensions greater than one, the number of matching coordinates is $\gcd(R-1,C-1)+1$. The one-row or one-column cases need separate treatment because the two orders then coincide throughout. These formulas compare two numerical representations; they do not make column-major traversal a second interpretation of the type and layout of one declared C rectangular array.

## PA05 | Decode the last axis first

**Stem clarification required.** State explicitly that all three axes are zero-based. Extents alone do not name logical lower bounds.

For zero-based row-major extents three, four and five, advancing the first coordinate skips twenty elements per unit, advancing the second skips five, and advancing the final coordinate skips one. Coordinate (2,1,3) therefore has offset

$$2\cdot20+1\cdot5+3=48.$$

Its starting byte address is $2000+4\cdot48=2192$. Each coordinate is legal and offset 48 lies below the total extent sixty.

To recover the coordinate of offset 47, take quotient and remainder by the final extent: $47=9\cdot5+2$. Hence the last coordinate is two. Decode the remaining quotient using the middle extent: $9=2\cdot4+1$. The first two coordinates are therefore two and one, giving (2,1,2). Reconstruction yields $(2\cdot4+1)5+2=47$.

This is mixed-radix uniqueness: each remainder is in the valid range of its corresponding axis, and the final first-coordinate quotient must be below three. Simply summing indices loses the skipped rows and planes. Offset sixty would fail the total-extent test even though repeated division could still produce a three-number tuple; the inverse algorithm must validate the recovered leading coordinate too.

## PA06 | Transposition changes the stride as well as the coordinates

The source has two rows and five columns. For a source flat offset o, recover its coordinates with quotient and remainder by five. Then swap the coordinates, and encode them using the destination's two columns, not the source's five.

For offset seven, $7=1\cdot5+2$ identifies source (1,2). Its transpose coordinate is (2,1), whose destination offset is $2\cdot2+1=5$. For offset nine, $9=1\cdot5+4$ gives source (1,4), destination (4,1), and new offset $4\cdot2+1=9$.

In general the mapping is

$$iC+j\longmapsto jR+i.$$

It is bijective because destination coordinates (j,i) recover the unique source (i,j), with the destination shape C by R. In this two-by-five case the complete source-to-destination offset list is [0,2,4,6,8,1,3,5,7,9], containing each offset zero through nine exactly once.

The fixed final offset nine therefore does not imply an unchanged arrangement. A transpose view that exchanges strides and a physically copied transpose are distinct implementations of the coordinate relation. Likewise, the pairwise square-matrix swap loop cannot be applied unchanged to this rectangular physical arrangement; its permutation contains longer cycles.

## PA07 | A negative stride reverses an axis without changing its bounds

The stated numerical affine map is

$$X(i,j)=1020+40i-4j,\qquad0\le i<3,\quad0\le j<6.$$

Thus $X(2,5)=1020+80-20=1080$, and $X(1,0)=1060$. The row term is increasing and the column term is decreasing over independent rectangular index bounds. Its minimum is therefore at (0,5), giving 1000, and its maximum is at (2,0), giving 1100.

The three rows select starting addresses 1020,1016,...,1000; then 1060,1056,...,1040; then 1100,1096,...,1080. This explicit list checks both extrema and exposes the gaps between successive selected row ranges. A shape-only dense row-major formula would incorrectly discard the negative column direction and the forty-byte row stride.

The requested extrema concern element starts. The statement does not explicitly declare element byte width, so it does not by itself determine the final occupied byte. If an additional four-byte-width convention is imposed, the last selected element occupies through 1103. That is a conditional conclusion, not an assumption inferred solely from a stride of minus four. A backing allocation and typed-object contract must also cover all accesses; these numerical addresses alone do not prove valid C pointer arithmetic or provenance.

## PA08 | Normalize by symmetry before using the packed formula

Only lower-triangle positions with $0\le j\le i<6$ are physically stored. The logical request (1,4) is above that diagonal. Symmetry of values permits redirecting it to stored coordinate (4,1); without symmetry, this replacement would have no general justification.

Before row four lie rows zero through three, of lengths one, two, three and four. Their total is ten. Column one is one position after the start of stored row four, so its flat offset is eleven and its address is

$$3000+8\cdot11=3088.$$

The lower-triangle row-major encoding is $i(i+1)/2+j$ on its declared domain. Substituting (4,1) reproduces eleven. Applying that encoding directly to the unnormalized upper coordinate (1,4) would produce six, but that number denotes a different physical position and is not an alternative correct answer.

The packed representation has $6\cdot7/2=21$ stored elements. Its final element starts at 3160, so the requested 3088 lies within the packed extent and has the required eight-byte alignment relative to the base. Equal total storage counts would not identify the order by themselves: storing columns, omitting the diagonal or packing the upper triangle would require a different coordinate formula.

## PA09 | Decreasing row lengths require a different prefix count

In an upper triangle of order five, stored row lengths are five, four, three, two and one. Before row two there are five plus four, or nine entries. That row begins at column two, so column four is two positions later. Its flat offset is $9+(4-2)=11$.

To invert offset nine, locate its row interval. Row zero occupies [0,5), row one [5,9), and row two [9,12). Therefore offset nine is the first entry of row two, coordinate (2,2), rather than the final entry of row one.

For general order n and a valid upper coordinate $0\le i\le j<n$, the preceding rows contain

$$\sum_{r=0}^{i-1}(n-r)=in-\frac{i(i-1)}2.$$

Adding within-row offset j-i gives the full encoding. This is not the lower-triangle prefix $i(i+1)/2$, because row lengths decrease instead of increase. Both conventions happen to store $n(n+1)/2$ entries, but equal capacities do not imply equal coordinate maps.

The half-open row intervals also give a safe inverse strategy: find the unique row whose start is at most the flat offset and whose next start is larger, then add the within-row displacement to that row's diagonal column. A final boundary equal to fifteen is one-past, not a valid stored coordinate.

## PA10 | Repeated boundaries identify empty rows, not duplicate elements

Starting with zero, prefix accumulation of row lengths [2,0,3,1] gives boundary array Q = [0,2,2,5,6]. Row i occupies the half-open flat interval [Q[i],Q[i+1]). Thus row zero contains offsets zero and one; row one contains no offset; row two contains two,three,four; row three contains five.

Offset two therefore belongs to row two at column zero, and offset five belongs to row three at column zero. The duplicate boundary two does not create two copies of an element. It records that the intervening row has length zero.

For a valid flat offset o, the inverse condition is

$$Q[i]\le o<Q[i+1],\qquad j=o-Q[i].$$

With nondecreasing boundaries and a prior check $0\le o<Q[4]$, this row can be found as the last boundary not exceeding o, equivalently a right-biased upper-bound search minus one. A first-equal-boundary rule fails at repeated boundaries: it can select the empty row one for offset two.

The input bound check is essential. Offset six is the final one-past boundary, so no row owns it. Repeated trailing boundaries from empty final rows do not change that conclusion. This representation packs element storage contiguously while allowing rows to have different lengths; it is not a dense rectangular matrix with one fixed row stride.

## PA11 | Count positions separately from summing their offsets

For zero-based diagonal coordinate (i,i) in a dense n-by-n row-major matrix, each earlier row contributes n elements and the column contributes another i. The flat offset is therefore $in+i=i(n+1)$ for $0\le i<n$.

There are n selected coordinates. Their offsets form an arithmetic progression with first term zero, last term $(n-1)(n+1)$ and spacing n+1. Hence

$$\sum_{i=0}^{n-1}i(n+1)=(n+1)\frac{n(n-1)}2.$$

For n equal to five, the selected offsets are [0,6,12,18,24], and their sum is sixty. The selection contains five positions, not twenty-five; the underlying matrix's capacity is not the number of loop visits on its diagonal.

For a nonempty matrix the offsets are distinct because n+1 is positive. At n equal to one, the only offset is zero. At n equal to zero, the abstract index set is empty, the count and sum are zero, and the symbolic formula agrees. This mathematical convention does not license a standard C fixed-size array with a zero bound. Finally, these are sums of positions: the sum of matrix values on those positions cannot be recovered without data values or a separate rule relating values to offsets.

## PA12 | Byte closeness cannot establish a common array object

The observed numerical difference is forty bytes, but C pointer subtraction requires more than a numerical address representation. Both pointer operands must designate elements of one array object, or its permitted one-past position, and the resulting element difference must be representable in ptrdiff_t. Two separate live allocations do not satisfy that shared-array requirement merely because their addresses happen to be near each other.

Moreover, the stem does not state sizeof(int). If a particular implementation uses four-byte integers, forty divided by four is ten as a numerical calculation. That conditional arithmetic does not make subtraction between the actual unrelated pointers defined. If the width is different, even the numerical quotient changes.

Under a different valid setup, let p designate element zero and q designate element ten of one sufficiently large live integer array, with a representable difference. Then q-p equals ten elements regardless of the byte width. Reversing the subtraction yields minus ten. If q is the permitted one-past element at index ten of a ten-element array, subtraction can still be valid although dereferencing q is not.

This separates three facts: byte-address arithmetic in a stipulated representation, element-distance arithmetic within a known array, and legal element access. Neither alignment nor a plausible integer result can substitute for the missing object-domain condition.
