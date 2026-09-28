---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
mystnb:
  # Workbook page: the task cells contain `___` blanks by design, so it must
  # not be executed at build time. Readers run it themselves with Live Code.
  execution_mode: 'off'
---

# Lab 5: Diffusive Fields

:::{admonition} Computer lab
:class: note

A practical companion to the lecture on [the heat equation in one dimension](../heat_equation_1d.md). Each task states a physical question, gives the steps, and ends with a self-check you can run.

Everything you write here is plain NumPy. The module `fwtools` only draws and checks: `fw.show_profiles` (a profile per instant, with a play button), `fw.show_spacetime` (a colour map over position and time), `fw.show_records` (time series at fixed positions) and the `fw.check...` functions. Every slider runs in the browser.
:::

## Learning objectives

- **Decaying modes.** Build an initial temperature from a Fourier series and explain why mode $n$ decays at $\kappa(n\pi/L)^2$, so fine structure goes first.
- **Boundaries.** Ends held at a fixed temperature let heat leave; insulated ends conserve it and drive the bar to its mean.
- **Superposition.** Evolve any initial temperature with the Green's function, and turn the $t\propto x^2$ it implies into a measurement: of $\kappa$ in a bar, of depth in the Earth.

---

## Part 0 — Setup

Run this once. It contains no physics: it fetches two packages the browser lacks and locates `fwtools`.

```{code-cell} ipython3
import sys, pathlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0, epsilon_0

# --- Live Code housekeeping, not part of the physics -----------------------
try:
    import plotly.io as pio
except ModuleNotFoundError:
    print("Fetching plotly. A few seconds, and only the first time...")
    import micropip
    await micropip.install("plotly")
    import plotly.io as pio

try:
    import nbformat                                    # noqa: F401
except ModuleNotFoundError:
    import micropip, types
    try:
        await micropip.install("nbformat")
    except Exception:
        _nb = types.ModuleType("nbformat")
        _nb.__version__ = "5.10.4"
        sys.modules["nbformat"] = _nb

for _p in (".", "book/3_diffusion_fields/labs"):
    if (pathlib.Path(_p) / "fwtools.py").exists():
        sys.path.insert(0, _p)
        break
try:
    import fwtools as fw
except ModuleNotFoundError:
    from pyodide.http import pyfetch
    _r = await pyfetch("fwtools.py")
    pathlib.Path("fwtools.py").write_bytes(await _r.bytes())
    import fwtools as fw

pio.renderers.default = "plotly_mimetype+notebook"
# ---------------------------------------------------------------------------
print("ready")
```

---

## Part 1 — A bar of finite length

A copper bar of length $L = 0.5$ m has thermal diffusivity $\kappa = 1.1\times10^{-4}$ m²/s. Its temperature $T$ is measured from a reference value, so it can be negative. Without sources, the temperature obeys

$$ \partial_t T = \kappa\,\partial_x^2 T . $$

The only time scale the bar has is $L^2/\kappa \approx 38$ min, so the natural clock is the Fourier number $\mathrm{Fo} = \kappa t/L^2$. The two ways of closing the ends lead to different series and to a different final state.

```{figure} figures/bar_boundary_conditions.svg
:name: fig-lab5-bcs
:width: 80%

The two bars of this part. In Tasks 1 and 2 the ends are clamped to reservoirs at the reference temperature. In Task 3 they are insulated.
```

### Task 1 — build the initial temperature from sines

With both ends held at $T=0$, separation of variables gives

$$ T(x,t) = \sum_{n=1}^{\infty} C_n \sin\!\left(\frac{n\pi x}{L}\right) \exp\!\left[-\kappa\left(\frac{n\pi}{L}\right)^2 t\right], \qquad C_n = \frac{2}{L}\int_0^L h(x)\sin\!\left(\frac{n\pi x}{L}\right)\mathrm{d}x , $$

where the coefficient formula follows from the orthogonality of the sines. At $t=0$ the series must rebuild the initial temperature $h(x)$. Here $h$ is $0$, $-1$, $1$, $0$ K on the four quarters of the bar.

1. Compute all $C_n$ at once by projecting $h$ onto every row of `S`.
2. Write the partial sum of the first `m` modes.
3. Drag the slider. **Before you do**, predict which coefficients vanish, using the symmetry of $h$ about $x=L/2$.

```{code-cell} ipython3
L, kappa = 0.5, 1.1e-4             # copper bar: length [m], thermal diffusivity [m^2/s]
ncell, N = 1200, 400               # grid cells, number of modes kept
dx = L / ncell
x = (np.arange(ncell) + 0.5) * dx  # cell centres, so an integral is a plain sum times dx
n = np.arange(1, N + 1)
S = np.sin(np.outer(n, np.pi * x / L))     # row n-1 is sin(n pi x / L), shape (N, ncell)
h = np.where(x < L/4, 0.0, np.where(x < L/2, -1.0,
             np.where(x < 3*L/4, 1.0, 0.0)))               # initial temperature [K]
print(f"L^2/kappa = {L**2/kappa:.0f} s;  slowest possible mode, tau_1 = L^2/(kappa pi^2)"
      f" = {L**2/(kappa*np.pi**2):.0f} s")

# Task 1 -- two blanks. An integral over the bar is np.sum(...) * dx; summing along
# axis=1 of an (N, ncell) array does all N integrals at once.
C = ___                                    # all C_n, shape (N,)
partial = lambda m: ___                    # sum of the first m modes at t = 0, shape (ncell,)

# --- given: the partial sums, one per slider position ---
Ns = np.array([1, 2, 4, 6, 10, 20, 40, 100, 400])
fw.show_profiles(x, np.array([partial(m) for m in Ns]), Ns, value_name="modes kept",
                 value_fmt="{:d}", reference=h, reference_name="h(x)",
                 ylabel="T [K]", title="Partial sums of the sine series")
print("C_1 .. C_6 =", np.round(C[:6], 4))

# --- self-check (leave this alone) ---
_C_exact = 2 * (2*np.cos(n*np.pi/2) - np.cos(n*np.pi/4) - np.cos(3*n*np.pi/4)) / (np.pi * n)
fw.check_abs("the first 40 C_n match the closed form", C[:40] - _C_exact[:40], 1e-3,
             hint="C_n = (2/L) * integral of h(x) sin(n pi x/L) dx, for every n at once")
_away = np.min(np.abs(x[:, None] - np.array([L/4, L/2, 3*L/4])), axis=1) > 0.04
fw.check_abs("400 modes rebuild h(x) more than 4 cm from a jump", partial(N) - h, 0.02, where=_away,
             hint="partial(m) should weight the first m rows of S by the first m coefficients")
```

