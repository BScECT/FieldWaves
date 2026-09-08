"""Generate field-line and equipotential figures for the electrostatics chapter."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


FIGURE_DIR = Path(__file__).parent / "figures"
FIGURE_DIR.mkdir(exist_ok=True)


def point_charge_field(x, z, charges):
    """Return dimensionless potential and field for (charge, x, z) tuples."""
    potential = np.zeros_like(x, dtype=float)
    field_x = np.zeros_like(x, dtype=float)
    field_z = np.zeros_like(z, dtype=float)

    for charge, source_x, source_z in charges:
        dx = x - source_x
        dz = z - source_z
        radius_squared = dx**2 + dz**2
        radius = np.sqrt(radius_squared)
        with np.errstate(divide="ignore", invalid="ignore"):
            potential += charge / radius
            field_x += charge * dx / radius**3
            field_z += charge * dz / radius**3

    return potential, field_x, field_z


def mask_near_sources(values, x, z, charges, radius=0.09):
    """Mask singular neighbourhoods for stable contour and streamline plots."""
    masked = np.array(values, copy=True)
    for _, source_x, source_z in charges:
        masked[np.hypot(x - source_x, z - source_z) < radius] = np.nan
    return masked


def plot_dipole():
    x_values = np.linspace(-2.2, 2.2, 500)
    z_values = np.linspace(-1.7, 1.7, 400)
    x, z = np.meshgrid(x_values, z_values)
    charges = [(1.0, -0.7, 0.0), (-1.0, 0.7, 0.0)]
    potential, field_x, field_z = point_charge_field(x, z, charges)

    potential = mask_near_sources(potential, x, z, charges)
    field_x = mask_near_sources(field_x, x, z, charges)
    field_z = mask_near_sources(field_z, x, z, charges)
    potential = np.clip(potential, -3.0, 3.0)

    fig, ax = plt.subplots(figsize=(8.8, 5.8), layout="constrained")
    levels = [-2.0, -1.2, -0.7, -0.35, -0.15, 0, 0.15, 0.35, 0.7, 1.2, 2.0]
    ax.contour(x, z, potential, levels=levels, colors="0.55", linewidths=0.8)
    ax.streamplot(
        x_values,
        z_values,
        field_x,
        field_z,
        color="#1769aa",
        density=1.25,
        linewidth=1.0,
        arrowsize=1.1,
    )
    ax.scatter([-0.7, 0.7], [0, 0], s=180, c=["#c43c39", "#2764ae"], zorder=4)
    ax.text(-0.7, 0, "+", color="white", ha="center", va="center", weight="bold")
    ax.text(0.7, 0, "−", color="white", ha="center", va="center", weight="bold")
    ax.set(xlabel="$x$", ylabel="$z$", xlim=(-2.2, 2.2), ylim=(-1.7, 1.7))
    ax.set_aspect("equal")
    ax.set_title("Electric dipole: field lines and equipotentials")
    fig.savefig(FIGURE_DIR / "electric_dipole_field.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_cloud_ground():
    x_values = np.linspace(-3.0, 3.0, 600)
    z_values = np.linspace(-2.2, 2.2, 500)
    x, z = np.meshgrid(x_values, z_values)
    height = 1.0
    charges = [(1.0, 0.0, height), (-1.0, 0.0, -height)]
    potential, field_x, field_z = point_charge_field(x, z, charges)

    potential = mask_near_sources(potential, x, z, charges)
    field_x = mask_near_sources(field_x, x, z, charges)
    field_z = mask_near_sources(field_z, x, z, charges)
    potential = np.clip(potential, -3.0, 3.0)

    fig, ax = plt.subplots(figsize=(8.8, 6.2), layout="constrained")
    levels = [-2.0, -1.2, -0.7, -0.35, -0.15, 0, 0.15, 0.35, 0.7, 1.2, 2.0]
    ax.contour(x, z, potential, levels=levels, colors="0.55", linewidths=0.8)
    ax.streamplot(
        x_values,
        z_values,
        field_x,
        field_z,
        color="#1769aa",
        density=1.15,
        linewidth=1.0,
        arrowsize=1.1,
    )
    ax.axhspan(-2.2, 0, color="#e8ecef", alpha=0.88, zorder=2)
    ax.axhline(0, color="#202428", linewidth=2.2, zorder=3)
    ax.scatter([0], [height], s=190, c="#c43c39", zorder=4)
    ax.text(0, height, "+Q", color="white", ha="center", va="center", weight="bold")
    ax.scatter([0], [-height], s=190, facecolors="none", edgecolors="#2764ae", zorder=4)
    ax.text(0, -height, "−Q", color="#2764ae", ha="center", va="center", weight="bold")
    ax.text(-2.85, 0.08, "physical region", va="bottom", color="0.25")
    ax.text(-2.85, -0.08, "image construction", va="top", color="0.35")
    ax.set(xlabel="$x$", ylabel="$z$", xlim=(-3, 3), ylim=(-2.2, 2.2))
    ax.set_aspect("equal")
    ax.set_title("Point-cloud model above grounded conducting Earth")
    fig.savefig(FIGURE_DIR / "cloud_ground_field.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    plot_dipole()
    plot_cloud_ground()
