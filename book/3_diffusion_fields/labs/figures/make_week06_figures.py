"""Regenerate the four model-setup schematics of the Week 6 lab.

Run:  python make_week06_figures.py

Same palette and conventions as make_figures.py: transparent SVG, grey ink so the
theme can invert it in dark mode, TU Delft cyan for the field under study and
orange for the source. Depth runs downward throughout, as it does on every figure
in the chapter. Long captions go in figure coordinates, so they never fight the
equal aspect ratio the circular panels need.
"""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, Polygon, Arc

INK, GND, SRC, FLD = "#6b7280", "#8a9199", "#EC6842", "#00A6D6"


def arrow(ax, p0, p1, color=SRC, lw=2.0, scale=13, z=5):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=scale,
                                 color=color, lw=lw, zorder=z, shrinkA=0, shrinkB=0))


def bare(ax, xlim, ylim, equal=False):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    if equal:
        ax.set_aspect("equal")


def caption(fig, text, y=0.035, size=8.5):
    fig.text(0.5, y, text, ha="center", va="bottom", color=INK, fontsize=size)


# ---------------------------------------------------------------------------
# Part 1: an infinite current sheet, seen edge-on
# ---------------------------------------------------------------------------
def sheet():
    fig, ax = plt.subplots(figsize=(6.8, 3.1))
    ax.add_patch(Rectangle((-1.0, -1.0), 2.0, 1.0, fc=GND, ec="none", alpha=0.16))
    ax.text(0.97, -0.96, "conductor  $\\sigma,\\ \\mu$", ha="right", va="bottom",
            color=INK, fontsize=9)

    # the sheet itself
    ax.plot([-1.0, 1.0], [0, 0], color=SRC, lw=3, solid_capstyle="butt", zorder=4)
    for x in np.linspace(-0.88, 0.72, 7):
        arrow(ax, (x, 0), (x + 0.16, 0), scale=9, lw=1.3)
    ax.text(0.0, 0.07, "current sheet at $z=0$:  current $I$ per unit width along $x$,"
            " infinite in $x$ and $y$",
            ha="center", va="bottom", color=SRC, fontsize=9)

    # depth axis
    arrow(ax, (-1.18, 0.0), (-1.18, -0.95), color=INK, lw=1.2, scale=11)
    ax.text(-1.23, -0.48, "depth $z$", ha="right", va="center", color=INK,
            fontsize=9.5, rotation=90)

    # spreading front, then the three receivers
    for z in np.linspace(-0.10, -0.94, 8):          # the spreading front, left margin only
        ax.plot([-0.97, -0.45], [z, z], color=FLD, lw=0.9, ls=":", alpha=0.55, zorder=2)
    for z, lab in ((-0.22, "100 m"), (-0.45, "300 m"), (-0.82, "1000 m")):
        ax.add_patch(Polygon([(-0.06, z), (0.06, z), (0.0, z + 0.055)], closed=True,
                             fc=FLD, ec=FLD, zorder=6))
        ax.text(0.11, z, f"receiver at {lab}", ha="left", va="center", color=FLD,
                fontsize=9)
        arrow(ax, (-0.36, z), (-0.11, z), color=FLD, lw=1.5, scale=10)
    ax.text(-0.40, -0.22, "$E_x$", ha="right", va="center", color=FLD, fontsize=10)

    bare(ax, (-1.45, 1.35), (-1.12, 0.26))
    caption(fig, "The field diffuses downward. The solution is even in $z$, so reading $z$"
                 " as depth idealises away the air above.")
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig("setup_sheet.svg", transparent=True, metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------------------
# Part 2: an infinite wire, and the plane the fields live in
# ---------------------------------------------------------------------------
def wire():
    fig, (a0, a1) = plt.subplots(1, 2, figsize=(7.4, 3.2),
                                 gridspec_kw=dict(width_ratios=[0.85, 1.15]))

    # left: the wire, with the plane of interest cutting it
    a0.plot([0, 0], [-1.1, 1.1], color=SRC, lw=3, zorder=5)
    for y in (-0.8, -0.05, 0.6):
        arrow(a0, (0, y), (0, y + 0.26), scale=11, lw=1.6)
    a0.text(0.1, 1.05, "wire along $z$,\ncurrent $I$", ha="left", va="top",
            color=SRC, fontsize=9.5)
    a0.add_patch(Polygon([(-0.95, -0.38), (0.5, -0.64), (0.95, -0.02), (-0.5, 0.24)],
                         closed=True, fc=FLD, ec=FLD, alpha=0.20, lw=1.2, zorder=2))
    a0.text(-1.08, -0.62, "the $(x,y)$-plane", ha="left", va="top", color=FLD,
            fontsize=9.5)
    a0.set_title("side view", color=INK, fontsize=9.5, pad=6)
    bare(a0, (-1.15, 1.35), (-1.35, 1.25))

    # right: that plane, seen along the wire
    for r in (0.34, 0.60, 0.86):
        a1.add_patch(Circle((0, 0), r, fc="none", ec=FLD, lw=1.3, ls="--", alpha=0.85))
    a1.add_patch(Arc((0, 0), 1.20, 1.20, theta1=22, theta2=68, color=FLD, lw=1.9))
    th = np.deg2rad(68)
    arrow(a1, (0.60 * np.cos(th), 0.60 * np.sin(th)),
          (0.60 * np.cos(th + 0.22), 0.60 * np.sin(th + 0.22)), color=FLD, lw=1.9,
          scale=13)
    a1.text(0.34, 0.80, "$\\boldsymbol{H}$ circles the wire", ha="left", va="bottom",
            color=FLD, fontsize=9.5)

    a1.add_patch(Circle((0, 0), 0.085, fc="none", ec=SRC, lw=2, zorder=6))
    a1.add_patch(Circle((0, 0), 0.026, fc=SRC, ec=SRC, zorder=6))
    a1.text(0.0, -0.14, "$I$ out, $E_z$ in", ha="center", va="top", color=SRC, fontsize=9)

    ta = np.deg2rad(-32)
    arrow(a1, (0, 0), (0.86 * np.cos(ta), 0.86 * np.sin(ta)), color=INK, lw=1.3,
          scale=11)
    a1.text(0.50, -0.40, "$\\varrho$", ha="left", va="top", color=INK, fontsize=11)
    a1.set_title("seen along the wire", color=INK, fontsize=9.5, pad=6)
    bare(a1, (-1.1, 1.25), (-1.1, 1.1), equal=True)

    caption(fig, "Nothing depends on $z$, so the fields live in the $(x,y)$-plane:"
                 " $I$ points out of it and $E_z$ into it, $\\boldsymbol{H}$ lies in it.\n"
                 "Receivers sit at three distances from the wire.", y=0.02)
    fig.tight_layout(rect=(0, 0.15, 1, 1))
    fig.savefig("setup_wire.svg", transparent=True, metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------------------
# Part 3: the same kernel, spreading over a plane, a cylinder and a sphere
# ---------------------------------------------------------------------------
def ladder():
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 3.0))
    titles = ("sheet, 1-D", "wire, 2-D", "point, 3-D")
    pees = ("$p = 1/2$", "$p = 1$", "$p = 3/2$")
    tps = ("$t_p = ?$", "$t_p = ?$", "$t_p = ?$")
    spreads = ("spreads one way", "spreads over a circle", "spreads over a sphere")

    for k, ax in enumerate(axes):
        if k == 0:
            ax.plot([-0.85, 0.85], [0, 0], color=SRC, lw=3, zorder=5)
            for z in (0.26, 0.5, 0.74):
                for s in (1, -1):
                    ax.plot([-0.85, 0.85], [s * z, s * z], color=FLD, lw=1.2, ls="--",
                            alpha=0.85)
            arrow(ax, (0.0, 0.0), (0.0, -0.72), color=FLD, lw=1.6)
            ax.text(0.09, -0.38, "$r$", color=FLD, fontsize=11, va="center")
        else:
            fills = (0.0, 0.11)[k == 2]
            for r, al in ((0.30, 0.9), (0.54, 0.65), (0.78, 0.4)):
                if fills:
                    ax.add_patch(Circle((0, 0), r, fc=FLD, ec="none", alpha=fills))
                ax.add_patch(Circle((0, 0), r, fc="none", ec=FLD, lw=1.2, ls="--",
                                    alpha=al))
            ax.add_patch(Circle((0, 0), 0.05, fc=SRC, ec=SRC, zorder=6))
            aa = np.deg2rad(38)
            arrow(ax, (0, 0), (0.78 * np.cos(aa), 0.78 * np.sin(aa)), color=FLD, lw=1.6)
            ax.text(0.20, 0.44, "$r$", color=FLD, fontsize=11,
                    ha="right", va="bottom")

        ax.set_title(titles[k], color=INK, fontsize=10.5, pad=8)
        ax.text(0.0, -1.06, spreads[k], ha="center", va="top", color=INK, fontsize=8.5)
        ax.text(0.0, -1.34, pees[k], ha="center", va="top", color=SRC, fontsize=11.5)
        ax.text(0.0, -1.66, tps[k], ha="center", va="top", color=INK, fontsize=10.5)
        bare(ax, (-1.0, 1.0), (-2.0, 1.0), equal=True)

    caption(fig, "One kernel, $\\exp(-\\sigma\\mu r^2/4t)$. Only the prefactor $t^{-p}$"
                 " changes. Your $t_p(r, p)$ fills in the three question marks.", y=0.025)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig("setup_ladder.svg", transparent=True, metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------------------
# Part 4: the loop, and the two planes the lab cuts through it
# ---------------------------------------------------------------------------
def loop():
    # axonometric projection: x right, y toward the viewer (down-left), z down
    def P(x, y, z):
        return (x - 0.52 * y, -0.30 * y - 0.92 * z)

    L, zc = 1.0, 0.72                       # half-side, and the depth of the (x,y) cut
    fig, ax = plt.subplots(figsize=(6.8, 3.6))

    # the vertical cut at y = 0, drawn first so the rest sits on top
    ax.add_patch(Polygon([P(-1.75, 0, -0.05), P(1.75, 0, -0.05), P(1.75, 0, 1.05),
                          P(-1.75, 0, 1.05)], closed=True, fc=FLD, ec=FLD, lw=1.0,
                         alpha=0.13, zorder=1))
    # the ground surface
    ax.add_patch(Polygon([P(-1.9, -1.8, 0), P(1.9, -1.8, 0), P(1.9, 1.8, 0),
                          P(-1.9, 1.8, 0)], closed=True, fc=GND, ec=INK, lw=0.8,
                         alpha=0.13, zorder=2))
    ax.text(*P(1.92, -1.8, 0), s="  surface", ha="left", va="center", color=INK,
            fontsize=9)
    # the horizontal cut at z = 10 m
    ax.add_patch(Polygon([P(-1.7, -1.6, zc), P(1.7, -1.6, zc), P(1.7, 1.6, zc),
                          P(-1.7, 1.6, zc)], closed=True, fc=FLD, ec=FLD, lw=1.1,
                         alpha=0.20, zorder=3))
    ax.text(*P(1.72, -1.6, zc), s="  the $(x,y)$-plane at $z=10$ m", ha="left",
            va="center", color=FLD, fontsize=9)
    ax.text(*P(-1.78, 0, 0.62), s="the $(x,z)$-plane\nat $y=0$   ", ha="right",
            va="center", color=FLD, fontsize=9)

    # the loop, 1 -> 2 -> 3 -> 4: clockwise seen from above, with z downward
    verts = [(-L, -L), (L, -L), (L, L), (-L, L)]
    for k in range(4):
        x0, y0 = verts[k]
        x1, y1 = verts[(k + 1) % 4]
        ax.plot(*zip(P(x0, y0, 0), P(x1, y1, 0)), color=SRC, lw=2.6, zorder=6,
                solid_capstyle="round")
        arrow(ax, P(x0 + 0.40 * (x1 - x0), y0 + 0.40 * (y1 - y0), 0),
              P(x0 + 0.60 * (x1 - x0), y0 + 0.60 * (y1 - y0), 0), scale=13, z=7)
    for (vx, vy), k in zip(verts, "1234"):
        px, py = P(vx, vy, 0)
        ax.text(px + (0.10 if vx > 0 else -0.10), py + 0.06, k, ha="center",
                va="bottom", color=SRC, fontsize=10.5, zorder=8)
    ax.text(-2.40, 0.88, "square loop on the surface\n$L_x = L_y = 100$ m\n"
            "$I$ switched on at $t=0$", ha="left", va="top", color=SRC,
            fontsize=9.5, zorder=8, linespacing=1.45)

    # axes, from the centre of the loop
    for (dx, dy, dz), lab, off in (((0.70, 0, 0), "$x$", (0.10, 0.02)),
                                   ((0, 0.70, 0), "$y$", (-0.10, -0.05)),
                                   ((0, 0, 0.95), "$z$", (0.10, 0.0))):
        arrow(ax, P(0, 0, 0), P(dx, dy, dz), color=INK, lw=1.3, scale=12, z=9)
        px, py = P(dx, dy, dz)
        ax.text(px + off[0], py + off[1], lab, color=INK, fontsize=11, zorder=9,
                ha="center", va="center")

    bare(ax, (-2.45, 3.15), (-1.45, 0.95))
    caption(fig, "The field is cut in the vertical plane $y = 0$ and in a horizontal"
                 " plane at depth $z$, with $D = \\sqrt{4t/\\sigma\\mu}$.")
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig("setup_loop.svg", transparent=True, metadata={"Date": None})
    plt.close(fig)


if __name__ == "__main__":
    sheet(); wire(); ladder(); loop()
    print("wrote setup_sheet.svg, setup_wire.svg, setup_ladder.svg, setup_loop.svg")