:::{admonition} Solution — Task 1
:class: dropdown

```python
C = (2 / L) * np.sum(h * S, axis=1) * dx
partial = lambda m: C[:m] @ S[:m]
```
:::

:::{admonition} Only even modes appear, and the overshoot at a jump never shrinks
:class: important dropdown

$h$ is antisymmetric about $x=L/2$, while $\sin(n\pi x/L)$ is symmetric about that point for odd $n$ and antisymmetric for even $n$. The projection of an antisymmetric function onto a symmetric one is zero, so $C_1=C_3=C_5=\dots=0$.

Near each jump the partial sums overshoot by about 9% of the jump. At $x=L/2$ the jump is 2 K, so the peak reaches about 1.18 K, whether you keep 10 modes or 100. Adding terms squeezes the overshoot towards the jump without lowering it; at 400 modes it becomes narrower than the grid spacing, and the plotted peak reads slightly lower. This is the Gibbs phenomenon: the series converges at every point, but not uniformly near a discontinuity.
:::

### Task 2 — let it diffuse

Every mode keeps its shape and decays with its own time constant

$$ \tau_n = \frac{L^2}{\kappa\,n^2\pi^2} . $$

Mode $n$ dies $n^2$ times faster than mode 1. **Predict** which mode is the last one visible, given the coefficients of Task 1.

1. Build the decay factors for all times and all modes in one array.
2. Weight each mode by $C_n$ and by its decay, and sum the modes.

```{code-cell} ipython3
t = np.logspace(-1, np.log10(0.25 * L**2 / kappa), 90)     # 0.1 s .. 568 s, i.e. Fo = 0.25

# Task 2 -- two blanks.
D = ___                                    # exp(-kappa (n pi/L)^2 t), shape (len(t), N)
T = ___                                    # T(x, t), shape (len(t), nx)

# --- given: the space-time map, then the profiles as a movie ---
fw.show_spacetime(x, t, T, t_label="t [s]", x_label="x [m]", c_label="T [K]",
                  title="Ends held at T = 0")
fw.show_profiles(x, T[::2], t[::2], value_name="t", value_fmt="{:.3g}", unit=" s",
                 reference=h, ylabel="T [K]", title="Ends held at T = 0", ylim=(-1.2, 1.2))

# --- self-check (leave this alone) ---
fw.check("T has one row per time and one column per grid cell", np.shape(T) == (len(t), ncell))
_i1, _i2 = np.argmin(np.abs(t - 0.05*L**2/kappa)), np.argmin(np.abs(t - 0.10*L**2/kappa))
_A = np.max(np.abs(T), axis=1)
_rate = np.log(_A[_i1] / _A[_i2]) / (t[_i2] - t[_i1])
fw.check_scalar("late-time decay rate of your T equals kappa (2 pi/L)^2", _rate,
                kappa * (2*np.pi/L)**2, rtol=0.01, unit=" 1/s",
                hint="each mode needs its own exponent kappa (n pi/L)^2 t")
```

:::{admonition} Solution — Task 2
:class: dropdown

```python
D = np.exp(-kappa * (n * np.pi / L)**2 * t[:, None])
T = (C * D) @ S
```
:::

:::{admonition} Mode 2 survives, because mode 1 was never there
:class: important dropdown

The sharp corners of $h$ are made of high modes, and those vanish within seconds: after one second, modes above $n\approx 15$ have decayed by a factor of $e$. By $t\approx 60$ s only $n=2$ and a trace of $n=4$ remain, so the profile has become a single sine wave that shrinks without changing shape. Mode 1 would have decayed four times more slowly still, but $h$ contains none of it. The heat flows out through the clamped ends and between the warm and cold halves, and the bar returns to the reference temperature.

The measured decay rate is the second eigenvalue, $\kappa(2\pi/L)^2 = 0.0174$ s$^{-1}$. A long-time temperature record thus reveals the lowest mode present, and with it $\kappa/L^2$.
:::

### Task 3 — insulate the ends

With $\partial_xT = 0$ at both ends, no heat crosses them. The eigenfunctions become cosines, and $\lambda=0$ is now an eigenvalue:

$$ T(x,t) = C_0 + \sum_{n=1}^{\infty} C_n \cos\!\left(\frac{n\pi x}{L}\right)\exp\!\left[-\kappa\left(\frac{n\pi}{L}\right)^2 t\right], \qquad C_0 = \frac{1}{L}\int_0^L h\,\mathrm{d}x, \quad C_n = \frac{2}{L}\int_0^L h\cos\!\left(\frac{n\pi x}{L}\right)\mathrm{d}x . $$

The initial temperature is now $1$, $-1$, $1$ K on the three thirds of the bar. The cosine projection is given; write $C_0$, the one mode the clamped bar of Task 2 did not have. **Predict** the temperature at late times, and whether the heat content $\int_0^L T\,\mathrm{d}x$ changes.

