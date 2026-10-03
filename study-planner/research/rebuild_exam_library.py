"""Authoritative reproducible exam revision: baseline + authored chapter revision.

Correct source-derived proofs remain as tutorials. Rejected old reviews are removed.
Run this AFTER any legacy builder; never ship a legacy builder's output by itself.
"""
import sys,re,json,hashlib,html
from pathlib import Path
from markdown_it import MarkdownIt
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'research/exam-rewrite'
sys.path.insert(0,str(BASE))
from mathml import markdown_math
from math_typography import normalize_math,normalize_scripts
md=MarkdownIt('commonmark',{'html':True}).enable('table')
manifest=json.loads((BASE/'manifest.json').read_text())
figures=json.loads((BASE/'figures.json').read_text()) if (BASE/'figures.json').exists() else {}
def polish(s):
 def prose(m):
  p=m.group()
  if p.startswith(('`','$','<')):return p
  p=re.sub(r'\b([A-Za-z]{3,})(\d+)',lambda q:q.group() if q[1].lower() in ('binary','uint','int','cs','ieee') else q[1]+' '+q[2],p)
  p=re.sub(r'(?<![A-Za-z])(\d+)(ns|bytes|bits|cells)\b',r'\1 \2',p)
  p=re.sub(r'\b(in|of|to|from|one|two|the)([A-Z])\b',r'\1 \2',p)
  p=re.sub(r'\b(\d+)/(\d+)\b',lambda q:'$\\frac{'+q[1]+'}{'+q[2]+'}$',p)
  return p
 parts=re.split(r'(```[\s\S]*?```|`[^`\n]+`|\$\$[\s\S]*?\$\$|\$[^$]+\$|<[^>]*>)',s)
 return ''.join(prose(re.match(r'[\s\S]*',x)) for x in parts)
def plain(s):return re.sub('<[^>]+>','',s)
def convert_logic(s):
 s=re.sub(r'\*\*Options\.\*\* ([\s\S]*?)(?=\n\n)',lambda m:'\n\n'.join('**'+p[0]+'.** '+p[3:].rstrip('.') for p in re.split(r'; (?=[ABCD]:)',m[1])),s)
 s=s.replace('**Correct option:','**Answer:').replace('### Problem ','### Question ')
 return s
