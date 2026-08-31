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

# Lab: Gradient and Divergence

:::{admonition} Computer lab
:class: note

A practical companion to the lectures on the gradient and the divergence. Each task states a physical question, gives you the steps, and ends with a self-check you can run. What we supply is the *plotting*, in a module called `fwtools` — drawing a transparent isosurface teaches you nothing about electromagnetism, so your time goes on physics instead.
:::

## Learning objectives

By the end of this lab you should be able to:

- **Truncate a series and know what you lost.** Sum a geometric series, approximate it by its leading term, and say how many terms buy a given accuracy — and where a Taylor series stops working altogether.
- **Read a gradient off a picture.** Show that $\nabla r = \hat{\boldsymbol{r}}$, that $\nabla f$ is perpendicular to the level surfaces of $f$, and that $dp/dl = \lvert\nabla p\rvert\cos\psi$ — so the gradient's magnitude *is* the maximum rate of change.
- **Turn a potential into a field, and a field into a survey.** Apply $\boldsymbol{E} = -\nabla V$ and Ohm's law $\boldsymbol{J} = -\rho^{-1}\nabla V$, and map the potential and current density of a two-electrode DC resistivity measurement.
- **Distinguish "arrows spreading apart" from divergence.** Compute $\nabla\cdot\boldsymbol{v}$, justify the answer by flux rather than algebra, and find the only radial flow that is incompressible.
- **Use the divergence theorem as a measurement.** Verify $\oint_S\boldsymbol{v}\cdot\hat{\boldsymbol{n}}\,dS = \int_{\mathcal{D}} \nabla\cdot\boldsymbol{v}\,dV$ numerically, and explain what happens when the source shrinks to a point.

:::{admonition} Two sessions
:class: note

**Session 1** runs to the end of Part 4, covering the gradient. **Part 5 onwards is the following session**, once the divergence has been lectured. Everything is in one page so you can work ahead if you want to.
:::

---

## Part 0 — Setup

Run this once. Nothing in it is physics: it fetches two packages the browser lacks, finds `fwtools`, and defines the Coulomb constant for later.

```{code-cell} ipython3
# Nothing above the K = ... line near the bottom is physics; skip to there.
import sys, pathlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0

# --- Live Code housekeeping; nothing here is part of the physics ------------
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

for _p in (".", "book/1_gradient_divergence_curl/labs"):
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

k_e = 1.0 / (4.0 * np.pi * epsilon_0)   # Coulomb constant, 8.99e9 V*m/C
Q = 1e-9                                # 1 nC test charge

print(f"epsilon_0 = {epsilon_0:.4e} F/m")
print(f"k_e       = {k_e:.4e} V*m/C")
```

---

## Part 1 — Series, and what you lose by truncating

Before any fields, one point that runs through the whole course: a physical quantity is often an infinite sum, and we almost always keep only the first few terms. This part is about what that costs.

### Task 1 — the bouncing ball

A ball leaves the ground at $z=0$ with upward velocity $v_0$. Between bounces it is in free fall,

$$ z(t) = v_0 t - \tfrac{1}{2}g t^2, $$

so it returns to the ground after $T_0 = 2v_0/g$ having reached a height $H = v_0^2/2g$. At each bounce it loses a fraction $\gamma$ of its energy, so $v_n = \sqrt{1-\gamma}\;v_{n-1}$, and since flight time is proportional to launch speed,

$$ T_n = (1-\gamma)^{n/2}\,T_0, \qquad T_0 = \sqrt{8H/g}. $$

Fill in the three physical lines. The plotting is written for you.

```{code-cell} ipython3
g, v0, gamma = 9.81, 5.0, 0.1
N = 12                                    # bounces to draw

H  = ___                                  # peak height of the first flight
T0 = ___                                  # duration of the first flight
T  = T0 * ___                             # durations of bounces 0 .. N-1

# --- given: draw one parabola per bounce ---
t_start = np.concatenate(([0.0], np.cumsum(T)[:-1]))
plt.figure(figsize=(9, 3.4))
for Tn, t0 in zip(T, t_start):
    tau = np.linspace(0, Tn, 200)
    plt.plot(t0 + tau, (g*Tn/2)*tau - g*tau**2/2, "C0")
plt.xlabel("$t$ [s]"); plt.ylabel("$z$ [m]"); plt.grid(alpha=0.3)
plt.title(f"bouncing ball, $\\gamma$ = {gamma}")
plt.show()

# --- self-check (leave this alone) ---
fw.check(f"H = {H:.4f} m", np.isclose(H, v0**2/(2*g)), "H = v0^2 / 2g")
fw.check(f"T0 = {T0:.4f} s", np.isclose(T0, 2*v0/g), "T0 = 2 v0 / g")
fw.check("T0 = sqrt(8H/g) too", np.isclose(T0, np.sqrt(8*H/g)))
fw.check(f"{N} bounce durations, shrinking", len(T) == N and T[-1] < T[0])
```

:::{admonition} Solution — Task 1
:class: dropdown

```python
H  = v0**2 / (2*g)
T0 = 2*v0 / g
T  = T0 * (1 - gamma)**(np.arange(N)/2)
```
:::

Now the series. The ball bounces for a total time

$$ T_\infty = \sum_{m=0}^{\infty} T_m = T_0\sum_{m=0}^{\infty}\left(\sqrt{1-\gamma}\right)^{m} = \frac{\sqrt{8H/g}}{1-\sqrt{1-\gamma}}, $$

which is a geometric series with ratio $\sqrt{1-\gamma}$. That ratio is smaller than 1 for any real bounce, so the sum is **finite** — infinitely many bounces, over in about twenty seconds. (Hold on to the condition: Task 2 is about what happens to a series when it fails.) For small $\gamma$ the expansion $\sqrt{1-\gamma}\approx 1-\gamma/2$ collapses that to something much simpler,

$$ T_\infty \approx \sqrt{8H/g}\;\frac{2}{\gamma}. $$

Two questions follow, and both are worth answering by measurement rather than by intuition: **how good is that approximation**, and **how many bounces must you actually add up** before the running total gets there?

```{code-cell} ipython3
rows = {}
print(f"{'gamma':>7} {'T_inf':>9} {'approx':>9} {'error':>7} {'n for 99%':>10}")
for gam in (0.5, 0.2, 0.1, 0.02):
    T_inf  = ___                          # the exact sum, from the formula above
    T_appr = ___                          # the small-gamma approximation

    # --- given: how many bounces to reach 99% of T_inf ---
    rows[gam] = (T_inf, T_appr)
    cum = np.cumsum(T0 * (1 - gam)**(np.arange(4000)/2))
    n99 = int(np.argmax(cum >= 0.99*T_inf)) + 1
    print(f"{gam:>7.2f} {T_inf:>8.3f}s {T_appr:>8.3f}s "
          f"{abs(T_appr-T_inf)/T_inf:>6.1%} {n99:>10}")

# --- self-check (leave this alone) ---
# Your closed form against a brute-force sum of 5000 bounces: the same
# number by two routes, one of which never assumed the series converges.
_summed = np.sum(T0 * (1 - 0.1)**(np.arange(5000)/2))
fw.check(f"your T_inf at gamma = 0.1 ({rows[0.1][0]:.3f} s) equals the "
         f"brute-force sum ({_summed:.3f} s)",
         np.isclose(rows[0.1][0], _summed, rtol=1e-6))
fw.check(f"your approximation overshoots by 2.6% there "
         f"({rows[0.1][1]/rows[0.1][0] - 1:.2%})",
         np.isclose(rows[0.1][1]/rows[0.1][0], 1.0263, rtol=1e-3))
```

:::{admonition} Solution — Task 1, continued
:class: dropdown

```python
    T_inf  = np.sqrt(8*H/g) / (1 - np.sqrt(1 - gam))
    T_appr = np.sqrt(8*H/g) * 2 / gam
```
:::

:::{admonition} What the table says
:class: important

At $\gamma = 0.5$ the leading-term approximation is 17% wrong; at $\gamma = 0.02$ it is 0.5%. "Keep only the first term" is not a statement about algebra — it is a statement about the *regime*, and it has to be earned.

The term count runs the other way. The more nearly elastic the ball, the more bounces you must sum for the same accuracy: 14 at $\gamma = 0.5$, 456 at $\gamma = 0.02$. Cheap approximation, expensive summation — and the two get cheap and expensive at opposite ends. You will meet that trade in every numerical method this course touches.
:::

### Task 2 — where a Taylor series stops working

A function that is smooth enough — and whose series actually sums back to it, which is the catch this task is about — can be written as a Taylor series about $x=0$,

$$ f(x) = f(0) + x f'(0) + \tfrac{1}{2}x^2 f''(0) + \cdots, $$

and in practice we truncate it after a few terms. Take two:

$$ \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots, \qquad\qquad \frac{1}{1+x} = 1 - x + x^2 - x^3 + \cdots $$

Both look equally harmless. Add terms to each and watch what happens.

```{code-cell} ipython3
x = np.linspace(-3, 3, 600)

# term m of each series, as a function of x
def sin_term(m, x):
    return 0.0 if m % 2 == 0 else ___     # (-1)^((m-1)/2) x^m / m!   [math.factorial]

def geo_term(m, x):
    return ___                            # term m of 1 - x + x^2 - ...

# --- given: exact curve plus four truncations, side by side ---
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for ax, (name, exact, term) in zip(axes, [
        (r"$\sin x$",   np.sin,            sin_term),
        (r"$1/(1+x)$",  lambda x: 1/(1+x), geo_term)]):
    ax.plot(x, exact(x), "k", lw=2, label="exact")
    for M in (2, 4, 8, 16):
        ax.plot(x, sum(term(m, x) for m in range(M + 1)), lw=1, label=f"M = {M}")
    ax.set_ylim(-3, 3); ax.set_xlabel("$x$"); ax.set_title(name)
    ax.grid(alpha=0.3); ax.legend(fontsize=8)
plt.tight_layout()
plt.show()

# --- self-check (leave this alone) ---
_s21 = sum(sin_term(m, x) for m in range(21))
_g_in  = sum(geo_term(m, 0.5) for m in range(40))
_g_out = sum(geo_term(m, 1.5) for m in range(40))
fw.check("21 terms reproduce sin(x) on -3 < x < 3", np.max(np.abs(_s21 - np.sin(x))) < 1e-6)
fw.check(f"1/(1+x) converges at x = 0.5 ({_g_in:.4f} vs {1/1.5:.4f})", np.isclose(_g_in, 1/1.5))
fw.check(f"1/(1+x) diverges at x = 1.5 (partial sum {_g_out:.2e})", abs(_g_out) > 1e3)
```

:::{admonition} Solution — Task 2
:class: dropdown

```python
import math

def sin_term(m, x):
    return 0.0 if m % 2 == 0 else (-1)**((m-1)//2) * x**m / math.factorial(m)

def geo_term(m, x):
    return (-x)**m
```
:::

:::{admonition} Radius of convergence
:class: important

$\sin x$ improves everywhere as you add terms. $1/(1+x)$ improves only inside $\lvert x\rvert < 1$; outside it, each extra term makes the partial sum *worse*, without limit — at $x = 1.5$ the 40-term "approximation" is off by millions.

The series has a **radius of convergence** of 1, and no amount of computing power moves it. What sets it is the distance from the point you expanded about to the nearest place the function blows up — here from $x=0$ to the pole at $x=-1$, one unit away. Notice that the failure is invisible at $x = 0$ itself: the function is perfectly smooth there, and the first few terms behave well. Expand the same function about $x = 1$ instead and the radius becomes 2, because the pole is now twice as far off. **The limit is set by where the function misbehaves, not by how well behaved it looks where you started.**

