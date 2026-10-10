from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/d_generating.js'
s=p.read_text(encoding='utf-8').replace("txt(28,342,'Other diagonals contribute to other target coefficients.')", "txt(470,286,'Other diagonals contribute')+txt(470,318,'to other target coefficients.')")
p.write_text(s,encoding='utf-8')
