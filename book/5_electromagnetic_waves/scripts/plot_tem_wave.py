"""Snapshot of a harmonic TEM plane wave: E along x, H along y, travelling along +z."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
figdir = root / 'figures'
figdir.mkdir(exist_ok=True)
plt.rcParams.update({'font.size': 12, 'figure.dpi': 140})
cyan = '#009fc4'
orange = '#d26b26'

# Coordinates: matplotlib X = physical z (propagation), matplotlib Y = physical y (H),
# matplotlib Z = physical x (E, drawn vertically). Lengths in wavelengths.
L = 2.0
z = np.linspace(0, L, 600)
field = np.cos(2 * np.pi * z)  # snapshot at t = 0 of cos(omega t - k z)

fig = plt.figure(figsize=(10, 4.2))
ax = fig.add_subplot(projection='3d')
ax.set_proj_type('ortho')

# Field-vector stems from the z axis to each curve
for zz in np.linspace(0, L, 41):
    f = np.cos(2 * np.pi * zz)
    ax.plot([zz, zz], [0, 0], [0, f], color=cyan, lw=0.9, alpha=0.55)
    ax.plot([zz, zz], [0, f], [0, 0], color=orange, lw=0.9, alpha=0.55)

ax.plot(z, 0 * z, field, color=cyan, lw=2.4)
ax.plot(z, field, 0 * z, color=orange, lw=2.4)

# Coordinate axes
arrow = dict(color='#333', arrow_length_ratio=0.06, lw=1.3)
ax.quiver(0, 0, 0, L + 0.5, 0, 0, **arrow)
ax.quiver(0, 0, 0, 0, 0, 1.45, arrow_length_ratio=0.12, color='#333', lw=1.3)
ax.quiver(0, 0, 0, 0, 1.45, 0, arrow_length_ratio=0.12, color='#333', lw=1.3)
ax.text(L + 0.55, 0, 0.1, 'z', fontsize=14)
ax.text(0, 0, 1.55, 'x', fontsize=14)
ax.text(0, 1.6, 0, 'y', fontsize=14)
ax.text(L + 0.1, 0, -0.45, 'propagation', color='#333', fontsize=11)

# Field labels
ax.text(0.78, 0, 1.18, r'$\vec E=\hat x\,E_x(z,t)$', color=cyan, fontsize=13)
ax.text(2.1, 1.05, 0.0, r'$\vec H=\hat y\,H_y(z,t)$', color=orange, fontsize=13)

# Wavelength marker
ax.plot([0, 1], [0, 0], [-1.3, -1.3], color='#555', lw=1)
for zz in (0, 1):
    ax.plot([zz, zz], [0, 0], [-1.37, -1.23], color='#555', lw=1)
ax.text(0.5, 0, -1.55, r'$\lambda$', ha='center', fontsize=13, color='#555')

ax.set_xlim(0, L + 0.7)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-1.4, 1.4)
ax.set_box_aspect((L + 0.7, 1.6, 1.6), zoom=1.25)
ax.view_init(elev=24, azim=-58)
ax.set_axis_off()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
out = figdir / 'plane_wave_tem.png'
fig.savefig(out, facecolor='white')
plt.close(fig)

# 3D axes keep a large empty margin; crop the image to its content
from PIL import Image, ImageChops
img = Image.open(out).convert('RGB')
box = ImageChops.difference(img, Image.new('RGB', img.size, 'white')).getbbox()
pad = 12
img.crop((max(box[0] - pad, 0), max(box[1] - pad, 0),
          min(box[2] + pad, img.width), min(box[3] + pad, img.height))).save(out)
