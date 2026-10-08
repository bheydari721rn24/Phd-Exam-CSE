from pathlib import Path
import json,hashlib,re
B=Path(__file__).resolve().parent;E=B/'p_strings-evidence';E.mkdir(exist_ok=True)
p=B/'p_strings-more-problems.en.txt';s=p.read_text(encoding='utf-8')
for a,b in [(r'$p`',r'$p$'),(r'$p+r`',r'$p+r$'),(r'$p+m`',r'$p+m$'),(r'$r\le n`',r'$r\le n$'),(r'$1/q`',r'$1/q$'),(r'$n`',r'$n$'),(r'$n+1`',r'$n+1$'),(r'$(n+1)/2`',r'$(n+1)/2$'),(r'$m=n`',r'$m=n$'),(r'$0\le i\le n-m`',r'$0\le i\le n-m$'),(r'$0\le j<m`',r'$0\le j<m$'),(r'$i+j\le n-m+m-1=n-1`',r'$i+j\le n-m+m-1=n-1$'),(r'$m`',r'$m$'),(r'$\lfloor\log_2 n\rfloor`',r'$\lfloor\log_2 n\rfloor$'),(r'$n\ge1`',r'$n\ge1$')]:s=s.replace(a,b)
p.write_text(s,encoding='utf-8')
p=B/'p_strings.en.md';s=p.read_text(encoding='utf-8').replace(" (Robert B. Washburn's course identifier; individual slide authorship is not independently established)"," (individual slide authorship is not independently established)");p.write_text(s,encoding='utf-8')
qs=[];rules=[]
for fn in ['p_strings-problems.en.txt','p_strings-more-problems.en.txt']:
 for block in (B/fn).read_text(encoding='utf-8').split('@@ ')[1:]:
  header,body=block.split('\n',1);a=header.split('|');stem,tail=body.split('---SOLUTION---');sol,rule=tail.split('---RULE---');n=int(a[0]);q=dict(id='p-strings-original-'+str(n),title=a[1],origin=a[2],stem=stem.strip(),solution=sol.strip())
  if len(a)>3:q['modelId']=a[3].strip()
  qs.append(q);rules.append(str(n)+'. **'+a[1]+'.** '+rule.strip())
assert len(qs)==80 and [q['id']for q in qs]==['p-strings-original-'+str(n)for n in range(1,81)]
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
save(B/'p_strings-questions.json',qs);(B/'p_strings-review.en.md').write_text('\n\n'.join(rules)+'\n',encoding='utf-8')
q=next(x for x in json.loads((B/'d_counting-authentic.json').read_text())if x['id']=='MS_CS_1405_Q123')
root=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source');assert hashlib.sha256((root/q['repoPath']).read_bytes()).hexdigest()==q['sourceSha256']
q['solution']=q['solution'].replace(r'\\',chr(92));q['stem']=q['stem'].replace(r'\\',chr(92));q['options']=[x.replace(r'\\',chr(92))for x in q['options']]
q['title']='Abstract string parity: authentic counting bridge revisit';q['origin']='Authentic MSc CS 1405 Q123, bridge revisit';q['verification']='Original PDF page 26 visually rechecked on 8 October 2026. Options retained in printed order. Previously included in the counting chapter; not claimed as a new unique archive question.'
q['solution']+='\n\n**Representation distinction.** The symbol 0 here is an abstract alphabet symbol (or the printable digit byte), not a C null character terminating a buffer. The question does not test C library behavior. Four-symbol strings of length four require five bytes if encoded as four nonzero character bytes plus the C terminator.'
save(B/'p_strings-authentic.json',[q]);save(E/'question-visual-decisions.json',[dict(questionId=q['id'],modelId=q.get('modelId'),decision='Exact parameter-matched memory or algorithm trace.' if q.get('modelId')else 'Full algebra, code reasoning or proof; no unrelated generic illustration.')for q in qs+[q]])
save(E/'reading.json',dict(reviewDate='2026-10-08',records=[dict(university='Harvard',course='CS50x 2025',instructor='David J. Malan',material='Notes 2: lines 343–821; Notes 4: string/pointer/comparison/copying sections, lines 271–684',role='core'),dict(university='Cambridge',course='Programming in C 2017–18',instructor='Neel Krishnaswami',material='Complete extracted text of Lectures 2 (19 slides) and 3 (25 slides)',role='core'),dict(university='MIT',course='6.087 January IAP 2010',instructor='Daniel Weller and Sharat Chikkerur',material='Lecture 5, relevant PDF pages 5 and 16–26, read as extracted text',role='core'),dict(university='Princeton',course='COS 217 Fall 2026',instructor='Individual slide author not independently established',material='Complete extracted text of 32-page Pointers, Arrays, and Strings slides',role='core'),dict(university='Stanford',course='CS107',material='Complete accessible C reference sheet',role='supplementary'),dict(university='WG14 (not a university)',course='N1570',material='Sections 7.24.1–7.24.6 relevant extracted text',role='primary contract reference')],qualification='Finite accessible candidate pool; not all courses worldwide. Original teaching and independently reconstructed problems, not wholesale external exercise copying.'))
print('Prepared 80 full solutions and rules, plus one original-PDF-rechecked abstract-string bridge.')
