from pathlib import Path
B=Path(__file__).resolve().parent;D=B.parent/'dist/chapters'
css=(D/'d_counting.css').read_text().replace('counting','inclusion')
css+='\n.inclusion-stage .math-label,.inclusion-print-trace .math-label,.inclusion-lab-diagram .math-label{font-family:"STIX Two Math",serif}.atom-input input{width:260px!important;max-width:100%}.inclusion-formula math{font-family:"STIX Two Math",serif}#inclusion-output table{font-size:.95rem}#inclusion-output td{padding:5px 10px}.inclusion-stage svg [data-entity] text{font-size:17px}#inclusion-form label{min-width:0;max-width:100%}#inclusion-form [hidden]{display:none!important}#inclusion-form select{width:100%;min-width:0;box-sizing:border-box}\n'
(D/'d_inclusion.css').write_text(css)
# Reuse reviewed accessible transport controls; every SVG model and lab is newly authored for inclusion-exclusion.
s=(D/'d_counting.js').read_text();s=s[:s.index('function subsets')].replace('counting','inclusion')
lab=(B/'d_inclusion-lab.js').read_text();(D/'d_inclusion.js').write_text(s+lab+'\n})();\n')
print('Installed dedicated inclusion models, laboratories and reviewed accessible controls.')
