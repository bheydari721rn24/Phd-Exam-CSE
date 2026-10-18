"""Finite binary CSP algorithms with explicit domains, queue direction and rollback."""
from collections import deque
from copy import deepcopy
from itertools import product

class CSP:
    def __init__(self, domains, constraints):
        self.variables=tuple(domains)
        if len(set(self.variables))!=len(self.variables):raise ValueError('Repeated variable')
        self.initial={v:list(values) for v,values in domains.items()}
        if any(not isinstance(v,str) or not v for v in self.variables):raise ValueError('Use nonempty string variable names')
        if any(type(a)is not int for values in self.initial.values() for a in values):raise ValueError('Teaching domains use integer values')
        if any(len(values)!=len(set(values)) for values in self.initial.values()):raise ValueError('Domains must contain distinct values')
        self.relations={};self.labels={};self.neighbors={v:[] for v in self.variables}
        for c in constraints:
            x,y=c['x'],c['y']
            if x not in domains or y not in domains or x==y:raise ValueError('Use distinct declared endpoints')
            allowed={tuple(p) for p in c['allowed']}
            if any(len(p)!=2 or p[0]not in domains[x]or p[1]not in domains[y]for p in allowed):raise ValueError('Relation tuple outside its original domains')
            if (x,y)in self.relations:allowed&=self.relations[x,y]
            self.relations[x,y]=allowed;self.relations[y,x]={(b,a)for a,b in allowed}
            self.labels[x,y]=c.get('label',x+' ~ '+y);self.labels[y,x]=self.labels[x,y]
        for x,y in self.relations:
            if y not in self.neighbors[x]:self.neighbors[x].append(y)
        for x in self.variables:self.neighbors[x].sort(key=self.variables.index)
    def arcs(self):
        return [(x,y)for x in self.variables for y in self.neighbors[x]]
    def valid(self,assignment):
        if any(x not in self.initial for x in assignment):return False
        return all(x not in assignment or assignment[x]in self.initial[x]for x in self.variables)and all(x not in assignment or y not in assignment or (assignment[x],assignment[y])in allowed for (x,y),allowed in self.relations.items())

def ac3(csp, domains=None, queue=None, record=True):
    """Mutate the supplied branch domains; True means arc consistency, not SAT."""
    D=deepcopy(csp.initial)if domains is None else domains
    Q=deque(dict.fromkeys(tuple(a)for a in(csp.arcs()if queue is None else queue)))
    queued=set(Q)
    if any((x,y)not in csp.relations for x,y in Q):raise ValueError('Queue contains a nonconstraint arc')
    events=[];checks=0
    def emit(kind,why,arc=None,removed=None,supports=None,before=None):
        if record:events.append({'kind':kind,'why':why,'arc':list(arc)if arc else None,'domains':deepcopy(D),'queue':[list(q)for q in Q],'removed':removed or[],'supports':supports or[],'before':before,'pairChecks':checks})
    emit('initial','Every displayed column is a variable domain. Queue entries are directed support tests.')
    if any(not D[v]for v in csp.variables):
        emit('failure','An initially empty domain is impossible, even when its variable is isolated.');return False,D,events
    while Q:
        x,y=Q.popleft();queued.remove((x,y));before=deepcopy(D)if record else None;allowed=csp.relations[x,y];removed=[];supports=[]
        for a in list(D[x]):
            witness=None
            for b in D[y]:
                checks+=1
                if (a,b)in allowed:witness=b;break
            supports.append({'tail':a,'head':witness})
            if witness is None:D[x].remove(a);removed.append(a)
        emit('revise','Inspect support in the head domain; delete only unsupported tail values.',(x,y),removed,supports,before)
        if removed:
            if not D[x]:emit('failure','This branch has no solution because its tail domain is empty.',(x,y));return False,D,events
            for z in csp.neighbors[x]:
                if z!=y and (z,x)not in queued:Q.append((z,x));queued.add((z,x))
            emit('requeue','A changed domain can invalidate supports in existing incoming neighboring arcs.',(x,y))
    emit('fixed-point','All queued support tests have stabilized. Nonempty arc-consistent domains alone do not prove satisfiability.')
    return True,D,events

def solve(csp, mode='mac', all_solutions=True):
    """Branch copying gives exact rollback; MRV, residual degree, then input order."""
    if mode not in ('plain','fc','mac'):raise ValueError('Unknown mode')
    answers=[]
    def visit(assignment,D):
        if any(not D[v]for v in csp.variables):return False
        if len(assignment)==len(csp.variables):
            if csp.valid(assignment):answers.append(dict(assignment));return not all_solutions
            return False
        remaining=[v for v in csp.variables if v not in assignment]
        x=min(remaining,key=lambda v:(len(D[v]),-sum(z not in assignment for z in csp.neighbors[v]),csp.variables.index(v)))
        for a in D[x]:
            branch=dict(assignment);branch[x]=a
            if not csp.valid(branch):continue
            child=deepcopy(D);child[x]=[a]
            if mode=='mac':ok,child,_=ac3(csp,child,[(z,x)for z in csp.neighbors[x]],False)
            elif mode=='fc':
                ok=True
                for z in csp.neighbors[x]:
                    if z in branch:continue
                    child[z]=[b for b in child[z]if (b,a)in csp.relations[z,x]]
                    if not child[z]:ok=False;break
            elif mode=='plain':ok=True
            else:raise ValueError('Unknown mode')
            if ok and visit(branch,child):return True
        return False
    D=deepcopy(csp.initial)
    if mode=='mac':
        ok,D,_=ac3(csp,D,record=False)
        if not ok:return answers
    visit({},D);return answers

def brute_force(csp):
    return [dict(zip(csp.variables,values))for values in product(*(csp.initial[v]for v in csp.variables))if csp.valid(dict(zip(csp.variables,values)))]

def relation(x,y,dx,dy,predicate,label=None):
    return {'x':x,'y':y,'allowed':[[a,b]for a in dx for b in dy if predicate(a,b)],'label':label or x+' ~ '+y}

def instance(domains,predicates):
    """Build an explicit finite relation table from declared mathematical rules."""
    return CSP(domains,[relation(x,y,domains[x],domains[y],f,label)for x,y,f,label in predicates])
