from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'research/qa_deep_correctness_revision.py';s=p.read_text(encoding='utf8')
needle='attached:near(v[0],v[1])&&near(v[2],v[3]),marker:'
replacement="attached:(()=>{const m=svg.getScreenCTM().inverse().multiply(p.getScreenCTM()),a=p.getPointAtLength(0).matrixTransform(m),b=p.getPointAtLength(p.getTotalLength()).matrixTransform(m);return near(a.x,a.y)&&near(b.x,b.y);})(),declaredAttached:near(v[0],v[1])&&near(v[2],v[3]),marker:"
if 'declaredAttached:'not in s:assert needle in s;s=s.replace(needle,replacement)
p.write_text(s,encoding='utf8')
