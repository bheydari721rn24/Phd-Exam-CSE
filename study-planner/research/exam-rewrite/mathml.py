"""Strict native MathML renderer for the revision's controlled TeX notation."""
import re,html,xml.etree.ElementTree as ET
SYMBOLS=dict(zip('Rightarrow Leftrightarrow forall exists land lor neg oplus equiv cdot in le ge ne Theta Omega alpha beta delta epsilon phi pi sigma omega cup cap subseteq subset times varnothing mid pm to mapsto iff notin wedge vee sum prod bigwedge bigvee'.split(),'⇒ ⇔ ∀ ∃ ∧ ∨ ¬ ⊕ ≡ · ∈ ≤ ≥ ≠ Θ Ω α β δ ε φ π σ ω ∪ ∩ ⊆ ⊂ × ∅ ∣ ± → ↦ ⇔ ∉ ∧ ∨ ∑ ∏ ⋀ ⋁'.split()))
SYMBOLS.update(setminus='∖',nmid='∤',omega='ω',infty='∞',limsup='lim sup',liminf='lim inf',lceil='⌈',rceil='⌉',lfloor='⌊',rfloor='⌋',leq='≤',geq='≥',neq='≠')
SYMBOLS.update(bigcup='⋃',bigcap='⋂',perp='⊥',langle='⟨',rangle='⟩',Vert='‖',vert='|',emptyset='∅',approx='≈',sim='∼',otimes='⊗',partial='∂')
SYMBOLS.update({'theta':'θ','lambda':'λ','mu':'μ','rho':'ρ','tau':'τ','varepsilon':'ε'})
SYMBOLS['int']='∫'
SYMBOLS['circ']='∘'
SYMBOLS['varphi']='ϕ'
SYMBOLS['leftarrow']='←'
SYMBOLS['subsetneq']='⊊'
SYMBOLS['triangle']='△'
SYMBOLS.update(Delta='Δ',kappa='κ')
def tag(t,s):return '<'+t+'>'+s+'</'+t+'>'
def atom(t,s):return tag(t,html.escape(s))
class Parser:
 def __init__(self,s):self.s=s;self.i=0
 def skip(self):
  while self.i<len(self.s) and self.s[self.i].isspace():self.i+=1
 def group(self):
  self.skip()
  if self.i<len(self.s) and self.s[self.i]=='{':
   self.i+=1;r=self.seq('}');assert self.i<len(self.s) and self.s[self.i]=='}',self.s;self.i+=1;return r
  if self.i<len(self.s) and self.s[self.i].isdigit():
   c=self.s[self.i];self.i+=1;return atom('mn',c)
  return self.base()
 def base(self):
  self.skip();assert self.i<len(self.s),self.s
  c=self.s[self.i];self.i+=1
  if c=='{':
   r=self.seq('}');assert self.i<len(self.s);self.i+=1;return r
  if c=='\\':
   m=re.match('[A-Za-z]+',self.s[self.i:])
   if not m:
    c=self.s[self.i];self.i+=1;return atom('mo',c) if c not in ',; ' else '<mspace width=".2em"/>'
   name=m.group();self.i+=len(name)
   if name in ('quad','qquad'):return '<mspace width="'+('1em' if name=='quad' else '2em')+'"/>'
   if name in ('left','right'):return self.base()
   if name=='begin':
    self.skip();m=re.match(r'\{(bmatrix|pmatrix|matrix)\}',self.s[self.i:])
    if not m:raise ValueError('Unsupported matrix environment in '+self.s)
    env=m.group(1);self.i+=len(m.group());end='\\end{'+env+'}'
    stop=self.s.find(end,self.i)
    if stop<0:raise ValueError('Unclosed matrix in '+self.s)
    content=self.s[self.i:stop];self.i=stop+len(end)
    rows=[row.strip().split('&') for row in re.split(r'\\\\',content.strip())]
    if not rows or len({len(row) for row in rows})!=1:raise ValueError('Ragged matrix in '+self.s)
    table='<mtable columnspacing=".6em" rowspacing=".3em">'+''.join('<mtr>'+''.join('<mtd>'+Parser(cell.strip() or '0').seq()+'</mtd>' for cell in row)+'</mtr>' for row in rows)+'</mtable>'
    if env=='matrix':return table
    brackets=('[',']') if env=='bmatrix' else ('(',')')
    return tag('mrow',atom('mo',brackets[0])+table+atom('mo',brackets[1]))
   if name=='frac':return tag('mfrac',self.group()+self.group())
   if name=='sqrt':return tag('msqrt',self.group())
   if name=='not':
    value=self.base()
    for old,new in (('⊆','⊈'),('∈','∉'),('=','≠'),('∣','∤')):
     if old in value:return value.replace(old,new)
    raise ValueError('Unsupported negated operator in '+self.s)
   if name=='binom':return tag('mrow',atom('mo','(')+'<mfrac linethickness="0">'+self.group()+self.group()+'</mfrac>'+atom('mo',')'))
   if name in ('text','operatorname','mathrm','mathbb','mathbf','mathcal'):
    self.skip()
    if self.s[self.i]=='{':
     start=self.i+1;end=self.s.index('}',start);s=self.s[start:end];self.i=end+1
    else:s=self.s[self.i];self.i+=1
    if name=='mathbb':s={'R':'ℝ','N':'ℕ','Z':'ℤ','C':'ℂ','Q':'ℚ'}.get(s,s)
    return ('<mi mathvariant="script">'+html.escape(s)+'</mi>') if name=='mathcal' else atom('mtext' if name=='text' else 'mi',s)
   if name in ('log','ln','min','max','gcd','lcm','sin','cos','exp','det','rank','tr','ker','lim','dim'):return '<mi mathvariant="normal">'+name+'</mi>'
   if name in ('mod','bmod'):return atom('mo','mod')
   if name=='pmod':return tag('mrow',atom('mo','(')+atom('mo','mod')+self.group()+atom('mo',')'))
   if name in ('bar','overline'):return tag('mover',self.group()+atom('mo','¯'))
   if name in ('hat','widehat'):return tag('mover',self.group()+atom('mo','^'))
   if name in ('ldots','cdots'):return atom('mo','…')
   if name in SYMBOLS:return atom('mi' if len(SYMBOLS[name])==1 and SYMBOLS[name].isalpha() else 'mo',SYMBOLS[name])
   raise ValueError('Unsupported TeX command: '+name+' in '+self.s)
  if c.isdigit():
   m=re.match(r'[0-9]*(?:\.[0-9]+)?',self.s[self.i:]);v=c+m.group();self.i+=len(m.group());return atom('mn',v)
  return atom('mi' if c.isalpha() else 'mo',c)
 def seq(self,end=''):
  out=[]
  while self.i<len(self.s):
   self.skip()
   if self.i>=len(self.s) or (end and self.s[self.i]==end):break
   v=self.base();sub=sup=None
   while True:
    self.skip()
    if self.i>=len(self.s) or self.s[self.i] not in '_^':break
    which=self.s[self.i];self.i+=1;g=self.group()
    if which=='_':sub=g
    else:sup=g
   large=any(x in v for x in ('∑','∏','⋀','⋁'))
   if sub is not None and sup is not None:v=tag('munderover' if large else 'msubsup',v+sub+sup)
   elif sub is not None:v=tag('munder' if large else 'msub',v+sub)
   elif sup is not None:v=tag('mover' if large else 'msup',v+sup)
   out.append(v)
  return tag('mrow',''.join(out))
