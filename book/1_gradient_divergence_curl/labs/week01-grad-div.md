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

By the end of this session you should be able to:

- **Read a gradient off a picture.** Explain why $\nabla f$ is perpendicular to the level surfaces of $f$, and why the single minus sign in $\mathbf{E} = -\nabla V$ is the step from geometry to physics.
- **Distinguish "arrows spreading apart" from divergence.** Compute $\nabla\cdot\mathbf{A}$ for fields, and justify the answer with a flux argument rather than with algebra.
- **Use Gauss's law as a measurement.** Verify $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ pointwise, verify the divergence theorem $\oint_S\mathbf{E}\cdot d\mathbf{s} = \int_v \nabla\cdot\mathbf{E}\,dv$ numerically, and explain what happens to both when the source shrinks to a point.


---

## Part 0 — Setup

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

First make a cube grid:

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

| $n$ | $\Delta x$ [m] | $\lvert\nabla R\rvert$ | $\nabla(1/R)$ | $\nabla\cdot\mathbf{E}$ |
| ---: | ---: | ---: | ---: | ---: |
| 21 | 0.200 | 4.1% | 12.5% | 9.1% |
| 41 | 0.100 | 1.8% | 3.3% | 2.4% |
| **61** | **0.067** | **0.8%** | **1.6%** | **1.1%** |
| 81 | 0.050 | 0.5% | 1.0% | 0.6% |

Halving $\Delta x$ quarters the error, as second order requires. $n = 61$ was chosen by that measurement: it is the coarsest grid that keeps every task under 2%, and each 3-D figure it produces weighs about 1.5 MB. **If you change `n`, keep it at 41 or above** — the self-checks below allow 5%, and $n = 31$ already fails Task 3.

Note also that the box is a finite window on fields that extend to infinity: the largest closed surface in Part 5 sits only 0.6 m inside the outer face.


The grid is built with `indexing='ij'`, so axis 0 is $x$, axis 1 is $y$, axis 2 is $z$.

1. **Derivatives come back in coordinate order:** `np.gradient(f, dx, dy, dz)` returns $\partial f/\partial x$, $\partial f/\partial y$, $\partial f/\partial z$. No transposes.
2. **Always pass the spacings.** Omit them and the derivative is silently wrong by a factor of $1/\Delta x = 15$.

Numpy's default is `indexing='xy'`, which returns the $y$-derivative first. That one fact is the origin of a large fraction of all numerical field bugs.
:::

---

## Part 1 — The distance function, and what its gradient is

Before any physics, one piece of pure geometry. The simplest scalar field there is:

