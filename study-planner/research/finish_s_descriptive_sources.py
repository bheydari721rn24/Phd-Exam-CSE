from pathlib import Path
import json
B=Path(__file__).resolve().parent
acq=json.loads((B/'s_descriptive-evidence/acquisition.json').read_text())
scopes={
'mit':'PDF pages 1–7: numerical summaries, n−1 variance, contingency tables, correlation, moving averages and EWMA; page 2 visually checked.',
'stanford-center':'Lecture 5 relevant full teaching body: center, balance, observational units and multimodality.',
'stanford-spread':'Lecture 7 relevant full teaching body: descriptive denominator n, SD, Chebyshev and quantiles.',
'stanford-robust':'Lecture 8 relevant full teaching body: mean sensitivity, outliers, robust summaries and misleading summaries.',
'berkeley-hist':'Frequency-table through percentile sections: unequal-width density area, modality, binning and percentile interpretation.',
'berkeley-location':'Location and loss, spread, affine transformations, Markov and Chebyshev sections. Lower nearest-rank median and decreasing-scale convention examined.',
'berkeley-correlation':'Full textual chapter: paired standard-score products, sign invariance and ecological correlation caveats.',
'cmu':'PDF pages 1–24, especially location, variance, shape, histograms, boxplots and Q–Q; page 21 visually checked.',
'harvard':'Sections 12.1–12.8 and 12.9.1–12.9.2: ECDF, distributions, quantile plots, stratification and outlier sensitivity.',
'oxford':'PDF pages 11–22 critically examined; page 17 visually checked for CV and moment-normalization defects.'}
records=[]
for r in acq:
 rec={k:v for k,v in r.items() if k!='path'}
 if r['id'] in scopes:rec.update(status='reviewed_bounded_scope',reviewScope=scopes[r['id']])
 else:rec['status']='index_screened_only' if 'eth' in r['id'] or 'toc' in r['id'] else 'unavailable_not_reviewed'
 records.append(rec)
(B/'s_descriptive-evidence/reading.json').write_text(json.dumps(dict(candidatePoolUniversities=7,selectedUniversities=['UC Berkeley','MIT','Stanford','Carnegie Mellon','Harvard'],selection='Four complementary core courses, plus Harvard to strengthen ECDF and Q–Q teaching; not a globally exhaustive ranking.',records=records),indent=2)+'\n',encoding='utf-8')
print([(r['id'],r['status']) for r in records])
