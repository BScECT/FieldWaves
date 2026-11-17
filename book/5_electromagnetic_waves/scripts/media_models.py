"""Small teaching models for media plots; SI units, exp(+j omega t).

Presets are illustrative parameters, not empirical fits or survey predictions.
The water-like single relaxation only illustrates molecular loss + ionic current.
"""
import numpy as np
EPS0=8.8541878128e-12
C=299792458.
MU0=1/(EPS0*C*C)
MODELS={
 'dry':dict(name='Dry-soil example',kind='constant',er=4.,tan=.005,sigma=1e-4),
 'wet':dict(name='Wetter-soil example',kind='constant',er=16.,tan=.03,sigma=.02),
 'fresh':dict(name='Freshwater-like example',kind='debye',es=80.,einf=5.,tau=9e-12,sigma=.005),
 'saline':dict(name='Saline-water-like example',kind='debye',es=80.,einf=5.,tau=9e-12,sigma=4.)}
def response(f,key):
 m=MODELS[key];w=2*np.pi*np.asarray(f)
 if m['kind']=='constant':return np.ones_like(w)*m['er'],np.ones_like(w)*m['er']*m['tan'],m['sigma']
 x=w*m['tau'];return m['einf']+(m['es']-m['einf'])/(1+x*x),(m['es']-m['einf'])*x/(1+x*x),m['sigma']
def propagation(f,er,dielectric_imag,sigma=0.,mur=1.):
 w=2*np.pi*np.asarray(f);ei=np.asarray(dielectric_imag)+sigma/(w*EPS0)
 b=np.sqrt((np.hypot(er,ei)+er)/2)
 beta=w/C*np.sqrt(mur)*b
 alpha=w/C*np.sqrt(mur)*ei/(2*b) # stable as loss tends to zero
 return alpha,beta
