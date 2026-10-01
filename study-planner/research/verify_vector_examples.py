"""Independent exact checks for vector examples and finite geometry identities.

These are numerical/algebraic regression checks, not substitutes for chapter proofs.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose, sqrt

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(c,x): return tuple(c*a for a in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def norm2(x): return dot(x,x)
def proj(x,b,inner=dot): return scale(F(inner(b,x),inner(b,b)),b)
def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])

checks = 0
def require(statement):
    global checks
    assert statement
    checks += 1

# Explicit worked-answer data, computed independently from coordinate definitions.
require(sub((-1,4,5),(2,-1,3)) == (-3,5,2))
require(add(scale(3,(1,2)),scale(2,(2,-1))) == (7,4))
require(norm2((1,-2,2)) == 9 and norm2(sub((1,-2,2),(-1,1,2))) == 13)
x=(2,-1,3); b=(1,2,2)
p=proj(x,b); r=sub(x,p)
require(p == (F(2,3),F(4,3),F(4,3)) and norm2(r)==10 and dot(r,b)==0)
x=(1,2,3); b1=(1,-1,0); b2=(1,1,-2)
p=add(proj(x,b1),proj(x,b2))
require(p==(-1,0,1) and norm2(sub(x,p))==12)
weighted=lambda a,b:4*a[0]*b[0]+a[1]*b[1]
p=proj((1,0),(1,1),weighted); r=sub((1,0),p)
require(p==(F(4,5),F(4,5)) and weighted(r,r)==F(4,5))
require(weighted(r,(1,1))==0)
inner=lambda a,b:sum(complex(u).conjugate()*v for u,v in zip(a,b))
x=(1j,0); b=(1,1j); coefficient=inner(b,x)/inner(b,b)
p=scale(coefficient,b); r=sub(x,p)
require(p==(.5j,-.5) and inner(b,r)==0 and inner(r,r)==.5)
require(inner((1,),(1j,))==1j and inner((1j,),(1,))==-1j)
require(abs(1+1j)**2 > 1.999999 and inner((1,),(1j,)) != 0)
qs=[scale(1/sqrt(2),(1,1,0)),scale(1/sqrt(6),(1,-1,2)),scale(1/sqrt(3),(-1,1,1))]
for i,q in enumerate(qs):
    for j,z in enumerate(qs): require(isclose(dot(q,z),int(i==j),abs_tol=1e-12))
qw=[scale(1/sqrt(5),(1,1)),scale(1/(2*sqrt(5)),(1,-4))]
require(isclose(weighted(qw[0],qw[1]),0,abs_tol=1e-12))
for q in qw: require(isclose(weighted(q,q),1,abs_tol=1e-12))
base=(1,2); x=(4,0); b=(2,1)
foot=add(base,proj(sub(x,base),b))
require(foot==(F(13,5),F(14,5)) and norm2(sub(x,foot))==F(49,5))
x=(3,1,2); n=(1,2,2); d=3
foot=sub(x,scale(F(dot(n,x)-d,norm2(n)),n))
require(foot==(F(7,3),F(-1,3),F(2,3)) and dot(n,foot)==d and norm2(sub(x,foot))==4)
require(cross((1,1,0),(0,1,2))==(2,-2,1))
require(dot((1,0,1),cross((0,2,0),(1,1,0)))==-2)

# Integral calculations are exact rational polynomial integrations over [-1,1].
def integral(coefficients): return sum(F(2*c,k+1) for k,c in enumerate(coefficients) if k%2==0)
require(integral([0,0,0,F(-1,3),0,1])==0)
require(integral([F(1,9),0,F(-2,3),0,1])==F(8,45))
require(integral([0,0,0,0,0,0,1])==F(2,7))

# Exhaustively test 729 vector pairs with coordinates in {-1,0,1}.
vectors=list(product((-1,0,1),repeat=3))
for x in vectors:
    for y in vectors:
        xy=dot(x,y); xx=norm2(x); yy=norm2(y)
        require(norm2(add(x,y))==xx+2*xy+yy)
        require(norm2(add(x,y))+norm2(sub(x,y))==2*(xx+yy))
        require(xy*xy <= xx*yy)
        z=cross(x,y)
        require(dot(x,z)==dot(y,z)==0)
        require(norm2(z)==xx*yy-xy*xy)
        if yy:
            p=proj(x,y); r=sub(x,p)
            require(dot(r,y)==0 and norm2(r)+norm2(p)==xx)
            for t in (-2,-1,0,1,2):
                c=F(xy,yy)
                require(norm2(sub(x,scale(t,y)))==norm2(r)+(t-c)**2*yy)
print(f"Vector verification passed: {checks} independent exact/numerical assertions, 729 vector pairs, worked-answer checks, complex/weighted projections, and exact polynomial integrals.")
