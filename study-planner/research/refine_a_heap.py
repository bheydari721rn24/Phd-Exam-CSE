from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
p=R/'dist/chapters/a_heap.js';s=p.read_text(encoding='utf-8')
s=s.replace('radius=22','radius=27').replace("label:e.id+' @ '+i","label:e.id").replace("label:t.id+' d='+t.children.length","label:t.id+'/'+t.children.length")
s=s.replace('txt(p.x,p.y+5,n.key','txt(p.x,p.y-3,n.key').replace("+'</g>'+txt(p.x,p.y+34,n.label,'hp-meta','middle')","+txt(p.x,p.y+17,n.label,'hp-id','middle')+'</g>'")
p.write_text(s,encoding='utf-8')
p=B/'build_a_heap.py';s=p.read_text(encoding='utf-8').replace('Eight offerings from seven universities','Nine offerings from eight universities').replace('font-size:19px!important;fill:#163d55','font-size:16px!important;fill:#163d55').replace('font-size:15px!important','font-size:14px!important')
if 'svg .hp-id{'not in s:s=s.replace("(R/'dist/chapters/a_heap.css').write_text","css+='\\n.hp-model svg .hp-id{font-family:STIX Two Math,serif!important;font-size:12px!important;fill:#385d6e}\\n'\n(R/'dist/chapters/a_heap.css').write_text")
p.write_text(s,encoding='utf-8')
p=B/'a_heap-source-audit.md';s=p.read_text(encoding='utf-8').replace('eight offerings from seven universities','nine offerings from eight universities').replace('final proof diagram inspected','final proof assumptions and all conclusions read in text');p.write_text(s,encoding='utf-8')
print('Refined compact node identities and corrected the bounded source pool count.')
