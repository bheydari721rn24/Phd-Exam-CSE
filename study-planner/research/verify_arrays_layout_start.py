"""Independent finite array-layout oracle. No native pointer operations."""
import bisect
import hashlib
import itertools
import json
import math
import pathlib

ROOT=pathlib.Path(r'C:/Users/bheydari/.codex/.chatgpt-projects/g-p-6ab41269e8bc8191af2b98ca68a67648/study-planner')
OUT=ROOT/'research/deep-library-revision'
checks=[]
def check(name,passed,evidence):
    checks.append(dict(name=name,passed=bool(passed),evidence=evidence))
    if not passed: raise AssertionError(name)

# Independent reference layouts are constructed by enumeration of coordinates,
# not by reusing the stride formula as both specification and implementation.
indices=list(range(-3,9))
starts={i:1600+4*k for k,i in enumerate(indices)}
occupied=[byte for i in indices for byte in range(starts[i],starts[i]+4)]
check('PA01 actual declared lower bound',starts[5]==1632 and len(occupied)==48 and max(occupied)==1647,dict(index5=starts[5],element_starts=starts,storage=len(occupied),last_byte=max(occupied),one_past=max(occupied)+1))

coords=[(i,j) for i in range(2,7) for j in range(-1,6)]
addresses={4096+8*k:ij for k,ij in enumerate(coords)}
check('PA02 row-major inversion',addresses[4312]==(5,5) and 4313 not in addresses,dict(recovered=addresses[4312],element_count=len(coords),misaligned_element_start_rejected=4313 not in addresses,total_bytes=8*len(coords)))

solutions=[]
for columns in range(3,101):
    # The first observation determines base; independently list rows to recover
    # the second observed address, retaining the same proposed column extent.
    row_order=list(itertools.product(range(4),range(columns)))
    base=1028-4*row_order.index((1,2))
    if base+4*row_order.index((3,1))==1064:
        solutions.append((columns,base))
check('PA03 shape recovery',solutions==[(5,1000)],dict(candidates_columns=[3,100],solutions=solutions,rows='at least4; no finite upper row bound follows'))

row=list(itertools.product(range(4),range(6)))
col=[(i,j) for j in range(6) for i in range(4)]
same=[ij for ij in row if row.index(ij)==col.index(ij)]
check('PA04 distinct layouts',800+2*row.index((2,3))==830 and 800+2*col.index((2,3))==828 and same==[(0,0),(3,5)],dict(row_address=830,column_address=828,matching_coordinates=same))

triples=list(itertools.product(range(3),range(4),range(5)))
check('PA05 three-dimensional layout',triples.index((2,1,3))==48 and triples[47]==(2,1,2),dict(selected_offset=48,selected_address=2000+4*48,inverse47=triples[47],scope='zero-based normalized indices must be explicit'))

source=list(itertools.product(range(2),range(5)))
destination=list(itertools.product(range(5),range(2)))
mapping=[destination.index((j,i)) for i,j in source]
check('PA06 transpose mapping',mapping[7]==5 and mapping[9]==9 and sorted(mapping)==list(range(10)),dict(mapping=mapping,selected=[mapping[7],mapping[9]]))

view={(i,j):1020+40*i-4*j for i in range(3) for j in range(6)}
check('PA07 negative byte stride',view[(2,5)]==1080 and view[(1,0)]==1060 and min(view.values())==1000 and max(view.values())==1100,dict(selected=[view[(2,5)],view[(1,0)]],min_start=min(view.values()),max_start=max(view.values()),distinct_starts=len(set(view.values())),width='element width is not stated; occupied maximum byte not determined solely by stride'))

lower=[(i,j) for i in range(6) for j in range(i+1)]
check('PA08 packed symmetric lookup',lower.index((4,1))==11 and len(lower)==21,dict(canonical_coordinate=[4,1],offset=11,address=3000+8*11,packed_elements=len(lower),packed_bytes=8*len(lower)))
upper=[(i,j) for i in range(5) for j in range(i,5)]
check('PA09 upper triangle',upper.index((2,4))==11 and upper[9]==(2,2),dict(offset24=upper.index((2,4)),coordinate9=upper[9],packed_elements=len(upper)))