$$ R(x,y,z) = \sqrt{(x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2} $$

*How far am I from that point?* One number at every location in space. No charge, no potential, no units of anything — just distance.

This is the **spherical** radial coordinate $R$ — distance from a point. The cylindrical $r$, distance from an axis, is a different quantity, and Part 4 returns to the distinction. The equations on this page use $R$; the code calls it `r`, because it is the only radius in the lab.

### Task 1 — build the distance field

```{code-cell} ipython3
# Task 1 -- distance from a source at (x0, y0, z0) to every point of the grid.

def distance_to(X, Y, Z, x0=0.0, y0=0.0, z0=0.0):
    return np.sqrt(___ + ___ + ___)


r = distance_to(___, ___, ___)          # source at the origin

# --- self-check (leave this alone) ---
fw.check_shape("r", r, X.shape)
fw.check("r = 0 at the origin", np.isclose(r[c, c, c], 0.0))
fw.check("r = 2 m at (2,0,0)", np.isclose(r[-1, c, c], 2.0))
fw.check("r = 2 m at (0,2,0)", np.isclose(r[c, -1, c], 2.0))
```

:::{admonition} Solution — Task 1
:class: dropdown

```python
def distance_to(X, Y, Z, x0=0.0, y0=0.0, z0=0.0):
    return np.sqrt((X - x0)**2 + (Y - y0)**2 + (Z - z0)**2)


r = distance_to(X, Y, Z)
```
:::

A surface on which $R$ takes one fixed value is an **isosurface**, or level set — the three-dimensional version of a contour line on a map. 

```{code-cell} ipython3
fw.show_isosurfaces(X, Y, Z, r, levels=[0.5, 1.0, 1.5], label="r  [m]",
                    title="Isosurfaces of the distance function r")
```


### Task 2 — the gradient of the distance

Compute $\nabla R$. Before you run anything, predict two things and write them down: **which way** the arrows point, and **how long** they are.

Then test the prediction quantitatively. The outward unit radial vector is $\hat{\mathbf{a}}_R = (x\,\hat{\mathbf{a}}_x + y\,\hat{\mathbf{a}}_y + z\,\hat{\mathbf{a}}_z)/R$, so the radial part of any vector field $\mathbf{A}$ is $\mathbf{A}\cdot\hat{\mathbf{a}}_R$. If $\nabla R$ is *purely* radial, that projection recovers its full magnitude.

```{code-cell} ipython3
# The outward unit radial vector, used again later.
Rs = np.maximum(r, 1e-12)                 # 0/0 at the source is not a lesson
aRx, aRy, aRz = X / Rs, Y / Rs, Z / Rs

# Task 2
#   1. grad r, as three components.
#   2. Its magnitude.
#   3. Its projection onto a_R.
#   4. Draw it, then rotate the figure and compare with the spheres above.

grx, gry, grz = np.gradient(___, ___, ___, ___)

grad_r_mag = np.sqrt(___ + ___ + ___)

radial_part = grx * ___ + gry * ___ + grz * ___

fw.show_cones(X, Y, Z, grx, gry, grz, step=8, label="|∇r|  [-]",
              title="grad r -- unit vectors pointing away from the source")

# --- self-check (leave this alone) ---
band = (r > 0.4) & (r < 1.6)
fw.check_shape("grad r (x-component)", grx, X.shape)
fw.check_close("|grad r| = 1 everywhere", grad_r_mag, 1.0, rtol=0.05, where=band)
fw.check_close("grad r is purely radial", radial_part, 1.0, rtol=0.05, where=band)
```

:::{admonition} Solution — Task 2
:class: dropdown

```python
grx, gry, grz = np.gradient(r, dx, dy, dz)
grad_r_mag = np.sqrt(grx**2 + gry**2 + grz**2)
radial_part = grx * aRx + gry * aRy + grz * aRz

print(f"|grad r| median in 0.4 < r < 1.6 m : "
      f"{np.median(grad_r_mag[(r > 0.4) & (r < 1.6)]):.4f}")
```
:::

:::{admonition} The magnitude is 1. Everywhere.
:class: important

Walk one metre directly away from the source and your distance from it grows by exactly one metre. The steepest rate of change of $R$ is 1 m/m, wherever you stand:

$$ \nabla R = \hat{\mathbf{a}}_R $$

The second check fixes the direction: moving *along* a sphere does not change $R$, so the gradient has no component there. **$\nabla f$ is normal to the level surfaces of $f$** — for every scalar field, not just this one.

The chain rule now settles the next two tasks in advance: $\nabla g(R) = \dfrac{dg}{dR}\,\hat{\mathbf{a}}_R$ for any $g$ depending on position only through $R$. Predict before you run.
:::

---

## Part 2 — Invert it, and watch the arrows turn round

Now the function the physics actually uses: not the distance, but **one over** the distance,

$$ f(R) = \frac{1}{R}, \qquad\text{so}\qquad \nabla f = \frac{d}{dR}\!\left(\frac{1}{R}\right)\hat{\mathbf{a}}_R = -\frac{1}{R^{2}}\,\hat{\mathbf{a}}_R $$

Same spheres as isosurfaces — $f$ is constant wherever $R$ is constant. But the *ordering* has been turned inside out: $f$ is now largest near the source and decays to nothing far away. Predict what that does to the arrows, then check the prediction against the formula above, then measure it.

### Task 3 — the gradient of the inverse distance

```{code-cell} ipython3
# The mask keeps the singularity at r = 0 off the grid. Everything within
# 0.25 m of the source becomes NaN and is simply not measured.
r_masked = np.where(r < 0.25, np.nan, r)
f = 1.0 / r_masked

# Task 3
#   1. grad f, as components fx, fy, fz; then its magnitude f_mag. The
#      self-check compares it against the predicted 1/R^2.
#   2. Draw it with normalise=True: every arrow the same length, so the
#      picture shows direction only. The magnitude is not lost -- it moves
#      into the colour, on a log scale (it spans three decades here). Pass
#      a label so the colorbar names the quantity, e.g.
#      label="|∇(1/R)|  [m<sup>-2</sup>]" -- plotly colorbars take
#      Unicode and a little HTML, not LaTeX.

fx, fy, fz = ___
f_mag = ___



# --- self-check (leave this alone) ---
outside = (r > 0.5) & interior            # `interior` was built in Part 0
fw.check_close("|grad(1/r)| = 1/r^2", f_mag, 1.0 / r_masked**2, rtol=0.05, where=outside)
fw.check("grad(1/r) points inward at (1,0,0)", fx[-1 - 15, c, c] < 0)
```

:::{admonition} Solution — Task 3
:class: dropdown

```python
fx, fy, fz = np.gradient(f, dx, dy, dz)
f_mag = np.sqrt(fx**2 + fy**2 + fz**2)

for rr in (0.6, 1.0, 1.5):
    i = int(np.argmin(np.abs(X[:, 0, 0] - rr)))
    print(f"r = {rr:.1f} m :  |grad f| = {f_mag[i, c, c]:8.4f}   1/r^2 = {1/rr**2:8.4f}")

fw.show_cones(X, Y, Z, fx, fy, fz, step=8, normalise=True,
              label="|∇(1/r)|  [m<sup>-2</sup>]",
              title="grad(1/r) -- pointing back towards the source")
```
:::

:::{admonition} The gradient points towards *increase* — always
:class: important

The arrows have reversed. Same spheres, same source, opposite direction:

$$ \nabla R = +\hat{\mathbf{a}}_R, \qquad\qquad \nabla\!\left(\frac{1}{R}\right) = -\frac{1}{R^{2}}\,\hat{\mathbf{a}}_R $$

Nothing about space changed. What changed is **which way the function climbs**. And the steepness changed too: $1/R$ climbs ever faster as you approach the source, so its gradient grows as $1/R^2$ rather than staying at 1.

A gradient knows nothing about sources, sinks, charges or fields. It only knows uphill.
:::

### Task 4 — from geometry to physics

Here the physics enters, and it enters as a single minus sign. The electric potential of a point charge $Q$ is the inverse-distance function with a constant in front,

$$ V(R) = \frac{1}{4\pi\varepsilon_0}\frac{Q}{R}\quad[\text{V}], $$

and the electric field is *defined* as

$$ \mathbf{E} = -\nabla V \quad[\text{V/m}]. $$

You already know what $\nabla V$ does: it points inward, uphill towards the charge. The minus sign turns it round, so **the field points downhill** — which is exactly the way a positive test charge released from rest would move, losing potential energy as it goes.

```{code-cell} ipython3
V = k_e * Q / r_masked

# Task 4
#   1. E = -grad V, as components Ex, Ey, Ez; then E_mag.
#   2. Compare E_mag against the analytic k_e*Q/R^2 at a few radii, in V/m.
#   3. Draw it with normalise=True and confirm it points OUTWARD for Q > 0.

Ex, Ey, Ez = ___
E_mag = ___



# --- self-check (leave this alone) ---
fw.check_close("|E| = Q/(4 pi eps0 R^2)", E_mag, k_e * Q / r_masked**2,
               rtol=0.05, where=outside)
fw.check("E points outward at (1,0,0)", Ex[-1 - 15, c, c] > 0)
```

:::{admonition} Solution — Task 4
:class: dropdown

```python
dVdx, dVdy, dVdz = np.gradient(V, dx, dy, dz)
Ex, Ey, Ez = -dVdx, -dVdy, -dVdz
E_mag = np.sqrt(Ex**2 + Ey**2 + Ez**2)

for rr in (0.6, 1.0, 1.5):
    i = int(np.argmin(np.abs(X[:, 0, 0] - rr)))
    print(f"r = {rr:.1f} m :  |E| = {E_mag[i, c, c]:8.3f} V/m   "
          f"analytic = {k_e*Q/rr**2:8.3f} V/m")

fw.show_cones(X, Y, Z, Ex, Ey, Ez, step=8, normalise=True,
              label="|<b>E</b>|  [V/m]",
              title="E = -grad V for a positive point charge")
```
:::

:::{admonition} Why bother with $V$ at all?
:class: tip

$V$ is a scalar: one number per point, no direction to keep track of. $\mathbf{E}$ is a vector: three. Anything you can do once on $V$ and then differentiate is cheaper — in arithmetic and in bookkeeping — than doing it three times on $\mathbf{E}$.

Part 3 is the first payoff, and it is the reason the potential is worth defining in the first place.
:::

---

## Part 3 — Two sources: superposition

One charge is symmetric enough to be boring. Put down two:

$$ V_{\text{total}} = \frac{1}{4\pi\varepsilon_0}\left(\frac{Q_1}{R_1} + \frac{Q_2}{R_2}\right) $$

**Superposition** for the potential is nothing more than adding two numbers at every point, because $V$ is a scalar. Adding the two *fields* instead would mean a vector sum at every point in the cube.

Since $\nabla$ is a linear operator, $-\nabla(V_1 + V_2) = \mathbf{E}_1 + \mathbf{E}_2$ exactly. So the efficient route is: **add the potentials, then take one gradient at the very end.** Nothing is lost.

### Task 5 — build a dipole

```{code-cell} ipython3
# Distances to two sources on the x-axis. The guard only trips if a grid
# point lands exactly on a charge; at n = 61 none does, so nothing is masked
# here and you see the full field. Raise it if you change the grid.
r_plus = np.where(distance_to(X, Y, Z, -0.5, 0.0, 0.0) < 0.01, np.nan,
                  distance_to(X, Y, Z, -0.5, 0.0, 0.0))
r_minus = np.where(distance_to(X, Y, Z, +0.5, 0.0, 0.0) < 0.01, np.nan,
                   distance_to(X, Y, Z, +0.5, 0.0, 0.0))

# Task 5
#   1. Superpose the potentials of +Q at (-0.5, 0, 0) and -Q at (+0.5, 0, 0)
#      into V_dip. Scalar addition -- just a sum.
#   2. Take ONE gradient, negate it: Ex_d, Ey_d, Ez_d.
#   3. Draw the z = 0 plane, potential as colour and field as streamlines
#      (replace ... with a title of your own):
#          fw.show_field_slice(X, Y, Z, Ex_d, Ey_d, background=V_dip,
#                              title=..., label="$V$ [V]")
#      then plt.show().

V_dip = ___
Ex_d, Ey_d, Ez_d = ___



# --- self-check (leave this alone) ---
mid = np.abs(X) < 1e-9                    # the plane x = 0, halfway between them
fw.check_shape("V_dip", V_dip, X.shape)
fw.check("V = 0 on the mid-plane",
         np.nanmax(np.abs(V_dip[mid])) < 1e-6 * np.nanmax(np.abs(V_dip)))
fw.check("E on the mid-plane points from + to -", np.nanmean(Ex_d[mid]) > 0)
```

:::{admonition} Solution — Task 5
:class: dropdown

```python
V_dip = k_e * Q / r_plus + k_e * (-Q) / r_minus

dVx, dVy, dVz = np.gradient(V_dip, dx, dy, dz)
Ex_d, Ey_d, Ez_d = -dVx, -dVy, -dVz

fw.show_field_slice(X, Y, Z, Ex_d, Ey_d, background=V_dip,
                    title="Source and sink: potential (colour) and field lines",
                    label="$V$ [V]")
plt.show()
```
:::

:::{admonition} Look at the mid-plane before you move on
:class: tip

Halfway between the two charges, at $x = 0$, the potential is **exactly zero** — the two contributions cancel. Yet the field there is not zero at all: it is at its strongest, pointing straight from the positive charge to the negative one.

The field is the *slope* of the potential, not its value. A landscape can be at sea level and still be steep. Notice also what the picture shows about direction: the streamlines cross the coloured contours at right angles everywhere, which is Task 2's normality result showing up in a field you did not construct radially.
:::

The same object in three dimensions — positive and negative equipotential surfaces together, drawn transparent:

```{code-cell} ipython3
lobe = np.nanpercentile(np.abs(V_dip), 97)
fw.show_isosurfaces(X, Y, Z, np.nan_to_num(V_dip), levels=[-lobe, -lobe/3, lobe/3, lobe],
                    colorscale="RdBu", opacity=0.3, label="V  [V]",
                    title="Equipotential surfaces of a dipole")
```

---

## Part 4 — Divergence: is anything being created here?

The gradient took a scalar and returned a vector. The divergence goes the other way — hand it a vector field, get back a scalar:

$$ \nabla\cdot\mathbf{A} \;=\; \lim_{\Delta v \to 0}\frac{1}{\Delta v}\oint_S \mathbf{A}\cdot d\mathbf{s} \;=\; \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z} $$

