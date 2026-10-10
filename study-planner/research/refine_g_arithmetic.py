from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
p=R/'dist/chapters/g_arithmetic.js';s=p.read_text(encoding='utf-8').replace("box(x,y,w-8,32,r<s.done", "box(x,y,w-8,34,r<s.done").replace('140+r*39','140+r*52').replace('box(x,y,w-8,34,r<s.done','box(x,y,w-8,44,r<s.done').replace('y+23,valid?val','y+29,valid?val').replace('155+s.n*39','155+s.n*52');p.write_text(s,encoding='utf-8')
p=B/'render_g_arithmetic.py';s=p.read_text(encoding='utf-8').replace("if q.get('visualQualification'):visual=", "if visual and not q.get('visualQualification'):visual='<p class=\"visual-scope\">Companion visualization: the diagram title specifies its sample operands and width. Follow the written solution for the problem\'s own parameters; this sample illustrates the reasoning pattern.</p>'+visual\n if q.get('visualQualification'):visual=")
# Avoid a single quote inside the generated single-quoted HTML string.
s=s.replace("problem's own parameters",'stated problem parameters')
p.write_text(s,encoding='utf-8')
p=B/'g_arithmetic.en.md';s=p.read_text(encoding='utf-8')
needle="Radix-two Booth recoding sets an implicit lower bit"
addition=r'''For n-bit A and m-bit B, write the signed product explicitly:

$$A_sB_s=\sum_{i=0}^{n-2}\sum_{j=0}^{m-2}a_ib_j2^{i+j}-\sum_{i=0}^{n-2}a_ib_{m-1}2^{i+m-1}-\sum_{j=0}^{m-2}a_{n-1}b_j2^{n-1+j}+a_{n-1}b_{m-1}2^{n+m-2}.$$

Each negative-weight Boolean product x can be replaced by its complement: $-x2^k=(1-x)2^k-2^k$. The weights subtracted across the two cross-term rows sum to $2^{n+m-1}-2^{m-1}-2^{n-1}$. Therefore the complemented array needs correction constant $2^{n+m-1}+2^{m-1}+2^{n-1}$ modulo $2^{n+m}$. For equal widths, combine the duplicated $2^{n-1}$ terms into $2^n$. These constants describe this exact two's-complement weighted arrangement, not every diagram labeled Baugh–Wooley.

For four-bit negative three times negative two, lower unsigned portions are five and six. Their product contributes thirty; complemented negative rows contribute sixteen and eight; the double-sign term contributes sixty-four; the correction constant is one hundred forty-four. Their total is 262, whose low eight bits represent six. This calculation checks the array's constants against the exact signed product without requiring a memorized circuit layout.

'''
if addition not in s:s=s.replace(needle,addition+needle)
p.write_text(s,encoding='utf-8')
print('Refined figure padding, sample qualification, and signed partial-product derivation.')
