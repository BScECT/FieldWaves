from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1]
figdir=root/'figures'; figdir.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':140})
c=3e8; cyan='#009fc4'; orange='#d26b26'
def pulse(tau):
 s=np.asarray(tau)/60e-9
 width=1+0.65*np.tanh(s)
 return np.exp(-(s/width)**2)
fig,axs=plt.subplots(2,1,figsize=(9,6.2)); z=np.linspace(0,300,1800)
ax=axs[0]
for t,col in [(0.3e-6,cyan),(0.7e-6,orange)]:
 ax.plot(z,pulse(t-z/c),color=col,label=f't = {t*1e6:.1f} μs',lw=2)
 ax.plot(c*t,1,'o',color=col); ax.annotate(f'z = {c*t:.0f} m',(c*t,1),xytext=(c*t,1.17),ha='center',color=col)
ax.annotate('',xy=(210,.65),xytext=(90,.65),arrowprops={'arrowstyle':'->','color':'#444','lw':1.5})
ax.text(150,.74,'same peak: t − z/c = 0',ha='center')
ax.set(title='Spatial snapshots: long tail on the left, steep front on the right',xlabel='Position z (m)',ylabel='Electric field / E₀',ylim=(-.05,1.4),xlim=(0,300)); ax.legend(loc='upper right',fontsize=9); ax.grid(alpha=.15)
times=np.linspace(0,1e-6,1800); sensor=150
ax=axs[1];ax.plot(times*1e6,pulse(times-sensor/c),lw=2,color='#356a97')
ax.plot(sensor/c*1e6,1,'o',color='#356a97')
ax.set(title='Fixed sensor at z = 150 m: rapid rise, then a long decay',xlabel='Time t (μs)',ylabel='Electric field / E₀',ylim=(-.05,1.3),xlim=(0,1));ax.grid(alpha=.15)
ax.annotate('peak arrives at 0.5 μs',xy=(.5,1),xytext=(.64,1.1),arrowprops={'arrowstyle':'->','color':'#444'})
fig.tight_layout(h_pad=1.7); fig.savefig(figdir/'plane_wave_pulse.png'); plt.close(fig)
f=100e6; omega=2*np.pi*f; k=omega/c; T=1/f; lam=c/f
fig,axs=plt.subplots(1,2,figsize=(10,3.3))
t=np.linspace(0,25e-9,1000); z=np.linspace(0,7.5,1000)
for ax,xx,yy,label,period,unit,col in [(axs[0],t*1e9,np.cos(omega*t),'Time t (ns), at z = 0',T*1e9,'T = 10 ns',cyan),(axs[1],z,np.cos(-k*z),'Position z (m), at t = 0',lam,'λ = 3 m',orange)]:
 ax.plot(xx,yy,color=col,lw=2); ax.set(xlabel=label,ylim=(-1.2,1.6)); ax.grid(alpha=.15)
 ax.annotate('',xy=(period,1.25),xytext=(0,1.25),arrowprops={'arrowstyle':'<->','color':'#444'}); ax.text(period/2,1.37,unit,ha='center')
axs[0].set_ylabel('Electric field / E₀'); axs[0].set_title('Temporal frequency f = 100 MHz'); axs[1].set_title('Spatial frequency 1/λ ≈ 0.333 cycles/m')
fig.tight_layout(); fig.savefig(figdir/'plane_wave_spatial_frequency.png'); plt.close(fig)
fig,ax=plt.subplots(figsize=(8,4.2)); ax.set_aspect('equal'); ax.axis('off')
for yy,col in [(0,'#dd7c35'),(2,'#888')]: ax.plot([0,5],[yy,yy],color=col,lw=7,solid_capstyle='butt')
for xx in [1.2,2.5,3.8]: ax.annotate('',xy=(xx,1.75),xytext=(xx,.25),arrowprops={'arrowstyle':'->','color':cyan,'lw':2})
ax.text(2.7,1.4,'E along +x',color=cyan)
ax.annotate('',xy=(4.3,.7),xytext=(.7,.7),arrowprops={'arrowstyle':'->','color':'#356a97','lw':2}); ax.text(2.5,.35,'H along +y',ha='center',color='#356a97')
ax.annotate('',xy=(5.5,2),xytext=(5.5,0),arrowprops={'arrowstyle':'<->'}); ax.text(5.65,1,'d',va='center')
ax.annotate('',xy=(5,-.65),xytext=(0,-.65),arrowprops={'arrowstyle':'<->'}); ax.text(2.5,-.9,'w',ha='center')
ax.text(-.45,0,'⊗',fontsize=23,ha='center',va='center'); ax.text(-.8,-.5,'I: +z into page',ha='left',fontsize=10)
ax.text(-.45,2,'⊙',fontsize=23,ha='center',va='center'); ax.text(-.8,2.4,'return current',ha='left',fontsize=10)
ax.text(5.15,.05,'+V',ha='left'); ax.text(5.15,1.95,'0',ha='left')
ax.set(xlim=(-1,6),ylim=(-1.2,2.9)); fig.tight_layout(); fig.savefig(figdir/'plane_wave_parallel_plates.png'); plt.close(fig)