Read the definition on the left, not the formula on the right: **treat $\mathbf{A}$ as the velocity of a fluid**, put a small box anywhere, and measure the net outflow through its walls per unit volume.

| $\nabla\cdot\mathbf{A}$ | Name | Picture |
| :---: | :--- | :--- |
| $> 0$ | **source** | a tap — more leaves than arrives |
| $< 0$ | **sink** | a drain — more arrives than leaves |
| $= 0$ | **solenoidal** | whatever flows in, flows out |

### Task 6 — write the divergence

```{code-cell} ipython3
# Task 6
#   Write divergence(Ax, Ay, Az, dx, dy, dz) returning
#   dAx/dx + dAy/dy + dAz/dz -- one derivative along one axis per component.
#   np.gradient(Ax, dx, axis=0) gives dAx/dx and nothing else; asking it for
#   all three and throwing two away costs three times the memory, which
#   matters in the browser. The cross terms are not part of a divergence.

# Write your code here:



# --- self-check (leave this alone) ---
# The position vector A = x a_x + y a_y + z a_z has divergence 1 + 1 + 1 = 3
# everywhere. Confirm that on paper before you trust the number.
fw.check_close("div of the position vector = 3",
               divergence(X, Y, Z, dx, dy, dz), 3.0, rtol=1e-6)
```

