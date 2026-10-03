"""Small authoring utility; content is explicit, independently solved chapter data."""
from pathlib import Path
def chapter(topic,teaching,questions,notes):
 s='## Teaching through formulas and conceptual decisions\n\n'+teaching.strip()+'\n\n## Formula and conceptual problem bank\n\n'
 for i,(title,prompt,options,answer,solution) in enumerate(questions,1):
  assert len(options)==4 and answer in 'ABCD'
  s+=f'### Question {i}. {title}\n\n{prompt}\n\n'
  s+='\n\n'.join(f'**{a}.** {v}' for a,v in zip('ABCD',options))
  s+=f'\n\n**Answer: {answer}.**\n\n{solution.strip()}\n\n'
 s+='## Applicable formulas and examination notes\n\n'
 for i,(title,body) in enumerate(notes,1):s+=f'### {i}. {title}\n\n{body.strip()}\n\n'
 Path(__file__).with_name(topic+'.md').write_text(s.rstrip()+'\n',encoding='utf-8')
 print(topic,len(questions),'questions;',len(notes),'specific examination notes')