```{code-cell} ipython3
Cc = np.cos(np.outer(n, np.pi * x / L))                    # row n-1 is cos(n pi x / L)
h_ins = np.where(x < L/3, 1.0, np.where(x < 2*L/3, -1.0, 1.0))   # initial temperature [K]

# Task 3 -- one blank: the n = 0 coefficient, the mode the clamped bar did not have.
C0 = ___                                   # the n = 0 coefficient [K]

# --- given: the rest is Task 2 with cosines in place of sines ---
Cn = (2 / L) * np.sum(h_ins * Cc, axis=1) * dx     # C_n for n = 1..N, shape (N,)
T_ins = C0 + (Cn * D) @ Cc                         # T(x, t), reusing D from Task 2

Q = np.sum(T_ins, axis=1) * dx            # heat content, per unit area and heat capacity [K m]

# --- given: the same two views as Task 2, to be compared with it ---
fw.show_spacetime(x, t, T_ins, t_label="t [s]", x_label="x [m]", c_label="T [K]",
                  title="Insulated ends")
fw.show_profiles(x, T_ins[::2], t[::2], value_name="t", value_fmt="{:.3g}", unit=" s",
                 reference=h_ins, ylabel="T [K]", title="Insulated ends", ylim=(-1.2, 1.2))
print(f"heat content: min {Q.min():.6f}, max {Q.max():.6f} K m over {t[0]:.1f} s .. {t[-1]:.0f} s")

# --- self-check (leave this alone) ---
fw.check_close("heat content stays at C0 L = 1/6 K m at every time", Q, (1/3) * L, rtol=1e-3)
_away3 = np.min(np.abs(x[:, None] - np.array([L/3, 2*L/3])), axis=1) > 0.02
fw.check_abs("at t = 0.1 s the series still equals h(x) away from the jumps",
             T_ins[0] - h_ins, 0.01, where=_away3,
             hint="compare your cosine projection with the sine projection of Task 1")
```

:::{admonition} Solution — Task 3
:class: dropdown

```python
C0 = np.sum(h_ins) * dx / L
```
:::

:::{admonition} Insulated ends conserve the heat, and the bar settles at its mean
:class: important dropdown

Every cosine with $n\ge1$ integrates to zero over the bar, so the heat content is $C_0L$ at all times, fixed by $h$ alone. The mode $n=0$ has decay rate zero, so it is all that remains: $T\to C_0 = 1/3$ K everywhere. In Task 2 every eigenvalue was positive and the temperature went to zero, because the clamped ends could absorb or supply heat. The boundary condition, not the equation, decides where the heat ends up.
:::

---

## Part 2 — An infinitely long wire

On an infinite wire the lecture notes solve the same equation twice. First in closed form, for an initial Gaussian $T(x,0) = T_0\exp(-x^2/L^2)$:

$$ T(x,t) = \frac{T_0 L}{\sqrt{4\kappa t + L^2}}\exp\!\left(-\frac{x^2}{4\kappa t + L^2}\right). $$

Then again as a cosine series, by putting the wire in a box of length $2M$ and letting $M$ grow. Task 7 takes up that second route; Parts 2 and 3 use the closed form, because it is the one you can read.

In this part and again in Task 7, $L$ is the width of the initial Gaussian and not a length of wire; the lecture notes use the one letter for both. The code keeps them apart: `L` is the bar of Part 1, `Lg` the Gaussian here, `Lw` the Gaussian of Task 7. Time enters only through $\kappa t$, which has units of m², so every result below holds for any material. The figures below use $L=3$ m, $-10<x<10$ m and $10^{-1}<\kappa t<10^{3}$ m².

### Task 4 — a spreading Gaussian, seen by thermometers

Setting $\partial_t T = 0$ gives the time at which the temperature at position $x$ peaks,

$$ \kappa t_p = \frac{2x^2 - L^2}{4}, \qquad T(x,t_p) = \frac{T_0 L}{\sqrt{2e}\,\lvert x\rvert}. $$

1. Write the solution as a function of `x` and `kt`.
2. Write $\kappa t_p$ as a function of `x`.
3. Before running, **predict** what the thermometer at $x=1$ m records.

```{code-cell} ipython3
Lg, T0 = 3.0, 1.0                          # initial width [m] (L in the notes), initial peak [K]
xg = np.linspace(-10.0, 10.0, 801)         # position along the wire [m]
kt = np.logspace(-1, 3, 400)               # kappa * t [m^2]

# Task 4 -- two blanks.
def T_gauss(x, kt):
    """Temperature of the spreading Gaussian. Works on arrays."""
    return ___

def kt_peak(x):
    """kappa * t at which the temperature at x peaks."""
    return ___

# --- given: the map, the movie, and four thermometers ---
Tg = T_gauss(xg[None, :], kt[:, None])
fw.show_spacetime(xg, kt, Tg, t_label=r"$\kappa t$ [m$^2$]", c_label="T [K]",
                  title="Gaussian on an infinite wire")
fw.show_profiles(xg, Tg[::5], kt[::5], value_name="κt", value_fmt="{:.3g}", unit=" m²",
                 reference=T_gauss(xg, 0.0), ylabel="T [K]", title="Gaussian on an infinite wire")
_sensors = [1.0, 3.0, 5.0, 8.0]
fw.show_records(kt, {f"x = {s:g} m": T_gauss(s, kt) for s in _sensors},
                peaks={f"x = {s:g} m": (kt_peak(s), T_gauss(s, kt_peak(s)))
                       for s in _sensors if kt_peak(s) > kt[0]},
                t_label=r"$\kappa t$ [m$^2$]", y_label="T [K]",
                title="Thermometer records; circles mark the predicted peaks")

# --- self-check (leave this alone) ---
_xw = np.linspace(-2000.0, 2000.0, 200001)
_heat = [np.sum(T_gauss(_xw, k)) * (_xw[1] - _xw[0]) for k in (0.1, 10.0, 1000.0)]
fw.check_close("heat content T0 L sqrt(pi) at kappa t = 0.1, 10, 1000 m^2",
               _heat, T0 * Lg * np.sqrt(np.pi), rtol=1e-3,
               hint="the prefactor must shrink exactly as fast as the width grows")
_ktf = np.logspace(-1, 3, 4001)
_rec = T_gauss(5.0, _ktf)
fw.check_scalar("your kt_peak(5 m) against the peak of your own record", kt_peak(5.0),
                _ktf[np.argmax(_rec)], rtol=0.01, unit=" m^2")
fw.check_scalar("peak temperature at 5 m", np.max(_rec), T0 * Lg / (np.sqrt(2*np.e) * 5.0),
                rtol=0.01, unit=" K")
```

:::{admonition} Solution — Task 4
:class: dropdown

```python
def T_gauss(x, kt):
    return T0 * Lg / np.sqrt(4*kt + Lg**2) * np.exp(-x**2 / (4*kt + Lg**2))

def kt_peak(x):
    return (2*x**2 - Lg**2) / 4
```
:::