:::{admonition} Solution — Task 6
:class: dropdown

```python
def divergence(Ax, Ay, Az, dx, dy, dz):
    return (np.gradient(Ax, dx, axis=0)
            + np.gradient(Ay, dy, axis=1)
            + np.gradient(Az, dz, axis=2))
```
:::

### Task 7 — three flows

Three velocity fields. For each: **sketch it in your head, predict the sign of the divergence, then measure.** Write the predictions down first — the point of this task is the gap between intuition and the answer.

| | Field $\mathbf{A}$ | What it looks like |
| :---: | :--- | :--- |
| **(a)** | $x\,\hat{\mathbf{a}}_x + y\,\hat{\mathbf{a}}_y + z\,\hat{\mathbf{a}}_z$ | flow rushing outward in all directions |
| **(b)** | $-y\,\hat{\mathbf{a}}_x + x\,\hat{\mathbf{a}}_y$ | fluid rotating about the $z$-axis |
| **(c)** | $x\,\hat{\mathbf{a}}_x - y\,\hat{\mathbf{a}}_y$ | stretching along $x$, squeezing along $y$ |

```{code-cell} ipython3
# Commit to your predictions BEFORE the next cell: +1 for a source, -1 for a
# sink, 0 for solenoidal. The next cell scores them.
predictions = {"a": ___, "b": ___, "c": ___}
```

```{code-cell} ipython3
# Task 7
#   1. Build the three fields as triples of arrays.
#   2. Take the divergence of each with your Task 6 function, as div_a,
#      div_b and div_c -- the self-check needs those names. Print the mean
#      of each.
#   3. Draw fields (a) and (c) side by side in the z = 0 plane, streamlines
#      over their own divergence as the background, both on the SAME scale
#      so the colours are comparable:
#          fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))
#          fw.show_field_slice(X, Y, Z, *Aa[:2], background=div_a, ax=axes[0],
#                              vmin=-3, vmax=3, label=r"$\nabla\cdot\mathbf{A}$",
#                              title="(a) outward flow")
#          ... and the same for (c) with Ac and div_c.
#      Look hard at the two before reading the note below.

# Write your code here:



# --- self-check (leave this alone) ---
fw.check_close("(a) div = 3", div_a, 3.0, rtol=1e-6)
fw.check_close("(b) div = 0 (rotation)", div_b + 1.0, 1.0, rtol=1e-6)
fw.check_close("(c) div = 0 (shear)", div_c + 1.0, 1.0, rtol=1e-6)

for key, measured in (("a", div_a), ("b", div_b), ("c", div_c)):
    sign = int(np.sign(np.round(measured.mean(), 6)))
    verdict = "as predicted" if predictions[key] == sign else "NOT what you predicted"
    print(f"  ({key}) you said {predictions[key]:+d}, measured {sign:+d}  --  {verdict}")
```

:::{admonition} Solution — Task 7
:class: dropdown

```python
zero = np.zeros_like(X)

Aa = (X, Y, Z)
Ab = (-Y, X, zero)
Ac = (X, -Y, zero)

div_a = divergence(*Aa, dx, dy, dz)
div_b = divergence(*Ab, dx, dy, dz)
div_c = divergence(*Ac, dx, dy, dz)

for name, d in [("(a) outward flow", div_a), ("(b) rotation", div_b), ("(c) shear", div_c)]:
    print(f"{name:20s} div = {d.mean():+.3f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))
for ax_, (name, A, d) in zip(axes, [("(a) outward flow", Aa, div_a),
                                    ("(c) shear flow", Ac, div_c)]):
    fw.show_field_slice(X, Y, Z, *A[:2], background=d, ax=ax_, density=1.1,
                        vmin=-3, vmax=3, colorbar=(ax_ is axes[-1]),
                        label=r"$\nabla\cdot\mathbf{A}$  [s$^{-1}$]", title=name)
plt.tight_layout()
plt.show()
```
:::

