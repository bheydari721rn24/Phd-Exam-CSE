from acquire_gauss_sources import fetch,OUT
from pypdf import PdfReader
import re,json,sys
if sys.argv[1]=='follow':
 pending=[('stanford-lu2','lu_factorization49.html'),('stanford-plu','permuted_lu.html')]
 results=[fetch((n,'https://web.stanford.edu/class/math114/decks/linear_systems/'+u)) for n,u in pending]
 for n in ['stanford-ge1','stanford-lu1','stanford-lu2','stanford-plu']:
  print(n,re.findall(r'data-link="(.*?)"',(OUT/(n+'.html')).read_text()))
 print(results)
 with (OUT/'additional-acquisition.json').open('w') as f:json.dump(results,f,indent=2)
 r=PdfReader(OUT/'oxford.pdf');print('\n'.join(str(i+1)+': '+p.extract_text()[:110] for i,p in enumerate(r.pages[13:27],13)))
elif sys.argv[1]=='remaining':
 pending=[('stanford-ge2','gauss_elim29.html'),('stanford-lu3','lu_factorization64.html'),('stanford-plu2','permuted_lu8.html')]
 results=[]
 for n,u in pending:
  results.append(fetch((n,'https://web.stanford.edu/class/math114/decks/linear_systems/'+u)))
  if n.startswith('stanford-plu'):
   for j in range(3,6):
    links=re.findall(r'data-link="(.*?)"',(OUT/(n+'.html')).read_text())
    if not links:break
    n='stanford-plu'+str(j);results.append(fetch((n,'https://web.stanford.edu/class/math114/decks/linear_systems/'+links[-1])))
 (OUT/'remaining-acquisition.json').write_text(json.dumps(results,indent=2))
 print(results)
elif sys.argv[1]=='pages':
 r=PdfReader(OUT/(sys.argv[2]+'.pdf'));print('\n\n'.join('PDF PAGE '+str(i+1)+'\n'+r.pages[i].extract_text() for i in range(int(sys.argv[3])-1,int(sys.argv[4]))))
elif sys.argv[1]=='text':
 for n in sys.argv[2:]:print('\nSOURCE '+n+'\n'+(OUT/(n+'.txt')).read_text())