:::{admonition} The heat spreads without loss, and a farther thermometer answers later and weaker
:class: important dropdown

The width grows as $\sqrt{4\kappa t+L^2}$, and the amplitude falls by exactly the same factor, so the area under the profile stays $T_0L\sqrt\pi$. With no ends, no heat is lost; it is only redistributed. At late times the temperature everywhere falls as $t^{-1/2}$.

The thermometers show the two faces of diffusion. The peak arrives at $\kappa t_p\propto x^2$: twice as far away takes four times as long. Its height falls as $1/\lvert x\rvert$. Inside $\lvert x\rvert<L/\sqrt2\approx2.1$ m, $\kappa t_p$ is negative. The record at $x=1$ m only ever falls, because that point was already past its peak at $t=0$.
:::

### Task 5 — two sources blur into one

The equation is linear, so two Gaussians centred at $x=\pm a$ evolve independently and their temperatures add. The lecture notes take $a=2L$. While the two are resolved, $T$ has a dip at $x=0$. They merge when the curvature there changes sign. With $w^2 = 4\kappa t+L^2$,

$$ \partial_x^2\left[e^{-(x-a)^2/w^2}+e^{-(x+a)^2/w^2}\right]_{x=0} = \frac{4}{w^2}\,e^{-a^2/w^2}\left(\frac{2a^2}{w^2}-1\right), $$

which vanishes at $w^2 = 2a^2$, that is at $\kappa t^\ast = (2a^2-L^2)/4$.

1. Write the pair as a superposition of `T_gauss`.
2. `kt_merge` is given, because it is `kt_peak` over again with $a$ in place of $x$. **Explain** why merging and peaking are the same event, from the two conditions that produced them, $w^2=2x^2$ and $w^2=2a^2$. The last figure sweeps the separation: watch the dashed line, your own merge time, track the instant the two ridges fuse.

```{code-cell} ipython3
# Task 5 -- one blank.
def T_pair(x, kt, a):
    """Two Gaussians of Task 4, centred at x = -a and x = +a."""
    return ___

# --- given: kappa t* after which T_pair has a single maximum, at x = 0.
# It is Task 4's peak time, with the separation in place of the position.
kt_merge = kt_peak

# --- given: the case of the lecture notes, a = 2L ---
fw.show_spacetime(xg, kt, T_pair(xg[None, :], kt[:, None], 2*Lg), t_label=r"$\kappa t$ [m$^2$]",
                  c_label="T [K]", title="Two Gaussians, a = 2L")
fw.show_profiles(xg, T_pair(xg[None, :], kt[::5, None], 2*Lg), kt[::5], value_name="κt",
                 value_fmt="{:.3g}", unit=" m²", reference=T_pair(xg, 0.0, 2*Lg),
                 ylabel="T [K]", title="Two Gaussians, a = 2L")

# --- given: the same map for a range of separations, with your kappa t* marked ---
_xs = np.linspace(-10.0, 10.0, 161)        # a coarser grid: five maps travel to the browser
_kts = np.logspace(-1, 3, 80)
_avals = np.array([0.5, 1.0, 1.5, 2.0, 3.0]) * Lg
fw.show_spacetime_slider(_xs, _kts,
                         [T_pair(_xs[None, :], _kts[:, None], av) for av in _avals], _avals,
                         value_name="a", value_fmt="{:.1f}", unit=" m",
                         t_label="κt [m²]", c_label="T [K]",
                         marks=[kt_merge(av) for av in _avals],
                         title="Separation sweep; the dashed line is your merge time")

# --- given: the merge time measured from the sign of the curvature at x = 0 ---
_seps = np.array([1.5, 2.0, 3.0]) * Lg
_ktf5 = np.logspace(-1, 3, 4001)
_eps = 0.01
_measured = np.array([_ktf5[np.argmax(T_pair(_eps, _ktf5, s) + T_pair(-_eps, _ktf5, s)
                                      - 2*T_pair(0.0, _ktf5, s) < 0)] for s in _seps])
for s, m in zip(_seps, _measured):
    print(f"a = {s:4.1f} m:  measured kappa t* = {m:6.2f} m^2,  your formula {kt_merge(s):6.2f} m^2")

# --- self-check (leave this alone) ---
_xw = np.linspace(-2000.0, 2000.0, 200001)
_pair = T_pair(_xw, 1.0, 2*Lg)
fw.check("the pair is symmetric about x = 0 and holds twice the heat of Task 4",
         np.allclose(_pair, _pair[::-1], atol=1e-12)
         and np.isclose(np.sum(_pair) * (_xw[1] - _xw[0]), 2*T0*Lg*np.sqrt(np.pi), rtol=1e-3),
         "one Gaussian at x = -a, one at x = +a, each exactly the T_gauss of Task 4")
fw.check_close("merge time: your formula against the measurement, three separations",
               kt_merge(_seps), _measured, rtol=0.02)
```

:::{admonition} Solution — Task 5
:class: dropdown

```python
def T_pair(x, kt, a):
    return T_gauss(x - a, kt) + T_gauss(x + a, kt)
```
:::

:::{admonition} After $\kappa t^\ast\propto a^2$, a record cannot tell two sources from one
:class: important dropdown

The two conditions are one condition. A thermometer at $x$ peaks when the spreading width reaches $w^2=2x^2$, and the dip at the centre fills in when $w^2=2a^2$: each source arrives at the other's centre exactly as the pair stops being two. Once $w^2>2a^2$ the profile has a single maximum, and it becomes ever harder to distinguish from one Gaussian of twice the heat. Sources that are closer together merge sooner, as $a^2$. For $a<L/\sqrt2$ they were never resolved at all. A diffusive field measured far away, or late, therefore carries little information about the fine structure of its source. This limits every survey that relies on diffusion, electromagnetic ones included.
:::

---

## Part 3 — When does the bar discover its ends?

A point of heat released at $x'$ at $t=0$ spreads on an infinite line as

$$ G(x-x',t) = \frac{1}{\sqrt{4\pi\kappa t}}\exp\!\left(-\frac{(x-x')^2}{4\kappa t}\right), $$

