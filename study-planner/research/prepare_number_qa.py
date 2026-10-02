from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'research/check_site_en.py';s=p.read_text(encoding='utf-8')
s=s.replace("assert flow['status'] == 'draft'", "assert flow['status'] == 'ready'")
if "number = next(c" not in s:
 s=s.replace('vector_html =',"number = next(c for w in lessons for c in w['chapters'] if c['topicId'] == 'g_number')\nassert number['status'] == 'draft' and number['url'] == 'chapters/g_number.html'\nvector_html =")
s=s.replace('"p_types", "p_flow"):', '"p_types", "p_flow", "g_number"):')
p.write_text(s,encoding='utf-8')
p=ROOT/'research/qa_proof_browser.py';s=p.read_text(encoding='utf-8')
s=s.replace('"p_types", "p_flow"}', '"p_types", "p_flow", "g_number"}')
if "if CHAPTER == 'g_number':" not in s:
 insert='''    if CHAPTER == 'g_number':
        cases=[(4,7,1,'add',8,-8,0,True),(4,15,1,'add',0,0,1,False),(4,8,8,'add',0,0,1,True),(4,7,8,'sub',15,-1,0,True),(4,0,0,'sub',0,0,1,False),(4,8,15,'sub',9,-7,0,False),(8,100,60,'add',160,-96,0,True),(16,65535,1,'add',0,0,1,False),(16,32767,1,'add',32768,-32768,0,True)]
        for n,a,b,op,word,signed,carry,overflow in cases:
            expression=f"document.getElementById('number-width').value={n};document.getElementById('number-a').value={a};document.getElementById('number-b').value={b};document.getElementById('number-operation').value='{op}';document.getElementById('number-operation').dispatchEvent(new Event('input'));JSON.stringify({...document.getElementById('number-result').dataset})".replace('JSON.stringify(', 'JSON.stringify(')
            state=json.loads(cdp('Runtime.evaluate',{'expression':expression,'returnByValue':True})['result']['value'])
            assert state['valid']=='true' and int(state['word'])==word and int(state['signed'])==signed and int(state['carry'])==carry and state['overflow']==str(overflow).lower(),state
        for bad in ('', '-1', '1.5', '65536'):
            cdp('Runtime.evaluate',{'expression':f"document.getElementById('number-a').value='{bad}';document.getElementById('number-a').dispatchEvent(new Event('input'))"})
            assert cdp('Runtime.evaluate',{'expression':"document.getElementById('number-result').dataset.valid",'returnByValue':True})['result']['value']=='false'
        cdp('Runtime.evaluate',{'expression':"document.getElementById('number-width').value=4;document.getElementById('number-a').value=7;document.getElementById('number-b').value=1;document.getElementById('number-operation').value='add';document.getElementById('number-operation').dispatchEvent(new Event('input'))"})
        info=json.loads(cdp('Runtime.evaluate',{'expression':"JSON.stringify({math:getComputedStyle(document.querySelector('math')).fontFamily,code:getComputedStyle(document.querySelector('pre code')).fontFamily,diagram:getComputedStyle(document.querySelector('svg .math-label')).fontFamily,index:getComputedStyle(document.querySelector('sub')).fontFamily,underline:[...document.querySelectorAll('a')].some(x=>getComputedStyle(x).textDecorationLine.includes('underline')),problems:[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length})",'returnByValue':True})['result']['value'])
        assert all('STIX Two Math' in info[k] for k in ('math','diagram','index')) and 'JetBrains Mono' in info['code'] and not info['underline'] and info['problems']==36,info
        for name,selector in [('laboratory','.number-lab'),('problems','#worked-problems'),('review','#quick-reference'),('diagram','.number-diagram'),('gray','#gray'),('codes','#decimal')]:
            cdp('Runtime.evaluate',{'expression':f"document.querySelector('{selector}').scrollIntoView({{block:'start'}})"})
            time.sleep(.15)
            (OUT/f'{name}-mobile-cdp.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
        print('Number laboratory: nine arithmetic states, four invalid inputs, math/code/index/diagram fonts, links and 36 solutions passed.',info)
'''
 # Escaped braces are needed in the embedded f-string, while object spread stays JS.
 insert=insert.replace('JSON.stringify({...document', 'JSON.stringify({{...document').replace(".dataset})\".replace('JSON.stringify(', 'JSON.stringify(')", ".dataset}})\"")
 s=s.replace("    if CHAPTER == 'p_flow':",insert+"    if CHAPTER == 'p_flow':",1)
