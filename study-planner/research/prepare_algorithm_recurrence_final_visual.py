from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_algorithm_recurrence_browser.py').read_text();a=s.index(" report['models']=");s=s[:a]+(B/'algorithm_recurrence_final_visual_body.txt').read_text();(B/'qa_algorithm_recurrence_final_visual.py').write_text(s,encoding='utf8')
