from pathlib import Path
B=Path(__file__).parent;s=(B/'read_divide_bank.py').read_text().replace('a_divide','a_correct')
needle="if __name__=='__main__':"
extra="""\n# The correctness course-derived bank has its own canonical source file.
canonical={q['id']:q for q in json.loads((B/'a_correct-questions.json').read_text())}
for r in rows:
 c=canonical.get(r['sourceId'])
 if c:
  clean=lambda s:s.replace(chr(92)*2,chr(92))
  r.update(stem=clean(c['stem']),options=[clean(v)for v in c['options']],answer=c['answer'],canonical=c)
"""
(B/'read_correctness_bank.py').write_text(s.replace(needle,extra+'\n'+needle),encoding='utf8')
