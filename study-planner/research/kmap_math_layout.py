"""Keep list fences and product factors intact while adding semantic continuation rows."""
import xml.etree.ElementTree as ET
from mathml import width
def table(rows):
 t=ET.Element('mtable',dict(displaystyle='true',columnalign='left',rowspacing='.45em'))
 for row in rows:
  tr=ET.SubElement(t,'mtr');cell=ET.SubElement(tr,'mtd');rr=ET.SubElement(cell,'mrow');rr.extend(row)
 return t
def wrap(value):
 root=ET.fromstring(value)
 def process(e):
  for ch in list(e):process(ch)
  if e.tag!='mrow':return
  children=list(e);units=[];i=0
  while i<len(children):
   ch=children[i]
   if ch.tag=='mo' and ch.text in ['(','[','{']:
    depth=1;j=i+1
    while j<len(children) and depth:
     if children[j].tag=='mo':
      if children[j].text in ['(','[','{']:depth+=1
      if children[j].text in [')',']','}']:depth-=1
     j+=1
    if depth==0:
     inside=children[i+1:j-1];group=ET.Element('mrow');group.append(ch)
     # Lists split only at top-level commas. One outer fence retains full scope.
     if any(x.tag=='mo' and x.text==',' for x in inside) and sum(width(x) for x in inside)>7:
      rows=[];row=[];w=0;d=0
      for x in inside:
       row.append(x);w+=width(x)
       if x.tag=='mo':
        if x.text in ['(','[','{']:d+=1
        if x.text in [')',']','}']:d-=1
        if x.text==',' and d==0 and w>=5:rows.append(row);row=[];w=0
      if row:rows.append(row)
      group.append(table(rows))
     else:group.extend(inside)
     group.append(children[j-1]);units.append(group);i=j;continue
   units.append(ch);i+=1
  e[:]=units
 process(root)
 if width(root)<=9:return ET.tostring(root,encoding='unicode')
 rows=[];row=[];w=0
 for u in list(root):
  isop=u.tag=='mo' and u.text in ['+','−','-','=','∨','∧','⊕','⇒','⇔',',']
  if row and ((w+width(u)>9 and not isop) or (isop and w>5)):
   rows.append(row);row=[];w=0
   # Explicit multiplication marks a continuation of adjacent POS factors.
   prev=rows[-1][-1]
   if u.tag=='mrow' and len(u) and u[0].tag=='mo' and u[0].text=='(' and prev.tag=='mrow' and len(prev) and prev[-1].tag=='mo' and prev[-1].text==')':
    dot=ET.Element('mo');dot.text='·';row.append(dot);w=width(dot)
  row.append(u);w+=width(u)
 if row:rows.append(row)
 root[:]=[table(rows)]
 return ET.tostring(root,encoding='unicode')