Keep that beside Task 1. There, more terms always helped and the only question was how many. Here, more terms are useless past a certain point. Knowing which situation you are in is the whole skill.
:::

---

## Part 2 — The distance function, and what its gradient is

Everything from here on lives on one cube of sample points.

```{code-cell} ipython3
n, L = 61, 2.0                          # odd n, so the origin is a sample point
axis = np.linspace(-L, L, n)            # one axis, shared by x, y and z
X, Y, Z = np.meshgrid(axis, axis, axis, indexing="ij")
dx = dy = dz = axis[1] - axis[0]

c = n // 2                              # index of the origin
# Masks the self-checks reuse. `interior` drops the two outermost cells so
# that comparisons never include the six faces of the box, where a field is
# sampled at its worst and np.gradient has only one-sided neighbours.
interior = np.zeros(X.shape, dtype=bool)
interior[2:-2, 2:-2, 2:-2] = True

print(f"grid shape {X.shape},  spacing {dx:.4f} m,  {X.size:,} sample points")
print(f"X[i,j,k] = x[i]   ->   X[-1, 0, 0] = {X[-1, 0, 0]:.1f} m")
```

:::{admonition} Grid convention
:class: tip

**Resolution.** Every derivative on this page is a centred difference, so its error falls as $\Delta x^{2}$. Measured worst-case error against the analytic answer:

| $n$ | $\Delta x$ [m] | $\lvert\nabla r\rvert$ | $\nabla(1/r)$ | $\nabla\cdot\boldsymbol{E}$ |
| ---: | ---: | ---: | ---: | ---: |
| 21 | 0.200 | 4.1% | 12.5% | 9.1% |
| 41 | 0.100 | 1.8% | 3.3% | 2.4% |
| **61** | **0.067** | **0.8%** | **1.6%** | **1.1%** |
| 81 | 0.050 | 0.5% | 1.0% | 0.6% |

These are **worst cases** over the region each self-check tests, which is what fixes the tolerances — not an average. Halve $\Delta x$ and the last two columns fall by very nearly the factor of four second order promises (12.5 → 3.3, 9.1 → 2.4). The first column falls by only 2.3, and the reason is worth knowing: the $|\nabla r|$ error grows as you approach the source, so the worst sample in the band $0.4 < r < 1.6$ m is whichever one happens to sit nearest its inner edge — and *that sample moves* when you change `n`. A worst case taken over a boundary the grid keeps redrawing is not a smooth sequence. The clean demonstration is the convergence cell at the end of Part 6, which measures a fixed quantity and does recover the factor of four.

$n = 61$ was chosen by this table: it is the coarsest grid that keeps every task under 2%, and each 3-D figure it produces weighs about 1.5 MB. **If you change `n`, keep it at 41 or above** — the self-checks below allow 5%, and $n = 31$ already fails Task 6 at 6.7%.

Two more things about this cube. It is a finite window on fields that extend to infinity: the largest closed surface in Part 6 sits only 0.6 m inside the outer face. And $z$ points **up** here, as in any ordinary right-handed frame — Part 4 works on the ground instead, and there $z$ points down into it, as Earth-science convention has it. Neither is more correct; what matters is saying which one you are in.


The grid is built with `indexing='ij'`, so axis 0 is $x$, axis 1 is $y$, axis 2 is $z$.

1. **Derivatives come back in coordinate order:** `np.gradient(f, dx, dy, dz)` returns $\partial f/\partial x$, $\partial f/\partial y$, $\partial f/\partial z$. No transposes.
2. **Always pass the spacings.** Omit them and the derivative is silently wrong by a factor of $1/\Delta x = 15$.

Numpy's default is `indexing='xy'`, which returns the $y$-derivative first. That one fact is the origin of a large fraction of all numerical field bugs.
:::

Now the geometry. The simplest scalar field there is:

$$ r(x,y,z) = \sqrt{(x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2} $$

*How far am I from that point?* One number at every location in space. No charge, no potential, no units of anything — just distance.

This is the **spherical** radial coordinate $r$ — distance from a point. The cylindrical $r$, distance from an axis, is a different quantity, and Part 5 returns to the distinction. The equations on this page use $r$; the code calls it `r`, because it is the only radius in the lab.

### Task 3 — build the distance field

**The question:** what do the surfaces of constant $r$ look like, and where do they crowd together? Answer it in your head first — this is the one field on the page you can picture completely before computing it — then build it and check.

The source has to be movable: Task 8 puts two of them down in different places, so write the offsets in now rather than hard-coding the origin.

```{code-cell} ipython3
# Task 3 -- distance from a source at (x0, y0, z0) to every point of the grid.

def distance_to(X, Y, Z, x0=0.0, y0=0.0, z0=0.0):
    return ___                          # root of the sum of three squares


r = ___                                 # call it: one source, at the origin

# --- self-check (leave this alone) ---
fw.check_shape("r", r, X.shape)
fw.check("r = 0 at the origin", np.isclose(r[c, c, c], 0.0))
fw.check("r = 2 m at (2,0,0)", np.isclose(r[-1, c, c], 2.0))
fw.check("r = 2 m at (0,2,0)", np.isclose(r[c, -1, c], 2.0))
fw.check("the source can be moved off the origin",
         np.isclose(distance_to(X, Y, Z, 1.0, 0.0, 0.0)[c, c, c], 1.0),
         "x0, y0, z0 have to appear in the expression -- Task 8 needs them")
```

:::{admonition} Solution — Task 3
:class: dropdown

```python
def distance_to(X, Y, Z, x0=0.0, y0=0.0, z0=0.0):
    return np.sqrt((X - x0)**2 + (Y - y0)**2 + (Z - z0)**2)


r = distance_to(X, Y, Z)
```
:::

A surface on which $r$ takes one fixed value is an **isosurface**, or level set — the three-dimensional version of a contour line on a map. Drag the opacity slider under the figure until you can see the inner shells through the outer one. Evenly spaced values of $r$ give evenly spaced shells: the distance function has no favourite radius, which is exactly what makes its gradient so simple in the next task.

```{code-cell} ipython3
fw.show_isosurfaces(X, Y, Z, r, levels=[0.5, 1.0, 1.5], label="r  [m]",
                    title="Isosurfaces of the distance function r")
```


### Task 4 — the gradient of the distance

Do this one on paper first. Differentiating $r = \sqrt{x^2+y^2+z^2}$ by the chain rule,

$$ \frac{\partial r}{\partial x} = \frac{x}{r}, \qquad \frac{\partial r}{\partial y} = \frac{y}{r}, \qquad \frac{\partial r}{\partial z} = \frac{z}{r} $$

so, collecting the three components,

$$ \nabla r \;=\; \frac{\partial r}{\partial x}\hat{\boldsymbol{x}} + \frac{\partial r}{\partial y}\hat{\boldsymbol{y}} + \frac{\partial r}{\partial z}\hat{\boldsymbol{z}} \;=\; \frac{x\,\hat{\boldsymbol{x}} + y\,\hat{\boldsymbol{y}} + z\,\hat{\boldsymbol{z}}}{r} \;=\; \hat{\boldsymbol{r}} $$

The last step is the definition of the outward unit radial vector: $\hat{\boldsymbol{r}}$ is exactly the position vector divided by its own length. So $\nabla r$ is a **unit** vector pointing **away** from the source — a direction and a magnitude you now know in advance.

The code below checks whether a finite-difference gradient on a grid reproduces that. Two measurements: the magnitude, which should be 1; and the projection $\nabla r \cdot \hat{\boldsymbol{r}}$, which recovers the full magnitude only if the gradient is *purely* radial, with nothing left over along the sphere.

```{code-cell} ipython3
# The outward unit radial vector, used again later.
rs = np.maximum(r, 1e-12)                 # 0/0 at the source is not a lesson
rhx, rhy, rhz = X / rs, Y / rs, Z / rs

# Task 4
#   1. grad r, as three components.
#   2. Its magnitude.
#   3. Its projection onto r-hat.
#   4. Draw it, then rotate the figure and compare with the spheres above.

grx, gry, grz = ___                       # all three spacings, in order

grad_r_mag = ___                          # the length of that vector

radial_part = ___                         # its projection onto (rhx, rhy, rhz)

fw.show_cones(X, Y, Z, grx, gry, grz, step=8, label="|∇r|", unit="-",
              title="grad r -- unit vectors pointing away from the source")

# --- self-check (leave this alone) ---
band = (r > 0.4) & (r < 1.6)
fw.check_shape("grad r (x-component)", grx, X.shape)
fw.check_close("|grad r| = 1 everywhere", grad_r_mag, 1.0, rtol=0.05, where=band)
fw.check_close("grad r is purely radial", radial_part, 1.0, rtol=0.05, where=band)
# The two checks above are the same measurement for THIS field, so they can
# only pass or fail together. This one is independent: it compares the three
# components against r-hat one at a time, so a gradient that had the right
# length but the wrong direction would be caught.
fw.check(f"grad r = r-hat, componentwise (worst "
         f"{np.nanmax(np.abs(np.stack([grx-rhx, gry-rhy, grz-rhz]))[:, band]):.3f} "
         f"of a unit vector)",
         np.nanmax(np.abs(np.stack([grx - rhx, gry - rhy, grz - rhz]))[:, band]) < 0.05)
```

:::{admonition} Solution — Task 4
:class: dropdown

```python
grx, gry, grz = np.gradient(r, dx, dy, dz)
grad_r_mag = np.sqrt(grx**2 + gry**2 + grz**2)
radial_part = grx * rhx + gry * rhy + grz * rhz

print(f"|grad r| median in 0.4 < r < 1.6 m : "
      f"{np.median(grad_r_mag[(r > 0.4) & (r < 1.6)]):.4f}")
```
:::

:::{admonition} What the algebra means
:class: important

$\lvert\nabla r\rvert = 1$ needs no calculus to see: walk one metre directly away from the source and your distance from it grows by exactly one metre, so the steepest rate of change of $r$ is 1 m/m wherever you stand. A gradient carries the direction of steepest increase and a length equal to that rate — here, "away" and 1.

The radial check fixes the other half: moving *along* a sphere does not change $r$, so the gradient has no component there. **$\nabla f$ is normal to the level surfaces of $f$** — for every scalar field, not just this one.

The same chain rule settles the next two tasks in advance: $\nabla g(r) = \dfrac{dg}{dr}\,\hat{\boldsymbol{r}}$ for any $g$ depending on position only through $r$. Derive before you run.
:::

### Task 5 — how fast does it change *that* way?

The gradient's *direction* is settled: steepest increase, normal to the level surface. Its *magnitude* is the claim we have not tested. It follows from

$$ dp = (\nabla p)\cdot d\boldsymbol{l} = \lvert\nabla p\rvert\,\lvert d\boldsymbol{l}\rvert\cos\psi
\qquad\Longrightarrow\qquad
\frac{dp}{dl} = \lvert\nabla p\rvert\cos\psi, $$

where $d\boldsymbol{l}$ is a small step in whatever direction you choose, $dl = \lvert d\boldsymbol{l}\rvert$ is its length, and $\psi$ is the angle between that step and the gradient. (The step is written $d\boldsymbol{l}$ rather than $d\boldsymbol{r}$ only because $r$ already means the distance from the origin on this page.)

Two things follow, and both are testable: the rate of change in *any* direction is $\lvert\nabla p\rvert\cos\psi$, and it can never exceed $\lvert\nabla p\rvert$ — reached only at $\psi = 0$.

Measure it. Pick one point, walk a short distance $\varepsilon$ along many different unit vectors $\hat{\boldsymbol{u}}$, and compare the measured rate against the prediction.

```{code-cell} ipython3
p_field = 1.0 / np.maximum(r, 0.25)       # any scalar field will do
gpx, gpy, gpz = np.gradient(p_field, dx, dy, dz)

ip, jp, kp = 40, 36, 34                   # one sample point, off-axis
gvec = np.array([gpx[ip, jp, kp], gpy[ip, jp, kp], gpz[ip, jp, kp]])
point = np.array([axis[ip], axis[jp], axis[kp]])

def p_exact(q):
    return 1.0 / np.linalg.norm(q)        # the same field, evaluated anywhere

# Task 5 -- fill in the four blanks; the plotting is given.
grad_mag = ___                            # |grad p| at the point, from gvec

rng = np.random.default_rng(0)
eps = 1e-4
cosines, rates = [], []
for _ in range(200):
    u = rng.normal(size=3)
    u = ___                               # make it a UNIT vector
    cosines.append(___)                   # cos(psi) = u . gvec / |grad p|
    rates.append(___)                     # centred difference of p_exact
                                          # along u, step eps, over 2*eps
cosines, rates = np.asarray(cosines), np.asarray(rates)

# --- given: measurements against the predicted straight line ---
plt.figure(figsize=(5.6, 4.4))
plt.scatter(cosines, rates, s=12, alpha=0.6, label="measured")
cs = np.linspace(-1, 1, 50)
plt.plot(cs, grad_mag*cs, "k", lw=1.5, label=r"$|\nabla p|\cos\psi$")
plt.xlabel(r"$\cos\psi$")
plt.ylabel(r"$dp/dl$  [m$^{-2}$]")
plt.legend(); plt.grid(alpha=0.3)
plt.show()

# --- self-check (leave this alone) ---
slope = float(np.polyfit(cosines, rates, 1)[0])
fw.check_scalar("fitted slope = |grad p|", slope, grad_mag, rtol=0.01)
fw.check("no direction beats |grad p|", np.max(np.abs(rates)) <= grad_mag * 1.001)
```

:::{admonition} Solution — Task 5
:class: dropdown

```python
grad_mag = float(np.linalg.norm(gvec))

# ... and inside the loop:
    u = u / np.linalg.norm(u)
    cosines.append(float(u @ gvec) / grad_mag)
    rates.append((p_exact(point + eps*u) - p_exact(point - eps*u)) / (2*eps))
```
:::

:::{admonition} The magnitude, earned
:class: important

Every measured rate lies on the line. Three readings of the same picture:

- **At $\cos\psi = 1$** you are walking straight up the gradient, and the rate equals $\lvert\nabla p\rvert$ exactly. Nothing beats it — that is what "steepest" means, now measured rather than asserted.
- **At $\cos\psi = 0$** you are moving along the level surface and $p$ does not change at all. This is the normality result of Task 4, arriving a second time by a different route.
- **At $\cos\psi = -1$** you get $-\lvert\nabla p\rvert$: the steepest *descent*, which is the direction $\boldsymbol{E} = -\nabla V$ will pick out in Part 3.

One vector carries a direction *and* a rate, and the cosine tells you what you get for walking at an angle to it.
:::

---

## Part 3 — Invert it, and watch the arrows turn round

Now the function the physics actually uses: not the distance, but **one over** the distance,

$$ f(r) = \frac{1}{r}, \qquad\text{so}\qquad \nabla f = \frac{d}{dr}\!\left(\frac{1}{r}\right)\hat{\boldsymbol{r}} = -\frac{1}{r^{2}}\,\hat{\boldsymbol{r}} $$

Same spheres as isosurfaces — $f$ is constant wherever $r$ is constant. But the *ordering* has been turned inside out: $f$ is now largest near the source and decays to nothing far away. Predict what that does to the arrows, then check the prediction against the formula above, then measure it.

### Task 6 — the gradient of the inverse distance

```{code-cell} ipython3
# The mask keeps the singularity at r = 0 off the grid. Everything within
# 0.25 m of the source becomes NaN and is simply not measured.
r_masked = np.where(r < 0.25, np.nan, r)
f = 1.0 / r_masked

# Task 6 -- two blanks. Predict the direction before you look at the figure.
fx, fy, fz = ___                          # grad f
f_mag = ___                               # its magnitude, to compare with 1/r^2

# --- given: the numbers, then the picture ---
for rr in (0.6, 1.0, 1.5):
    i = int(np.argmin(np.abs(X[:, 0, 0] - rr)))
    print(f"r = {rr:.1f} m :  |grad f| = {f_mag[i, c, c]:8.4f}   1/r^2 = {1/rr**2:8.4f}")

# normalise=True draws every arrow the same length, so the picture carries
# direction only; the magnitude moves into the colour, on a log scale,
# because the drawn arrows span a factor of 62.
fw.show_cones(X, Y, Z, fx, fy, fz, step=8, normalise=True,
              label="|∇(1/r)|", unit="m<sup>-2</sup>",
              title="grad(1/r) -- pointing back towards the source")

# --- self-check (leave this alone) ---
outside = (r > 0.5) & interior            # `interior` was built in Part 2
fw.check_close("|grad(1/r)| = 1/r^2", f_mag, 1.0 / r_masked**2, rtol=0.05, where=outside)
fw.check("grad(1/r) points inward at (1,0,0)", fx[-1 - 15, c, c] < 0)
```

:::{admonition} Solution — Task 6
:class: dropdown

```python
fx, fy, fz = np.gradient(f, dx, dy, dz)
f_mag = np.sqrt(fx**2 + fy**2 + fz**2)
```
:::

:::{admonition} The gradient points towards *increase* — always
:class: important

The arrows have reversed. Same spheres, same source, opposite direction:

$$ \nabla r = +\hat{\boldsymbol{r}}, \qquad\qquad \nabla\!\left(\frac{1}{r}\right) = -\frac{1}{r^{2}}\,\hat{\boldsymbol{r}} $$

Nothing about space changed. What changed is **which way the function climbs**. And the steepness changed too: $1/r$ climbs ever faster as you approach the source, so its gradient grows as $1/r^2$ rather than staying at 1.

A gradient knows nothing about sources, sinks, charges or fields. It only knows uphill.
:::

### Task 7 — from geometry to physics

Here the physics enters, and it enters as a single minus sign. The electric potential of a point charge $Q$ is the inverse-distance function with a constant in front,

$$ V(r) = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r}\quad[\text{V}], $$

