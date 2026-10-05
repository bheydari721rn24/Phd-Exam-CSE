from pathlib import Path
from itertools import permutations
from math import factorial
import json
B=Path(__file__).resolve().parent;rows=[]
def row(mode,n,m,cap,count,atoms=None):rows.append(dict(mode=mode,n=n,m=m,cap=cap,count=count,atoms=atoms or []))
for n in range(9):
 for m in range(5):
  s=[1]+[0]*m
  for _ in range(n):s=[0]+[s[k-1]+k*s[k] for k in range(1,m+1)]
  row('maps',n,m,2,factorial(m)*s[m])
 for m in range(min(n,4)+1):row('permutations',n,m,2,sum(all(p[i]!=i for i in range(m)) for p in permutations(range(n))))
 for m in range(1,5):
  for cap in range(6):
   a=[1]+[0]*n
   for _ in range(m):a=[sum(a[t-i] for i in range(min(cap,t)+1)) for t in range(n+1)]
   row('caps',n,m,cap,a[n])
for seed in range(12):
 atoms=[(seed+i*i+3*i)%51 for i in range(8)];row('sets',0,0,0,sum(atoms[1:]),atoms)
(B/'d_inclusion-lab-reference.json').write_text(json.dumps(rows)+'\n');print('Independent exact lab reference cases:',len(rows))
