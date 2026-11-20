"""Build two self-contained embedded media explorers, matching earlier activities.

Python generates HTML; browser calculations work on the static TeachBook host.
SI physics, peak phasors and exp(+j omega t). No separate notebook or network calls.
"""
from pathlib import Path
import html,json
from media_models import MODELS
ROOT=Path(__file__).resolve().parents[1]
STYLE='''*{box-sizing:border-box}body{font:15px system-ui,sans-serif;color:#243743;background:white;margin:0;padding:14px}h2{font-size:21px;margin:0 0 9px}p{line-height:1.5;margin:9px 0}.controls{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px 20px;margin:15px 0}label{display:block;font-weight:600}label output{display:block;font-weight:400;min-height:23px;font-variant-numeric:tabular-nums}input[type=range],select{width:100%;accent-color:#008dab}select{font:inherit;padding:6px;background:white;color:#243743;border:1px solid #8296a0}input[type=checkbox]{accent-color:#008dab}button{font:inherit;padding:6px 15px;background:white;border:1px solid #78909b;border-radius:4px}.plots{display:grid;grid-template-columns:1fr 1fr;gap:12px}canvas{width:100%;height:auto;border:0}.readout{font-variant-numeric:tabular-nums;line-height:1.65;font-size:16px}.hint,details{font-size:14px;line-height:1.5;color:#435963}summary{cursor:pointer}details p{margin:7px 0}.blue{color:#007fa8}.orange{color:#bd641d}.green{color:#63823a}.legend{font-size:14px}button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #007fa8;outline-offset:3px}@media(max-width:690px){.plots{grid-template-columns:1fr}.controls{grid-template-columns:1fr 1fr}body{font-size:14px}}@media(max-width:420px){.controls{grid-template-columns:1fr}}'''
COMMON=r'''
"use strict";
const EPS0=8.8541878128e-12,C=299792458,MU0=1/(EPS0*C*C);
const el=id=>document.getElementById(id);
function fmt(x,unit=''){if(!Number.isFinite(x))return '∞'+(unit?' '+unit:'');if(x===0)return '0'+(unit?' '+unit:'');return (Math.abs(x)>=1e4||Math.abs(x)<.001?x.toExponential(2):Number(x.toPrecision(4)).toString())+(unit?' '+unit:'');}
function physics(f,er,di,sigma=0){
 const w=2*Math.PI*f,ei=di+sigma/(w*EPS0),b=Math.sqrt((Math.hypot(er,ei)+er)/2),beta=w/C*b,alpha=w/C*ei/(2*b);
 return {f,w,er,di,sigma,ei,beta,alpha,depth:alpha===0?Infinity:1/alpha,lambda:2*Math.PI/beta,v:w/beta,hphase:-Math.atan2(alpha,beta),conductionRatio:sigma/(w*EPS0*Math.hypot(er,di))};
}
function chart(id,o){
 const cv=el(id),c=cv.getContext('2d'),W=cv.width,H=cv.height,l=79,r=36,t=45,b=58;
 const tx=x=>o.logx?Math.log10(x):x,ty=y=>o.logy?Math.log10(y):y;
 const x0=tx(o.xmin),x1=tx(o.xmax),y0=ty(o.ymin),y1=ty(o.ymax);
 const X=x=>l+(tx(x)-x0)/(x1-x0)*(W-l-r),Y=y=>t+(y1-ty(y))/(y1-y0)*(H-t-b);
 c.clearRect(0,0,W,H);c.fillStyle='#243743';c.textAlign='left';c.font='21px system-ui';c.fillText(o.title,l,24);
 c.font='17px system-ui';
 for(const y of o.yticks){c.strokeStyle='#e4ecef';c.lineWidth=1;c.beginPath();c.moveTo(l,Y(y));c.lineTo(W-r,Y(y));c.stroke();c.fillStyle='#435963';c.textAlign='right';c.fillText(o.logy?(y===1?'1':'10^'+Math.round(Math.log10(y))):fmt(y),l-9,Y(y)+5);}
 for(const x of o.xticks){c.strokeStyle='#e4ecef';c.beginPath();c.moveTo(X(x),t);c.lineTo(X(x),H-b);c.stroke();c.fillStyle='#435963';c.textAlign='center';c.fillText(o.xformat?o.xformat(x):fmt(x),X(x),H-b+24);}
 c.save();c.beginPath();c.rect(l,t,W-l-r,H-t-b);c.clip();
 for(const line of o.lines){c.strokeStyle=line.colour;c.lineWidth=line.width||2.6;c.setLineDash(line.dash||[]);c.beginPath();let started=false;for(let i=0;i<=1200;i++){const x=o.logx?10**(x0+(x1-x0)*i/1200):o.xmin+(o.xmax-o.xmin)*i/1200,y=line.fn(x);if(!Number.isFinite(y)||(o.logy&&y<=0)){started=false;continue;}if(!started){c.moveTo(X(x),Y(y));started=true;}else c.lineTo(X(x),Y(y));}c.stroke();}
 if(o.marker){c.setLineDash([4,4]);c.strokeStyle='#7d8d96';c.lineWidth=1.5;c.beginPath();c.moveTo(X(o.marker),t);c.lineTo(X(o.marker),H-b);c.stroke();}
 c.restore();c.setLineDash([]);c.strokeStyle='#879ba5';c.lineWidth=1;c.beginPath();c.moveTo(l,t);c.lineTo(l,H-b);c.lineTo(W-r,H-b);c.stroke();c.textAlign='center';c.font='18px system-ui';c.fillStyle='#243743';c.fillText(o.xlabel,(l+W-r)/2,H-11);
}
'''
WAVE_BODY='''<h2>A wave can fade without spreading</h2>
<p>Hold the electric field just inside the material fixed. Start with <strong>zero conductivity</strong>: dielectric loss alone can attenuate the wave. The common harmonic time factor is eʲωᵗ.</p>
<div class="controls">
<label>Frequency<output id="freq-label"></output><input id="freq" type="range" min="7" max="9" step="any" value="8" aria-label="Logarithmic frequency"></label>
<label>Real relative permittivity ε′/ε₀<output id="er-label"></output><input id="er" type="range" min="1" max="25" step=".1" value="4"></label>
<label>Dielectric loss ratio ε″d/ε′<output id="loss-label"></output><input id="loss" type="range" min="0" max="1" step=".005" value=".15"></label>
<label>Plot length<output id="length-label"></output><input id="length" type="range" min="-1" max="1" step="any" value=".47712125472" aria-label="Logarithmic plot length in metres"></label>
<label><input id="conduction" type="checkbox"> Add conduction<output id="sigma-label"></output><input id="sigma" type="range" min="-6" max="0" step="any" value="-2" aria-label="Logarithmic conductivity in siemens per metre" disabled></label>
<div><p><button id="play" type="button" aria-pressed="false">Play</button> <button id="reset" type="button">Reset</button></p><output id="clock"></output></div>
</div>
<p class="legend"><span class="blue">Blue: real E / E₀</span> · <span class="orange">Orange: real H / |H(0)|</span> · Grey dashed: ±e⁻ᵅᶻ envelopes. Time is slowed for viewing.</p>
<div class="plots"><canvas id="fields" width="650" height="340" role="img" aria-label="Normalized electric and magnetic components versus depth with fixed amplitude scales"></canvas><canvas id="power" width="650" height="340" role="img" aria-label="Mean Poynting flux relative to its value at zero depth"></canvas></div>
<div class="readout" aria-live="polite"><p id="k-value"></p><p id="wave-value"></p><p id="power-value"></p><p id="phase-value"></p></div>
<p class="hint">Changing the material can change S(0), because E₀ is held fixed. The power graph is S(z)/S(0), so it isolates decay inside each material. Field and power axes stay fixed. Frequency, length and conductivity sliders are logarithmic.</p>
<details><summary>Equations and assumptions</summary><p>εd/ε₀ = er − j er × loss ratio. εeff/ε₀ = er − j[er × loss ratio + σ/(ωε₀)]. k² = ω²μ₀εeff, k = β − jα with α ≥ 0, β &gt; 0. E(z)/E₀ = e⁻ᵅᶻe⁻ʲᵝᶻ and H(z) = k E(z)/(ωμ₀). The curves show their real parts after multiplication by eʲωᵗ. H has its own peak normalization so its phase is visible; its plotted height is not its SI magnitude relative to E.</p><p>S(z)/S(0) = e⁻²ᵅᶻ. The dielectric and conduction heating fractions are ωε″d/(ωε″d+σ) and σ/(ωε″d+σ). The medium is homogeneous, isotropic and has real μ=μ₀. These independent controls specify a single-frequency teaching model, not a fitted material spectrum. No reflection, geometric spreading or scattering is included.</p></details>'''
WAVE_JS=r'''
let phase=0,timer=null;
function state(){const f=10**Number(el('freq').value),er=Number(el('er').value),loss=Number(el('loss').value),sigma=el('conduction').checked?10**Number(el('sigma').value):0,L=10**Number(el('length').value);return {...physics(f,er,er*loss,sigma),L,loss};}
function draw(){
 const p=state(),L=p.L;el('freq-label').value=fmt(p.f/1e6,'MHz');el('er-label').value=fmt(p.er);el('loss-label').value=fmt(p.loss);el('length-label').value=fmt(L,'m');el('sigma').disabled=!el('conduction').checked;el('sigma-label').value=p.sigma===0?'σ = 0 (off)':fmt(p.sigma,'S/m');el('clock').value='Phase at z=0: '+(phase*180/Math.PI).toFixed(0)+'°';
 const opts={xmin:0,xmax:L,xticks:[0,L/4,L/2,3*L/4,L],xlabel:'Depth z (m)'};
 chart('fields',{...opts,ymin:-1.15,ymax:1.15,yticks:[-1,0,1],title:'Normalized real fields',lines:[{colour:'#a7b6bc',dash:[5,4],width:1.4,fn:z=>Math.exp(-p.alpha*z)},{colour:'#a7b6bc',dash:[5,4],width:1.4,fn:z=>-Math.exp(-p.alpha*z)},{colour:'#bd641d',fn:z=>Math.exp(-p.alpha*z)*Math.cos(phase-p.beta*z+p.hphase)},{colour:'#007fa8',fn:z=>Math.exp(-p.alpha*z)*Math.cos(phase-p.beta*z)}]});
 chart('power',{...opts,ymin:0,ymax:1.05,yticks:[0,.25,.5,.75,1],title:'Average flux S(z) / S(0)',lines:[{colour:'#007fa8',fn:z=>Math.exp(-2*p.alpha*z)}]});
 const total=p.w*EPS0*p.di+p.sigma,die=total===0?0:p.w*EPS0*p.di/total;
 el('k-value').textContent='α = '+fmt(p.alpha,'1/m')+'; β = '+fmt(p.beta,'rad/m')+'; k = β − jα.';
 el('wave-value').textContent='Wavelength = '+fmt(p.lambda,'m')+'; phase speed = '+fmt(p.v/C)+' c; field attenuation depth = '+fmt(p.depth,'m')+'.';
 el('power-value').textContent='At the end: field envelope '+(100*Math.exp(-p.alpha*L)).toPrecision(3)+'%; average flux '+(100*Math.exp(-2*p.alpha*L)).toPrecision(3)+'%. '+(total===0?'No heating.':'Heating: '+(100*die).toFixed(1)+'% dielectric, '+(100*(1-die)).toFixed(1)+'% conduction.');
 el('phase-value').textContent='H lags E by '+(-p.hphase*180/Math.PI).toFixed(2)+'°. The power curve is a time average and does not oscillate.';
 window.mediaWaveState=p;
}
function pause(){if(timer!==null)clearInterval(timer);timer=null;el('play').textContent='Play';el('play').setAttribute('aria-pressed','false');}
el('play').addEventListener('click',()=>{if(timer!==null){pause();return;}el('play').textContent='Pause';el('play').setAttribute('aria-pressed','true');timer=setInterval(()=>{phase=(phase+Math.PI/30)%(2*Math.PI);draw();},70);});
for(const id of ['freq','er','loss','length','sigma'])el(id).addEventListener('input',draw);
el('conduction').addEventListener('change',draw);
el('reset').addEventListener('click',()=>{pause();phase=0;for(const [k,v] of Object.entries({freq:'8',er:'4',loss:'.15',length:String(Math.log10(3)),sigma:'-2'}))el(k).value=v;el('conduction').checked=false;draw();});
document.addEventListener('visibilitychange',()=>{if(document.hidden)pause();});draw();
'''
PEN_BODY='''<h2>Frequency, material response and penetration</h2>
<p>The solid curve uses the full complex permittivity. Compare it with the dashed good-conductor approximation. The same formula need not work across every radar band.</p>
<div class="controls"><label>Illustrative material<select id="material" aria-label="Material example"><option value="dry">Dry-soil example</option><option value="wet">Wetter-soil example</option><option value="fresh">Freshwater-like example</option><option value="saline">Saline-water-like example</option></select></label>
<label>Selected frequency<output id="freq-label"></output><input id="freq" type="range" min="6" max="10" step="any" value="8" aria-label="Logarithmic selected frequency"></label>
<label>Reflector depth<output id="depth-label"></output><input id="depth" type="range" min="-3" max="2" step="any" value="0" aria-label="Logarithmic reflector depth in metres"></label></div>
<p id="parameters" class="hint"></p>
<p class="hint">Thin vertical line: selected frequency.</p>
<div class="plots"><div><canvas id="response" width="650" height="365" role="img" aria-label="Real permittivity, dielectric loss and conduction contribution on logarithmic axes"></canvas><p class="legend"><span class="blue">Blue: ε′/ε₀</span> · <span class="orange">Orange dashed: ε″d/ε₀</span> · <span class="green">Green dotted: σ/(ωε₀)</span></p></div><div><canvas id="penetration" width="650" height="365" role="img" aria-label="Exact field attenuation depth and good conductor approximation versus frequency on logarithmic axes"></canvas><p class="legend"><span class="blue">Blue: exact δE</span> · <span class="orange">Orange dashed: conductor approximation</span></p></div></div>
<div class="readout" aria-live="polite"><p id="material-value"></p><p id="depth-value"></p><p id="regime-value"></p><p id="echo-value"></p></div>
<p class="hint">Both plots use fixed logarithmic scales across presets. δE is a field-amplitude scale, not a maximum survey depth. Only absorption is included in the echo factors.</p>
<details><summary>Model parameters, scope and equations</summary><p>All presets are illustrative, not measured material fits. The soil examples have constant ε′ and constant dielectric loss ratio over this displayed band. Dry: ε′/ε₀=4, ε″d/ε′=0.005, σ=0.0001 S/m. Wetter: ε′/ε₀=16, ε″d/ε′=0.03, σ=0.02 S/m.</p><p>Both water-like examples use εd/ε₀ = 5 + 75/(1+jωτ), τ=9 ps; conductivity is 0.005 S/m for the freshwater-like example and 4 S/m for the saline example. This choice isolates added ionic conduction while holding the molecular response fixed. It does not reproduce the full temperature/salinity dependence of real water. For quantitative models see <a href="https://images.remss.com/papers/rsspubs/Meissner_TGRS_2004_dielectric.pdf" target="_blank" rel="noopener">Meissner and Wentz (2004)</a>.</p><p>εeff = εd − jσ/ω; k² = ω²μ₀εeff; δE = 1/α, with k=β−jα. The dashed depth is √[2/(ωμ₀σ)] and requires σ much greater than ω|εd|. The criterion uses the complete dielectric current, including dielectric loss. One-way power depth is δE/2. Down-and-back absorption factors at depth d are e⁻²ᵅᵈ for field and e⁻⁴ᵅᵈ for power. No surface transmission, reflection strength, scattering, spreading, instrument noise or frequency-dependent σ is modelled.</p></details><p><button id="reset" type="button">Reset</button></p>'''
PEN_JS=r'''
const MODELS=MODELDATA;
function material(f,key){const m=MODELS[key],w=2*Math.PI*f;if(m.kind==='constant')return {er:m.er,di:m.er*m.tan,sigma:m.sigma};const x=w*m.tau;return {er:m.einf+(m.es-m.einf)/(1+x*x),di:(m.es-m.einf)*x/(1+x*x),sigma:m.sigma};}
function prop(f,key){const m=material(f,key);return physics(f,m.er,m.di,m.sigma);}
function powerFactor(log10Value){return log10Value< -3?'10^('+log10Value.toFixed(1)+')':fmt(10**log10Value);}
function update(){
 const key=el('material').value,m=MODELS[key],f=10**Number(el('freq').value),d=10**Number(el('depth').value),p=prop(f,key);
 el('freq-label').value=fmt(f/1e6,'MHz');el('depth-label').value=fmt(d,'m');
 el('parameters').textContent=m.kind==='constant'?'Illustrative fixed parameters: ε′/ε₀ = '+m.er+', dielectric loss ratio = '+m.tan+', σ = '+fmt(m.sigma,'S/m')+'.':'Illustrative single relaxation: εs/ε₀ = '+m.es+', ε∞/ε₀ = '+m.einf+', τ = '+fmt(m.tau*1e12,'ps')+', σ = '+fmt(m.sigma,'S/m')+'. Molecular response held identical in both water-like cases.';
 const opts={xmin:1e6,xmax:1e10,logx:true,xticks:[1e6,1e7,1e8,1e9,1e10],xformat:x=>String(Math.round(x/1e6)),xlabel:'Frequency (MHz)',marker:f};
 chart('response',{...opts,ymin:1e-4,ymax:1e5,logy:true,yticks:[1e-4,1e-2,1,1e2,1e4],title:'Relative response components',lines:[{colour:'#007fa8',fn:x=>material(x,key).er},{colour:'#bd641d',dash:[7,4],fn:x=>material(x,key).di},{colour:'#63823a',dash:[2,4],fn:x=>m.sigma/(2*Math.PI*x*EPS0)}]});
 chart('penetration',{...opts,ymin:1e-4,ymax:1e4,logy:true,yticks:[1e-4,1e-2,1,1e2,1e4],title:'Field attenuation depth (m)',lines:[{colour:'#007fa8',fn:x=>prop(x,key).depth},{colour:'#bd641d',dash:[7,4],fn:x=>Math.sqrt(2/(2*Math.PI*x*MU0*m.sigma))}]});
 el('material-value').textContent='At this frequency: ε′/ε₀ = '+fmt(p.er)+'; dielectric ε″d/ε₀ = '+fmt(p.di)+'; conduction σ/(ωε₀) = '+fmt(p.ei-p.di)+'.';
 el('depth-value').textContent='Field depth δE = '+fmt(p.depth,'m')+'; one-way power depth = '+fmt(p.depth/2,'m')+'; wavelength inside = '+fmt(p.lambda,'m')+'.';
 el('regime-value').textContent='Conduction / dielectric-current magnitude = '+fmt(p.conductionRatio)+'. '+(p.conductionRatio>=10?'Conduction dominates: the skin-depth approximation is useful.':p.conductionRatio>=1?'The currents are comparable: use the full result.':'Conduction does not dominate: use the full result.');
 el('echo-value').textContent='At depth '+fmt(d,'m')+', round-trip absorption factor: field '+powerFactor(-2*p.alpha*d/Math.LN10)+'; power '+powerFactor(-4*p.alpha*d/Math.LN10)+' ('+fmt(40*p.alpha*d/Math.LN10,'dB')+' power loss).';
 window.mediaPenetrationState={...p,d,key};
}
for(const id of ['material','freq','depth'])el(id).addEventListener(id==='material'?'change':'input',update);
el('reset').addEventListener('click',()=>{el('material').value='dry';el('freq').value='8';el('depth').value='0';update();});update();
'''.replace('MODELDATA',json.dumps(MODELS))
def build():
 dest=ROOT/'interactives';dest.mkdir(exist_ok=True)
 for stem,title,body,js in [('media_wave','A decaying wave and its energy flux',WAVE_BODY,WAVE_JS),('media_penetration','Radar penetration through illustrative media',PEN_BODY,PEN_JS)]:
  page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+STYLE+'</style></head><body>'+body+'<script>'+COMMON+js+'</script></body></html>'
  (dest/(stem+'.html')).write_text(page)
  fragment='<iframe title="'+title+'" style="width:100%;height:1150px;border:0" sandbox="allow-scripts" loading="lazy" srcdoc="'+html.escape(page,quote=True)+'"></iframe>\n'
  (dest/(stem+'_embed.html')).write_text(fragment)
 print('Built two self-contained media explorers and their embedded versions.')
if __name__=='__main__':build()