def render(s,display=False):
 p=Parser(s);value=p.seq();assert p.i==len(s),(p.i,s)
 if display:value=wrap_display(value)
 return '<math xmlns="http://www.w3.org/1998/Math/MathML" display="'+('block' if display else 'inline')+'" aria-label="'+html.escape(s,quote=True)+'">'+value+'</math>'
def width(e):
 children=list(e)
 if not children:
  t=e.text or ''
  if e.tag=='mo':return .4 if t in '|()[]{}' else 1.15
  return max(.5,len(t)*(.7 if t.isupper() else .6))
 if e.tag=='mfrac':return max(map(width,children))+.7
 if e.tag in ('msup','msub','msubsup'):return width(children[0])+max(map(width,children[1:]))*.7
 if e.tag in ('mover','munder','munderover'):return max(map(width,children))
 if e.tag=='mtable':return max(map(width,children))
 if e.tag=='mtr':return sum(map(width,children))+.6*max(0,len(children)-1)
 return sum(map(width,children))
def wrap_display(value):
 root=ET.fromstring(value);children=list(root)
 if width(root)<14.5:return value
 lines=[];current=[];w=0;depth=0
 for i,e in enumerate(children):
  s=e.text or '';legal=e.tag=='mo' and s in ('+','-','−','=','∨','∧','⊕') and depth==0
  # Wrap at a semantic operator without splitting a fraction or script cluster.
  if current and legal and w>7.5:
   ahead=width(e)+(width(children[i+1]) if i+1<len(children) else 0)
   if w+ahead>14.5:lines.append(current);current=[];w=0
  current.append(e);w+=width(e)
  if e.tag=='mo' and s in ('(','[','{'):depth+=1
  if e.tag=='mo' and s in (')',']','}'):depth-=1
 if current:lines.append(current)
 if len(lines)==1:return value
 return '<mtable displaystyle="true" columnalign="left" rowspacing=".55em">'+''.join('<mtr><mtd><mrow>'+''.join(ET.tostring(e,encoding='unicode') for e in row)+'</mrow></mtd></mtr>' for row in lines)+'</mtable>'
def markdown_math(s,md):
 slots=[]
 def hold(m):
  display=m.group(1) is not None;formula=m.group(1) if display else m.group(2)
  result=render(formula,display);slots.append('<div class="formula-block">'+result+'</div>' if display else result)
  return ('\n\n' if display else ' ')+'MATHSLOT'+str(len(slots)-1)+'END'+('\n\n' if display else ' ')
 s=re.sub(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',hold,s)
 s=re.sub(r'(MATHSLOT\d+END) +([,.;:?)])',r'\1\2',s)
 value=md.render(s)
 for i,slot in enumerate(slots):
  marker='MATHSLOT'+str(i)+'END'
  value=value.replace('<p>'+marker+'</p>',slot).replace(marker,slot)
 return value
