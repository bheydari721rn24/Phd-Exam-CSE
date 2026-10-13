from pathlib import Path
B=Path(__file__).parent
s=(B/'verify_invariants_printed_numerics.py').read_text().replace('d_invariants','d_number');(B/'verify_discrete_number_printed_numerics.py').write_text(s,encoding='utf-8')
s=(B/'repair_invariants_static_ports.py').read_text();a=s.index(" if 'Primary coordinate first' in raw:");z=s.index(' for marker in',a);s=s[:a]+s[z:];s=s.replace('d_invariants','d_number').replace('assert len(records)==4','assert len(records)>=4').replace("'diagrams':4","'diagrams':len(records)")
(B/'repair_discrete_number_static_ports.py').write_text(s,encoding='utf-8')