:::{admonition} Field (c) is the one that costs marks
:class: warning

Along the $x$-axis, field (c) rushes outward. It looks like a source. It is not:

$$ \nabla\cdot\mathbf{A} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(-y) = 1 - 1 = 0 $$

Put a box at the origin: fluid pours out through the left and right walls and in through the top and bottom at exactly the same rate. The parcel changes **shape**, never **volume**.

*Arrows pointing apart* is not divergence. Outflow in one direction can be cancelled exactly by inflow in another — and in Task 9 you will put a closed surface around this field and measure that cancellation, rather than take it on the strength of this paragraph.
:::

### Task 8 — the divergence as a charge detector

Maxwell's first equation says

$$ \nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0} $$

which is a strong claim: **the divergence of $\mathbf{E}$ at a point tells you the charge density at that point and nothing else.** Wherever there is no charge, $\mathbf{E}$ is solenoidal, however dramatically its arrows spread out.

Test that pointwise on a real source. Not a point charge — that is an idealisation with infinite density at one location, and no grid can hold it. Take instead a charge **smeared over a finite blob**, which is what any actual charged object is:

$$ \rho(R) = \rho_0\,e^{-R^{2}/a^{2}}, \qquad \rho_0 = 10^{-9}\ \text{C/m}^3, \qquad a = 0.5\ \text{m} $$

Integrating that over a sphere of radius $R$ gives the charge it encloses (bookwork — you do not need to do the integral now):

$$ Q_{\text{enc}}(R) = \int_0^{R}\!\rho\,4\pi R'^{2}\,dR' = 4\pi\rho_0\left[\frac{a^{3}\sqrt{\pi}}{4}\operatorname{erf}\!\left(\frac{R}{a}\right) - \frac{a^{2}R}{2}e^{-R^{2}/a^{2}}\right] $$

and Gauss's law in the form you already know, $E_R = Q_{\text{enc}}/4\pi\varepsilon_0R^{2}$, then gives the field — the $4\pi$ cancelling:

$$ E_R(R) = \frac{\rho_0}{\varepsilon_0 R^{2}}\left[\frac{a^{3}\sqrt{\pi}}{4}\operatorname{erf}\!\left(\frac{R}{a}\right) - \frac{a^{2}R}{2}e^{-R^{2}/a^{2}}\right] $$

Check it at small $R$ before trusting it. There $Q_{\text{enc}} \to \frac{4}{3}\pi R^{3}\rho_0$, so $E_R \to \rho_0R/3\varepsilon_0$: the field **rises linearly** from zero at the centre, because the charge enclosed grows faster than the $R^{2}$ of the surface. It peaks near $R \approx a$ and only then falls off.

```{code-cell} ipython3
from scipy.special import erf

a, rho0 = 0.5, 1e-9

# Task 8
#   1. rho = rho0 * exp(-r^2 / a^2) on the grid.
#   2. E_R from the formula above, using Rs in the denominators. (The two
#      bracketed terms very nearly cancel for R << a, so the closed form
#      loses accuracy below R ~ 1e-6 m; on this grid the only such sample
#      is the origin, where the a_R components are zero anyway.)
#   3. Turn the radial magnitude into components along a_R:
#      Ex_b = E_R * aRx, and likewise for y and z.
#   4. div_blob = divergence(...), and compare it against rho / epsilon_0
#      everywhere -- including inside the source.
#   5. Plot both, side by side, in the z = 0 plane. Pass the SAME vmin and
#      vmax to each panel, or they get separate auto-scales and the two
#      pictures are no longer comparable -- which is the whole point:
#          hi = float(np.nanmax(rho / epsilon_0))
#          fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))
#          fw.show_scalar_slice(X, Y, Z, div_blob, ax=axes[0], cmap="magma",
#                               vmin=0, vmax=hi, label=..., title=...)
#          fw.show_scalar_slice(X, Y, Z, rho / epsilon_0, ax=axes[1], ...)

# Write your code here:



# --- self-check (leave this alone) ---
peak = np.nanmax(rho / epsilon_0)
_e = np.abs(div_blob[interior] - (rho / epsilon_0)[interior]) / peak
cart_worst, cart_median = float(_e.max()), float(np.median(_e))
fw.check(f"div E = rho/eps0 pointwise (worst {cart_worst:.2%} of peak)",
         cart_worst < 0.05, "check the component construction Ex_b = E_R * aRx")
```

:::{admonition} Solution — Task 8
:class: dropdown

```python
rho = rho0 * np.exp(-r**2 / a**2)

E_R = rho0 / (epsilon_0 * Rs**2) * (
    (a**3 * np.sqrt(np.pi) / 4) * erf(Rs / a) - (a**2 * Rs / 2) * np.exp(-Rs**2 / a**2)
)
Ex_b, Ey_b, Ez_b = E_R * aRx, E_R * aRy, E_R * aRz

div_blob = divergence(Ex_b, Ey_b, Ez_b, dx, dy, dz)

hi = float(np.nanmax(rho / epsilon_0))
units = r"[V m$^{-2}$]"
fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))
fw.show_scalar_slice(X, Y, Z, div_blob, ax=axes[0], cmap="magma", label=units,
                     vmin=0, vmax=hi, title=r"measured $\nabla\cdot\mathbf{E}$")
fw.show_scalar_slice(X, Y, Z, rho / epsilon_0, ax=axes[1], cmap="magma", label=units,
                     vmin=0, vmax=hi, title=r"actual $\rho/\varepsilon_0$")
plt.tight_layout()
plt.show()

print(f"peak of rho/eps0    : {np.nanmax(rho/epsilon_0):8.2f}")
print(f"peak of measured div: {np.nanmax(div_blob):8.2f}")
```
:::