p.write_text(s,encoding='utf-8')
records=json.loads(Path(r'C:/Users/bheydari/AppData/Local/Temp/g_number_sources/manifest.json').read_text(encoding='utf-8'))
stan=Path(r'C:/Users/bheydari/AppData/Local/Temp/p_types_sources/stanford.pdf')
records.append(dict(name='stanford',url='https://web.stanford.edu/class/archive/cs/cs107/cs107.1204/lectures/2/Lecture2.pdf',status='cached_original_read',sha256=hashlib.sha256(stan.read_bytes()).hexdigest(),pages=115))
(ROOT/'research/g_number-source-manifest.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
p=ROOT/'dist/course-audit-week1.en.json';data=json.loads(p.read_text(encoding='utf-8'))
courses=data['courses']
for name,uni,course,url,topics,limit in [
 ('mit-number','MIT','6.004 Spring 2017; Chris Terman; Chapter 1 annotated notes','https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s1/','Fixed-length codes, integer encodings, Hamming distance and parity','Huffman compression excluded; worksheet landing only screened.'),
 ('berkeley-number','UC Berkeley','CS61C living course teaching-team notes; Number Representation','https://notes.cs61c.org/content/number-rep/integer-representations/','Radix, signed encodings, bias, range and zero counts','Complete in-scope written bodies read; ones complement carry and signed-zero qualifications supplied.'),
 ('stanford-number','Stanford','CS107 Winter 2020; Jerry Cain and Lisa Yan; Lecture 2','https://web.stanford.edu/class/archive/cs/cs107/cs107.1204/lectures/2/Lecture2.pdf','PDF pages 8–50, 53–84, 109–114; conversion, range, extension','Machine-specific C assumptions not treated as universal; full course not claimed read.'),
 ('cornell-number','Cornell','CS3410 Fall 2024; Adrian Sampson and Giulia Guidi; written notes','https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/float.html','Switches and Numbers plus Real Numbers in Binary and Fixed-Point Numbers','Primary web text read; local certificate verification failed. Full IEEE details deferred.'),
 ('cmu-number','Carnegie Mellon','15-213/14-513/15-513 Spring 2025; teaching team; From Bits through Integers','https://www.cs.cmu.edu/afs/cs/academic/class/15213-s25/www/lectures/02-bits-bytes-ints.pdf','PDF pages 7–10, 19, 21–35, 39–64; word arithmetic, product widths, shifts','Selected supplement; abstract word behavior separated from C17 expressions. Endianness deferred.'),
 ('princeton-number','Princeton','Algorithms lecture resources; Robert Sedgewick and Kevin Wayne; Combinatorial Search','https://algs4.cs.princeton.edu/lectures/keynote/67CombinatorialSearch.pdf','PDF pages 35–37 visually read; Gray reflection, enumeration and encoders','Selected Gray supplement; damaged local text resolved by original page images, year not guessed.')]:
 if not any(c['id']==name for c in courses):courses.append(dict(id=name,subject='logic',university=uni,course=course,url=url,evidence=url,topics=['g_number'],advantage=topics,limit=limit,access='official_written_course_material',reviewLevel='reviewed_in_scope_written_sections'))
p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Updated chapter QA and six actual-reading course records; saved source-byte manifest.')