def rebuild(c):
 t=c['topicId'];path=BASE/(t+'.md')
 if not path.exists():return False
 s=path.read_text(encoding='utf-8');s=polish(convert_logic(s))
 pieces=re.split(r'^## ',s,flags=re.M)[1:];assert len(pieces)==3,(t,len(pieces))
 qcount=len(re.findall(r'^### Question \d+',pieces[1],re.M));ncount=len(re.findall(r'^### \d+',pieces[2],re.M))
 assert qcount>=10 and ncount>=10,(t,qcount,ncount)
 assert len(re.findall(r'^\*\*Answer: [ABCD]\.\*\*',pieces[1],re.M))==qcount,t
 for letter in 'ABCD':assert len(re.findall(r'^\*\*'+letter+r'\.\*\*',pieces[1],re.M))==qcount,(t,letter)
 original=(BASE/'baseline'/(t+'.html')).read_text(encoding='utf-8')
 assert hashlib.sha256((BASE/'baseline'/(t+'.html')).read_bytes()).hexdigest()==c['baselineSha256']
 h2=list(re.finditer(r'<h2(?:\s[^>]*)?>[\s\S]*?</h2>',original))
 banks=[(i,m) for i,m in enumerate(h2) if re.search(r'worked.*problem|problem bank|explained problem',plain(m.group()),re.I)]
 assert len(banks)==1,(t,[(i,plain(m.group())) for i,m in banks]);i,bank=banks[0];notes=h2[i+1];after=h2[i+2]
 bankid=re.search(r'id="([^"]+)"',bank.group())[1];notesid=re.search(r'id="([^"]+)"',notes.group())[1]
 tutorial=original[bank.end():notes.start()]
 tutorial=re.sub(r'(<h3[^>]*>)(Problem\s+\d+)',r'\1Tutorial \2',tutorial).replace('Tutorial Problem','Tutorial')
 intro='<h2 id="proof-tutorials">Detailed derivation tutorials</h2><p>The following complete proofs and implementations support the new examination problems. They develop the reasoning needed to derive formulas; the separately labeled examination bank below tests calculation, concepts and distractor decisions.</p>'
 rendered=[]
 for p,anchor in zip(pieces,('exam-methods',bankid,notesid)):
  title,body=p.split('\n',1)
  if anchor==bankid:body='These are original questions derived from the chapter concepts, not reproduced Iranian examination items. Solve under the exact domain, encoding and cost assumptions stated in each question.\n\n'+body
  val='<h2 id="'+anchor+'">'+html.escape(title)+'</h2>'+markdown_math(body,md)
  if anchor=='exam-methods' and t in figures:val+=figures[t]
  rendered.append(normalize_scripts(normalize_math(val)))
 replacement=rendered[0]+intro+tutorial+rendered[1]+rendered[2]
 output=original[:bank.start()]+replacement+original[after.start():]
 output=output.replace('Boolean <span class="math-inline">OR/AN</span>D arithmetic','Boolean OR and AND arithmetic')
 output=output.replace('<span class="math-inline">56 / PD</span>F pp.','56; PDF pp.').replace('<span class="math-inline">110 / PD</span>F pp.','110; PDF pp.')
 # Preserve source exercise attribution to the retained tutorials, not new questions.
 reference=re.search(r'<h2[^>]*id="references"[^>]*>',output)
 if reference:
  output=output[:reference.start()]+re.sub(r'\bProblem (\d+)',r'Tutorial \1',output[reference.start():])
 output=re.sub(r'(<header class="hero">[\s\S]*?<h1[^>]*>[\s\S]*?</h1>)[\s\S]*?</header>',r'\1<p>Examination revision draft · '+str(qcount)+' original formula and conceptual questions · '+str(ncount)+' applicable examination notes · deep proofs and source audits retained</p></header>',output,count=1)
 output=output.replace('</nav>','<a href="#exam-methods">Formula-solving methods</a> <a href="#proof-tutorials">Derivation tutorials</a></nav>',1)
 if 'exam-revision.css' not in output:output=output.replace('</head>','<link rel="stylesheet" href="exam-revision.css"></head>',1)
 output=output.replace('Student-approved chapter','Examination revision draft')
 # Remove stale counts in metadata that described the rejected bank.
 output=re.sub(r'(<meta name="description" content=")[^"]*(")',r'\1A detailed university-source chapter with revised formula-solving instruction, original conceptual and numerical examination questions, full solutions and applicable examination notes.\2',output,count=1)
 def unique_svg(m):
  unique_svg.index+=1
  svg=m.group()
  for sid in re.findall(r'\bid="([^"]+)"',svg):
   new=t+'-figure-'+str(unique_svg.index)+'-'+sid
   svg=svg.replace('id="'+sid+'"','id="'+new+'"').replace('url(#'+sid+')','url(#'+new+')')
  return svg
 unique_svg.index=0
 output=re.sub(r'<svg\b[\s\S]*?</svg>',unique_svg,output)
 (ROOT/'dist/chapters'/(t+'.html')).write_text(output,encoding='utf-8')
 c.update(state='rewritten_draft',questionCount=qcount,notesCount=ncount,authoringFile='research/exam-rewrite/'+t+'.md',revisionSha256=hashlib.sha256(s.encode()).hexdigest())
 return True
done=sum(rebuild(c) for c in manifest['chapters'])
manifest['state']='in_progress'
(BASE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
lessons=json.loads((ROOT/'dist/lessons.json').read_text())
for week in lessons:
 for c in week['chapters']:
  c['status']='draft';c['statusLabel']='Examination revision draft'
  c['revisionState']=next(x['state'] for x in manifest['chapters'] if x['topicId']==c['topicId'])
  audit=next(x for x in manifest['chapters'] if x['topicId']==c['topicId'])
  c['questionCount']=audit['questionCount'];c['examNotesCount']=audit['notesCount']
(ROOT/'dist/lessons.json').write_text(json.dumps(lessons,indent=2)+'\n')
print('Rebuilt',done,'of 22 chapters. All existing chapters remain revision drafts.')
