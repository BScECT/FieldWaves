"""Reproduce the media section's editable SVG diagrams and scientific plot."""
from pathlib import Path
import os,tempfile
os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'fieldwaves-media-mpl'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1];D=R/'figures';D.mkdir(exist_ok=True)
BLUE='#007fa8';ORANGE='#bd641d';INK='#243743'
plt.rcParams.update({'font.size':13,'mathtext.fontset':'cm','axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','text.color':INK,'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK})
fig,axs=plt.subplots(1,2,figsize=(11,3.7));fig.subplots_adjust(wspace=.30,left=.07,right=.98,bottom=.18,top=.83)
t=np.linspace(0,4*np.pi,601)
axs[0].plot(t/(2*np.pi),np.cos(t),color=BLUE,lw=2,label='Electric field')
axs[0].plot(t/(2*np.pi),np.cos(t-np.pi/4),color=ORANGE,lw=2,label='Polarization')
axs[0].set(xlim=(0,2),ylim=(-1.15,1.15),xlabel='Time / period',ylabel='Each trace / its own peak',title=r'Response lags at $\omega\tau=1$');axs[0].legend(frameon=True,facecolor='white',edgecolor='white',framealpha=.95,loc='upper right',fontsize=10)
x=np.geomspace(.01,100,601);chi=4
axs[1].semilogx(x,1+chi/(1+x*x),color=BLUE,lw=2,label=r'$\epsilon^\prime/\epsilon_0$')
axs[1].semilogx(x,chi*x/(1+x*x),color=ORANGE,lw=2,label=r'$\epsilon^{\prime\prime}_d/\epsilon_0$')
axs[1].axvline(1,color='#a4b5be',ls=':',lw=1);axs[1].set(xlabel=r'$\omega\tau$',ylabel='Relative permittivity components',ylim=(0,5.4),title='One response, two frequency curves');axs[1].legend(frameon=False,fontsize=12)
# Embed lettering as vector outlines: browser font fallback cannot reproduce
# the Computer Modern math fonts' legacy character mappings reliably.
with plt.rc_context({'svg.fonttype': 'path'}):
 fig.savefig(D/'media_dielectric_lag.svg')
fig.savefig(D/'media_dielectric_lag.png',dpi=160);plt.close(fig)
head='''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="405" viewBox="0 0 1100 405"><defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#007fa8"/></marker></defs><rect width="1100" height="405" fill="white"/><g font-family="Arial,sans-serif" fill="#243743">'''
parts=[head,'<text x="550" y="29" text-anchor="middle" font-size="23">An electric field can produce different kinds of motion</text>']
for x,title in [(180,'Bound charges'),(550,'Molecular dipoles'),(920,'Mobile ions')]:
 parts.append(f'<text x="{x}" y="80" text-anchor="middle" font-size="22">{title}</text><path d="M{x-95} 112H{x+95}" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#a)"/><text x="{x+108}" y="118" font-size="20">E</text>')
for y in [175,240]:
 parts.append(f'<ellipse cx="180" cy="{y}" rx="100" ry="27" fill="#f1f5f6" stroke="#c3d1d7"/>')
 for cx,sgn,col in [(155,'−',BLUE),(205,'+',ORANGE)]:parts.append(f'<circle cx="{cx}" cy="{y}" r="15" fill="{col}"/><text x="{cx}" y="{y+6}" fill="white" font-size="22" text-anchor="middle">{sgn}</text>')
for cx,cy,angle in [(500,180,-20),(595,180,10),(500,245,15),(595,245,-15)]:
 parts.append(f'<g transform="translate({cx} {cy}) rotate({angle})"><path d="M-22 0H22" stroke="#82949d" stroke-width="3"/><circle cx="-22" cy="0" r="13" fill="{BLUE}"/><circle cx="22" cy="0" r="13" fill="{ORANGE}"/><text x="-22" y="5" fill="white" font-size="19" text-anchor="middle">−</text><text x="22" y="5" fill="white" font-size="19" text-anchor="middle">+</text></g>')
for cx,cy,sgn,col,end in [(865,180,'+',ORANGE,975),(975,245,'−',BLUE,865)]:
 parts.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{col}"/><text x="{cx}" y="{cy+7}" fill="white" font-size="24" text-anchor="middle">{sgn}</text><path d="M{cx+(25 if end>cx else -25)} {cy}H{end}" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#a)"/>')
for x,line1,line2 in [(180,'Small relative displacement','Charge remains bound'),(550,'Dipoles tend to align','Their response can lag'),(920,'Charges travel through material','Conduction adds current')]:parts.append(f'<text x="{x}" y="315" text-anchor="middle" font-size="18">{line1}</text><text x="{x}" y="341" text-anchor="middle" font-size="18">{line2}</text>')
parts.append('<text x="550" y="389" text-anchor="middle" font-size="17" fill="#526a77">Bulk soil response combines mineral grains, pore air and pore water.</text></g></svg>')
(D/'media_material_response.svg').write_text(''.join(parts))
svg='''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="400" viewBox="0 0 1000 400"><defs><marker id="b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#007fa8"/></marker><marker id="o" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#bd641d"/></marker></defs><rect width="1000" height="400" fill="white"/><rect x="70" y="95" width="860" height="240" fill="#f4f5ef"/><g font-family="Arial,sans-serif" fill="#243743" font-size="21"><text x="500" y="32" text-anchor="middle" font-size="24">The echo makes two trips through the material</text><path d="M70 95H930" stroke="#7c8d78" stroke-width="2"/><text x="82" y="81">z = 0</text><text x="82" y="317">z = d</text><path d="M365 104V288" stroke="#007fa8" stroke-width="4" marker-end="url(#b)"/><path d="M635 288V104" stroke="#bd641d" stroke-width="4" marker-end="url(#o)"/><path d="M305 305H695" stroke="#758370" stroke-width="7"/><text x="500" y="365" text-anchor="middle">reflector</text><text x="245" y="66" fill="#007fa8">Start: E₀</text><text x="690" y="66" fill="#bd641d">Return: E₀ e⁻²ᵅᵈ</text><text x="120" y="206" fill="#007fa8">Down: × e⁻ᵅᵈ</text><text x="690" y="206" fill="#bd641d">Back: × e⁻ᵅᵈ</text><text x="500" y="281" text-anchor="middle">At depth: E₀ e⁻ᵅᵈ</text><text x="500" y="392" text-anchor="middle" font-size="16" fill="#526a77">Absorption factors only; the two path legs are shown side by side.</text></g></svg>'''
(D/'media_round_trip.svg').write_text(svg)
print('Generated three media figures (editable SVG; dielectric plot also PNG).')
