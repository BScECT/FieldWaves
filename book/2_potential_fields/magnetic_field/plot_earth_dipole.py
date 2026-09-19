"""Reproducible Earth dipole / IGRF-14 figures, epoch 2025.0.

Run: MPLCONFIGDIR=/tmp/fieldwaves-mpl conda run -n fieldwaves python
     book/2_potential_fields/magnetic_field/plot_earth_dipole.py
Only NumPy and Matplotlib are required. Coefficients are stored beside the book.
Uses geocentric coordinates, Schmidt semi-normalization without Condon–Shortley
phase, and a spherical reference surface a=6371.2 km, not ellipsoidal sea level.
"""
from pathlib import Path
from math import factorial, sqrt
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

HERE = Path(__file__).resolve().parent
OUT = HERE / 'figures'
A = 6371.2  # km: IGRF reference radius
BLUE, ORANGE = '#1769aa', '#bd561b'
plt.rcParams.update({'font.size': 11, 'svg.fonttype': 'none'})


def coefficients():
    """Return g,h arrays in nT for the explicitly named 2025 epoch."""
    lines = (HERE/'data/igrf14coeffs.txt').read_text().splitlines()
    header = next(x.split() for x in lines if x.startswith('g/h'))
    col = header.index('2025.0')
    g, h = np.zeros((14,14)), np.zeros((14,14))
    for line in lines:
        t = line.split()
        if t and t[0] in ('g','h'):
            (g if t[0]=='g' else h)[int(t[1]),int(t[2])] = float(t[col])
    return g,h


def legendre(theta, nmax):
    """Pbar_n^m(cos theta) and dPbar/dtheta by differentiating recurrence."""
    x, s = np.cos(theta), np.sin(theta)
    shape = (nmax+1,nmax+1)+theta.shape
    p, d = np.zeros(shape), np.zeros(shape)
    p[0,0] = 1
    for m in range(nmax+1):
        if m:
            p[m,m] = (2*m-1)*s*p[m-1,m-1]
            d[m,m] = (2*m-1)*(x*p[m-1,m-1]+s*d[m-1,m-1])
        if m<nmax:
            p[m+1,m] = (2*m+1)*x*p[m,m]
            d[m+1,m] = (2*m+1)*(-s*p[m,m]+x*d[m,m])
        for n in range(m+2,nmax+1):
            p[n,m] = ((2*n-1)*x*p[n-1,m]-(n+m-1)*p[n-2,m])/(n-m)
            d[n,m] = ((2*n-1)*(-s*p[n-1,m]+x*d[n-1,m])-(n+m-1)*d[n-2,m])/(n-m)
    for n in range(nmax+1):
        for m in range(n+1):
            norm = sqrt((2 if m else 1)*factorial(n-m)/factorial(n+m))
            p[n,m] *= norm
            d[n,m] *= norm
    return p,d


def field(theta, phi, r=A, nmax=13):
    """Return potential [nT km], Br,Btheta,Bphi [nT]; exclude polar singularities."""
    theta,phi = np.broadcast_arrays(np.asarray(theta,dtype=float),np.asarray(phi,dtype=float))
    assert np.all((theta>0)&(theta<np.pi))
    g,h = coefficients(); p,d = legendre(theta,nmax)
    v,br,bt,bp = [np.zeros(theta.shape) for _ in range(4)]
    for n in range(1,nmax+1):
        for m in range(n+1):
            c = g[n,m]*np.cos(m*phi)+h[n,m]*np.sin(m*phi)
            dc = m*(-g[n,m]*np.sin(m*phi)+h[n,m]*np.cos(m*phi))
            v += A*(A/r)**(n+1)*c*p[n,m]
            br += (n+1)*(A/r)**(n+2)*c*p[n,m]
            bt -= (A/r)**(n+2)*c*d[n,m]
            bp -= (A/r)**(n+2)*dc*p[n,m]/np.sin(theta)
    return v,br,bt,bp


