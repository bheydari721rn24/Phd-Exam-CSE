from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/d_generating.js'
s=p.read_text(encoding='utf-8')
s=s.replace('650/values.length','660/values.length')
s=s.replace("txt(28,34,'Choose only", "txt(28,24,'Choose only")
s=s.replace('const cell=34,x0=155,y0=75','const cell=38,x0=155,y0=55')
s=s.replace('y0+i*cell+23','y0+i*cell+25').replace('x0+i*cell+16','x0+i*cell+18').replace('x0+j*cell+16','x0+j*cell+18')
s=s.replace('y0+i*cell,32,32','y0+i*cell,36,36')
s=s.replace("txt(28,333,'Other diagonals", "txt(28,344,'Other diagonals")
s=s.replace("txt(28,105+i*57,'Row '","txt(14,105+i*57,'Row '")
p.write_text(s,encoding='utf-8')
