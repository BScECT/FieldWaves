"""Regenerate the schematic of the diffusive-fields lab.  Run: python make_figures.py"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

INK, BAR, RES, OUT = "#6b7280", "#8a9199", "#00A6D6", "#EC6842"


def bar(ax, y, label):
    ax.add_patch(Rectangle((0, y - 0.18), 1, 0.36, fc=BAR, ec=INK, alpha=0.35, lw=1))
    ax.text(0.5, y + 0.3, label, ha="center", va="bottom", color=INK, fontsize=10)


def arrow(ax, x0, x1, y):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>", mutation_scale=14,
                                 color=OUT, lw=2))


fig, ax = plt.subplots(figsize=(6.4, 3.0))
# Dirichlet: ends clamped to reservoirs at the reference temperature
bar(ax, 1.25, "Example 1:  $T(0,t)=T(L,t)=0$,  ends held at the reference temperature")
for x0 in (-0.13, 1.0):
    ax.add_patch(Rectangle((x0, 0.98), 0.13, 0.54, fc=RES, ec=RES, alpha=0.55))
ax.text(-0.065, 0.9, "$T=0$", ha="center", va="top", color=INK, fontsize=9)
ax.text(1.065, 0.9, "$T=0$", ha="center", va="top", color=INK, fontsize=9)
arrow(ax, 0.1, -0.2, 1.25); arrow(ax, 0.9, 1.2, 1.25)
ax.text(1.24, 1.25, "heat can\nleave", ha="left", va="center", color=OUT, fontsize=8)

# Neumann: insulated ends
bar(ax, 0.0, r"Example 2:  $\partial_x T(0,t)=\partial_x T(L,t)=0$,  insulated ends")
for x0 in (-0.05, 1.0):
    ax.add_patch(Rectangle((x0, -0.27), 0.05, 0.54, fc="none", ec=INK, hatch="////", lw=1))
ax.text(1.12, 0.0, "no flux", ha="left", va="center", color=INK, fontsize=8)

ax.set_xticks([0, 1], ["$0$", "$L$"]); ax.set_yticks([])
ax.set_xlim(-0.35, 1.45); ax.set_ylim(-0.5, 1.95)
for s in ("left", "right", "top"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK); ax.tick_params(colors=INK)
ax.set_xlabel("$x$", color=INK)
fig.tight_layout()
fig.savefig("bar_boundary_conditions.svg", transparent=True, metadata={"Date": None})
