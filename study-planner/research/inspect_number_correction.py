from pathlib import Path
B=Path(__file__).parent;R=B.parent
p=(B/'counting-question-renderer.js').read_text();a=p.index("if(s.kind==='parity')");print(p[a:a+1300])
for n in ['d_counting','a_loop']:
 p=(R/f'dist/chapters/{n}.html').read_text();a=p.index('data-source-id="MS_CS_1405_Q129"');print(n,p[a-200:a+650])