:::{admonition} What you just did
:class: important

The two pictures are the same picture. You never told the code where the charge was — you handed it a *field*, differentiated it, and the charge distribution came back out.

Notice where the divergence vanishes: everywhere outside the blob, where the field is still large and still spreading. **Strong field, zero divergence** — the two ideas are unrelated.
:::

### The same operator, a different formula

Everything so far used the Cartesian formula, because `np.gradient` differentiates along array axes. But the divergence *is* flux per unit volume — a physical quantity, which cannot depend on the axes you happened to choose. Only the formula changes:

| | Gradient $\nabla T$ | Divergence $\nabla\cdot\mathbf{A}$ |
| :--- | :--- | :--- |
| Cartesian $(x,y,z)$ | $\dfrac{\partial T}{\partial x}\hat{\mathbf{a}}_x + \dfrac{\partial T}{\partial y}\hat{\mathbf{a}}_y + \dfrac{\partial T}{\partial z}\hat{\mathbf{a}}_z$ | $\dfrac{\partial A_x}{\partial x} + \dfrac{\partial A_y}{\partial y} + \dfrac{\partial A_z}{\partial z}$ |
| Cylindrical $(r,\phi,z)$ | $\dfrac{\partial T}{\partial r}\hat{\mathbf{a}}_r + \dfrac{1}{r}\dfrac{\partial T}{\partial \phi}\hat{\mathbf{a}}_\phi + \dfrac{\partial T}{\partial z}\hat{\mathbf{a}}_z$ | $\dfrac{1}{r}\dfrac{\partial (rA_r)}{\partial r} + \dfrac{1}{r}\dfrac{\partial A_\phi}{\partial \phi} + \dfrac{\partial A_z}{\partial z}$ |
| Spherical $(R,\theta,\phi)$ | $\dfrac{\partial T}{\partial R}\hat{\mathbf{a}}_R + \dfrac{1}{R}\dfrac{\partial T}{\partial \theta}\hat{\mathbf{a}}_\theta + \dfrac{1}{R\sin\theta}\dfrac{\partial T}{\partial \phi}\hat{\mathbf{a}}_\phi$ | $\dfrac{1}{R^{2}}\dfrac{\partial (R^{2}A_R)}{\partial R} + \dfrac{1}{R\sin\theta}\dfrac{\partial (A_\theta \sin\theta)}{\partial \theta} + \dfrac{1}{R\sin\theta}\dfrac{\partial A_\phi}{\partial \phi}$ |

Cylindrical $r$ is the distance from the $z$-axis; spherical $R$, used throughout this lab, is the distance from the origin.

Both fields you have built are spherically symmetric — $\mathbf{E} = E_R(R)\,\hat{\mathbf{a}}_R$, with no $\theta$ or $\phi$ dependence — so two of the three spherical terms vanish and the divergence collapses to one ordinary derivative along one line:

$$ \nabla\cdot\mathbf{E} \;=\; \frac{1}{R^{2}}\frac{d}{dR}\!\left(R^{2}E_R\right) $$

```{code-cell} ipython3
dR = 0.005
R_line = np.arange(0.05, 2.0 + dR, dR)          # one radial line, not a cube

# the same two fields as before, as functions of R alone
E_R_blob = rho0 / (epsilon_0 * R_line**2) * (
    (a**3 * np.sqrt(np.pi) / 4) * erf(R_line / a)
    - (a**2 * R_line / 2) * np.exp(-R_line**2 / a**2))
E_R_point = k_e * Q / R_line**2

div_blob_sph = np.gradient(R_line**2 * E_R_blob, dR) / R_line**2
div_point_sph = np.gradient(R_line**2 * E_R_point, dR) / R_line**2

rho_line = rho0 * np.exp(-R_line**2 / a**2)
err_sph = np.abs(div_blob_sph - rho_line / epsilon_0)[1:-1] / np.max(rho_line / epsilon_0)
print(f"blob : {R_line.size} samples on a line vs {X.size:,} in the cube")
print(f"       worst error {err_sph.max():.3%} of peak, median {np.median(err_sph):.4%}")
print(f"       Cartesian, from Task 8: {cart_worst:.3%} and {cart_median:.4%}")
print(f"point: R^2 E_R varies by {np.ptp(R_line**2 * E_R_point):.1e} over the whole line")
print(f"       max |div E| = {np.abs(div_point_sph).max():.1e}")
```

:::{admonition} Why anyone bothers with curvilinear coordinates
:class: important

Same field, same operator, same answer — from a few hundred samples on a line instead of a quarter of a million in a cube, and several times more accurately.

For the point charge the gain is not accuracy but certainty. $R^{2}E_R = q/4\pi\varepsilon_0$ is a **constant**, so its derivative is exactly zero for every $R>0$ — not "1.35% of something", but zero. Cartesian coordinates could only ever report that the divergence was small.

Match your coordinates to the symmetry of the source and three noisy numerical derivatives collapse into one line of algebra. That is what the second and third rows of the table are for.
:::

---

## Part 5 — Flux, and the divergence theorem

Part 4 used the *differential* form of Gauss's law, which compares two numbers at one point. The *integral* form connects a volume to the surface enclosing it:

$$ \oint_S \mathbf{E}\cdot d\mathbf{s} \;=\; \int_v \nabla\cdot\mathbf{E}\;dv \;=\; \frac{Q_{\text{enc}}}{\varepsilon_0} $$

