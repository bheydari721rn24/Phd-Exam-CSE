"""Install reviewed SVGs in both live lessons and printable no-JavaScript previews."""
from pathlib import Path
import json,re,hashlib,tempfile,html
from math_typography import normalize_math,normalize_scripts
ROOT=Path(__file__).resolve().parents[1];PREVIEW=Path(tempfile.gettempdir())/'subject-visual-review'
CHAPTERS=json.loads((ROOT/'research/subject-visual-review.json').read_text())['chapters']
SVG=re.compile(r'<svg\b[\s\S]*?</svg>')
FIGURE=re.compile(r'<figure\b[\s\S]*?</figure>')
STATIC={
'g_gates':{1:('gate-symbols','Distinctive-shape symbols distinguish AND, OR, NOR, NAND, XOR and XNOR. An output bubble complements the gate result. Two inputs are shown; a multi-input exactly-one function is not parity.'),2:('nand-mux','The four-NAND selector computes ¬s·d0 + s·d1. This drawn valuation is s=1, d0=0, d1=1; thus the selected output is 1. The first NAND has tied inputs. Wire crossings without junction dots are not connections.'),3:('cmos-nand','The schematic has parallel pMOS channels from VDD and series nMOS channels to ground. The displayed A=B=1 state conducts through the pull-down network. These are ideal stable switch states, not analog transient waveforms.'),6:('half-subtractor','PhD CE 1405, Q23: five NAND gates implement F1=x XOR y and F2=¬x·y. The final lower NAND has tied inputs. The shown valuation x=1, y=0 is illustrative; all source connections and variable order are retained.')},
'g_boolean':{3:('half-subtractor','PhD CE 1405, Q23: the five-NAND half-subtractor retains the original net connections. F1 is difference and F2 is borrow. The displayed illustrative valuation x=1, y=0 yields 1 and 0.')},
'g_combin':{1:('comb-priority','The enabled priority network contains the enable guards on both grants. The drawn example E=R1=R0=1 grants only R1. The full case analysis and all eight input valuations remain in the lesson and animated model.'),2:('comb-dag','The actual gate network computes p=AB, q=C+D, r=pq, Y=r+E and Z=r XOR H. One shared internal r drives both outputs. The final settled checkpoint is shown; playback exposes the prior evaluation stages.'),3:('factored','The factored network computes (a+b+c)(d+e)f+g using two wide OR gates, one three-input AND and one final OR. It uses four gates only under this declared wide-gate library. A two-input library requires another mapping.'),4:('comb-cofactor','The physical multiplexer data connections are D0=C, D1=1, D2=C and D3=C. Select order is AB, with A the most significant select bit. The residual row pair, rather than intuition, determines each data connection.'),5:('comb-rom','A shared 3:8 decoder feeds distinct parity and majority output columns. Dots in the array indicate the programmed row-to-column connections. These are logical array connections, not a transistor-level ROM layout.'),6:('comb-nand','Three conventional NAND symbols implement the complemented AB and AC products followed by their NAND combination. The gate outputs and wire polarities are explicit. No primary-input complements are assumed free.'),7:('multi-miter','Two corresponding output pairs feed separate XOR gates; their discrepancies are ORed into one miter. The drawn example agrees on both outputs. Equivalence requires zero discrepancy for every allowed input, not only this example.'),8:('comb-interval','The gate schematic follows p=AB, q=p+C, Y=qD. The delay intervals (1,3), (2,4), (1,2) yield final structural bounds [1,9]. Stable illustrative logic values are separate from these timing bounds.')},
}
def main():
    previews={}
    for row in CHAPTERS:
        p=ROOT/f'dist/chapters/{row["topicId"]}.html';s=p.read_text(encoding='utf-8')
        def widget(m):
            block=m[0];id=re.search(r'data-scenes="([^"]+)"',block)[1].split(',')[0];svg=(PREVIEW/(id+'.first.svg')).read_text(encoding='utf-8');previews[id]=svg
            return SVG.sub(lambda _:svg,block,count=1)
        s=re.sub(r'<!-- CONCEPT ANIMATION START [^>]+ -->[\s\S]*?<!-- CONCEPT ANIMATION END -->',widget,s)
        i=0
        def figure(m):
            nonlocal i
            i+=1;spec=STATIC.get(row['topicId'],{}).get(i)
            if not spec:return m[0]
            id,caption=spec;svg=(PREVIEW/(id+'.svg')).read_text(encoding='utf-8')
            block=SVG.sub(lambda _:svg,m[0],count=1)
            caption_html=normalize_math(normalize_scripts('<figcaption>'+html.escape(caption)+'</figcaption>'))
            return re.sub(r'<figcaption[^>]*>[\s\S]*?</figcaption>',lambda _:caption_html,block)
        s=FIGURE.sub(figure,s)
        for name in ['chapter.en.css','concept-animation.css','concept-animation.js','semantic-diagrams.js','math-layout.js']:
            s=re.sub(r'((?:src|href)="'+re.escape(name)+r')(?:\?[^" ]*)?("\s*)',r'\1?v=67\2',s)
        p.write_text(s,encoding='utf-8');row['staticSchematicsRewritten']=len(STATIC.get(row['topicId'],{}));row['printablePreviewCount']=len(re.findall('<!-- CONCEPT ANIMATION START',s));row['htmlSha256']=hashlib.sha256(p.read_bytes()).hexdigest()
    # Every reusable scene retains its first checkpoint for later chapter rebuilds.
    for p in PREVIEW.glob('*.first.svg'):previews[p.name[:-10]]=p.read_text(encoding='utf-8')
    (ROOT/'research/subject-visual-previews.json').write_text(json.dumps(previews,indent=2)+'\n')
    review=json.loads((ROOT/'research/subject-visual-review.json').read_text());review['chapters']=CHAPTERS;(ROOT/'research/subject-visual-review.json').write_text(json.dumps(review,indent=2)+'\n')
    print(json.dumps(dict(chapters=len(CHAPTERS),previews=len(previews),schematics=sum(len(x) for x in STATIC.values()))))
if __name__=='__main__':main()
