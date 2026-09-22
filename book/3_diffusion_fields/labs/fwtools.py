"""Plotting and self-check helpers for the ECTB2140 *Fields and Waves* labs,
diffusive-fields edition.

You are **not** expected to read or edit this file during a lab session. It
exists so that your time goes on the physics -- series coefficients, decay
rates, Gaussian kernels -- rather than on plotting boilerplate.

The self-check functions have the same names and behaviour as in the Lab 1
and Lab 2 module. Everything here is one-dimensional in space: fields are
arrays of shape (nt, nx), one row per time.

Requires: numpy, matplotlib, plotly.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
import plotly.graph_objects as go

__all__ = [
    "show_profiles", "show_spacetime", "show_spacetime_slider", "show_records",
    "check", "check_close", "check_abs", "check_scalar",
]

# --------------------------------------------------------------------------
# Figures
# --------------------------------------------------------------------------

def _fmt(v, fmt):
    return fmt.format(v) if isinstance(fmt, str) else fmt(v)


def show_profiles(x, frames, values, *, value_name="t", value_fmt="{:.3g}",
                  unit="", reference=None, reference_name="initial condition",
                  xlabel="x [m]", ylabel="", title="", ylim=None, height=430,
                  ms_per_frame=90, colors=("#00A6D6", "#EC6842", "#7B61FF")):
    """Profiles over time, with a play button and a draggable progress bar.

    ``frames`` is either one array of shape (len(values), nx), or a dict
    ``{name: array}`` to draw several curves that evolve together. Press play
    to run from the start, or drag the bar to any instant. Both run in the
    browser; nothing here needs the kernel once the figure exists.
    """
    if not isinstance(frames, dict):
        frames = {"profile": frames}
    frames = {k: np.asarray(v, float) for k, v in frames.items()}
    x = np.asarray(x, float)
    allv = np.concatenate([v.ravel() for v in frames.values()])
    lo, hi = (np.nanmin(allv), np.nanmax(allv)) if ylim is None else ylim
    pad = 0.06 * (hi - lo if hi > lo else 1.0)

    fig = go.Figure()
    if reference is not None:
        fig.add_trace(go.Scatter(x=x, y=reference, mode="lines", name=reference_name,
                                 line=dict(color="#8a9199", dash="dash", width=1.5)))
    live = []
    for k, (name, arr) in enumerate(frames.items()):
        fig.add_trace(go.Scatter(x=x, y=arr[0], mode="lines", name=name,
                                 line=dict(color=colors[k % len(colors)],
                                           width=2.5 if k == 0 else 2.0)))
        live.append(len(fig.data) - 1)

    n_steps = len(values)
    fig.frames = [go.Frame(name=str(k),
                           data=[go.Scatter(y=arr[k]) for arr in frames.values()],
                           traces=live)
                  for k in range(n_steps)]
    still = dict(mode="immediate", frame=dict(duration=0, redraw=False),
                 transition=dict(duration=0))
    steps = [dict(method="animate", label=_fmt(v, value_fmt), args=[[str(k)], still])
             for k, v in enumerate(values)]

    fig.update_layout(
        title=title, height=height, margin=dict(l=60, r=20, t=50, b=30),
        xaxis_title=xlabel, yaxis_title=ylabel,
        yaxis_range=[lo - pad, hi + pad], legend=dict(x=0.99, xanchor="right", y=0.99),
        sliders=[dict(active=0, steps=steps, len=0.82, x=0.18, y=0, pad=dict(t=50, b=8),
                      currentvalue=dict(prefix=f"{value_name} = ", suffix=unit,
                                        font=dict(size=13)))],
        updatemenus=[dict(type="buttons", direction="left", showactive=False,
                          x=0.0, y=0, xanchor="left", yanchor="top", pad=dict(t=55, b=8),
                          buttons=[
                              dict(label="▶ play", method="animate",
                                   args=[None, dict(mode="immediate", fromcurrent=False,
                                                    frame=dict(duration=ms_per_frame, redraw=False),
                                                    transition=dict(duration=0))]),
                              dict(label="❚❚", method="animate", args=[[None], still])])])
    fig.show()


def show_spacetime(x, t, T, *, t_label="t [s]", x_label="x [m]", c_label="T [K]",
                   title="", signed=None, log_t=True, marks=None, curve=None,
                   curve_label="prediction", deeper_down=False):
    """Colour map of T(x, t): time along the horizontal axis, position vertical.

    A signed field gets a diverging colour map centred on zero; a positive one
    gets a sequential map. ``marks`` is an optional list of (t, x) points to
    overlay, e.g. predicted peak times.
    """
    T = np.asarray(T, float)
    if signed is None:
        signed = np.nanmin(T) < 0 < np.nanmax(T)
    fig, ax = plt.subplots(figsize=(8.2, 3.6))
    if signed:
        vmax = np.nanmax(np.abs(T))
        im = ax.pcolormesh(t, x, T.T, cmap="RdBu_r", shading="auto",
                           norm=TwoSlopeNorm(0.0, -vmax, vmax))
    else:
        im = ax.pcolormesh(t, x, T.T, cmap="inferno", shading="auto", vmin=0)
    if curve is not None:
        ax.plot(curve[0], curve[1], "--", color="#00A6D6", lw=2, label=curve_label)
        ax.legend(loc="upper left", fontsize=8)
    if marks is not None:
        mt, mx = zip(*marks)
        ax.plot(mt, mx, "o", mfc="none", mec="#00A6D6", mew=1.5, ms=7, label="predicted peak")
        ax.legend(loc="upper left", fontsize=8)
    if log_t:
        ax.set_xscale("log")
    ax.set_xlim(np.min(t), np.max(t))    # an overlaid curve must not stretch the axis
    if deeper_down:                      # depth axes read downward
        ax.invert_yaxis()
    ax.set_xlabel(t_label); ax.set_ylabel(x_label); ax.set_title(title)
    fig.colorbar(im, ax=ax, label=c_label, pad=0.02)
    fig.tight_layout()
    plt.show()


def show_spacetime_slider(x, t, maps, values, *, value_name="a", value_fmt="{:.3g}",
                          unit="", t_label="t [s]", x_label="x [m]", c_label="T [K]",
                          title="", marks=None, height=430):
    """One space-time map per slider position, for a parameter of the problem.

    ``maps`` has shape (len(values), len(t), len(x)). ``marks[k]`` optionally
    draws a vertical line at that time on map k, e.g. a predicted merge time.
    The slider updates the map and the line together, client-side.
    """
    maps = np.asarray(maps, float)
    x, t = np.asarray(x, float), np.asarray(t, float)
    zmin, zmax = float(np.nanmin(maps)), float(np.nanmax(maps))

    def line(k):
        if marks is None or not np.isfinite(marks[k]) or marks[k] <= t[0]:
            return []
        return [dict(type="line", x0=marks[k], x1=marks[k], y0=x[0], y1=x[-1],
                     xref="x", yref="y", line=dict(color="#00A6D6", width=2, dash="dash"))]

    fig = go.Figure(go.Heatmap(z=maps[0].T, x=t, y=x, colorscale="Inferno",
                               zmin=zmin, zmax=zmax, colorbar=dict(title=c_label)))
    steps = [dict(method="update", label=_fmt(v, value_fmt),
                  args=[{"z": [m.T]}, {"shapes": line(k)}])
             for k, (v, m) in enumerate(zip(values, maps))]
    fig.update_layout(
        title=title, height=height, margin=dict(l=60, r=20, t=50, b=30),
        xaxis=dict(title=t_label, type="log"), yaxis_title=x_label,
        shapes=line(0),
        sliders=[dict(active=0, steps=steps, len=0.82, x=0.12, y=0, pad=dict(t=50, b=8),
                      currentvalue=dict(prefix=f"{value_name} = ", suffix=unit,
                                        font=dict(size=13)))])
    fig.show()


def show_records(t, records, *, t_label="t [s]", y_label="T [K]", title="",
                 peaks=None, log_t=True):
    """Time series at fixed positions, as a thermometer or a receiver records them.

    ``records`` maps a label to an array over ``t``. ``peaks`` optionally maps
    the same labels to a predicted (t_peak, value_peak), drawn as an open circle.
    """
    fig, ax = plt.subplots(figsize=(8.2, 3.4))
    for k, (lab, y) in enumerate(records.items()):
        ax.plot(t, y, color=f"C{k}", lw=2, label=lab)
        if peaks and lab in peaks:
            ax.plot(*peaks[lab], "o", mfc="none", mec=f"C{k}", mew=1.5, ms=9)
    if log_t:
        ax.set_xscale("log")
    ax.set_xlabel(t_label); ax.set_ylabel(y_label); ax.set_title(title)
    ax.grid(alpha=0.3); ax.legend(fontsize=8)
    fig.tight_layout()
    plt.show()


# --------------------------------------------------------------------------
# Self-checks (same behaviour as the Lab 1 and Lab 2 module)
# --------------------------------------------------------------------------

def check(label: str, ok: bool, hint: str = "") -> None:
    """Report a pass, or raise with a hint about what to look at."""
    if ok:
        print(f"  [ok] {label}")
    else:
        raise AssertionError(f"{label} -- {hint}" if hint else label)


def check_close(label: str, got, want, rtol=0.05, where=None, hint: str = "") -> None:
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
          hint or f"worst relative error {worst:.2%} exceeds {rtol:.0%}")


def check_abs(label: str, got, atol, where=None, hint: str = "") -> None:
    """Compare an array against zero on an absolute scale, in the field's own units."""
    got = np.asarray(got, float)
    m = np.isfinite(got)
    if where is not None:
        m = m & where
    if not m.any():
        raise AssertionError(f"{label} -- nothing left to compare")
    worst = float(np.max(np.abs(got[m])))
    check(f"{label}: worst |value| {worst:.2e}", worst < atol,
          hint or f"worst deviation {worst:.2e} exceeds {atol:.1e}")


def check_scalar(label: str, got: float, want: float, rtol: float = 0.01,
                 unit: str = "", hint: str = "") -> None:
    """Compare two single numbers and report the relative discrepancy."""
    got, want = float(got), float(want)
    rel = abs(got - want) / max(abs(want), 1e-30)
    check(f"{label}: {got:.4g}{unit} vs {want:.4g}{unit} ({rel:.2%} apart)",
          rel < rtol, hint or f"these should agree to better than {rtol:.0%}")
