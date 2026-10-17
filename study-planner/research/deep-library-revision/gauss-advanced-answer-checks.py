"""Independent bounded checks for LG26--LG69 expanded teaching solutions.

These exact checks support particular calculations and finite test families.
They do not turn finite examples into proofs of general theorems, establish
fresh source review, or mark the chapter approved. No dist files are changed.
"""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import re
import sys
from decimal import Decimal, localcontext, ROUND_HALF_EVEN

import sympy as s

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
M = s.Matrix
Q = s.Rational
I = s.eye
rows = {}
current = None


def task(identifier):
    global current
    current = identifier
    rows[identifier] = {"assertions": 0, "status": "passed"}


def check(condition):
    assert bool(condition), current
    rows[current]["assertions"] += 1


task("LG26")
A, b = M([[1, 1], [1, -1]]), M([1, 3])
E = M([[1, 1], [1, 1]])
check(A.inv() * b == M([2, -1]))
check(E.det() == 0 and E * A == M([[2, 0], [2, 0]]))
for t in range(-5, 6):
    check(E * A * M([2, t]) == E * b)
    check((A * M([2, t]) == b) == (t == -1))

task("LG27")
E, b = M([[1, 0], [-1, 1]]), M([3, 1])
check(E * b == M([3, -2]))
check(A.inv() * b == M([2, 1]))
bad = (E * A).inv() * b
check(bad == M([Q(7, 2), Q(-1, 2)]))
check(b - A * bad == M([0, -3]))
check(E.inv() * b == M([3, 4]))

task("LG28")
S, T = M([[0, 1], [1, 0]]), M([[1, 0], [3, 1]])
E, F = T * S, M([[-3, 1], [1, 0]])
check(E == M([[0, 1], [1, 3]]))
check(E * F == I(2) and F * E == I(2) and E.det() == -1)

task("LG29")
A, b = M([[1, 2], [3, 4]]), M([5, 11])
check(A * S == M([[2, 1], [4, 3]]))
y = (A * S).inv() * b
check(y == M([2, 1]) and S * y == M([1, 2]))
check(A * y == M([4, 10]))
check(A * S * y == b)

task("LG30")
A, Qm, b = M([[1, 2], [0, 1]]), M([[1, -2], [0, 1]]), M([5, 2])
check(A * Qm == I(2))
check(Qm * b == M([1, 2]))
check(A * Qm * b == b and Qm.inv() * M([1, 2]) == b)

task("LG31")
A, B = M([[2, 1], [1, 1]]), M([[1, -1], [-1, 2]])
check(A * B == I(2) and B * A == I(2))
check(A.det() == 1)
trace = [M([[2, 1, 1, 0], [1, 1, 0, 1]])]
trace.append(S * trace[-1])
trace.append(M([[1, 0], [-2, 1]]) * trace[-1])
trace.append(s.diag(1, -1) * trace[-1])
trace.append(M([[1, -1], [0, 1]]) * trace[-1])
check(trace[-1] == I(2).row_join(B))

task("LG32")
A, E = M([[1, 2], [2, 4]]), M([[1, 0], [-2, 1]])
check(E * A == M([[1, 2], [0, 0]]))
check(A.rank() == 1 and E.det() == 1)
t, c = s.symbols("t c")
check(A * M([c - 2*t, t]) == M([c, 2*c]))
check(M([[-2, 1]]) * A == s.zeros(1, 2))

task("LG33")
A, B = M([[1, 0], [0, 1], [1, 1]]), M([[1, 0, 0], [0, 1, 0]])
w = M([[-1, -1, 1]])
check(B * A == I(2))
check(A * B == M([[1, 0, 0], [0, 1, 0], [1, 1, 0]]))
check(w * A == s.zeros(1, 2))
u, v = s.symbols("u v")
check((B + M([u, v]) * w) * A == I(2))

task("LG34")
A = M([[2, 1, 1], [4, -6, 0], [-2, 7, 2]])
L, U = M([[1, 0, 0], [2, 1, 0], [-1, -1, 1]]), M([[2, 1, 1], [0, -8, -2], [0, 0, 1]])
b, y, x = M([5, -2, 9]), M([5, -12, 2]), M([1, 1, 2])
check(L * U == A)
check(L * y == b and U * x == y and A * x == b)

