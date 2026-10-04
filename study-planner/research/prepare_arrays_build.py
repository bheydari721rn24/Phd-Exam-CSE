"""Prepare chapter renderer and integrate original array concept models."""
from pathlib import Path
import re
B=Path(__file__).resolve().parent;R=B.parent
p=B/'p_arrays.en.md';s=p.read_text(encoding='utf-8')
if 'is a sixth reviewed comparison' not in s:s=s.replace('is a fifth reviewed comparison for dynamic backing arrays.','is a fifth reviewed comparison for dynamic backing arrays. MIT 6.0001 (Ana Bell, Eric Grimson and John Guttag, Fall 2016) is a sixth reviewed comparison for list cloning and mutation during iteration.')
s=s.replace('6. Python Software','7. Python Software').replace('7. ISO/IEC','8. ISO/IEC').replace('8. Original Iranian','9. Original Iranian')
s=s.replace('7. Python Software','6. Massachusetts Institute of Technology — Ana Bell, Eric Grimson and John Guttag. 6.0001, Fall 2016. [Lecture 5: Tuples, Lists, Aliasing, Mutability and Cloning](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/1776670e271578eeb99fc25975f20586_MIT6_0001F16_Lec5.pdf), all 24 slides, particularly slides 7–23. Older print syntax is normalized to Python 3 in new examples.\n7. Python Software')
p.write_text(s,encoding='utf-8')
p=B/'build_concept_animations.py';s=p.read_text().replace('rank,functions\n','rank,functions,arrays\n');p.write_text(s)
p=B/'animations/catalog.py';s=p.read_text();s=s[:-2]+",\n'p_arrays':{'representation':['arr-boundary'],'layouts':['arr-row','arr-column','arr-transpose'],'traversals':['arr-prefix'],'mutation':['arr-copy-bad','arr-copy-right','arr-copy-left','arr-insert','arr-reverse','arr-rotate','arr-difference','arr-compact'],'python':['arr-sharing'],'strings':['arr-search'],'growth':['arr-growth'],'packed':['arr-packed','arr-ring']}\n}\n" if "'p_arrays':" not in s else s;p.write_text(s)
p=B/'qa_animations_browser.py';s=p.read_text().replace('scene.id.startsWith("functions-custom-")','(scene.id.startsWith("functions-custom-")||scene.id.startsWith("arrays-custom-"))');p.write_text(s)
s=(B/'build_functions_chapter.py').read_text()
start=s.index('figures={}');end=s.index('questions=json.loads')
figcode='''figures={}
b=label(350,30,'Six live elements, seven logical boundaries',23)
for i,v in enumerate([2,4,6,8,10,12]):
 b+=box(20+100*i,110,90,60,str(v))+label(65+100*i,205,'i = '+str(i),21)
b+=label(650,140,'end',22)+label(350,290,'0 ≤ i < 6 permits reads; boundary 6 is one-past',22)
figures['boundaries']=fig('arrays-boundaries','Element indices and exclusive end',340,b,'Figure 1. Values occupy indices zero through five. The exclusive endpoint is a valid boundary but contains no readable element.')
b=label(350,30,'Row-major strides: four elements per row',23)
for i in range(3):
 for j in range(4):b+=box(25+165*j,70+75*i,150,55,str(i)+','+str(j)+' → '+str(4*i+j))
b+=label(350,335,'Inverse: row = floor(offset / 4); column = offset mod 4',20)
figures['layouts']=fig('arrays-layouts','Dense layout and inverse map',380,b,'Figure 2. The row index skips complete rows; the column index advances within one row. Quotient and remainder uniquely undo the map.')
b=label(350,30,'Prefix values belong to boundaries',23)
for i,v in enumerate([0,3,1,6,7,3]):b+=box(20+110*i,100,100,55,str(v))+label(70+110*i,200,'P['+str(i)+']',21)
b+=label(350,285,'Sum A[1:4) = P[4] − P[1] = 7 − 3 = 4',22)
figures['prefix']=fig('arrays-prefix','Prefix boundaries and cancellation',330,b,'Figure 3. The five-element input [3, −2, 5, 1, −4] has six prefix boundaries. A half-open query subtracts two prefix values.')
b=label(350,30,'Rightward overlap: preserve the original source',22)
b+=box(30,90,280,65,'forward → [1,1,1,1]')+box(390,90,280,65,'reverse → [1,1,2,3]')
b+=box(150,225,400,65,'original source segment: [1,2,3]')
b+=label(350,360,'Copy high indices first when destination is to the right',21)
figures['overlap']=fig('arrays-overlap','Overlap counterexample and safe direction',400,b,'Figure 4. Both moves begin with [1,2,3,4] and target positions one through three. Only reverse copying preserves the original source values.')
b=label(350,30,'New outer list, shared inner row',23)
b+=box(30,90,270,60,'A: outer object 1')+box(400,90,270,60,'B: outer object 2')
b+=box(200,240,300,65,'one shared row: [2,7]')+line(165,150,300,240)+line(535,150,400,240)
b+=label(350,370,'An outer slice copies references, not inner objects',22)
figures['sharing']=fig('arrays-sharing','Nested row sharing',410,b,'Figure 5. An append through either copied outer reference changes the same inner row. Rebinding one outer slot has a different effect.')
b=label(350,30,'Expansion: length 3, capacity 3 → 6',23)
b+=box(30,95,270,65,'old: [2,4,6]')+box(390,95,280,65,'new: [2,4,6,_,_,_]')+line(300,127,390,127)
b+=box(150,240,400,65,'peak storage: 3 + 6 = 9 slots')
b+=label(350,370,'Release old storage only after copying all live entries',21)
figures['growth']=fig('arrays-growth','Distinct backing objects during growth',410,b,'Figure 6. Logical length remains three while capacity doubles. Two allocations coexist during the copy, so peak storage differs from final capacity.')
b=label(350,30,'Lower triangle: row starts are triangular counts',22)
for i in range(3):
 for j in range(i+1):b+=box(50+180*j,90+75*i,150,55,str(i)+','+str(j)+' → '+str(i*(i+1)//2+j))
b+=label(350,350,'offset = i(i + 1)/2 + j, with 0 ≤ j ≤ i',22)
figures['packed']=fig('arrays-packed','Packed lower-triangle positions',395,b,'Figure 7. Each earlier row contributes its length. Adding the within-row index gives a unique offset; upper-triangle coordinates are outside this domain.')
figures={k:v.replace('conditional-diagram','arrays-diagram') for k,v in figures.items()}
'''
s=s[:start]+figcode+s[end:]
s=s.replace('p_functions','p_arrays').replace('functions-lab','arrays-lab').replace('functions-form','arrays-form').replace('functions-output','arrays-output').replace('functions-player','arrays-player').replace('functions-diagram','arrays-diagram')
start=s.index("lab='''");end=s.index('source=(BASE/',start)
s=s[:start]+'''lab='''+"'''"+'''<section class="lab" id="arrays-lab"><form id="arrays-form"><label>Exact transformation<select name="mode"><option value="prefix">Prefix boundaries</option><option value="right">Overlap-safe rightward move</option><option value="bad">Counterexample: forward rightward move</option><option value="reverse">Pair-swap reversal</option><option value="difference">Original-neighbor differences</option><option value="compact">Stable compaction: retain even values</option></select></label><label>One to six comma-separated integers, each −20 through 20<input name="input" type="text" value="2,4,6,8,10,12" required></label><button type="submit">Restart exact trace</button></form><p id="arrays-output" aria-live="polite"></p><section class="concept-animation" id="arrays-player" data-loaded="true"></section><p>Rightward copy moves the original first n−1 values one slot right. The counterexample changes loop direction only. Reversal swaps symmetric pairs; differences preserve the first entry; compaction keeps only its stated logical prefix. Every checkpoint begins paused.</p></section>'''+"'''"+'''\n'''+s[end:]
s=s.replace('<!-- LAB:functions -->','<!-- LAB:arrays -->')
s=s.replace("anchors=['sources','interfaces','frames','values','scope','pointers','order','contracts','callbacks','python','problems','review','laboratory','references']","anchors=['sources','representation','layouts','c-semantics','traversals','mutation','python','strings','growth','packed','problems','review','laboratory','references']")
s=s.replace('==91','==83').replace("title='Functions, Variable Scope, and Parameter Passing'","title='Arrays and Indexing'")
s=s.replace('91 worked problems','83 worked problems').replace('12 concept simulations','18 concept simulations').replace('Authentic call-semantics bridge revisits','Authentic array-reasoning bridge revisits').replace('← Functions chapter','← Arrays chapter').replace('Functions chapter audit','Arrays chapter audit')
s=s.replace('questionCount=91','questionCount=83').replace('originalQuestionCount=89','originalQuestionCount=81')
s=s.replace('Built sole functions draft: 91 worked questions, 80 rules, seven figures, twelve models and adjustable trace lab.','Built sole arrays draft: 83 worked questions, 80 rules, seven figures, seventeen models and adjustable trace lab.')
(B/'build_arrays_chapter.py').write_text(s,encoding='utf-8')
(R/'dist/chapters/p_arrays.css').write_text((R/'dist/chapters/p_functions.css').read_text().replace('functions','arrays'))
print('Prepared array renderer and seventeen concept placements.')
