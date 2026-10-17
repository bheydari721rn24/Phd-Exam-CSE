"""Exact, compact problem-specific probability figures; no random scene aliases."""
from conditional_problem_figures import figure,cells,text
from fractions import Fraction as F

def masses(title,rows,caption):
 body=''
 for i,(name,prior,like,joint,post)in enumerate(rows):
  y=110+i*49
  for x,s in zip([25,190,325,460,595],[name,prior,like,joint,post]):body+=text(x,y,s,x!=25)
 for x,s in zip([25,190,325,460,595],['State','Prior','Likelihood','Joint mass','Posterior']):body+=text(x,76,s)
 return figure(title,body,caption+' Column values carry the probabilities; row heights are schematic.')

def density(kind):
 # Equal horizontal and vertical scales are shared within this one panel.
 f={'head':lambda x:2*x,'mixed':lambda x:12*x*x*(1-x),'nonuniform':lambda x:6*x*(1-x),'three':lambda x:4*x**3}[kind]
 title={'head':'One head: density 2θ','mixed':'HHT: density 12θ²(1 − θ)','nonuniform':'Nonuniform prior, then one tail','three':'Three heads: density 4θ³'}[kind]
 body='<path d="M55 280H390M55 280V64" stroke="#869e94" fill="none"/>'
 pts=' '.join(f'{55+335*j/100},{280-50*f(j/100)}'for j in range(101))
 body+='<polyline points="'+pts+'" fill="none" stroke="#17636a" stroke-width="3"/>'+text(46,305,'0',True)+text(380,305,'1',True)+text(23,84,'4',True)+text(135,316,'Rate θ; vertical axis is density',True)
 notes={'head':['Normalized integral: 1','Area for θ > 1/2: 3/4','Predictive mean: 2/3'],'mixed':['Normalized integral: 1','Prior: uniform','Predictive mean: 3/5'],'nonuniform':['Normalized integral: 1','Prior density: 2θ','Predictive mean: 1/2'],'three':['Density at 9/10: 729/250','Tail above 9/10: 3439/10000','Point probability: 0']}[kind]
 for i,s in enumerate(notes):body+=text(420,105+50*i,s,True)
 if kind in['head','three']:
  lo=.5 if kind=='head'else .9
  pts=f'{55+335*lo},280 '+' '.join(f'{55+335*(lo+(1-lo)*j/50)},{280-50*f(lo+(1-lo)*j/50)}'for j in range(51))+' 390,280'
  body='<polygon points="'+pts+'" fill="#b8d7c9" opacity="0.8"/>'+body
 return figure(title,body,'The filled region, when present, is the requested parameter tail. A curve height is a density, not a point probability. The graph uses fifty drawing units per density unit and335per horizontal unit; these are different physical dimensions.')

