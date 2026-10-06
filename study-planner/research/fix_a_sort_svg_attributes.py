from pathlib import Path
B=Path(__file__).parent
for name in ['a_sort_engine.py','build_a_sort_models.py','a_sort_lab.js']:
 p=B/name;s=p.read_text(encoding='utf-8')
 for a in ['data-box','data-contained','data-edge']:s=s.replace(a+' ',a+'="" ')
 p.write_text(s,encoding='utf-8')
