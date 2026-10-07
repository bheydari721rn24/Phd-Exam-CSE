from acquire_l_det import CACHE,E,get
import requests,re,json,fitz
extra=[('cambridge','https://www.damtp.cam.ac.uk/user/sjc1/teaching/VandM/notes.pdf')]
for name,num in [('mit-cofactors','6'),('mit-cramer','7')]:
 url='https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/resources/mit18_06scf11_ses2-'+num+'sum/'
 h=requests.get(url,timeout=45).text
 pdfs=re.findall(r'href="([^"<>]+\.pdf)"',h)
 pdf=next(p for p in pdfs if 'sum.pdf' in p)
 extra.append((name,requests.compat.urljoin(url,pdf)))
records=json.loads((E/'acquisition.json').read_text())
records.extend(get(p)for p in extra)
(E/'acquisition.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records[-3:],indent=2))
doc=fitz.open(CACHE/'oxford.pdf')
for i in range(13,21):print('\nOXFORD PDF PAGE',i+1,'\n',doc[i].get_text())
for name in ['mit-cofactors','mit-cramer']:
 print('\nSOURCE',name,'\n',(CACHE/(name+'.txt')).read_text(encoding='utf-8'))
doc=fitz.open(CACHE/'cambridge.pdf')
for i,p in enumerate(doc):
 text=p.get_text()
 if 'determinant' in text.lower():print('CAMBRIDGE MATCH PAGE',i+1,text[:500])
