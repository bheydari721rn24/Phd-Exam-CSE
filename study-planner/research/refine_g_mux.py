from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/g_mux.js';s=p.read_text(encoding='utf-8')
s=s.replace("const text=(x,y,s,cls='mx-label')=>", "const text=(x,y,s,cls='mx-label')=>s===''?'':")
s=s.replace('const s=validate(raw),r=evaluate(s),frames=[];',"const s=validate(raw);if(['priority','rotate'].includes(s.operation)&&s.n>3)throw Error('Priority diagrams support at most eight requests.');const r=evaluate(s),frames=[];")
p.write_text(s,encoding='utf-8')
report=json.loads((R/'research/g_mux-evidence/browser.json').read_text(encoding='utf-8'))
print([i for i in report['geometry']['issues']if i.get('text')][:30])
