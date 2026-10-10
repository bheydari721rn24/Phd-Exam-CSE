from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/d_recurrence.js';s=p.read_text(encoding='utf-8')
s=s.replace("b+=line([from,to],C.active,true);", "if(mapping[mapping[i]-1]===i+1){const mid=[(from[0]+to[0])/2-18*dy/d,(from[1]+to[1])/2+18*dx/d];b+=`<path d=\"M${from[0]} ${from[1]} Q${mid[0]} ${mid[1]} ${to[0]} ${to[1]}\" fill=\"none\" stroke=\"${C.active}\" stroke-width=\"2\" marker-end=\"url(#rc-arrow)\"/>`;}else b+=line([from,to],C.active,true);")
s=s.replace("'All image choices: '+(z.two??0)+' + '+(z.long??0)+' = '+z.value", "z.step<2?'Boundary D = '+z.value:'All image choices: '+z.two+' + '+z.long+' = '+z.value")
s=s.replace("'Forcing injected at j, propagated to the target index'", "'Earlier forcing contributions; bar heights show absolute magnitudes'")
s=s.replace("'Length '+z.step+': u is one restricted-ending count; v ends in two'", "'Length '+z.step+': restricted-ending state and unrestricted-ending state'")
s=s.replace("'Normalized values u = a / 2 to the index power'", "'Normalized sequence after division by the exponential base power'")
s=s.replace("'Current exact a = '+z.value+'; second difference = '", "'Exact term = '+z.value+'; second difference = '")
s=s.replace("'Exact companion update: (a, b) becomes (5a − 6b, a)'", "'Exact companion update from two preceding values'")
f=r'''function frameFormula(s,z,r){const n=z.step;
 if(s.operation==='unrolling')return 'W_{'+n+'}='+z.sum;
 if(s.operation==='differences')return '\\Delta^{'+n+'}q(n)'+(n===2?'=2':n===3?'=0':'');
 if(s.operation==='boundary')return 'a_0=4,\\quad a_1=5,\\quad a_n=6\\cdot2^{n-2}\\quad(n\\ge2)';
 if(s.operation==='tiling')return 'T_{'+s.n+'}=T_{'+(s.n-1)+'}+T_{'+(s.n-2)+'}='+r.vertical+'+'+r.horizontal+'='+r.count;
 if(s.operation==='resonance')return 'u_{'+n+'}=\\frac{'+n+'('+n+'-1)}{2},\\quad a_{'+n+'}='+z.value;
 if(s.operation==='automaton')return 'u_{n+1}=u_n+v_n,\\quad v_{n+1}=2u_n+v_n';
 if(s.operation==='derangements')return n<2?'D_{'+n+'}='+z.value:'D_{'+n+'}=('+n+'-1)(D_{'+(n-1)+'}+D_{'+(n-2)+'})='+z.value;
 if(s.operation==='partitions')return 'S(n,k)=S(n-1,k-1)+kS(n-1,k)';
 if(s.operation==='ferrers')return 'p('+s.n+',3)=p('+(s.n-1)+',2)+p('+(s.n-3)+',3)='+r.withOne+'+'+r.withoutOne+'='+r.count;
 if(s.operation==='catalan')return 'C_{'+s.n+'}=\\sum_{j=0}^{'+(s.n-1)+'}C_jC_{'+(s.n-1)+'-j}='+r.count;
 if(s.operation==='modular')return 'F_{'+n+'}\\equiv '+z.u+'\\pmod{'+s.modulus+'},\\quad F_{'+(n+1)+'}\\equiv '+z.v+'\\pmod{'+s.modulus+'}';
 return '(a_{'+n+'},a_{'+(n-1)+'})=('+z.a+','+z.b+')';
}
'''
# Raw insertion uses two source slashes to produce one mathematical command slash at runtime.
assert 'function frameFormula'not in s;s=s.replace('function makeModel(id,title,raw){',f+'function makeModel(id,title,raw){').replace("formula:'',snapshot:","formula:frameFormula(s,z,r),snapshot:")
p.write_text(s,encoding='utf-8');print('Added exact native-math formulas, separated opposite cycle arrows and corrected boundary captions.')
