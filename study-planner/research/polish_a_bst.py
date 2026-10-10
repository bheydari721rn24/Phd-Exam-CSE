from pathlib import Path
P=Path(__file__).resolve().parents[1]/'dist/chapters/a_bst.js';s=P.read_text(encoding='utf-8')
s=s.replace("lines:['Left subtree size: '+l,'Accumulated strict rank: '+acc,'Residual select rank: '+j]", "lines:s.operation==='rank'?['Query key: '+s.q,'Left subtree size: '+l,'Accumulated strict rank: '+acc]:['Residual rank: '+j,'Left subtree size: '+l,'Use zero-based selection.']")
P.write_text(s,encoding='utf-8')
print('Removed irrelevant select-state labels from strict-rank checkpoints.')