the Green's function of the heat equation. It is the Gaussian of Part 2 in the limit of a source
squeezed to a point, and it carries unit heat at every time. Because the equation is linear, an
arbitrary initial temperature is a continuous superposition of such points,

$$ T_{\text{free}}(x,t) = \int_0^L G(x-x',t)\,h(x')\,\mathrm{d}x' , $$

which is how the lecture notes build the electromagnetic field from its impulse response.

This solution knows nothing about the ends of the bar, while the series of Part 1 holds $T=0$ at
both of them. Early on the heat has not reached the ends, so the two must agree. **They part when
the bar discovers that it is finite**, and that gives a way to measure $\kappa$.

### Task 6 — the same heat, with and without ends

The initial temperature is now a narrow Gaussian bump of width $w=3$ cm, centred a distance $x_c$
from the near end. Build the free-space solution by superposition: `d2[i, j]` holds the squared
distance between grid points $i$ and $j$, so the kernel is a matrix and the integral is a
matrix-vector product.

The departure time is plotted against $x_c^2$, not against $x_c$. **Predict** the sign of the
intercept before you look, and say what sets its size.

```{code-cell} ipython3
w_b = 0.03                                  # width of the initial bump [m]
xs = x[::4]                                 # every fourth cell: 300 points is enough here
dxs = xs[1] - xs[0]
d2 = (xs[:, None] - xs[None, :])**2         # squared distance between grid points [m^2]
t6 = np.logspace(-1, 2.5, 150)              # 0.1 s .. 316 s

# Task 6 -- two blanks.
def T_free(tv, h_on_grid):
    """The initial temperature h_on_grid, evolved as if the bar had no ends."""
    G = ___        # the kernel above, for every pair of points: shape (xs.size, xs.size)
    return ___     # superpose: integrate G against h_on_grid over the bar

# --- given: the same bump evolved both ways, and where they part company ---
def both_ways(xc):
    """(free-space solution, series solution) for a bump centred at xc, on the grid xs."""
    h_b = np.exp(-(x - xc)**2 / w_b**2)
    C_b = (2 / L) * np.sum(h_b * S, axis=1) * dx
    bar = (C_b * np.exp(-kappa * (n * np.pi / L)**2 * t6[:, None])) @ S
    return np.array([T_free(tv, h_b[::4]) for tv in t6]), bar[:, ::4]

free, bar = both_ways(0.15)
fw.show_profiles(xs, {"the bar, with ends": bar[::3], "no ends": free[::3]}, t6[::3],
                 value_name="t", value_fmt="{:.3g}", unit=" s", ylabel="T [K]",
                 title="The same heat, with and without ends")
fw.show_spacetime(xs, t6, np.abs(free - bar), t_label="t [s]", x_label="x [m]",
                  c_label="|difference| [K]", signed=False,
                  title="What the ends cost: the two solutions differ from the near end inwards")

# The instant the two differ by `thresh` of the peak, for five positions of the bump.
thresh = 0.01                               # try 0.002 and 0.02: kappa should not care
xcs = np.array([0.10, 0.125, 0.15, 0.20, 0.25])
t_dep = []
for xc in xcs:
    f, b = both_ways(xc)
    rel = np.max(np.abs(f - b), axis=1) / np.max(np.abs(f), axis=1)
    t_dep.append(t6[np.argmax(rel > thresh)])
t_dep = np.array(t_dep)

slope, intercept = np.polyfit(xcs**2, t_dep, 1)
kappa_fit = 1 / (4 * slope * np.log(1 / thresh))
plt.figure(figsize=(5.2, 3.2))
plt.plot(xcs**2, t_dep, "o", color="#00A6D6", label="measured")
plt.plot(xcs**2, slope * xcs**2 + intercept, "-", color="#8a9199",
         label=f"fit: $\\kappa$ = {kappa_fit:.2e} m$^2$/s")
plt.xlabel("$x_c^2$ [m$^2$]"); plt.ylabel("departure time [s]")
plt.grid(alpha=0.3); plt.legend(fontsize=8); plt.tight_layout(); plt.show()
print(f"departure times [s]: {np.round(t_dep, 2)}")
print(f"intercept: {intercept:.2f} s   (-w^2/(4 kappa) = {-w_b**2/(4*kappa):.2f} s)")
print(f"kappa from the fit: {kappa_fit:.3e} m^2/s   (the bar was built with {kappa:.3e})")

# --- self-check (leave this alone) ---
_h_check = np.exp(-(x - 0.15)**2 / w_b**2)[::4]
fw.check_abs("at t = 0.1 s the superposition reproduces the series solution",
             T_free(t6[0], _h_check) - bar[0], 1e-6,
             hint="the kernel must carry unit heat: check the 1/sqrt(4 pi kappa t) factor "
                  "and that the sum over x' is multiplied by dxs")
fw.check_scalar("kappa recovered from the departure times", kappa_fit, kappa, rtol=0.05,
                unit=" m^2/s")
```

:::{admonition} Solution — Task 6
:class: dropdown

```python
def T_free(tv, h_on_grid):
    G = np.exp(-d2 / (4 * kappa * tv)) / np.sqrt(4 * np.pi * kappa * tv)
    return G @ h_on_grid * dxs
```
:::

:::{admonition} The ends are felt when the tail reaches them, and that measures $\kappa$
:class: important dropdown

The bump spreads to width $\sqrt{4\kappa t + w^2}$, so the temperature at the near end, as a
fraction of the peak, is $\exp[-x_c^2/(4\kappa t + w^2)]$. Setting that ratio to the threshold
$\theta$ gives

$$ 4\kappa\,t_{\text{dep}} = \frac{x_c^2}{\ln(1/\theta)} - w^2 , $$

a straight line in $x_c^2$, which is what the second figure shows. Its slope is
$1/(4\kappa\ln(1/\theta))$, so the fit returns $\kappa$ to about 1%. The intercept is negative:
$-w^2/(4\kappa) = -2.05$ s predicted against $-1.96$ s measured, the head start the bump gets from
the width it already had at $t=0$.