lengths=[2,0,3,1]
flat=[(i,j) for i,length in enumerate(lengths) for j in range(length)]
boundaries=[0]
for length in lengths:boundaries.append(boundaries[-1]+length)
check('PA10 empty jagged row',boundaries==[0,2,2,5,6] and flat[2]==(2,0) and flat[5]==(3,0),dict(boundaries=boundaries,offset2=flat[2],offset5=flat[5],first_equal_boundary2=boundaries.index(2),correct_upper_bound_row2=bisect.bisect_right(boundaries,2)-1))

n=5
flat=list(itertools.product(range(n),range(n)))
diagonal=[flat.index((i,i)) for i in range(n)]
check('PA11 diagonal',diagonal==[0,6,12,18,24] and sum(diagonal)==60,dict(offsets=diagonal,sum=sum(diagonal),distinct_count=len(set(diagonal))))
check('PA12 object relation',True,dict(classification='Separate allocations do not permit C pointer subtraction',missing_width='sizeof(int)=4 is not stated in original stem',conditional_numerical_calculation='(1040-1000)/4=10 only if four-byte elements are additionally stipulated',valid_array_alternative='same live array positions0 and10, legal endpoints, ptrdiff_t representable; object must have at least10 elements for position10 one-past, or11 for element10'))

layout_positions=layout_shapes=0
for R in range(1,17):
    for C in range(1,17):
        layout_shapes+=1
        rows=list(itertools.product(range(R),range(C)))
        cols=[(i,j) for j in range(C) for i in range(R)]
        col_index={ij:k for k,ij in enumerate(cols)}
        matching=0
        transposed=list(itertools.product(range(C),range(R)))
        transposed_index={ij:k for k,ij in enumerate(transposed)}
        targets=[]
        for offset,(i,j) in enumerate(rows):
            layout_positions+=1
            assert offset==i*C+j
            assert col_index[(i,j)]==j*R+i
            assert divmod(offset,C)==(i,j)
            same=offset==col_index[(i,j)]
            assert same==(i*(C-1)==j*(R-1))
            matching+=same
            target=transposed_index[(j,i)]
            assert target==j*R+i
            dj,di=divmod(target,R)
            assert (di,dj)==(i,j)
            targets.append(target)
        assert matching==math.gcd(R-1,C-1)+1
        assert sorted(targets)==list(range(R*C))
check('General2D layout/inverse/transpose',True,dict(shapes=layout_shapes,positions=layout_positions,extents='R,C=1..16',matching_count='gcd(R-1,C-1)+1, including single-axis cases',inverse='transpose inverse uses swapped destination shape'))

mixed_shapes=mixed_positions=0
for a,b,c in itertools.product(range(1,9),repeat=3):
    mixed_shapes+=1
    for offset,(i,j,k) in enumerate(itertools.product(range(a),range(b),range(c))):
        mixed_positions+=1
        assert offset==(i*b+j)*c+k
        q,t=divmod(offset,c)
        u,v=divmod(q,b)
        assert (u,v,t)==(i,j,k)
check('General mixed-radix proof support',True,dict(shapes=mixed_shapes,positions=mixed_positions,extents='each1..8',empty_extent='no element offset exists; division-based inversion must not be attempted'))

triangle_positions=symmetric_positions=0
for n in range(1,101):
    lower=[(i,j) for i in range(n) for j in range(i+1)]
    upper=[(i,j) for i in range(n) for j in range(i,n)]
    lower_index={ij:k for k,ij in enumerate(lower)}
    assert len(lower)==len(upper)==n*(n+1)//2
    for offset,(i,j) in enumerate(lower):
        triangle_positions+=1
        assert offset==i*(i+1)//2+j
    for offset,(i,j) in enumerate(upper):
        triangle_positions+=1
        assert offset==i*n-i*(i-1)//2+j-i
    for i,j in itertools.product(range(n),repeat=2):
        symmetric_positions+=1
        a,b=max(i,j),min(i,j)
        assert lower_index[(a,b)]==a*(a+1)//2+b
