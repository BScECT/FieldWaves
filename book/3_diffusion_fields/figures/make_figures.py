"""Regenerate the initial-condition sketches of the heat-equation exercises.

Run from this directory:  python make_figures.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#6b7280"       # neutral grey, readable on light and dark backgrounds
LINE = "#00A6D6"      # TU Delft cyan

def step_sketch(fname, edges, values, xticks, xticklabels):
    fig, ax = plt.subplots(figsize=(4.2, 2.4))
    xs, ys = [], []
    for (a, b), v in zip(zip(edges[:-1], edges[1:]), values):
        xs += [a, b]
        ys += [v, v]
    ax.plot(xs, ys, color=LINE, lw=2)
    ax.axhline(0, color=INK, lw=0.8)
    ax.set_xlim(-0.05, 1.12)
    ax.set_ylim(-1.35, 1.35)
    ax.set_xticks(xticks, xticklabels)
    ax.set_yticks([-1, 0, 1])
    ax.set_xlabel("$x$", color=INK)
    ax.set_ylabel("$h(x)$", color=INK)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(INK)
    ax.tick_params(colors=INK)
    fig.tight_layout()
    fig.savefig(fname, transparent=True, metadata={"Date": None})
    plt.close(fig)

# exercise 4: h = 0, -1, 1, 0 on the four quarters of the bar, T(0,t) = T(L,t) = 0
step_sketch("heat_ic_quarters.svg",
            [0, 0.25, 0.5, 0.75, 1.0], [0, -1, 1, 0],
            [0, 0.25, 0.5, 0.75, 1.0], ["0", "$L/4$", "$L/2$", "$3L/4$", "$L$"])

# exercise 5: h = 1, -1, 1 on the three thirds of the bar, insulated ends
step_sketch("heat_ic_thirds.svg",
            [0, 1/3, 2/3, 1.0], [1, -1, 1],
            [0, 1/3, 2/3, 1.0], ["0", "$L/3$", "$2L/3$", "$L$"])
