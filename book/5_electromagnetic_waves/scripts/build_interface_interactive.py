"""Build a self-contained TeachBook activity: moisture, field matching and reflection.

Python creates both HTML forms. Browser calculations run on the static book host.
The real, lossless mixing example is illustrative, with fixed porosity/constituents.
"""
from pathlib import Path
import html,json
ROOT=Path(__file__).resolve().parents[1]
PARAMETERS=dict(porosity=.45,solid=5.,water=80.,air=1.,frequency=300e6,incident=1.)
STYLE=r'''*{box-sizing:border-box}body{margin:0;padding:14px;color:#253a46;background:white;font:15px system-ui,sans-serif}h2{font-size:22px;margin:0 0 8px}p{line-height:1.5;margin:8px 0}.controls{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:15px;margin:15px 0}label{font-weight:600;display:block}output{display:block;font-weight:400;font-variant-numeric:tabular-nums;min-height:23px}input[type=range]{width:100%;accent-color:#007fa8}input[type=checkbox]{accent-color:#007fa8}.actions{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:10px 0}button{font:inherit;background:white;border:1px solid #78909b;border-radius:4px;padding:6px 12px;color:#253a46}.legend,.hint,details{font-size:14px;line-height:1.5;color:#435963}.key{display:inline-block;width:20px;border-top:3px solid;vertical-align:middle;margin-right:5px}.air{color:#007fa8}.soil{color:#63823a}.reflected{color:#b65e22}.fields canvas{display:block;width:100%;height:auto;margin:7px 0}.powers{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:10px 0}.power-track{height:16px;background:#e5edf0;overflow:hidden;border:1px solid #cad6dc}.power-fill{height:100%}.readout{font-variant-numeric:tabular-nums;line-height:1.6}.summary{padding:9px 12px;background:#f2f7fa;margin-top:10px}.history canvas{display:block;width:100%;height:auto}summary{cursor:pointer;font-weight:600}details p{margin:8px 0}button:focus-visible,input:focus-visible{outline:3px solid #007fa8;outline-offset:3px}@media(max-width:620px){.controls{grid-template-columns:1fr 1fr}.powers{grid-template-columns:1fr}body{font-size:14px}}@media(max-width:390px){.controls{grid-template-columns:1fr}}'''
BODY=r'''<h2>Rain changes the soil. What happens to the reflected wave?</h2>
<p>Keep the transmitter and interface fixed. Change the <strong>volumetric water content</strong>—the fraction of the whole soil volume occupied by water—and watch the material response and field matching change.</p>
<div class="controls">
<label>Soil water content<output id="moisture-label"></output><input id="moisture" type="range" min="0" max="45" step=".1" value="5" aria-label="Volumetric soil water content in percent"></label>
<label>Oscillation phase ωt<output id="phase-label"></output><input id="phase" type="range" min="0" max="360" step="any" value="35" aria-label="Carrier oscillation phase in degrees"></label>
<label>Example: rain, then drying<output id="day-label"></output><input id="day" type="range" min="0" max="10" step=".05" value="0" aria-label="Day in an illustrative rain and drying sequence"></label>
</div>
<div class="actions"><button id="dry" type="button">Before rain</button><button id="rain" type="button">After rain</button><button id="drying" type="button">Drying out</button><button id="play" type="button" aria-pressed="false">Play wave</button><button id="reset" type="button">Reset</button><label><input id="components" type="checkbox"> Show incident and reflected components</label></div>
<p class="hint">The day sequence represents separate visits to the same ground. The phase control shows one much faster wave cycle, slowed for viewing. Each moisture setting is a steady harmonic solution.</p>
<div class="readout summary" aria-live="polite"><div id="material"></div><div id="coefficients"></div></div>
<p class="legend"><span class="air"><span class="key"></span>Total field in air</span> · <span class="soil"><span class="key"></span>Transmitted field in soil</span>. Optional dashed curves: incident (grey), reflected (orange).</p>
<div class="fields"><canvas id="electric" width="1000" height="270" role="img" aria-label="Real electric field across the interface with a fixed amplitude scale"></canvas><canvas id="magnetic" width="1000" height="270" role="img" aria-label="Real magnetic field across the interface normalized by the incident magnetic amplitude"></canvas></div>
<div class="readout" id="boundary"></div>
<div class="powers"><div><div id="reflected-label" class="readout"></div><div class="power-track" role="meter" id="reflected-meter" aria-label="Reflected fraction of incident power" aria-valuemin="0" aria-valuemax="100"><div class="power-fill" id="reflected-bar" style="background:#b65e22"></div></div></div><div><div id="transmitted-label" class="readout"></div><div class="power-track" role="meter" id="transmitted-meter" aria-label="Transmitted fraction of incident power" aria-valuemin="0" aria-valuemax="100"><div class="power-fill" id="transmitted-bar" style="background:#63823a"></div></div></div></div>
<p class="readout" id="comparison"></p>
<div class="history"><canvas id="history" width="1000" height="270" role="img" aria-label="Modeled plane-interface reflected power over an illustrative rain and drying sequence"></canvas></div>
<p class="hint" id="history-hint"></p>
<details><summary>Read the model and its assumptions</summary>
<p>The soil has fixed porosity φ = 0.45. Mineral grains occupy 1−φ, water occupies θᵥ and air occupies φ−θᵥ. Water replaces pore air; it does not replace the mineral grains. The illustration uses real relative permittivities εᵣ,solid = 5, εᵣ,water = 80 and εᵣ,air = 1:</p>
<p>√εᵣ,soil = (1−φ)√εᵣ,solid + θᵥ√εᵣ,water + (φ−θᵥ)√εᵣ,air.</p>
<p>All media are nonmagnetic and lossless here. At fixed f = 300 MHz, k₂/k₁ = √εᵣ,soil, η₂/η₁ = 1/√εᵣ,soil, and λ₂/λ₁ = 1/√εᵣ,soil. With the common factor eʲωᵗ, E₁/Eᵢ = e⁻ʲᵏ¹ᶻ + r e⁺ʲᵏ¹ᶻ and E₂/Eᵢ = t e⁻ʲᵏ²ᶻ. The reflected H has the opposite companion sign. r = (η₂−η₁)/(η₂+η₁), t = 1+r, ℛ = |r|² and 𝒯 = (η₁/η₂)|t|².</p>
<p>Electric amplitude Eᵢ = 1 V/m. H is normalized by Eᵢ/η₁ so it fits on a dimensionless graph. Fixed axes let you compare moisture settings. At the interface, E and H each match across the boundary; E and H do not have the same physical units.</p>
<p>The illustrative weather sequence starts at 5% water content, rises to 30% between days 1 and 2, then dries towards 5% with a three-day exponential time scale. This is a supplied scenario, not a soil-water forecast. Moving the moisture slider chooses a custom state outside that day sequence.</p>
<p>This activity isolates the material dependence of normal-incidence reflection. It supplies a building block for interpreting changing radar echoes. Off-nadir radar backscatter also needs target geometry and roughness; this graph is not a prediction of radar σ⁰. Dielectric loss, conductivity, vegetation, changing roughness and subsurface reflectors are outside this activity. The mixing parameters are teaching choices, not a calibrated soil retrieval.</p>
<p>Background: <a href="https://em.geosci.xyz/content/physical_properties/dielectric_permittivity/dielectric_permittivity_factors.html" target="_blank" rel="noopener">EM GeoSci: porosity, saturation and dielectric response</a>.</p></details>'''
JS=r'''
"use strict";
const P=__PARAMETERS__,C=299792458,EPS0=8.8541878128e-12,ETA0=1/(EPS0*C),D=Math.PI/180;
const $=id=>document.getElementById(id);
let historyActive=true,playing=false,raf=null,lastTime=null;
function moistureAtDay(day){return day<1?.05:day<2?.05+.25*(day-1):.05+.25*Math.exp(-(day-2)/3);}
function model(theta,phaseDegrees=0){
 const n=(1-P.porosity)*Math.sqrt(P.solid)+theta*Math.sqrt(P.water)+(P.porosity-theta)*Math.sqrt(P.air);
 const er=n*n,eta=ETA0/n,r=(1-n)/(1+n),t=2/(1+n),R=r*r,T=n*t*t;
 return {theta,n,er,eta,r,t,R,T,k1:2*Math.PI*P.frequency/C,k2:2*Math.PI*P.frequency/C*n,lambda1:C/P.frequency,lambda2:C/P.frequency/n,phase:phaseDegrees*D};
}
function fields(p,z){
 const incident=Math.cos(p.phase-p.k1*z),reflected=p.r*Math.cos(p.phase+p.k1*z),transmitted=p.t*Math.cos(p.phase-p.k2*z);
 return {ei:incident,er:reflected,et:transmitted,hi:incident,hr:-reflected,ht:p.n*transmitted,E:z<=0?incident+reflected:transmitted,H:z<=0?incident-reflected:p.n*transmitted};
}
function line(c,fn,xmin,xmax,X,Y,color,width=2.5,dash=[]){
 c.strokeStyle=color;c.lineWidth=width;c.setLineDash(dash);c.beginPath();for(let i=0;i<=850;i++){const x=xmin+(xmax-xmin)*i/850;if(i===0)c.moveTo(X(x),Y(fn(x)));else c.lineTo(X(x),Y(fn(x)));}c.stroke();c.setLineDash([]);
}
function fieldPlot(id,p,magnetic){
 const cv=$(id),c=cv.getContext('2d'),W=cv.width,H=cv.height,l=67,r=25,top=43,b=43,xmin=-1,xmax=.7,ymax=2.05;
 const X=x=>l+(x-xmin)/(xmax-xmin)*(W-l-r),Y=y=>top+(ymax-y)/(2*ymax)*(H-top-b);
 c.clearRect(0,0,W,H);c.fillStyle='#f2f7fa';c.fillRect(l,top,X(0)-l,H-top-b);c.fillStyle='#fff7ee';c.fillRect(X(0),top,W-r-X(0),H-top-b);
 c.fillStyle='#253a46';c.font='21px system-ui';c.textAlign='left';c.fillText(magnetic?'Magnetic field: η₁ Hᵧ / Eᵢ':'Electric field: Eₓ / Eᵢ',l,25);
 c.font='17px system-ui';
 for(const y of [-2,-1,0,1,2]){c.strokeStyle=y===0?'#b7c7cf':'#e0e9ed';c.lineWidth=1;c.beginPath();c.moveTo(l,Y(y));c.lineTo(W-r,Y(y));c.stroke();c.fillStyle='#435963';c.textAlign='right';c.fillText(String(y),l-9,Y(y)+5);}
 for(const x of [-1,-.5,0,.5]){c.fillStyle='#435963';c.textAlign='center';c.fillText(String(x),X(x),H-b+23);}
 c.save();c.beginPath();c.rect(l,top,W-l-r,H-top-b);c.clip();
 if($('components').checked){line(c,z=>fields(p,z)[magnetic?'hi':'ei'],xmin,0,X,Y,'#7d8d96',1.8,[7,5]);line(c,z=>fields(p,z)[magnetic?'hr':'er'],xmin,0,X,Y,'#b65e22',1.8,[5,4]);}
 line(c,z=>fields(p,z)[magnetic?'H':'E'],xmin,0,X,Y,'#007fa8',3);
 line(c,z=>fields(p,z)[magnetic?'ht':'et'],0,xmax,X,Y,'#63823a',3);
 c.strokeStyle='#253a46';c.lineWidth=1.5;c.beginPath();c.moveTo(X(0),top);c.lineTo(X(0),H-b);c.stroke();
 const v=magnetic?p.n*p.t*Math.cos(p.phase):p.t*Math.cos(p.phase);c.fillStyle='#253a46';c.beginPath();c.arc(X(0),Y(v),4.5,0,2*Math.PI);c.fill();c.restore();
 c.fillStyle='#435963';c.textAlign='left';c.font='16px system-ui';c.fillText('Air',l+10,top+18);c.fillText('Soil',X(0)+10,top+18);c.textAlign='center';c.font='17px system-ui';c.fillText('Position z (m); interface at z = 0',(l+W-r)/2,H-5);
}
function historyPlot(p){
 const cv=$('history'),c=cv.getContext('2d'),W=cv.width,H=cv.height,l=67,r=25,top=44,b=43;
 const X=x=>l+x/10*(W-l-r),Y=y=>top+(.5-y)/.5*(H-top-b);
 c.clearRect(0,0,W,H);c.fillStyle='#253a46';c.font='21px system-ui';c.textAlign='left';c.fillText('A changing surface: reflected fraction ℛ over days',l,25);
 c.fillStyle='#eaf1f5';c.fillRect(X(1),top,X(2)-X(1),H-top-b);c.fillStyle='#435963';c.font='15px system-ui';c.fillText('Rain',X(1)+8,top+18);
 c.font='17px system-ui';for(const y of [0,.1,.2,.3,.4,.5]){c.strokeStyle='#e0e9ed';c.lineWidth=1;c.beginPath();c.moveTo(l,Y(y));c.lineTo(W-r,Y(y));c.stroke();c.fillStyle='#435963';c.textAlign='right';c.fillText((100*y).toFixed(0)+'%',l-9,Y(y)+5);}
 for(const x of [0,2,4,6,8,10]){c.textAlign='center';c.fillText(String(x),X(x),H-b+22);}
 line(c,d=>model(moistureAtDay(d)).R,0,10,X,Y,'#b65e22',3);
 c.strokeStyle='#7d8d96';c.lineWidth=1.4;c.setLineDash([5,4]);c.beginPath();c.moveTo(l,Y(p.R));c.lineTo(W-r,Y(p.R));c.stroke();c.setLineDash([]);
 if(historyActive){const day=Number($('day').value);c.strokeStyle='#253a46';c.beginPath();c.moveTo(X(day),top);c.lineTo(X(day),H-b);c.stroke();c.fillStyle='#253a46';c.beginPath();c.arc(X(day),Y(p.R),5,0,2*Math.PI);c.fill();}
 c.fillStyle='#253a46';c.textAlign='center';c.fillText('Day in the illustrative wetting/drying sequence',(l+W-r)/2,H-5);
}
function draw(){
 const p=model(Number($('moisture').value)/100,Number($('phase').value)),ref=model(.05);
 $('moisture-label').value=(100*p.theta).toFixed(1)+'% of soil volume';$('phase-label').value=Number($('phase').value).toFixed(0)+'°';
 $('day-label').value=historyActive?'Day '+Number($('day').value).toFixed(2):'Custom moisture; choose a day to rejoin';
 $('material').textContent='Water content → εᵣ = '+p.er.toFixed(2)+' → ηsoil = '+p.eta.toFixed(1)+' Ω; wavelength in soil = '+p.lambda2.toFixed(3)+' m.';
 $('coefficients').textContent='Electric amplitude coefficients: r = '+p.r.toFixed(3)+', t = '+p.t.toFixed(3)+'. Frequency = 300 MHz; incident peak Eᵢ = 1 V/m.';
 const E=p.t*Math.cos(p.phase),H=p.n*p.t/ETA0*Math.cos(p.phase);
 $('boundary').textContent='At z = 0: E₁ₓ = E₂ₓ = '+E.toFixed(3)+' V/m; H₁ᵧ = H₂ᵧ = '+(1000*H).toFixed(3)+' mA/m. Both fields match across the interface.';
 $('reflected-label').textContent='Reflected power ℛ = '+(100*p.R).toFixed(1)+'%';$('transmitted-label').textContent='Transmitted power 𝒯 = '+(100*p.T).toFixed(1)+'%';
 for(const [key,v] of [['reflected',p.R],['transmitted',p.T]]){$(key+'-bar').style.width=(100*v)+'%';$(key+'-meter').setAttribute('aria-valuenow',String(100*v));}
 $('comparison').textContent='ℛ + 𝒯 = '+(p.R+p.T).toFixed(3)+'. Reflected power is '+(p.R/ref.R).toFixed(2)+' × the before-rain value, with the same illumination.';
 $('history-hint').textContent=historyActive?'The dot marks this visit; the dashed line is its reflected-power fraction. Change the day to follow wetting and drying.':'The dashed line marks your custom moisture state; the weather curve remains the supplied example.';
 fieldPlot('electric',p,false);fieldPlot('magnetic',p,true);historyPlot(p);
 window.interfaceFieldsState={...p,historyActive,day:Number($('day').value)};
}
function stop(){playing=false;if(raf!==null)cancelAnimationFrame(raf);raf=null;lastTime=null;$('play').textContent='Play wave';$('play').setAttribute('aria-pressed','false');}
function tick(now){if(!playing)return;if(lastTime!==null)$('phase').value=String((Number($('phase').value)+Math.min(now-lastTime,100)*.07)%360);lastTime=now;draw();raf=requestAnimationFrame(tick);}
function chooseDay(day){historyActive=true;$('day').value=String(day);$('moisture').value=String(100*moistureAtDay(day));draw();}
$('moisture').addEventListener('input',()=>{historyActive=false;draw();});$('day').addEventListener('input',()=>chooseDay(Number($('day').value)));
$('phase').addEventListener('input',()=>{stop();draw();});$('components').addEventListener('change',draw);
$('dry').addEventListener('click',()=>chooseDay(0));$('rain').addEventListener('click',()=>chooseDay(2));$('drying').addEventListener('click',()=>chooseDay(5));
$('play').addEventListener('click',()=>{if(playing){stop();return;}playing=true;lastTime=null;$('play').textContent='Pause wave';$('play').setAttribute('aria-pressed','true');raf=requestAnimationFrame(tick);});
$('reset').addEventListener('click',()=>{stop();$('phase').value='35';$('components').checked=false;chooseDay(0);});
document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();});draw();
'''
def build(root=ROOT):
    dest=root/'interactives';dest.mkdir(exist_ok=True)
    js=JS.replace('__PARAMETERS__',json.dumps(PARAMETERS))
    title='Match the fields: soil moisture and reflection'
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+STYLE+'</style></head><body>'+BODY+'<script>'+js+'</script></body></html>'
    (dest/'interface_fields.html').write_text(page)
    (dest/'interface_fields_embed.html').write_text('<iframe title="'+title+'" style="width:100%;height:1510px;border:0" sandbox="allow-scripts" loading="lazy" srcdoc="'+html.escape(page,quote=True)+'"></iframe>\n')
if __name__=='__main__':build()
