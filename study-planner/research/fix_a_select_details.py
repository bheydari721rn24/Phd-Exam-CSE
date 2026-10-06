from pathlib import Path
B=Path(__file__).resolve().parent
p=B.parent/'dist/chapters/a_select.js';s=p.read_text(encoding='utf-8')
s=s.replace('r.v<=result?palette.less:palette.unknown','result!==null&&r.v<=result?palette.less:palette.unknown')
s=s.replace('phase===2?(r.v<=p?palette.less:palette.greater):palette.unknown','phase===2?(r.v<p?palette.less:r.v===p?palette.equal:palette.greater):palette.unknown')
p.write_text(s,encoding='utf-8')
p=B/'prepare_a_select_bank.py';s=p.read_text(encoding='utf-8').replace("stem='For distinct keys","stem=r'For distinct keys");p.write_text(s,encoding='utf-8')