$\theta$ cancels out of $\kappa$ because the Gaussian tail is exactly log-quadratic, so moving the
threshold scales every departure time by one common factor and the slope absorbs it. Set `thresh`
to 0.002 and to 0.02: the nearest bump departs at 1.7 s instead of 4.0 s, yet $\kappa$ comes back as
$1.08\times10^{-4}$ and $1.09\times10^{-4}$ m²/s against the $1.09\times10^{-4}$ of the 1% run. A bump
whose tail was not Gaussian would not cancel. Push `thresh` to 0.05 and the fit finally drifts 5%
low, because by then the departure is being read off the shoulder of the bump rather than its tail.

Two things are worth taking from this. A boundary makes itself felt through the tail of the
distribution, long before the diffusion length $\sqrt{4\kappa t}$ equals the distance to it.
And the same $t\propto x^2$ that set the peak time in Task 4 sets this departure time, because
a diffusive field has only one way to convert a distance into a time.
:::


### Task 7 — how big a box, and how many modes?

Part 2 used the closed form on the infinite wire. The lecture notes reach the same field a second
way: put the wire in a box of length $2M$, expand the initial Gaussian in cosines, and let each
mode decay at its own rate. With $M\gg L$ the coefficients can be integrated in closed form, and
the series collapses to

$$ T(x,t) = \frac{T_0L\sqrt{\pi}}{M}\left\{\frac{1}{2} + \sum_{n=1}^{N}\cos\!\left(\frac{n\pi x}{M}\right)\exp\!\left[-\left(\frac{n\pi}{2M}\right)^2\!(4\kappa t+L^2)\right]\right\} . $$

The box is fictitious, so $M$ and $N$ are ours to choose, and a wrong choice shows up as an error
against the exact solution. Take $L=10$ m, $-3L<x<3L$ and $-1<\log_{10}(\kappa t)<4$.

1. Write the series above as a function of `kt`, `M` and `Nc`. It is one matrix product: build
   $\cos(n\pi x/M)$ with rows $n=1\ldots N$, the decay $\exp[-(n\pi/2M)^2(4\kappa t+L^2)]$ with
   rows over time, and multiply.
2. The given code measures the largest error against the exact solution over the whole window,
   for a grid of $M$ and $N$, and prints it as a table. Read off the **smallest** pair that stays
   under 0.1%, and enter it below.
3. Before you look: which of $M$ and $N$ do you expect to matter, and why?

```{code-cell} ipython3
Lw, xw = 10.0, np.linspace(-30.0, 30.0, 401)   # Gaussian width [m], position [m]
ktw = np.logspace(-1, 4, 120)                  # kappa * t [m^2]
Ms, Ns = np.array([10, 15, 20, 25, 30, 35, 40]) * Lw, np.array([10, 20, 30, 40, 60, 80, 120])

# Task 7 -- two blanks.
def T_cos(kt, M, Nc):
    """The cosine series above, on the grid xw. Returns shape (len(kt), len(xw))."""
    return ___

M_ok, N_ok = ___, ___          # the smallest pair in the table that stays under 0.1%

# --- given: the exact solution, and the error of the series against it ---
_w2 = 4*ktw[:, None] + Lw**2                   # the spreading width squared [m^2]
T_ex = T0 * Lw / np.sqrt(_w2) * np.exp(-xw[None, :]**2 / _w2)
def worst(M, Nc):
    """Largest error over the window, as a fraction of the peak at the same instant."""
    return np.max(np.abs(T_cos(ktw, M, Nc) - T_ex) / np.max(np.abs(T_ex), axis=1)[:, None])

print("max error against the exact solution, per cent of the peak\n")
print("       " + "".join(f"{'N=' + str(v):>8s} " for v in Ns))
for M in Ms:
    print(f"M={M/Lw:4.0f}L " + "".join(f"{worst(M, v)*100:8.3f} " for v in Ns))

# --- given: your own choice, against the exact solution ---
fw.show_profiles(xw, {"cosine series": T_cos(ktw, M_ok, N_ok)[::3], "exact": T_ex[::3]}, ktw[::3],
                 value_name="κt", value_fmt="{:.3g}", unit=" m²", ylabel="T [K]",
                 title=f"A wire in a box of {M_ok/Lw:.0f}L, with {N_ok} modes")

# --- self-check (leave this alone) ---
fw.check("a box of 40L with 120 modes reproduces the exact solution to 0.1%",
         worst(40 * Lw, 120) < 1e-3,
         "check the prefactor T0 L sqrt(pi) / M, the lone 1/2 for the n = 0 mode, "
         "and that the decay carries (4 kt + L^2), not 4 kt")
fw.check(f"your pair M = {M_ok/Lw:.0f}L, N = {N_ok} stays under 0.1%", worst(M_ok, N_ok) < 1e-3)
fw.check("it is the smallest such pair: one step down in M, or in N, breaks 0.1%",
         worst(Ms[max(np.searchsorted(Ms, M_ok) - 1, 0)], N_ok) > 1e-3
         and worst(M_ok, Ns[max(np.searchsorted(Ns, N_ok) - 1, 0)]) > 1e-3,
         "a generous box passes the previous check but is not the answer to the question")
```

:::{admonition} Solution — Task 7
:class: dropdown

```python
def T_cos(kt, M, Nc):
    nc = np.arange(1, Nc + 1)
    C = np.cos(np.outer(nc, np.pi * xw / M))
    D = np.exp(-(nc * np.pi / (2*M))**2 * (4*np.asarray(kt)[:, None] + Lw**2))
    return T0 * Lw * np.sqrt(np.pi) / M * (0.5 + D @ C)

M_ok, N_ok = 300.0, 60
```
:::

:::{admonition} The box must outrun the heat, and the modes must resolve the source
:class: important dropdown

The table falls into two halves. At and below $M=25L$ the box itself is the limit: adding modes
drives the error down to a floor of 23% at $15L$, 4.3% at $20L$ and 0.50% at $25L$, and no
further. By the end of the window the Gaussian has spread to $\sqrt{4\kappa t}=20L$, so a box of
$15L$ has heat piled against a wall that is not there in the real problem. The box has to outrun the diffusion length, and $30L$
against $20L$ is the margin that does it.

