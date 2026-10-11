from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/a_amortized.js';s=p.read_text(encoding='utf-8')
s=s.replace("let out=txt(30,y-16,label),cols=", "let out=txt(30,y-16,capacity>16?label.split('·')[0]+'· '+capacity+' slots; first sixteen shown':label),cols=")
s=s.replace("if(capacity>16)out+=txt(30,y-36,'Shown indices 0–15 of capacity '+capacity+'; full state is in the snapshot.');",'')
p.write_text(s,encoding='utf-8')
print('Kept capacity qualifiers in their own row heading, without colliding with source-record identifiers.')
