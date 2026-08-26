from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.patches import Circle


figure_path = Path(__file__).parent / "figures" / "helmholtz_field_comparison.png"

coordinates = np.linspace(-0.9, 0.9, 13)
x, y = np.meshgrid(coordinates, coordinates)
radius = np.hypot(x, y)
inside = radius <= 0.92

fields = [
    (-x, -y, "Irrotational: gravity inside a sphere"),
    (-y, x, "Solenoidal: magnetic field inside a wire"),
]

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.8), layout="constrained")
normalization = Normalize(0, 1)

for ax, (field_x, field_y, title) in zip(axes, fields):
    field_x = np.where(inside, field_x, np.nan)
    field_y = np.where(inside, field_y, np.nan)
    magnitude = np.hypot(field_x, field_y)

    ax.add_patch(Circle((0, 0), 1, facecolor="#eeeeee", edgecolor="0.25", lw=1.5, zorder=-2))
    quiver = ax.quiver(
        x,
        y,
        field_x,
        field_y,
        magnitude,
        cmap="viridis",
        norm=normalization,
        angles="xy",
        scale_units="xy",
        scale=5.2,
        width=0.008,
        pivot="mid",
    )
    ax.plot(0, 0, "o", ms=4, color="0.2")
    ax.set(
        xlim=(-1.08, 1.08),
        ylim=(-1.08, 1.08),
        xlabel="$x$",
        ylabel="$y$",
        title=title,
    )
    ax.set_aspect("equal")
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])

for radius_guide in (0.3, 0.6, 0.9):
    axes[1].add_patch(
        Circle((0, 0), radius_guide, fill=False, edgecolor="0.55", lw=0.7, ls=":", zorder=-1)
    )

fig.colorbar(
    quiver,
    ax=axes,
    orientation="horizontal",
    label="field magnitude (normalized)",
    shrink=0.72,
    pad=0.06,
    aspect=38,
)
fig.savefig(figure_path, dpi=200, bbox_inches="tight")
plt.close(fig)