def validate():
    # Independent Cartesian point-dipole expression versus degree-one synthesis.
    th=np.array([.3,.9,1.7,2.8]); ph=np.array([-.7,1.2,2.9,-2.1]); r=1.2*A
    g,h=coefficients(); b=np.array([g[1,1],h[1,1],g[1,0]])
    er=np.array([np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph),np.cos(th)])
    et=np.array([np.cos(th)*np.cos(ph),np.cos(th)*np.sin(ph),-np.sin(th)])
    ep=np.array([-np.sin(ph),np.cos(ph),np.zeros_like(th)])
    cart=(A/r)**3*(3*np.sum(b[:,None]*er,axis=0)*er-b[:,None])
    v,br,bt,bp=field(th,ph,r,1)
    for got,basis in [(br,er),(bt,et),(bp,ep)]:
        np.testing.assert_allclose(got,np.sum(cart*basis,axis=0),atol=1e-10)
    # All-degree field is the negative gradient of its independently differenced potential.
    eps=1e-5; dr=.01
    v,br,bt,bp=field(th,ph,r)
    np.testing.assert_allclose(br,-(field(th,ph,r+dr)[0]-field(th,ph,r-dr)[0])/(2*dr),rtol=2e-8)
    np.testing.assert_allclose(bt,-(field(th+eps,ph,r)[0]-field(th-eps,ph,r)[0])/(2*eps*r),rtol=2e-8)
    np.testing.assert_allclose(bp,-(field(th,ph+eps,r)[0]-field(th,ph-eps,r)[0])/(2*eps*r*np.sin(th)),rtol=2e-8)
    # Exact-degree quadrature validates normalization, spectrum and no-monopole flux.
    x,w=np.polynomial.legendre.leggauss(48)
    th=np.arccos(x)[:,None];ph=np.linspace(-np.pi,np.pi,96,endpoint=False)[None,:]
    full=field(th,ph);dip=field(th,ph,nmax=1)
    avg=lambda f: float(np.sum(w[:,None]*f)/192)
    spectrum=sum((n+1)*np.sum(g[n,:]**2+h[n,:]**2) for n in range(1,14))
    ms=avg(sum(q*q for q in full[1:]));ms1=avg(sum(q*q for q in dip[1:]))
    np.testing.assert_allclose(ms,spectrum,rtol=1e-12)
    assert abs(avg(full[1]))<1e-9
    residual=avg(sum((f-d)**2 for f,d in zip(full[1:],dip[1:])))
    np.testing.assert_allclose(ms,ms1+residual,rtol=1e-12)
    stats={'epoch':2025.0,'reference_radius_km':A,'dipole_mean_square_fraction':ms1/ms,
           'dipole_equatorial_microtesla':float(np.linalg.norm(b)/1000),
           'axis_tilt_deg':float(np.rad2deg(np.arctan2(np.hypot(b[0],b[1]),-b[2]))),
           'full_vector_rms_microtesla':sqrt(ms)/1000,'residual_vector_rms_microtesla':sqrt(residual)/1000}
    # Named geocentric test points make boundary comparison reproducible.
    stats['surface_samples']=[]
    for lat,lon in [(0,0),(45,0),(-45,0),(52,4)]:
        t,p=np.deg2rad(90-lat),np.deg2rad(lon)
        q=field(t,p);d=field(t,p,nmax=1)
        stats['surface_samples'].append({'latitude_deg':lat,'longitude_deg':lon,
             'Br_full_microtesla':float(q[1]/1000),'Br_dipole_microtesla':float(d[1]/1000),
             'Br_residual_microtesla':float((q[1]-d[1])/1000)})
    (HERE/'data/dipole_checks.json').write_text(json.dumps(stats,indent=2)+'\n')
    print(json.dumps(stats,indent=2))


def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),bbox_inches='tight')
    fig.savefig(OUT/(name+'.png'),dpi=170,bbox_inches='tight')
    plt.close(fig)


