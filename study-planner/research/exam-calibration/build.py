"""Idempotent overlay after the legacy 22-chapter builder; source files stay immutable."""
import sys,re,json,html,hashlib
from pathlib import Path
from urllib.parse import quote
from markdown_it import MarkdownIt
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
from figures import nand,mux
sys.path.insert(0,str(ROOT/'research/exam-rewrite'))
from mathml import markdown_math,render,width
sys.path.insert(0,str(ROOT/'research'))
from math_typography import normalize_math,normalize_scripts
import mathml
import xml.etree.ElementTree as ET
md=MarkdownIt('commonmark',{'html':True}).enable('table')
actual=json.loads((BASE/'actual-items.json').read_text())
original=[q for f in sorted(BASE.glob('original-*.json')) for q in json.loads(f.read_text())]
archive=json.loads((BASE/'archive-manifest.json').read_text())
oldmanifest=json.loads((ROOT/'research/exam-rewrite/manifest.json').read_text())
tripling=json.loads((BASE/'tripling-baseline.json').read_text()) if (BASE/'tripling-baseline.json').exists() else None
manifest=dict(date='2026-10-03',state='revision_draft',archiveCommit=archive['commit'],inventoryFiles=len(archive['files']),authenticUniqueItems=sum(q['answer'] is not None for q in actual),excludedSourceRecords=sum(q['answer'] is None for q in actual),newOriginalItems=len(original),retainedOriginalChallenges=44,answerPolicy='Independent derivations; no claim of official-key verification.',coveragePolicy='Purposeful question-level sample. Inventory is not a claim that all 84 PDFs or all years have been read.',chapters=[])

def e(s):return html.escape(str(s))
def compact_display(value):
 root=ET.fromstring(value);children=list(root)
 if width(root)<=10.5:return value
 rows=[];current=[];size=0;paren=0
 for child in children:
  legal=child.tag=='mo' and (child.text or '') in ('+','-','−','=','∨','∧','⊕','⇒','⇔','∪','∩')
  legal=legal or (child.tag=='mo' and child.text==',' and paren==0)
  if current and legal and size>5.5:
   rows.append(current);current=[];size=0
  current.append(child);size+=width(child)
  if child.tag=='mo' and child.text=='(':paren+=1
  if child.tag=='mo' and child.text==')':paren-=1
 if current:rows.append(current)
 return '<mtable displaystyle="true" columnalign="left" rowspacing=".5em">'+''.join('<mtr><mtd><mrow>'+''.join(ET.tostring(x,encoding='unicode') for x in row)+'</mrow></mtd></mtr>' for row in rows)+'</mtable>' if len(rows)>1 else value
mathml.wrap_display=compact_display
def prep(s):
 s=s.replace("\\'", "'")
 # Long formulas use a block, preserving the entire formula and visible scope.
 s=re.sub(r'(?<!\$)\$([^$\n]+)\$(?!\$)',lambda m:'\n\n$$'+m[1]+'$$\n\n' if width(list(ET.fromstring(render(m[1])))[0])>10.5 else m.group(),s)
 return s
def text(s):return normalize_scripts(normalize_math(markdown_math(prep(s),md)))
def source_link(q):return 'https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+archive['commit']+'/'+quote(q['repoPath'],safe='/')+'#page='+str(q['pdfPage'])
def item(q,n,authentic=False,figure=''):
 title=(('MSc' if q['booklet'].startswith('MS_') else 'PhD')+' '+q['booklet'].split('_')[1]+' '+q['booklet'].split('_')[2]+', Q'+str(q['questionNumber'])+' — ' if authentic else '')+q['title']
 meta='Authentic examination · English translation' if authentic else 'Original examination analogue · author-assessed '+q['difficulty'].lower()+' difficulty'
 provenance=('<p class="exam-provenance"><a href="'+e(source_link(q))+'" target="_blank" rel="noopener">Original booklet · PDF page '+str(q['pdfPage'])+' · question '+str(q['questionNumber'])+'</a>. '+e(q['answerProvenance'])+'.</p>') if authentic else '<p class="exam-provenance">Pattern reference: '+e(q['pattern'])+'. This is an original problem, not a question from those booklets.</p>'
 options=''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+text(o)+'</div></div>' for i,o in enumerate(q['options'],1))
 return '<section class="exam-question" data-kind="'+('authentic' if authentic else 'original')+'" data-answer="'+str(q['answer'])+'" data-source-id="'+e(q.get('id',''))+'"><h3>Question '+str(n)+'. '+e(title)+'</h3><p class="exam-label">'+e(meta)+'</p>'+provenance+text(q['stem'])+figure+'<div class="exam-options">'+options+'</div><details class="exam-solution"><summary>Read the complete solution and option analysis</summary><p><strong>Correct option: '+str(q['answer'])+'.</strong></p>'+text(q['solution'])+'</details></section>'

