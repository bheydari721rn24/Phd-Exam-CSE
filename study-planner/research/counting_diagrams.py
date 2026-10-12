import itertools,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'exam-rewrite'));import mathml
def native(formula,x,y,w,h):
 m=mathml.render(formula)
 return f'<foreignObject x="{x}" y="{y}" width="{w}" height="{h}"><div xmlns="http://www.w3.org/1999/xhtml" style="height:100%;display:flex;align-items:center;justify-content:center;font:16px STIX Two Math,serif;overflow:hidden">{m}</div></foreignObject>'
def reports():
 pairs=list(itertools.product([1,2,3],repeat=2));summaries=list(itertools.combinations_with_replacement([1,2,3],2));tags={s:chr(65+i) for i,s in enumerate(summaries)}
 s='<figure class="logic-diagram"><svg viewBox="0 0 760 360" role="img" aria-label="All nine uniform ordered pairs induce six multiset reports with unequal masses"><title>All nine pairs and all six induced reports</title><text x="195" y="30" text-anchor="middle" font-size="20">Nine detailed outcomes</text><text x="590" y="30" text-anchor="middle" font-size="20">Six multiset reports</text>'
 for i,pair in enumerate(pairs):
  x=25+(i%3)*125;y=75+(i//3)*76;tag=tags[tuple(sorted(pair))]
  s+=f'<rect x="{x}" y="{y}" width="110" height="55" rx="7" fill="#edf5f7" stroke="#a8bec8"/>'+native(rf'({pair[0]},{pair[1]})\to\text{{{tag}}}',x+3,y+4,104,47)
 for i,pair in enumerate(summaries):
  y=50+i*46;count=1 if pair[0]==pair[1] else 2;tag=tags[pair]
  s+=f'<rect x="465" y="{y}" width="250" height="43" rx="5" fill="#e4f1e9" stroke="#acc6bc"/>'+native(rf'\text{{{tag}}}:\ \{{{pair[0]},{pair[1]}\}},\quad P=\frac{{{count}}}9',470,y+1,240,41)
 s+='<text x="195" y="318" text-anchor="middle" font-size="17">Each ordered pair has mass 1/9.</text></svg><figcaption>Both draws independently choose uniformly from three labels. The report letters identify the unique sorted multiset on the right. A repeated-label report has one preimage; a distinct-label report has two. All nine detailed outcomes and all six reports are shown. The report masses total one and are not uniform.</figcaption></figure>'
 return s
