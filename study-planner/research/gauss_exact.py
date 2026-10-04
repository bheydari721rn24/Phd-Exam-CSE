"""Exact row-operation certificates and independently checked chapter fixtures."""
from fractions import Fraction as F
def matrix(a):return [[F(x) for x in r] for r in a]
def identity(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def multiply(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mattex(a):
 def t(x):
  x=F(x);return str(x.numerator) if x.denominator==1 else ('-' if x<0 else '')+r'\frac{'+str(abs(x.numerator))+'}{'+str(x.denominator)+'}'
 return r'\begin{bmatrix}'+r'\\'.join('&'.join(t(x) for x in row) for row in a)+r'\end{bmatrix}'
def reduce(a,n=None):
 a=matrix(a);m=len(a);n=len(a[0]) if n is None else n;e=identity(m);steps=[];ids=list(range(m));pivots=[]
 def save(op):steps.append(dict(op=op,matrix=[list(map(str,r)) for r in a],transform=[list(map(str,r)) for r in e],ids=ids[:],pivots=pivots[:]))
 save('Original augmented matrix');r=0
 for c in range(n):
  p=next((i for i in range(r,m) if a[i][c]),None)
  if p is None:save('Skip coefficient column '+str(c+1)+': no available pivot');continue
  if p!=r:
   a[p],a[r]=a[r],a[p];e[p],e[r]=e[r],e[p];ids[p],ids[r]=ids[r],ids[p];save('Swap rows '+str(p+1)+' and '+str(r+1))
  v=a[r][c]
  if v!=1:
   a[r]=[x/v for x in a[r]];e[r]=[x/v for x in e[r]];save('Divide row '+str(r+1)+' by '+str(v))
  pivots.append(c)
  for i in range(m):
   if i!=r and a[i][c]:
    v=a[i][c];a[i]=[x-v*y for x,y in zip(a[i],a[r])];e[i]=[x-v*y for x,y in zip(e[i],e[r])];save('Row '+str(i+1)+' minus ('+str(v)+') times row '+str(r+1))
  r+=1
  if r==m:break
 save('Coefficient reduction complete');return a,pivots,e,steps
def solve(a):
 n=len(a[0])-1;r,p,e,s=reduce(a,n)
 if any(not any(row[:n]) and row[n] for row in r):return r,p,None,[],e,s
 x=[F(0)]*n
 for i,c in enumerate(p):x[c]=r[i][n]
 basis=[]
 for c in range(n):
  if c not in p:
   v=[F(0)]*n;v[c]=1
   for i,k in enumerate(p):v[k]=-r[i][c]
   basis.append(v)
 return r,p,x,basis,e,s
def plu(a):
 u=matrix(a);n=len(u);l=identity(n);p=identity(n)
 for k in range(n):
  j=max(range(k,n),key=lambda i:abs(u[i][k]))
  if not u[j][k]:raise ValueError('Singular')
  if j!=k:
   u[k],u[j]=u[j],u[k];p[k],p[j]=p[j],p[k]
   l[k][:k],l[j][:k]=l[j][:k],l[k][:k]
  for i in range(k+1,n):
   l[i][k]=u[i][k]/u[k][k]
   for c in range(k,n):u[i][c]-=l[i][k]*u[k][c]
 return p,l,u
