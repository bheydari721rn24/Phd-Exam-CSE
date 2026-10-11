from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/a_hash.js';s=p.read_text(encoding='utf-8')
s=s.replace('const rh=Math.min(43,310/z.capacity)', 'const rh=Math.min(43,280/z.capacity)').replace(',42,34,i)',',42,30,i)').replace(',56,34,b[j].key',',56,30,b[j].key').replace('y+17','y+15')
# Empty text elements have no glyph bounds and should not exist.
s=s.replace('${esc(value)}</text>${label?', '${esc(value)}</text>${label?')
s=s.replace("return out+'</svg>';", "return out.replace(/<text[^>]*><\\/text>/g,'')+'</svg>';")
s=s.replace("typeof v==='number'?v:'',i,active?", "typeof v==='number'?v:'','',active?")
s=s.replace("return cell+(v&&typeof v==='object'?", "return cell+txt(x+i*width+(width-4)/2,y+62,String(i))+ (v&&typeof v==='object'?")
p.write_text(s,encoding='utf-8')
p=R/'research/build_a_hash.py';s=p.read_text(encoding='utf-8').replace(".hs-model svg .hs-caption{font-size:17px!important}",".hs-model svg .hs-caption{font-size:17px!important}.hs-model [data-hs-model=chaining] svg .hs-key{font-size:14px!important}")
# The initial chaining model and editable chains share the same readable type size.
s=s.replace("css+='\\n.hs-model svg [data-entity=", "css+='\\n.hs-model svg [data-entity=")
s=s.replace("(R/'dist/chapters/a_hash.css').write_text", "css+='\\n.hs-model svg [data-entity^=bucket-] .hs-key,.hs-model svg [data-entity^=K] .hs-key{font-size:14px!important}\\n'\n(R/'dist/chapters/a_hash.css').write_text")
p.write_text(s,encoding='utf-8')
print('Removed empty glyph elements; preserved fixed indices and readable chain spacing.')