def get(id):
 models={
 'SB01':('Three sources after the same alert',[('Source 1','1/2','1/10','3/60','3/13'),('Source 2','1/3','1/5','4/60','4/13'),('Source 3','1/6','3/5','6/60','6/13')],'Evidence mass is13/60.'),
 'SB02':('Two factories: output share is part of the model',[('Factory 1','3/4','1/50','3/200','3/8'),('Factory 2','1/4','1/10','5/200','5/8')],'Evidence mass is8/200.'),
 'SB03':('Every column is conditional on subgroup C',[('Source 1','2/3','1/4','2/12','2/5'),('Source 2','1/3','3/4','3/12','3/5')],'Evidence within C is5/12; population priors are not used.'),
 'SB04':('Disjoint cells resolve the overlap',[('Both A and B','1/5','1','8/40','8/15'),('A only','1/5','1/2','4/40','4/15'),('B only','3/10','1/4','3/40','3/15'),('Neither','3/10','0','0','0')],'A comprises the first two rows, so its posterior is12/15.'),
 'SB10':('Eligibility after observing two second-round heads',[('K = 2','6/16','1/4','12/128','4/9'),('K = 3','4/16','3/8','12/128','4/9'),('K = 4','1/16','6/16','3/128','1/9')],'K below two has zero likelihood. The evidence mass is27/128.'),
 'SB22':('History-specific joint report likelihoods',[('Target','1/3','3/8','1/8','1/2'),('Background','2/3','3/16','1/8','1/2')],'The likelihood column multiplies the first-positive likelihood by the second-positive likelihood given the first.'),
 'SB23':('One coin remains fixed across three heads',[('Fair coin','1/2','125/1000','125/2000','125/854'),('Biased coin','1/2','729/1000','729/2000','729/854')],'Posterior prediction weights1/2and9/10by the last column.'),
 'SB26':('Without-replacement RR likelihoods identify the urn',[('Urn A','1/2','12/30','12/60','6/7'),('Urn B','1/2','2/30','2/60','1/7')],'The second draw uses five remaining objects in each urn.'),
 'SB28':('Unequal priors and an HHT history',[('Type 1','2/3','3/64','2/64','2/5'),('Type 2','1/3','9/64','3/64','3/5')],'Evidence mass is5/64; predictive likelihoods are1/4and3/4.'),
 'SB29':('First success on trial three means TTH',[('Rate 1/2','1/2','8/64','8/128','8/11'),('Rate 3/4','1/2','3/64','3/128','3/11')],'The count event has three times each likelihood, so its posterior coincides here although its evidence probability differs.'),
 'SB31':('Uniformly observed child, not a family existential report',[('BB','1/4','1','2/8','1/2'),('BG','1/4','1/2','1/8','1/4'),('GB','1/4','1/2','1/8','1/4'),('GG','1/4','0','0','0')],'Likelihoods for the at-least-one report would instead be1,1,1,0.'),
 'SB34':('Informed host: the exact opening of door three',[('Prize 1','1/3','1/4','1/12','1/5'),('Prize 2','1/3','1','4/12','4/5'),('Prize 3','1/3','0','0','0')],'Switching wins exactly when prize2is true after this report.'),
 'SB35':('Ignorant host: door three opened and empty',[('Prize 1','1/3','1/2','1/6','1/2'),('Prize 2','1/3','1/2','1/6','1/2'),('Prize 3','1/3','0','0','0')],'Opening and emptiness are both included in the report likelihood.'),
 'SB36':('Uniform pairs, then equal-weight filtering',[('HH','1/45','1','1/45','1/29'),('HL','16/45','0','0','0'),('LL','28/45','1','28/45','28/29')],'Pair multiplicities determine priors. Heavy and light denote two distinct common weights.'),
 'SB37':('A visible red face weights cards unequally',[('RR','1/3','1','2/6','2/3'),('RB','1/3','1/2','1/6','1/3'),('BB','1/3','0','0','0')],'Each of the six card-face positions was equally likely before the visible color was known.'),
 'SB49':('Likelihood and posterior optimize different columns',[('Class 1','9/10','1/5','9/50','9/13'),('Class 2','1/10','4/5','4/50','4/13')],'The second likelihood is larger, but the first posterior is larger.')}
 if id in models:return masses(*models[id])
 if id=='SB07':return cells('Recover and verify all four joint cells',[('H and E','5/40','E likelihood: 5/8'),('H and not E','3/40','H total: 8/40'),('Not H and E','5/40','E likelihood: 5/32'),('Neither','27/40','Not H total: 32/40')],'The evidence total is10/40. Divide an evidence cell by its class total for a forward likelihood, or by the evidence total for a posterior.')
 if id in['SB11','SB12']:return cells('Exact synthetic population of two thousand',[('Target, alert','18','Target total: 20'),('Background, alert','99','Background: 1980'),('Target, no alert','2','No-alert total: 1883'),('Background, no alert','1881','Alert total: 117')],'These are scaled model weights. Credibility uses a report total; accuracy adds the first and fourth cells. The boxes are not drawn proportional to counts.')
 if id=='SB21':return cells('Different report mechanisms give different posteriors',[('One positive','4/13','Likelihood ratio: 4'),('Independent pair','16/25','Joint ratio: 16'),('One report copied','4/13','Joint ratio: 4')],'The copy adds no evidence conditional on the first positive. Independent repetition needs independence inside both hypotheses.')
 if id=='SB25':return cells('Count and sequence differ by a common factor',[('Count, type 1','40/243','Exactly three heads'),('Count, type 2','80/243','Exactly three heads'),('Sequence, type 1','4/243','One specified order'),('Sequence, type 2','8/243','One specified order')],'All entries are likelihoods. The shared factor ten cancels from the posterior but multiplies the absolute evidence probability.')
 if id=='SB33':return cells('Six families supply ten selectable children',[('Size-one families','3 families','Supply 3 children'),('Size-two families','2 families','Supply 4 children'),('Size-three families','1 family','Supply 3 children')],'This exact finite population realizes the specified family proportions. A uniformly selected child sees family-size weights3/10,4/10,3/10.')
 if id=='SB40':return cells('A coarse report is an evidence-weighted mixture',[('Report 1','Mass 1/5','Target share: 1/4'),('Report 2','Mass 3/10','Target share: 3/4'),('Union report','Mass 1/2','Target share: 11/20')],'The reports are disjoint. Conditional mixture weights inside their union are2/5and3/5, not one half each.')
 if id=='SB48':return cells('Two admissible dependence tables with the same marginals',[('Class 1: ++','1/2','Mixed cells: 1/4 each'),('Class 1: −−','0','Both marginals: 3/4'),('Class 2: ++','3/4','Mixed cells: 0'),('Class 2: −−','1/4','Both marginals: 3/4')],'Equal individual-report likelihoods do not imply equal two-report likelihoods. Equal priors and the ++ report give class1posterior2/5.')
 if id in['SB50','SB51','SB53']:
  rows={'SB50':[('Choose target','Risk 11/13','Cost: false positive 1'),('Choose background','Risk 18/13','Cost: false negative 9')],'SB51':[('At LR = 19/4','Posterior 1/5','Prior odds: 1/19'),('Choose target','Risk 8/5','Ties at threshold'),('Choose background','Risk 8/5','Ties at threshold')],'SB53':[('Choose target','Risk 2/5','Wrong-label loss 1'),('Choose background','Risk 3/5','Wrong-label loss 1'),('Abstain','Risk 1/4','Constant action cost')]}[id]
  return cells('Evaluate posterior risk for every allowed action',rows,'The smallest risk determines an optimal action. Risks have loss units and need not be probabilities. Changing costs or allowed actions leaves the posterior unchanged.')
 if id in['SB56','SB57','SB58','SB61']:return density({'SB56':'head','SB57':'mixed','SB58':'nonuniform','SB61':'three'}[id])
 return ''
