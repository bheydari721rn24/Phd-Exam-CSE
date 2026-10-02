/* Exact finite-state certificates; no remote data and no student test. */
(function () {
  'use strict';
  function analyzeSystem(adj, initial, property, ranks) {
    const n = adj.length;
    if (!n || !adj.every(row => row.length === n && row.every(x => typeof x === 'boolean'))) throw new Error('Use a square Boolean transition matrix.');
    if (property.length !== n || !property.every(x => typeof x === 'boolean') || ranks.length !== n || !ranks.every(x => Number.isSafeInteger(x) && x >= 0)) throw new Error('Use Boolean membership and nonnegative integer ranks.');
    if (!initial.every(x => Number.isInteger(x) && x >= 0 && x < n)) throw new Error('Initial states must be valid indices.');
    const parent = Array(n).fill(null), reached = Array(n).fill(false), queue = [];
    initial.forEach(s => { if (!reached[s]) { reached[s] = true; queue.push(s); } });
    for (let head = 0; head < queue.length; head++) {
      const s = queue[head];
      for (let t = 0; t < n; t++) if (adj[s][t] && !reached[t]) { reached[t] = true; parent[t] = s; queue.push(t); }
    }
    const closureViolations = [], rankViolations = [];
    for (let s = 0; s < n; s++) for (let t = 0; t < n; t++) if (adj[s][t]) {
      if (property[s] && !property[t]) closureViolations.push([s, t]);
      if (reached[s] && !(ranks[t] < ranks[s])) rankViolations.push([s, t]);
    }
    const bad = queue.find(s => !property[s]);
    let unsafePath = null;
    if (bad !== undefined) { unsafePath = []; for (let s = bad; s !== null; s = parent[s]) unsafePath.push(s); unsafePath.reverse(); }
    const color = Array(n).fill(0), stack = []; let cycle = null;
    function visit(s) {
      color[s] = 1; stack.push(s);
      for (let t = 0; t < n && !cycle; t++) if (adj[s][t]) {
        if (color[t] === 1) cycle = stack.slice(stack.indexOf(t)).concat(t);
        else if (color[t] === 0) visit(t);
      }
      stack.pop(); color[s] = 2;
    }
    for (const s of queue) if (!cycle && color[s] === 0) visit(s);
    return {reachable: reached.flatMap((x,i) => x ? [i] : []), initialized: initial.every(s => property[s]), preserved: !closureViolations.length, safe: bad === undefined, closureViolations, rankViolations, unsafePath, cycle, terminates: !cycle};
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {analyzeSystem};
  if (typeof document === 'undefined') return;
  const holder = document.getElementById('invariant-input'); if (!holder) return;
  const output = document.getElementById('invariant-output');
  let adj, property, ranks;
  const presets = {
    noninductive: {edges:[[0,1],[2,3]], property:[true,true,true,false], ranks:[3,2,1,0]},
    inductive: {edges:[[0,1],[1,0],[2,3]], property:[true,true,false,false], ranks:[3,2,1,0]},
    unsafe: {edges:[[0,1],[1,3],[2,3]], property:[true,true,true,false], ranks:[3,2,1,0]},
    chain: {edges:[[0,1],[1,2],[2,3]], property:[true,true,true,true], ranks:[3,2,1,0]},
    cycle: {edges:[[0,1],[1,2],[2,1]], property:[true,true,true,true], ranks:[3,2,1,0]},
    badrank: {edges:[[0,1],[1,2],[2,3]], property:[true,true,true,true], ranks:[0,0,0,0]}
  };
  const math = s => '<span class="math-inline">' + s + '</span>';
  const set = xs => math('{' + xs.join(', ') + '}');
  const path = xs => math(xs.join(' → '));
  const edges = xs => xs.length ? xs.map(path).join('; ') : 'None';
  function renderResult() {
    const result = analyzeSystem(adj, [0], property, ranks);
    const member = property.flatMap((x,i) => x ? [i] : []);
    output.innerHTML = '<dl>' +
      '<dt>Reachable set</dt><dd>' + set(result.reachable) + '</dd>' +
      '<dt>Proposed truth set</dt><dd>' + set(member) + '</dd>' +
      '<dt>Initialization</dt><dd>' + (result.initialized ? 'Pass: initial state ' + math('0') + ' is included.' : 'Fail: initial state ' + math('0') + ' is excluded.') + '</dd>' +
      '<dt>Preservation</dt><dd>' + (result.preserved ? 'Pass: every transition from the truth set stays inside it.' : 'Fail on these edges: ' + edges(result.closureViolations)) + '</dd>' +
      '<dt>Reachable safety</dt><dd>' + (result.safe ? 'Pass: every reachable state satisfies the predicate.' : 'Fail. A shortest violating path is ' + path(result.unsafePath) + '.') + '</dd>' +
      '<dt>Inductive certificate</dt><dd>' + (result.initialized && result.preserved ? 'Valid: initialized and preserved.' : 'Invalid: initialization or preservation failed.') + '</dd>' +
      '<dt>Supplied rank</dt><dd>' + (!result.rankViolations.length ? 'Valid: all reachable edges strictly decrease the nonnegative integer rank.' : 'Invalid on reachable edges: ' + edges(result.rankViolations)) + '</dd>' +
      '<dt>Independent termination decision</dt><dd>' + (result.terminates ? 'Every execution is finite: the reachable subgraph has no directed cycle.' : 'An infinite execution is possible. Repeat this reachable cycle: ' + path(result.cycle) + '.') + '</dd></dl>';
    output.dataset.safe = String(result.safe); output.dataset.preserved = String(result.preserved); output.dataset.terminates = String(result.terminates);
  }
  function renderInputs() {
    holder.innerHTML = '<table class="transition-table"><caption>Transitions: checked row-to-column entries are enabled edges.</caption><thead><tr><th scope="col">From / to</th>' + [0,1,2,3].map(i => '<th scope="col">'+math(i)+'</th>').join('') + '</tr></thead><tbody>' + adj.map((row,s) => '<tr><th scope="row">'+math(s)+'</th>' + row.map((x,t) => '<td><input type="checkbox" data-edge="'+s+','+t+'" aria-label="Transition from '+s+' to '+t+'" '+(x?'checked':'')+'></td>').join('') + '</tr>').join('') + '</tbody></table>' +
    '<table><caption>Candidate assertion and rank for each state. Initial state is '+math('0')+'.</caption><thead><tr><th scope="col">State</th><th scope="col">In truth set</th><th scope="col">Rank</th></tr></thead><tbody>' + property.map((x,s) => '<tr><th scope="row">'+math(s)+'</th><td><input type="checkbox" data-member="'+s+'" aria-label="Include state '+s+' in the predicate" '+(x?'checked':'')+'></td><td><input class="rank-input" type="number" min="0" max="1000000" step="1" data-rank="'+s+'" value="'+ranks[s]+'" aria-label="Rank of state '+s+'"></td></tr>').join('') + '</tbody></table>';
    renderResult();
  }
  holder.addEventListener('change', event => {
    const node = event.target;
    if (node.dataset.edge) {const [s,t] = node.dataset.edge.split(',').map(Number);adj[s][t]=node.checked;}
    if (node.dataset.member !== undefined) property[Number(node.dataset.member)]=node.checked;
    if (node.dataset.rank !== undefined) {
      const v = Number(node.value);
      if (node.value.trim()==='' || !Number.isSafeInteger(v) || v<0 || v>1000000) {node.setCustomValidity('Enter a whole number from zero through one million.');node.reportValidity();return;}
      node.setCustomValidity('');ranks[Number(node.dataset.rank)]=v;
    }
    renderResult();
  });
  function preset(name) {const p=presets[name];adj=Array.from({length:4},()=>Array(4).fill(false));p.edges.forEach(([s,t])=>adj[s][t]=true);property=p.property.slice();ranks=p.ranks.slice();renderInputs();}
  document.querySelectorAll('[data-preset]').forEach(button=>button.addEventListener('click',()=>preset(button.dataset.preset)));
  preset('noninductive');
})();