Adding modes cannot repair that, but neither is $N$ free. Read down the $N=10$ column: the error
*grows* as the box grows, from 23% at $15L$ to 56% at $40L$. The shortest wavelength in the series
is $2M/N$, and it has to resolve the initial Gaussian, so $N$ must grow in step with $M$:
$N\gtrsim 2M/L$. At $M=30L$ that is $N=60$, which is exactly where the table turns.

So the two knobs answer two different physical questions, one about the far field at late time and
one about the source at early time. This is Task 6 read backwards. There we asked when a real
boundary makes itself felt; here we ask how far away to put a fictitious one so that it never does.
:::

---

## Part 4 — The same kernel in the Earth

A horizontal current sheet is switched on at $t=0$ with current $I$ per unit width. In the diffusive approximation the electric field a distance $z$ from the sheet is

$$ E_x(z,t) = -I\sqrt{\frac{\mu}{4\pi\sigma t}}\exp\!\left(-\frac{\sigma\mu z^2}{4t}\right), \qquad t>0 . $$

The exponential is the kernel of Part 2 with $\kappa$ replaced by $1/(\sigma\mu)$, so the field soaks into the ground as heat spreads along a wire. The prefactors differ by the constant $I/\sigma$, which sets the amplitude and not the shape. Rock is non-magnetic, so $\mu=\mu_0$.

The sheet sits in a uniform conductor and the solution is even in $z$, so reading $z$ as depth means ignoring the air above: an idealisation, not a consequence of the derivation. The approximation also neglects $\varepsilon\,\partial_t\boldsymbol{E}$, which is justified when $t$ is much longer than the charge relaxation time $\tau_r = \varepsilon/\sigma$. This is the one-dimensional idealisation behind time-domain electromagnetic sounding; a real system uses a finite loop and records $\partial_t B$.

### Task 8 — when does the field arrive, and in what ground?

Write the time at which $\lvert E_x\rvert$ at depth $z$ peaks, from $\partial_t\lvert E_x\rvert = 0$. Differentiating $\ln\lvert E_x\rvert$ is easier and has the same roots. **Predict** first whether a deeper receiver peaks earlier or later, and by what power of $z$.

Then the same receiver in three grounds: seawater at 4 S/m, saturated sediments at $10^{-2}$ S/m, crystalline basement at $10^{-4}$ S/m. **Predict**, before running, how they rank by arrival time at 300 m and by what factor $t_p$ changes from basement to seawater.

The second blank is the margin the diffusive approximation has left, $t_p/\tau_r$ with $\tau_r=\varepsilon/\sigma$. Write it in closed form, in terms of $z$ and $\sigma$, and watch what $\sigma$ does to it.

```{code-cell} ipython3
sigma, eps_r, I_s = 0.01, 10.0, 1.0        # sediments [S/m], relative permittivity, current [A/m]
tau_r = eps_r * epsilon_0 / sigma          # charge relaxation time [s]
t_em = np.logspace(-6, -1, 3001)           # [s], from about 100 relaxation times
_depths = [100.0, 300.0, 1000.0]           # [m]

def E_step(z, t, s=sigma):
    return -I_s * np.sqrt(mu_0 / (4*np.pi*s*t)) * np.exp(-s*mu_0*z**2 / (4*t))

# Task 8 -- two blanks. `s` is the conductivity [S/m]; it defaults to the sediments above.
def t_peak_em(z, s=sigma):
    """Time at which |E_x| at depth z peaks [s]."""
    return ___

def peak_over_relax(z, s):
    """How many charge relaxation times the peak waits: t_p / tau_r. Dimensionless."""
    return ___

# --- given, 1: the field soaking downward. Drag the bar, or press play ---
_zs = np.linspace(1.0, 2000.0, 400)                     # depth [m]
_tp = np.logspace(-6, -1.3, 60)                         # [s]
_prof = np.array([np.abs(E_step(_zs, tv)) / np.abs(E_step(1.0, tv)) for tv in _tp])
fw.show_profiles(_zs, _prof, _tp, value_name="t", value_fmt="{:.2g}", unit=" s",
                 xlabel="depth z [m]", ylabel="|E<sub>x</sub>| / its value at the surface",
                 title="The field diffuses into the Earth", ylim=(0.0, 1.05))

# --- given, 2: depth against time, with your arrival-time curve over it ---
fw.show_spacetime(_zs, _tp, _prof, t_label="t [s]", x_label="depth z [m]",
                  c_label=r"$|E_x|$ / surface value", signed=False,
                  curve=(t_peak_em(_zs), _zs), curve_label=r"your $t_p(z)$", deeper_down=True,
                  title=r"Deeper means later: $t_p \propto z^2$")

# --- given, 3: what a receiver records at three depths ---
fw.show_records(t_em, {f"z = {z:g} m": np.abs(E_step(z, t_em)) / np.max(np.abs(E_step(z, t_em)))
                       for z in _depths},
                peaks={f"z = {z:g} m": (t_peak_em(z), 1.0) for z in _depths},
                t_label="t [s]", y_label=r"$|E_x|$ / peak value",
                title=r"Step response at depth, $\sigma$ = 0.01 S/m")
for z in _depths:
    print(f"z = {z:6.0f} m:  t_p = {t_peak_em(z):.3g} s,  t_p / tau_r = {t_peak_em(z)/tau_r:.2g},"
          f"  |E| at the peak = {abs(E_step(z, t_peak_em(z))):.3g} V/m")

# --- self-check (leave this alone) ---
for z in _depths:
    fw.check_scalar(f"t_p at {z:g} m against the peak of the record", t_peak_em(z),
                    t_em[np.argmax(np.abs(E_step(z, t_em)))], rtol=0.01, unit=" s")
fw.check_close("t_p / tau_r against t_p and tau_r built separately, over five decades of sigma",
               [peak_over_relax(300.0, sv) for sv in (1e-4, 1e-3, 1e-2, 1e-1, 1.0)],
               [t_peak_em(300.0, sv) / (eps_r * epsilon_0 / sv)
                for sv in (1e-4, 1e-3, 1e-2, 1e-1, 1.0)], rtol=1e-6,
               hint="tau_r = eps_r eps_0 / sigma shrinks as t_p grows, so the ratio carries sigma twice")
fw.check("a tenfold drop in conductivity costs a hundredfold in t_p / tau_r",
         np.isclose(peak_over_relax(300.0, 1e-3) / peak_over_relax(300.0, 1e-4), 100.0, rtol=1e-9),
         "the margin goes as sigma^2, not as sigma")
```

