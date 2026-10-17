"""Reusable editorial content, separate from historical generators and rendering."""
from pathlib import Path
import copy, re
E = Path(__file__).resolve().parent / 'deep-library-revision'

def blocks(path, prefix='LG'):
    pieces = re.split(r'^## (' + prefix + r'\w+)\s*$', path.read_text(encoding='utf8'), flags=re.M)
    return {pieces[i]:pieces[i+1].strip() for i in range(1,len(pieces),2)}

def revise_questions(original):
    questions = copy.deepcopy(original)
    elementary = blocks(E/'l_gauss-elementary-answer-expansions.en.md')
    middle = blocks(E/'l_gauss-answer-expansions.en.md')
    advanced = blocks(E/'l_gauss-advanced-answer-expansions.en.md')
    assert len(elementary)==12 and len(middle)==13 and len(advanced)==44
    for q in questions:
        ident=q['id']
        if ident in elementary:
            # Keep the actual exact row-operation arrays; replace only their conclusion.
            markers=['Set every free coefficient variable','The final coefficient-zero row']
            cut=min(q['solution'].index(x) for x in markers if x in q['solution'])
            q['solution']=q['solution'][:cut].rstrip()+'\n\n'+elementary[ident]
        elif ident in middle:
            q['solution']=middle[ident]
        else:
            body=advanced[ident]
            for label,key in [('Title','title'),('Question','stem'),('Provenance','origin'),('Difficulty','difficulty')]:
                match=re.search(r'\*\*'+label+r'\.\*\* (.*?)(?=\n\n)',body,re.S)
                assert match and match[1].strip()==q[key], (ident,label)
            q['solution']=body.split('### Teaching solution',1)[1].strip()
    assert {q['id']for q in questions}=={'LG'+str(i).zfill(2) for i in range(1,70)}
    return questions

def revise_authentic(original):
    questions=copy.deepcopy(original)
    answers=blocks(E/'l_gauss-authentic-expanded-solutions.en.md',r'(?:Phd|MS)_')
    assert len(answers)==2
    for q in questions:
        q['solution']=answers[q['id']]
        if q['id']=='MS_CS_1405_Q113':q['options'][0]='37'
    return questions
