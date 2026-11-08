"""Build self-contained inline activities for the plane-wave TeachBook page.

Matches the potential-fields pattern: Python prepares the embedded HTML; small
browser-side calculations keep the sliders live on the static book host.
Run from any directory. No kernel or external runtime is required by readers.
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parents[1]
STYLE = '''
*{box-sizing:border-box}body{font:15px system-ui,sans-serif;color:#243743;background:#fff;margin:0;padding:12px}label{display:block;font-weight:600;margin:8px 0}input[type=range]{width:100%;accent-color:#008dab}output{font-weight:400;font-variant-numeric:tabular-nums}button{font:inherit;border:1px solid #78909b;border-radius:4px;background:#fff;padding:6px 15px;cursor:pointer}.controls{display:grid;grid-template-columns:1fr 1fr;gap:10px 24px}.plots{display:grid;grid-template-columns:1fr 1fr;gap:12px}canvas{width:100%;height:auto;border:1px solid #ccd8de;background:#fff}.readout{line-height:1.7;padding:8px 0;font-variant-numeric:tabular-nums}.hint{color:#435963;font-size:14px;margin:6px 0}.title{font-weight:600;margin:4px 0 8px} @media(max-width:650px){.plots,.controls{grid-template-columns:1fr}.hint{font-size:13px}}
'''
COMMON = '''
"use strict";
const C=3e8;
function pulse(tau){const s=tau/60e-9,w=1+0.65*Math.tanh(s);return Math.exp(-((s/w)**2));}
function plot(id,fn,xmax,xlabel,title,colour,ymin=-1.2){
 const el=document.getElementById(id),ctx=el.getContext('2d'),W=el.width,H=el.height;
 const L=48,R=18,T=32,B=46,ymax=1.3;
 const xpx=x=>L+x/xmax*(W-L-R),ypx=y=>T+(ymax-y)/(ymax-ymin)*(H-T-B);
 ctx.clearRect(0,0,W,H);ctx.font='18px system-ui';ctx.textAlign='left';ctx.fillStyle='#243743';ctx.fillText(title,L,19);
 ctx.font='17px system-ui';
 for(let j=0;j<=4;j++){const x=xmax*j/4;ctx.strokeStyle='#e5ecef';ctx.beginPath();ctx.moveTo(xpx(x),T);ctx.lineTo(xpx(x),H-B);ctx.stroke();ctx.fillStyle='#435963';ctx.textAlign='center';ctx.fillText(Number(x.toPrecision(3)).toString(),xpx(x),H-B+18);}
 for(const y of (ymin>-.5?[0,.5,1]:[-1,-.5,0,.5,1])){ctx.strokeStyle='#e5ecef';ctx.beginPath();ctx.moveTo(L,ypx(y));ctx.lineTo(W-R,ypx(y));ctx.stroke();ctx.textAlign='right';ctx.fillStyle='#435963';ctx.fillText(y.toString(),L-7,ypx(y)+4);}
 ctx.strokeStyle='#627d89';ctx.strokeRect(L,T,W-L-R,H-T-B);ctx.textAlign='center';ctx.fillStyle='#243743';ctx.fillText(xlabel,(L+W-R)/2,H-8);
 ctx.save();ctx.beginPath();ctx.rect(L,T,W-L-R,H-T-B);ctx.clip();ctx.strokeStyle=colour;ctx.lineWidth=2.4;ctx.beginPath();
 for(let j=0;j<=900;j++){let x=xmax*j/900,y=fn(x);if(j===0)ctx.moveTo(xpx(x),ypx(y));else ctx.lineTo(xpx(x),ypx(y));}ctx.stroke();ctx.restore();
 return {ctx,xpx,ypx,L,R,T,B,W,H};
}
function dot(p,x,y,colour){p.ctx.beginPath();p.ctx.arc(p.xpx(x),p.ypx(y),5,0,2*Math.PI);p.ctx.fillStyle=colour;p.ctx.fill();}
function vertical(p,x){p.ctx.save();p.ctx.setLineDash([4,4]);p.ctx.strokeStyle='#61747e';p.ctx.beginPath();p.ctx.moveTo(p.xpx(x),p.T);p.ctx.lineTo(p.xpx(x),p.H-p.B);p.ctx.stroke();p.ctx.restore();}
'''
PULSE_BODY = '''
<div class="title">Follow a moving feature; watch from a fixed sensor</div>
<div class="controls">
<label>Time: <output id="time-label"></output><input id="time" aria-label="Time in microseconds" type="range" min="0.1" max="0.9" step="0.01" value="0.4"></label>
<label>Sensor position: <output id="sensor-label"></output><input id="sensor" aria-label="Sensor position in metres" type="range" min="30" max="270" step="15" value="150"></label>
</div>
<div class="plots"><canvas id="space" width="580" height="300" aria-label="Spatial snapshot of the asymmetric pulse"></canvas><canvas id="trace" width="580" height="300" aria-label="Time record at a fixed sensor"></canvas></div>
<div id="values" class="readout" aria-live="polite"></div>
<p class="hint">Both vertical axes show Eₓ/E₀. Orange marks the moving peak in the snapshot and the current measurement in the sensor record. The dashed line in the snapshot is the fixed sensor. Read the steep side and long tail from left to right in each graph.</p>
<button id="reset" type="button">Reset</button>
'''
PULSE_JS = '''
function update(){
 const t=Number(document.getElementById('time').value)*1e-6,z=Number(document.getElementById('sensor').value),peak=C*t;
 document.getElementById('time-label').value=(t*1e6).toFixed(2)+' μs';document.getElementById('sensor-label').value=z.toFixed(0)+' m';
 const a=plot('space',x=>pulse(t-x/C),300,'Position z (m)','Space at the selected time','#009fc4',-.08);dot(a,peak,1,'#d26b26');vertical(a,z);
 const b=plot('trace',x=>pulse(x*1e-6-z/C),1.2,'Time t (μs)','Time at the fixed sensor','#356a97',-.08);dot(b,t*1e6,pulse(t-z/C),'#d26b26');vertical(b,t*1e6);
 const atPeak=(t-peak/C)*1e6,atSensor=(t-z/C)*1e6;
 document.getElementById('values').textContent='Moving peak: z = '+peak.toFixed(1)+' m; t − z/c = '+atPeak.toFixed(3)+' μs.  Fixed sensor: t − z/c = '+atSensor.toFixed(3)+' μs.';
}
for(const id of ['time','sensor'])document.getElementById(id).addEventListener('input',update);
document.getElementById('reset').addEventListener('click',()=>{document.getElementById('time').value='0.4';document.getElementById('sensor').value='150';update();});update();
'''
FREQUENCY_BODY = '''
<div class="title">Temporal frequency and spatial frequency</div>
<div class="controls">
<label>Frequency: <output id="frequency-label"></output><input id="frequency" aria-label="Frequency in megahertz" type="range" min="20" max="200" step="10" value="100"></label>
<label>Phase: <output id="phase-label"></output><input id="phase" aria-label="Phase in degrees" type="range" min="-180" max="180" step="15" value="0"></label>
</div>
<div class="plots"><canvas id="temporal" width="580" height="300" aria-label="Harmonic field versus time at z equals zero"></canvas><canvas id="spatial" width="580" height="300" aria-label="Harmonic field versus position at t equals zero"></canvas></div>
<div id="values" class="readout" aria-live="polite"></div>
<p class="hint">Both vertical axes show Eₓ/E₀. Axes stay fixed. Count the cycles in a second and a metre. Phase shifts the crests, while frequency changes their spacing. The vacuum speed stays fixed.</p>
<button id="reset" type="button">Reset</button>
'''
FREQUENCY_JS = '''
function update(){
 const f=Number(document.getElementById('frequency').value)*1e6,deg=Number(document.getElementById('phase').value),phi=deg*Math.PI/180,omega=2*Math.PI*f,k=omega/C,lambda=C/f,period=1/f;
 document.getElementById('frequency-label').value=(f/1e6).toFixed(0)+' MHz';document.getElementById('phase-label').value=deg.toFixed(0)+'°';
 plot('temporal',x=>Math.cos(omega*x*1e-9+phi),60,'Time t (ns), at z = 0','Time trace','#009fc4');
 plot('spatial',x=>Math.cos(-k*x+phi),18,'Position z (m), at t = 0','Spatial snapshot','#d26b26');
 document.getElementById('values').textContent='T = '+(period*1e9).toFixed(2)+' ns; λ = '+lambda.toFixed(2)+' m; ω = '+(omega/1e6).toFixed(1)+' × 10⁶ rad/s; k = '+k.toFixed(3)+' rad/m; spatial frequency = '+(1/lambda).toFixed(3)+' cycles/m.  fλ = ω/k = 3.0 × 10⁸ m/s.';
}
for(const id of ['frequency','phase'])document.getElementById(id).addEventListener('input',update);
document.getElementById('reset').addEventListener('click',()=>{document.getElementById('frequency').value='100';document.getElementById('phase').value='0';update();});update();
'''

def build():
    dest=ROOT/'interactives'; dest.mkdir(exist_ok=True)
    for name,title,body,js in [
        ('pulse','Plane-wave pulse explorer',PULSE_BODY,PULSE_JS),
        ('frequency','Plane-wave spatial-frequency explorer',FREQUENCY_BODY,FREQUENCY_JS),
    ]:
        page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+STYLE+'</style></head><body>'+body+'<script>'+COMMON+js+'</script></body></html>'
        (dest/(name+'.html')).write_text(page)
        # srcdoc bundles the activity with the page; no hosted asset-copy rule is needed.
        fragment='<iframe title="'+title+'" style="width:100%;height:650px;border:0" sandbox="allow-scripts" loading="lazy" srcdoc="'+html.escape(page,quote=True)+'"></iframe>\n'
        (dest/(name+'_embed.html')).write_text(fragment)

if __name__=='__main__':build()