and the electric field is *defined* as

$$ \boldsymbol{E} = -\nabla V \quad[\text{V/m}]. $$

You already know what $\nabla V$ does: it points inward, uphill towards the charge. The minus sign turns it round, so **the field points downhill** — which is exactly the way a positive test charge released from rest would move, losing potential energy as it goes.

```{code-cell} ipython3
V = k_e * Q / r_masked

# Task 7 -- two blanks. Mind the minus sign; it is the whole task.
Ex, Ey, Ez = ___                          # E = -grad V
E_mag = ___

# --- given: against the analytic k_e*Q/r^2, then the picture ---
for rr in (0.6, 1.0, 1.5):
    i = int(np.argmin(np.abs(X[:, 0, 0] - rr)))
    print(f"r = {rr:.1f} m :  |E| = {E_mag[i, c, c]:8.3f} V/m   "
          f"analytic = {k_e*Q/rr**2:8.3f} V/m")

fw.show_cones(X, Y, Z, Ex, Ey, Ez, step=8, normalise=True,
              label="|<b>E</b>|", unit="V/m",
              title="E = -grad V for a positive point charge")

# --- self-check (leave this alone) ---
fw.check_close("|E| = Q/(4 pi eps0 r^2)", E_mag, k_e * Q / r_masked**2,
               rtol=0.05, where=outside)
fw.check("E points outward at (1,0,0)", Ex[-1 - 15, c, c] > 0)
```

:::{admonition} Solution — Task 7
:class: dropdown

```python
dVdx, dVdy, dVdz = np.gradient(V, dx, dy, dz)
Ex, Ey, Ez = -dVdx, -dVdy, -dVdz
E_mag = np.sqrt(Ex**2 + Ey**2 + Ez**2)
```
:::

:::{admonition} Why bother with $V$ at all?
:class: tip

$V$ is a scalar: one number per point, no direction to keep track of. $\boldsymbol{E}$ is a vector: three. Anything you can do once on $V$ and then differentiate is cheaper — in arithmetic and in bookkeeping — than doing it three times on $\boldsymbol{E}$.

Part 4 is the first payoff, and it is the reason the potential is worth defining in the first place.
:::

---

## Part 4 — Two sources: superposition

One charge is symmetric enough to be boring. Put down two:

$$ V_{\text{total}} = \frac{1}{4\pi\varepsilon_0}\left(\frac{Q_1}{r_1} + \frac{Q_2}{r_2}\right) $$

**Superposition** for the potential is nothing more than adding two numbers at every point, because $V$ is a scalar. Adding the two *fields* instead would mean a vector sum at every point in the cube.

Since $\nabla$ is a linear operator, $-\nabla(V_1 + V_2) = \boldsymbol{E}_1 + \boldsymbol{E}_2$ exactly. So the efficient route is: **add the potentials, then take one gradient at the very end.** Nothing is lost.

### Task 8 — build a dipole

```{code-cell} ipython3
# Distances to the two charges. +Q sits at x = +d/2, -Q at x = -d/2 -- the
# same placement Task 9 will give the current source and sink, so the two
# pictures can be laid side by side. The guard only trips if a grid point
# lands exactly on a charge; at n = 61 none does, so nothing is masked here
# and you see the full field. Raise it if you change the grid.
d_sep = 1.0                               # charge separation [m]
r_plus = np.where(distance_to(X, Y, Z, +d_sep/2, 0.0, 0.0) < 0.01, np.nan,
                  distance_to(X, Y, Z, +d_sep/2, 0.0, 0.0))
r_minus = np.where(distance_to(X, Y, Z, -d_sep/2, 0.0, 0.0) < 0.01, np.nan,
                   distance_to(X, Y, Z, -d_sep/2, 0.0, 0.0))

# Task 8 -- two blanks.
V_dip = ___                               # superpose: +Q over r_plus, -Q over r_minus
Ex_d, Ey_d, Ez_d = ___                    # ONE gradient of the sum, negated

# --- given: the z = 0 plane, potential as colour, field as streamlines ---
fw.show_field_slice(X, Y, Z, Ex_d, Ey_d, background=V_dip,
                    title="Source and sink: potential (colour) and field lines",
                    label="$V$ [V]")
plt.show()

# --- self-check (leave this alone) ---
mid = np.abs(X) < 1e-9                    # the plane x = 0, halfway between them
fw.check_shape("V_dip", V_dip, X.shape)
fw.check("V = 0 on the mid-plane",
         np.nanmax(np.abs(V_dip[mid])) < 1e-6 * np.nanmax(np.abs(V_dip)))
fw.check("E on the mid-plane points from + to -", np.nanmean(Ex_d[mid]) < 0)
```

:::{admonition} Solution — Task 8
:class: dropdown

```python
V_dip = k_e * Q / r_plus + k_e * (-Q) / r_minus

dVx, dVy, dVz = np.gradient(V_dip, dx, dy, dz)
Ex_d, Ey_d, Ez_d = -dVx, -dVy, -dVz
```
:::

:::{admonition} Look at the mid-plane before you move on
:class: tip

At $x = 0$, the potential is **exactly zero**. Yet the field there is not zero at all: it is at its strongest, pointing straight from the positive charge to the negative one — here in the $-\hat{\boldsymbol{x}}$ direction, since $+Q$ sits on the right.

