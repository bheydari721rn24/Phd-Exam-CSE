from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'dist/chapters/concept-unified.js';s=p.read_text(encoding='utf-8')
s=s.replace("players=[];let dataPromise;","players=[],pending=new WeakMap();let dataPromise;")
s=s.replace("async function init(host){if(host.dataset.loaded)return;host.dataset.loaded='loading';try{", "function init(host){if(pending.has(host))return pending.get(host);if(host.dataset.loaded==='true')return Promise.resolve(players.find(p=>p.host===host));const task=initialize(host);pending.set(host,task);return task;}\n async function initialize(host){host.dataset.loaded='loading';try{")
p.write_text(s,encoding='utf-8')
p=R/'dist/chapters/problem-visuals.js';s=p.read_text(encoding='utf-8')
s=s.replace("let data;const players=[];", "let data;const pending=new WeakMap(),players=[];")
s=s.replace("async function mount(host){if(host.dataset.loaded)return;const fallbackMarkup", "function mount(host){if(pending.has(host))return pending.get(host);if(host.dataset.loaded==='true')return Promise.resolve(players.find(p=>p.host===host));const task=initialize(host);pending.set(host,task);return task;}\nasync function initialize(host){const fallbackMarkup")
p.write_text(s,encoding='utf-8')
p=R/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8')
a='const tip=(pathEl)=>{const defs=E("defs"),m=E("marker",{id:"relation-tip-"+p.index'
b='const tip=(pathEl)=>{const existing=g.querySelector("[id=relation-tip-"+p.index+"]");if(existing){pathEl.setAttribute("marker-end","url(#relation-tip-"+p.index+")");return;}const defs=E("defs"),m=E("marker",{id:"relation-tip-"+p.index'
assert a in s;s=s.replace(a,b);p.write_text(s,encoding='utf-8')
print('Pending-load promises shared, repeated relation marker definitions eliminated.')
