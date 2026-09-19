"""Reproduce the chapter's vector figures: python plot_magnetic_fields.py."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 12, "svg.fonttype": "none"})
BLUE, ORANGE, INK = "#1769aa", "#bd561b", "#243746"


def arrow(ax, start, end, color=BLUE, lw=1.8):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw))


def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", facecolor="white")
    fig.savefig(Path('/tmp') / f"{name}.png", dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def wire():
    fig, ax = plt.subplots(figsize=(7, 5.5))
    for r in [.6, 1.15, 1.7]:
        ax.add_patch(Circle((0, 0), r, fill=False, color=BLUE, lw=1.8))
        for t in [.3, 2.4, 4.5]:
            arrow(ax, (r*np.cos(t), r*np.sin(t)),
                  (r*np.cos(t+.16), r*np.sin(t+.16)))
    ax.scatter([0], [0], s=240, facecolor="white", edgecolor=ORANGE, lw=2, zorder=5)
    ax.scatter([0], [0], s=35, color=ORANGE, zorder=6)
    ax.text(0, -1.95, "$I$: out of the page", color=ORANGE, ha="center")
    arrow(ax, (0, 0), (1.15, 0), INK, 1.2)
    ax.text(.4, .09, "$s$", color=INK)
    arrow(ax, (1.15, 0), (1.15, .65))
    ax.text(1.27, .4, "$\\vec B$", color=BLUE)
    ax.text(-.97, .85, "$C$", color=BLUE)
    ax.set_title("Straight wire: field in a perpendicular plane", pad=18)
    ax.text(0, -2.3, "$B=\\mu_0 I/(2\\pi s)$     •     counterclockwise circulation", ha="center")
    ax.set(xlim=(-2.2, 2.2), ylim=(-2.5, 1.95), aspect="equal")
    ax.axis("off")
    save(fig, "straight_wire_field")


def linked_paths():
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    cases = [(1, .6, [0], "(a) Linked once", "$I_{\\rm linked}=I$\n$\\oint_C\\vec B\\cdot d\\vec\\ell=\\mu_0 I$"),
             (0, .58, [0], "(b) Unlinked: no crossings", "$I_{\\rm linked}=0$\n$\\oint_C\\vec B\\cdot d\\vec\\ell=0$"),
             (0, 1.4, [0], "(c) Unlinked: opposite crossings", "$I_{\\rm linked}=I-I=0$\n$\\oint_C\\vec B\\cdot d\\vec\\ell=0$"),
             (1, .78, [-.36, 0, .36], "(d) Three turns linked", "$I_{\\rm linked}=3I$\n$\\oint_C\\vec B\\cdot d\\vec\\ell=3\\mu_0 I$")]
    t = np.linspace(0, 2*np.pi, 600)
    for ax, (c, r, offsets, title, result) in zip(axes.flat, cases):
        # Turns lie in parallel xy planes; disk lies in xz.
        # Projection (x,y,z) -> (x+.35*y, z+.5*y); y<0 is in front.
        back = np.linspace(0, np.pi, 300)
        front = np.linspace(np.pi, 2*np.pi, 300)
        bx = np.cos(back)+.35*np.sin(back)
        for z0 in offsets:
            ax.plot(bx, z0+.5*np.sin(back), color=ORANGE, lw=2.5)
        ax.fill(c+r*np.cos(t), r*np.sin(t), color="#edf5fb", zorder=3)
        ax.plot(c+r*np.cos(t), r*np.sin(t), color=BLUE, lw=2, zorder=4)
        for z0 in offsets:
            by = z0+.5*np.sin(back)
            hidden = (bx-c)**2+by**2 < r*r
            ax.plot(np.where(hidden, bx, np.nan), by, color=ORANGE,
                    lw=1.8, ls=(0, (4, 3)), zorder=4)
            ax.plot(np.cos(front)+.35*np.sin(front), z0+.5*np.sin(front),
                    color=ORANGE, lw=2.5, zorder=5)
            for x in [-1, 1]:
                if (x-c)**2+z0**2 < r*r:
                    ax.scatter([x], [z0], color=ORANGE, s=30, zorder=7)
                    ax.text(x+(.22 if x == 1 else -.22), z0-.12,
                            "$+I$" if x == 1 else "$-I$", color=ORANGE,
                            ha="center", fontsize=11, zorder=8)
            a, b = 4.15, 4.4
            arrow(ax, (np.cos(a)+.35*np.sin(a), z0+.5*np.sin(a)),
                  (np.cos(b)+.35*np.sin(b), z0+.5*np.sin(b)), ORANGE, 2)
        # Clockwise path in xz has normal +y; right-hand crossings carry +I.
        arrow(ax, (c, r), (c+.22, np.sqrt(r*r-.22**2)))
        ax.text(c-.16, r+.12, "$C$", color=BLUE)
        ax.text(c-.3, .12 if len(offsets)>1 else .20, "$S$",
                color=BLUE, ha="center", zorder=6)
        ax.text(-.35, min(offsets)-.78, "$I$", color=ORANGE)
        ax.set_title(title, fontsize=13, pad=10)
        ax.text(.1, -1.85, result, ha="center", va="top", linespacing=1.8)
        ax.set(xlim=(-1.75, 1.95), ylim=(-2.5, 1.8), aspect="equal")
        ax.axis("off")
    fig.suptitle("Orange: current loop or coil\nBlue: integration path C and spanning surface S", fontsize=14)
    fig.tight_layout(rect=(0, 0, 1, .95))
    save(fig, "loop_linked_paths")


def dipoles():
    v = np.linspace(-3, 3, 351)
    x, z = np.meshgrid(v, v)
    for kind in ["electric", "magnetic"]:
        fx, fz = np.zeros_like(x), np.zeros_like(x)
        if kind == "electric":
            for q, z0 in [(1, .65), (-1, -.65)]:
                rr = x*x+(z-z0)**2
                fx += q*x / np.maximum(rr, 1e-12)**1.5
                fz += q*(z-z0) / np.maximum(rr, 1e-12)**1.5
            mask = (x*x+(z-.65)**2 < .13**2) | (x*x+(z+.65)**2 < .13**2)
        else:
            # Midpoint Biot-Savart quadrature of a unit-radius circular loop.
            # Omit the overall mu0 I / (4 pi) factor: only directions are plotted.
            n = 600
            for t in (np.arange(n)+.5)*2*np.pi/n:
                dx, dy = x-np.cos(t), -np.sin(t)
                rr = (dx*dx+dy*dy+z*z)**1.5
                fx += np.cos(t)*z/rr * (2*np.pi/n)
                fz += (1-x*np.cos(t))/rr * (2*np.pi/n)
            mask = ((x-1)**2+z*z < .13**2) | ((x+1)**2+z*z < .13**2)
        fx[mask], fz[mask] = np.nan, np.nan
        fig, ax = plt.subplots(figsize=(6.6, 6.9))
        if kind == "magnetic":
            theta = (np.arange(240)+.5)*2*np.pi/240
            ct, st = np.cos(theta), np.sin(theta)
            def tangent(_, point):
                xx, zz = point
                rr = ((xx-ct)**2+st**2+zz**2)**1.5
                field = np.array([np.sum(ct*zz/rr), np.sum((1-xx*ct)/rr)])
                return field / np.linalg.norm(field)
            for seed in [.08, .2, .4, .55, .7, .84]:
                point = np.array([seed, 1e-6])
                points = [point.copy()]
                escaped = False
                h = .008
                for _ in range(6000):
                    k1 = tangent(0, point)
                    k2 = tangent(0, point+h*k1/2)
                    k3 = tangent(0, point+h*k2/2)
                    k4 = tangent(0, point+h*k3)
                    new = point+h*(k1+2*k2+2*k3+k4)/6
                    if point[1] < 0 <= new[1]:
                        points.append(np.array([seed, 0]))
                        break
                    points.append(new.copy())
                    point = new
                    if np.max(np.abs(point)) > 3.02:
                        escaped = True
                        break
                points = np.array(points)
                for sign in [-1, 1]:
                    xx, zz = sign*points[:, 0], points[:, 1]
                    # Reflect the upper outgoing segment below the midplane
                    # when its return lies beyond the plotted window.
                    ax.plot(xx, zz, color=BLUE, lw=1.3)
                    if escaped:
                        ax.plot(xx, -zz, color=BLUE, lw=1.3)
                    for fraction in [.2, .65]:
                        k = int(fraction*(len(xx)-2))
                        arrow(ax, (xx[k], zz[k]), (xx[min(k+8, len(xx)-1)], zz[min(k+8, len(xx)-1)]), lw=1.3)
        else:
            seed_x = np.array([-2.9, -2.2, -1.4, -.9, -.55, -.3, -.12, .12, .3, .55, .9, 1.4, 2.2, 2.9])
            extra = [[xx, zz] for xx in [-2, -1, -.4, .4, 1, 2] for zz in [-2.9, 2.9]]
            seeds = np.vstack((np.column_stack((seed_x, np.zeros_like(seed_x))), extra))
            ax.streamplot(v, v, fx, fz, start_points=seeds, color=BLUE,
                          density=2, linewidth=1.3, arrowsize=1.3, broken_streamlines=False)
        if kind == "electric":
            for z0, label, col in [(.65, "+", ORANGE), (-.65, "−", BLUE)]:
                ax.add_patch(Circle((0, z0), .14, color=col, zorder=5))
                ax.text(0, z0, label, ha="center", va="center", color="white", zorder=6)
            arrow(ax, (.45, -.4), (.45, .4), INK, 2)
            ax.text(.54, .02, "$\\vec p$", color=INK)
            title = "Electric dipole: electric field E"
            note = "Field lines leave +q and end on −q."
        else:
            for x0, symbol in [(-1, "⊙"), (1, "⊗")]:
                ax.add_patch(Circle((x0, 0), .15, color="white", zorder=5))
                ax.text(x0, 0, symbol, ha="center", va="center", color=ORANGE, fontsize=23, zorder=6)
            arrow(ax, (0, -.38), (0, .42), INK, 2)
            ax.text(.1, .08, "$\\vec m$", color=INK)
            title = "Current loop: magnetic field B"
            note = "Wire seen edge-on: ⊙ current out, ⊗ current in.\nField lines continue through the centre of the loop."
        ax.set_title(title, pad=16)
        ax.text(.5, -.04, note, ha="center", va="top", transform=ax.transAxes, fontsize=11)
        ax.set(xlim=(-3, 3), ylim=(-3, 3), aspect="equal")
        ax.axis("off")
        save(fig, f"{kind}_dipole_field")


if __name__ == "__main__":
    wire()
    linked_paths()
    dipoles()