The field is the *slope* of the potential, not its value. A landscape can be at sea level and still be steep. Notice also what the picture shows about direction: the streamlines cross the coloured contours at right angles everywhere, which is Task 4's normality result showing up in a field you did not construct radially.
:::

### Far away, it is one object

Now the connection back to Part 1. Nothing about $V_{\text{dip}}$ is a series — it is two exact terms. But step far enough back and the two charges stop being resolvable, and what survives is a **truncation**.

Expand $1/r_\pm$ in powers of $d/r$ and add. The two leading terms are equal and opposite — the charges cancel, as they must, since the pair carries no net charge — and the first thing left is

$$ V \;\approx\; \frac{1}{4\pi\varepsilon_0}\frac{\boldsymbol{p}\cdot\hat{\boldsymbol{r}}}{r^{2}}, \qquad \boldsymbol{p} = Q d\,\hat{\boldsymbol{x}}, $$

the **dipole moment** $\boldsymbol{p}$ pointing from the negative charge to the positive one. Everything dropped is smaller by a further factor of $(d/r)^2$ — so this is Task 1's question again, asked of space instead of time: *how far away do you have to stand before one term is enough?*

```{code-cell} ipython3
# --- given: exact against the one-term far field, along the +x axis ---
p_mom = Q * d_sep                              # dipole moment [C m]
r_ff = np.logspace(np.log10(0.8), np.log10(60), 2000)
V_ex = k_e * Q * (1/np.abs(r_ff - d_sep/2) - 1/np.abs(r_ff + d_sep/2))
V_ff = k_e * p_mom / r_ff**2                   # p . r-hat = p on the axis
err_ff = np.abs(V_ff - V_ex) / np.abs(V_ex)

plt.figure(figsize=(5.8, 4.2))
plt.loglog(r_ff / d_sep, err_ff, "k", lw=1.6)
for tol, colour in ((0.10, "C1"), (0.01, "C2"), (0.001, "C3")):
    r_ok = r_ff[np.argmax(err_ff < tol)] / d_sep
    plt.axhline(tol, color=colour, lw=0.8, ls=":")
    plt.plot([r_ok], [tol], "o", color=colour, ms=5)
    print(f"  one term is good to {tol:6.1%} beyond r = {r_ok:5.1f} separations")
plt.xlabel("$r$ / separation $d$"); plt.ylabel("relative error of the one-term form")
plt.grid(alpha=0.3, which="both"); plt.title("How far is far?")
plt.show()

# --- self-check (leave this alone) ---
fw.check("the far-field error falls as (d/r)^2",
         np.isclose(np.polyfit(np.log(r_ff[r_ff > 10]), np.log(err_ff[r_ff > 10]), 1)[0],
                    -2.0, atol=0.05))
```

:::{admonition} The same question as the bouncing ball
:class: important

Two decades of accuracy cost about a factor of ten in distance: good to 10% at $1.6\,d$, to 1% at $5\,d$, to 0.1% at $16\,d$. That is the $(d/r)^2$ law, and $\sqrt{10} \approx 3.2$ is the factor between each pair.

Compare it with Task 1. There, "how many terms for 1%?" had the answer 88, and it grew as the ball became more elastic. Here the knob is not a term count but a *distance*, and the answer grows the closer you stand. In both cases the truncation is only as good as the regime, and in both cases you can find out which regime you are in by measuring rather than hoping.

This one term is why a compass works. A magnet has a complicated field close up; a metre away it is a dipole and nothing else, which is exactly why the Earth's field is worth writing as the single term you will meet in Task 11.
:::

The same object in three dimensions — positive and negative equipotential surfaces together, drawn transparent:

```{code-cell} ipython3
lobe = np.nanpercentile(np.abs(V_dip), 97)
fw.show_isosurfaces(X, Y, Z, np.nan_to_num(V_dip), levels=[-lobe, -lobe/3, lobe/3, lobe],
                    colorscale="RdBu", reversescale=True, opacity=0.3, label="V  [V]",
                    title="Equipotential surfaces of a dipole")
```

### Task 9 — the same mathematics, as a geophysical survey

Everything you just built was two charges in vacuum. Now change nothing about the mathematics and everything about the physics.

Drive a current $I$ into the ground through one electrode and take it out through another, a distance $a$ apart. In ground of resistivity $\rho$ the current spreads through the **lower half-space only** — air does not conduct — so each electrode contributes $\rho I/2\pi r$ rather than $\rho I / 4\pi r$, and superposition gives

$$ V(x,y,z) = \frac{\rho I}{2\pi}\left(\frac{1}{\lvert\boldsymbol{r}-\boldsymbol{a}/2\rvert} - \frac{1}{\lvert\boldsymbol{r}+\boldsymbol{a}/2\rvert}\right), \qquad z \ge 0 \ \text{(down into the ground)}. $$

The field follows as before, $\boldsymbol{E} = -\nabla V$, and Ohm's law in local form turns it into a **current density**:

$$ \boldsymbol{J} = \rho^{-1}\boldsymbol{E} = -\rho^{-1}\nabla V \quad [\text{A}/\text{m}^2]. $$

This is a real measurement — a DC resistivity survey, the workhorse of near-surface geophysics. Map it two ways: on the ground surface, where the electrodes are planted, and on a vertical section cut down between them.

:::{admonition} Careful — $\rho$ means something else here
:class: warning

In this task $\rho$ is the **electrical resistivity** in Ω·m. In Task 13 it will be a charge density in C/m³, written $\rho_v$ to keep them apart. The symbol is overloaded across the whole subject; the units tell you which is which.
:::

The ground is a half-space, so this needs its own grid: $x$ and $y$ still run $-L$ to $L$, but $z$ runs from $0$ (the surface) **downwards**, the Earth-science convention.

A real electrode is a metal stake, not a mathematical point: a conductor of some finite radius $r_{\text{el}}$, held at one potential over its whole surface. Model it that way — floor the distance at $r_{\text{el}}$ — and $1/r$ never blows up. Nothing is masked, no sample is thrown away, and every derivative below is taken on a field that is finite everywhere.

```{code-cell} ipython3
rho, I, a_sep = 100.0, 1.0, 1.0           # ohm.m, ampere, electrode spacing [m]
r_el = 0.12                               # electrode radius [m]

axis_g = np.linspace(-2.0, 2.0, 81)       # x and y, across the survey line
depth  = np.linspace(0.0, 2.0, 51)        # z, down into the ground
Xg, Yg, Zg = np.meshgrid(axis_g, axis_g, depth, indexing="ij")
dxg = axis_g[1] - axis_g[0]
dzg = depth[1] - depth[0]
print(f"dxg = {dxg:.3f} m,  dzg = {dzg:.3f} m   <- deliberately not equal")

def dist_to(x0):
    """Distance to an electrode at (x0, 0, 0), floored at its own radius."""
    return np.maximum(np.sqrt((Xg - x0)**2 + Yg**2 + Zg**2), r_el)

# Task 9 -- two blanks. This is Task 8 again, in different clothes.
#   V:  the formula above, source at x = +a_sep/2, sink at x = -a_sep/2.
#       dist_to floors the distance at the electrode radius, so there is
#       nothing to mask and nothing to nan_to_num.
#   J:  -grad(V)/rho. Pass dxg, dxg, dzg. On this grid z really is spaced
#       differently from x and y, and passing dxg three times costs 6.5% on
#       the current measured in the next cell -- enough to fail its check.

V_dc = ___
Jx, Jy, Jz = ___

# --- given: the survey, both panels on one colour scale and one colorbar ---
# plane="z" is the ground surface; plane="y" is the vertical section, where
# the in-plane components are (Jx, Jz), not (Jx, Jy).
vm = float(np.nanpercentile(np.abs(V_dc[:, :, 0]), 98))
fig, axes = plt.subplots(2, 1, figsize=(7.2, 9.2))
for ax_, comps, pl, ttl in ((axes[0], (Jx, Jy), "z", "a) ground surface, $z=0$"),
                            (axes[1], (Jx, Jz), "y", "b) vertical section, $y=0$")):
    _, cf = fw.show_field_slice(Xg, Yg, Zg, *comps, background=V_dc, ax=ax_,
                                plane=pl, vmin=-vm, vmax=vm, colorbar=False,
                                density=1.2, title=ttl)
axes[1].invert_yaxis()                    # depth increases downwards
fig.colorbar(cf, ax=axes, label="$V$ [V]", fraction=0.05, pad=0.03)
plt.show()

# --- self-check (leave this alone) ---
mid_dc = np.abs(Xg) < 1e-9
fw.check("V is finite everywhere -- no holes in the model",
         np.all(np.isfinite(V_dc)) and np.all(np.isfinite(Jx)))
fw.check("V = 0 on the mid-plane between the electrodes",
         np.nanmax(np.abs(V_dc[mid_dc])) < 1e-6 * np.nanmax(np.abs(V_dc)))
fw.check("current flows from the source towards the sink at the surface",
         np.nanmean(Jx[mid_dc]) < 0)
```

:::{admonition} Solution — Task 9
:class: dropdown

```python
V_dc = rho * I / (2*np.pi) * (1/dist_to(+a_sep/2) - 1/dist_to(-a_sep/2))

gVx, gVy, gVz = np.gradient(V_dc, dxg, dxg, dzg)
Jx, Jy, Jz = -gVx/rho, -gVy/rho, -gVz/rho
```

One presentation point worth stealing for your own figures: `show_field_slice` returns `(ax, cf)`, so passing `colorbar=False` on both panels and handing the mappable `cf` to `fig.colorbar(..., ax=axes)` draws **one** bar beside the pair. Two bars carrying identical numbers is clutter, and it invites the reader to think the scales differ.
:::

Now use the field as an instrument. *All* the current injected at one electrode has to cross any closed surface you draw around it — there is nowhere else for it to go. Test that.

```{code-cell} ipython3
# The five faces of a box buried in the ground around one electrode. The top
# face is deliberately absent: it lies in the surface z = 0, where no current
# crosses into the air, so its contribution is zero by physics.
def buried_box_current(xc, hw=0.3):
    i0 = int(np.argmin(np.abs(axis_g - (xc - hw))))
    i1 = int(np.argmin(np.abs(axis_g - (xc + hw))))
    j0 = int(np.argmin(np.abs(axis_g + hw)))
    j1 = int(np.argmin(np.abs(axis_g - hw)))
    k1 = int(np.argmin(np.abs(depth - hw)))
    sx, sy, sz = slice(i0, i1+1), slice(j0, j1+1), slice(0, k1+1)
    return (fw.area_integral(Jx[i1, sy, sz], dxg, dzg) - fw.area_integral(Jx[i0, sy, sz], dxg, dzg)
          + fw.area_integral(Jy[sx, j1, sz], dxg, dzg) - fw.area_integral(Jy[sx, j0, sz], dxg, dzg)
          + fw.area_integral(Jz[sx, sy, k1], dxg, dxg))

for xc, name in ((+a_sep/2, "source"), (-a_sep/2, "sink")):
    print(f"current out of a box around the {name:6s}: {buried_box_current(xc):+7.4f} A")
print(f"                            injected: {I:+7.4f} A")

# --- self-check (leave this alone) ---
fw.check_scalar("box around the source carries I", buried_box_current(+a_sep/2), I, rtol=0.01, unit=" A")
fw.check_scalar("box around the sink carries -I", buried_box_current(-a_sep/2), -I, rtol=0.01, unit=" A")
```

:::{admonition} Why five faces and not six?
:class: important

The box is closed by the ground surface itself. Air does not conduct, so $J_z = 0$ at $z=0$ — a **boundary condition**, true by physics, not something to be measured.

