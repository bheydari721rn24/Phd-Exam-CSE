"""Render an archive booklet or selected pages for direct mathematical reading."""
import json,sys
from pathlib import Path
import pypdfium2 as pdfium
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[2];CACHE=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406')
files=json.loads((ROOT/'research/exam-calibration/archive-manifest.json').read_text())['files']
key=sys.argv[1];level,field,year=key.split('_')
matches=[x for x in files if (x['level'],x['field'],x['year'])==(level,field,year)]
if len(matches)>1:
 matches=[x for x in matches if sys.argv[2] in x['repoPath']];pages_arg=sys.argv[3:]
else:pages_arg=sys.argv[2:]
assert len(matches)==1,matches
f=matches[0];doc=pdfium.PdfDocument(CACHE/'source'/f['repoPath']);out=CACHE/'pages'/key;out.mkdir(parents=True,exist_ok=True)
numbers=[int(n) for n in pages_arg] if pages_arg else list(range(1,len(doc)+1))
for n in numbers:
 page=doc[n-1];image=page.render(scale=2.1).to_pil();image.save(out/f'{n:02}.png');page.close()
print(key,'pages',len(doc),'rendered',numbers)
thumbs=[]
for n in numbers:
 im=Image.open(out/f'{n:02}.png');im.thumbnail((480,670));canvas=Image.new('RGB',(500,710),'#edf1f4');canvas.paste(im,((500-im.width)//2,30));ImageDraw.Draw(canvas).text((15,10),f'{key} / PDF page {n}',fill='black');thumbs.append(canvas)
for start in range(0,len(thumbs),6):
 sheet=Image.new('RGB',(1500,1420),'#edf1f4')
 for j,im in enumerate(thumbs[start:start+6]):sheet.paste(im,((j%3)*500,(j//3)*710))
 sheet.save(out/f'contact-{start//6+1}.png')
doc.close()
