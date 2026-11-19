const fs=require('fs');
for (const f of fs.readdirSync('project')) {
  const s=fs.readFileSync('project/'+f,'utf8');
  const js=s.split(/<script type="text\/x-dc"[^>]*>/)[1].split('</script>')[0];
  try {
    const C = new Function('DCLogic','window', js+'\nreturn Component;')(class { constructor(p){this.props=p||{};} setState(o){Object.assign(this.state,o);} }, {});
    const c = new C({}); const v = c.renderVals();
    console.log(f, 'OK', Object.keys(v).join(','), v.events? v.events.length+' evts, '+v.events[0].pills.length+' pills':'' , v.choix||'');
  } catch(e) { console.log(f, 'ERREUR', e.message); }
}
