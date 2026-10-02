"""Independent finite-domain checks of the chapter's arithmetic/proof claims."""
from math import gcd,ceil
count=0
def check(condition):
 global count
 assert condition
 count+=1
for a in range(-20,21):
 for b in range(-20,21):
  for step in range(1,9):
   check(len(range(a,b,step))==max(0,ceil((b-a)/step)))
   check(len(range(a,b-1,-step))==max(0,(a-b)//step+1))
for modulus in (4,8,16,32,64):
 for step in range(1,modulus):
  seen=set();value=0
  while value not in seen: seen.add(value);value=(value+step)%modulus
  check(len(seen)==modulus//gcd(modulus,step))
  for target in range(modulus):check((target in seen)==(target%gcd(modulus,step)==0))
for n in range(101):
 i=odd_sum=0;odd=1
 while i<n:
  check(odd_sum==i*i and odd==2*i+1)
  odd_sum+=odd;odd+=2;i+=1
 check(odd_sum==n*n and odd_sum<=10000 and odd<=201)
 for budget in range(0,10001,37):
  accepted=[];s=0
  for value in range(1,n,2):
   if s+value>budget:break
   accepted.append(value);s+=value
  check(s<=budget and s==sum(accepted))
  candidates=list(range(1,n,2));k=len(accepted)
  check(k==len(candidates) or s+candidates[k]>budget)
for a in range(101):
 for b in range(101):
  if not(a or b):continue
  x,y=a,b
  while y:
   r=x%y;check(0<=r<y);check(gcd(x,y)==gcd(y,r));x,y=y,r
  check(x==gcd(a,b))
check((2.0**53)+1.0==2.0**53)
print(f'{count} independent finite-domain assertions passed: progression counts, modular reachability, accumulator invariants, budget exit and Euclid preservation.')
