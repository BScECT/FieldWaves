"""Plotting and self-check helpers for the ECTB2140 *Fields and Waves* labs.

You are **not** expected to read or edit this file during a lab session. It
exists so that your time goes on the physics -- writing fields, gradients and
divergences -- rather than on plotting boilerplate.

Everything here works on a 3-D Cartesian grid built with ``indexing='ij'``,
which means the array axes are (x, y, z) in that order. That choice matters:
it makes ``np.gradient(F, dx, dy, dz)`` return the derivatives in the same
order as the coordinates, with no index gymnastics.

Requires: numpy, matplotlib, plotly.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

__all__ = [
    "make_grid_3d", "z0_index", "slice_z0",
    "box_indices", "area_integral", "volume_integral",
    "show_isosurfaces", "show_cones", "show_scalar_slice", "show_field_slice",
    "check", "check_shape", "check_close", "check_scalar",
]

# --------------------------------------------------------------------------
# Grid
# --------------------------------------------------------------------------

def make_grid_3d(n: int = 61, L: float = 2.0):
    """A cube of sample points on [-L, L]^3 with n points per side.

    Returns
    -------
    X, Y, Z : (n, n, n) float arrays
        Coordinates, built with indexing='ij' so that X[i, j, k] = x[i],
        Y[i, j, k] = y[j] and Z[i, j, k] = z[k].
    dx, dy, dz : float
        Uniform spacings. np.gradient needs these -- omit them and it assumes
        a spacing of 1, making every derivative wrong by a constant factor.
    """
    if n % 2 == 0:
        raise ValueError("use an odd n so that the grid contains the origin exactly")
    a = np.linspace(-L, L, n)
    X, Y, Z = np.meshgrid(a, a, a, indexing="ij")
    h = a[1] - a[0]
    return X, Y, Z, h, h, h


def z0_index(Z: np.ndarray) -> int:
    """Index k of the z = 0 plane in an indexing='ij' grid."""
    return int(np.argmin(np.abs(Z[0, 0, :])))


def slice_z0(F: np.ndarray, Z: np.ndarray) -> np.ndarray:
    """The z = 0 plane of a scalar field, as a 2-D (x, y) array."""
    return F[:, :, z0_index(Z)]


# --------------------------------------------------------------------------
# Integration over grid-aligned boxes and faces
#
# These evaluate the integrals in the definition of the divergence and in the
# divergence theorem. They are quadrature boilerplate: the trapezoidal weights
# below simply stop the end samples from being counted as full cells.
# --------------------------------------------------------------------------

def _trapezoid_weights(n: int) -> np.ndarray:
    w = np.ones(n)
    w[0] = w[-1] = 0.5
    return w


def box_indices(X: np.ndarray, half_width: float):
    """Index range (i0, i1) of the sub-cube |x|, |y|, |z| <= ``half_width``.

    The same pair works on all three axes because the grid is cubic. The
    returned indices are snapped to the nearest grid planes, so ask for a
    half-width that is a multiple of the spacing (0.6, 1.0 and 1.4 m are
    exact on the default 61-point grid) if you want the box you asked for.
    """
    axis = X[:, 0, 0]
    i0 = int(np.argmin(np.abs(axis + half_width)))
    i1 = int(np.argmin(np.abs(axis - half_width)))
    return i0, i1


def area_integral(F2: np.ndarray, da: float, db: float) -> float:
    """Integrate a 2-D array of samples over the rectangle it spans.

    Use it on one face of a box to evaluate that face's contribution to a
    surface integral.
    """
    F2 = np.asarray(F2, float)
    wa, wb = _trapezoid_weights(F2.shape[0]), _trapezoid_weights(F2.shape[1])
    return float(np.nansum(F2 * wa[:, None] * wb[None, :]) * da * db)


def volume_integral(F3: np.ndarray, dx: float, dy: float, dz: float) -> float:
    """Integrate a 3-D array of samples over the box it spans."""
    F3 = np.asarray(F3, float)
    wx, wy, wz = (_trapezoid_weights(m) for m in F3.shape)
    w = wx[:, None, None] * wy[None, :, None] * wz[None, None, :]
    return float(np.nansum(F3 * w) * dx * dy * dz)


# --------------------------------------------------------------------------
# 3-D views (plotly)
# --------------------------------------------------------------------------

def show_isosurfaces(X, Y, Z, F, levels, *, title="", opacity=0.35,
                     colorscale="Viridis", show_caps=False, size=620, step=2):
    """Draw one or more isosurfaces (level sets) of a scalar field F.

    An isosurface is the set of points where F takes one fixed value -- the
    3-D analogue of a contour line. Transparency lets you see the inner
    surfaces through the outer ones, so pass a list of levels and look at the
    nesting.
    """
    levels = np.atleast_1d(np.asarray(levels, dtype=float))
    # Subsample before handing the volume to plotly. A full 61^3 grid embeds
    # ~12 MB of JSON per figure; every other point looks identical on screen.
    sl = (slice(None, None, step),) * 3
    X, Y, Z, F = X[sl], Y[sl], Z[sl], np.asarray(F)[sl]
    fig = go.Figure(
        go.Isosurface(
            x=X.ravel(), y=Y.ravel(), z=Z.ravel(), value=np.asarray(F).ravel(),
            isomin=float(levels.min()), isomax=float(levels.max()),
            surface_count=int(levels.size), opacity=opacity,
            colorscale=colorscale, showscale=True,
            caps=dict(x_show=show_caps, y_show=show_caps, z_show=show_caps),
        )
    )
    _style_3d(fig, title, size)
    return fig


def show_cones(X, Y, Z, Ax, Ay, Az, *, step=8, title="", sizeref=0.6,
               colorscale="Blues", size=620, normalise=False):
    """Draw a 3-D vector field as a lattice of cones (arrows).

    Only every ``step``-th sample in each direction is drawn -- a full grid of
    cones is an unreadable haystack. Set ``normalise=True`` to show direction
    only, with every cone the same length; this is often clearer for fields
    whose magnitude varies over orders of magnitude.
    """
    sl = (slice(None, None, step),) * 3
    x, y, z = X[sl].ravel(), Y[sl].ravel(), Z[sl].ravel()
    u, v, w = np.asarray(Ax)[sl].ravel(), np.asarray(Ay)[sl].ravel(), np.asarray(Az)[sl].ravel()

    finite = np.isfinite(u) & np.isfinite(v) & np.isfinite(w)
    x, y, z, u, v, w = (a[finite] for a in (x, y, z, u, v, w))

    if normalise:
        mag = np.sqrt(u**2 + v**2 + w**2)
        mag[mag == 0] = 1.0
        u, v, w = u / mag, v / mag, w / mag

    fig = go.Figure(
        go.Cone(x=x, y=y, z=z, u=u, v=v, w=w,
                sizemode="scaled", sizeref=sizeref, anchor="tail",
                colorscale=colorscale, showscale=True,
                colorbar=dict(title="|A|")),
    )
    _style_3d(fig, title, size)
    return fig


def _style_3d(fig, title, size):
    fig.update_layout(
        title=title, width=size, height=size,
        margin=dict(l=0, r=0, t=40 if title else 0, b=0),
        scene=dict(
            xaxis_title="x [m]", yaxis_title="y [m]", zaxis_title="z [m]",
            aspectmode="cube",          # equal aspect: never distort a field
            camera=dict(eye=dict(x=1.6, y=1.6, z=1.1)),
        ),
    )


# --------------------------------------------------------------------------
# 2-D views of the z = 0 plane (matplotlib)
# --------------------------------------------------------------------------

def show_scalar_slice(X, Y, Z, F, *, title="", label="", cmap="RdYlBu_r",
                      levels=25, symmetric=False, percentile=99, ax=None):
    """Filled contours of a scalar field in the z = 0 plane."""
    k = z0_index(Z)
    x2, y2, f2 = X[:, :, k], Y[:, :, k], np.asarray(F)[:, :, k]

    hi = np.nanpercentile(np.abs(f2) if symmetric else f2, percentile)
    lo = -hi if symmetric else np.nanpercentile(f2, 100 - percentile)
    lv = np.linspace(lo, hi, levels)

    created = ax is None
    if created:
        _, ax = plt.subplots(figsize=(5.4, 4.5))
    cf = ax.contourf(x2, y2, np.clip(f2, lo, hi), levels=lv, cmap=cmap, extend="both")
    ax.set_aspect("equal")                 # course rule: never distort a field plot
    ax.set_xlabel("$x$ [m]")
    ax.set_ylabel("$y$ [m]")
    ax.set_title(title)
    if created:
        ax.figure.colorbar(cf, ax=ax, label=label)
    return ax, cf


def show_field_slice(X, Y, Z, Ax, Ay, *, background=None, title="", label="",
                     cmap="RdBu_r", density=1.3, symmetric=True, ax=None,
                     percentile=98):
    """Streamlines of a vector field in the z = 0 plane, over an optional
    scalar background (typically the potential that generated it)."""
    k = z0_index(Z)
    created = ax is None
    if created:
        _, ax = plt.subplots(figsize=(5.8, 4.8))

    cf = None
    if background is not None:
        _, cf = show_scalar_slice(X, Y, Z, background, cmap=cmap, symmetric=symmetric,
                                  percentile=percentile, ax=ax)

    # streamplot needs 1-D increasing axes and arrays shaped (ny, nx); our
    # indexing='ij' arrays are (nx, ny), hence the transposes.
    x1 = X[:, 0, k]
    y1 = Y[0, :, k]
    u = np.nan_to_num(np.asarray(Ax)[:, :, k]).T
    v = np.nan_to_num(np.asarray(Ay)[:, :, k]).T
    ax.streamplot(x1, y1, u, v, color="k", linewidth=0.7,
                  density=density, arrowsize=0.9)

    ax.set_aspect("equal")
    ax.set_xlim(x1.min(), x1.max())
    ax.set_ylim(y1.min(), y1.max())
    ax.set_xlabel("$x$ [m]")
    ax.set_ylabel("$y$ [m]")
    ax.set_title(title)
    if created and cf is not None:
        ax.figure.colorbar(cf, ax=ax, label=label)
    return ax


# --------------------------------------------------------------------------
# Self-checks
# --------------------------------------------------------------------------

def check(label: str, ok: bool, hint: str = "") -> None:
    """Report a pass, or raise with a hint about what to look at."""
    if ok:
        print(f"  [ok] {label}")
    else:
        raise AssertionError(f"{label} -- {hint}" if hint else label)


def check_shape(label: str, arr, expected) -> None:
    arr = np.asarray(arr)
    check(f"{label}: shape {arr.shape}", arr.shape == tuple(expected),
          f"expected {tuple(expected)}, got {arr.shape}. Did every array come "
          f"from the same grid?")


def check_close(label: str, got, want, rtol=0.05, where=None) -> None:
    """Compare two arrays where both are finite (and where `where` is True)."""
    got, want = np.asarray(got, float), np.broadcast_to(np.asarray(want, float), np.shape(got))
    m = np.isfinite(got) & np.isfinite(want)
    if where is not None:
        m = m & where
    if not m.any():
        raise AssertionError(f"{label} -- nothing left to compare; the mask removed every point")
    rel = np.abs(got[m] - want[m]) / np.maximum(np.abs(want[m]), 1e-30)
    worst = float(np.max(rel))
    check(f"{label}: worst error {worst:.2%}", worst < rtol,
          f"worst relative error {worst:.2%} exceeds {rtol:.0%}. Check your "
          f"np.gradient call -- did you pass dx, dy, dz, and in that order?")


def check_scalar(label: str, got: float, want: float, rtol: float = 0.01,
                 unit: str = "") -> None:
    """Compare two single numbers and report the relative discrepancy."""
    got, want = float(got), float(want)
    rel = abs(got - want) / max(abs(want), 1e-30)
    check(f"{label}: {got:.4g}{unit} vs {want:.4g}{unit} ({rel:.2%} apart)",
          rel < rtol,
          f"these should agree to better than {rtol:.0%}. Check the sign of "
          f"each face, and that every face uses its own outward normal.")
