from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
p=R/'dist/chapters/g_arithmetic.js';s=p.read_text(encoding='utf-8').replace("'division','nand']","'division','booth','nand']").replace("frame.formulaHtml=mathText('Exact integer state: '+JSON.stringify(m.result))","frame.formulaHtml=mathText(frame.caption)").replace("[833,238]","[833,233]")
p.write_text(s,encoding='utf-8')
p=B/'g_arithmetic.en.md';s=p.read_text(encoding='utf-8').replace('At position $i$, pair `01`','At position $i$, the ordered pair $(b_i,b_{i-1})$ `01`').replace('## 23. Binary division','<!-- SIM: booth -->\n\n## 23. Binary division');p.write_text(s,encoding='utf-8')
p=B/'prepare_g_arithmetic.py';s=p.read_text(encoding='utf-8').replace("specs=[('full-basic'","specs=[('booth-signed','Signed Booth rows: negative three times negative two',dict(operation='booth',n=4,a=13,b=14,c=0,z=0),'booth'),('booth-minimum','Booth at the minimum negative boundary',dict(operation='booth',n=4,a=8,b=15,c=0,z=0),'booth'),('full-basic'").replace("53:'booth-signed'", "53:'booth-signed'").replace("56:'divide-45'","51:'booth-signed',52:'booth-minimum',53:'booth-signed',54:'booth-signed',56:'divide-45'")
# Reuse diagrams only where their sample assumptions actually match or qualify the problem.
s=s.replace("qs.append(dict(id=", "qs.append(dict(id=")
p.write_text(s,encoding='utf-8')
p=B/'render_g_arithmetic.py';s=p.read_text(encoding='utf-8').replace("'division','nand']","'division','booth','nand']").replace('13 circuit/process models','15 circuit/process models').replace('animationCount=13,animationWalkthroughCount=13','animationCount=15,animationWalkthroughCount=15').replace('13 stored circuit/process models','15 stored circuit/process models');p.write_text(s,encoding='utf-8')
print('Updated the signed arithmetic model and its explicit pair convention.')
