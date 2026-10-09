from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'research/qa_unified_library.py';s=p.read_text()
needle="  time.sleep(.2)\n  result="
addition="""  time.sleep(.2)
  # Explicitly exercise form-generated diagrams as well as stored ones.
  js('document.querySelectorAll(\"form\").forEach(f=>f.dispatchEvent(new Event(\"submit\",{cancelable:true})))')
  time.sleep(.1)
  result="""
assert needle in s;s=s.replace(needle,addition)
needle="  rows=js('AdvancedSimulations.players.map"
addition="""  modelFile=R/f'dist/chapters/{topic}-models.json'
  if modelFile.exists():
   expected={m['id']for m in json.loads(modelFile.read_text())['models']};actual=set(js('AdvancedSimulations.players.map(p=>p.model.id)'));result['missingStoredModels']=sorted(expected-actual)
  else:result['missingStoredModels']=[]
  result['unloadedHosts']=js('[...document.querySelectorAll(\".concept-animation[data-scenes],[data-problem-visual]\")].filter(h=>h.dataset.loaded!==\"true\").map(h=>h.dataset.scenes??h.dataset.problemVisual)')
  result['compactWidth']=js('[...document.querySelectorAll(\".sim-redesign\")].every(h=>h.getBoundingClientRect().width<=h.parentElement.getBoundingClientRect().width+1)')
  rows=js('AdvancedSimulations.players.map"""
assert needle in s;s=s.replace(needle,addition)
s=s.replace("c['errors']or c['failedHosts']", "c['errors']or c['failedHosts']or c['missingStoredModels']or c['unloadedHosts']or not c['compactWidth']")
p.write_text(s,encoding='utf-8')
print('All stored model coverage, editable forms and parent-column width checks enabled.')
