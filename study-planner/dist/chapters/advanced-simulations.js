/* Exact checkpoints, subject-specific focus views, and interruptible geometric replay.
 * Arithmetic is never interpolated. The original scientific snapshots are read-only.
 */
"use strict";
(() => {
 const NS='http://www.w3.org/2000/svg',MNS='http://www.w3.org/1998/Math/MathML';
 const reduced=matchMedia('(prefers-reduced-motion: reduce)'),players=[];
 const esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const el=(tag,text,cls)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;};
 const num=x=>typeof x==='number'&&Number.isFinite(x)?Number(x.toPrecision(7)).toString():String(x??'—');
 const actual=f=>({...f.snapshot??f.state??f.teaching?.currentState??(f.rows?Object.fromEntries(f.rows.map(r=>[r.name,r.values??r.cells])):Object.fromEntries((f.nodes??[]).map(n=>[n.id,n.label]))),...(f.metrics?{counters:f.metrics}:{})});
 const diff=(a,b,path='')=>{if(JSON.stringify(a)===JSON.stringify(b))return [];if(a&&b&&typeof a==='object'&&typeof b==='object'&&Array.isArray(a)===Array.isArray(b))return [...new Set([...Object.keys(a),...Object.keys(b)])].flatMap(k=>diff(a[k],b[k],path?path+'.'+k:k));return [{field:path,before:a??null,after:b??null}];};
 const mathValue=(v,compact=false)=>{const n=document.createElementNS(MNS,'math');if(typeof v==='string'&&/^-?\d+\/\d+$/.test(v)){const q=document.createElementNS(MNS,'mfrac');v.split('/').forEach(x=>{const c=document.createElementNS(MNS,'mn');c.textContent=x;q.append(c);});n.append(q);}else{if(compact&&typeof v==='number'&&num(v)!==String(v)){const approx=document.createElementNS(MNS,'mo');approx.textContent='≈';n.append(approx);n.setAttribute('title','Stored value: '+String(v));}const c=document.createElementNS(MNS,typeof v==='number'?'mn':'mtext');c.textContent=typeof v==='object'?JSON.stringify(v):v===null?'not present':compact?num(v):String(v);n.append(c);}return n;};
 // Each kind has an explicit reading contract; these are not interchangeable cartoons.
 const focus={
 'rank-certificate':'Track the less-than and equality classes separately. A repeated key occupies an interval of occurrence ranks.',
 'linear-equality':'Follow the equality test at each index. An unsuccessful test rules out only the inspected record.',
 'binary-boundary':'Watch the half-open interval shrink. The boundary can equal the array length even when no record qualifies.',
 'paired-extrema':'A pair comparison chooses two candidates; only the smaller challenges the minimum and only the larger challenges the maximum.',
 'three-way-selection':'Keep record identities through swaps. The four regions are less, equal, unclassified and greater; a swapped-in record must still be inspected.',
 'tournament-certificate':'Follow the connected winner tree. Only records that lost directly to the maximum can be second largest.',
 'median-groups':'Read medians of constant-size groups, then the pivot certificate. A partial group must not silently count as a complete group.',
 'two-array-cuts':'Move cuts rather than elements. The two left partitions contain exactly k records; check both cross inequalities.',
 'weighted-mass':'Compare cumulative weight with half the total weight. Equal keys enter as one complete mass block.',
 'pivot-expectation':'Each pivot rank contributes its probability times its residual cost. This is an expectation over pivot choices, not one execution.',
 'histogram-density':'Compare bin area, not height alone. A wide bin with the same count must have a lower density.',
 'empirical-step-function':'Open markers show excluded left limits; filled markers show the right-continuous value. Ties produce one complete jump.',
 'squared-loss':'See the center move against fixed observations. Sum the squared residuals; the minimum occurs at the mean.',
 'absolute-loss':'See distances rather than signed residuals. For even sample sizes a whole median interval can minimize the loss.',
 'residual-energy':'Signed residuals become nonnegative squares before accumulation. The denominator is applied only after the energy is known.',
 'affine-transform':'Record identities stay fixed while positions move. Intermediate positions illustrate the map and are not additional statistical observations.',
 'boxplot-construction':'Separate quartiles, fences and observed whisker endpoints. A fence need not coincide with an observation.',
 'outlier-contamination':'Follow one replaced observation and compare its effects on the mean, median and variance on the same scale.',
 'paired-covariance':'Keep the original x–y pairing. The sign of each centered product depends on the quadrant relative to the means.',
 'quantile-comparison':'Pair common probability levels, not original subjects. The Q–Q plot compares distributional shapes.',
 'quantile-conventions':'Distinguish the observed ceiling-rank value from interpolation between adjacent order statistics.',
 'streaming-moments':'Follow the incoming value, old mean, updated mean and M₂ in their actual update order.',
 'time-series-smoothing':'The highlighted window or previous smoother determines the next estimate. A forecast uses only information already available.',
 'within-between-decomposition':'Recenter each group at the pooled mean. Within-group and between-group energies are separate additive components.',
 'mixture-rate-reversal':'Compare subgroup rates first, then subgroup weights. Aggregated rates need not preserve the subgroup ordering.',
 'weighted-fiber-map':'Follow each source atom to its output fiber. Probabilities of atoms with the same output must be added.',
 'many-to-one-transformation':'The map can merge distinct inputs. One output mass is the sum of all its incoming probability masses.',
 'cdf-jump-construction':'Build the cumulative law in support order. Each jump equals the probability mass at that atom.',
 'conditional-law-filter':'Discard excluded atoms, then divide surviving masses by the event probability. The unconditioned and conditioned laws differ.',
 'countable-bayes-reweighting':'Multiply each prior weight by its likelihood, then normalize by evidence. Keep the unshown tail explicit.',
 'interval-endpoint-tests':'Endpoint membership is a logical test, not a visual approximation. Strict and non-strict inequalities treat atoms differently.',
 'inverse-sampling-cells':'Locate the uniform input in cumulative-probability cells. The returned value is an atom, not the probability coordinate.',
 'quantile-threshold-selection':'Select the first support value whose cumulative mass reaches the threshold; a boundary convention matters.',
 'weighted-convolution-grid':'Each joint cell contributes product mass to its sum diagonal. Add all cells with the same output.',
 'maximum-joint-grid':'A maximum threshold selects a square region of the joint grid. A single diagonal cell is insufficient.',
 'binomial-count-recurrence':'Each old mass splits into failure and success branches. Contributions merge into the next count, preserving total mass.',
 'poisson-binomial-recurrence':'Use the probability of the current trial, not one common probability. Merge the two branches at each count.',
 'binomial-poisson-limit':'Compare masses on a shared axis as n changes with fixed mean. Approximation errors are finite-n quantities.',
 'geometric-wait':'The current success mass is survival so far times the current hazard. Remaining survival is not another observed success.',
 'varying-hazard-wait':'Changing hazards change each successive survival factor. Memorylessness cannot be assumed.',
 'censored-wait':'The final cell includes paths that reach the cap. Do not confuse censoring mass with success exactly at the cap.',
 'negative-binomial-stopping':'The final trial is the last required success. Count arrangements only in the preceding trials.',
 'hypergeometric-subsets':'Choose success and failure subsets without replacement. The feasible support is bounded by both populations.',
 'latent-probability-mixture':'Condition on the latent probability before averaging. Shared latent randomness creates dependence.',
 'poisson-mass-recurrence':'Generate adjacent masses by their exact recurrence; the probability beyond the displayed support remains a tail.',
 'urn-state-propagation':'Without replacement, branch probabilities depend on the current composition. Merge states with the same success count.',
 'signed-weighted-balance':'Each contribution is transformed value times probability. Negative and positive contributions accumulate with their signs.',
 'integrability-tail-test':'A finite prefix cannot prove an infinite expectation exists. Track positive, negative and absolute contributions separately.',
 'outcome-wise-linearity':'Compute the expression inside each outcome before averaging. Linearity does not require independence.',
 'permutation-match-count':'One diagram is one permutation; the expected count averages indicators over all uniform permutations.',
 'running-record-algorithm':'Distinguish a realized record update from its probability. At position i, symmetry gives the record probability.',
 'occupancy-ball-placement':'A new ball may create a new occupied bin or a collision. Realized counts and expected counts are different quantities.',
 'integer-tail-layer-cake':'An outcome contributes one horizontal layer for each attained threshold. Tail probabilities recover moments by weighted sums.',
 'capped-waiting-survival':'The kth trial runs only if earlier trials failed. Sum execution probabilities, not stopping-time masses.',
 'least-squares-loss':'Separate irreducible variance from the squared displacement of the proposed constant from the mean.',
 'graph-edge-and-triangle-count':'Edge and triangle indicators have different event requirements. Shared edges do not prevent linearity of expectation.',
 'overlapping-success-windows':'Count every eligible window, including overlapping ones. Dependence between windows does not invalidate summing expectations.',
 'oriented-parallelogram':'Connected edges describe signed area. Orientation changes the sign; physical area is its absolute value.',
 'cofactor-deletion':'Strike the selected row and column, preserve the surviving minor, then apply the checkerboard sign.',
 'permutation-term-grid':'Select exactly one entry in each row and column. The inversion parity sets the sign of the product.',
 'row-operation-matrix-ledger':'Track the displayed matrix and the determinant multiplier separately. Row addition, swapping and scaling have different effects.',
 'adjugate-product-grid':'The adjugate is the transposed cofactor matrix. Follow the selected row–column product in the identity A adj(A).',
 'cramer-column-replacement':'Replace only the selected column with b. Divide that determinant by the original coefficient determinant.',
 'diagonal-subspace-volume':'Each direction supplies one factor. A collapsed direction makes the full oriented volume zero.',
 'quadratic-form-direction-factors':'Test the relevant directional factors rather than treating a positive determinant alone as positive definiteness.',
 'partitioned-block-elimination':'Eliminate the coupled block with its stated invertibility assumption. The remaining block is the Schur complement.',
 'rank-one-selected-column-expansion':'Multilinearity permits one replaced column at a time. Terms with repeated update directions vanish.',
 'node-to-power-matrix':'Follow node differences and repeated-node collapse. Distinct nodes are the condition behind the Vandermonde product.',
 'continuant-recurrence-plot':'The last diagonal term and neighboring off-diagonal pair supply the two recurrence contributions.',
 'gram-minor-area':'Gram determinants measure squared geometric size. A dependence relation collapses the relevant area.',
 'oriented-triangle-translation':'Translate all vertices together and compare edge differences. Translation preserves signed area.',
 'reflection-vector-geometry':'The normal component reverses while tangential components remain. Connect this geometric action to determinant sign.',
 'plane-geometry':'Follow the vector and its constraint residual. The displayed projection is a view of three-dimensional coordinates, not an extra equation.',
 'vector-geometry':'Connect coefficients, the resulting vector and membership. A union of subspaces need not contain their sum.',
 'quotient-geometry':'Move representatives along the identified direction while quotient coordinates remain unchanged.',
 'polynomial-plot':'Read coefficients as vector coordinates. A polynomial curve alone does not display all linear constraints.',
 'finite-field-table':'Operations occur in the stated finite field. Real-number geometric intuition does not count finite-field choices.',
 'matrix-column-selection':'A spanning set can contain redundant columns. Follow the selected independent columns and resulting rank.',
 'matrix-constraint-coupling':'Row and column sum constraints overlap. Their equations cannot all be counted as independent.',
 'matrix-decomposition':'Separate complementary components and check that their sum recovers the original matrix.',
 'matrix-row-reduction':'Row operations preserve the represented solution constraints and rank. Track the row operator with the reduced matrix.',
 'matrix-symmetry-constraint':'Symmetry and trace conditions couple entries. Count free parameters only after all relations are imposed.',
 'agent-loop':'Follow environment, percept, internal decision and action in causal order. A percept is not automatically the full physical state.',
 'utility-bars':'Compare expected utilities under the stated objective. A larger outcome in one state need not mean larger expected utility.',
 'belief-bars':'Evidence changes posterior weights. Distinguish the probability of the evidence from the posterior conditional on it.',
 'information-tree':'Follow each information branch, optimize within that branch, then average. Information cost is subtracted last.',
 'learning-architecture':'Follow the selected learning-agent component and its actual input/output links; the critic does not choose the external action.',
 'task-specification':'Read performance, environment, actuators and sensors as different parts of one task specification.',
 'probability-threshold':'Follow utility lines on fixed axes. Their crossing separates the regions where each action is optimal.',
 'discount-bars':'Changing the discount changes the value of later rewards. The displayed order follows the actual discounted returns.',
 'regret-table':'Regret is relative to the best action in each state. The minimax action minimizes its largest statewise regret.',
 'payoff-table':'Compare the objective assigned to each participant. Common interest and conflicting interest imply different decisions.',
 'counter-game':'Follow legal removals, whose turn it is and the remaining counters. A legal path alone is not an optimal strategy proof.',
 'history-aliasing':'Identical current observations can conceal different histories that require different optimal actions.',
 'state-cycle':'Different search histories can revisit the same physical state. An unbounded history tree can arise from a finite state graph.',
 'state-legality-graph':'The chosen state representation must include information needed to decide legal actions, such as possession of a key.',
 'state-versus-node':'A search node carries a path, depth and cost; multiple nodes may represent the same state.',
 'vacuum-belief-set':'An action updates the set of states still consistent with uncertainty. This set is not one actual world.',
 'vacuum-motion':'Follow robot position, dirt state and accumulated action cost. Movement and cleaning alter different state components.',
 'search-graph':'Read the frontier using the algorithm-specific order alongside the graph. Generated, selected, expanded, duplicate and stale entries are separate events.',
 'search-count':'Distinguish state count, path count, frontier size and repeated depth-limit work. They grow according to different sums.',
 'bidirectional-layers':'Expand complete layers from both endpoints. Meeting depth and work estimates must use the stated branching assumptions.',
 'cost-contour':'A finite depth can accumulate cost below a contour. Positive individual costs do not imply a common positive lower bound.',
 'grid-path':'Follow one route through grid states while distinguishing the number of routes from the number of states.',
 'byte-memory':'Addresses stay fixed. Read and write heads identify exact bytes; the first zero byte terminates a C string, not its containing allocation.',
 'recursion-stack':'Keep suspended callers visible. A return removes one invocation and resumes its saved continuation; depth is not total calls.',
 'call-tree':'Each node is one invocation and each edge is an actual parent–child call. Repeated arguments can occur in different invocations.',
 'hanoi-pegs':'Follow a top disk through lift, transfer and lowering. Transit geometry is not a settled legal puzzle configuration.',
 'interval-shrink':'Track the half-open interval and tested positions. The recursion continues only inside the retained interval.',
 'koch-geometry':'Each segment is replaced by four connected segments of one-third its length. Segment count and total length change differently.'
 };
 focus['decision-belief']=focus['information-tree'];focus['exact-generator-row-reduction']=focus['matrix-row-reduction'];focus['editable-exact-row-elimination']=focus['row-operation-matrix-ledger'];focus['editable-oriented-area']=focus['oriented-parallelogram'];
 const colors={ink:'#294655',blue:'#286f96',green:'#36816c',gold:'#b58132',pale:'#eaf2f6',border:'#9bb8c5'};
 const tx=(x,y,text,cls='')=>`<text x="${x}" y="${y}" class="${cls}" text-anchor="middle">${esc(text)}</text>`;
 const rect=(x,y,w,h,fill=colors.pale)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="8" fill="${fill}" stroke="${colors.border}"/>`;
 const line=(x1,y1,x2,y2,color=colors.border)=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="2"/>`;
 const wrap=(body,title,height=420)=>`<svg xmlns="${NS}" viewBox="0 0 1000 ${height}" role="img" aria-label="${esc(title)}"><title>${esc(title)}</title><defs><marker id="focus-arrow" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1L7 4L1 7" fill="none" stroke="context-stroke" stroke-width="1.2"/></marker></defs>${body}</svg>`;
 function slots(a,y,{label='',key='cell',active=()=>false,style=()=>colors.pale,format=num}={}){
  const w=Math.min(116,850/Math.max(1,a.length)),start=75;
  return (label?tx(500,y-30,label):'')+a.map((v,j)=>`<g data-entity="${key}-${esc(v?.id??j)}">${rect(start+j*w,y,w-10,62,active(j)?'#ffe6ad':style(j))}${tx(start+j*w+(w-10)/2,y+38,format(v),'sim-number')}</g>${tx(start+j*w+(w-10)/2,y+88,j,'sim-number sim-slot-index')}`).join('');
 }
 function selection(m,f){
  const s=actual(f),k=m.kind;let b='';
  if(k==='two-array-cuts'){
   const row=(a,y,cut,key)=>slots(a,y,{label:key.toUpperCase()+' · cut '+cut,key})+`<g data-entity="cut-${key}">${line(70+Math.min(116,850/Math.max(1,a.length))*cut,y-12,70+Math.min(116,850/Math.max(1,a.length))*cut,y+70,colors.gold)}</g>`;
   b=row(s.a,100,s.i??0,'a')+row(s.b,260,s.j??0,'b');return wrap(b,'Two sorted arrays with moving partition cuts',400);
  }
  const a=s.records??s.values;if(!Array.isArray(a))return null;
  const v=a.map(x=>x?.v??x);const st=j=>k==='three-way-selection'?(j<s.lo||j>=s.hi?'#f2f3f4':j<s.lt?'#d4e8f2':j<s.i?'#d5ede1':j>=s.gt?'#f1e0ce':'#fff3d3'):k==='binary-boundary'?(j<s.lo?'#d4e8f2':j>=s.hi?'#d5ede1':colors.pale):j<(s.inspected??s.tested??0)?'#d5ede1':colors.pale;
  b=slots(a,110,{label:'Records · indices are zero-based',style:st,active:j=>j===(s.mid??s.index??s.active??s.i),format:x=>num(x?.v??x)});
  if(k==='binary-boundary'){const step=Math.min(116,850/Math.max(1,a.length)),mark=(v,label)=>`<g data-entity="boundary-${label}">${line(70+step*v,95,70+step*v,181,colors.gold)}${tx(70+step*v,45,label+' = '+v,'sim-number')}</g>`;b+=s.lo===s.hi?mark(s.lo,'lo = hi'):mark(s.lo,'lo')+mark(s.hi,'hi');}
  if(k==='rank-certificate'){
   const c=[['Less than key',s.less??0],['Equal to key',s.equal??0],['Greater than key',Math.max(0,(s.inspected??0)-(s.less??0)-(s.equal??0))],['Uninspected',Math.max(0,a.length-(s.inspected??0))]];b+=c.map(([name,n],j)=>`<g data-entity="class-${j}">${rect(75+j*217,265,202,95,j===1?'#d5ede1':colors.pale)}${tx(176+j*217,299,name)}${tx(176+j*217,336,n,'sim-number')}</g>`).join('');
  }else if(k==='weighted-mass'){
   const total=s.total||1;let x=75;b+=tx(500,255,'Cumulative probability weight · total '+num(s.total));a.forEach((r,j)=>{const width=850*r.w/total;b+=`<g data-entity="weight-${r.id??j}">${rect(x,285,width,50,r.v<=s.key?'#d5ede1':colors.pale)}${width>65?tx(x+width/2,317,r.w,'sim-number'):''}</g>`;x+=width;});b+=`<g data-entity="threshold">${line(75+850*(s.threshold??0)/total,275,75+850*(s.threshold??0)/total,350,colors.gold)}</g>`+tx(500,384,'Gold line: half of total weight');
  }else{
   const legend=k==='three-way-selection'?['Less','Equal','Unclassified','Greater']:k==='binary-boundary'?['Excluded left','Active interval','Excluded right']:['Inspected','Current test','Uninspected'],palette=k==='three-way-selection'?['#d4e8f2','#d5ede1','#fff3d3','#f1e0ce']:k==='binary-boundary'?['#d4e8f2',colors.pale,'#d5ede1']:['#d5ede1','#ffe6ad',colors.pale];b+=legend.map((l,j)=>rect(80+j*225,255,205,48,palette[j])+tx(182+j*225,286,l)).join('');
   if(s.result!==undefined&&s.result!==null)b+=tx(500,360,'Returned value: '+num(s.result),'sim-number');
  }
  return wrap(b,'Record classification with fixed indices',420);
 }
 function bytes(m,f){
  const s=actual(f);let b='';const rows=['source','destination'];const max=Math.max(...rows.map(r=>s[r]?.length||0),1),w=850/max;
  rows.forEach((row,r)=>{const y=100+r*190,arr=s[row]??[];b+=tx(500,y-54,row==='source'?'Source / pattern bytes':'Destination bytes');let zero=arr.indexOf(0);
   arr.forEach((v,j)=>{const x=75+j*w,reading=s.read?.row===row&&s.read.index===j,writing=s.write?.row===row&&s.write.index===j;const char=v===0?'\\0':v>=32&&v<=126?String.fromCharCode(v):'byte';b+=`<g data-entity="${row}-${j}">${rect(x,y,w-8,84,writing?'#ffe3ad':reading?'#cce5f2':zero>=0&&j>zero?'#f1f1f2':colors.pale)}${tx(x+(w-8)/2,y+29,char,'sim-code')}${tx(x+(w-8)/2,y+58,v,'sim-number')}${tx(x+(w-8)/2,y+112,j,'sim-number')}</g>`;if(reading||writing)b+=tx(x+(w-8)/2,y-10,writing?'WRITE':'READ');});
  });
  if(s.read&&s.write){const same=s.read.row===s.write.row,x1=75+(s.read.index+1)*w-18,x2=75+(s.write.index+1)*w-18,y1=s.read.row==='source'?184:374,y2=same?y1:s.write.row==='source'?184:290,route=same?y1+54:240;b+=`<path data-entity="byte-transfer" d="M${x1} ${y1} C${x1} ${route},${x2} ${route},${x2} ${y2}" fill="none" stroke="${colors.gold}" stroke-width="3" marker-end="url(#focus-arrow)"/>`;}
  b+=tx(500,455,'Blue: read · Gold: write · Gray: bytes beyond the first terminator');return wrap(b,'Addressed byte memory with separate read and write heads',490);
 }
 function stack(m,f){
  const s=actual(f),frames=s.stack??[],op=m.spec?.operation;let b=tx(285,50,'Live invocations · deepest frame is active'),h=Math.max(440,frames.length*88+125);
  const continuation=x=>op==='factorial'&&Number(x.n)>0?`Pending: ${x.n} × child return`:['fib','memo'].includes(op)&&Number(x.n)>1?'Pending: sum two child returns':op==='power'&&Number(x.n)>0?'Pending: square / multiply child result':op==='digits'?'Pending: add the last digit to child return':op==='around'?'Pending: output after the child returns':op==='subsets'?'Pending: complete include / exclude branch':'Pending: resume the saved continuation';
  frames.forEach((x,j)=>{const y=85+j*88;b+=`<g data-entity="frame-${x.id}">${rect(45,y,460,72,j===frames.length-1?'#cce5f2':colors.pale)}${tx(275,y+28,x.label,'sim-code')}${tx(275,y+55,j===frames.length-1?'Active invocation':continuation(x))}</g>`;if(j)b+=`<path d="M520 ${y-52}V${y+32}H507" fill="none" stroke="${colors.blue}" stroke-width="2" marker-end="url(#focus-arrow)"/>`;});
  if(!frames.length)b+=tx(275,140,'No live invocation');
  b+=tx(745,80,'Returned value')+rect(585,100,330,64,'#d5ede1')+tx(750,139,num(s.returned),'sim-number');
  const output=s.output??[];b+=tx(745,215,'Output is appended in execution order');const shown=output.slice(-8);shown.forEach((x,j)=>{const y=240+j*36;b+=tx(745,y,typeof x==='object'?JSON.stringify(x):x,'sim-code');});h=Math.max(h,output.length?shown.length*36+265:440);
  if(s.cache){const entries=Object.entries(s.cache);b+=tx(745,200,'Completed cache entries');entries.forEach(([k,v],j)=>{const x=580+(j%3)*114,y=225+Math.floor(j/3)*64;b+=`<g data-entity="cache-${k}">${rect(x,y,104,50,'#d5ede1')}${tx(x+52,y+32,k+' → '+v,'sim-number')}</g>`;});h=Math.max(h,300+Math.ceil(entries.length/3)*64);}
  if(s.chosen)b+=tx(745,h-35,'Current subset: {'+s.chosen.join(', ')+'}','sim-number');
  return wrap(b,'Call stack with explicit suspended work and returned value',h);
 }
 function callTree(m,f){
  const s=actual(f),all=m.frames.at(-1).snapshot?.nodes??[],visible=s.nodes??[],pos=new Map(),children=id=>all.filter(n=>n.parent===id);let leaf=0;
  const layout=n=>{const kids=children(n.id);const xs=kids.map(layout);const x=xs.length?xs.reduce((a,b)=>a+b,0)/xs.length:leaf++;pos.set(n.id,x);return x;};
  all.filter(n=>n.parent===null).forEach(layout);const spacing=850/Math.max(1,leaf),xof=n=>75+(pos.get(n.id)+.5)*spacing,yof=n=>85+n.d*100,maxDepth=Math.max(0,...all.map(n=>n.d));let b=tx(500,36,'Invocation tree · fixed node positions across the entire run');
  const byid=new Map(visible.map(n=>[n.id,n]));for(const n of visible){const parent=byid.get(n.parent);if(parent)b+=`<path data-entity="edge-${n.id}" d="M${xof(parent)} ${yof(parent)+58}L${xof(n)} ${yof(n)}" fill="none" stroke="${colors.blue}" stroke-width="2" marker-end="url(#focus-arrow)"/>`;}
  for(const n of visible){const x=xof(n),y=yof(n),active=n.id===s.stack?.at(-1)?.id;b+=`<g data-entity="node-${n.id}">${rect(x-42,y,84,58,active?'#cce5f2':n.done?'#d5ede1':colors.pale)}${tx(x,y+25,'n = '+n.n,'sim-number')}${tx(x,y+47,'call '+n.id)}</g>`;}
  b+=tx(500,85+(maxDepth+1)*100,'Blue: active invocation · Green: completed · Pale: suspended caller');return wrap(b,'Distinct invocation identities and connected caller–child edges',Math.max(350,130+(maxDepth+1)*100));
 }
 function interval(m,f){
  const s=actual(f),a=s.array??[],l=s.interval?.[0]??0,r=s.interval?.[1]??a.length,w=Math.min(116,850/Math.max(1,a.length));let b=tx(500,40,'Retained half-open interval ['+l+', '+r+')')+slots(a,135,{label:'',style:j=>j>=l&&j<r?'#cce5f2':'#f1f2f3',format:x=>x});
  const bound=(v,name,y)=>`<g data-entity="boundary-${name}">${line(70+w*v,105,70+w*v,210,colors.gold)}${tx(70+w*v,y,name+' = '+v,'sim-number')}</g>`;
  b+=bound(l,'left',85)+bound(r,'right',285);if(!a.length)b+=tx(500,165,'Empty input · no byte may be inspected');b+=tx(500,355,l===r?'Empty interval: apply the base-case contract.':'Only blue records remain candidates; gray records are excluded.');return wrap(b,'Recursive interval with explicit inclusive and exclusive boundaries',400);
 }
 function matrix(m,f){
  const s=actual(f),a=s.matrix;if(!Array.isArray(a)||!a.every(Array.isArray))return null;
  const k=m.kind,cols=Math.max(...a.map(r=>r.length)),cell=75;let b=tx(260,55,'Current matrix');
  const one=(matrix,x,y,key,selected)=>matrix.map((row,r)=>row.map((v,c)=>`<g data-entity="${key}-${r}-${c}">${rect(x+c*cell,y+r*cell,cell-8,cell-8,selected(r,c)?'#ffe3ad':colors.pale)}${tx(x+c*cell+(cell-8)/2,y+r*cell+42,v,'sim-number')}</g>`).join('')).join('');
  const select=(r,c)=>k==='cofactor-deletion'?r===s.row||c===s.column:k==='permutation-term-grid'?s.permutation?.[r]===c:k==='matrix-column-selection'?s.selected?.some(v=>v[0]===r&&v[1]===c):k==='cramer-column-replacement'?c===s.column:k==='adjugate-product-grid'?r===s.i:false;
  b+=one(a,85,85,'matrix',select);
  const other=s.minor??s.adjugate??s.coefficient??s.rowOperator??s.schur;
  if(Array.isArray(other)&&other.every(Array.isArray)){const name=s.minor?'Surviving minor':s.adjugate?'Adjugate':s.coefficient?'Original coefficient matrix':s.rowOperator?'Row operator':'Schur complement';b+=tx(730,55,name)+one(other,560,85,'companion',(r,c)=>k==='adjugate-product-grid'?c===s.j:false);}
  const y=Math.max(a.length,other?.length??0)*cell+130;
  if(k==='cofactor-deletion')b+=tx(500,y,'Gold: selected row and column are deleted; the companion keeps only survivors.');
  else if(k==='permutation-term-grid')b+=tx(500,y,'Gold: exactly one entry per row and column. Inversions determine the sign.');
  else if(k==='matrix-constraint-coupling')b+=tx(500,y,'Row sums: '+(s.rowSums??[]).join(', ')+' · Column sums: '+(s.columnSums??[]).join(', '),'sim-number');
  else b+=tx(500,y,'Read the operation and exact formula beside the matrices.');
  return wrap(b,'Matrix entries and their operation-dependent companion',Math.max(390,y+70));
 }
 function probability(m,f){
  const s=actual(f);let v,p;
  if(s.masses&&Array.isArray(s.masses)&&s.masses.every(x=>typeof x==='number')){p=s.masses;v=s.values??p.map((_,i)=>i);}
  else if(Array.isArray(s.law)){if(s.law.every(x=>typeof x==='number')){p=s.law;v=p.map((_,i)=>i);}else if(s.law.every(x=>x&&typeof x==='object')){v=s.law.map(x=>x.x??x.k??x.value??x.t);p=s.law.map(x=>x.mass??x.p??x.probability);}}
  if(!p||p.length>25||p.some(x=>!Number.isFinite(x))||v?.length!==p.length)return null;
  const top=Math.max(.05,...m.frames.flatMap(g=>{const q=actual(g);return Array.isArray(q.masses)?q.masses:Array.isArray(q.law)?q.law.map(x=>typeof x==='number'?x:x.mass??x.p??x.probability??0):[];})),extent=Math.max(1,...m.frames.map(g=>{const q=actual(g);return(q.masses??q.law??[]).length;})),w=800/extent;let b=tx(500,40,'Probability mass · axes are fixed across this replay');
  b+=line(90,320,920,320)+line(90,70,90,320);[0,.5,1].forEach(q=>{const y=320-240*q;b+=line(85,y,920,y,'#dce7ec')+tx(55,y+6,num(q*top),'sim-number');});
  p.forEach((x,j)=>{const h=240*x/top,split=s.successContributions?.[j],fail=s.failureContributions?.[j],valid=Number.isFinite(split)&&Number.isFinite(fail)&&Math.abs(split+fail-x)<1e-10;let bars=`<rect x="${100+j*w}" y="${320-h}" width="${w-12}" height="${h}" fill="${v[j]===(s.k??s.t)?'#e9c177':'#93bfcf'}" stroke="${colors.blue}"/>`;if(valid)bars=`<rect x="${100+j*w}" y="${320-240*fail/top}" width="${w-12}" height="${240*fail/top}" fill="#93bfcf"/><rect x="${100+j*w}" y="${320-h}" width="${w-12}" height="${240*split/top}" fill="#8dc6a8"/>`;b+=`<g data-entity="atom-${j}">${bars}${tx(100+j*w+(w-12)/2,350,v[j],'sim-number')}${p.length<=10?tx(100+j*w+(w-12)/2,320-h-12,num(x),'sim-number'):''}</g>`;});
  b+=tx(500,395,'Shown mass sum: '+num(p.reduce((a,b)=>a+b,0))+(s.tail!==undefined?' · Recorded remaining tail: '+num(s.tail):''),'sim-number');if(p.length>10)b+=tx(500,429,'Exact probability masses are listed in the explanation panel.');return wrap(b,'Discrete probability masses on fixed axes',455);
 }
 function expectation(m,f){
  const s=actual(f);if(m.kind==='signed-weighted-balance'){
   const c=s.contributions||[],max=Math.max(.1,...c.map(Math.abs)),w=800/Math.max(1,c.length);let b=tx(500,40,'Signed contributions · transformed value × probability')+line(100,215,900,215);
   c.forEach((x,j)=>{const h=150*Math.abs(x)/max,y=x>=0?215-h:215;b+=`<g data-entity="contribution-${j}"><rect x="${110+j*w}" y="${y}" width="${w-24}" height="${h}" fill="${x>=0?'#93c9b4':'#e1b28e'}" stroke="${colors.border}"/>${tx(110+j*w+(w-24)/2,x>=0?y-12:y+h+25,num(x),'sim-number')}${tx(110+j*w+(w-24)/2,405,'atom '+j)}</g>`;});b+=tx(500,460,'Accumulated so far: '+num(s.acc)+' · Complete expectation: '+num(s.mu),'sim-number');return wrap(b,'Signed probability-weighted accumulation',500);
  }
  if(m.kind==='occupancy-ball-placement'){
   let b=tx(500,40,'One realized allocation · expected quantities appear in the ledger'),w=820/s.counts.length;
   s.counts.forEach((n,j)=>{const x=90+j*w;b+=`<g data-entity="bin-${j}">${rect(x,95,w-20,230)}${tx(x+(w-20)/2,70,'Bin '+j)}${tx(x+(w-20)/2,365,'Count '+n,'sim-number')}`;for(let i=0;i<n;i++)b+=`<circle cx="${x+35+(i%4)*40}" cy="${295-Math.floor(i/4)*36}" r="12" fill="${colors.blue}"/>`;b+='</g>';});b+=tx(500,418,'Realized occupied bins: '+s.occupied+' · Realized collisions: '+s.collisions,'sim-number');return wrap(b,'Ball placement and realized occupancy',450);
  }
  return null;
 }
 function statistics(m,f){
  const s=actual(f),k=m.kind;
  if(k==='histogram-density'){
   const n=s.values.length,edges=s.edges,x0=edges[0],x1=edges.at(-1),X=x=>90+820*(x-x0)/(x1-x0),heights=s.counts.map((c,j)=>c/n/(edges[j+1]-edges[j])),max=Math.max(.01,...m.frames.flatMap(g=>{const q=actual(g);return q.counts.map((c,j)=>c/n/(edges[j+1]-edges[j]));}));let b=tx(500,38,'Density histogram · bin widths keep their actual numerical scale')+line(90,320,930,320)+line(90,65,90,320);
   [0,.5,1].forEach(q=>{const y=320-225*q;b+=line(90,y,930,y,'#dce7ec')+tx(48,y+6,num(q*max),'sim-number');});edges.forEach(x=>b+=tx(X(x),350,x,'sim-number'));
   heights.forEach((h,j)=>{const x=X(edges[j]),width=X(edges[j+1])-x;b+=`<g data-entity="bin-${j}"><rect x="${x}" y="${320-225*h/max}" width="${width}" height="${225*h/max}" fill="${j===s.bin?'#efcc8e':'#a5c7d6'}" stroke="${colors.blue}"/>${tx(x+width/2,320-225*h/max-13,'count '+s.counts[j])}</g>`;});b+=tx(500,399,'Current total area = inspected observations / final sample size','sim-number');return wrap(b,'Density heights, unequal bin widths and probability areas',440);
  }
  if(['squared-loss','absolute-loss'].includes(k)){
   const values=s.values,all=m.frames.flatMap(g=>[actual(g).center,...(actual(g).values??[])]).filter(Number.isFinite),lo=Math.min(...all)-1,hi=Math.max(...all)+1,X=x=>100+800*(x-lo)/(hi-lo),max=Math.max(1,...m.frames.flatMap(g=>actual(g).contributions??[]));let b=tx(500,38,'Center and observations · signed displacement precedes the loss')+line(100,110,900,110);
   values.forEach((x,j)=>{const yy=85-j%3*15;b+=`<g data-entity="observation-${j}"><circle cx="${X(x)}" cy="${yy}" r="6" fill="${colors.blue}"/>${tx(X(x),yy-15,x,'sim-number')}</g>`;b+=`<path data-entity="residual-${j}" d="M${X(s.center)} 165L${X(x)} ${yy+7}" stroke="${colors.border}" stroke-width="2" fill="none"/>`;});b+=`<g data-entity="center"><circle cx="${X(s.center)}" cy="165" r="8" fill="${colors.gold}"/>${tx(X(s.center),195,'center '+num(s.center),'sim-number')}</g>`;
   const w=800/values.length;(s.contributions??[]).forEach((c,j)=>{const h=150*c/max;b+=`<g data-entity="loss-${j}"><rect x="${110+j*w}" y="${385-h}" width="${w-20}" height="${h}" fill="#9bc6b6" stroke="${colors.green}"/>${tx(110+j*w+(w-20)/2,385-h-12,num(c),'sim-number')}${tx(110+j*w+(w-20)/2,413,'record '+j)}</g>`;});b+=line(100,385,900,385)+tx(500,464,'Total '+(k==='squared-loss'?'squared':'absolute')+' loss: '+num(s.loss),'sim-number');return wrap(b,'Residuals and their individual contributions to loss',500);
  }
  return null;
 }
 const frontierOrder=s=>s.algorithm==='dfs'?[...(s.frontier??[])].reverse():s.frontier??[];
 const frontierTitle=s=>['dls','ids'].includes(s.algorithm)?'Active recursion path · root to current caller':s.algorithm==='dfs'?'LIFO frontier · next removal is first':s.algorithm==='ucs'?'Priority frontier · lowest cost first; stable ties':'FIFO frontier · next removal is first';
 function graphLedger(m,f){
  const s=actual(f),front=frontierOrder(s),box=el('div');box.innerHTML=f.svg;const svg=box.querySelector('svg');
  // The checked graph and its edge ports are retained; replace the abbreviated
  // frontier with complete path-aware cards. DFS order is explicitly reversed.
  svg.querySelectorAll('[data-entity^="frontier-"]').forEach(n=>n.remove());for(const t of svg.querySelectorAll('text'))if(Number(t.getAttribute('y'))>390)t.remove();
  const pathLines=path=>{const lines=[];let line='';for(const state of path){const candidate=line?line+' → '+state:state;if(candidate.length>20&&line){lines.push(line+' →');line=state;}else line=candidate;}if(line)lines.push(line);return lines;};
  const records=m.frames.flatMap(g=>actual(g).frontier??[]),maxLines=Math.max(1,...records.map(n=>pathLines(n.path).length)),cardHeight=76+maxLines*24,rowStep=cardHeight+20,maxRows=Math.max(1,...m.frames.map(g=>Math.ceil((actual(g).frontier?.length??0)/4))),height=525+maxRows*rowStep;svg.setAttribute('viewBox','0 0 1000 '+height);
  let b=tx(500,425,frontierTitle(s));front.forEach((n,j)=>{const x=65+(j%4)*225,y=455+Math.floor(j/4)*rowStep,key=n.path.join('-')+'-'+n.cost;b+=`<g data-entity="frontier-${esc(key)}">${rect(x,y,210,cardHeight,j===0&&!['dls','ids'].includes(s.algorithm)?'#ffe3ad':colors.pale)}${tx(x+105,y+27,n.state+' · cost '+num(n.cost),'sim-number')}${tx(x+105,y+53,'depth '+n.depth,'sim-number')}${pathLines(n.path).map((l,k)=>tx(x+105,y+81+k*24,l,'sim-code')).join('')}</g>`;});if(!front.length)b+=tx(500,500,'No pending frontier record');b+=tx(500,height-34,'A path record includes state, cost, depth and history; it is not only a state.');const part=document.createElementNS(NS,'g');part.innerHTML=b;svg.append(part);return svg.outerHTML;
 }
 const rational=x=>typeof x==='string'&&x.includes('/')?x.split('/').map(Number).reduce((a,b)=>a/b):Number(x);
 function agent(m,f){
  const s=actual(f),k=m.kind;let b='';
  if(k==='belief-bars'){
   const p=rational(s.posteriorH),w=820;b=tx(500,40,s.branch+' · conditional belief')+tx(500,85,'Posterior distribution over hidden states');b+=`<g data-entity="belief-H">${rect(90,115,w*p,70,'#9fcbb7')}</g><g data-entity="belief-not-H">${rect(90+w*p,115,w*(1-p),70,'#b9d4e4')}</g>`;b+=tx(290,223,'P(H | branch) = '+s.posteriorH,'sim-number')+tx(720,223,'Other state = '+num(1-p),'sim-number');const q=rational(s.branchProbability);b+=tx(500,287,'Probability of observing this branch: '+s.branchProbability,'sim-number')+`<g data-entity="evidence-mass">${rect(90,310,w*q,42,'#ebcd93')}</g>`+line(90,360,910,360)+tx(500,403,'The evidence probability is not the posterior probability.');return wrap(b,'Posterior composition separated from evidence probability',445);
  }
  if(k==='utility-bars'||k==='discount-bars'){
   const keys=k==='utility-bars'?['safe','risky']:['A','B'],all=m.frames.flatMap(g=>keys.map(key=>rational(actual(g)[key]))),lo=Math.min(0,...all),hi=Math.max(1,...all),X=x=>200+680*(x-lo)/(hi-lo);b=tx(500,40,k==='utility-bars'?'Compare expected utilities under the stated objective':'Compare discounted returns on fixed axes')+line(X(0),75,X(0),325);keys.forEach((key,j)=>{const v=rational(s[key]),y=105+j*120;b+=tx(100,y+38,key)+`<g data-entity="utility-${key}">${rect(Math.min(X(0),X(v)),y,Math.abs(X(v)-X(0)),56,j?'#b9d4e4':'#9fcbb7')}${tx(530,y+87,s[key],'sim-number')}</g>`;});b+=tx(500,388,'Bar length encodes value; compare the exact rational values below each bar.');return wrap(b,'Expected or discounted utility comparison',430);
  }
  if(k==='vacuum-motion'){
   b=tx(500,40,'Two-room physical world · position and dirt are separate state variables');[s.leftDirt,s.rightDirt].forEach((dirty,j)=>{const x=85+j*445;b+=rect(x,90,385,250,'#f5f8fa')+tx(x+192,125,j?'Right room':'Left room');if(dirty)for(let i=0;i<3;i++)b+=`<g data-entity="dirt-${j}-${i}"><circle cx="${x+75+i*35}" cy="${300-(i%2)*12}" r="8" fill="#b58132"/></g>`;else b+=tx(x+192,302,'Clean');});const x=s.position==='L'?325:770;b+=`<g data-entity="vacuum-robot">${rect(x-46,195,92,65,'#b9d4e4')}<circle cx="${x-25}" cy="265" r="12" fill="${colors.ink}"/><circle cx="${x+25}" cy="265" r="12" fill="${colors.ink}"/>${tx(x,230,'Agent')}</g>`;b+=tx(500,398,'Accumulated action cost: '+s.cost,'sim-number');return wrap(b,'Vacuum movement, cleaning and accumulated cost',435);
  }
  return null;
 }
 function drawing(m,f){
  let svg=null,renderer='retained-geometry';
  if(['rank-certificate','linear-equality','binary-boundary','paired-extrema','three-way-selection','two-array-cuts','weighted-mass'].includes(m.kind)){svg=selection(m,f);renderer='record-regions';}
  else if(m.kind==='byte-memory'){svg=bytes(m,f);renderer='addressed-memory';}
  else if(m.kind==='recursion-stack'){svg=stack(m,f);renderer='continuation-stack';}
  else if(m.kind==='call-tree'){svg=callTree(m,f);renderer='fixed-invocation-tree';}
  else if(m.kind==='interval-shrink'){svg=interval(m,f);renderer='explicit-half-open-interval';}
  else if(['cofactor-deletion','permutation-term-grid','row-operation-matrix-ledger','adjugate-product-grid','cramer-column-replacement','matrix-column-selection','matrix-constraint-coupling','matrix-decomposition','matrix-row-reduction','matrix-symmetry-constraint'].includes(m.kind)){svg=matrix(m,f);renderer='matrix-companion';}
  else if(['binomial-count-recurrence','poisson-binomial-recurrence','geometric-wait','varying-hazard-wait','negative-binomial-stopping','poisson-mass-recurrence','urn-state-propagation'].includes(m.kind)){svg=probability(m,f);renderer='fixed-mass-axis';}
  else if(['signed-weighted-balance','occupancy-ball-placement'].includes(m.kind)){svg=expectation(m,f);renderer='signed-contribution-or-allocation';}
  else if(['histogram-density','squared-loss','absolute-loss'].includes(m.kind)){svg=statistics(m,f);renderer='density-or-residual-contributions';}
  else if(m.kind==='search-graph'){svg=graphLedger(m,f);renderer='graph-and-complete-frontier';}
  else if(['belief-bars','utility-bars','discount-bars','vacuum-motion'].includes(m.kind)){svg=agent(m,f);renderer='belief-utility-or-physical-world';}
  if(!svg){svg=f.svg;renderer='retained-geometry';}
  return {svg,renderer};
 }
 const preferred={a_select:['lo','hi','mid','lt','i','gt','target','less','equal','count','iterations','booleans','mass','threshold','result'],s_descriptive:['seen','count','center','loss','minimizer','mean','m2','energy','n','v','r','within','between','summary'],s_discrete:['trials','k','p','mass','tail','total','denominator','evidence','survivalBefore','survivalAfter','probability'],s_expectation:['k','acc','mu','total','positive','negative','absolute','signedPrefix','occupied','collisions','expected','variance','loss','tail'],l_det:['determinant','physicalArea','factor','cofactor','term','accumulator','entry','numerator','denominator','coordinate'],l_spaces:['rank','residual','inUnion','trace','dimension','choices','chosen','t'],i_agents:['stage','phase','prior','priorValue','signalValue','netValue','discount','A','B','posteriorH','branchProbability','counters','turn','cost','position','size'],i_uninformed:['algorithm','selected','expanded','generated','duplicates','stale','limit','nodes','leaves','paths','totalPaths','forwardDepth','backwardDepth'],p_strings:['reads','writes','comparisons','alignment','matchedPrefix','readIndex','writeIndex','left','right'],p_recursion:['calls','depth','ops','moves','phase','order','returned']};
 const names={lo:'Left boundary',hi:'Right boundary',mid:'Midpoint',lt:'Equal region begins',gt:'Greater region begins',i:'Scan cursor',count:'Recorded count',m2:'Residual energy M₂',v:'Population variance',n:'Sample / problem size',k:'Current threshold / count',acc:'Accumulated contribution',mu:'Complete mean',r:'Recorded parameter',p:'Recorded probability',prior:'Prior probability',posteriorH:'Posterior probability',ops:'Local operations',depth:'Maximum observed depth',calls:'Total invocations',factor:'Determinant multiplier',inUnion:'Membership in union',less:'Records less than key',equal:'Records equal to key',mass:'Current probability / weight mass',minimum:'Current minimum',maximum:'Current maximum',reads:'Bytes read',writes:'Bytes written',comparisons:'Byte comparisons',determinant:'Signed determinant',physicalArea:'Physical area'};
 function normalize(markup,hostID){
  const box=el('div');box.innerHTML=markup;const svg=box.querySelector('svg');if(!svg){if(!box.querySelector('math'))throw Error('Missing scientific drawing or mathematical derivation');box.className='sim-exact sim-math-proof';box.setAttribute('role','group');box.setAttribute('aria-label','Exact mathematical step');return box;}svg.classList.add('sim-exact');
  const ids=new Map();for(const n of svg.querySelectorAll('[id]')){const old=n.id,id=hostID+'-'+old;ids.set(old,id);n.id=id;}
  for(const n of svg.querySelectorAll('*'))for(const a of [...n.attributes]){let v=a.value;for(const [from,to]of ids){v=v.replaceAll('url(#'+from+')','url(#'+to+')');if(v==='#'+from)v='#'+to;}if(v!==a.value)n.setAttribute(a.name,v);}
  return svg;
 }
 function fit(svg){
  if(svg.tagName.toLowerCase()!=='svg')return;
  window.DiagramLayout?.finish(svg,{arrows:false,labels:true});
  // Pack multiple labels in a card only when real glyph bounds reveal a collision
  // or insufficient padding. Shapes and scientific coordinates are unchanged.
  for(const shape of svg.querySelectorAll('rect[data-layout-box],circle[data-layout-box]')){
   const allLabels=[...svg.querySelectorAll('text')].filter(t=>t.dataset.layoutLabelFor===shape.dataset.layoutBox),columns=[];
   for(const t of allLabels){const a=DiagramLayout.box(svg,t),x=a.x+a.w/2;let col=columns.find(c=>Math.abs(c.x-x)<4);if(!col){col={x,labels:[]};columns.push(col);}col.labels.push(t);}
   for(const {labels}of columns){if(labels.length<2)continue;
   const b=DiagramLayout.box(svg,shape),boxes=labels.map(t=>DiagramLayout.box(svg,t));
   const overlap=boxes.some((a,i)=>boxes.some((c,j)=>i<j&&Math.min(a.y+a.h,c.y+c.h)-Math.max(a.y,c.y)>-3));
   if(!overlap&&boxes.every(a=>a.y>=b.y+6&&a.y+a.h<=b.y+b.h-6))continue;
   labels.sort((a,c)=>DiagramLayout.box(svg,a).y-DiagramLayout.box(svg,c).y);
   const cell=(b.h-12)/labels.length;
   labels.forEach((t,j)=>{let a=DiagramLayout.box(svg,t),fs=parseFloat(getComputedStyle(t).fontSize);t.style.setProperty('font-size',Math.max(10,fs*Math.min(1,(cell-2)/a.h,(b.w-16)/a.w))+'px','important');a=DiagramLayout.box(svg,t);const dx=0,dy=b.y+6+(j+.5)*cell-a.y-a.h/2,m=svg.getScreenCTM().inverse().multiply(t.getScreenCTM()).inverse(),o=new DOMPoint(0,0).matrixTransform(m),d=new DOMPoint(dx,dy).matrixTransform(m);t.setAttribute('x',Number(t.getAttribute('x')??0)+d.x-o.x);t.setAttribute('y',Number(t.getAttribute('y')??0)+d.y-o.y);for(const n of t.querySelectorAll('tspan[x]'))n.setAttribute('x',Number(n.getAttribute('x'))+d.x-o.x);});
   }
  }
  // Fit labels inside their own rectangles without changing any scientific coordinates.
  for(const g of svg.querySelectorAll('[data-entity]')){const r=g.querySelector('rect');if(!r)continue;const rx=Number(r.getAttribute('x')),ry=Number(r.getAttribute('y')),rw=Number(r.getAttribute('width')),rh=Number(r.getAttribute('height'));
   for(const t of g.querySelectorAll('text')){const x=Number(t.getAttribute('x')),y=Number(t.getAttribute('y'));if(!(x>=rx&&x<=rx+rw&&y>=ry&&y<=ry+rh))continue;const b=t.getBBox(),available=Math.max(1,rw-20);if(b.width>available)t.style.setProperty('font-size',Math.max(10,parseFloat(getComputedStyle(t).fontSize)*available/b.width)+'px','important');}
  }
 }
  function insetEmptyLabels(svg){for(const t of svg.querySelectorAll('text[data-layout-label-for]')){if(t.textContent!=='empty')continue;const shape=[...svg.querySelectorAll('rect[data-layout-box]')].find(n=>n.dataset.layoutBox===t.dataset.layoutLabelFor);if(!shape)continue;const a=DiagramLayout.box(svg,t),b=DiagramLayout.box(svg,shape);if(Math.min(a.x-b.x,b.x+b.w-a.x-a.w)>=8)continue;const dx=b.x+b.w/2-a.x-a.w/2,m=svg.getScreenCTM().inverse().multiply(t.getScreenCTM()).inverse(),o=new DOMPoint(0,0).matrixTransform(m),d=new DOMPoint(dx,0).matrixTransform(m);t.setAttribute('x',Number(t.getAttribute('x')??0)+d.x-o.x);}}
 function pairGeometry(before,after,model){
   if(!before.viewBox||!after.viewBox)return []; // Native MathML steps do not have SVG geometry.
   if(before.viewBox.baseVal.width!==after.viewBox.baseVal.width||before.viewBox.baseVal.height!==after.viewBox.baseVal.height||model.kind==='median-groups')return []; // A camera or grouping change is a layout update, not physical record transit.
  const map=new Map([...before.querySelectorAll('[data-entity]')].map(n=>[n.dataset.entity,n])),pairs=[],seen=new WeakMap();
  // Entity descendants morph only when their structural signatures match.
  // External connectors require stable endpoint identities; rewiring is atomic.
  const add=(a,b)=>{if(!a||!b||a.tagName!==b.tagName)return;if(b.tagName.toLowerCase()==='path'&&['source','target','layoutSource','layoutTarget','net'].some(k=>a.dataset[k]!==b.dataset[k]))return;if(model.kind==='heap'&&!['text','tspan'].includes(b.tagName.toLowerCase()))return;for(const attr of ['x','y','x1','y1','x2','y2','cx','cy','r','width','height','points','d','transform']){const av=a.getAttribute(attr),bv=b.getAttribute(attr);if(av===null||bv===null||av===bv)continue;const pattern=/-?(?:\d*\.\d+|\d+\.?\d*)(?:e[-+]?\d+)?/ig,aa=(av.match(pattern)||[]).map(Number),bb=(bv.match(pattern)||[]).map(Number);if(aa.length&&aa.length===bb.length&&av.replace(pattern,'#')===bv.replace(pattern,'#')&&aa.every(Number.isFinite)&&bb.every(Number.isFinite)){if(!seen.has(b))seen.set(b,new Set());if(seen.get(b).has(attr))continue;seen.get(b).add(attr);pairs.push({node:b,attr,a:aa,b:bb,template:bv,target:bv});}}};
  for(const g of after.querySelectorAll('[data-entity]')){const old=map.get(g.dataset.entity);if(!old)continue;const a=[old,...old.querySelectorAll('*')],b=[g,...g.querySelectorAll('*')];if(a.length===b.length&&a.every((n,i)=>n.tagName===b[i].tagName))b.forEach((n,i)=>add(a[i],n));}
  const outside=svg=>[...svg.querySelectorAll('line,path,polyline,polygon')].filter(n=>!n.closest('[data-entity]')&&!n.closest('defs'));
  const key=n=>[n.tagName,n.dataset.source??n.dataset.layoutSource??'',n.dataset.target??n.dataset.layoutTarget??'',n.dataset.net??''].join('|');
  const linked=new Map(outside(before).filter(n=>n.dataset.source||n.dataset.layoutSource||n.dataset.net).map(n=>[key(n),n]));
  for(const n of outside(after)){const a=linked.get(key(n));if(a&&(n.dataset.source||n.dataset.layoutSource||n.dataset.net))add(a,n);} // A changed target is an atomic rewire, never an unattached moving tip.
  return pairs;
 }
 let serial=0, insertion=0;
 function structure(host){
  const controls=el('div',undefined,'sim-controls');for(const [key,label]of [['reset','Restart'],['prev','Previous'],['play','Play'],['next','Next']]){const b=el('button',label);b.type='button';b.dataset[key]='';controls.append(b);}
  const speed=el('select');speed.dataset.speed='';for(const [n,label]of [[4400,'Slow'],[2200,'Normal'],[1400,'Fast']]){const o=el('option',label);o.value=n;o.selected=n===2200;speed.append(o);}const label=el('label','Speed');label.append(speed);controls.append(label);
  const seek=el('input');seek.dataset.seek='';seek.type='range';seek.min=0;seek.step=1;seek.value=0;const checkpoint=el('label','Checkpoint');checkpoint.append(seek);controls.append(checkpoint);
  const stage=el('div',undefined,'sim-stage'),caption=el('p',undefined,'sim-caption'),formula=el('div',undefined,'sim-formula'),printRoot=el('div',undefined,'sim-print'),progress=el('p');progress.dataset.progress='';stage.tabIndex=0;caption.setAttribute('aria-live','polite');host.append(controls,stage,caption,formula,progress,printRoot);return {controls,stage,caption,formula,printRoot,progress};
 }
 function adaptRaw(o){
  players.filter(p=>!p.host.isConnected).forEach(p=>p.dispose());
  const {host}=o,oldControls=o.play?.parentElement;
  if(oldControls&&oldControls!==host&&oldControls.contains(o.prev)&&oldControls.contains(o.next))oldControls.remove();
  for(const n of [o.seek,o.speed,o.progress])if(n?.isConnected)n.remove();
  const temporary=el('div'),parts=structure(temporary);o.stage.before(parts.controls);o.stage.after(parts.progress);
  const formula=o.formula??parts.formula;if(!o.formula)host.append(formula);
  const printRoot=o.printRoot??parts.printRoot;if(!o.printRoot)host.append(printRoot);
  const model={...o.model,id:o.model.id??host.dataset.problemVisual??host.id??'model',title:o.model.title??o.model.reading??o.model.kind};
  return mount(host,model,{topic:location.pathname.split('/').at(-1).replace(/\.html$/,''),elements:{controls:parts.controls,stage:o.stage,caption:o.caption??parts.caption,formula,printRoot,progress:parts.progress},reading:model.reading??model.teachingPolicy?.reading??model.invariant??model.scope,retainDrawing:true});
 }
 function mount(host,model,{topic,prefix,elements,renderFrame,reading,retainDrawing=false}={}){
  const readingContract=reading??focus[model.kind]??model.reading??model.teachingPolicy?.reading??model.invariant??model.scope;
  if(!readingContract)throw Error('Missing concept-specific reading contract: '+model.kind);
  host.classList.add('sim-redesign');host.dataset.redesign='causal-replay-v1';host.dataset.modelKind=model.kind;
  host.querySelector('.teaching-panel')?.remove();host.querySelector('.sim-shell')?.remove();host.querySelector('.sim-timeline')?.remove();
  let {controls,stage,caption,formula,printRoot,progress}=elements??{controls:host.querySelector('.'+prefix+'-controls'),stage:host.querySelector('.'+prefix+'-stage'),caption:host.querySelector('.'+prefix+'-caption'),formula:host.querySelector('.'+prefix+'-formula'),printRoot:host.querySelector('.'+prefix+'-print')??host.querySelector('.'+prefix+'-print-trace'),progress:host.querySelector('[data-progress]')};
  if(!formula){formula=el('div',undefined,'sim-formula');host.append(formula);}if(!progress){progress=el('p');progress.dataset.progress='';host.append(progress);}
  if(!controls||!stage||!caption||!formula||!printRoot)throw Error('Incomplete player structure');
  controls.classList.add('sim-toolbar');stage.classList.add('sim-stage');caption.classList.add('sim-caption');formula.classList.add('sim-formula');printRoot.classList.add('sim-print');progress.classList.add('sim-live');
  const shell=el('div',undefined,'sim-shell'),visual=el('div',undefined,'sim-visual'),bar=el('div',undefined,'sim-viewbar'),teach=el('section',undefined,'sim-teaching'),phase=el('span','Exact checkpoint','sim-phase');teach.setAttribute('aria-label','Current operation and its explanation');
  const viewButtons={};for(const [key,label]of [['after','Result'],['before','Before'],['compare','Compare'],['reference','Original overview']]){const b=el('button',label);b.type='button';b.dataset.view=key;b.setAttribute('aria-pressed',String(key==='after'));bar.append(b);viewButtons[key]=b;}
  const zoom=el('button','Zoom');zoom.type='button';zoom.dataset.zoom='';zoom.setAttribute('aria-pressed','false');zoom.setAttribute('aria-label','Enlarge the diagram inside its bounded frame');zoom.onclick=()=>{const active=stage.dataset.zoomed!=='true';stage.dataset.zoomed=String(active);zoom.setAttribute('aria-pressed',String(active));zoom.textContent=active?'Fit':'Zoom';};bar.append(zoom,phase);visual.append(bar,stage,caption);const motionControl=el('div',undefined,'sim-motion-control'),motionLabel=el('label','Transition'),motionSeek=el('input');motionSeek.type='range';motionSeek.min=0;motionSeek.max=100;motionSeek.value=100;motionSeek.setAttribute('aria-label','Geometric progress between the previous and current exact checkpoints');motionLabel.append(motionSeek);const note=el('span','Exact state. Use Next to replay one operation.','sim-motion-note');motionControl.append(motionLabel,note);visual.append(motionControl);shell.append(visual,teach);controls.after(shell);
  const timeline=el('details',undefined,'sim-timeline'),list=el('ol',undefined,'sim-timeline-list');timeline.append(el('summary','Browse all operations'),list);shell.after(timeline);
  const play=host.querySelector('[data-play]'),prev=host.querySelector('[data-prev]'),next=host.querySelector('[data-next]'),reset=host.querySelector('[data-reset]'),seek=host.querySelector('[data-seek]'),speed=host.querySelector('[data-speed]');
  play.textContent='Play';prev.textContent='Previous';next.textContent='Next';reset.textContent='Restart';speed.replaceChildren();for(const [v,label]of [[4400,'Slow'],[2200,'Normal'],[1400,'Fast']]){const option=el('option',label);option.value=v;option.selected=v===2200;speed.append(option);}
  seek.max=model.frames.length-1;seek.setAttribute('aria-label',model.title+' exact checkpoint');speed.setAttribute('aria-label',model.title+' playback speed');
  const id='advanced-'+(++serial);let index=0,replayFrom=0,running=false,timer=null,raf=null,clock=null,continueMotion=null,pairs=[],affected=[],flows=[],recordRoutes=[],hiddenAnnotations=[],view='after',transition=1,disposed=false,detailsOpen=new Set();
  if(!host.id)host.id=document.getElementById('sim-'+model.id)?'sim-'+model.id+'-'+serial:'sim-'+model.id;
  const stops=()=>{clearTimeout(timer);timer=null;running=false;play.textContent='Play';play.setAttribute('aria-pressed','false');if(clock){const now=Number(clock.currentTime??0);clock.pause();clock.currentTime=now;setGeometry(Math.min(1,now/900));}if(raf)cancelAnimationFrame(raf);raf=null;syncPlay();};
  const cancelMotion=()=>{if(raf)cancelAnimationFrame(raf);raf=null;clock?.cancel();clock=null;continueMotion=null;};
  const exactCache=new Map();
  const exactView=(i,reference=false)=>{const key=i+'-'+reference;if(exactCache.has(key))return freshDrawing(exactCache.get(key));const svg=normalize(renderFrame?renderFrame(model.frames[i],i):reference||retainDrawing?model.frames[i].svg??model.frames[i].html:drawing(model,model.frames[i]).svg,id+'-'+i+'-'+(reference?'reference':'focus'));if(svg.tagName.toLowerCase()==='svg'){if(model.id==='dp-ramsey'){const graph=document.createElementNS(NS,'g');graph.setAttribute('transform','translate(0 40)');for(const n of [...svg.children])if(n.tagName.toLowerCase()!=='title'&&!(n.tagName.toLowerCase()==='text'&&n.textContent.startsWith('A same-color star')))graph.append(n);svg.append(graph);svg.setAttribute('viewBox','0 0 760 440');}const measuring=el('div',undefined,stage.className);measuring.style.cssText='position:fixed;left:-10000px;top:0;width:760px;visibility:hidden';measuring.append(svg);stage.parentElement.append(measuring);fit(svg);insetEmptyLabels(svg);svg.remove();measuring.remove();}exactCache.set(key,svg.cloneNode(true));return freshDrawing(svg);};
  // Every inserted copy has distinct marker/clip IDs, including printed and compare copies.
  function freshDrawing(node){const copy=node.cloneNode(true),suffix='-copy-'+(++insertion),ids=new Map();for(const n of copy.querySelectorAll('[id]')){ids.set(n.id,n.id+suffix);n.id+=suffix;}for(const n of [copy,...copy.querySelectorAll('*')])for(const a of [...n.attributes]){let value=a.value;for(const [old,id]of ids){value=value.replaceAll('url(#'+old+')','url(#'+id+')');if(value==='#'+old)value='#'+id;}if(value!==a.value)n.setAttribute(a.name,value);}return copy;}
  const syncPlay=()=>{const moving=clock?.playState==='running';play.textContent=running||moving?'Pause':'Play';play.setAttribute('aria-pressed',String(running||moving));host.dataset.playback=running?'playing':moving?'stepping':transition<1?'paused-transition':'paused';};
  function setGeometry(t){transition=t;const smooth=x=>x*x*(3-2*x),horizontal=smooth(Math.max(0,Math.min(1,(t-.25)/.5))),lift=t<.25?smooth(t/.25):t>.75?smooth((1-t)/.25):1;
   for(const n of hiddenAnnotations)n.style.visibility=t<1?'hidden':'';
for(const f of flows){const q=f.path.getPointAtLength(t*f.length);f.token.setAttribute('cx',q.x);f.token.setAttribute('cy',q.y);f.token.style.display=t<1?'':'none';}for(const p of pairs){let j=0;p.node.setAttribute(p.attr,t===1?p.target:p.template.replace(/-?(?:\d*\.\d+|\d+\.?\d*)(?:e[-+]?\d+)?/ig,()=>String(p.a[j]+(p.b[j]-p.a[j++])*(p.route?horizontal:t))));}for(const r of recordRoutes){if(t===1){if(r.base)r.node.setAttribute('transform',r.base);else r.node.removeAttribute('transform');}else{const base=r.transformPair?r.node.getAttribute('transform'):r.base;r.node.setAttribute('transform',(base||'')+' translate('+(r.axis==='y'?r.lane*lift:0)+' '+(r.axis==='x'?r.lane*lift:0)+')');}}// Empty-slot markers appear only after the traveling record vacates the slot.
   if(pairs.length){const svg=stage.querySelector('svg'),records=[...svg.querySelectorAll('[data-entity]>rect')].filter(r=>!r.parentElement.dataset.entity.startsWith('hole-')).map(r=>DiagramLayout.box(svg,r));for(const g of svg.querySelectorAll('[data-entity^="hole-"]')){const r=g.querySelector('rect');if(!r)continue;const b=DiagramLayout.box(svg,r),covered=records.some(a=>Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x)>1&&Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y)>1);g.style.visibility=t<1&&covered?'hidden':'';}}
   for(const n of affected)n.style.opacity=t===1?'':String(.45+.55*t);motionSeek.value=Math.round(t*100);phase.textContent=t===1?'Exact checkpoint':(replayFrom>index?'Reverse replay':flows.length?'Dependency / copy replay':pairs.length?'Geometric replay':'Operation emphasis')+' · '+Math.round(t*100)+'%';note.textContent=t===1?'Exact state. Values and counters belong to this checkpoint.':recordRoutes.length?'Records lift, travel in separate lanes, and settle into their target slots. Displayed values describe the target checkpoint; slot labels reappear after the movement.':'Highlighted objects are changing. Displayed numbers describe the target checkpoint; motion does not assert intermediate arithmetic values.';host.dataset.transition=String(t);}
  function animate(){if(reduced.matches||!stage.querySelector('svg')){setGeometry(1);return;}const svg=stage.querySelector('svg'),probe=document.createElementNS(NS,'rect');probe.setAttribute('width','0');probe.setAttribute('height','0');probe.setAttribute('aria-hidden','true');svg.append(probe);clock=probe.animate([{opacity:0},{opacity:0}],{duration:900,fill:'forwards'});clock.playbackRate=2200/Number(speed.value);setGeometry(0);syncPlay();const tick=()=>{if(!clock)return;const t=Math.min(1,Number(clock.currentTime??0)/900);setGeometry(t);if(t<1)raf=requestAnimationFrame(tick);else{clock.cancel();clock=null;probe.remove();raf=null;continueMotion=null;syncPlay();}};continueMotion=tick;raf=requestAnimationFrame(tick);}
  function readouts(s,old,shown){const metrics=el('div',undefined,'sim-metrics');const specific=model.kind==='signed-weighted-balance'?{k:'Current atom index'}:model.kind==='weighted-mass'?{mass:'Cumulative weight',threshold:'Half of total weight'}:model.kind==='geometric-wait'||model.kind==='varying-hazard-wait'?{k:'Current trial'}:{};const source=preferred[topic]?s:s.counters??s,previous=preferred[topic]?old:old.counters??old;for(const key of preferred[topic]??Object.keys(source).filter(k=>typeof source[k]!=='object').slice(0,10)){if(source[key]===undefined||source[key]===null||typeof source[key]==='object')continue;const box=el('div',undefined,'sim-metric');box.dataset.changed=String(shown>0&&JSON.stringify(previous[key])!==JSON.stringify(source[key]));box.append(el('span',specific[key]??(preferred[topic]?names[key]:undefined)??key.replace(/([a-z])([A-Z])/g,'$1 $2')),mathValue(source[key],true));metrics.append(box);}return metrics;}
  function details(key,title,content){const d=el('details');d.dataset.detail=key;d.open=detailsOpen.has(key);d.append(el('summary',title),content);d.ontoggle=()=>d.open?detailsOpen.add(key):detailsOpen.delete(key);return d;}
  function explain(){
   const shown=view==='before'?Math.max(0,index-1):index,f=model.frames[shown],s=actual(f),old=shown?actual(model.frames[shown-1]):{},t=window.TeachingTransitions?.metadata(model,f,shown)??f.teaching??{},changes=shown?diff(old,s):[];host.dataset.displayedFrame=shown;
   teach.replaceChildren();teach.dataset.explanation=t.why??f.caption;teach.append(el('p',shown?'Operation '+(shown+1)+' of '+model.frames.length:'Initial displayed checkpoint','sim-eyebrow'),el('h4',!t.operation||t.operation.length<24?f.caption:t.operation,'sim-operation'),el('p',t.why??f.caption,'sim-why'),readouts(s,old,shown));
   formula.innerHTML=f.formulaHtml??'';formula.hidden=!Boolean(f.formulaHtml?.trim());teach.append(formula);const checks=el('div',undefined,'sim-checks');for(const c of t.checks??[]){const row=el('div',undefined,'sim-check'),q=el('span');q.innerHTML=c.mathHtml;row.append(q,el('span',String(c.result),'sim-check-result'));checks.append(row);}teach.append(checks);
   if(t.testHtml){const test=el('div',undefined,'sim-check');test.innerHTML=t.testHtml;test.append(el('span',String(t.decision??''),'sim-check-result'));teach.append(test);}
   if(t.regions?.length){const regions=el('ul',undefined,'sim-regions');for(const r of t.regions){const item=el('li',r.label+' '),math=document.createElementNS(MNS,'math');math.innerHTML='<mrow><mo>[</mo><mn>'+esc(r.lo)+'</mn><mo>,</mo><mn>'+esc(r.hi)+'</mn><mo>)</mo></mrow>';item.append(math);regions.append(item);}teach.append(regions);}
   if(t.counterexample||f.counterexample)teach.append(el('p','Counterexample: this checkpoint belongs to the deliberately failing variant.','sim-counterexample'));
   teach.append(el('p',readingContract,'sim-focus'));if(!retainDrawing&&!renderFrame)teach.append(el('p','Numerical focus diagrams use up to seven significant digits; ≈ marks a rounded readout. Full stored values and the governing formulas are available below.','sim-numeric-note'));
  if(topic==='i_uninformed'&&model.kind==='search-graph'){
    const q=el('div'),head=el('p',frontierTitle(s));q.append(head);const table=el('table',undefined,'sim-delta');const tr=el('tr');['Order','State','Cost','Depth','Path'].forEach(x=>tr.append(el('th',x)));table.append(tr);for(const [j,x]of frontierOrder(s).entries()){const r=el('tr');[j+1,x.state,num(x.cost),x.depth,x.path?.join(' → ')].forEach(x=>r.append(el('td',String(x))));table.append(r);}q.append(table);if(!(s.frontier?.length))q.append(el('p','The frontier is empty at this checkpoint.'));detailsOpen.add('frontier');teach.append(details('frontier','Frontier and path records',q));
   }
   const law=s.masses??s.law;
   if(Array.isArray(law)&&law.length&&law.every(x=>typeof x==='number'||x&&typeof x==='object')){const wrap=el('div',undefined,'sim-delta-wrap'),table=el('table',undefined,'sim-delta'),head=el('tr');['Support value','Exact stored mass'].forEach(x=>head.append(el('th',x)));table.append(head);law.forEach((x,j)=>{const row=el('tr'),a=el('td'),b=el('td');a.append(mathValue(typeof x==='number'?s.values?.[j]??j:x.x??x.k??x.value??x.t??j));b.append(mathValue(typeof x==='number'?x:x.mass??x.p??x.probability));row.append(a,b);table.append(row);});wrap.append(table);teach.append(details('law','Exact probability masses',wrap));}
   const delta=el('div',undefined,'sim-delta-wrap'),table=el('table',undefined,'sim-delta');const header=el('tr');['Field','Before','After'].forEach(x=>header.append(el('th',x)));table.append(header);for(const c of changes){const tr=el('tr'),key=el('th');key.append(el('code',c.field));tr.append(key);for(const v of[c.before,c.after]){const td=el('td');td.append(mathValue(v));tr.append(td);}table.append(tr);}delta.append(table);if(!changes.length)delta.replaceChildren(el('p',shown?'This step tests or exposes the recorded state without changing its stored fields.':'There is no earlier displayed checkpoint. This is the starting state.'));teach.append(details('delta','Exact changes · '+changes.length+' fields',delta));
   const guide=el('div');if(t.reading)guide.append(el('p',t.reading));if(t.guide?.length){const code=el('ol');t.guide.forEach((x,j)=>{const item=el('li',x);if(j===t.activeLine)item.setAttribute('aria-current','step');code.append(item);});guide.append(code);}if(model.invariant)guide.append(el('p','Invariant: '+model.invariant));teach.append(details('guide','Reading guide and invariant',guide));teach.append(details('state','Full exact state',el('pre',JSON.stringify(s,null,2))));
   caption.textContent=f.caption;progress.textContent='Checkpoint '+(index+1)+' of '+model.frames.length+'. '+(view==='before'?'Showing checkpoint '+Math.max(1,index)+'.':view==='compare'?'Previous and current exact states are shown side by side.':'');seek.value=index;seek.setAttribute('aria-valuetext','Checkpoint '+(index+1)+' of '+model.frames.length);prev.disabled=index===0;next.disabled=index===model.frames.length-1;motionSeek.disabled=replayFrom===index||view!=='after'||reduced.matches||!stage.querySelector('svg');host.dataset.frame=index;host.dataset.checkpoint='ready';host.dataset.ready='true';host.dataset.renderer=renderFrame?'subject-specific-semantic-diagram':retainDrawing?'retained-domain-diagram':drawing(model,f).renderer;
   for(const [key,b]of Object.entries(viewButtons))b.setAttribute('aria-pressed',String(view===key));viewButtons.before.disabled=index===0;viewButtons.compare.disabled=index===0;for(const [j,b]of [...list.querySelectorAll('button')].entries()){if(j===index)b.setAttribute('aria-current','step');else b.removeAttribute('aria-current');}
  }
  function recordMovementRoutes(svg,before){
   if(!(['a_sort','a_select'].includes(topic)||model.kind==='concept:bars')||model.kind==='heap')return;
   const old=new Map([...before.querySelectorAll('[data-entity]')].map(n=>[n.dataset.entity,n])),translation=n=>{const q=n.getAttribute('transform');if(!q)return [0,0];const match=q.match(/^translate\(\s*(-?[\d.]+)[ ,]+(-?[\d.]+)\s*\)$/);return match?[+match[1],+match[2]]:null;};
   for(const g of svg.querySelectorAll('[data-entity]')){const a=old.get(g.dataset.entity),r=g.querySelector(':scope>rect'),oldRect=a?.querySelector(':scope>rect');if(!a||!r||!oldRect)continue;const A=translation(a),B=translation(g);if(!A||!B)continue;const dims=n=>['x','y','width','height'].map(k=>Number(n.getAttribute(k)));const [x,y,w,h]=dims(r),[ox,oy,ow,oh]=dims(oldRect),dx=x+B[0]-ox-A[0],dy=y+B[1]-oy-A[1],axis=Math.abs(dx)>=2&&Math.abs(dy)<.1?'x':Math.abs(dy)>=2&&Math.abs(dx)<.1?'y':null;if(!axis||w!==ow||h!==oh)continue;
    const related=pairs.filter(p=>p.node===g||g.contains(p.node));if(!related.length)continue;const lane=-Math.sign(axis==='x'?dx:dy)*((axis==='x'?h:w)+10),route={node:g,base:g.getAttribute('transform')??'',lane,axis,transformPair:related.some(p=>p.node===g&&p.attr==='transform')};related.forEach(p=>p.route=true);recordRoutes.push(route);
    const corridor={x:Math.min(x+B[0],ox+A[0])+(axis==='y'?Math.min(0,lane):0),y:Math.min(y+B[1],oy+A[1])+(axis==='x'?Math.min(0,lane):0),w:Math.abs(dx)+w+(axis==='y'?Math.abs(lane):0),h:Math.abs(dy)+h+(axis==='x'?Math.abs(lane):0)};
    for(const t of svg.querySelectorAll('text')){if(t.closest('[data-entity]')||t.closest('defs'))continue;const b=DiagramLayout.box(svg,t);if(Math.min(b.x+b.w,corridor.x+corridor.w)>Math.max(b.x,corridor.x)&&Math.min(b.y+b.h,corridor.y+corridor.h)>Math.max(b.y,corridor.y))hiddenAnnotations.push(t);}
   }
  }
  function dependencyFlows(svg,before){
   const nodes=new Map([...before.querySelectorAll('[data-entity]')].map(n=>[n.dataset.entity,n]));
   for(const path of svg.querySelectorAll('path[data-source-entity],path[data-net]')){
    const copied=path.dataset.sourceEntity&&nodes.has(path.dataset.sourceEntity)&&[...svg.querySelectorAll('[data-entity]')].some(n=>n.dataset.entity===path.dataset.targetEntity);
    const old=path.dataset.net?[...before.querySelectorAll('path[data-net]')].find(n=>n.dataset.net===path.dataset.net&&n.getAttribute('d')===path.getAttribute('d')):null;
    const established=old&&old.getAttribute('stroke')==='#c1cbd1'&&path.getAttribute('stroke')!=='#c1cbd1';if(!copied&&!established)continue;
    const length=path.getTotalLength();if(!length||!Number.isFinite(length))continue;const token=document.createElementNS(NS,'circle');token.setAttribute('r','4');token.setAttribute('fill','#b58132');token.dataset.dependencyToken='true';token.setAttribute('aria-hidden','true');svg.append(token);flows.push({path,length,token});
   }
  }
  function draw(i,withMotion=false){
   const origin=index;cancelMotion();index=Math.max(0,Math.min(model.frames.length-1,Math.trunc(i)));replayFrom=withMotion?origin:Math.max(0,index-1);stage.replaceChildren();pairs=[];affected=[];flows=[];recordRoutes=[];hiddenAnnotations=[];
   if(view==='compare'){
    const compare=el('div',undefined,'sim-compare');for(const [j,label]of[[Math.max(0,index-1),'Before · checkpoint '+Math.max(1,index)],[index,'After · checkpoint '+(index+1)]]){const figure=el('figure');figure.append(el('figcaption',label),exactView(j));compare.append(figure);}stage.append(compare);stage.querySelectorAll('svg').forEach(insetEmptyLabels);
   }else{const svg=exactView(view==='before'?Math.max(0,index-1):index,view==='reference');stage.append(svg);insetEmptyLabels(svg);if(replayFrom!==index&&view==='after'){const before=exactView(replayFrom);pairs=pairGeometry(before,svg,model);recordMovementRoutes(svg,before);if(replayFrom<index)dependencyFlows(svg,before);const old=new Map([...before.querySelectorAll('[data-entity]')].map(n=>[n.dataset.entity,n]));const signature=g=>[...g.querySelectorAll('*')].map(n=>[n.tagName,n.textContent,...['x','y','x1','y1','x2','y2','points','d','cx','cy','r','width','height','fill','stroke'].map(a=>n.getAttribute(a))]).map(JSON.stringify).join('|');affected=[...svg.querySelectorAll('[data-entity]')].filter(n=>!old.has(n.dataset.entity)||signature(n)!==signature(old.get(n.dataset.entity)));for(const n of affected)n.dataset.simChange='true';} }
   setGeometry(1);phase.textContent=view==='before'?'Previous exact checkpoint':view==='compare'?'Two exact checkpoints':'Exact checkpoint';explain();if(withMotion&&view==='after')animate();syncPlay();
  }
  function schedule(){if(!running||disposed)return;timer=setTimeout(()=>{if(index>=model.frames.length-1){stops();return;}draw(index+1,true);schedule();},Math.max(1400,Number(speed.value)||2200));}
  for(const [j,f]of model.frames.entries()){const b=el('button');b.type='button';b.append(el('b',String(j+1)),el('span',f.teaching?.operation??f.caption));b.onclick=()=>{stops();view='after';draw(j);};const item=el('li');item.append(b);list.append(item);}
  play.onclick=()=>{if(running||clock?.playState==='running'){stops();return;}players.forEach(p=>p.pause());if(index===model.frames.length-1&&transition===1){view='after';draw(0);}else if(view!=='after'){view='after';draw(index);}running=true;play.textContent='Pause';play.setAttribute('aria-pressed','true');if(clock&&clock.currentTime<900){clock.play();if(continueMotion)raf=requestAnimationFrame(continueMotion);}else if(transition<1&&stage.querySelector('svg')){const start=transition;animate();clock.currentTime=start*900;setGeometry(start);}syncPlay();schedule();};
  prev.onclick=()=>{stops();view='after';draw(index-1,true);};next.onclick=()=>{stops();view='after';draw(index+1,true);};reset.onclick=()=>{stops();view='after';draw(0);};seek.oninput=()=>{stops();view='after';draw(Number(seek.value));};speed.onchange=()=>{clock?.updatePlaybackRate(2200/Number(speed.value));if(running){clearTimeout(timer);schedule();}};
  for(const [key,b]of Object.entries(viewButtons))b.onclick=()=>{stops();view=key;draw(index);};motionSeek.oninput=()=>{const target=Number(motionSeek.value)/100;stops();cancelMotion();setGeometry(target);syncPlay();};
  host.onkeydown=e=>{if(e.target.closest('input,select,button,summary,textarea'))return;if(['ArrowLeft','ArrowRight','Home','End',' '].includes(e.key)){e.preventDefault();if(e.key===' ')play.click();else{stops();view='after';draw(e.key==='Home'?0:e.key==='End'?model.frames.length-1:index+(e.key==='ArrowRight'?1:-1));}}};
  function print(){printRoot.replaceChildren();model.frames.forEach((f,i)=>{const figure=el('figure');figure.append(exactView(i),el('figcaption','Checkpoint '+(i+1)+'. '+f.caption+' '+(f.teaching?.why??'')));const formula=el('div');formula.innerHTML=f.formulaHtml??'';figure.append(formula);printRoot.append(figure);});}
  const api={host,model,draw,show:i=>{stops();view='after';draw(i);},pause:stops,print,clearPrint:()=>printRoot.replaceChildren(),get index(){return index;},get replayFrom(){return replayFrom;},get running(){return running;},get transition(){return transition;},get motionPairs(){return pairs.length;},get recordRoutes(){return recordRoutes.length;},get dependencyFlows(){return flows.length;},teaching:{root:teach},dispose(){disposed=true;stops();cancelMotion();shell.remove();timeline.remove();const i=players.indexOf(api);if(i>=0)players.splice(i,1);}};
  draw(0);players.push(api);if(location.hash==='#'+host.id)queueMicrotask(()=>host.scrollIntoView({block:'start',behavior:'instant'}));return api;
 }
 addEventListener('beforeprint',()=>players.forEach(p=>p.print()));addEventListener('afterprint',()=>players.forEach(p=>p.clearPrint()));addEventListener('pagehide',()=>players.forEach(p=>p.pause()));document.addEventListener('visibilitychange',()=>{if(document.hidden)players.forEach(p=>p.pause());});reduced.addEventListener('change',()=>players.forEach(p=>{p.pause();p.show(p.index);}));
 window.AdvancedSimulations={mount,structure,adaptRaw,players,focus,drawing,difference:diff,state:actual};
})();
