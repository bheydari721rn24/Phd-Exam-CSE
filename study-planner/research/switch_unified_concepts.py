from pathlib import Path
import re
R=Path(__file__).resolve().parents[1]
for p in list((R/'dist/chapters').glob('*.html'))+list((R/'research').glob('render_*.py')):
 s=p.read_text(encoding='utf-8');n=re.sub(r'src="concept-animation.js(?:\?[^\"]*)?"','src="concept-unified.js?v=library-unified-1"',s)
 if n!=s:p.write_text(n,encoding='utf-8')
print('Written chapters and rendering templates use the unified concept adapter.')
