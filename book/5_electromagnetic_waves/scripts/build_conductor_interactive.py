"""Self-contained thin-sheet and conducting-half-space activity.

Peak phasors, exp(+j omega t). Exact homogeneous bulk response avoids applying
uniform-film conductance to a thick conductor. HTML runs on the static book host.
"""
from pathlib import Path
import html
ROOT=Path(__file__).resolve().parents[1]
STYLE='''*{box-sizing:border-box}body{margin:0;padding:14px;color:#253a46;background:white;font:15px system-ui,sans-serif}h2{font-size:22px;margin:0 0 8px}p{line-height:1.5;margin:8px 0}.controls{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:14px 0}label{display:block;font-weight:600}output{display:block;font-weight:400;min-height:23px;font-variant-numeric:tabular-nums}input[type=range],select{width:100%;accent-color:#007fa8}select{font:inherit;color:#253a46;padding:6px;border:1px solid #91a5af;background:white}button{font:inherit;color:#253a46;background:white;border:1px solid #78909b;border-radius:4px;padding:6px 12px}.actions{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:10px 0}.actions label{font-weight:400}.readout{font-variant-numeric:tabular-nums;line-height:1.6}.summary{background:#f2f7fa;padding:10px 12px}.hint,details,.legend{font-size:14px;color:#435963;line-height:1.5}canvas{display:block;width:100%;height:auto;margin:8px 0}.powers{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:12px 0}.track{height:16px;background:#e5edf0;border:1px solid #cad6dc;overflow:hidden}.fill{height:100%}.key{display:inline-block;width:20px;border-top:3px solid;vertical-align:middle;margin-right:4px}.blue{color:#007fa8}.purple{color:#8b467c}.green{color:#63823a}.orange{color:#b65e22}.question{padding:8px 12px;border-left:3px solid #b65e22;background:#fff7ee}summary{font-weight:600;cursor:pointer}details p{margin:8px 0}[hidden]{display:none!important}button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #007fa8;outline-offset:3px}@media(max-width:650px){.controls{grid-template-columns:1fr 1fr}.powers{grid-template-columns:1fr}body{font-size:14px}}@media(max-width:390px){.controls{grid-template-columns:1fr}}'''
BODY=r'''<h2>A small surface field, but a finite current</h2>
<p>Keep the incident wave fixed. Make the conductor better. Predict what happens to the <strong>total electric field at the surface</strong> and the <strong>current integrated through its thickness</strong>.</p>
<div class="controls"><label>Conductor model<output id="mode-label"></output><select id="mode"><option value="sheet">Thin conducting sheet</option><option value="bulk">Thick conductor: semi-infinite</option></select></label>
<label id="strength-control">Conductance / conductivity<output id="strength-label"></output><input id="strength" type="range" min="-6" max="4" step="any" value="-2.274993" aria-label="Logarithmic sheet conductance"></label>
<label>Oscillation phase ωt<output id="phase-label"></output><input id="phase" type="range" min="0" max="360" step="any" value="35" aria-label="Carrier oscillation phase in degrees"></label></div>
<div class="actions"><button id="weak" type="button">Weak conductor</button><button id="finite" type="button">Finite loss</button><button id="good" type="button">Almost perfect</button><button id="play" type="button" aria-pressed="false">Play wave</button><button id="reset" type="button">Reset</button><label><input id="components" type="checkbox"> Show incident and current-generated fields</label></div>
<div class="summary readout" aria-live="polite"><div id="surface-value"></div><div id="current-value"></div><div id="parameter-value"></div></div>
<p class="legend"><span class="blue"><span class="key"></span>Total field outside</span> · <span class="green"><span class="key"></span>Total field on the right</span> · Optional dashed curves: incident (grey), current-generated (orange).</p>
<canvas id="fields" width="1000" height="285" role="img" aria-label="Real electric field on both sides of the surface with fixed spatial and field scales"></canvas>
<p id="field-hint" class="hint"></p>
<p class="legend"><span class="blue"><span class="key"></span>Surface field amplitude |Eₛ|/Eᵢ</span> · <span class="purple"><span class="key"></span>Integrated current η₀|K|/Eᵢ</span>. The dashed level is the limiting current 2Eᵢ/η₀.</p>
<canvas id="limits" width="1000" height="285" role="img" aria-label="Surface electric field tending to zero and integrated current tending to a finite limit as conductivity or conductance increases"></canvas>
<div class="powers"><div><div id="R-label"></div><div class="track" role="meter" id="R-meter" aria-label="Reflected fraction" aria-valuemin="0" aria-valuemax="100"><div id="R-bar" class="fill" style="background:#b65e22"></div></div></div><div><div id="T-label"></div><div class="track" role="meter" id="T-meter" aria-label="Power leaving through the sheet or entering the thick conductor" aria-valuemin="0" aria-valuemax="100"><div id="T-bar" class="fill" style="background:#63823a"></div></div></div><div id="A-row"><div id="A-label"></div><div class="track" role="meter" id="A-meter" aria-label="Remaining power fraction" aria-valuemin="0" aria-valuemax="100"><div id="A-bar" class="fill" style="background:#8b467c"></div></div></div></div>
<p id="power-question" class="question"></p>
<button id="reveal" type="button" aria-expanded="false">Where does the remaining power go?</button>
<div id="answer" hidden><p id="power-answer"></p><canvas id="power" width="1000" height="285" role="img" aria-label="Power accounting for the selected conductor model"></canvas><p id="heat-check" class="readout"></p></div>
<details><summary>Equations, normalization and the two models</summary>
<p>Incident peak Eᵢ = 1 V/m, f = 100 MHz, and the external medium is vacuum with impedance η₀. The common time factor is eʲωᵗ. The upper field graph uses z/λ₀ on both sides and shows Re{E(z)eʲωᵗ}/Eᵢ. Its scales stay fixed. Carrier animation is slowed down. The limit graph shows phasor magnitudes, which do not oscillate.</p>
<p><strong>Thin sheet:</strong> x = η₀Gₛ, r = −x/(2+x), Eₛ/Eᵢ = t = 2/(2+x), and η₀K/Eᵢ = xt. ℛ = |r|², 𝒯 = |t|² and 𝒜 = x|t|². The same lossless medium is on both sides. Incident plus current-generated field gives the total field on each side.</p>
<p><strong>Thick conductor:</strong> a homogeneous conducting half-space fills z &gt; 0; there is no back face. Its background ε = ε₀ and μ = μ₀, and its finite conductivity σ supplies Joule heating. The exact model uses k² = ω²μ₀ε₀ − jωμ₀σ and k = β−jα, α &gt; 0. Surface impedance Zₛ = ωμ₀/k, r = (Zₛ−η₀)/(Zₛ+η₀), and Eₛ/Eᵢ = 1+r. Inside, E(z) = Eₛe⁻ᵅᶻe⁻ʲᵝᶻ and J(z) = σE(z).</p>
<p>The plotted integrated current is K = ∫₀∞J(z) dz = σEₛ/(α+jβ), in A/m. At finite conductivity this is an integrated volume current, rather than a literal delta sheet or a magnetic-field jump at the surface. In the good-conductor limit it approaches the tangential surface H. Here δE = 1/α is the field attenuation depth; it becomes the familiar skin depth in the conductive limit.</p>
<p>Mean power entering the half-space is Penter/Pincident = η₀ Re{1/Zₛ}|Eₛ/Eᵢ|² = 1−ℛ. At depth z it has the factor e⁻²ᵅᶻ. Mean heating per unit volume is σ|E(z)|²/2. Its integral accounts for all entered power. The power-depth plot uses z/δE to resolve the skin layer; that is a different scale from the upper field graph.</p>
<p>For a good conductor Zₛ ≈ (1+j)/(σδE). Its reciprocal has a phase as well as a conductance. A thick conductor is not modeled by inserting its full thickness into Gₛ = σh. The exact bulk formulas remain valid at the weaker-conductivity settings too.</p>
<p>With components visible in bulk mode, the grey incident field is mathematically continued into z &gt; 0. The orange current-generated field cancels much of that reference field there. The green sum is the actual field.</p>
</details>'''
JS=r'''
"use strict";
const LIGHT=299792458,EPS0=8.8541878128e-12,MU0=1/(EPS0*LIGHT*LIGHT),ETA0=1/(EPS0*LIGHT),F=1e8,W=2*Math.PI*F,K0=W/LIGHT,D=Math.PI/180;
const $=id=>document.getElementById(id);
const add=(a,b)=>[a[0]+b[0],a[1]+b[1]],sub=(a,b)=>[a[0]-b[0],a[1]-b[1]],scale=(a,s)=>[a[0]*s,a[1]*s],mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],div=(a,b)=>[(a[0]*b[0]+a[1]*b[1])/(b[0]*b[0]+b[1]*b[1]),(a[1]*b[0]-a[0]*b[1])/(b[0]*b[0]+b[1]*b[1])],abs=a=>Math.hypot(...a),real=(a,p)=>a[0]*Math.cos(p)-a[1]*Math.sin(p);
const fmt=x=>Math.abs(x)<1e-3&&x!==0||Math.abs(x)>=1e4?x.toExponential(3):Number(x.toPrecision(4)).toString(),pct=x=>fmt(100*x)+'%';
let revealed=false,playing=false,raf=null,lastTime=null;
function model(mode,strength){
 if(mode==='sheet'){
  const x=ETA0*strength,t=2/(2+x),r=-x/(2+x),e=[t,0],current=[x*t,0];
  return {mode,strength,x,r:[r,0],e,current,R:r*r,T:t*t,A:x*t*t,alpha:0,beta:K0,delta:Infinity,zs:null,min:-6,max:4};
 }
 const ratio=strength/(W*EPS0),nr=Math.sqrt((Math.hypot(1,ratio)+1)/2),ni=ratio/(2*nr),beta=K0*nr,alpha=K0*ni;
 const zr=div([1,0],[nr,-ni]),r=div(sub(zr,[1,0]),add(zr,[1,0])),e=div(scale(zr,2),add(zr,[1,0])),current=div(scale(e,ETA0*strength),[alpha,beta]);
 return {mode,strength,ratio,nr,ni,r,e,current,R:abs(r)**2,T:0,A:nr*abs(e)**2,alpha,beta,delta:1/alpha,zs:scale(zr,ETA0),min:-3,max:8};
}
function field(p,u,phase){
 const inc=Math.cos(phase-2*Math.PI*u);
 if(u<0){const gen=real(p.r,phase+2*Math.PI*u);return {inc,gen,total:inc+gen};}
 const z=u*LIGHT/F,total=p.mode==='sheet'?real(p.e,phase-2*Math.PI*u):Math.exp(-p.alpha*z)*real(p.e,phase-p.beta*z);
 return {inc,gen:total-inc,total};
}
function line(c,fn,x0,x1,X,Y,color,width=2.6,dash=[]){
 c.strokeStyle=color;c.lineWidth=width;c.setLineDash(dash);c.beginPath();for(let i=0;i<=850;i++){const x=x0+(x1-x0)*i/850,y=fn(x);if(i===0)c.moveTo(X(x),Y(y));else c.lineTo(X(x),Y(y));}c.stroke();c.setLineDash([]);
}
function frame(id,title,xmin,xmax,ymin,ymax,xticks,yticks,xlabel,yformat=x=>fmt(x),xformat=x=>fmt(x)){
 const cv=$(id),c=cv.getContext('2d'),l=69,r=25,t=44,b=47,X=x=>l+(x-xmin)/(xmax-xmin)*(cv.width-l-r),Y=y=>t+(ymax-y)/(ymax-ymin)*(cv.height-t-b);
 c.clearRect(0,0,cv.width,cv.height);c.fillStyle='#253a46';c.textAlign='left';c.font='21px system-ui';c.fillText(title,l,25);c.font='17px system-ui';
 for(const y of yticks){c.strokeStyle=y===0?'#b8c9d1':'#e0e9ed';c.lineWidth=1;c.beginPath();c.moveTo(l,Y(y));c.lineTo(cv.width-r,Y(y));c.stroke();c.fillStyle='#435963';c.textAlign='right';c.fillText(yformat(y),l-9,Y(y)+5);}
 for(const x of xticks){c.fillStyle='#435963';c.textAlign='center';c.fillText(xformat(x),X(x),cv.height-b+23);}
 c.fillStyle='#253a46';c.textAlign='center';c.fillText(xlabel,(l+cv.width-r)/2,cv.height-7);
 return {c,cv,l,r,t,b,X,Y};
}
function fieldsPlot(p){
 const phase=Number($('phase').value)*D,g=frame('fields','Real electric field Eₓ / Eᵢ',-1,.7,-2.05,2.05,[-1,-.5,0,.5],[-2,-1,0,1,2],'Position z / λ₀ (same spatial scale on both sides)'),{c,cv,l,r,t,b,X,Y}=g;
 c.save();c.beginPath();c.rect(l,t,cv.width-l-r,cv.height-t-b);c.clip();
 if($('components').checked){line(c,u=>field(p,u,phase).inc,-1,.7,X,Y,'#7d8d96',1.8,[7,5]);line(c,u=>field(p,u,phase).gen,-1,0,X,Y,'#b65e22',1.8,[5,4]);line(c,u=>field(p,u,phase).gen,0,.7,X,Y,'#b65e22',1.8,[5,4]);}
 line(c,u=>field(p,u,phase).total,-1,0,X,Y,'#007fa8',3);line(c,u=>field(p,u,phase).total,0,.7,X,Y,'#63823a',3);
 c.strokeStyle='#253a46';c.lineWidth=1.5;c.beginPath();c.moveTo(X(0),t);c.lineTo(X(0),cv.height-b);c.stroke();c.fillStyle='#253a46';c.beginPath();c.arc(X(0),Y(real(p.e,phase)),4.5,0,2*Math.PI);c.fill();c.restore();
 c.font='16px system-ui';c.textAlign='left';c.fillStyle='#435963';c.fillText('Incident side',l+10,t+18);c.fillText(p.mode==='sheet'?'Other side of sheet':'Conducting half-space',X(0)+10,t+18);
}
function limitsPlot(p){
 const xt=p.mode==='sheet'?[-6,-4,-2,0,2,4]:[-3,-1,1,3,5,7],g=frame('limits','Surface field falls; integrated current reaches a plateau',p.min,p.max,0,2.12,xt,[0,.5,1,1.5,2],p.mode==='sheet'?'Sheet conductance Gₛ (S), logarithmic scale':'Conductivity σ (S/m), logarithmic scale',fmt,x=>'10^'+x),{c,cv,r,t,b,l,X,Y}=g;
 line(c,x=>abs(model(p.mode,10**x).e),p.min,p.max,X,Y,'#007fa8',3);line(c,x=>abs(model(p.mode,10**x).current),p.min,p.max,X,Y,'#8b467c',3);
 c.strokeStyle='#8b467c';c.lineWidth=1.2;c.setLineDash([5,4]);c.beginPath();c.moveTo(l,Y(2));c.lineTo(cv.width-r,Y(2));c.stroke();c.setLineDash([]);
 const x=Math.log10(p.strength);c.strokeStyle='#253a46';c.beginPath();c.moveTo(X(x),t);c.lineTo(X(x),cv.height-b);c.stroke();
 for(const [v,col] of [[abs(p.e),'#007fa8'],[abs(p.current),'#8b467c']]){c.fillStyle=col;c.beginPath();c.arc(X(x),Y(v),4.5,0,2*Math.PI);c.fill();}
}
function powerPlot(p){
 if(p.mode==='sheet'){
  const {c,cv,t,b,X,Y}=frame('power','Thin sheet: reflected, transmitted and absorbed fractions',p.min,p.max,0,1.05,[-6,-4,-2,0,2,4],[0,.25,.5,.75,1],'Sheet conductance Gₛ (S), logarithmic scale',x=>(100*x).toFixed(0)+'%',x=>'10^'+x);
  for(const [key,col] of [['R','#b65e22'],['T','#63823a'],['A','#8b467c']])line(c,x=>model('sheet',10**x)[key],p.min,p.max,X,Y,col,2.8);
  c.strokeStyle='#253a46';c.lineWidth=1.2;c.beginPath();c.moveTo(X(Math.log10(p.strength)),t);c.lineTo(X(Math.log10(p.strength)),cv.height-b);c.stroke();
  $('heat-check').textContent='Orange: reflected; green: transmitted; purple: sheet heating. At your setting ℛ + 𝒯 + 𝒜 = '+fmt(p.R+p.T+p.A)+'. Mean sheet heating = '+fmt(p.A/(2*ETA0))+' W/m².';
 }else{
  const {c,X,Y}=frame('power','Inside the conductor: flux falls, deposited heat accumulates',0,5,0,1.05,[0,1,2,3,4,5],[0,.25,.5,.75,1],'Depth z / δE (zoomed skin-layer scale)',x=>(100*x).toFixed(0)+'%');
  line(c,z=>p.A*Math.exp(-2*z),0,5,X,Y,'#007fa8',3);line(c,z=>p.A*(-Math.expm1(-2*z)),0,5,X,Y,'#b65e22',3);
  $('heat-check').textContent='Blue: power still flowing into the conductor; orange: heat deposited between 0 and z. Both are fractions of incident power. One field attenuation depth is '+fmt(p.delta)+' m. At that depth, '+pct(Math.exp(-2))+' of the entered power remains as flux.';
 }
}
function draw(){
 const mode=$('mode').value,p=model(mode,10**Number($('strength').value)),e=abs(p.e),k=abs(p.current);
 $('mode-label').value=mode==='sheet'?'Two open sides, a localized sheet':'No back face; current occupies a skin layer';
 $('strength-label').value=mode==='sheet'?'Gₛ = '+fmt(p.strength)+' S; η₀Gₛ = '+fmt(p.x):'σ = '+fmt(p.strength)+' S/m';$('phase-label').value=Number($('phase').value).toFixed(0)+'°';
 $('surface-value').textContent='Surface electric amplitude |Eₛ| = '+fmt(e)+' V/m ('+fmt(e)+' × the incident amplitude).';
 $('current-value').textContent=(mode==='sheet'?'Sheet current':'Depth-integrated conduction current')+' |K| = '+fmt(1000*k/ETA0)+' mA/m; '+pct(k/2)+' of its limiting value 2Eᵢ/η₀ = '+fmt(2000/ETA0)+' mA/m.';
 $('parameter-value').textContent=mode==='sheet'?'Eₛ = Eᵢ + Eemitted; K = GₛEₛ. Improve the conductor while holding Eᵢ = 1 V/m fixed.':'Zₛ = '+fmt(p.zs[0])+' + j'+fmt(p.zs[1])+' Ω; δE = '+fmt(p.delta)+' m; σ/(ωε₀) = '+fmt(p.ratio)+'.';
 $('field-hint').textContent=mode==='sheet'?'The surface value tends to zero. The exterior field can still form a standing-wave pattern. The current limit is a finite value, not zero.':'The actual field decays inside the conducting half-space. For a good conductor the skin layer is too thin to resolve on this wavelength scale; reveal the power plot to zoom into it.';
 fieldsPlot(p);limitsPlot(p);
 $('R-label').textContent='Reflected: '+pct(p.R);$('T-label').textContent=(mode==='sheet'?'Transmitted through sheet: ':'Entering the conductor: ')+pct(mode==='sheet'?p.T:p.A);
 $('A-row').hidden=mode!=='sheet';$('A-label').textContent=(revealed?'Sheet heating: ':'Remainder: ')+pct(p.A);
 for(const [key,v] of [['R',p.R],['T',mode==='sheet'?p.T:p.A],['A',p.A]]){$(key+'-bar').style.width=(100*v)+'%';$(key+'-meter').setAttribute('aria-valuenow',String(100*v));}
 $('power-question').textContent=mode==='sheet'?'Compare reflected plus transmitted power with the incident power. Where does the remainder go? Does making the sheet more conductive always increase that remainder?':'Some incoming power is not reflected. This conductor has no back face: where does the entered power go, and what should its flux do with depth?';
 $('answer').hidden=!revealed;$('reveal').textContent=revealed?'Hide power explanation':'Where does the remaining power go?';$('reveal').setAttribute('aria-expanded',String(revealed));
 $('power-answer').textContent=mode==='sheet'?'The remainder heats the sheet: ⟨pheat⟩ = Gₛ|Eₛ|²/2 per unit area. In the perfect-conductor limit the surface field and absorption vanish, while the current approaches 2Eᵢ/η₀.':'The entered power becomes Joule heat in the skin layer: ⟨q⟩ = σ|E(z)|²/2. The decreasing Poynting flux and integrated heating account for it together. ℛ + entered fraction = '+fmt(p.R+p.A)+'.';
 if(revealed)powerPlot(p);window.conductorReflectionState={...p,phase:Number($('phase').value),revealed};
}
function stop(){playing=false;if(raf!==null)cancelAnimationFrame(raf);raf=null;lastTime=null;$('play').textContent='Play wave';$('play').setAttribute('aria-pressed','false');}
function tick(now){if(!playing)return;if(lastTime!==null)$('phase').value=String((Number($('phase').value)+Math.min(now-lastTime,100)*.07)%360);lastTime=now;draw();raf=requestAnimationFrame(tick);}
function configure(){stop();revealed=false;const sheet=$('mode').value==='sheet';$('strength').min=sheet?'-6':'-3';$('strength').max=sheet?'4':'8';$('strength').value=String(Math.log10(sheet?2/ETA0:.1));$('strength').setAttribute('aria-label',sheet?'Logarithmic sheet conductance in siemens':'Logarithmic bulk conductivity in siemens per metre');draw();}
$('mode').addEventListener('change',configure);$('strength').addEventListener('input',draw);$('phase').addEventListener('input',()=>{stop();draw();});$('components').addEventListener('change',draw);
for(const [id,x,sigma] of [['weak',.03,.001],['finite',2,.1],['good',1e5,1e7]])$(id).addEventListener('click',()=>{$('strength').value=String(Math.log10($('mode').value==='sheet'?x/ETA0:sigma));draw();});
$('reveal').addEventListener('click',()=>{revealed=!revealed;draw();});$('play').addEventListener('click',()=>{if(playing){stop();return;}playing=true;lastTime=null;$('play').textContent='Pause wave';$('play').setAttribute('aria-pressed','true');raf=requestAnimationFrame(tick);});
$('reset').addEventListener('click',()=>{$('mode').value='sheet';$('phase').value='35';$('components').checked=false;configure();});document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();});configure();
'''
def build(root=ROOT):
    dest=root/'interactives';dest.mkdir(exist_ok=True)
    title='Conducting reflection: surface fields, current and power'
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+STYLE+'</style></head><body>'+BODY+'<script>'+JS+'</script></body></html>'
    (dest/'conductor_reflection.html').write_text(page)
    (dest/'conductor_reflection_embed.html').write_text('<iframe title="'+title+'" style="width:100%;height:1660px;border:0" sandbox="allow-scripts" loading="lazy" srcdoc="'+html.escape(page,quote=True)+'"></iframe>\n')
if __name__=='__main__':build()