check('General packed triangle/canonical lookup',True,dict(n_range=[1,100],triangle_coordinates=triangle_positions,symmetric_coordinates=symmetric_positions,integer_scope='unbounded products; C requires intermediate-overflow proof'))

jagged_shapes=jagged_positions=0
for rows in range(6):
    for lengths in itertools.product(range(5),repeat=rows):
        jagged_shapes+=1
        boundaries=[0]
        for length in lengths:boundaries.append(boundaries[-1]+length)
        expected=[(i,j) for i,length in enumerate(lengths) for j in range(length)]
        for offset,(i,j) in enumerate(expected):
            jagged_positions+=1
            row=bisect.bisect_right(boundaries,offset)-1
            assert boundaries[row]<=offset<boundaries[row+1]
            assert (row,offset-boundaries[row])==(i,j)
        assert boundaries[-1]==len(expected)
check('General jagged inversion with empty rows',True,dict(shapes=jagged_shapes,positions=jagged_positions,row_counts='0..5',lengths='each0..4',algorithm='reject offset outside[0,total), then upper_bound(Q,offset)-1',all_empty='no valid offset; never return a coordinate'))

diagonal_cases=0
for n in range(101):
    offsets=[i*n+i for i in range(n)]
    diagonal_cases+=1
    assert len(set(offsets))==n and sum(offsets)==(n+1)*n*(n-1)//2
check('General diagonal sum and empty case',True,dict(cases=diagonal_cases,n_range=[0,100],empty='abstract only, not fixed-size C zero-bound declaration'))

affine_cases=0
for R,C in itertools.product(range(1,7),repeat=2):
    for sr,sc in itertools.product(range(-5,6),repeat=2):
        affine_cases+=1
        starts=[1000+sr*i+sc*j for i in range(R) for j in range(C)]
        assert min(starts)==1000+min(0,sr*(R-1))+min(0,sc*(C-1))
        assert max(starts)==1000+max(0,sr*(R-1))+max(0,sc*(C-1))
check('General affine min/max starts',True,dict(cases=affine_cases,shape='each axis1..6',strides='each-5..5',qualifications='zero stride or colliding strides can alias; byte coverage also needs element width; empty shape has no min/max'))

# Demonstrate a concrete contradiction in the unqualified lesson statement:
# D[l] += c is invalid for the permitted empty segment [n:n) in an n-entry D.
n=3
A=[1,2,3]
D=[A[0]]+[A[i]-A[i-1] for i in range(1,n)]
empty_error=None
try:D[n]+=7
except IndexError as e:empty_error=type(e).__name__
check('Lesson difference-rule boundary counterexample',empty_error=='IndexError',dict(n=n,permitted_segment=[n,n],D_length=len(D),failure=empty_error,correction='if l==r, do nothing; if n==0 do not read A[0] or D[0]; nonempty l<r implies l<n'))

result=dict(status='pass',check_count=len(checks),checks=checks,source_sha256=hashlib.sha256((ROOT/'research/p_arrays-questions.json').read_bytes()).hexdigest(),scope='PA01–PA12 and main-lesson representation/boundary consistency',limitations=['No C/C++ compilation or native pointer operation.','Numerical byte addresses do not establish pointer provenance or allocation validity.','Finite enumeration supports separately supplied proofs; it is not an exhaustive mathematical proof.','The original first12 answers have correct stated numeric outputs; model and boundary gaps are separately reported.'])
(OUT/'p_arrays-layout-independent-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(status=result['status'],checks=len(checks),output=str(OUT/'p_arrays-layout-independent-checks.json')),indent=2))
