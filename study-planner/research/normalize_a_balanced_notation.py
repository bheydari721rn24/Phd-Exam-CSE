"""Convert authored plaintext subscripts/powers to explicit LaTeX, excluding code and existing math."""
from pathlib import Path
import re
B=Path(__file__).resolve().parent
atom=re.compile(r'(?<![A-Za-z_/])([A-Za-z]+|[0-9]+)([_^])(\([^()\n]{1,30}\)|−?[0-9]+|[A-Za-z](?:[0-9]+)?)(?![\w])')
def convert(m):
 a,op,b=m.groups();b=b[1:-1]if b.startswith('(')else b
 a='\\'+a if a in ['phi','psi','beta']else a
 return '$'+a+op+'{'+b.replace('−','-')+'}$'
for name in ['a_balanced.en.md','a_balanced-problems.en.md','a_balanced-problems-2.en.md','a_balanced-problems-3.en.md','a_balanced-review.en.md']:
 p=B/name;s=p.read_text(encoding='utf-8')
 s=re.sub(r'\$\$(\\(?:phi|psi|beta))\$\^',r'$\1^',s)
 s=s.replace(r'$\log_{$\phi$}$',r'$\log_{\phi}$')
 s=re.sub(r'\$\\log_\{[^}\n]*\}\$',lambda m:r'$\log_{\phi}$'if 'phi'in m[0]else m[0],s)
 s=re.sub(r'([24])\^\$\\beta\$',lambda m:'$'+m[1]+r'^{\beta}$',s)
 parts=re.split(r'(```[\s\S]*?```|`[^`\n]*`|\$\$[\s\S]*?\$\$|\$[^$\n]*\$)',s)
 for i in range(0,len(parts),2):
  parts[i]=atom.sub(convert,parts[i])
  sub=re.split(r'(\$[^$\n]*\$)',parts[i])
  for j in range(0,len(sub),2):
   sub[j]=re.sub(r'\b(phi|psi|beta)\b',lambda m:'$\\'+m[1]+'$',sub[j])
   sub[j]=sub[j].replace('log_phi',r'$\log_{\phi}$').replace('log_2',r'$\log_{2}$')
  parts[i]=''.join(sub)
 p.write_text(''.join(parts),encoding='utf-8')
