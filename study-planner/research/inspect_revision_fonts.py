import ast,unicodedata
from pathlib import Path
from html.parser import HTMLParser
from math_typography import LIST_MARKER,SINGLE_VARIABLE
tree=ast.parse(Path(__file__).with_name('check_site_en.py').read_text())
for node in tree.body:
 if isinstance(node,ast.ClassDef) and node.name=='MathCoverage':exec(compile(ast.Module(body=[node],type_ignores=[]),'<coverage>','exec'))
class Inspect(MathCoverage):
 def handle_data(self,data):
  before=len(self.unstyled);super().handle_data(data)
  if len(self.unstyled)>before:print(repr(data),self.unstyled[before:])
for p in Path(__file__).resolve().parents[1].joinpath('dist/chapters').glob('*.html'):
 parser=Inspect();print(p.stem);parser.feed(p.read_text(encoding='utf-8'))
