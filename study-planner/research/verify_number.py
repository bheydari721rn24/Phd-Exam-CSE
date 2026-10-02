"""Independent finite arithmetic and codebook checks; no archived exams."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
checks=0
def check(condition):
 global checks
 assert condition
 checks+=1
def signed(u,n):return u-(1<<n) if u&(1<<(n-1)) else u
for n in range(2,9):
 M=1<<n;top=M//2
 for a in range(M):
  sa=signed(a,n)
  check(sa==sum((((a>>i)&1)*(-top if i==n-1 else 1<<i)) for i in range(n)))
  neg=(-a)%M
  check(neg==((M-1-a)+1)%M)
  check((neg==a)==(a in (0,top)))
  for b in range(M):
   sb=signed(b,n)
   for subtract in (False,True):
    exact=sa-sb if subtract else sa+sb
    r=(a-b if subtract else a+b)%M;sr=signed(r,n)
    overflow=not -top<=exact<top
    sign_formula=((sa<0)!=(sb<0)) and ((sr<0)!=(sa<0)) if subtract else ((sa<0)==(sb<0)) and ((sr<0)!=(sa<0))
    check(overflow==sign_formula)
    # Carry into sign bit from independent lower-word arithmetic.
    op=(M-1-b) if subtract else b;initial=int(subtract)
    cin=((a%(top))+(op%(top))+initial)//top
    cout=(a+op+initial)//M
    check(overflow==(cin!=cout))
    check(exact==sr+(cin-cout)*M)
    if subtract:
     check(cout==int(a>=b))
     check((sr<0)^overflow==(sa<sb))
   check((sa*sb)%M==(a*b)%M)
  # Width-preservation criteria, checked against exact decoded values.
  for m in range(1,n):
   retained=a% (1<<m);preserved=signed(retained,m)==sa
   expected=(a>>m)==((1<<(n-m))-1 if retained&(1<<(m-1)) else 0)
   check(preserved==expected)
  wider=(a+((1<<(n+3))-M) if sa<0 else a)
  check(signed(wider,n+3)==sa)
  for k in range(1,n):
   shifted=((a>>k)|(((M-1)<<(n-k))&(M-1))) if sa<0 else a>>k
   check(signed(shifted,n)==sa//(1<<k))
   towardzero=-(abs(sa)//(1<<k)) if sa<0 else sa//(1<<k)
   biased=(sa+(1<<k)-1)//(1<<k) if sa<0 else sa//(1<<k)
   check(towardzero==biased)
for n in range(1,13):
 M=1<<n;codes=[i^(i>>1) for i in range(M)]
 check(len(set(codes))==M)
 for i,g in enumerate(codes):
  v=g;decode=0
  while v:decode^=v;v>>=1
  check(decode==i)
  check((g^codes[(i+1)%M]).bit_count()==1)
for a in range(10):
 for b in range(10):
  for cin in (0,1):
   t=a+b+cin;originalcarry=t//16;low=t%16
   correction=bool(originalcarry or low>9)
   digit=(low+6 if correction else low)%16
   check(digit==t%10)
   check(int(correction)==t//10)
aiken=[0,1,2,3,4,11,12,13,14,15]
for d,w in enumerate(aiken):
 check(sum(((w>>(3-i))&1)*weight for i,weight in enumerate((2,4,2,1)))==d)
 check((w^15)==aiken[9-d])
 check(((d+3)^15)==(9-d)+3)
def encode_hamming(data):
 bits=[0]*8
 for position,value in zip((3,5,6,7),data):bits[position]=value
 for p in (1,2,4):bits[p]=sum(bits[i] for i in range(1,8) if i&p)%2
 return sum(bits[i]<<(i-1) for i in range(1,8))
def syndrome(word):
 return sum((sum((word>>(i-1))&1 for i in range(1,8) if i&p)%2)*p for p in (1,2,4))
codewords=[encode_hamming([(x>>i)&1 for i in range(4)]) for x in range(16)]
check(min((a^b).bit_count() for a,b in combinations(codewords,2))==3)
extended=[w|((w.bit_count()%2)<<7) for w in codewords]
check(min((a^b).bit_count() for a,b in combinations(extended,2))==4)
for w in codewords:
 check(syndrome(w)==0)
 for p in range(1,8):
  corrupted=w^(1<<(p-1));s=syndrome(corrupted)
  check(s==p);check((corrupted^(1<<(s-1)))==w)
for w in extended:
 for errors in (0,1,2):
  for positions in combinations(range(8),errors):
   corrupted=w
   for p in positions:corrupted^=1<<p
   s=syndrome(corrupted&127);parity=corrupted.bit_count()%2
   if errors==0:check(s==parity==0)
   elif errors==1:
    check(parity==1)
    corrected=corrupted^(1<<(s-1)) if s else corrupted^128
    check(corrected==w)
   else:check(parity==0 and s!=0)
# Exact numerical answers from the worked problems and manuscript.
check(int('1004',7)==347)
check(F(43)+F(6,16)==F('43.375'))
check(F(53)+F(11,16)==F('53.6875'))
check(F(1,12)+F(9,144)==F(7,48))
check(F(1,4)+F(5,28)==F(3,7))
check(F(3,30)==F(1,10)) # 0.0 repeating 0011 in binary.
check(F('0.1')-F(25,256)==F('0.00234375'))
check(F(26,256)-F('0.1')==F('0.0015625'))
check(1029==int('010000000101',2)==int('2005',8)==int('405',16))
check(encode_hamming((1,0,1,1))==int('1100110',2)) # positional storage is low-position-first.
for integer in range(-100,101):
 for den in (2,4,8,10,16,32):
  x=F(integer,den)
  for f in range(0,7):
   q=round(x*(1<<f));check(abs(F(q,1<<f)-x)<=F(1,1<<(f+1)))
report=dict(assertions=checks,wordWidths=list(range(2,9)),grayWidths=list(range(1,13)),bcdSubtotals=200,hammingDataWords=16,quantizerCases=201*6*7,limitations='Finite arithmetic/codebook verification, not a universal correctness proof or an examination guarantee.')
out=Path(__file__).with_name('g_number-verification.json');out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
