from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'render_i_agents_impl.py').read_text(encoding='utf-8').replace('i_agents','i_uninformed').replace('ag-','us-').replace('#ag-','#us-').replace('LAB: agents','LAB: search').replace('Intelligent Agents, Rationality, Task Environments, and Problem Formulation','Uninformed Search: BFS, DFS, Uniform Cost, and Iterative Deepening').replace('82','81').replace('authenticQuestionCount=2','authenticQuestionCount=1').replace('Authentic examinations: task environment and agent learning','Authentic examination: iterative deepening').replace('Intelligent agents chapter','Uninformed search chapter')
a=s.index("lab='<section");b=s.index('\nsource=',a)
lab='''<section class="lab"><form id="us-form"><label>Algorithm<select name="algorithm"><option value="bfs">BFS</option><option value="dfs">DFS</option><option value="ucs" selected>Uniform cost</option><option value="dls">Depth limited</option><option value="ids">Iterative deepening</option></select></label><label>Start state<input name="start" value="S"></label><label>Goal state<input name="goal" value="G"></label><label>Maximum depth limit<input name="limit" type="number" min="0" max="12" value="4"></label><label>Directed edges: source destination cost<textarea name="edges">S A 4
S B 1
B A 1
A G 2
B G 8</textarea></label><button type="submit">Run the search and inspect every checkpoint</button></form><p id="us-error" role="alert"></p><p>Costs are nonnegative integers from 0 to 10000. Use at most eight states and sixteen directed edges. Edge-list order defines successor order. Depth limits range from zero to twelve. Every walkthrough starts paused. An invalid input preserves the preceding valid result.</p><div id="us-output"></div></section>'''
s=s[:a]+'lab='+repr(lab)+s[b:]
a=s.index('anchors=[');b=s.index(';it=iter(anchors)',a)
anchors=['sources','nodes','events','framework','bfs-invariant','bfs-trace','bfs-properties','bfs-counts','dfs','dfs-properties','dls','depth-budgets','ids','ids-counts','ucs','ucs-proof','ucs-code','ucs-completeness','ucs-complexity','transformations','bidirectional-bfs','bidirectional-ucs','state-keys','applications','comparison','exam-workflow','summary','problems','review','laboratory','references']
s=s[:a]+'anchors='+repr(anchors)+s[b:]
(B/'render_i_uninformed.py').write_text(s,encoding='utf-8')
