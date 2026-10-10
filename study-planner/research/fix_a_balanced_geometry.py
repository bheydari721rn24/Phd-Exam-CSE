from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
p=R/'dist/chapters/a_balanced.js';s=p.read_text(encoding='utf-8').replace('w=Math.max(56,t.keys.length*38+24)','w=Math.max(80,t.keys.length*38+24,t.keys.join(\' | \').length*11+24)')
p.write_text(s,encoding='utf-8')
