from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/advanced-simulations.js'
s=p.read_text(encoding='utf-8').replace('recordMovementRoutes(svg,before);dependencyFlows(svg,before);','recordMovementRoutes(svg,before);if(replayFrom<index)dependencyFlows(svg,before);')
s=s.replace("(flows.length?'Dependency / copy replay':pairs.length?'Geometric replay':'Operation emphasis')","(replayFrom>index?'Reverse replay':flows.length?'Dependency / copy replay':pairs.length?'Geometric replay':'Operation emphasis')")
p.write_text(s,encoding='utf-8')
