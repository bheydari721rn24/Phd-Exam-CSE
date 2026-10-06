from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'qa_library_teaching_browser.py').read_text(encoding='utf-8')
a=s.index(' for id in json');b=s.index(' # The actual 37 pages');s=s[:a]+s[b:]
s=s.replace("for chapter in inventory['chapters']:","for chapter in [r for r in inventory['chapters'] if r['topicId'] >= 'l_vectors']:")
s=s.replace("(A/'browser.json')","(A/'controls-browser.json')")
(R/'qa_library_teaching_controls.py').write_text(s,encoding='utf-8')
