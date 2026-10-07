from pathlib import Path
import re
B=Path(__file__).resolve().parent
p=B/'s_discrete-problems.en.txt';s=p.read_text(encoding='utf-8')
ids={22:'affine-three',25:'cyclic-five',26:'indicator-five',31:'bin-five-threequarter',35:'bin-four-quarter',38:'bin-six-half',42:'hyper-batch',44:'hyper-observed',50:'hyper-half',61:'nb-third',62:'nb-second',66:'poisson-six',70:'poisson-limit',71:'count-cap',72:'count-distance',75:'quadratic-six',78:'max-four'}
for n,id in ids.items():
 s=re.sub(r'^(@@ '+str(n)+r'\|[^\n]+)$',lambda m:m[0]+'|'+id if m[0].count('|')==2 else m[0],s,flags=re.M)
s=s.replace('patternSSF','pattern SSF').replace('andFSS','and FSS').replace('“Random selection”alone','“Random selection” alone')
p.write_text(s,encoding='utf-8')
p=B.parent/'dist/chapters/s_discrete.js';s=p.read_text(encoding='utf-8').replace('Each path: p^r (1−p)^(t−r); mass','Each path has r successes and t−r failures; mass');p.write_text(s,encoding='utf-8')
print('Aligned convolution inputs and added exact diagrams to 17 further problems.')