The first equality is the **divergence theorem** — pure vector calculus, true for any well-behaved field. The second is the physics. Together: measuring $\mathbf{E}$ on a closed surface tells you how much charge is inside, and nothing about how it is arranged, or about any charge outside.

Take $S$ to be a cube of half-width $h$ centred on the origin, faces on grid planes. On the $+x$ face the outward normal is $+\hat{\mathbf{a}}_x$, so it contributes $\int\!\!\int E_x\,dy\,dz$; on the $-x$ face the normal is $-\hat{\mathbf{a}}_x$ and the same integral enters negatively. Six faces, three pairs.

### Task 9 — close the surface

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


# Task 9  (using the blob field Ex_b, Ey_b, Ez_b from Task 8)
#   1. Finish closed_box_flux above.
#   2. For h = 0.6, 1.0 and 1.4 m, print three numbers in V*m and check they
#      agree: the surface integral; the volume integral of div_blob over the
#      same cube (fw.volume_integral(div_blob[s, s, s], dx, dy, dz), with
#      i0, i1 = fw.box_indices(X, h)); and the enclosed charge, the volume
#      integral of rho over that cube divided by epsilon_0.
#   3. Keep the h = 1.0 m surface integral as `flux_1m` -- the self-check
#      below needs that exact name.
#   4. Now settle Task 7 by measurement rather than by argument: print
#      closed_box_flux for fields (b) and (c). Both look like they are
#      throwing fluid outwards somewhere; a closed surface is the arbiter.

# Write your code here:



# --- self-check (leave this alone) ---
i0, i1 = fw.box_indices(X, 1.0)
s = slice(i0, i1 + 1)
fw.check_scalar("closed-surface flux = Q_enc/eps0", flux_1m,
                fw.volume_integral(rho[s, s, s], dx, dy, dz) / epsilon_0,
                rtol=0.01, unit=" V*m")
fw.check_scalar("divergence theorem: surface = volume", flux_1m,
                fw.volume_integral(div_blob[s, s, s], dx, dy, dz),
                rtol=0.01, unit=" V*m")
```

:::{admonition} Solution — Task 9
:class: dropdown

```python
    flux_y = (fw.area_integral(Ay[s, i1, s], dx, dz)
              - fw.area_integral(Ay[s, i0, s], dx, dz))
    flux_z = (fw.area_integral(Az[s, s, i1], dx, dy)
              - fw.area_integral(Az[s, s, i0], dx, dy))
    return flux_x + flux_y + flux_z


flux_1m = closed_box_flux(Ex_b, Ey_b, Ez_b, 1.0)          # step 6

print(f"{'h [m]':>6} {'surface':>12} {'volume':>12} {'Q_enc/eps0':>12}")
for h in (0.6, 1.0, 1.4):
    i0, i1 = fw.box_indices(X, h)
    s = slice(i0, i1 + 1)
    surf = closed_box_flux(Ex_b, Ey_b, Ez_b, h)
    vol = fw.volume_integral(div_blob[s, s, s], dx, dy, dz)
    qenc = fw.volume_integral(rho[s, s, s], dx, dy, dz) / epsilon_0
    print(f"{h:6.1f} {surf:12.3f} {vol:12.3f} {qenc:12.3f}")

zero = np.zeros_like(X)
print(f"\nflux of (b), the rotation : {closed_box_flux(-Y, X, zero, 1.0):+.2e}")
print(f"flux of (c), the shear    : {closed_box_flux(X, -Y, zero, 1.0):+.2e}")
```
:::

:::{admonition} Three routes, one number
:class: important

Three genuinely different calculations. The first never looks inside the box; the second never looks at the surface; the third never looks at the field at all. They agree to a fraction of a percent.

The number grows with $h$ and then stops: once the cube holds essentially all the charge, enlarging it adds surface but no charge. Charge outside a closed surface contributes exactly nothing — the field lines it sends in through one wall leave through another.
:::

### And now shrink the source to a point

Run the same surface integral on the point-charge field from Task 4 — the one whose divergence you could never measure at the origin, because you had to mask it away.

```{code-cell} ipython3
for h in (0.6, 1.0, 1.4):
    print(f"h = {h:.1f} m :  flux = {closed_box_flux(Ex, Ey, Ez, h):8.3f} V*m"
          f"   (Q/eps0 = {Q / epsilon_0:.3f} V*m)")

shell = interior & (r > 0.5) & (r < 1.6)
div_point = divergence(np.nan_to_num(Ex), np.nan_to_num(Ey), np.nan_to_num(Ez), dx, dy, dz)
scale = (E_mag / Rs)[shell]                # the natural size of a derivative of E here
print(f"\n|div E| away from the origin: median {np.median(np.abs(div_point[shell]) / scale):.2%} "
      f"of |E|/r -- zero to within the accuracy of the grid")
