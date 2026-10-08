from pathlib import Path
import json,subprocess,sys,ast
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef)and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
p=R/'dist/chapters/p_strings.js';s=p.read_text();old=(R/'dist/chapters/i_uninformed.js').read_text();mount=old[old.index('function mount(host,m)'):old.index('const controls=')].replace('us-','st-').replace('search-graph|search-count|cost-contour|grid-path|bidirectional-layers','byte-memory')
if '/* PLAYER_MOUNT */'in s:s=s.replace('/* PLAYER_MOUNT */',mount)
s=s.replace('height="30" rx="6"','height="36" rx="6"').replace('(y+21)','(y+24)').replace('(y+30)','(y+36)');p.write_text(s,encoding='utf-8')
css=(R/'dist/chapters/i_uninformed.css').read_text().replace('us-','st-');css+='\n.st-stage svg .st-byte,.st-print svg .st-byte{font-family:"JetBrains Mono",monospace!important;font-size:19px!important}.st-stage svg .st-index,.st-print svg .st-index{font-family:"STIX Two Math",serif!important;font-size:14px!important}.st-stage svg .st-head,.st-print svg .st-head{font-size:16px!important}#st-form select{width:100%}.st-model .teaching-panel pre{white-space:pre-wrap}\n';(R/'dist/chapters/p_strings.css').write_text(css,encoding='utf-8')
specs=[];groups={}
def add(id,title,group=None,**s):
 s.setdefault('capacity',12);s.setdefault('destination','');specs.append(dict(id=id,title=title,spec=s))
 if group:groups.setdefault(group,[]).append(id)
add('scan-embedded','First NUL in an eight-byte initialized source','scan',operation='scan',source=[97,98,0,99,100,0,120,0],raw=True,capacity=8)
add('scan-missing','A bounded source scan with no terminator','scan',operation='scan',source=[97,98,99,100,101],raw=True,capacity=5)
add('scan-empty','An empty source still has a terminator','scan',operation='scan',source='',capacity=1)
add('copy-fit','Six content bytes and a seventh terminator slot','copy',operation='copy',source='planet',capacity=7)
add('copy-empty','Copying an empty string writes one zero','copy',operation='copy',source='',capacity=1)
add('copy-reject','Reject a destination with no terminator slot','copy',operation='copy',source='planet',capacity=6)
add('pad-copy','Bounded copying pads to five written bytes','bounded-copy',operation='ncpy',source='ab',destination='xxxxxxxx',capacity=8,limit=5)
add('prefix-copy','Four copied content bytes do not create a zero','bounded-copy',operation='ncpy',source='abcdef',destination='xxxx',capacity=4,limit=4)
add('zero-copy','A zero bound preserves all destination bytes','bounded-copy',operation='ncpy',source='abcd',destination='xxxx',capacity=4,limit=0)
add('append-fit','Append XY after orbit and move the terminator','append',operation='append',source='XY',destination='orbit',capacity=10)
add('append-bound','Append only three content bytes to length four','append',operation='append',source='abcdefgh',destination='code',capacity=10,limit=3)
add('append-short','A short source fits despite a large conceptual bound','append',operation='append',source='ab',destination='1234567',capacity=10,limit=16)
add('append-reject','Reject append before overwriting an out-of-range byte','append',operation='append',source='XYZ',destination='orbit',capacity=8)
add('move-right','Overlapping right shift: copy backward including NUL','overlap',operation='move',source='',destination='abcd',capacity=8,from_=0,to=1,count=5)
specs[-1]['spec']['from']=specs[-1]['spec'].pop('from_')
add('move-left','Overlapping left shift: preserve the original suffix','overlap',operation='move',source='',destination='abcdef',capacity=7,from_=2,to=0,count=5)
specs[-1]['spec']['from']=specs[-1]['spec'].pop('from_')
add('insert-main','Insert X into abcde at position two','overlap',operation='insert',source='X',destination='abcde',capacity=7,position=2)
add('delete-main','Delete index two of planet, including the moved zero','overlap',operation='delete',source='',destination='planet',capacity=7,position=2,remove=1)
add('compare-main','algorithm versus algebra: the first mismatch','compare',operation='compare',source='algorithm',destination='algebra',capacity=10)
add('compare-prefix','cat versus catalog: zero is the first mismatch','compare',operation='compare',source='cat',destination='catalog',capacity=8)
add('compare-bound','Three equal prefix bytes hide the later mismatch','compare',operation='compare',source='cat',destination='catalog',capacity=8,limit=3)
add('compare-equal','Equal strings require the terminating zero pair','compare',operation='compare',source='same',destination='same',capacity=5)
add('match-overlap','All three overlapping aaa occurrences','match',operation='match',source='aaa',destination='aaaaa',capacity=6,all=True)
add('match-worst','Five alignments each force four comparisons','match',operation='match',source='aaab',destination='aaaaaaaa',capacity=9)
add('match-empty','An empty pattern matches at position zero','match',operation='match',source='',destination='ab',capacity=3)
add('match-long','Reject candidate alignments when the pattern is longer','match',operation='match',source='abcd',destination='ab',capacity=3)
add('reverse-main','Reverse abcde without moving its NUL','reverse',operation='reverse',source='',destination='abcde',capacity=6)
add('reverse-empty','Empty reversal performs no swaps','reverse',operation='reverse',source='',destination='',capacity=1)
add('compact-main','Remove a from banana with read/write heads','compact',operation='compact',source='a',destination='banana',capacity=7)
add('compact-all','All rejected: write the new zero at index zero','compact',operation='compact',source='x',destination='xxxx',capacity=5)
add('tokens-main','Preserve empty fields in a,,b,','tokens',operation='tokens',source=',',destination='a,,b,',capacity=6)
script="const fs=require('fs'),a=require('./dist/chapters/p_strings.js');process.stdout.write(JSON.stringify(JSON.parse(fs.readFileSync(0,'utf8')).map(s=>a.makeModel(s.id,s.title,s.spec))));"
models=json.loads(subprocess.check_output(['node','-e',script],input=json.dumps(specs).encode(),cwd=R))
for m in models:
 for f in m['frames']:
  f['formulaHtml']=mathml.wrap_display(mathml.Parser(f.pop('formula')).seq())
  f['teaching']['checks']=[dict(mathHtml='<p>'+x['expression']+'</p>',result=x['result'])for x in f['teaching']['checks']]
(R/'dist/chapters/p_strings-models.json').write_text(json.dumps(dict(models=models,groups=groups),indent=2)+'\n',encoding='utf-8')
qs=json.loads((B/'p_strings-questions.json').read_text());qs[14]['modelId']='append-bound';qs[79]['modelId']='append-fit';qs[79]['additionalModelIds']=['delete-main','reverse-main'];qs[79]['visualQualification']='The first trace exactly illustrates the initial append. The deletion and reversal traces are separately labelled examples; the question solution supplies its own five-byte surviving string and must not substitute those examples.'
# Do not attach mismatched examples to the final combined question.
qs[79].pop('additionalModelIds');qs[79].pop('visualQualification')
(B/'p_strings-questions.json').write_text(json.dumps(qs,indent=2)+'\n',encoding='utf-8')
print(len(models),'models',sum(len(m['frames'])for m in models),'checkpoints')
