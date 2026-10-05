"""Targeted mathematical typography and problem-specific visual scope corrections."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent
replacements={
 '2^ceil(log2(m))−1':r'$2^{\lceil\log_2 m\rceil}-1$',
 'Catalan Cn equals binom(2n,n)/(n+1)':r'Catalan $C_n$ equals $\binom{2n}{n}/(n+1)$',
 'leftTop+1=rightTop':r'$\ell+1=r$',
 'rightTop−leftTop−1':r'$r-\ell-1$',
 '(f+j) mod C':r'$(f+j)\bmod C$',
 '(f+n) mod C':r'$(f+n)\bmod C$',
 '(r+1) mod C=f':r'$(r+1)\bmod C=f$',
 '(r−f+C) mod C':r'$(r-f+C)\bmod C$',
 'e+2t+d':r'$e+2t+d$',
 't≤e':r'$t\le e$',
 '3e+d':r'$3e+d$',
 '2|I|':r'$2|I|$',
 'ceil(n/2)':r'$\lceil n/2\rceil$',
 '0≤pushes−pops≤h':r'$0\le p-d\le h$',
 'n²':r'$n^2$',
 'rightExclusive−leftBlocking−1':r'$i-k-1$',
}
p=B/'a_stackqueue-review.en.md';s=p.read_text(encoding='utf-8')
if '$2^{\\lceil' not in s:
 for old,new in replacements.items():s=s.replace(old,new)
 p.write_text(s,encoding='utf-8')
p=B/'a_stackqueue-questions.json';a=json.loads(p.read_text(encoding='utf-8'))
specific={
 'SQ_16':{'1+2+4+8+16+32+64=127':r'$1+2+4+8+16+32+64=127$'},
 'SQ_19':{'64/2-17=15':r'$64/2-17=15$','2*16-32=0':r'$2\cdot16-32=0$','17+0-15=2':r'$17+0-15=2$'},
 'SQ_24':{'actual cost <=3e+d+2k':r'actual cost $T\le3e+d+2k$'},
 'SQ_26':{'25^2=625':r'$25^2=625$'},
 'SQ_34':{'2i<11':r'$2i<11$','ceil(n/2)':r'$\lceil n/2\rceil$'},
 'SQ_39':{'C6=binom(12,6)/7=132':r'$C_6=\binom{12}{6}/7=132$','6!=720':r'$6!=720$','132/720=11/60':r'$132/720=11/60$'},
 'SQ_41':{'C5=sum(j=0..4) Cj*C(4-j)=14+5+4+5+14=42':r'$C_5=\sum_{j=0}^{4}C_jC_{4-j}=14+5+4+5+14=42$','binom(10,5)/6=42':r'$\binom{10}{5}/6=42$'},
 'SQ_42':{'binom(10,4)=210':r'$\binom{10}{4}=210$','binom(10,3)=120':r'$\binom{10}{3}=120$','p>=d':r'$p\ge d$'},
 'SQ_50':{'8-2-b=1':r'$8-2-b=1$'},
 'SQ_62':{'4-2-1=1':r'$4-2-1=1$','4-1-1=2':r'$4-1-1=2$'},
 'SQ_73':{'2*36+1=73':r'$2\cdot36+1=73$'},
}
for q in a:
 for old,new in specific.get(q['id'],{}).items():
  if new not in q['solution']:q['solution']=q['solution'].replace(old,new)
p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
p=B/'a_stackqueue-authentic.json';a=json.loads(p.read_text(encoding='utf-8'))
for q in a:q['visualScope']='Separate concrete teaching example of the source question’s general design or aggregate bound; these values are not claimed as original exam data.'
p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Polished formula-heavy solutions and retrieval rules; clarified all archive model input scopes.')
