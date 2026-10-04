"""Keep punctuation attached while preserving scoped numeric-list continuation."""
import xml.etree.ElementTree as ET
from kmap_math_layout import wrap as scoped_wrap
def wrap(value):
 root=ET.fromstring(scoped_wrap(value))
 for table in list(root.iter('mtable')):
  rows=list(table)
  for i,row in enumerate(rows):
   if i==0:continue
   leaves=[x for x in row.iter() if not len(x)]
   if leaves and all(x.tag=='mo' and x.text in ['.',';',':'] for x in leaves):
    previous=list(table)[list(table).index(row)-1]
    dest=next(previous.iter('mrow'))
    dest.extend(leaves);table.remove(row)
 return ET.tostring(root,encoding='unicode')
