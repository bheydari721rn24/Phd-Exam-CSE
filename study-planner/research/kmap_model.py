"""Exact small Boolean-cube model. Lexicographic terms, then literals."""
from itertools import product,combinations

def cells(c):
 return frozenset(i for i in range(1<<len(c)) if all(v=='-' or v==str((i>>(len(c)-1-j))&1) for j,v in enumerate(c)))
def valid(n,on,dc=()):
 allowed=set(on)|set(dc)
 return {''.join(c):cells(c) for c in product('01-',repeat=n) if cells(c)<=allowed and cells(c)&set(on)}
def primes(n,on,dc=()):
 vs=valid(n,on,dc)
 return {c:s for c,s in vs.items() if not any(s<t for t in vs.values())}
def qm(n,on,dc=()):
 current={format(i,f'0{n}b') for i in set(on)|set(dc)};out=set();levels=[]
 while current:
  used=set();nxt=set()
  for a,b in combinations(sorted(current),2):
   if [i for i,x in enumerate(a) if x=='-'] != [i for i,x in enumerate(b) if x=='-']:continue
   dif=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y]
   if len(dif)==1:
    j=dif[0];nxt.add(a[:j]+'-'+a[j+1:]);used.update([a,b])
  out|=current-used;levels.append(sorted(current));current=nxt
 return {c:cells(c) for c in sorted(out) if cells(c)&set(on)},levels
def cost(cover):return len(cover),sum(sum(v!='-' for v in c) for c in cover)
def optimum(n,on,dc=()):
 ps=primes(n,on,dc);on=set(on)
 if not on:return ps,[()],(0,0)
 best=None;solutions=[]
 for r in range(1,len(ps)+1):
  for cover in combinations(sorted(ps),r):
   if on<=set().union(*(ps[c] for c in cover)):
    k=cost(cover)
    if best is None or k<best:best=k;solutions=[cover]
    elif k==best:solutions.append(cover)
  if best is not None:break
 return ps,solutions,best
def term(c,pos=False):
 parts=[]
 for j,b in enumerate(c):
  if b=='-':continue
  name='ABCDEF'[j];negative=(b=='1' if pos else b=='0')
  parts.append('\\overline{'+name+'}' if negative else name)
 if not parts:return '0' if pos else '1'
 return '('+'+'.join(parts)+')' if pos else ''.join(parts)
def expr(cover,pos=False):
 if not cover:return '1' if pos else '0'
 return (' '.join if pos else '+'.join)(term(c,pos) for c in cover)
def essentials(ps,on):return sorted({next(c for c,s in ps.items() if m in s) for m in on if sum(m in s for s in ps.values())==1})
def petrick(ps,on):
 choices={frozenset()}
 for m in sorted(on):
  candidates={s|{c} for s in choices for c,v in ps.items() if m in v}
  choices={s for s in candidates if not any(t<s for t in candidates)}
 return sorted((tuple(sorted(s)) for s in choices),key=lambda s:(cost(s),s))
