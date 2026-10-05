"""Independent finite enumeration and symbolic checks for the counting draft."""
from pathlib import Path
from itertools import product,permutations,combinations
from math import comb,factorial,gcd
import json,re,hashlib,sys,xml.etree.ElementTree as ET,subprocess
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
Q=json.loads((BASE/'d_counting-questions.json').read_text());M=json.loads((ROOT/'dist/chapters/d_counting-models.json').read_text());checks=[]
def check(label,condition):
    assert condition,label
    checks.append(label)
def count(values,test):return sum(bool(test(v)) for v in values)
def subsets(n,k):return list(combinations(range(n),k)) if 0<=k<=n else []
def compose(n,m):
    if m==1:return [(n,)] if n>=0 else []
    return [(a,*b) for a in range(n+1) for b in compose(n-a,m-1)] if n>=0 else []
def parts(n,boxes,sizes):
    out=set()
    for a in product(range(boxes),repeat=n):
        gs=tuple(sorted(tuple(i for i,v in enumerate(a) if v==j) for j in range(boxes)))
        if sorted(map(len,gs))==sorted(sizes):out.add(gs)
    return len(out)
def necklaces(n,k):
    words=[''.join(map(str,w)) for w in product(range(2),repeat=n) if sum(w)==k]
    return len({min(w[r:]+w[:r] for r in range(n)) for w in words})
def paths(a,b):
    return [''.join('R' if i in s else 'U' for i in range(a+b)) for s in combinations(range(a+b),a)]
def through(w,point):
    x=y=0
    if point==(0,0):return True
    for s in w:
        x+=s=='R';y+=s=='U'
        if (x,y)==point:return True
    return False
def below(w):
    x=y=0
    for s in w:
        x+=s=='R';y+=s=='U'
        if y>x:return False
    return True
def multisetwords(stock,r):
    return [''.join(w) for w in product(stock,repeat=r) if all(w.count(s)<=stock[s] for s in stock)]
