from pathlib import Path
B=Path(__file__).resolve().parent
p=B.parent/'dist/chapters/a_select.js';s=p.read_text(encoding='utf-8')
old="if(p!==null)s+=text(40,535,'Selected representative pivot: '+p,'math');return wrap(s,575);"
new="""if(p!==null){s+=text(40,535,'Selected representative pivot: '+p,'math');s+=text(40,575,'Copied representative keys; select their lower median');g.forEach((col,j)=>{const r=col[Math.floor((col.length-1)/2)];s+=cell({v:r.v,id:'m'+j},85+j*170,600,r.v===p?palette.equal:palette.unknown,78);});}return wrap(s,p===null?575:710);"""
assert old in s;s=s.replace(old,new)
s=s.replace("<mo>-</mo>","<mo>−</mo>")
p.write_text(s,encoding='utf-8')
