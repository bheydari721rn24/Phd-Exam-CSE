from pathlib import Path
import re
p=Path(__file__).resolve().parent/'animations/gauss.py'
s=p.read_text()
values=iter([r'M=TM_0',r'x-y=-1,\quad4x+2y=8\quad\Rightarrow\quad6y=12',r'(\alpha+2)z=\alpha^2-4',r'A=LU',r'PA=LU',r'x=1+z,\quad y=z\quad(\bmod\,2)',r'Q=\begin{bmatrix}1&-2\\0&1\end{bmatrix},\quad x=Qy',r'x_{\mathrm{exact}}=\frac{10000}{9999},\quad y_{\mathrm{exact}}=\frac{9998}{9999}'])
s=re.sub(r"formula=r'[^']*'",lambda m:"formula=r'"+next(values)+"'",s,flags=re.S)
p.write_text(s)
assert not any(ord(x)<32 and x not in '\n\r\t' for x in s)
print('All animation formulas use valid explicit notation.')