```

:::{admonition} Where did the charge go?
:class: important

Every box returns $Q/\varepsilon_0$, yet the divergence is zero everywhere you can measure — *exactly* zero, by the spherical calculation above — and the boxes share nothing but the origin.

So the whole source sits at one point, where $\nabla\cdot\mathbf{E}$ is not a large number but no number at all: $\rho$ has become a **Dirac delta**, zero everywhere, infinite at one point, with a finite integral $Q$. The integral form survives exactly where the differential form breaks down.

The same statement for magnetism carries no source term at all:

$$ \nabla\cdot\mathbf{B} = 0 \qquad\Longleftrightarrow\qquad \oint_S \mathbf{B}\cdot d\mathbf{s} = 0 \ \ \text{for every closed } S $$

Run this measurement around any closed surface anywhere and you get zero: there are no magnetic monopoles, and field lines of $\mathbf{B}$ never begin and never end.
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
    rho_t = rho0 * np.exp(-rt**2 / a**2)
    E_Rt = rho0 / (epsilon_0 * Rst**2) * (
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

So the 1.06% in Task 8 is not noise to be tolerated: it is a number you can predict, and buy down if you need to. And the choice of $n = 61$ in Part 0 is now yours to audit rather than take on trust.
:::

---

## Closing

Today's chain, in one line:

$$ \rho \;\longrightarrow\; V \;\xrightarrow{\ -\nabla\ }\; \mathbf{E} \;\xrightarrow{\ \nabla\cdot\ }\; \rho/\varepsilon_0 $$

- **Gradient** — scalar in, vector out. Points along steepest increase, perpendicular to the level surfaces, with length equal to the rate of increase.
- **Divergence** — vector in, scalar out. Net flux per unit volume: what is being created here, and nothing else.

### The same two operators, elsewhere in ECT

Electrostatics is the convenient place to *learn* this pair, not the only place to use it. Every row below is a potential, its gradient, and a statement about sources — and the numerical machinery you wrote today applies unchanged to all of them:

| System | Potential | Field | Source equation |
| :--- | :--- | :--- | :--- |
| Electrostatics | $V$ [V] | $\mathbf{E} = -\nabla V$ &nbsp; [V/m] | $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ |
| Gravitation | $\Phi$ [J/kg] | $\mathbf{g} = -\nabla \Phi$ &nbsp; [m/s$^2$] | $\nabla\cdot\mathbf{g} = -4\pi G\rho_m$ |
| Heat conduction | $T$ [K] | $\mathbf{q}_T = -k\nabla T$ &nbsp; [W/m$^2$] | $\nabla\cdot\mathbf{q}_T = 0$ (steady, no sources) |
| Groundwater flow | $h$ [m] | $\mathbf{q}_h = -K\nabla h$ &nbsp; [m/s] | $\nabla\cdot\mathbf{q}_h = 0$ (steady, incompressible) |

with $k$ the thermal conductivity [W m$^{-1}$ K$^{-1}$] and $K$ the hydraulic conductivity [m/s].

The minus signs are all the same minus sign: heat flows from hot to cold, water flows from high head to low, a positive charge falls from high potential to low. Flow runs downhill, and the gradient points uphill.

The last two rows are why a solenoidal field matters so much in practice. $\nabla\cdot\mathbf{q} = 0$ in an aquifer is not an approximation of convenience — it is conservation of water written locally.

### What is still missing

Go back to field **(b)**, the rotation. Its divergence is zero everywhere, so by that measure it is indistinguishable from a field doing nothing at all. But it plainly *is* doing something — it circulates, and every streamline closes on itself.

Divergence cannot see circulation. The operator that can is the **curl**, the third of the three this chapter is named after.

Keep `fwtools.py` to hand: the later labs in this chapter reuse the same helpers and the same grid conventions.

### Homework

**Exercise A — a heat source in a room.** Replace the spherical blob with a flat rectangular heater, $1.0 \times 0.6$ m in the $z = 0$ plane. A steady point source of power $P$ in a medium of conductivity $k$ raises the temperature as $P/4\pi k R$ — the same $1/R$ you have worked with all afternoon — so superpose a $20 \times 12$ grid of them over the rectangle, exactly as you superposed two charges in Task 5:

$$ T(\mathbf{r}) = \frac{P}{4\pi k}\sum_i \frac{\Delta A}{\lvert \mathbf{r} - \mathbf{r}_i \rvert}, \qquad k_{\text{air}} = 0.026\ \text{W m}^{-1}\text{K}^{-1} $$

with $P$ the total power (take 100 W) and $\Delta A$ the area each sample represents. Then:

- Plot the isosurfaces. Close to the plate they should be rounded rectangles; far away they should become spheres. Why does the shape forget its source?
- Compute the heat flux $\mathbf{q} = -k\nabla T$ — the same minus sign, the same reason.
- Check that $\nabla\cdot\mathbf{q} \approx 0$ away from the heater, and that the closed-surface flux through a box containing the plate is *not* zero. State what each result means physically for a room at steady state.

**Exercise B — the $R^n$ family.** Using $\nabla g(R) = \dfrac{dg}{dR}\hat{\mathbf{a}}_R$, derive $|\nabla R| = 1$ and $|\nabla(1/R)| = 1/R^2$ on paper, then find which power $n$ in $R^{n}$ gives a field falling off as $1/R^{3}$.

**Exercise C — why $1/R^2$, and not any other power.** Compute the flux of $\hat{\mathbf{a}}_R/R^{n}$ through spheres of two different radii. Show that it is independent of radius only for $n = 2$, and connect that to the fact that we live in three dimensions. This is the deepest reason Coulomb's law has the exponent it has.

**Exercise D — the same argument in cylindrical coordinates.** An infinite line charge of density $\lambda$ on the $z$-axis produces

$$ \mathbf{E} = \frac{\lambda}{2\pi\varepsilon_0 r}\,\hat{\mathbf{a}}_r $$

with $r$ now the distance from the *axis*, not the origin. Use the cylindrical divergence from the table to show $\nabla\cdot\mathbf{E} = 0$ for $r > 0$, in one line — note which power of $r$ makes $rA_r$ constant, and compare it with the $R^2E_R$ of the spherical case. Then take a cylinder of radius $r$ and length $L$ about the axis and show its flux is $\lambda L/\varepsilon_0$, independent of $r$. Why is the exponent 1 here where it was 2 before?
