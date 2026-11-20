"""Snapshots of E_x along z for the two valid fields in question 5 of the EM-waves lab."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
figdir = root / 'labs' / 'figures'
figdir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.size': 10, 'axes.spines.top': False,
                     'axes.spines.right': False, 'figure.dpi': 140})
c = 3e8
cyan = '#009fc4'
orange = '#d26b26'

# (a) Harmonic plane wave: snapshots at t = 0 and t = T/4, z in wavelengths.
z = np.linspace(0, 2, 800)
fig, ax = plt.subplots(figsize=(6, 2.3))
ax.plot(z, np.cos(-2 * np.pi * z), color=cyan, lw=2, label='$t=0$')
ax.plot(z, np.cos(np.pi / 2 - 2 * np.pi * z), color=orange, lw=2, ls='--', label='$t=T/4$')
ax.annotate('', xy=(1.25, 1.12), xytext=(1.0, 1.12),
            arrowprops={'arrowstyle': '->', 'color': '#444', 'lw': 1.3})
ax.text(1.125, 1.22, r'$\lambda/4$', ha='center', color='#444')
ax.annotate('', xy=(1, -1.3), xytext=(0, -1.3),
            arrowprops={'arrowstyle': '<->', 'color': '#444'})
ax.text(0.5, -1.38, r'$\lambda$', ha='center', va='top', color='#444')
ax.set(xlabel=r'Position $z/\lambda$', ylabel=r'$E_x/E_0$', xlim=(0, 2), ylim=(-1.75, 1.45))
ax.legend(loc='upper right', fontsize=8, frameon=False, ncol=2, bbox_to_anchor=(1, 1.18))
ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(figdir / 'q5a_harmonic_snapshot.png')
plt.close(fig)

# (b) Gaussian pulse with tau = 0.1 us: snapshots at t = 1 us and t = 2 us.
tau = 0.1e-6
z = np.linspace(0, 800, 1600)
fig, ax = plt.subplots(figsize=(6, 2.3))
for t, col, ls in [(1e-6, cyan, '-'), (2e-6, orange, '--')]:
    ax.plot(z, np.exp(-((t - z / c) / tau) ** 2), color=col, lw=2, ls=ls,
            label=fr'$t={t * 1e6:.0f}\ \mu$s')
    ax.plot(c * t, 1, 'o', color=col, ms=4)
    ax.text(c * t, 1.08, f'z = {c * t:.0f} m', ha='center', color=col, fontsize=9)
ax.set(xlabel=r'Position $z$ (m)', ylabel=r'$E_x/E_0$', xlim=(0, 800), ylim=(-0.05, 1.3))
ax.legend(loc='upper left', fontsize=8, frameon=False)
ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(figdir / 'q5b_pulse_snapshot.png')
plt.close(fig)
