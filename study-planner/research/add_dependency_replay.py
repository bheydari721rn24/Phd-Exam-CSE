from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/advanced-simulations.js';s=p.read_text()
s=s.replace("pairs=[],affected=[],view='after'","pairs=[],affected=[],flows=[],view='after'")
s=s.replace("function setGeometry(t){transition=t;", "function setGeometry(t){transition=t;for(const f of flows){const q=f.path.getPointAtLength(t*f.length);f.token.setAttribute('cx',q.x);f.token.setAttribute('cy',q.y);f.token.style.display=t<1?'':'none';}")
s=s.replace("(pairs.length?'Geometric replay':'Operation emphasis')", "(flows.length?'Dependency / copy replay':pairs.length?'Geometric replay':'Operation emphasis')")
needle="  function draw(i,withMotion=false){"
new="""  function dependencyFlows(svg,before){
   const nodes=new Map([...before.querySelectorAll('[data-entity]')].map(n=>[n.dataset.entity,n]));
   for(const path of svg.querySelectorAll('path[data-source-entity],path[data-net]')){
    const copied=path.dataset.sourceEntity&&nodes.has(path.dataset.sourceEntity)&&[...svg.querySelectorAll('[data-entity]')].some(n=>n.dataset.entity===path.dataset.targetEntity);
    const old=path.dataset.net?[...before.querySelectorAll('path[data-net]')].find(n=>n.dataset.net===path.dataset.net&&n.getAttribute('d')===path.getAttribute('d')):null;
    const established=old&&old.getAttribute('stroke')==='#c1cbd1'&&path.getAttribute('stroke')!=='#c1cbd1';if(!copied&&!established)continue;
    const length=path.getTotalLength();if(!length||!Number.isFinite(length))continue;const token=document.createElementNS(NS,'circle');token.setAttribute('r','4');token.setAttribute('fill','#b58132');token.dataset.dependencyToken='true';token.setAttribute('aria-hidden','true');svg.append(token);flows.push({path,length,token});
   }
  }
  function draw(i,withMotion=false){"""
assert needle in s;s=s.replace(needle,new)
s=s.replace('pairs=[];affected=[];', 'pairs=[];affected=[];flows=[];')
needle="pairs=pairGeometry(before,svg,model);"
s=s.replace(needle,needle+"dependencyFlows(svg,before);")
s=s.replace('get motionPairs(){return pairs.length;}', 'get motionPairs(){return pairs.length;},get dependencyFlows(){return flows.length;}')
p.write_text(s,encoding='utf-8')
print('Copy and dependency markers follow the existing exact connected routes; pause and scrubbing share the same clock.')
