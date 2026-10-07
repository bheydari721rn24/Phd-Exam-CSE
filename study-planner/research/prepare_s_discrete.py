from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];B=R/'research'
for name in ['s_discrete.en.md','s_discrete-problems.en.txt','s_discrete-review.en.md']:
 p=B/name;s=p.read_text(encoding='utf-8');parts=re.split(r'(\$\$[\s\S]*?\$\$|\$[^$\n]+\$|https?://[^\s)]+|```[\s\S]*?```)',s)
 for i in range(0,len(parts),2):
  parts[i]=re.sub(r'(?<=\d)(?=[A-Za-z])',' ',parts[i]);parts[i]=re.sub(r'(?<=[A-Za-z])(?=\d)',' ',parts[i]);parts[i]=re.sub(r'(?<=[,;:])(?=[A-Za-z])',' ',parts[i])
  if i+1<len(parts) and parts[i+1].startswith('$') and parts[i] and parts[i][-1].isalnum():parts[i]+=' '
  if i and parts[i-1].startswith('$') and parts[i] and parts[i][0].isalnum():parts[i]=' '+parts[i]
 p.write_text(''.join(parts),encoding='utf-8')
qs=[]
for block in (B/'s_discrete-problems.en.txt').read_text(encoding='utf-8').split('@@ ')[1:]:
 header,body=block.split('\n',1);parts=header.split('|');stem,sol=body.split('---SOLUTION---',1);q=dict(id='s-discrete-original-'+parts[0],title=parts[1],origin=parts[2],stem=stem.strip(),solution=sol.strip())
 if len(parts)>3:q['modelId']=parts[3]
 if parts[0]=='50':q['additionalModelIds']=['bin-four-half']
 qs.append(q)
assert len(qs)==80
(B/'s_discrete-questions.json').write_text(json.dumps(qs,indent=2)+'\n')
source=json.loads((B/'exam-calibration/actual-items.json').read_text());auth=[]
for id in ['MS_CE_1405_Q35','Phd_CS_1404_Q68','Phd_CS_1404_Q69']:
 q=next(q for q in source if q['id']==id).copy();q['booklet']=q['booklet'].replace('_',' ');q['pdfSha256']=q['sourceSha256'];q['answerStatus']='independently_derived_not_official';q['verification']='Original PDF page visually rechecked in this chapter turn; printed option order preserved.'
 q['modelId']={'MS_CE_1405_Q35':'bin-four-quarter','Phd_CS_1404_Q68':'bin-three-third','Phd_CS_1404_Q69':'family-conditioning'}[id]
 if id=='Phd_CS_1404_Q68':q['verification']+=' The attached n=3 diagram is explicitly a worked specialization of the symbolic n>=2 problem, not its full proof.'
 auth.append(q)
(B/'s_discrete-authentic.json').write_text(json.dumps(auth,indent=2)+'\n')
css=(R/'dist/chapters/s_descriptive.css').read_text().replace('stat-','disc-').replace('#stat','#disc')
css+='\n.disc-stage svg text{font-family:"Source Sans 3",sans-serif!important;font-size:17px}.disc-stage svg .disc-math{font-family:"STIX Two Math",serif!important}.disc-model{margin:1.5rem 0}.disc-stage{padding:1rem 0}.lab form label{min-width:180px}\n'
(R/'dist/chapters/s_discrete.css').write_text(css)
print('80 complete problem records, 3 original-PDF-checked adaptations, and chapter styles prepared.')
