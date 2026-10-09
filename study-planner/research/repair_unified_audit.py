from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'research/qa_unified_library.py';s=p.read_text();s=s.replace("   if topic in report['chapters']and not report['chapters'][topic].get('failedHosts'):continue","  if topic in report['chapters']and not report['chapters'][topic].get('failedHosts'):continue")
s=s.replace("if(!svg){issues.push({frame:i,kind:'missing scientific diagram'});continue;}","if(!svg){if(!p.host.querySelector('.sim-stage math'))issues.push({frame:i,kind:'missing scientific diagram or derivation'});checks++;continue;}")
p.write_text(s,encoding='utf-8')
p=R/'dist/chapters/a_arrays.js';s=p.read_text();s=s.replace('frames:z.states.map(f=>({svg:picture(z,f),','frames:z.states.map(f=>({state:f,svg:picture(z,f),');p.write_text(s,encoding='utf-8')
print('Audit supports exact MathML steps; existing computed array-lab state is now exposed.')