It is worth seeing what happens if you do try to measure it. `np.gradient` has no neighbour above $z=0$, so it falls back to a one-sided difference there — and reports a spurious $J_z$ averaging $+0.25$ A/m² over the top of the box, current apparently sinking in from the air. The outward normal on that face is $-\hat{\boldsymbol{z}}$, so it enters the sum as $-0.088$ A and drags the box from $1.003$ A down to $0.915$ A: an **8.5% error**, on a result that is otherwise good to 0.3%.

The lesson generalises well beyond this lab: **where you know a boundary condition exactly, impose it — do not ask a finite-difference stencil to rediscover it.** Numerical derivatives are least trustworthy exactly where your domain stops.
:::

---

:::{admonition} End of session 1
:class: note

Parts 1–4 are the gradient, and that is where the first afternoon ends. **Part 5 onwards needs the divergence**, which is lectured next — come back to it in the following session, or read ahead if you are curious.
:::

---

## Part 5 — Divergence: is anything being created here?

The gradient took a scalar and returned a vector. The divergence goes the other way — hand it a vector field, get back a scalar:

$$ \nabla\cdot\boldsymbol{A} \;=\; \lim_{\Delta V \to 0}\frac{1}{\Delta V}\oint_S \boldsymbol{A}\cdot\hat{\boldsymbol{n}}\,dS \;=\; \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z} $$

Read the definition on the left, not the formula on the right: **treat $\boldsymbol{A}$ as the velocity of a fluid**, put a small box anywhere, and measure the net outflow through its walls per unit volume.

| $\nabla\cdot\boldsymbol{A}$ | Name | Picture |
| :---: | :--- | :--- |
| $> 0$ | **source** | a tap — more leaves than arrives |
| $< 0$ | **sink** | a drain — more arrives than leaves |
| $= 0$ | **solenoidal** | whatever flows in, flows out |

### Task 10 — the operator, and where it is measured from

The operator itself is three lines, and you are given them. One derivative along one axis per component: `np.gradient(Ax, dx, axis=0)` returns $\partial A_x/\partial x$ and nothing else, where asking for all three and discarding two would cost three times the memory. The cross terms are not part of a divergence.

**The question is the one the definition raises.** Flux per unit volume is measured around *a point* — so does the answer depend on which point you call the origin? Take the outward flow $\boldsymbol{A} = \boldsymbol{r}$, whose divergence you can do on paper: $1+1+1 = 3$. Now shift the whole field so it streams out of $(0.8, -0.4, 0.3)$ instead. Predict the divergence before you compute it.

```{code-cell} ipython3
# --- given ---
def divergence(Ax, Ay, Az, dx, dy, dz):
    return (np.gradient(Ax, dx, axis=0)
            + np.gradient(Ay, dy, axis=1)
            + np.gradient(Az, dz, axis=2))

# Task 10 -- two blanks. The same outward flow, seen from somewhere else.
x0, y0, z0 = 0.8, -0.4, 0.3
Sx, Sy, Sz = ___                          # the field r - r0, as three arrays
div_shifted = ___                         # its divergence

# --- self-check (leave this alone) ---
fw.check_close("div of the position vector = 3",
               divergence(X, Y, Z, dx, dy, dz), 3.0, rtol=1e-6)
fw.check_close("...and 3 again when the source is moved",
               div_shifted, 3.0, rtol=1e-6)
fw.check("the shifted field really is different from the original",
         not np.allclose(Sx, X))
```

:::{admonition} Solution — Task 10
:class: dropdown

```python
Sx, Sy, Sz = X - x0, Y - y0, Z - z0
div_shifted = divergence(Sx, Sy, Sz, dx, dy, dz)
```
:::

:::{admonition} Why it had to be 3 either way
:class: tip

Moving the source changed every arrow in the box, and changed the divergence nowhere. Differentiation kills the constant: $\partial(x - x_0)/\partial x = 1$ whatever $x_0$ is.

That is worth more than it looks. The divergence is a **local** quantity — it is built from a limit taken around one point, so it can only know about the field in a shrinking neighbourhood of that point, and nothing about where you chose to put your axes. Every operator in this course has that property, and it is what lets you write $\nabla\cdot\boldsymbol{E} = \rho_v/\varepsilon_0$ as a statement about *places* rather than about coordinate systems.
:::

### Task 11 — the only incompressible radial flow

A first use of the operator. Water of constant density flows outward from a source at the origin. Away from that source nothing is created or destroyed, so the flow must be **incompressible**:

$$ \nabla\cdot\boldsymbol{v} = 0 \qquad \text{for } r \neq 0. $$

Constant density and a point source force the flow to be radial, $\boldsymbol{v} = f(r)\,\boldsymbol{r}$, and incompressibility then pins $f$ down completely:

$$ \nabla\cdot\boldsymbol{v} = 3f(r) + r\frac{df}{dr} = 0 \qquad\Longrightarrow\qquad f(r) = \frac{A}{r^{3}}. $$

Do not take that on trust — find it. Try four candidates and let the divergence pick.

```{code-cell} ipython3
# The measure to report, once, so the loop below reads as physics:
#
#       |div v| / (|v| / r),  median over the test band
#
# |v|/r is the natural size of a derivative of v, so the ratio is a pure
# number -- 1 means "as large as a derivative of this field could be".

r_safe = np.where(r < 0.3, np.nan, r)
band_i = interior & (r > 0.6) & (r < 1.6)

# Task 11 -- three blanks, inside the loop.
results = {}
for name, f_r in [("const", np.ones_like(r_safe)),
                  ("1/r^2", 1/r_safe**2),
                  ("1/r^3", 1/r_safe**3),
                  ("1/r^4", 1/r_safe**4)]:
    vx, vy, vz = ___                      # v = f(r) * (X, Y, Z): three arrays
    dv = ___                              # its divergence (nan_to_num each part)
    scale = ___                           # |v|/r AT THE BAND POINTS -- index it
                                          # with [band_i], so it comes out 1-D
                                          # and the same length as dv[band_i]

    # --- given ---
    results[name] = np.nanmedian(np.abs(dv[band_i]) / scale)
    print(f"  f = {name:6s}:  median |div v| / (|v|/r) = {results[name]:8.2%}")

# --- self-check (leave this alone) ---
fw.check(f"scale is one value per band point ({np.shape(scale)} vs "
         f"{np.shape(dv[band_i])})", np.shape(scale) == np.shape(dv[band_i]),
         "index it with [band_i] -- a whole-grid array or a single median "
         "both change the statistic being reported")
fw.check(f"1/r^3 is the divergence-free one ({results['1/r^3']:.2%})",
         results["1/r^3"] < 0.05)
fw.check("...and the other three are not",
         min(results[k] for k in ("const", "1/r^2", "1/r^4")) > 0.5)
fw.check(f"f = const reproduces Task 10's div(r) = 3 ({results['const']:.2%})",
         np.isclose(results["const"], 3.0, rtol=1e-3))
```

:::{admonition} Solution — Task 11
:class: dropdown

```python
    vx, vy, vz = f_r*X, f_r*Y, f_r*Z
    dv = divergence(*(np.nan_to_num(q) for q in (vx, vy, vz)), dx, dy, dz)
    scale = (np.sqrt(vx**2 + vy**2 + vz**2) / r_safe)[band_i]
```
:::

:::{admonition} Where the inverse-square law comes from
:class: important

One candidate sits at 300%, two at almost exactly 100%, and one at 0.66%. Only $f = A/r^{3}$ survives, exactly as the algebra says.

The 300% is not an accident, and it is worth recognising: for $f = \text{const}$ the field *is* the position vector, $\boldsymbol{v} = \boldsymbol{r}$, whose divergence you measured in Task 10 as exactly 3 — while $\lvert\boldsymbol{v}\rvert/r = 1$, so the ratio has to be 3. Note also what the surviving case means for the field itself:

$$ \boldsymbol{v} = \frac{A}{r^{3}}\boldsymbol{r} = \frac{A}{r^{2}}\,\hat{\boldsymbol{r}}. $$

**That is the same $1/r^{2}$ you have been working with since Task 6.** Here it was not assumed, and no charge was mentioned: it fell out of "nothing is created away from the source" plus "space is three-dimensional". The surface of a sphere grows as $r^{2}$, so a fixed amount of stuff crossing it must thin as $1/r^{2}$.

Coulomb's law, Newton's gravity and this water all share an exponent for that one geometric reason.
:::

### Task 11, continued — a field with no source anywhere

Notice the small print on that result: $\nabla\cdot\boldsymbol{v} = 0$ **for $r \neq 0$**. The origin is excluded, and it has to be — that is where the water is injected. Put a closed surface around it and you would find the tap.

Now a field with no such exception. To first order the Earth's magnetic field is a **dipole**: a north and a south pole so close together that they coincide. With dipole moment $\boldsymbol{m}$,

$$ \boldsymbol{B} = \frac{3\boldsymbol{r}\,(\boldsymbol{r}\cdot\boldsymbol{m}) - r^{2}\boldsymbol{m}}{r^{5}}. $$

Take $\boldsymbol{m} = \hat{\boldsymbol{z}}$ on the cube of Part 2, where $z$ points up, and measure the divergence with the same function.

