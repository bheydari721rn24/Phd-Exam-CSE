"""Independent exact checks of worked arithmetic and guard boundary models.

This is not a C compiler and does not execute examples labelled undefined.
General arguments remain in the lesson; finite checks catch concrete slips.
"""
from fractions import Fraction
from pathlib import Path
import json, math, re
count=0
def check(condition):
 global count
 assert condition
 count+=1
def quotient(a,b):
 q=abs(a)//abs(b)
 return -q if (a<0)!=(b<0) else q

L,H=-128,127
for a in range(L,H+1):
 for b in range(L,H+1):
  accepted=not ((b>0 and a>H-b) or (b<0 and a<L-b))
  check(accepted == (L<=a+b<=H))
  sub=not ((b>0 and a<L+b) or (b<0 and a>H+b))
  check(sub == (L<=a-b<=H))
  if b and not (a==L and b==-1):
   q=quotient(a,b); r=a-b*q
   check(L<=q<=H and a==b*q+r and abs(r)<abs(b) and (r==0 or (r<0)==(a<0)))

for a in range(256):
 for b in range(256):
  check(a+b<=510 and (a+b)%256 == (a+b-256 if a+b>=256 else a+b))
  s=(a+b)%256
  check((s<a)==(a+b>=256)) # actual 8-bit unsigned arithmetic model
  check((a-b)%256==(a+256-b)%256)
for n in range(1000):
 for d in range(1,21):
  check(n//d+(n%d!=0)==-(-n//d))
for a in range(-1000,1001):
 for m in range(1,21):
  r=a-m*quotient(a,m)
  residue=r+m if r<0 else r
  check(residue==a%m and 0<=residue<m)

for (a,b),expected in { (17,5):(3,2),(-17,5):(-3,-2),(17,-5):(-3,2),(-17,-5):(3,-2)}.items():
 q=quotient(a,b); check((q,a-b*q)==expected)
check([z%256 for z in [-513,-256,-1,256,769]]==[255,0,255,0,1])
check((-3)%(2**32)==4294967293)
check(50000**2==2500000000 and 60000**2==3600000000)
check(Fraction(9,4)==Fraction(225,100))
check(float(2**53+1)==float(2**53) and float(2**53+2)!=float(2**53))
check((1e16 + -1e16)+1.0==1.0 and 1e16+(-1e16+1.0)==0.0)
check(0.1+0.2!=0.3)
check((6&3,6|3,6^3)==(2,7,5))
check(2147483647//2+(2147483647%2!=0)==1073741824)

ROOT=Path(__file__).resolve().parents[1]
manuscript='\n'.join((ROOT/'research'/f).read_text(encoding='utf-8') for f in ['p_types.en.md','p_types-problems.en.md','p_types-review.en.md'])
check(len(re.findall(r'^### Problem \d+ —',manuscript,re.M))==36)
for block in re.split(r'^### Problem \d+ —',manuscript,flags=re.M)[1:]:
 check('**Task.**' in block and '**Solution.**' in block)
rules=manuscript.split('### Fifty complete examination rules')[1].split('### Compact failure-to-repair map')[0]
check(len(re.findall(r'^\d+\. ',rules,re.M))==50)
check(not re.search(r'[\u0600-\u06ff\ufffd]',manuscript))
courses=json.loads((ROOT/'research/p_types-reviewed-courses.json').read_text(encoding='utf-8'))
check(len({c['university'] for c in courses})==5)
print(f'{count} exact/model and manuscript assertions passed. C examples were not compiled; undefined snippets were not run.')
