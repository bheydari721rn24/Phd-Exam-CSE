"""Normalize joined prose words/numbers without touching formulas or code."""
import re
from space_number_prose import Prose,clean
class TeachingProse(Prose):
 def handle_data(self,s):
  if any(skip for _,skip in self.stack):self.out.append(s);return
  s=clean(s);s=re.sub(r'(?<=\d)(?!(?:st|nd|rd|th)\b)(?=[A-Za-z])',' ',s)
  s=re.sub(r'\b(method)([AB])\b',r'\1 \2',s)
  self.out.append(s)
def fix(s):
 p=TeachingProse();p.feed(s);p.close();return''.join(p.out)
