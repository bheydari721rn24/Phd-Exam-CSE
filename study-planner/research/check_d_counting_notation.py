from pathlib import Path
import json,re,sys,xml.etree.ElementTree as ET,tokenize,io
BASE=Path(__file__).resolve().parent
p=BASE/'author_d_counting_bank.py';s=p.read_text();tokens=[]
for t in tokenize.generate_tokens(io.StringIO(s).readline):
    if t.type==tokenize.STRING and '$' in t.string and '\\' in t.string and not re.match('[rRfF]',t.string):t=t._replace(string='r'+t.string)
    tokens.append(t)
p.write_text(tokenize.untokenize(tokens),encoding='utf-8')
sys.path.insert(0,str(BASE/'exam-rewrite'));from mathml import render
if __name__=='__main__':
    import subprocess
    subprocess.run([sys.executable,'-X','utf8',str(p)],check=True)
    bad=[]
    for q in json.loads((BASE/'d_counting-questions.json').read_text()):
        for s in [q['stem'],q['solution']]:
            for m in re.finditer(r'\$([^$]+)\$',s):
                try:ET.fromstring(render(m[1]))
                except Exception as ex:bad.append((q['id'],m[1],str(ex)))
    print('Malformed mathematical expressions:',bad)
    assert not bad