for c in oldmanifest['chapters']:
 t=c['topicId'];p=ROOT/'dist/chapters'/(t+'.html');s=p.read_text(encoding='utf-8')
 auth=[q for q in actual if t in q['topics'] and q['answer'] is not None]
 new=[q for q in original if q['topic']==t];assert len(new)>=8,(t,len(new))
 legacy=(ROOT/'research/exam-rewrite'/(t+'.md')).read_text(encoding='utf-8')
 chunks=re.findall(r'^### Question \d+\. Challenge: ([\s\S]*?)(?=^### |^## |\Z)',legacy,re.M)
 assert len(chunks)==2,(t,len(chunks))
 count=len(auth)+len(new)+len(chunks)
 target=next(x for x in tripling['chapters'] if x['topicId']==t) if tripling else None
 if target:assert count>=target['minimum'],(t,count,target['minimum'])
 h2=list(re.finditer(r'<h2(?:\s[^>]*)?>[\s\S]*?</h2>',s))
 bank=next(m for m in h2 if re.search(r'Formula and conceptual problem bank',m.group()))
 end=next(m for m in h2 if m.start()>bank.start())
 bankid=re.search(r'id="([^"]+)"',bank.group())[1]
 notesid=re.search(r'id="([^"]+)"',end.group())[1]
 body=bank.group()+'<p>This bank combines authentic Iranian entrance-examination questions, newly authored medium/hard analogues, and two retained multistep challenges. The original four-option numbering is retained for authentic questions. Difficulty labels for original problems are qualitative author judgments, not calibrated response statistics.</p><p class="bank-navigation"><a href="#authentic-questions">Authentic examinations</a> · <a href="#original-analogues">Original analogues</a> · <a href="#integrated-challenges">Integrated challenges</a></p><h3 id="authentic-questions">Authentic examination questions</h3>'
 if t in ('p_types','d_induction','d_invariants','a_model','l_matrices'):
  association={'p_types':'The authentic items below test numeric primitives, precision, and encoding; they do not claim to be C17 type-system questions. The original questions make the language rules explicit.','d_induction':'The original items use induction directly. Some authentic items are applications whose identities or recurrences can be proved by induction, rather than questions explicitly asking for an induction proof.','d_invariants':'The authentic questions below support correctness, index, and structural invariants. They are not all labeled invariant questions in their original subject sections.','a_model':'The authentic items connect the computation model to exact comparisons, expected updates, and structural work. They do not constitute an archive census of bit-complexity questions.','l_matrices':'The coupled integer-equation item is a cross-topic boundary example: real linear-system dimension alone does not count nonnegative integer solutions.'}[t]
  body+='<p class="notice">'+association+'</p>'
 n=0
 for a in auth:
  n+=1
  fig=nand() if a['id']=='Phd_CE_1405_Q23' else mux() if a['id']=='MS_CE_1404_Q80' else ''
  fig=normalize_scripts(normalize_math(fig))
  body+=item(a,n,True,fig)
 body+='<h3 id="original-analogues">Original formula and conceptual analogues</h3>'
 if target:body+='<p>This chapter had '+str(target['before'])+' questions in version 55. Its minimum expansion target is '+str(target['minimum'])+' and it now contains '+str(count)+' questions. Expanded families contain two exact calculation instances, one symbolic-generalization question and one boundary or counterexample question. The family variants are explicitly related, not counted as different university sources.</p>'
 family_index={q['family']:q['title'].split(' — ')[0] for q in new if q.get('family')}
 if family_index:body+='<details class="family-index"><summary>Choose a calculation and concept family</summary><ul>'+''.join('<li><a href="#family-'+e(k)+'">'+e(v)+'</a></li>' for k,v in family_index.items())+'</ul></details>'
 lastfamily=None
 for q in new:
  if q.get('family') and q['family']!=lastfamily:
   lastfamily=q['family'];body+='<h4 class="problem-family" id="family-'+e(q['family'])+'">'+e(q['title'].split(' — ')[0])+'</h4>'
  n+=1;body+=item(q,n)
 body+='<h3 id="integrated-challenges">Integrated multistep challenges</h3>'
 for chunk in chunks:
  n+=1;title,rest=chunk.split('\n',1)
  rest=re.sub(r'^\*\*([ABCD])\.\*\*',lambda m:'**'+str('ABCD'.index(m[1])+1)+'.**',rest,flags=re.M)
  rest=re.sub(r'\*\*Answer: ([ABCD])\.\*\*',lambda m:'**Correct option: '+str('ABCD'.index(m[1])+1)+'.**',rest)
  body+='<section class="exam-question" data-kind="retained-original"><h3>Question '+str(n)+'. '+e(title)+'</h3><p class="exam-label">Original integrated challenge · retained after review</p>'+text(rest)+'</section>'
 s=s[:bank.start()]+body+s[end.start():]
 # The visible counts in the chapter navigation must match this bank.
 s=re.sub(r'(<a href="#'+re.escape(bankid)+r'">)[^<]*(</a>)',r'\g<1>'+str(count)+' explained questions'+r'\2',s)
 s=re.sub(r'(<a href="#'+re.escape(notesid)+r'">)[^<]*(</a>)',r'\g<1>'+str(c['notesCount'])+' examination notes'+r'\2',s)
 s=re.sub(r'(<header class="hero">[\s\S]*?<h1[^>]*>[\s\S]*?</h1>)[\s\S]*?</header>',r'\1<p>Examination revision draft · '+str(len(auth))+' authentic questions · '+str(len(new)+2)+' original problems · '+str(c['notesCount'])+' examination notes · full university instruction retained</p></header>',s,count=1)
 if 'exam-calibration.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="exam-calibration.css"></head>')
 if 'exam-calibration.js' not in s:s=s.replace('</body>','<script src="exam-calibration.js"></script></body>')
 # A separate bibliography preserves the distinction between university teaching and exam provenance.
 s=re.sub(r'<!-- EXAM REFERENCES START -->[\s\S]*?<!-- EXAM REFERENCES END -->','',s)
 bibliography='<!-- EXAM REFERENCES START --><section class="exam-references"><h2 id="exam-references">Examination booklet references</h2><p>The following source questions were translated from the original scanned pages. Solutions are independently derived, not certified official keys. The question-specific PDF links above identify the exact pages.</p><ul>'
 for book in sorted({q['booklet'] for q in auth}):
  items=[q for q in auth if q['booklet']==book]
  bibliography+='<li><a href="'+e(source_link(items[0]))+'">'+e(book.replace('_',' '))+'</a> — questions '+e(', '.join(str(q['questionNumber']) for q in items))+'. Repository revision '+archive['commit'][:12]+'.</li>'
 bibliography+='</ul><p><a href="../exam-source-audit.html">Read the source-ambiguity audit</a> · <a href="../library-review.html">Review all revised banks</a></p></section><!-- EXAM REFERENCES END -->'
 s=s.replace('</article>',bibliography+'</article>',1)
 # Remove the superseded policy from current lessons, retaining historical audits in research.
 s=re.sub(r'[^<>.]*[Ii]ranian[^<>.]*?(?:final month|final-month|final study month)[^<>.]*\.', ' Original Iranian MSc and PhD questions are now included under the student instruction of 3 October 2026.',s)
 p.write_text(s,encoding='utf-8')
 manifest['chapters'].append(dict(topicId=t,title=re.sub('<[^>]+>','',re.search(r'<h1[^>]*>([\s\S]*?)</h1>',s)[1]),authenticQuestions=len(auth),newOriginalQuestions=len(new),retainedChallenges=2,totalQuestions=count,baselineQuestions=target['before'] if target else None,minimumQuestions=target['minimum'] if target else None,expandedFamilies=len({q['family'] for q in new if 'family' in q}),authenticIds=[q['id'] for q in auth],notes=c['notesCount'],figures=sum('<svg' in f for f in re.findall(r'<figure\b[\s\S]*?</figure>',s)),bankId=bankid,notesId=notesid,sourceAudit=c.get('sourceAuditPath'),htmlSha256=hashlib.sha256(p.read_bytes()).hexdigest()))

