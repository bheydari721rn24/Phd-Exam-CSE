"""Keep matching MathML fences and scripts on a complete mathematical base.

TeX `(x+y)^2` needs msup(mrow('(', x+y, ')'), 2), not a script
whose base is only ')'. Token order and all non-mrow structures are retained.
Half-open intervals are legitimate mixed fence pairs, not missing glyphs.
"""
import xml.etree.ElementTree as ET
from collections import Counter

NS='http://www.w3.org/1998/Math/MathML'
ET.register_namespace('',NS)
OPEN='([{⌈⌊⟨';CLOSE=')]}⌉⌋⟩';PAIRS=dict(zip(OPEN,CLOSE))
SCRIPTS={'msup','msub','msubsup','mover','munder','munderover'}

def local(e):return e.tag.rsplit('}',1)[-1]
def glyph(e):return e.text if local(e)=='mo' else None
def delimiter(e):
 if local(e) in SCRIPTS and len(e):return glyph(e[0]),e[0]
 return glyph(e),e
def signature(e):
 return Counter((local(n),tuple(sorted(n.attrib.items())),n.text or '') for n in e.iter() if local(n)!='mrow')

def group_fences(root):
 count=0
 for row in list(root.iter())[::-1]:
  if local(row) not in {'mrow','math','mtd'}:continue
  children=list(row);stack=[];i=0
  while i<len(children):
   item=children[i];symbol,token=delimiter(item)
   if symbol and symbol in OPEN and local(item)=='mo':stack.append((i,symbol))
   elif symbol and symbol in CLOSE and stack:
    start,opening=stack[-1]
    # ()/[] can close an explicitly half-open interval. Other mixed pairs
    # are not silently "repaired"; the audit must report them for review.
    if PAIRS[opening]!=symbol and not(opening in '([' and symbol in ')]'):
     i+=1;continue
    stack.pop();whole=start==0 and i==len(children)-1 and local(item)=='mo'
    if not whole:
     group=ET.Element(row.tag.rsplit('}',1)[0]+'}mrow' if '}' in row.tag else 'mrow')
     for node in children[start:i]:group.append(node)
     if local(item) in SCRIPTS:
      item.remove(token);group.append(token);item.insert(0,group);replacement=item
     else:group.append(item);replacement=group
     children[start:i+1]=[replacement];i=start;count+=1
   i+=1
  row[:]=children
 return count

def normalize_fences(value):
 root=ET.fromstring(value);before=''.join(root.itertext());counts=signature(root)
 changes=group_fences(root)
 assert ''.join(root.itertext())==before,'Fence grouping changed mathematical text'
 assert signature(root)==counts,'Fence grouping changed non-row tokens or scripts'
 return ET.tostring(root,encoding='unicode',short_empty_elements=True) if changes else value

def closing_script_bases(root):
 return [n for n in root.iter() if local(n) in SCRIPTS and len(n) and glyph(n[0]) and glyph(n[0]) in CLOSE]

def delimiter_issues(root):
 """Audit real fence tokens, allowing half-open intervals and case braces."""
 case_braces=set()
 for row in root.iter():
  if local(row)=='mrow' and len(row)==2 and glyph(row[0])=='{' and local(row[1])=='mtable':case_braces.add(id(row[0]))
 stack=[];issues=[]
 for n in root.iter():
  if id(n) in case_braces:continue
  s=glyph(n)
  if s and s in OPEN:stack.append(s)
  elif s and s in CLOSE:
   if not stack:issues.append('Unmatched closing '+s);continue
   opening=stack.pop()
   if PAIRS[opening]!=s and not(opening in '([' and s in ')]'):issues.append('Mismatched '+opening+s)
 issues.extend('Unmatched opening '+s for s in stack)
 return issues
