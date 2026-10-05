"""Keep the distribution's existing compact JSON format."""
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/concept-animations.json'
p.write_text(json.dumps(json.loads(p.read_text()),ensure_ascii=True,separators=(',',':'))+'\n')