manifest['authenticChapterOccurrences']=sum(c['authenticQuestions'] for c in manifest['chapters'])
manifest['totalQuestions']=sum(c['totalQuestions'] for c in manifest['chapters'])
manifest['figures']=sum(c['figures'] for c in manifest['chapters'])
manifest['baselineTotalQuestions']=tripling['total'] if tripling else None
manifest['additionalOriginalQuestions']=sum('family' in q for q in original)
manifest['additionalFamilies']=sum(c['expandedFamilies'] for c in manifest['chapters'])
manifest['expansionPolicy']='Every chapter count must be at least three times its frozen version-55 baseline; each added family contains two numerical instances, a symbolic generalization, and a scope question.'
(BASE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
lessons=json.loads((ROOT/'dist/lessons.json').read_text())
for week in lessons:
 for c in week['chapters']:
  audit=next(a for a in manifest['chapters'] if a['topicId']==c['topicId'])
  c.update(status='draft',statusLabel='Expanded examination revision draft',questionCount=audit['totalQuestions'],authenticQuestionCount=audit['authenticQuestions'],originalQuestionCount=audit['newOriginalQuestions']+2,examNotesCount=audit['notes'],revisionState='exam_grounded_draft')
(ROOT/'dist/lessons.json').write_text(json.dumps(lessons,indent=2)+'\n')
print(json.dumps({k:v for k,v in manifest.items() if k!='chapters'},indent=2))