def geometry():
    fig,axs=plt.subplots(1,2,figsize=(11,4.8),layout='constrained')
    ax=axs[0]; ax.add_patch(Circle((0,0),1,fc='#e6eef5',ec=BLUE,lw=2))
    ax.plot([0,0],[-1.35,1.35],color='gray',ls='--');ax.text(.08,1.28,'geographic north',fontsize=10)
    # Exaggerated tilt to make axis conventions clear.
    u=np.array([-.28,.96]);ax.plot([-1.3*u[0],1.3*u[0]],[-1.3*u[1],1.3*u[1]],color=ORANGE)
    ax.annotate('',xy=-.78*u,xytext=(0,0),arrowprops={'arrowstyle':'->','lw':3,'color':ORANGE})
    ax.text(.36,-.62,r'$\mathbf{m}$',color=ORANGE,fontsize=16)
    ax.text(-1.4,1.13,'northern dipole-axis end',fontsize=10)
    ax.text(-1.4,-1.5,'Present polarity: moment points toward\nthe southern dipole-axis end.',fontsize=11)
    ax.set(title='Earth: rotation axis and dipole moment',xlim=(-1.6,1.6),ylim=(-1.7,1.55),aspect='equal');ax.axis('off')
    ax=axs[1];ax.add_patch(Circle((0,0),1,fc='#e6eef5',ec=BLUE,lw=2))
    ax.annotate('',xy=(0,1.5),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':ORANGE});ax.text(.09,1.4,r'$+z_m\ \parallel\ \mathbf{m}$',fontsize=13)
    t=.75;P=np.array([np.sin(t),np.cos(t)])*1.2
    ax.plot([0,P[0]],[0,P[1]],color='black');ax.scatter(*P,c='black',s=15);ax.text(P[0]-.13,P[1]+.1,'P')
    ax.add_patch(Arc((0,0),.75,.75,theta1=90-np.rad2deg(t),theta2=90));ax.text(.15,.47,r'$\theta$')
    er=P/np.linalg.norm(P);et=np.array([np.cos(t),-np.sin(t)])
    for direction,label,offset in [(er,r'$\hat{r}$',(.05,.02)),(et,r'$\hat{\theta}$',(.06,-.08))]:
        end=P+.43*direction;ax.annotate('',xy=end,xytext=P,arrowprops={'arrowstyle':'->','color':BLUE,'lw':2});ax.text(*(end+offset),label,color=BLUE)
    ax.text(-1.25,-1.5,'For the calculation, rotate the axes:\nθ is measured from the moment direction.',fontsize=11)
    ax.set(title='Dipole-aligned coordinates for the calculation',xlim=(-1.5,1.9),ylim=(-1.7,1.75),aspect='equal');ax.axis('off')
    save(fig,'earth_dipole_coordinates')


def comparison():
    lon=np.linspace(-180,180,361);lat=np.linspace(-89.75,89.75,180)
    ph,th=np.meshgrid(np.deg2rad(lon),np.deg2rad(90-lat))
    full=field(th,ph)[1]/1000;dip=field(th,ph,nmax=1)[1]/1000
    fig,axs=plt.subplots(3,1,figsize=(10,10),layout='constrained',sharex=True,sharey=True)
    for ax,z,title in zip(axs,[dip,full,full-dip],['Centred tilted dipole (degree 1)','IGRF-14 main-field model (degrees 1–13)','Boundary residual: IGRF-14 minus dipole']):
        im=ax.pcolormesh(lon,lat,z,cmap='RdBu_r',vmin=-70,vmax=70,shading='auto',rasterized=True)
        ax.contour(lon,lat,z,levels=[0],colors='black',linewidths=.6)
        ax.set(title=title,ylabel='Geocentric latitude (°)',yticks=[-60,0,60])
        ax.grid(alpha=.2);fig.colorbar(im,ax=ax,label=r'$B_r$ (μT), positive outward',pad=.015)
    axs[-1].set(xlabel='Longitude east (°)',xticks=[-180,-90,0,90,180])
    fig.suptitle('Surface boundary comparison • epoch 2025.0 • r = 6371.2 km\nObservation-based reference model, not raw measurements',fontsize=13)
    save(fig,'earth_dipole_boundary_comparison')


def harmonics():
    lon=np.linspace(-180,180,241);lat=np.linspace(-90,90,121)
    ph,la=np.meshgrid(np.deg2rad(lon),np.deg2rad(lat));x=np.sin(la)
    patterns=[x,np.sqrt(1-x*x)*np.cos(ph),.5*(3*x*x-1),.5*(5*x**3-3*x)]
    titles=['Degree 1: axisymmetric dipole','Degree 1: rotated dipole','Degree 2: an axisymmetric pattern','Degree 3: an axisymmetric pattern']
    fig,axs=plt.subplots(2,2,figsize=(11,5.8),layout='constrained',sharex=True,sharey=True)
    for ax,p,title in zip(axs.flat,patterns,titles):
        im=ax.pcolormesh(lon,lat,p,cmap='RdBu_r',vmin=-1,vmax=1,shading='auto',rasterized=True)
        ax.contour(lon,lat,p,[0],colors='black',linewidths=.6)
        ax.set(title=title,xticks=[-180,0,180],yticks=[-90,0,90]);ax.grid(alpha=.2)
    for ax in axs[-1]:ax.set_xlabel('Longitude (°)')
    for ax in axs[:,0]:ax.set_ylabel('Latitude (°)')
    fig.colorbar(im,ax=axs,label='Normalized angular pattern (arbitrary amplitude)',shrink=.8)
    fig.suptitle('Simple patterns on a sphere • examples, not measured magnetic maps',fontsize=13)
    save(fig,'spherical_harmonic_patterns')
    fig,ax=plt.subplots(figsize=(8,4.4),layout='constrained')
    height=np.linspace(0,1500,250)
    for l in [1,2,5,10]:ax.plot(height,(A/(A+height))**(l+2),lw=2,label=f'Degree {l}')
    ax.axvline(500,color='gray',ls=':',lw=1)
    ax.set(xlabel='Height above the reference sphere (km)',ylabel='Field amplitude / surface amplitude',title='Internal-source structure fades with height',ylim=(0,1.02));ax.grid(alpha=.2);ax.legend()
    save(fig,'magnetic_harmonic_attenuation')


if __name__=='__main__':
    OUT.mkdir(exist_ok=True);validate();geometry();comparison();harmonics()
