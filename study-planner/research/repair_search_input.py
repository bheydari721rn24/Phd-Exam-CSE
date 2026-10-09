from pathlib import Path
import re,html
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/i_uninformed.html';s=p.read_text(encoding='utf-8')
def repair(m):return m[1]+html.unescape(re.sub(r'<[^>]*>','',m[2]))+m[3]
s=re.sub(r'(<textarea name="edges">)([\s\S]*?)(</textarea>)',repair,s)
p.write_text(s,encoding='utf-8')
