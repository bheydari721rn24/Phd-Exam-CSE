from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/a_hash.js';s=p.read_text(encoding='utf-8')
s=s.replace('y="34" class="hs-caption"','y="38" class="hs-caption"')
s=s.replace(',42,28,i)',',42,34,i)').replace('y+14','y+17').replace(',56,28,b[j].key',',56,34,b[j].key')
s=s.replace("),51,", "),47,") # Probe y is embedded after the coordinate expression.
s=s.replace("/z.slots.length),51,", "/z.slots.length),47,").replace("/z.slots.length)-4,24,'probe'", "/z.slots.length)-4,32,'probe'")
s=s.replace("'Second-level arrays: exact stored positions'", "'Second-level stored positions'")
s=s.replace(",30,v?v.key:",",34,v?v.key:")
p.write_text(s,encoding='utf-8')
print('Adjusted measured glyph insets and compact column headings.')
