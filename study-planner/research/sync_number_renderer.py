from pathlib import Path
import re
B=Path(__file__).parent;p=B.parent/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8');new=(B/'number-question-renderer.js').read_text(encoding='utf-8')
marker='/* NUMBER QUESTION RENDERER */'
if marker in s:s=s[:s.index(marker)]+s[s.index('/* END NUMBER QUESTION RENDERER */')+len('/* END NUMBER QUESTION RENDERER */'):]
i=s.index('function flowQuestion');s=s[:i]+marker+'\n'+new+'\n/* END NUMBER QUESTION RENDERER */\n'+s[i:]
if 'id.startsWith("number-question-")' not in s:
 needle='if(id.startsWith("flow-question-"))';assert needle in s;s=s.replace(needle,'if(id.startsWith("number-question-"))return numberQuestion(p,g,f);'+needle,1)
p.write_text(s,encoding='utf-8')
