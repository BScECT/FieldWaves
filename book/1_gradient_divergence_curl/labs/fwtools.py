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
    "z0_index", "slice_z0",
    "box_indices", "area_integral", "volume_integral",
    "show_isosurfaces", "show_cones", "show_scalar_slice", "show_field_slice",
    "check", "check_shape", "check_close", "check_abs", "check_scalar",
]

# --------------------------------------------------------------------------
# Grid helpers (the grid itself is built in the open, on the lab page)
# --------------------------------------------------------------------------

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
    surface integral. The rule is the trapezoidal one, second order in the
    spacing: on the fields in this lab the flux error falls from 0.17% at
    n = 21 to 0.018% at n = 61.

    Raises if any sample is NaN. A masked sample silently integrated as zero
    returns a plausible and wrong number -- which is what happens if you put
    a face inside a region you have masked out.
    """
    F2 = np.asarray(F2, float)
    _reject_masked(F2, "This face passes through masked samples")
    wa, wb = _trapezoid_weights(F2.shape[0]), _trapezoid_weights(F2.shape[1])
    return float(np.sum(F2 * wa[:, None] * wb[None, :]) * da * db)


def volume_integral(F3: np.ndarray, dx: float, dy: float, dz: float) -> float:
    """Integrate a 3-D array of samples over the box it spans.

    Trapezoidal, second order, and it raises on masked samples for the same
    reason ``area_integral`` does.
    """
    F3 = np.asarray(F3, float)
    _reject_masked(F3, "This box contains masked samples")
    wx, wy, wz = (_trapezoid_weights(m) for m in F3.shape)
    w = wx[:, None, None] * wy[None, :, None] * wz[None, None, :]
    return float(np.sum(F3 * w) * dx * dy * dz)


def _reject_masked(F, what):
    n = int(np.count_nonzero(~np.isfinite(F)))
    if n:
        raise ValueError(
            f"{what} ({n} of {F.size} are NaN or infinite). Integrating them "
            f"as zero would return a plausible but wrong number. Move the "
            f"surface outside the masked region, or unmask the field.")


# --------------------------------------------------------------------------
# 3-D views (plotly)
# --------------------------------------------------------------------------

# Directional shading. Without it plotly lights an isosurface almost flatly
# and a nest of transparent spheres reads as a set of flat rings; the
# specular highlight and limb darkening are what make it look like a ball.
_LIGHTING = dict(ambient=0.35, diffuse=0.9, specular=0.5, roughness=0.4, fresnel=0.2)
_LIGHTPOSITION = dict(x=100, y=200, z=200)


def show_isosurfaces(X, Y, Z, F, levels, *, title="", label="", opacity=0.3,
                     colorscale="Viridis", reversescale=False, show_caps=False,
                     size=620, step=2, opacity_slider=True, slice_z=None):
    """Draw one or more isosurfaces (level sets) of a scalar field F.

    An isosurface is the set of points where F takes one fixed value -- the
    3-D analogue of a contour line. Pass an **evenly spaced** list of levels
    and look at the nesting; anything else is refused, because plotly draws
    evenly spaced surfaces between the extremes and would quietly move them.

    Parameters that matter for seeing the shape
    -------------------------------------------
    opacity_slider : bool
        Adds a slider under the figure. Drag it up towards 1 and the outermost
        surface becomes a solid, shaded ball; drag it down towards 0.1 and it
        turns to glass so the inner surfaces show through. Sweeping it is the
        quickest way to convince yourself these are shells and not discs.
    label : str
        Colorbar title. Give it the physical quantity and its unit.
        **Plotly does not render LaTeX here.** Colorbar titles accept plain
        text plus a small HTML subset (``<sub>``, ``<sup>``, ``<b>``), so
        write ``"|\u2207r|  [-]"`` and ``"[m<sup>-2</sup>]"`` with Unicode
        symbols -- a ``$...$`` label silently comes out as garbled glyphs.
        The matplotlib helpers below are the opposite: mathtext works there.
    reversescale : bool
        Flip the colorscale. Needed for a signed field on ``"RdBu"``: plotly
        runs that scale dark *red* at the low end and dark *blue* at the high
        end, the opposite of matplotlib's ``"RdBu_r"`` used by the 2-D
        helpers below. Without this flag a positive lobe drawn in 3-D comes
        out blue while the same lobe in the slice beside it is red.
    slice_z : float or None
        If given, also draw a filled cut plane at that value of z, exposing
        the interior. A strong depth cue, at the cost of hiding part of the
        nesting.
    """
    levels = np.sort(np.atleast_1d(np.asarray(levels, dtype=float)))
    # plotly draws surface_count EVENLY SPACED surfaces between isomin and
    # isomax; it never sees the individual values. Unevenly spaced levels
    # would therefore be silently redrawn at the wrong values, so refuse them
    # rather than return a picture that lies.
    if levels.size > 2:
        gaps = np.diff(levels)
        if not np.allclose(gaps, gaps[0], rtol=1e-6):
            drawn = np.linspace(levels[0], levels[-1], levels.size)
            raise ValueError(
                f"levels must be evenly spaced: plotly would draw "
                f"{np.round(drawn, 4).tolist()} instead of "
                f"{np.round(levels, 4).tolist()}. Use an evenly spaced set, "
                f"or call this once per level.")
    # Subsample before handing the volume to plotly. A full 61^3 grid embeds
    # ~12 MB of JSON per figure; every other point looks identical on screen.
    sl = (slice(None, None, step),) * 3
    X, Y, Z, F = X[sl], Y[sl], Z[sl], np.asarray(F)[sl]
    trace = go.Isosurface(
        x=X.ravel(), y=Y.ravel(), z=Z.ravel(), value=np.asarray(F).ravel(),
        isomin=float(levels.min()), isomax=float(levels.max()),
        surface_count=int(levels.size), opacity=opacity,
        colorscale=colorscale, reversescale=reversescale, showscale=True,
        colorbar=dict(title=label, len=0.7),
        lighting=_LIGHTING, lightposition=_LIGHTPOSITION,
        caps=dict(x_show=show_caps, y_show=show_caps, z_show=show_caps),
    )
    if slice_z is not None:
        trace.slices = dict(z=dict(show=True, locations=[float(slice_z)]))
    fig = go.Figure(trace)
    _style_3d(fig, title, size, bottom_margin=55 if opacity_slider else 0)
    if opacity_slider:
        _add_opacity_slider(fig, opacity)
    return _display(fig)


def _add_opacity_slider(fig, current):
    """A client-side opacity control: no kernel needed once the figure exists."""
    values = [round(0.1 * i, 1) for i in range(1, 11)]
    active = int(np.argmin([abs(v - current) for v in values]))
    fig.update_layout(sliders=[dict(
        active=active,
        currentvalue=dict(prefix="opacity: ", font=dict(size=13)),
        pad=dict(t=8, b=8), len=0.7, x=0.15, y=0,
        steps=[dict(method="restyle", args=[{"opacity": v}], label=f"{v:.1f}")
               for v in values],
    )])


def show_cones(X, Y, Z, Ax, Ay, Az, *, step=8, title="", label="", unit="",
               size=620,
               normalise=False, length=None, head=0.35, colorscale="Viridis",
               slider=True, width=4, log_colour=None):
    """Draw a 3-D vector field as arrows: a shaft with a barbed head.

    Every arrow is built from line segments -- a shaft, plus four barbs swept
    back from the tip. plotly's ``go.Cone`` is not used: a cone takes both its
    size and its colour from the norm of the vector it is given, so size and
    colour cannot be set independently, and a field whose magnitudes are all
    close to 1 comes out with heads larger than the box.

    Only every ``step``-th sample in each direction is drawn; an arrow at every
    grid point is an unreadable haystack.

    Parameters
    ----------
    label, unit : str
        The plotted quantity and its unit, kept apart, e.g.
        ``label="|<b>E</b>|", unit="V/m"``. A linear colorbar is then titled
        ``|<b>E</b>|  [V/m]``; a log one ``log<sub>10</sub>(|<b>E</b>| /
        (V/m))``, because the logarithm of a dimensional quantity does not
        carry that quantity's unit. Plotly renders no LaTeX here -- see the
        note in ``show_isosurfaces``.
    normalise : bool
        Draw every arrow the same length, showing direction only. Use it for
        fields whose magnitude spans orders of magnitude, where true-to-scale
        arrows leave a few giants and a lot of invisible dust. The magnitude is
        not lost -- it is still in the colour.
    length : float or None
        Length of the longest arrow, in metres. Defaults to 0.85 of the
        spacing between drawn arrows, so a full-length arrow almost touches
        its neighbour.
    head : float
        Fraction of an arrow taken up by its head.
    slider : bool
        Add a size slider under the figure, scaling whole arrows (head
        included) between 0.5x and 2x.
    log_colour : bool or None
        Colour by log10|A| rather than |A|. ``None`` decides automatically and
        switches over once the magnitude spans more than a factor of 50: on a
        linear scale a $1/r^2$ field puts all but a handful of arrows into the
        bottom percent of the colour range, where they are indistinguishable.
    """
    sl = (slice(None, None, step),) * 3
    x, y, z = X[sl].ravel(), Y[sl].ravel(), Z[sl].ravel()
    u = np.asarray(Ax)[sl].ravel()
    v = np.asarray(Ay)[sl].ravel()
    w = np.asarray(Az)[sl].ravel()

    finite = np.isfinite(u) & np.isfinite(v) & np.isfinite(w)
    x, y, z, u, v, w = (a[finite] for a in (x, y, z, u, v, w))

    mag = np.sqrt(u**2 + v**2 + w**2)
    safe = np.maximum(mag, 1e-30)
    ux, uy, uz = u / safe, v / safe, w / safe          # unit direction

    spacing = float(abs(X[step, 0, 0] - X[0, 0, 0])) if X.shape[0] > step else 1.0
    base = 0.85 * spacing if length is None else float(length)
    rel = np.ones_like(mag) if normalise else mag / max(float(mag.max()), 1e-30)

    positive = mag[mag > 0]
    if log_colour is None:
        log_colour = (positive.size > 0
                      and float(positive.max()) > 50.0 * float(positive.min()))
    name = label or "|A|"
    if log_colour:
        cval = np.log10(np.maximum(mag, float(positive.min())))
        # log10 of a dimensional quantity is dimensionless: the unit belongs
        # inside the logarithm, as a divisor, never appended in brackets.
        clabel = (f"log<sub>10</sub>({name} / {unit})" if unit
                  else f"log<sub>10</sub> {name}")
    else:
        cval = mag
        clabel = f"{name}  [{unit}]" if unit else name

    px, py, pz = _arrow_lines(x, y, z, ux, uy, uz, rel * base, head)
    fig = go.Figure(go.Scatter3d(
        x=px, y=py, z=pz, mode="lines", hoverinfo="skip", showlegend=False,
        line=dict(color=np.tile(np.repeat(cval, 3), _SEGMENTS_PER_ARROW),
                  colorscale=colorscale, width=width,
                  cmin=float(cval.min()), cmax=float(cval.max()),
                  showscale=True, colorbar=dict(title=clabel, len=0.7)),
    ))
    _style_3d(fig, title, size, bottom_margin=75 if slider else 0)
    # Pin the box to the sampled volume; without this the arrows themselves
    # drive the autorange and the domain silently grows.
    fig.update_scenes(
        xaxis=dict(range=[float(X.min()), float(X.max())], title="x [m]"),
        yaxis=dict(range=[float(Y.min()), float(Y.max())], title="y [m]"),
        zaxis=dict(range=[float(Z.min()), float(Z.max())], title="z [m]"),
    )
    if slider:
        _add_arrow_slider(fig, x, y, z, ux, uy, uz, rel, base, head)
    return _display(fig)


_SEGMENTS_PER_ARROW = 5          # one shaft, four barbs


def _arrow_lines(x, y, z, ux, uy, uz, lengths, head):
    """One polyline per segment, all arrows in one flat pair of arrays.

    Segments are separated by NaN, which plotly renders as a break. The four
    barbs are swept back from the tip in two mutually perpendicular planes, so
    the head reads as a head from any viewing angle.
    """
    n = x.size
    tx, ty, tz = x + ux * lengths, y + uy * lengths, z + uz * lengths

    d = np.stack([ux, uy, uz], axis=1)
    # A reference direction not parallel to d, so the cross product is stable.
    ref = np.where(np.abs(uz)[:, None] < 0.9,
                   np.array([0.0, 0.0, 1.0]), np.array([1.0, 0.0, 0.0]))
    p = np.cross(d, ref)
    p /= np.maximum(np.linalg.norm(p, axis=1, keepdims=True), 1e-30)
    q = np.cross(d, p)

    barb = lengths * head
    spread = 0.45
    xs, ys, zs = [], [], []

    def add(x0, y0, z0, x1, y1, z1):
        for a, b, out in ((x0, x1, xs), (y0, y1, ys), (z0, z1, zs)):
            seg = np.empty(3 * n)
            seg[0::3], seg[1::3], seg[2::3] = a, b, np.nan
            out.append(seg)

    add(x, y, z, tx, ty, tz)                                  # the shaft
    for side in (p, -p, q, -q):                               # the four barbs
        add(tx, ty, tz,
            tx - ux * barb + side[:, 0] * barb * spread,
            ty - uy * barb + side[:, 1] * barb * spread,
            tz - uz * barb + side[:, 2] * barb * spread)
    return (np.concatenate(xs).astype(np.float32),
            np.concatenate(ys).astype(np.float32),
            np.concatenate(zs).astype(np.float32))


def _add_arrow_slider(fig, x, y, z, ux, uy, uz, rel, base, head):
    """One client-side control scaling whole arrows, head included."""
    scales = [0.5, 0.75, 1.0, 1.5, 2.0]
    steps = []
    for sc in scales:
        px, py, pz = _arrow_lines(x, y, z, ux, uy, uz, rel * base * sc, head)
        steps.append(dict(method="restyle", label=f"{sc:g}x",
                          args=[{"x": [px], "y": [py], "z": [pz]}, [0]]))
    fig.update_layout(sliders=[dict(
        active=scales.index(1.0), steps=steps, len=0.7, x=0.15, y=0,
        pad=dict(t=8, b=8),
        currentvalue=dict(prefix="arrow size: ", font=dict(size=13)),
    )])


def _display(fig):
    """Show the figure and return nothing.

    Jupyter renders only the value of a cell's LAST expression, so a plotting
    call followed by a self-check would otherwise draw nothing at all. Showing
    it here makes the call work wherever it sits; returning None keeps it from
    being drawn a second time when it does happen to come last.
    """
    fig.show()
    return None


def _style_3d(fig, title, size, bottom_margin=0):
    fig.update_layout(
        title=title, width=size, height=size,
        margin=dict(l=0, r=0, t=40 if title else 0, b=bottom_margin),
        scene=dict(
            xaxis_title="x [m]", yaxis_title="y [m]", zaxis_title="z [m]",
            aspectmode="cube",          # equal aspect: never distort a field
            camera=dict(eye=dict(x=1.6, y=1.6, z=1.1)),
        ),
    )


# --------------------------------------------------------------------------
# 2-D views of a coordinate plane (matplotlib)
# --------------------------------------------------------------------------

def _plane_slice(X, Y, Z, F, plane):
    """Cut a 3-D field on a coordinate plane through the origin.

    ``plane="z"`` gives the z = 0 plane in (x, y); ``plane="y"`` gives the
    y = 0 plane in (x, z) -- the vertical cross-section a geophysical survey
    is usually drawn on. Returns the two 1-D axes, the 2-D field, and the two
    axis labels.
    """
    F = None if F is None else np.asarray(F)
    if plane == "z":
        k = z0_index(Z)
        return (X[:, 0, k], Y[0, :, k], None if F is None else F[:, :, k],
                "$x$ [m]", "$y$ [m]")
    if plane == "y":
        j = int(np.argmin(np.abs(Y[0, :, 0])))
        return (X[:, j, 0], Z[0, j, :], None if F is None else F[:, j, :],
                "$x$ [m]", "$z$ [m]")
    raise ValueError(f"plane must be 'z' or 'y', not {plane!r}")

def show_scalar_slice(X, Y, Z, F, *, title="", label="", cmap=None,
                      levels=25, symmetric=False, percentile=99, ax=None,
                      colorbar=True, vmin=None, vmax=None, plane="z"):
    """Filled contours of a scalar field on a coordinate plane.

    ``colorbar`` is drawn whether or not the axes was supplied by the caller;
    a panel in a side-by-side comparison needs its scale just as much as a
    standalone figure does. ``show_field_slice`` passes ``colorbar=False``
    because it adds its own.

    Pass ``vmin``/``vmax`` to pin the colour limits. Without them the limits
    come from percentiles of *this* panel, so two panels of a comparison end
    up on different scales and the extremes are clipped -- give both panels
    the same explicit pair whenever the point is that they match.

    ``cmap`` defaults to a diverging map when ``symmetric=True`` and a
    sequential one otherwise, so a one-signed field never gets a colour scale
    implying a meaningful zero crossing.

    ``plane="z"`` cuts z = 0, ``plane="y"`` cuts y = 0 for a vertical section.
    """
    a1, b1, f2, alab, blab = _plane_slice(X, Y, Z, F, plane)
    x2, y2 = np.meshgrid(a1, b1, indexing="ij")

    if cmap is None:
        cmap = "RdBu_r" if symmetric else "viridis"
    if vmax is None:
        vmax = np.nanpercentile(np.abs(f2) if symmetric else f2, percentile)
    if vmin is None:
        vmin = -vmax if symmetric else np.nanpercentile(f2, 100 - percentile)
    hi, lo = float(vmax), float(vmin)

    # A contour boundary usually falls exactly on 0.0, so a field that is zero
    # only to round-off gets sorted into the first warm and the first cool band
    # and renders as structure that is not there. The shear flow of Lab 2's
    # Task 3 is the case that matters: div = +-5e-15, drawn as faint red lobes,
    # which is precisely the "it looks like a source" reading the task exists to
    # refute. Anything this far below the plotted range is noise, not signal.
    span = max(abs(hi), abs(lo))
    if span > 0.0:
        f2 = np.where(np.abs(f2) < 1e-9 * span, 0.0, f2)

    lv = np.linspace(lo, hi, levels)

    created = ax is None
    if created:
        _, ax = plt.subplots(figsize=(5.4, 4.5))
    cf = ax.contourf(x2, y2, np.clip(f2, lo, hi), levels=lv, cmap=cmap, extend="both")
    ax.set_aspect("equal")                 # course rule: never distort a field plot
    ax.set_xlabel(alab)
    ax.set_ylabel(blab)
    ax.set_title(title)
    if colorbar:
        ax.figure.colorbar(cf, ax=ax, label=label)
    return ax, cf


def show_field_slice(X, Y, Z, Ax, Ay, *, background=None, title="", label="",
                     cmap="RdBu_r", density=1.3, symmetric=True, ax=None,
                     percentile=98, colorbar=True, vmin=None, vmax=None,
                     plane="z"):
    """Streamlines of a vector field on a coordinate plane, over an optional
    scalar background (typically the potential that generated it).

    ``plane="z"`` cuts z = 0 and expects the (x, y) components; ``plane="y"``
    cuts y = 0 and expects the (x, z) components -- pass ``Ax, Az`` there.

    Returns ``(ax, cf)``. ``cf`` is the filled-contour mappable, or ``None``
    if no background was given; pass ``colorbar=False`` on every panel of a
    multi-panel figure and hand ``cf`` to ``fig.colorbar(cf, ax=axes, ...)``
    to draw a single bar spanning the lot.
    """
    created = ax is None
    if created:
        _, ax = plt.subplots(figsize=(5.8, 4.8))

    cf = None
    if background is not None:
        _, cf = show_scalar_slice(X, Y, Z, background, cmap=cmap, symmetric=symmetric,
                                  percentile=percentile, ax=ax, colorbar=False,
                                  vmin=vmin, vmax=vmax, plane=plane)

    # streamplot needs 1-D increasing axes and arrays shaped (nb, na); our
    # indexing='ij' arrays are (na, nb), hence the transposes.
    x1, y1, u2, alab, blab = _plane_slice(X, Y, Z, Ax, plane)
    _, _, v2, _, _ = _plane_slice(X, Y, Z, Ay, plane)
    u = np.nan_to_num(u2).T
    v = np.nan_to_num(v2).T
    ax.streamplot(x1, y1, u, v, color="k", linewidth=0.7,
                  density=density, arrowsize=0.9)

    ax.set_aspect("equal")
    ax.set_xlim(x1.min(), x1.max())
    ax.set_ylim(y1.min(), y1.max())
    ax.set_xlabel(alab)
    ax.set_ylabel(blab)
    ax.set_title(title)
    if colorbar and cf is not None:
        ax.figure.colorbar(cf, ax=ax, label=label)
    return ax, cf


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


def check_abs(label: str, got, atol, where=None, hint: str = "") -> None:
    """Compare an array against **zero**, on an absolute scale.

    ``check_close`` divides by the expected value, so it cannot be pointed at
    a quantity whose answer is exactly zero -- a solenoidal field, say. Give
    this one a tolerance in the field's own units instead. ``atol`` is usually
    a small fraction of the scale the field could have had: for a divergence
    built from ``A ~ r`` on a grid of spacing ``dx``, anything below about
    ``1e-9`` is round-off.
    """
    got = np.asarray(got, float)
    m = np.isfinite(got)
    if where is not None:
        m = m & where
    if not m.any():
        raise AssertionError(f"{label} -- nothing left to compare")
    worst = float(np.max(np.abs(got[m])))
    check(f"{label}: worst |value| {worst:.2e}", worst < atol,
          hint or f"worst deviation from zero, {worst:.2e}, exceeds {atol:.1e}")


def check_scalar(label: str, got: float, want: float, rtol: float = 0.01,
                 unit: str = "") -> None:
    """Compare two single numbers and report the relative discrepancy."""
    got, want = float(got), float(want)
    rel = abs(got - want) / max(abs(want), 1e-30)
    check(f"{label}: {got:.4g}{unit} vs {want:.4g}{unit} ({rel:.2%} apart)",
          rel < rtol,
          f"these should agree to better than {rtol:.0%}. Check the sign of "
          f"each face, and that every face uses its own outward normal.")
