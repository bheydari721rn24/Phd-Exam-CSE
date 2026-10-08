"""Bound the bundled workflow's network wait; credentials remain on hidden stdin."""
import os,subprocess,sys
env=os.environ.copy();n=int(env.get('GIT_CONFIG_COUNT','0'))
for key,value in [('http.lowSpeedLimit','1'),('http.lowSpeedTime','20')]:
 env['GIT_CONFIG_KEY_'+str(n)]=key;env['GIT_CONFIG_VALUE_'+str(n)]=value;n+=1
env['GIT_CONFIG_COUNT']=str(n)
p=subprocess.Popen(['node','C:/Users/bheydari/.codex/plugins/cache/openai-curated-remote/sites/0.1.75/scripts/site-workflow.mjs','--project-id','appgprj_6ab5666f72b081918286c6b371c1eb1b'],env=env)
try:sys.exit(p.wait(timeout=55))
except subprocess.TimeoutExpired:
 subprocess.run(['taskkill','/PID',str(p.pid),'/T','/F'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);print('The Site source workflow exceeded the bounded network wait; local content is retained.',file=sys.stderr);sys.exit(124)
