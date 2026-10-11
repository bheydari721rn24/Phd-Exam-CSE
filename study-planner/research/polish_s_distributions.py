"""Fix notation and explicit instructional wording before isolated rendering."""
from pathlib import Path
import json,re
B=Path(__file__).resolve().parent
p=B/'s_distributions-questions.json';qs=json.loads(p.read_text(encoding='utf-8'))
for q in qs:
 q['stem']=q['stem'].replace(r'\mathbin{\mathrm{xor}}',r'\operatorname{xor}')
 if q['title']=='Reject impossible binomial moments':q['stem']+=' Also assess mean $3$ and variance $7/3$.'
p.write_text(json.dumps(qs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for p in [B/'s_distributions.en.md',B/'s_distributions-source-audit.md']:
 s=p.read_text(encoding='utf-8').replace('Cambridge attempted handout:','Mateja Jamnik and Thomas Sauerwald. Cambridge Introduction to Probability, Lecture 4, 2023–24. Read handout:')
 # Course references are prose, not unspaced course codes.
 for a,b in [('MIT18.05','MIT 18.05'),('CS70','CS 70'),('CS109','CS 109'),('Michaelmas2019','Michaelmas 2019'),('Spring2022','Spring 2022'),('Spring2016','Spring 2016'),('Fall2016','Fall 2016'),('Winter2022','Winter 2022'),('Lecture4','Lecture 4'),('Lecture8','Lecture 8'),('Classes4','Classes 4'),('All23','All 23'),('All8','All 8'),('All66','All 66'),('PDFpages','PDF pages'),('PDF18','PDF 18'),('PDF34','PDF 34'),('and39','and 39')]:s=s.replace(a,b)
 p.write_text(s,encoding='utf-8')
print('Polished explicit notation, the moment-rejection stem and readable references.')