(The Earth's own moment points roughly geographic *south*, which is why the magnetic pole in the Arctic is magnetically a **south** pole and pulls the north end of a compass needle towards it. Reversing $\boldsymbol{m}$ reverses every arrow below and changes nothing at all about $\nabla\cdot\boldsymbol{B}$, which is the point of the task.)

```{code-cell} ipython3
# Task 11, continued -- fill in the three components.
#   With m = z-hat, the dot product r . m is simply Z.
#   Careful with the second term: it appears only in the z-component.

r_dot_m = Z
Bx = ___
By = ___
Bz = ___

div_B = divergence(np.nan_to_num(Bx), np.nan_to_num(By), np.nan_to_num(Bz), dx, dy, dz)

# --- given: the same scale-free measure as above ---
B_mag = np.sqrt(Bx**2 + By**2 + Bz**2)
print(f"  dipole B : median |div B| / (|B|/r) = "
      f"{np.nanmedian(np.abs(div_B[band_i]) / (B_mag/r_safe)[band_i]):8.2%}")

# --- self-check (leave this alone) ---
fw.check("B is divergence-free",
         np.nanmedian(np.abs(div_B[band_i]) / (B_mag/r_safe)[band_i]) < 0.05)
fw.check("B is not simply radial (it has a north and a south)",
         np.nanmin((Bx*X + By*Y + Bz*Z)[band_i]) < 0)
```

:::{admonition} Solution — Task 11, continued
:class: dropdown

```python
Bx = 3*X*r_dot_m / r_safe**5
By = 3*Y*r_dot_m / r_safe**5
Bz = (3*Z*r_dot_m - r_safe**2) / r_safe**5
```
:::

:::{admonition} No magnetic monopoles
:class: important

Both fields are divergence-free where you measured, but they are not the same statement.

The water needed an exclusion: $\nabla\cdot\boldsymbol{v} = 0$ *away from the origin*, because the origin is a tap. The dipole needs none — $\nabla\cdot\boldsymbol{B} = 0$ holds **everywhere in space, including at the source itself**. There is no point you could exclude and find a magnet leaking field the way the tap leaks water. That is one of Maxwell's equations, and it says magnetic monopoles do not exist: field lines of $\boldsymbol{B}$ never begin and never end, they only close on themselves.

Two footnotes on the numbers. Both cells report the same scale-free measure, so the numbers are directly comparable: the dipole's 1.8% is worse than the radial flow's 0.66% — not because the physics is shakier but because $\boldsymbol{B}$ falls off as $1/r^{3}$ instead of $1/r^{2}$, so a centred difference has more curvature to miss. Part 6 pushes the "no exception" claim far below that 2%, by putting a closed surface around the dipole instead of differentiating it.

And the second check is worth a moment: $\boldsymbol{B}\cdot\boldsymbol{r}$ goes negative somewhere, which the outward flow of Task 11 never does. The dipole points *inward* over part of space — it returns. That is what "closes on itself" looks like in a number.
:::

### Task 12 — three flows

Three velocity fields. For each: **sketch it in your head, predict the sign of the divergence, then measure.** Write the predictions down first — the point of this task is the gap between intuition and the answer.

| | Field $\boldsymbol{A}$ | What it looks like |
| :---: | :--- | :--- |
| **(a)** | $x\,\hat{\boldsymbol{x}} + y\,\hat{\boldsymbol{y}} + z\,\hat{\boldsymbol{z}}$ | flow rushing outward in all directions |
| **(b)** | $-y\,\hat{\boldsymbol{x}} + x\,\hat{\boldsymbol{y}}$ | fluid rotating about the $z$-axis |
| **(c)** | $x\,\hat{\boldsymbol{x}} - y\,\hat{\boldsymbol{y}}$ | stretching along $x$, squeezing along $y$ |

```{code-cell} ipython3
# Commit to your predictions BEFORE the next cell: +1 for a source, -1 for a
# sink, 0 for solenoidal. The next cell scores them.
predictions = {"a": ___, "b": ___, "c": ___}
```

```{code-cell} ipython3
# Task 12 -- six blanks: three fields, three divergences.
zero = np.zeros_like(X)
Aa = ___                                  # (a) outward flow, as a triple
Ab = ___                                  # (b) rotation about z
Ac = ___                                  # (c) stretch in x, squeeze in y

div_a = ___
div_b = ___
div_c = ___

# --- given: the three side by side, one shared scale, one colorbar ---
for name, d in [("(a) outward flow", div_a), ("(b) rotation", div_b),
                ("(c) shear", div_c)]:
    print(f"{name:20s} div = {d.mean():+.3f}")

fig, axes = plt.subplots(1, 3, figsize=(16, 4.6))
for ax_, (name, A, d) in zip(axes, [("(a) outward flow", Aa, div_a),
                                    ("(b) rotation", Ab, div_b),
                                    ("(c) shear flow", Ac, div_c)]):
    fw.show_field_slice(X, Y, Z, *A[:2], background=d, ax=ax_, density=1.1,
                        vmin=-3, vmax=3, colorbar=(ax_ is axes[-1]),
                        label=r"$\nabla\cdot\boldsymbol{A}$  [s$^{-1}$]", title=name)
plt.tight_layout()
plt.show()
# Look hard at (b) and (c) before reading the note below: both come out a
# uniform zero, and they get there for completely different reasons.

# --- self-check (leave this alone) ---
# (a) has a non-zero answer, so a relative test works. (b) and (c) are
# exactly zero, which nothing can be measured *relative* to -- those get an
# absolute tolerance instead.
fw.check_close("(a) div = 3", div_a, 3.0, rtol=1e-6)
fw.check_abs("(b) div = 0 (rotation)", div_b, atol=1e-9)
fw.check_abs("(c) div = 0 (shear)", div_c, atol=1e-9)

for key, measured in (("a", div_a), ("b", div_b), ("c", div_c)):
    sign = int(np.sign(np.round(measured.mean(), 6)))
    verdict = "as predicted" if predictions[key] == sign else "NOT what you predicted"
    print(f"  ({key}) you said {predictions[key]:+d}, measured {sign:+d}  --  {verdict}")
```

:::{admonition} Solution — Task 12
:class: dropdown

```python
Aa = (X, Y, Z)
Ab = (-Y, X, zero)
Ac = (X, -Y, zero)

div_a = divergence(*Aa, dx, dy, dz)
div_b = divergence(*Ab, dx, dy, dz)
div_c = divergence(*Ac, dx, dy, dz)
```
:::

:::{admonition} Field (c) is the one that costs marks
:class: warning

Along the $x$-axis, field (c) rushes outward. It looks like a source. It is not:

$$ \nabla\cdot\boldsymbol{A} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(-y) = 1 - 1 = 0 $$

Put a box at the origin: fluid pours out through the left and right walls and in through the top and bottom at exactly the same rate. The parcel changes **shape**, never **volume**.

*Arrows pointing apart* is not divergence. Outflow in one direction can be cancelled exactly by inflow in another — and in Task 14 you will put a closed surface around this field and measure that cancellation, rather than take it on the strength of this paragraph.
:::

### Task 13 — the divergence as a charge detector

Gauss's law, for a field in vacuum, says

$$ \nabla\cdot\boldsymbol{E} = \frac{\rho_v}{\varepsilon_0} $$

which is a strong claim: **the divergence of $\boldsymbol{E}$ at a point tells you the charge density at that point and nothing else.** Wherever there is no charge, $\boldsymbol{E}$ is solenoidal, however dramatically its arrows spread out.

Test that pointwise on a real source. Not a point charge — that is an idealisation with infinite density at one location, and no grid can hold it. Take instead a charge **smeared over a finite blob**, which is what any actual charged object is:

$$ \rho_v(r) = \rho_{v0}\,e^{-r^{2}/a^{2}}, \qquad \rho_{v0} = 10^{-9}\ \text{C/m}^3, \qquad a = 0.5\ \text{m} $$

Here $a$ is the **width of the blob**. In Task 9 the same letter was an electrode separation — the second overloaded symbol on this page, after $\rho$. The code keeps them apart as `a` and `a_sep`; your algebra has only the context to go on.

Integrating that over a sphere of radius $r$ gives the charge it encloses (bookwork — you do not need to do the integral now):

$$ Q_{\text{enc}}(r) = \int_0^{r}\!\rho_v\,4\pi r'^{2}\,dr' = 4\pi\rho_{v0}\left[\frac{a^{3}\sqrt{\pi}}{4}\operatorname{erf}\!\left(\frac{r}{a}\right) - \frac{a^{2}r}{2}e^{-r^{2}/a^{2}}\right] $$

and Gauss's law, $E_r = Q_{\text{enc}}/4\pi\varepsilon_0r^{2}$, then gives the field — the $4\pi$ cancelling:

$$ E_r(r) = \frac{\rho_{v0}}{\varepsilon_0 r^{2}}\left[\frac{a^{3}\sqrt{\pi}}{4}\operatorname{erf}\!\left(\frac{r}{a}\right) - \frac{a^{2}r}{2}e^{-r^{2}/a^{2}}\right] $$

One sanity check: near the centre $Q_{\text{enc}}$ grows as $r^{3}$ while the surface grows as $r^{2}$, so $E_r \to \rho_{v0} r/3\varepsilon_0$ — zero at the centre, rising linearly, peaking at $r \approx a$.

```{code-cell} ipython3
from scipy.special import erf

a, rho_v0 = 0.5, 1e-9

# --- given: the charge density, and the field Gauss's law gives it ---
# (Transcribing the erf expression teaches nothing; deciding what to do with
# it does. The two bracketed terms nearly cancel for r << a, so the closed
# form loses accuracy below r ~ 1e-6 m; on this grid the only such sample is
# the origin, where the r-hat components are zero anyway.)
rho_v = rho_v0 * np.exp(-r**2 / a**2)
E_r = rho_v0 / (epsilon_0 * rs**2) * (
    (a**3 * np.sqrt(np.pi) / 4) * erf(rs / a) - (a**2 * rs / 2) * np.exp(-rs**2 / a**2)
)

# Task 13 -- two blanks.
#   E_r is a radial MAGNITUDE. Give it a direction, then differentiate.
Ex_b, Ey_b, Ez_b = ___                    # components along (rhx, rhy, rhz)
div_blob = ___                            # your Task 10 operator

# --- given: the two pictures, forced onto one scale so they are comparable ---
hi = float(np.nanmax(rho_v / epsilon_0))
units = r"[V m$^{-2}$]"
fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))
fw.show_scalar_slice(X, Y, Z, div_blob, ax=axes[0], cmap="magma", label=units,
                     vmin=0, vmax=hi, title=r"measured $\nabla\cdot\boldsymbol{E}$")
fw.show_scalar_slice(X, Y, Z, rho_v / epsilon_0, ax=axes[1], cmap="magma", label=units,
                     vmin=0, vmax=hi, title=r"actual $\rho_v/\varepsilon_0$")
plt.tight_layout()
plt.show()

print(f"peak of rho_v/eps0  : {np.nanmax(rho_v/epsilon_0):8.2f}")
print(f"peak of measured div: {np.nanmax(div_blob):8.2f}")

# --- self-check (leave this alone) ---
peak = np.nanmax(rho_v / epsilon_0)
_e = np.abs(div_blob[interior] - (rho_v / epsilon_0)[interior]) / peak
cart_worst, cart_median = float(_e.max()), float(np.median(_e))
fw.check(f"div E = rho_v/eps0 pointwise (worst {cart_worst:.2%} of peak)",
         cart_worst < 0.05, "check the component construction Ex_b = E_r * rhx")
```

:::{admonition} Solution — Task 13
:class: dropdown

```python
Ex_b, Ey_b, Ez_b = E_r * rhx, E_r * rhy, E_r * rhz
div_blob = divergence(Ex_b, Ey_b, Ez_b, dx, dy, dz)
```
:::

:::{admonition} What you just did
:class: important

The two pictures are the same picture. You never told the code where the charge was — you handed it a *field*, differentiated it, and the charge distribution came back out.

Notice where the divergence vanishes: everywhere outside the blob, where the field is still large and still spreading. **Strong field, zero divergence** — the two ideas are unrelated.
:::

### The same operator, a different formula

Everything so far used the Cartesian formula, because `np.gradient` differentiates along array axes. But the divergence *is* flux per unit volume — a physical quantity, which cannot depend on the axes you happened to choose. Only the formula changes:

| | Gradient $\nabla T$ | Divergence $\nabla\cdot\boldsymbol{A}$ |
| :--- | :--- | :--- |
| Cartesian $(x,y,z)$ | $\dfrac{\partial T}{\partial x}\hat{\boldsymbol{x}} + \dfrac{\partial T}{\partial y}\hat{\boldsymbol{y}} + \dfrac{\partial T}{\partial z}\hat{\boldsymbol{z}}$ | $\dfrac{\partial A_x}{\partial x} + \dfrac{\partial A_y}{\partial y} + \dfrac{\partial A_z}{\partial z}$ |
| Cylindrical $(\varrho,\phi,z)$ | $\dfrac{\partial T}{\partial \varrho}\hat{\boldsymbol{\varrho}} + \dfrac{1}{\varrho}\dfrac{\partial T}{\partial \phi}\hat{\boldsymbol{\phi}} + \dfrac{\partial T}{\partial z}\hat{\boldsymbol{z}}$ | $\dfrac{1}{\varrho}\dfrac{\partial (\varrho v_\varrho)}{\partial \varrho} + \dfrac{1}{\varrho}\dfrac{\partial v_\phi}{\partial \phi} + \dfrac{\partial v_z}{\partial z}$ |
| Spherical $(r,\phi,\theta)$ | $\dfrac{\partial T}{\partial r}\hat{\boldsymbol{r}} + \dfrac{1}{r}\dfrac{\partial T}{\partial \theta}\hat{\boldsymbol{\theta}} + \dfrac{1}{r\sin\theta}\dfrac{\partial T}{\partial \phi}\hat{\boldsymbol{\phi}}$ | $\dfrac{1}{r^{2}}\dfrac{\partial (r^{2}v_r)}{\partial r} + \dfrac{1}{r\sin\theta}\dfrac{\partial (v_\theta \sin\theta)}{\partial \theta} + \dfrac{1}{r\sin\theta}\dfrac{\partial v_\phi}{\partial \phi}$ |

Cylindrical $\varrho=\sqrt{x^2+y^2}$ is the distance from the $z$-axis; spherical $r=\sqrt{x^2+y^2+z^2}$, used throughout this lab, is the distance from the origin. They are written differently precisely to keep them apart.

One reading note: the spherical coordinates are *named* $(r,\phi,\theta)$, but the terms in the row above are listed $r$, then $\theta$, then $\phi$ — the order in which the scale factors $(1,\ r,\ r\sin\theta)$ are derived. A sum does not care about the order of its terms; only about which ones are in it.

Both fields you have built are spherically symmetric — $\boldsymbol{E} = E_r(r)\,\hat{\boldsymbol{r}}$, with no $\theta$ or $\phi$ dependence — so two of the three spherical terms vanish and the divergence collapses to one ordinary derivative along one line:

$$ \nabla\cdot\boldsymbol{E} \;=\; \frac{1}{r^{2}}\frac{d}{dr}\!\left(r^{2}E_r\right) $$

```{code-cell} ipython3
dr = 0.005
r_line = np.arange(0.05, 2.0 + dr, dr)          # one radial line, not a cube

# the same two fields as before, as functions of r alone
E_R_blob = rho_v0 / (epsilon_0 * r_line**2) * (
    (a**3 * np.sqrt(np.pi) / 4) * erf(r_line / a)
    - (a**2 * r_line / 2) * np.exp(-r_line**2 / a**2))
E_r_point = k_e * Q / r_line**2

div_blob_sph = np.gradient(r_line**2 * E_R_blob, dr) / r_line**2
div_point_sph = np.gradient(r_line**2 * E_r_point, dr) / r_line**2

rho_v_line = rho_v0 * np.exp(-r_line**2 / a**2)

# --- given: the radial profile Task 13 asserted but never drew ---
Q_total = np.pi**1.5 * rho_v0 * a**3                  # all of the blob's charge
plt.figure(figsize=(5.8, 4.2))
plt.plot(r_line, E_R_blob, "k", lw=1.8, label="$E_r(r)$, exact")
plt.plot(r_line, rho_v0 * r_line / (3 * epsilon_0), "C1--", lw=1.2,
         label=r"small $r$:  $\rho_{v0}r/3\varepsilon_0$")
plt.plot(r_line, Q_total / (4 * np.pi * epsilon_0 * r_line**2), "C2:", lw=1.4,
         label=r"large $r$:  $Q/4\pi\varepsilon_0 r^2$")
plt.axvline(a, color="C0", lw=1, alpha=0.6)
plt.annotate("$r = a$", (a, 1.12 * E_R_blob.max()), color="C0", ha="left")
plt.xlabel("$r$ [m]"); plt.ylabel(r"$E_r$ [V m$^{-1}$]")
plt.ylim(0, 1.25 * E_R_blob.max()); plt.grid(alpha=0.3); plt.legend(fontsize=8)
plt.title("The blob's field: linear inside, inverse-square outside")
plt.show()

err_sph = np.abs(div_blob_sph - rho_v_line / epsilon_0)[1:-1] / np.max(rho_v_line / epsilon_0)
print(f"blob : {r_line.size} samples on a line vs {X.size:,} in the cube")
print(f"       worst error {err_sph.max():.3%} of peak, median {np.median(err_sph):.4%}")
print(f"       Cartesian, from Task 13: {cart_worst:.3%} and {cart_median:.4%}")
print(f"point: r^2 E_r varies by {np.ptp(r_line**2 * E_r_point):.1e} over the whole line")
print(f"       max |div E| = {np.abs(div_point_sph).max():.1e}  (round-off, not physics)")
```

:::{admonition} Why anyone bothers with curvilinear coordinates
:class: important

Same field, same operator, same answer — from a few hundred samples on a line instead of a quarter of a million in a cube, and several times more accurately.

For the point charge the gain is not accuracy but certainty. $r^{2}E_r = Q/4\pi\varepsilon_0$ is a **constant**, so its derivative is *analytically* zero for every $r>0$ — not "1% of something", but zero, by one line of algebra. What the cell prints is only how well double precision can subtract two equal numbers: $10^{-13}$ or so, and exactly $0$ if the arithmetic happens to cancel. Change `dr` and that last digit will move; the algebra will not. Cartesian coordinates could never have got past "the divergence is small".

Match your coordinates to the symmetry of the source and three noisy numerical derivatives collapse into one line of algebra. That is what the second and third rows of the table are for.
:::

---

## Part 6 — Flux, and the divergence theorem

Part 5 used the *differential* form of Gauss's law, which compares two numbers at one point. The *integral* form connects a volume to the surface enclosing it:

$$ \oint_S \boldsymbol{E}\cdot\hat{\boldsymbol{n}}\,dS \;=\; \int_{\mathcal{D}} \nabla\cdot\boldsymbol{E}\;dV \;=\; \frac{Q_{\text{enc}}}{\varepsilon_0} $$

with $S$ the closed surface, $\hat{\boldsymbol{n}}$ its outward unit normal, and $\mathcal{D}$ the volume it encloses.

The first equality is the **divergence theorem** — pure vector calculus, true for any well-behaved field. The second is the physics. Together: measuring $\boldsymbol{E}$ on a closed surface tells you how much charge is inside, and nothing about how it is arranged, or about any charge outside.

Take $S$ to be a cube of half-width $h$ centred on the origin, faces on grid planes. On the $+x$ face the outward normal is $+\hat{\boldsymbol{x}}$, so it contributes $\int\!\!\int E_x\,dy\,dz$; on the $-x$ face the normal is $-\hat{\boldsymbol{x}}$ and the same integral enters negatively. Six faces, three pairs.

### Task 14 — close the surface

```{code-cell} ipython3
# `fw.area_integral(F2, da, db)` integrates a 2-D array over the face it
# spans; `fw.volume_integral(F3, dx, dy, dz)` does the same over a box.
# `fw.box_indices(X, h)` gives the index range of the cube |x|,|y|,|z| <= h.
#
# The x pair is written for you; the pattern is one row per axis:
#
#     face pair   outward samples   inward samples    spacings
#     x           Ax[i1, s, s]      Ax[i0, s, s]      dy, dz
#     y           Ay[s, i1, s]      Ay[s, i0, s]      dx, dz
#     z           Az[s, s, i1]      Az[s, s, i0]      dx, dy
#
# The axis you pin to i0/i1 is the axis whose spacing you leave out.
# NOTE: this closes over X, dx, dy, dz from the cell above -- it is tied to
# this grid, not a general-purpose function.

def closed_box_flux(Ax, Ay, Az, half_width):
    """Net outward flux through the cube |x|,|y|,|z| <= half_width."""
    i0, i1 = fw.box_indices(X, half_width)
    s = slice(i0, i1 + 1)
    flux_x = (fw.area_integral(Ax[i1, s, s], dy, dz)
              - fw.area_integral(Ax[i0, s, s], dy, dz))
    flux_y = ___
    flux_z = ___
    return flux_x + flux_y + flux_z


# --- given: three routes to the same number, and the Task 12 arbiter ---
# Finish closed_box_flux above; everything below is written for you.
flux_1m = closed_box_flux(Ex_b, Ey_b, Ez_b, 1.0)

print(f"{'h [m]':>6} {'surface':>12} {'volume':>12} {'Q_enc/eps0':>12}")
for h in (0.6, 1.0, 1.4):
    i0, i1 = fw.box_indices(X, h)
    s_ = slice(i0, i1 + 1)
    surf = closed_box_flux(Ex_b, Ey_b, Ez_b, h)
    vol = fw.volume_integral(div_blob[s_, s_, s_], dx, dy, dz)
    qenc = fw.volume_integral(rho_v[s_, s_, s_], dx, dy, dz) / epsilon_0
    print(f"{h:6.1f} {surf:12.3f} {vol:12.3f} {qenc:12.3f}")

# Task 12 settled by measurement rather than by argument. Both (b) and (c)
# look like they throw fluid outwards somewhere; a closed surface is the
# arbiter, and it never had to differentiate anything.
print(f"\nflux of (b), the rotation : {closed_box_flux(-Y, X, zero, 1.0):+.2e}")
print(f"flux of (c), the shear    : {closed_box_flux(X, -Y, zero, 1.0):+.2e}")

# --- self-check (leave this alone) ---
i0, i1 = fw.box_indices(X, 1.0)
s = slice(i0, i1 + 1)
fw.check_scalar("closed-surface flux = Q_enc/eps0", flux_1m,
                fw.volume_integral(rho_v[s, s, s], dx, dy, dz) / epsilon_0,
                rtol=0.01, unit=" V*m")
fw.check_scalar("divergence theorem: surface = volume", flux_1m,
                fw.volume_integral(div_blob[s, s, s], dx, dy, dz),
                rtol=0.01, unit=" V*m")
```

:::{admonition} Solution — Task 14
:class: dropdown

```python
    flux_y = (fw.area_integral(Ay[s, i1, s], dx, dz)
              - fw.area_integral(Ay[s, i0, s], dx, dz))
    flux_z = (fw.area_integral(Az[s, s, i1], dx, dy)
              - fw.area_integral(Az[s, s, i0], dx, dy))
    return flux_x + flux_y + flux_z
```
:::

:::{admonition} Three routes, one number
:class: important

Three genuinely different calculations. The first never looks inside the box; the second never looks at the surface; the third never looks at the field at all. They agree to a fraction of a percent.

The number grows with $h$ and then stops: once the cube holds essentially all the charge, enlarging it adds surface but no charge. Charge outside a closed surface contributes exactly nothing — the field lines it sends in through one wall leave through another.
:::

### And now shrink the source to a point

Run the same surface integral on the point-charge field from Task 7 — the one whose divergence you could never measure at the origin, because you had to mask it away.

Rearranged, Gauss's law turns your flux into a **charge meter**: $Q_{\text{enc}} = \varepsilon_0 \oint_S \boldsymbol{E}\cdot\hat{\boldsymbol{n}}\,dS$. So weigh the charge inside each box, in coulombs, and compare it with the 1 nC you put there.

```{code-cell} ipython3
print("box half-width      charge it finds")
for h in (0.6, 1.0, 1.4):
    Q_found = epsilon_0 * closed_box_flux(Ex, Ey, Ez, h)
    print(f"   {h:.1f} m           {Q_found * 1e12:8.2f} pC")
print(f"\n   actually there   {Q * 1e12:8.2f} pC")

# The shell between the 0.6 m and 1.4 m boxes holds no charge at all. Weigh it:
# what enters the small box must leave the large one, so the difference of the
# two fluxes is the charge in between.
Q_shell = epsilon_0 * (closed_box_flux(Ex, Ey, Ez, 1.4)
                       - closed_box_flux(Ex, Ey, Ez, 0.6))
print(f"\ncharge in the shell between them: {Q_shell * 1e12:+.2f} pC "
      f"({abs(Q_shell) / Q:.2%} of the charge at the centre)")
```

:::{admonition} Where did the charge go?
:class: important

Every box weighs the same 1 nC, to a fraction of a percent — and the shell between two of them weighs nothing. All the charge is in the only region every box has in common: the origin.

So the whole source sits at one point, where $\nabla\cdot\boldsymbol{E}$ is not a large number but no number at all: $\rho_v$ has become a **Dirac delta**, zero everywhere, infinite at one point, with a finite integral $Q$. The integral form survives exactly where the differential form breaks down.

The same statement for magnetism carries no source term at all:

$$ \nabla\cdot\boldsymbol{B} = 0 \qquad\Longleftrightarrow\qquad \oint_S \boldsymbol{B}\cdot\hat{\boldsymbol{n}}\,dS = 0 \ \ \text{for every closed } S $$

Run this measurement around any closed surface anywhere and you get zero: there are no magnetic monopoles, and field lines of $\boldsymbol{B}$ never begin and never end.
:::

### And the dipole, exactly

Task 11 measured $\nabla\cdot\boldsymbol{B} = 0$ for the Earth's dipole and got 1.8% — grid error, not physics. Now make the same claim without differentiating anything: put a closed surface around the dipole and weigh what comes out.

One warning before you read the numbers. A box centred on the origin is a
suspiciously easy test for *this* dipole: with $\boldsymbol{m} = \hat{\boldsymbol{z}}$, $B_x$ and $B_y$ are odd in $z$ and $B_z$ is even, so on a $z$-symmetric box the faces cancel in pairs *before* any physics enters. A lopsided box is the honest one, so the cell below runs both.

```{code-cell} ipython3
r_dot_m = Z
Bx = 3*X*r_dot_m / r_safe**5
By = 3*Y*r_dot_m / r_safe**5
Bz = (3*Z*r_dot_m - r_safe**2) / r_safe**5

B = tuple(np.nan_to_num(q) for q in (Bx, By, Bz))
v = tuple(np.nan_to_num(q / r_safe**3) for q in (X, Y, Z))

# --- given: the same surface integral over any grid-aligned box, centred
#     on the origin or not. Same six faces, same three pairs as Task 14.
def box_flux(A, x0, x1, y0, y1, z0, z1):
    i = [int(np.argmin(np.abs(axis - q))) for q in (x0, x1, y0, y1, z0, z1)]
    sx, sy, sz = slice(i[0], i[1]+1), slice(i[2], i[3]+1), slice(i[4], i[5]+1)
    return (fw.area_integral(A[0][i[1], sy, sz], dy, dz) - fw.area_integral(A[0][i[0], sy, sz], dy, dz)
          + fw.area_integral(A[1][sx, i[3], sz], dx, dz) - fw.area_integral(A[1][sx, i[2], sz], dx, dz)
          + fw.area_integral(A[2][sx, sy, i[5]], dx, dy) - fw.area_integral(A[2][sx, sy, i[4]], dx, dy))

boxes = [("centred, h = 0.6", (-0.6, 0.6, -0.6, 0.6, -0.6, 0.6)),
         ("centred, h = 1.0", (-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)),
         ("centred, h = 1.4", (-1.4, 1.4, -1.4, 1.4, -1.4, 1.4)),
         ("lopsided in z   ", (-1.0, 1.0, -1.0, 1.0, -0.6, 1.0)),
         ("lopsided in x, z", (-0.6, 1.0, -1.0, 1.0, -0.6, 1.0))]

print("  box                 flux of B      flux of the radial flow v")
for name, lim in boxes:
    print(f"  {name}   {box_flux(B, *lim):+11.2e}   {box_flux(v, *lim):+12.4f}")
print(f"\n  4*pi = {4*np.pi:.4f};  the integrator misses it by "
      f"{4*np.pi - box_flux(v, -1, 1, -1, 1, -1, 1):.1e} on the flow")

# --- self-check (leave this alone) ---
fw.check("the dipole encloses nothing -- even in a box that is not centred on it",
         max(abs(box_flux(B, *lim)) for _, lim in boxes) < 1e-2)
fw.check("...and the same integrator does find the tap in the radial flow",
         abs(box_flux(v, -1, 1, -1, 1, -1, 1) - 4*np.pi) < 0.01 * 4*np.pi)
```

:::{admonition} Two kinds of "divergence-free"
:class: important

The radial flow returns $4\pi$ through every surface, whatever its size — there is a tap at the origin, and every box finds the same one, exactly as every box found the same 1 nC a moment ago.

The dipole returns **nothing**, through any of them. On the three centred boxes the answer is zero to machine precision — but read that with the warning above in mind: those boxes cancel the field against itself by symmetry, so they were never going to say anything else. The lopsided boxes are the measurement that counts, and they return $-2.5\times10^{-3}$ and $-2.2\times10^{-4}$. That sounds like a retreat until you put it beside the column next to it: the very same integrator, on the very same grid, misses $4\pi$ by $6.8\times10^{-3}$ on the radial flow. **The dipole's flux is zero to better than the accuracy with which this method can measure anything at all.**

So the two "divergence-free" fields are not the same statement. The flow has a tap you can find by shrinking a surface onto it; the dipole has nothing to find, at any size or placement of the surface. That is $\nabla\cdot\boldsymbol{B} = 0$ in the form that admits no exception, and it is why the integral form was worth building: it settles matters *at* the source, where the differential form had to be masked away.
:::

### Where do the 1% errors come from?

Every derivative on this page is a centred difference, accurate to $O(\Delta x^{2})$. That is a law, not an excuse: halve the spacing and the error should fall by four. Confirm it — the whole study is one loop.

```{code-cell} ipython3
print(f"{'n':>4} {'dx [m]':>8} {'worst error':>12} {'ratio':>7}")
prev = None
for n_test in (21, 31, 41, 61):
    ax_t = np.linspace(-L, L, n_test)
    h_t = ax_t[1] - ax_t[0]
    Xt, Yt, Zt = np.meshgrid(ax_t, ax_t, ax_t, indexing="ij")
    rt = np.sqrt(Xt**2 + Yt**2 + Zt**2)
    Rst = np.maximum(rt, 1e-12)
    rho_t = rho_v0 * np.exp(-rt**2 / a**2)
    E_Rt = rho_v0 / (epsilon_0 * Rst**2) * (
        (a**3 * np.sqrt(np.pi) / 4) * erf(Rst / a)
        - (a**2 * Rst / 2) * np.exp(-Rst**2 / a**2))
    dv = divergence(E_Rt * Xt / Rst, E_Rt * Yt / Rst, E_Rt * Zt / Rst, h_t, h_t, h_t)
    inner = np.zeros(Xt.shape, bool)
    inner[2:-2, 2:-2, 2:-2] = True
    e = np.nanmax(np.abs(dv[inner] - (rho_t / epsilon_0)[inner])) / np.nanmax(rho_t / epsilon_0)
    ratio = "-" if prev is None else f"{prev / e:.2f}"
    print(f"{n_test:>4} {h_t:>8.4f} {e:>11.2%} {ratio:>7}")
    prev = e
```

:::{admonition} Second order, by measurement
:class: important

Compare each ratio with the square of the spacing ratio — $1.5^2 = 2.25$ from $n=21$ to $31$, $1.33^2 = 1.78$ from $31$ to $41$, $1.5^2 = 2.25$ from $41$ to $61$.

So the 1.06% in Task 13 is not noise to be tolerated: it is a number you can predict, and buy down if you need to. And the choice of $n = 61$ in Part 2 is now yours to audit rather than take on trust.
:::

---

## Closing

Today's chain, in one line:

$$ \rho_v \;\longrightarrow\; V \;\xrightarrow{\ -\nabla\ }\; \boldsymbol{E} \;\xrightarrow{\ \nabla\cdot\ }\; \rho_v/\varepsilon_0 $$

- **Gradient** — scalar in, vector out. Points along steepest increase, perpendicular to the level surfaces, with length equal to the rate of increase.
- **Divergence** — vector in, scalar out. Net flux per unit volume: what is being created here, and nothing else.

### The same two operators, elsewhere in ECT

Electrostatics is the convenient place to *learn* this pair, not the only place to use it. Every row below is a potential, its gradient, and a statement about sources — and the numerical machinery you wrote today applies unchanged to all of them:

| System | Potential | Field | Source equation |
| :--- | :--- | :--- | :--- |
| Electrostatics | $V$ [V] | $\boldsymbol{E} = -\nabla V$ &nbsp; [V/m] | $\nabla\cdot\boldsymbol{E} = \rho_v/\varepsilon_0$ |
| Gravitation | $\Phi$ [J/kg] | $\boldsymbol{g} = -\nabla \Phi$ &nbsp; [m/s$^2$] | $\nabla\cdot\boldsymbol{g} = -4\pi G\rho_m$ |
| Heat conduction | $T$ [K] | $\boldsymbol{q}_T = -k\nabla T$ &nbsp; [W/m$^2$] | $\nabla\cdot\boldsymbol{q}_T = 0$ (steady, no sources) |
| Groundwater flow | $h$ [m] | $\boldsymbol{q}_h = -K\nabla h$ &nbsp; [m/s] | $\nabla\cdot\boldsymbol{q}_h = 0$ (steady, incompressible) |

with $k$ the thermal conductivity [W m$^{-1}$ K$^{-1}$] and $K$ the hydraulic conductivity [m/s].

The minus signs are all the same minus sign: heat flows from hot to cold, water flows from high head to low, a positive charge falls from high potential to low. Flow runs downhill, and the gradient points uphill.

The last two rows are why a solenoidal field matters so much in practice. $\nabla\cdot\boldsymbol{q} = 0$ in an aquifer is not an approximation of convenience — it is conservation of water written locally.

### What is still missing

Go back to field **(b)**, the rotation. Its divergence is zero everywhere, so by that measure it is indistinguishable from a field doing nothing at all. But it plainly *is* doing something — it circulates, and every streamline closes on itself.

Divergence cannot see circulation. The operator that can is the **curl**, the third of the three this chapter is named after.

### Homework

The exercises in your lecture notes are the written homework. Below is the lab's own extension — the one piece that is computational rather than pen-and-paper, and that carries the afternoon's operators into a system you can feel.

**A heat source in a room.** Replace the spherical blob with a flat rectangular heater, $1.0 \times 0.6$ m in the $z = 0$ plane. A steady point source of power $P$ in a medium of conductivity $k$ raises the temperature above ambient by $P/4\pi k r$ — the same $1/r$ you have worked with all afternoon. Split the plate into $N = 20 \times 12$ sub-sources, give each an equal share $P/N$ of the power, and superpose, exactly as you superposed two charges in Task 8:

$$ T(\boldsymbol{r}) = \frac{P}{4\pi k N}\sum_{i=1}^{N} \frac{1}{\lvert \boldsymbol{r} - \boldsymbol{r}_i \rvert}, \qquad P = 100\ \text{W}, \qquad k_{\text{air}} = 0.026\ \text{W m}^{-1}\text{K}^{-1}. $$

Check the dimensions before you code it: $[P]/[k] = \text{W}/(\text{W m}^{-1}\text{K}^{-1}) = \text{m}\cdot\text{K}$, divided by a distance, so $T$ comes out in kelvin. A formula for a temperature that does not is a formula with a bug in it. Then:

- Plot the isosurfaces. Close to the plate they should be rounded rectangles; far away they should become spheres. Why does the shape forget its source?
- Compute the heat flux $\boldsymbol{q}_T = -k\nabla T$ — the same minus sign, the same reason as $\boldsymbol{E} = -\nabla V$.
- Check that $\nabla\cdot\boldsymbol{q}_T \approx 0$ away from the heater, and that the closed-surface flux through a box containing the plate is *not* zero. Say what each result means physically for a room at steady state, and which of the two fields you met in Task 11 the heater resembles.
- **Then look at the number.** One metre from a 100 W panel this model predicts about $+290$ K above ambient — a room at 300 °C. The arithmetic is right, so the *physics* is wrong. Which assumption failed? (Two are worth naming: what actually carries heat through air, and where this solution puts the room's walls.) Re-run it with $k = 1.5$ W m⁻¹K⁻¹, the conductivity of soil, and you get $+5$ K — the same equations, now describing a buried heating element, which is a problem pure conduction really does solve.
