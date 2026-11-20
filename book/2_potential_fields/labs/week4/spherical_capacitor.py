"""Simple model of a spherical capacitor: V(r) = A + B/r between the shells.

Boundary conditions: V(r_inner) = 0 and V(r_outer) = V_outer (user-set).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FIGURE_DIR = Path(__file__).parent / "figures"
FIGURE_DIR.mkdir(exist_ok=True)


def solve_coefficients(r_inner, r_outer, v_outer):
    """Solve for A, B given V(r_inner) = 0 and V(r_outer) = v_outer."""
    b = v_outer / (1.0 / r_outer - 1.0 / r_inner)
    a = -b / r_inner
    return a, b


def potential(r, r_inner, r_outer, v_outer):
    """Return V(r): 0 inside the inner shell, A + B/r between, v_outer beyond."""
    a, b = solve_coefficients(r_inner, r_outer, v_outer)
    v = np.full_like(r, v_outer, dtype=float)
    between = (r >= r_inner) & (r <= r_outer)
    v[between] = a + b / r[between]
    v[r < r_inner] = 0.0
    return v


def electric_field(r, r_inner, r_outer, v_outer):
    """Return E(r) = -dV/dr = B / r**2 between the shells, else zero."""
    _, b = solve_coefficients(r_inner, r_outer, v_outer)
    e = np.zeros_like(r, dtype=float)
    between = (r >= r_inner) & (r <= r_outer)
    e[between] = b / r[between] ** 2
    return e


def plot_spherical_capacitor(r_inner=1.0, r_outer=2.5, v_outer=10.0):
    r = np.linspace(0.01, 1.5 * r_outer, 500)
    v = potential(r, r_inner, r_outer, v_outer)
    e = electric_field(r, r_inner, r_outer, v_outer)

    fig, (ax_v, ax_e) = plt.subplots(2, 1, figsize=(7.5, 7.5), sharex=True, layout="constrained")

    ax_v.plot(r, v, color="#2764ae")
    ax_v.axvline(r_inner, color="0.6", linestyle="--", linewidth=1)
    ax_v.axvline(r_outer, color="0.6", linestyle="--", linewidth=1)
    ax_v.set_ylabel("$V(r)$")
    ax_v.set_title("Spherical capacitor: potential and field between shells")

    ax_e.plot(r, e, color="#c43c39")
    ax_e.axvline(r_inner, color="0.6", linestyle="--", linewidth=1)
    ax_e.axvline(r_outer, color="0.6", linestyle="--", linewidth=1)
    ax_e.set_xlabel("$r$")
    ax_e.set_ylabel("$E(r)$")

    fig.savefig(FIGURE_DIR / "spherical_capacitor.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    plot_spherical_capacitor()

