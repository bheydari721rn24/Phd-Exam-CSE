from pathlib import Path
import re
p=Path(__file__).resolve().parent/'s_distributions-review.en.md'
s=p.read_text(encoding='utf-8')
s=re.sub(r'^#{1,2} ', '### ', s, flags=re.M)
p.write_text(s,encoding='utf-8')
