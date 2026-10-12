from pathlib import Path
B=Path(__file__).parent;R=B.parent;p=R/'dist/chapters/semantic-diagrams.js';s=p.read_text();a=s.index('function vectorNative(');b=s.index('function countingFormula(',a);s=s[:a]+(B/'vectors-question-renderer.js').read_text()+'\n'+s[b:];p.write_text(s)
