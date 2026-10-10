from pathlib import Path
p=Path(__file__).with_name('build_d_generating.py')
s=p.read_text(encoding='utf-8')
s=s.replace('for n in[5,18,43,50,75,77]', 'for n in[5,9,18,43,46,50,75,77]')
start=s.index(" else:q['solution']+=")
end=s.index('# Store only',start)
s=s[:start]+s[end:]
s=s.replace("(B/'render_d_generating.py').write_text(s", "s=s.replace('import mathml', 'import mathml\\nmathml.SYMBOLS.update(cosh=\"cosh\")')\n(B/'render_d_generating.py').write_text(s")
p.write_text(s,encoding='utf-8')