```{code-cell} ipython3
# --- given: one receiver at 300 m, three grounds -----------------------------
media = {"seawater, 4 S/m": 4.0,
         "saturated sediments, 1e-2 S/m": 0.01,
         "crystalline basement, 1e-4 S/m": 1e-4}
z_s = 300.0                                             # the receiver depth [m]
t_s = np.logspace(-8, 1, 900)                           # [s]

fw.show_records(t_s, {k: np.abs(E_step(z_s, t_s, sv)) / np.max(np.abs(E_step(z_s, t_s, sv)))
                      for k, sv in media.items()},
                peaks={k: (t_peak_em(z_s, sv), 1.0) for k, sv in media.items()},
                t_label="t [s]", y_label="|E| / peak value",
                title=f"The same receiver at {z_s:.0f} m, in three grounds")

print(f"at z = {z_s:.0f} m\n")
print(f"{'ground':<30}{'t_p [s]':>11}{'tau_r [s]':>11}{'t_p / tau_r':>13}")
for k, sv in media.items():
    print(f"{k:<30}{t_peak_em(z_s, sv):>11.3g}{eps_r*epsilon_0/sv:>11.3g}"
          f"{peak_over_relax(z_s, sv):>13.3g}")

print("\na survey looking 500 m down, able to record for 10 ms:")
for k, sv in media.items():
    _tp = t_peak_em(500.0, sv)
    print(f"  {k:<30} t_p = {_tp:.3g} s   {'inside' if _tp < 1e-2 else 'beyond'} the window")

# --- self-check (leave this alone) ---
_tf = np.logspace(-8, 1, 20001)
for k, sv in media.items():
    fw.check_scalar(f"t_p at {z_s:.0f} m in {k.split(',')[0]}", t_peak_em(z_s, sv),
                    _tf[np.argmax(np.abs(E_step(z_s, _tf, sv)))], rtol=0.01, unit=" s")
fw.check("basement to seawater is a factor 4e4 in arrival time",
         np.isclose(t_peak_em(z_s, 4.0) / t_peak_em(z_s, 1e-4), 4e4, rtol=1e-9),
         "t_p is linear in sigma, and the two conductivities differ by 4e4")
```

:::{admonition} Solution — Task 8
:class: dropdown

```python
def t_peak_em(z, s=sigma):
    return s * mu_0 * z**2 / 2

def peak_over_relax(z, s):
    return s**2 * mu_0 * z**2 / (2 * eps_r * epsilon_0)
```
:::

:::{admonition} Depth maps onto arrival time, as $t_p\propto z^2$
:class: important dropdown

A layer ten times deeper answers a hundred times later: 63 µs at 100 m, 6.3 ms at 1 km, for $\sigma=0.01$ S/m. On the map your curve $t_p(z)$ runs along the shoulder of the diffusing field, because $|E_x|$ has fallen to $1/\sqrt e$ of its surface value exactly where $t = \sigma\mu z^2/2$. Time-domain electromagnetic soundings rest on this: the later part of a record senses the deeper Earth. In a more conductive Earth the arrival is later, since $t_p\propto\sigma$. The ratio $t_p/\tau_r$ is 7000 at 100 m and grows as $z^2$, so neglecting $\varepsilon\,\partial_t\boldsymbol{E}$ is well justified at these depths. The blurring of Task 5 applies here too: deep structure arrives late, and therefore blurred.

The peak amplitude is 0.24 V/m at 100 m and 0.024 V/m at 1 km. A factor of ten in depth costs a factor of ten in signal and a factor of a hundred in time, which is the $1/\lvert x\rvert$ law of Task 4 with depth in place of distance along the wire.

The chapter's three-dimensional impulse response peaks at $t_p=\sigma\mu r^2/6$, three times earlier than the $\sigma\mu z^2/2$ you found here, and its amplitude falls as $1/r^3$. Both follow from the same differentiation: a prefactor $t^{-p}$ gives $t_p=\sigma\mu r^2/(4p)$, with $p=1/2$ for the sheet and $p=3/2$ for the point.
:::

:::{admonition} Conductivity sets the clock, and it sets the margin twice over
:class: important dropdown

At 300 m the peak arrives after 0.23 s in seawater, 0.57 ms in sediments and 5.7 µs in basement. That is a factor $4\times10^{4}$ from basement to seawater, exactly the ratio of the two conductivities, because $t_p=\sigma\mu z^2/2$ is linear in $\sigma$. A conductive ground holds the field up; a resistive one lets it through almost at once.

The margin behaves differently. $\tau_r=\varepsilon/\sigma$ grows as the ground becomes resistive while $t_p$ shrinks, so

$$ \frac{t_p}{\tau_r} = \frac{\sigma^2\mu z^2}{2\varepsilon} $$

carries $\sigma$ twice and falls a hundredfold for every tenfold drop in conductivity: $10^{10}$ in seawater, $6.4\times10^{4}$ in sediments, and **6.4 in basement**. The diffusive approximation is comfortable in the first two and running out in the third, and it is the *resistive* ground that breaks it, not the conductive one. Dropping $\varepsilon\,\partial_t\boldsymbol{E}$ was never a statement about depth. It is a statement about how fast charge can relax, and in a resistive ground it cannot relax quickly.

The survey question resolves the same way from the other end. Looking 500 m down with a 10 ms record: seawater peaks at 0.63 s, far beyond the window, so the target is never reached in time. Sediments peak at 1.6 ms, comfortably inside. Basement peaks at 16 µs, inside the window but so early that a real transmitter is still switching off, and the useful signal is buried in the turn-off transient. Conductivity, not instrument quality, decides which depths a time-domain sounding can reach.
:::
