"""Use explicit density coordinates and annotate the selected boxplot median."""
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/s_descriptive.js';s=p.read_text(encoding='utf-8')
old="+axis([edges[0],edges.at(-1)],330,'Measured value')"
new="+line(90,330,910,330)+text(500,387,'Measured value','label','middle')+edges.map(v=>line(x(v),330,x(v),336)+text(x(v),358,fmt(v),'math','middle')).join('')+line(90,100,90,330)+[0,.25,.5,.75,1].map(f=>text(74,335-f*230,fmt(f*maxHeight),'math','end')).join('')+text(32,60,'Density')"
s=s.replace(old,new)
s=s.replace("text(40,30,'Type 7; strict 1.5-IQR outlier rule')","text(40,30,'Type 7; strict 1.5-IQR rule; median '+fmt(med))")
s=s.replace('y=z=>320-200*z/maxLoss','y=z=>320-240*z/maxLoss')
s=s.replace("+axis(r,320,'Candidate center c')+", "+axis(r,320,'Candidate center c')+vertical([0,maxLoss],'Total loss')+")
p.write_text(s,encoding='utf-8')