task("LG35")
A = S
check(A.det() == -1 and A * A == I(2))
l11, l21, l22, u11, u12, u22 = s.symbols("l11 l21 l22 u11 u12 u22")
check((M([[l11, 0], [l21, l22]]) * M([[u11, u12], [0, u22]]))[0, 0] == l11*u11)

task("LG36")
A = M([[4, 2, 0], [2, 1, 1], [1, 3, 1]])
P = M([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
L, U = M([[1, 0, 0], [Q(1, 4), 1, 0], [Q(1, 2), 0, 1]]), M([[4, 2, 0], [0, Q(5, 2), 1], [0, 0, 1]])
check(P * A == L * U)
badL = M([[1, 0, 0], [Q(1, 2), 1, 0], [Q(1, 4), 0, 1]])
check(list(badL * U)[3:] == [2, Q(7, 2), 1, 1, Q(1, 2), 1])
check(badL * U != P * A)

task("LG37")
P0, b = M([[0, 1, 0], [0, 0, 1], [1, 0, 0]]), M([1, 2, 3])
check(P0.T * b == M([3, 1, 2]))
check(P0 * (P0.T * b) == b)
check(P0 * (P0 * b) == M([3, 1, 2]))
check(P0 != P0.T)

task("LG38")
D = s.diag(2, 3, 5)
check((L * D) * (D.inv() * U) == L * U)
check(all((L * D)[i, j] == 0 for i in range(3) for j in range(i+1, 3)))
check(all((D.inv() * U)[i, j] == 0 for i in range(3) for j in range(i)))

task("LG39")
# Finite family instances support the determinant identity; the manuscript
# separately contains the induction proof of the universally quantified claim.
for z in range(-3, 4):
    LL = M([[1, 0, 0], [z, 1, 0], [2-z, z+1, 1]])
    UU = M([[2, z, 1], [0, -3, z-2], [0, 0, 5]])
    AA = LL * UU
    for k in (1, 2, 3):
        check(AA[:k, :k].det() == s.prod(UU[i, i] for i in range(k)))
    aa, rr, cc, dd = AA[0,0], AA[:1,1:], AA[1:,:1], AA[1:,1:]
    Sch = dd - cc * rr / aa
    for j in (1, 2):
        check(AA[:j+1,:j+1].det() == aa * Sch[:j,:j].det())

task("LG40")
delta = [1, 2, -6, 24]
pivots = [Q(delta[k], delta[k-1]) for k in (1, 2, 3)]
check(pivots == [2, -3, -4])
for k in (1, 2, 3):
    check(s.prod(pivots[:k]) == delta[k])

task("LG41")
A, b, x = M([[2, 1, 1], [4, 3, -1], [-2, 1, 2]]), M([1, 2, 0]), M([Q(5, 18), Q(1, 3), Q(1, 9)])
check(A * x == b)
Sch = A[1:, 1:] - A[1:, :1] * A[:1, 1:] / A[0,0]
check(Sch == M([[1, -3], [2, 3]]) and Sch.det() == 9)
check(b[1:, :] - A[1:, :1] * b[0] / A[0,0] == M([0, 1]))

task("LG42")
L, U = M([[1,0],[2,1]]), M([[3,1],[0,2]])
A = L * U
check(A == M([[3,1],[6,4]]))
for b, y, x in [(M([4,10]), M([4,2]), M([1,1])), (M([1,0]), M([1,-2]), M([Q(2,3),-1]))]:
    check(L*y == b and U*x == y and A*x == b)

task("LG43")
for n in range(1, 51):
    visits = sum(1 for i in range(n) for j in range(i+1, n))
    check(visits == n*(n-1)//2)
    check(2*visits+n == n*n)

task("LG44")
for n in range(1, 51):
    divides = sum(n-1-k for k in range(n-1))
    updates = sum(sum(1 for i in range(k+1,n) for j in range(k+1,n)) for k in range(n-1))
    check(divides == n*(n-1)//2)
    check(updates == (n-1)*n*(2*n-1)//6)
    check(divides+2*updates == Q(2,3)*n**3-Q(1,2)*n**2-Q(1,6)*n)

task("LG45")
A, b = M([[Q(1,10000),1],[1,1]]), M([1,2])
x = M([Q(10000,9999), Q(9998,9999)])
check(A*x == b)
def rounded_solve(pivot):
    # Decimal context rounds EACH multiplication/subtraction/division.
    with localcontext() as ctx:
        ctx.prec = 3
        ctx.rounding = ROUND_HALF_EVEN
        a,b,c,d,e,f = (map(Decimal, ["1","1","2","0.0001","1","1"]) if pivot else map(Decimal,["0.0001","1","1","1","1","2"]))
        mult = d/a
        newe = e-mult*b
        newf = f-mult*c
        yy = newf/newe
        xx = (c-b*yy)/a
        return (xx,yy)
check(rounded_solve(False) == (Decimal(0),Decimal(1)))
check(rounded_solve(True) == (Decimal(1),Decimal(1)))
check(b-A*M([0,1]) == M([0,1]))
check(b-A*M([1,1]) == M([-Q(1,10000),0]))
check(max(abs(z) for z in M([1,1])-x) == Q(1,9999))

task("LG46")
eps = s.symbols("eps", positive=True)
A, b, x, xh = M([[1,1],[1,1+eps]]), M([2,2+eps]), M([1,1]), M([2,0])
check(A*x == b and A.det() == eps)
check(b-A*xh == M([0,eps]))
check(A.inv() == M([[1+eps,-1],[-1,1]])/eps)
check(s.simplify((1+eps+1)/eps - (2+eps)/eps) == 0)
check(-A.inv()*(b-A*xh) == xh-x)

task("LG47")
A = s.diag(1,Q(1,10**12))
check(A.rank() == 2 and (10**12*A).rank() == 2)
check(sum(bool(abs(A[i,i]) > Q(1,10**10)) for i in range(2)) == 1)
check(sum(bool(abs((10**12*A)[i,i]) > Q(1,10**10)) for i in range(2)) == 2)
check(M([[1,-1],[1,1]]).det() == 2)

task("LG48")
A, L, U = M([[1,-1],[1,1]]), M([[1,0],[1,1]]), M([[1,-1],[0,2]])
check(L*U == A and abs(L[1,0]) <= 1)
check(max(abs(z) for z in U) == 2*max(abs(z) for z in A))
for a, c in itertools.product(range(-5,6), repeat=2):
    if max(abs(a),abs(c)):
        pivot = a if abs(a)>=abs(c) else c
        lower = c if abs(a)>=abs(c) else a
        check(abs(Q(lower,pivot)) <= 1)

task("LG49")
A,b = M([[1,1,0],[0,1,1],[1,0,1]]), M([1,0,1])
sol = [v for v in itertools.product(range(2),repeat=3) if all(z%2 == 0 for z in A*M(v)-b)]
check(sol == [(0,1,1),(1,0,0)])
check(A.det() == 2 and A.inv()*b == M([1,0,0]))

task("LG50")
A,b = M([[1,2],[2,4]]), M([1,2])
sol = [v for v in itertools.product(range(5),repeat=2) if all(z%5 == 0 for z in A*M(v)-b)]
expected = [(1,0),(4,1),(2,2),(0,3),(3,4)]
check(set(sol) == set(expected) and len(sol) == 5)
check([(1-2*t)%5 for t in range(5)] == [1,4,2,0,3])

task("LG51")
A = M([[1,1],[1,-1]])
check(A.det() == -2 and A.nullspace() == [])
sol = [v for v in itertools.product(range(2),repeat=2) if all(z%2 == 0 for z in A*M(v))]
check(sol == [(0,0),(1,1)])

task("LG52")
A,b = M([[2,1],[4,3]]), M([3,7])
check(A.inv()*b == M([1,1]))
bad = M([[2,1],[0,3]]).inv()*b
check(bad == M([Q(1,3),Q(7,3)]))
check(b-A*bad == M([0,-Q(4,3)]))

task("LG53")
A,b = M([[1],[1],[1]]), M([0,1,-1])
check(M([[-2,1,1]])*A == s.zeros(1,1))
check(M([[-2,1,1]])*b == M([0]))
check(A.rank() != A.row_join(b).rank())
R = M([[1,2,0],[0,1,3]])
c1,c2 = s.symbols("c1 c2")
xx = R.T*(R*R.T).inv()*M([c1,c2])
check(R*xx == M([c1,c2]))

task("LG54")
D = M([[1,0],[1,1],[0,-1]])
H = M([[1,-1,0],[0,1,1]])
xp = M([1,0,2])
check(H*D == M([[0,-1],[1,0]]) and (H*D).det() == 1)
check(xp+D*M([2,1]) == M([3,3,1]))
check(H*M([3,3,1]) == M([0,4]))

task("LG55")
A,E = M([[1,0],[1,0]]), M([[1,0],[-1,1]])
R = E*A
check(R == M([[1,0],[0,0]]))
check(A.rowspace() == R.rowspace() and A.nullspace() == R.nullspace())
check(A.columnspace() != R.columnspace())
check(E*M([1,1]) == M([1,0]))

task("LG56")
A = M([[1,2,3],[2,4,7]])
check(A.rref()[1] == (0,2))
check(A[:,[0,2]].det() == 1 and A.rank() == 2)
B = M([[1,2,3],[2,4,7],[3,6,10]])
T1,T2,T3 = M([[1,0,0],[-2,1,0],[0,0,1]]), M([[1,0,0],[0,1,0],[-3,0,1]]), M([[1,0,0],[0,1,0],[0,-1,1]])
SS = T3*T2*T1*B
check(SS == M([[1,2,3],[0,0,1],[0,0,0]]))
check(M([[-1,-1,1]])*B == s.zeros(1,3))
check(B.rank()==2 and SS.rank()==2)
check(B.row_join(M([1,0,0])).rank()==3)
check(SS.row_join(M([1,0,0])).rank()==2)
check(B.row_join(M([1,-1,0])).rank()==2)

task("LG57")
check(s.zeros(0,3).shape == (0,3) and s.zeros(0,3).rank()==0)
check(s.zeros(4,0).shape == (4,0) and s.zeros(4,0).rank()==0)
check(list(itertools.product([],repeat=0)) == [()])

task("LG58")
A,b = M([[2,1],[1,-2]]), M([1,0])
check(A.det()==-5 and A.inv()*b == M([Q(2,5),Q(1,5)]))
check(all((5*y-1)%5 != 0 for y in range(-10,11)))

task("LG59")
t = s.symbols("t", real=True)
x = M([t,t,4-2*t])
check(M([[1,1,1],[1,-1,0]])*x == M([4,0]))
check((1-t/2)*M([0,0,4])+(t/2)*M([2,2,0]) == x)
check(s.reduce_inequalities([t>=0,4-2*t>=0],t).as_set() == s.Interval(0,2))

task("LG60")
check((-1)**2 * s.prod([2,-3,5]) == -30)
check((-1)**1 * s.prod([2,-3,5]) == 30)

task("LG61")
A = M([[1,1],[2,2]])
check(A.det()==0 and A.rank()==1)
check(A.row_join(M([1,2])).rank()==1)
check(A.row_join(M([1,3])).rank()==2)
check(A*M([1-t,t]) == M([1,2]))

task("LG62")
B,C,D,E = M([[2,1],[1,2]]), M([[1,2,0],[0,1,1]]), M([[1,3],[-2,1]]), M([[1,0,2],[3,-1,1]])
AA = B.row_join(C).col_join(D.row_join(E))
TT = I(2).row_join(s.zeros(2,2)).col_join((-D*B.inv()).row_join(I(2)))
check(TT*AA == B.row_join(C).col_join(s.zeros(2,2).row_join(E-D*B.inv()*C)))
f,g = M([1,2]),M([3,4])
check(TT*f.col_join(g) == f.col_join(g-D*B.inv()*f))
check(TT.det()==1)

task("LG63")
L = M([[1,0,0],[2,1,0],[-1,3,1]])
N = L-I(3)
B = M([[1,0,0],[-2,1,0],[7,-3,1]])
check(N**3 == s.zeros(3,3) and N**2 == M([[0,0,0],[0,0,0],[6,0,0]]))
check(B == I(3)-N+N**2 and L*B == I(3) and B*L == I(3))
check((L*(I(3)-N))[2,0] == -6)

task("LG64")
g = M([0,0,2,-3])
e = M([[0,1,0,0]])
N = g*e
check(N**2 == s.zeros(4,4))
check((I(4)-N)*(I(4)+N) == I(4))
g1,g2 = s.symbols("g1 g2")
N = M([g1,g2])*M([[1,0]])
check(N**2 == g1*N)
check(s.simplify((I(2)-N)*(I(2)+N/(1-g1))) == I(2))
check((I(2)-M([1,3])*M([[1,0]])).det()==0)

task("LG65")
A = M([[1,0],[0,0],[0,0]])
b = M([0,2,5])
check(A.rank()==1 and A.row_join(b).rank()==2)
check(M([[0,0,2],[0,0,5]]).rank()==1)
check(s.zeros(2,1).row_join(I(2)).rank()==2)

task("LG66")
A,C = M([[1,0]]),M([[2,0]])
check(A.nullspace() == C.nullspace())
check(A*M([1,t])==M([1]) and C*M([Q(1,2),t])==M([1]))
check(C*M([1,t])==M([2]))

task("LG67")
A,b = M([[1,1,1],[2,-1,1]]),M([2,1])
check(A*M([1,1,0])==b)
check(A*M([1,1,-2])==M([0,-1]))
check(A*M([2,1,-3])==M([0,0]))
check(A*(M([1,1,0])+t*M([2,1,-3]))==b)
check(A.rank()==2 and len(A.nullspace())==1)

task("LG68")
f = (1+t)**2+(2-t)**2
check(s.expand(f-(2*(t-Q(1,2))**2+Q(9,2)))==0)
check(M([Q(3,2),Q(3,2)]).dot(M([1,-1]))==0)
check(f.subs(t,Q(1,2))==Q(9,2) and s.diff(f,t,2)==4)

task("LG69")
A = M([[1,1],[2,3]])
check(A.rref()[0]==I(2) and (S*A).rref()[0]==I(2))
for aa,bb in itertools.product(range(-3,4),repeat=2):
    b = M([aa,bb])
    check(A.row_join(b).rref()[0] == (S*A).row_join(S*b).rref()[0])

# Read exact question/provenance fields back from the final assembled manuscript.
manuscript = OUT / "l_gauss-advanced-answer-expansions.en.md"
text = manuscript.read_text(encoding="utf-8")
parts = re.split(r"^## (LG\d+)\s*$", text, flags=re.M)
sections = dict(zip(parts[1::2],parts[2::2]))
bank = json.loads((ROOT/"research/l_gauss-questions.json").read_text(encoding="utf-8"))
expected = [q for q in bank if 26<=int(q["id"][2:])<=69]
assert set(sections)=={q["id"] for q in expected}
for q in expected:
    section = sections[q["id"]]
    assert "**Question.** "+q["stem"] in section, q["id"]
    assert "**Provenance.** "+q["origin"] in section, q["id"]
    assert "**Title.** "+q["title"] in section, q["id"]
    assert "**Difficulty.** "+q["difficulty"] in section, q["id"]

# Strict native renderer validation tests actual manuscript formulas, including
# all stems, all matrices and each expanded mathematical explanation.
sys.path.insert(0,str(ROOT/"research/exam-rewrite"))
import mathml
mathml.wrap_display=lambda value:value
formulas = re.findall(r"\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$",text)
for display,inline in formulas:
    mathml.render(display or inline,bool(display))

report={
    "state":"passed_bounded_advanced_solution_checks",
    "chapter":"l_gauss",
    "questionRange":"LG26-LG69",
    "questions":len(expected),
    "assertions":sum(v["assertions"] for v in rows.values()),
    "formulasStrictlyRendered":len(formulas),
    "exactQuestionAndProvenanceFieldsPreserved":True,
    "manuscriptWordsIncludingStems":len(text.split()),
    "manuscriptSha256":hashlib.sha256(manuscript.read_bytes()).hexdigest(),
    "perQuestion":rows,
    "individualChapterReviewComplete":False,
    "studentApproval":False,
    "limits":[
        "Finite matrix families do not substitute for the universally quantified proofs written in the solutions.",
        "No fresh four-university source reread is claimed by this bounded answer revision.",
        "Browser layout, existing animations and authentic examination placements are outside this script's scope.",
        "The Decimal rounding model is three significant decimal digits after each scalar operation, not IEEE binary double precision.",
        "No guarantee is made about correctness on every possible unseen examination question."
    ]
}
(OUT/"gauss-advanced-answer-checks.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in report.items() if k!="perQuestion"},indent=2))
