from pathlib import Path
import json
E=Path(__file__).parent/'deep-library-revision'
p=E/'d_number-static-ports.json';d=json.loads(p.read_text());d.update(status='passed_actual_boundary_and_marker_checks',straightConnections=9,curvedConnections=2);p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
p=E/'d_number-browser.json';d=json.loads(p.read_text());d['humanInspectedScreenshots']+=['static-1-delivery.png','static-4-delivery.png','question-8-delivery.png'];d['latestVisualQualification']='Final Hasse center-direction endpoints, directed transient arrows without duplicate arrow glyphs, side-placed orbit indices and mixed prose/math labels were freshly inspected.';p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