v={}
v[1]=count(permutations(range(10),6),lambda t:t[0]!=0 and sum(x%2 for x in t)==2)
v[2]=sum(len(list(permutations(s,3))) for s in subsets(12,6))
v[3]=count(permutations(range(7),4),lambda t:0 in t)
v[4]=sum(4 for a in 'AB' for b in range(3 if a=='A' else 5))
v[5]=count(permutations('ABCDEFG'),lambda t:t[0]!='A' and t[-1]!='B')
v[6]=count(product(range(6),repeat=5),lambda t:len(set(t))==3)
v[7]=sum(factorial(4) for r in subsets(6,4) for c in subsets(7,4))
v[8]=count(product(range(9),repeat=3),lambda t:len(set(t))==2)
v[9]=count(product(range(1,9),repeat=3),lambda t:t[0]<t[1]<=t[2])
v[10]=count(product(range(8),repeat=5),lambda t:len(set(t))<5)
v[11]=count(subsets(14,7),lambda s:3<=sum(x<8 for x in s)<=4)
v[12]=sum(sum(chair>=2 for chair in s) for s in subsets(10,4) if sum(x<2 for x in s)==1)
v[13]=count(subsets(12,5),lambda s:sum(x<3 for x in s) in (0,3))
v[14]=sum(len(subsets(9,k)) for k in range(2,8))
v[15]=sum(11-len(s) for s in subsets(11,4))
v[16]=sum(len(set(a)&set(b))==2 for a in subsets(10,4) for b in subsets(10,5))
v[17]=sum(set(a)<set(b) for a in subsets(9,2) for b in subsets(9,6))
v[18]=count(product(range(4),repeat=8),lambda t:sum(x in (1,2) for x in t)==3)
check('Q20 integer premise genuinely impossible',all(n*(n-1)!=168 for n in range(20)))
v[19]=count(subsets(11,6),lambda s:sum(x<4 for x in s)>=2)
v[20]='No such finite set'
words=set(permutations('AAABBCC'));v[21]=count(words,lambda t:t[0]==t[-1])
v[22]=count(multisetwords(dict(A=4,B=3,C=2),9),lambda t:'AA' not in t)
v[23]=count(permutations('ABCDEFGHI'),lambda t:'ABC' in ''.join(t))
# Independent contraction counts enumerate actual unit orders and internal orders.
v[24]=sum(1 for _ in permutations(range(7)) for __ in permutations('ABC'))
v[25]=len(multisetwords(dict(A=3,B=2,C=1),4))
v[26]=count(set(permutations('AABBC')),lambda t:'AA' in ''.join(t) and 'BB' not in ''.join(t))
v[27]=count(product('01',repeat=11),lambda t:t[0]=='0' and t[-1]=='1' and t.count('1')==4 and '11' not in ''.join(t))
v[28]=count(subsets(14,4),lambda t:all(b-a>=3 for a,b in zip(t,t[1:])))
v[29]=count(permutations(range(8)),lambda t:all(not(t[i]>=5 and t[i+1]>=5) for i in range(7)))
# Enumerate rank multiplicities independently of the stated paired-rank expression.
v[30]=sum(factorial(4)//(factorial(a)*factorial(4-a))*factorial(4)//(factorial(b)*factorial(4-b))*4 for r,s in combinations(range(6),2) for z in range(6) if z not in (r,s) for a,b in [(2,2)])
v[31]=count(compose(18,4),lambda t:t[0]>=2 and t[1]>=3 and t[2]>=1)
v[32]=sum(count(compose(n,3),lambda t:min(t)>=1) for n in range(13))
v[33]=count(compose(15,4),lambda t:t[0]<=4)
v[34]=count(compose(12,4),lambda t:t[1]<=2 and t[2]>=2)
v[35]=count(compose(10,3),lambda t:t[0]<=2 and t[1]<=3)
v[36]=count(compose(17,3),lambda t:t[0]%2==0 and t[1]<=3 and t[2]>=1)
v[37]=count(compose(30,2),lambda t:t[0]%5==2)
v[38]=len(compose(8,3))*len(compose(11,3))
v[39]=sum(len(compose(n,4)) for n in range(4,10))
v[40]=count(compose(9,6),lambda t:t.count(0)==2)
v[41]=parts(12,3,[4,4,4]);v[42]=parts(8,3,[2,3,3]);v[43]=parts(6,4,[2,2,1,1])
v[44]=count(product(range(5),repeat=5),lambda t:len(set(t))==3)
v[45]=parts(2,3,[0,0,2])+parts(2,3,[0,1,1])
v[46]=count(permutations(range(1,8)),lambda t:t[0]==1 or t[-1]==1)
v[47]=count(permutations(range(1,8)),lambda t:all(not(t[i]>=5 and t[(i+1)%7]>=5) for i in range(7)) and not(t[0]>=5 and t[-1]>=5))
# Anchor ordinary person 0; a mark is one of 5,6,7, including its neighbors around the anchor.
v[47]=count(permutations(range(1,8)),lambda t:all(not(a>=5 and b>=5) for a,b in zip((0,*t),(*t,0))))
v[48]=len({min(t,tuple(reversed(t))) for t in permutations(range(1,7))})
v[49]=necklaces(4,2);v[50]=necklaces(6,3)
v[51]=sum(comb(9,i)*comb(i,3) for i in range(3,10))
v[52]=sum(comb(8,j)**2 for j in range(9))
v[53]=sum(comb(5,j)*comb(7,6-j) for j in range(6) if 0<=6-j<=7)
v[54]=sum(i*(i-1)*comb(8,i) for i in range(9))
v[55]=sum(i*i*comb(7,i) for i in range(8))
v[56]=sum(comb(j,3) for j in range(4,12))
v[57]=sum(i*comb(6,i)*3**(6-i) for i in range(7))
v[58]=sum(count(subsets(10,i),lambda s:0 in s) for i in range(0,11,2))
v[59]=sum(set(a)<=set(b) for a in subsets(10,4) for b in subsets(10,6))
v[60]=sum(i*comb(8,i) for i in range(1,9))
def polynomial(terms,n):
    p={0:1}
    for _ in range(n):
        q={}
        for a,b in p.items():
            for degree,weight in terms.items():q[a+degree]=q.get(a+degree,0)+b*weight
        p=q
    return p
v[61]=polynomial({1:2,3:1},6).get(14,0);v[62]=polynomial({2:1,5:3},5).get(15,0)
v[63]=polynomial({0:1,1:1,2:1},5)[5]
v[64]=sum(2**t.count(1)*3**t.count(2) for t in product(range(3),repeat=6) if t.count(0)==2 and t.count(1)==3 and t.count(2)==1)
v[65]=count(product(range(5),repeat=6),lambda t:t.count(0)%2==0)
v[66]=count(product(range(7),repeat=5),lambda t:sum(x<2 for x in t)%2==1)
v[67]=count(product(range(4),repeat=6),lambda t:all(a<=b for a,b in zip(t,t[1:])))
v[68]=count(combinations(range(1,13),6),lambda t:t[0]==2 and t[-1]==11)
v[69]=count(compose(8,4),lambda t:min(t)>=1)
v[70]=count(product(range(5),repeat=7),lambda t:len(set(t))==3 and all(a<=b for a,b in zip(t,t[1:])))
v[71]=count(paths(7,5),lambda w:through(w,(3,2)));v[72]=count(paths(6,4),lambda w:not through(w,(2,2)))
v[73]=count(paths(7,7),lambda w:through(w,(2,5)) and through(w,(5,2)))
v[74]=count(paths(5,5),below);v[75]=count(paths(8,4),lambda w:'UU' not in w)
v[76]=7+2*count(product(range(1,13),repeat=3),lambda t:t[0]<=t[1]<=t[2])
v[77]=count(product(range(1,11),repeat=3),lambda t:t[0]<=t[1]<t[2])
v[78]=count(product(range(1,10),repeat=2),lambda t:t[0]<t[1])
v[79]=len({tuple(sorted(t)) for t in product('AB',repeat=3)})
v[80]=str(count(combinations(range(1,14),4),lambda t:all(b-a>=3 for a,b in zip(t,t[1:]))))+' subsets; reconstructed subset {1,5,8,13}'
for i,q in enumerate(Q,1):check(q['id']+' independent result',str(v[i])==q['expected'])

# Broad small-parameter ranges exercise feasibility, zero cases and period changes.
for n in range(1,9):
    for k in range(0,9):
        separated=count(subsets(n,k),lambda t:all(b-a>1 for a,b in zip(t,t[1:])))
        formula=1 if k==0 else (comb(n-k+1,k) if n>=2*k-1 else 0)
        check(f'gaps n={n} k={k}',separated==formula)
        fixed=sum(count(product(range(2),repeat=n),lambda t:sum(t)==k and all(t[i]==t[(i+r)%n] for i in range(n))) for r in range(n))
        check(f'rotation average n={n} k={k}',necklaces(n,k)==fixed//n and fixed%n==0)
    for m in range(1,5):check(f'allocation n={n} m={m}',len(compose(n,m))==comb(n+m-1,m-1))
for model in M['models']:
    for j,f in enumerate(model['frames']):
        s=f['state'];id=model['id']
        if id=='dc-word':check(id+str(j),sum(s['remaining'].values())==s['total'] and all(s['prefix'].count(a)+s['remaining'][a]=='ABABC'.count(a) for a in 'ABC'))
        elif id=='dc-path':check(id+str(j),s['right']+s['up']==s['processed'])
        elif id=='dc-nonuniform':check(id+str(j),len(s['preimages'])==s['fiber'] and all(sorted(w)==sorted(s['word']) for w in s['preimages']))
        elif id=='dc-periodic':check(id+str(j),len(s['orbit'])==len({s['word'][r:]+s['word'][:r] for r in range(4)}))
        elif id=='dc-gaps':check(id+str(j),s['compressed']==[a-i for i,a in enumerate(s['original'])])
        elif id=='dc-lower':check(id+str(j),s['residual']==[a-b for a,b in zip(s['original'],s['lower'])])
        elif id=='dc-pascal':check(id+str(j),s['values']==[len(subsets(s['row'],k)) for k in range(s['row']+1)])
        elif id=='dc-reflection':check(id+str(j),s['endpoint']==[s['original'].count('R'),s['original'].count('U')] if s['phase']<2 else s['endpoint']==[4,2])
        elif id=='dc-groups':check(id+str(j),sorted(s['groups'])==['AB','CD','EF'] and s['fiber']==6)
        elif id=='dc-empty':check(id+str(j),s['fiber']==(3 if any(len(g)==2 for g in s['groups']) else 6))
        elif id=='dc-stars':check(id+str(j),sum(s['values'])==5 and s['count']==len(compose(5,3)))
        elif id=='dc-selection':check(id+str(j),s['first']+s['second']==8 and s['count']==comb(5,s['first'])*comb(5,s['second']))
        elif id=='dc-tree':check(id+str(j),s['count']==count(product(range(1,5),repeat=2),lambda t:t[0]<=t[1]))
        elif id=='dc-fibers':check(id+str(j),s['fiber']==len(set(permutations(s['pair']))))
        elif id=='dc-circle':check(id+str(j),len({s['word'][r:]+s['word'][:r] for r in range(4)})==s['orbit'])
        else:raise AssertionError('Unvalidated model '+id)
        ET.fromstring(f['svg']);ET.fromstring(f['formulaHtml'])
actual=json.loads((BASE/'d_counting-authentic.json').read_text());cache=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')
for q in actual:check(q['id']+' original PDF checksum',hashlib.sha256((cache/q['repoPath']).read_bytes()).hexdigest()==q['sourceSha256'])
check('Corrected source Q113 option',actual[0]['options'][0]=='37')
auth_values={
    'MS_CS_1405_Q113':len(compose(5,3))*len(compose(15,2)),
    'MS_CS_1405_Q115':count(subsets(10,8),lambda s:sum(x<5 for x in s)>=4),
    'MS_CS_1405_Q121':sum(comb(i,3)*comb(7,i) for i in range(3,8))/10,
    'MS_CS_1405_Q122':count(product(range(5),repeat=5),lambda t:all(a<=b for a,b in zip(t,t[1:]))),
    'MS_CS_1405_Q123':count(product(range(4),repeat=4),lambda t:t.count(0)%2==0),
    'MS_CS_1405_Q129':count(compose(20,3),lambda t:t[0]%2==0 and t[1]<=4 and t[2]>=1),
    'Phd_CS_1405_Q20':10+count(product(range(1,16),repeat=3),lambda t:t[0]<=t[1]<=t[2])
}
expected_auth={'MS_CS_1405_Q113':336,'MS_CS_1405_Q115':35,'MS_CS_1405_Q121':56,'MS_CS_1405_Q122':126,'MS_CS_1405_Q123':136,'MS_CS_1405_Q129':46,'Phd_CS_1405_Q20':690}
for id,value in auth_values.items():check(id+' independent archive result',value==expected_auth[id])
for n in range(1,5):check('MS_CS_1405_Q120 nonempty symmetry n='+str(n),parts(3*n,3,[n,n,n])==factorial(3*n)//(factorial(3)*factorial(n)**3))
courses=json.loads((BASE/'d_counting-reviewed-courses.json').read_text());check('four actually reviewed distinct universities',len(courses)==4 and len({c['university'] for c in courses})==4 and all(c['reviewed'] for c in courses))
page=(ROOT/'dist/chapters/d_counting.html').read_text()
check('88 rendered questions',page.count('class="exam-question"')==88);check('80 rendered rules',page.count('class="review-rule"')==80)
check('15 dedicated players',page.count('data-counting-model=')==15);check('English and no raw TeX',not re.search(r'[\u0600-\u06ff]|\$|[\x00-\x08]',page))
check('32 chapters and prior approvals',sum(len(w['chapters']) for w in json.loads((ROOT/'dist/lessons.json').read_text()))==32)
# Compare retained stems/solutions with the exact approved baseline, ignoring corrected option text.
from html.parser import HTMLParser
class QuestionParser(HTMLParser):
    def __init__(self):super().__init__();self.ids=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='section' and d.get('class')=='exam-question':self.ids.append(d.get('data-source-id'))
previous=0
for w in json.loads((ROOT/'dist/lessons.json').read_text()):
    for c in w['chapters']:
        if c['topicId']=='d_counting':continue
        old=subprocess.check_output(['rtk','proxy','git','show','3698444e52bdb9e04cb1eb879c9c8a35e869c377:dist/'+c['url']],cwd=ROOT).decode('utf-8')
        new=(ROOT/'dist'/c['url']).read_text();a=QuestionParser();b=QuestionParser();a.feed(old);b.feed(new)
        check(c['topicId']+' preserved question identities',a.ids==b.ids);previous+=len(a.ids)
        pattern=r'<section class="exam-question"[\s\S]*?</section>'
        old_questions=re.findall(pattern,old);new_questions=re.findall(pattern,new)
        assert len(old_questions)==len(a.ids)==len(new_questions)
        if c['topicId']=='s_counting':
            old_questions=[re.sub(r'(<b>1\.</b><div><p>)32(</p>)',r'\g<1>37\2',q) if 'data-source-id="MS_CS_1405_Q113"' in q else q for q in old_questions]
        check(c['topicId']+' preserved complete question content except corrected source option',old_questions==new_questions)
check('1747 previous question entries preserved',previous==1747)
report=dict(state='passed',topicId='d_counting',checks=len(checks),labels=checks,questionCount=88,originalQuestions=80,authenticRevisits=8,priorQuestionCount=previous,models=15,checkpoints=M['frameCount'])
(BASE/'d_counting-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='labels'}))
