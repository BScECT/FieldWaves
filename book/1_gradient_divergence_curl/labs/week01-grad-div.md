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

# Gradient and Divergence

:::{admonition} Computer lab
:class: note

A practical companion to the lecture notes on the gradient and the divergence. You build both operators yourself, in three dimensions, and then use them to recover a charge distribution from nothing but its field.
:::

## Learning objectives

By the end of this session you should be able to:

- **Read a gradient off a picture.** Explain why $\nabla f$ is perpendicular to the level surfaces of $f$, why $\nabla r = \hat{\mathbf{a}}_R$, and why the single minus sign in $\mathbf{E} = -\nabla V$ is the step from geometry to physics.
- **Distinguish "arrows spreading apart" from divergence.** Compute $\nabla\cdot\mathbf{A}$ for fields that look like sources and are not, and justify the answer with a flux argument rather than with algebra.
- **Use Gauss's law as a measurement.** Verify $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ pointwise, verify the divergence theorem $\oint_S\mathbf{E}\cdot d\mathbf{s} = \int_v \nabla\cdot\mathbf{E}\,dv$ numerically, and explain what happens to both when the source shrinks to a point.

## How this lab works

**You write the code.** Each task states a physical question, gives you the steps, and ends with a self-check you can run. What we supply is the *plotting*, in a module called `fwtools` — drawing a transparent isosurface teaches you nothing about electromagnetism, so your time goes on physics instead.

**Nine tasks.** The scaffolding thins out as the afternoon goes on: the first tasks have blanks to fill, the last ones give you an empty cell and a list of steps. After each task there is a dropdown solution — open it *after* you have tried, or when you have been stuck on syntax for more than a couple of minutes.

---

## Part 0 — Setup

```{code-cell} ipython3
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

for _p in (".", "week-01-Grad-Div", "/week-01-Grad-Div", "book/1_gradient_divergence_curl/labs"):
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

K = 1.0 / (4.0 * np.pi * epsilon_0)     # Coulomb constant, 8.99e9 V*m/C
Q = 1e-9                                # 1 nC test charge

print(f"epsilon_0 = {epsilon_0:.4e} F/m")
print(f"K         = {K:.4e} V*m/C")
```

:::{admonition} What that middle block is for
:class: dropdown

Live Code runs Python inside your browser using Pyodide. Pyodide ships numpy, scipy and matplotlib but not plotly, and plotly in turn refuses to draw anything unless it can find a package called `nbformat` — which it uses only to convince itself that it is running in a notebook. The block installs both, then locates `fwtools.py`, whose position depends on whether you are in JupyterLab or in the browser's virtual filesystem. Running locally, none of those branches execute.
:::

Everything in this lab lives on one cube of sample points.

```{code-cell} ipython3
X, Y, Z, dx, dy, dz = fw.make_grid_3d(n=61, L=2.0)

print(f"grid shape {X.shape},  spacing {dx:.4f} m,  {X.size:,} sample points")
print(f"domain: {X.min():.1f} m to {X.max():.1f} m on each axis")
```

:::{admonition} Grid convention — two rules for the whole afternoon
:class: tip

The grid is built with `indexing='ij'`, so axis 0 is $x$, axis 1 is $y$, axis 2 is $z$.

1. **Derivatives come back in coordinate order:** `np.gradient(f, dx, dy, dz)` returns $\partial f/\partial x$, $\partial f/\partial y$, $\partial f/\partial z$. No transposes.
2. **Always pass the spacings.** Omit them and the derivative is silently wrong by a factor of $1/\Delta x = 15$.

Numpy's default is `indexing='xy'`, which returns the $y$-derivative first. That one fact is the origin of a large fraction of all numerical field bugs.
:::

---

## Part 1 — The distance function, and what its gradient is

Before any physics, one piece of pure geometry. The simplest scalar field there is:

$$ r(x,y,z) = \sqrt{(x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2} $$

*How far am I from that point?* One number at every location in space. No charge, no potential, no units of anything — just distance.

### Task 1 — build the distance field

```{code-cell} ipython3
# Task 1 -- distance from a source at (x0, y0, z0) to every point of the grid.

def distance_to(X, Y, Z, x0=0.0, y0=0.0, z0=0.0):
    return np.sqrt(___ + ___ + ___)


r = distance_to(___, ___, ___)          # source at the origin

# --- self-check (leave this alone) ---
c = X.shape[0] // 2                       # index of the origin
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

A surface on which $r$ takes one fixed value is an **isosurface**, or level set — the three-dimensional version of a contour line on a map. Draw a few, with transparency, so the inner ones show through the outer ones.

```{code-cell} ipython3
fw.show_isosurfaces(X, Y, Z, r, levels=[0.5, 1.0, 1.5],
                    title="Isosurfaces of the distance function r")
```

**Drag the figure to rotate it.** They are nested spheres — which is only to say that "all the points 1 metre from here" *is* a sphere. Nothing deeper than that. But keep the picture in mind: in a moment the gradient will turn out to be perpendicular to these surfaces, and that will not be a coincidence.

### Task 2 — the gradient of the distance

Compute $\nabla r$. Before you run anything, predict two things and write them down: **which way** the arrows point, and **how long** they are.

Then test the prediction quantitatively. The outward unit radial vector is $\hat{\mathbf{a}}_R = (x\,\hat{\mathbf{a}}_x + y\,\hat{\mathbf{a}}_y + z\,\hat{\mathbf{a}}_z)/r$, so the radial part of any vector field $\mathbf{A}$ is $\mathbf{A}\cdot\hat{\mathbf{a}}_R$. If $\nabla r$ is *purely* radial, that projection recovers its full magnitude and nothing is left over.

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

fw.show_cones(X, Y, Z, ___, ___, ___, step=8,
              title="grad r -- unit vectors pointing away from the source")

# --- self-check (leave this alone) ---
band = (r > 0.4) & (r < 1.6)
fw.check_shape("grad r", grx, X.shape)
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

fw.show_cones(X, Y, Z, grx, gry, grz, step=8,
              title="grad r -- unit vectors pointing away from the source")
```
:::

:::{admonition} The magnitude is 1. Everywhere.
:class: important

That is not a numerical accident.

Walk one metre directly away from the source point and your distance from it increases by exactly one metre. The steepest possible rate of change of $r$ is therefore 1 metre per metre — a slope of 1 — no matter where you are standing. So

$$ \nabla r = \hat{\mathbf{a}}_R $$

This is the cleanest illustration of what a gradient *is*: a direction of steepest increase, carrying a length equal to that rate of increase.

The second check says something else worth having. The arrows are perpendicular to the spheres because moving *along* a sphere does not change $r$ at all — and a direction that produces no change contributes nothing to the gradient. That argument holds for every scalar field: **$\nabla f$ is always normal to the level surfaces of $f$.**
:::

:::{admonition} A rule you will use twice more today
:class: tip

Any field that depends on position only through $r$ — call it $g(r)$ — has level surfaces that are spheres, so its gradient must be radial. Its magnitude is just the ordinary derivative:

$$ \nabla g(r) = \frac{dg}{dr}\,\hat{\mathbf{a}}_R $$

Task 2 is the case $g = r$, giving $\nabla r = 1\cdot\hat{\mathbf{a}}_R$. **Use this rule to predict the next two tasks before you run them.**
:::

---

## Part 2 — Invert it, and watch the arrows turn round

Now the function the physics actually uses: not the distance, but **one over** the distance,

$$ f(r) = \frac{1}{r}, \qquad\text{so}\qquad \nabla f = \frac{d}{dr}\!\left(\frac{1}{r}\right)\hat{\mathbf{a}}_R = -\frac{1}{r^{2}}\,\hat{\mathbf{a}}_R $$

Same spheres as isosurfaces — $f$ is constant wherever $r$ is constant. But the *ordering* has been turned inside out: $f$ is now largest near the source and decays to nothing far away. Predict what that does to the arrows, then check the prediction against the formula above, then measure it.

### Task 3 — the gradient of the inverse distance

```{code-cell} ipython3
# The mask keeps the singularity at r = 0 off the grid. Everything within
# 0.25 m of the source becomes NaN and is simply not measured.
r_masked = np.where(r < 0.25, np.nan, r)
f = 1.0 / r_masked

# Task 3
#   1. grad f, as components fx, fy, fz; then its magnitude f_mag.
#   2. Print f_mag against the predicted 1/r^2 at r = 0.6, 1.0 and 1.5 m.
#   3. Draw it with normalise=True (direction only -- the magnitude spans
#      three orders of magnitude across this box and would swamp the picture).

# Write your code here:



# --- self-check (leave this alone) ---
interior = np.zeros_like(r, dtype=bool)
interior[2:-2, 2:-2, 2:-2] = True         # np.gradient is one-sided at the edges
outside = (r > 0.5) & interior
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
              title="grad(1/r) -- pointing back towards the source")
```
:::

:::{admonition} The gradient points towards *increase* — always
:class: important

The arrows have reversed. Same spheres, same source, opposite direction:

$$ \nabla r = +\hat{\mathbf{a}}_R, \qquad\qquad \nabla\!\left(\frac{1}{r}\right) = -\frac{1}{r^{2}}\,\hat{\mathbf{a}}_R $$

Nothing about space changed. What changed is **which way the function climbs**. And the steepness changed too: $1/r$ climbs ever faster as you approach the source, so its gradient grows as $1/r^2$ rather than staying at 1.

A gradient knows nothing about sources, sinks, charges or fields. It only knows uphill.
:::

### Task 4 — from geometry to physics

Here the physics enters, and it enters as a single minus sign. The electric potential of a point charge $q$ is the inverse-distance function with a constant in front,

$$ V(r) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}\quad[\text{V}], $$

and the electric field is *defined* as

$$ \mathbf{E} = -\nabla V \quad[\text{V/m}]. $$

You already know what $\nabla V$ does: it points inward, uphill towards the charge. The minus sign turns it round, so **the field points downhill** — which is exactly the way a positive test charge released from rest would move, losing potential energy as it goes.

```{code-cell} ipython3
V = K * Q / r_masked

# Task 4
#   1. E = -grad V, as components Ex, Ey, Ez; then E_mag.
#   2. Compare E_mag against the analytic K*Q/r^2 at a few radii, in V/m.
#   3. Draw it with normalise=True and confirm it points OUTWARD for q > 0.

# Write your code here:



# --- self-check (leave this alone) ---
fw.check_close("|E| = q/(4 pi eps0 r^2)", E_mag, K * Q / r_masked**2,
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
          f"analytic = {K*Q/rr**2:8.3f} V/m")

fw.show_cones(X, Y, Z, Ex, Ey, Ez, step=8, normalise=True,
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

$$ V_{\text{total}} = \frac{1}{4\pi\varepsilon_0}\left(\frac{q_1}{r_1} + \frac{q_2}{r_2}\right) $$

**Superposition** for the potential is nothing more than adding two numbers at every point, because $V$ is a scalar. Adding the two *fields* instead would mean a vector sum at every point in the cube.

Since $\nabla$ is a linear operator, $-\nabla(V_1 + V_2) = \mathbf{E}_1 + \mathbf{E}_2$ exactly. So the efficient route is: **add the potentials, then take one gradient at the very end.** Nothing is lost.

### Task 5 — build a dipole

```{code-cell} ipython3
# Distances to two sources placed on the x-axis, both masked as before.
r_plus = np.where(distance_to(X, Y, Z, -0.5, 0.0, 0.0) < 0.25, np.nan,
                  distance_to(X, Y, Z, -0.5, 0.0, 0.0))
r_minus = np.where(distance_to(X, Y, Z, +0.5, 0.0, 0.0) < 0.25, np.nan,
                   distance_to(X, Y, Z, +0.5, 0.0, 0.0))

# Task 5
#   1. Superpose the potentials of +Q at (-0.5, 0, 0) and -Q at (+0.5, 0, 0)
#      into V_dip. Scalar addition -- just a sum.
#   2. Take ONE gradient, negate it: Ex_d, Ey_d, Ez_d.
#   3. Draw the z = 0 plane, potential as colour and field as streamlines:
#          fw.show_field_slice(X, Y, Z, Ex_d, Ey_d, background=V_dip,
#                              title=..., label="$V$ [V]")
#      then plt.show().

# Write your code here:



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
V_dip = K * Q / r_plus + K * (-Q) / r_minus

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
                    colorscale="RdBu", opacity=0.3,
                    title="Equipotential surfaces of a dipole")
```

---

## Part 4 — Divergence: is anything being created here?

The gradient took a scalar and returned a vector. The divergence goes the other way — hand it a vector field, get back a scalar:

$$ \nabla\cdot\mathbf{A} \;=\; \lim_{\Delta v \to 0}\frac{1}{\Delta v}\oint_S \mathbf{A}\cdot d\mathbf{s} \;=\; \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z} $$

Read the definition on the left, not the formula on the right. **Think of $\mathbf{A}$ as the velocity of a fluid.** Draw a small box anywhere. Measure how much fluid flows out through its walls, subtract how much flows in, divide by the volume of the box, and shrink the box. That number is the divergence:

| $\nabla\cdot\mathbf{A}$ | Name | Picture |
| :---: | :--- | :--- |
| $> 0$ | **source** | a tap — more leaves than arrives |
| $< 0$ | **sink** | a drain — more arrives than leaves |
| $= 0$ | **solenoidal** | whatever flows in, flows out |

### Task 6 — write the divergence

```{code-cell} ipython3
# Task 6
#   Write divergence(Ax, Ay, Az, dx, dy, dz) returning
#   dAx/dx + dAy/dy + dAz/dz. You need one component from each of three
#   separate gradient calls -- the x-derivative of Ax, the y-derivative of
#   Ay, the z-derivative of Az. The cross terms are not part of a divergence.

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
    dAx_dx = np.gradient(Ax, dx, dy, dz)[0]
    dAy_dy = np.gradient(Ay, dx, dy, dz)[1]
    dAz_dz = np.gradient(Az, dx, dy, dz)[2]
    return dAx_dx + dAy_dy + dAz_dz
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
# Task 7
#   1. Build the three fields as triples of arrays.
#   2. Take the divergence of each with your Task 6 function; print the mean.
#   3. Draw field (c) in the z = 0 plane with fw.show_field_slice(...) and
#      look hard at it before reading the note below.

# Write your code here:



# --- self-check (leave this alone) ---
fw.check_close("(a) div = 3", div_a, 3.0, rtol=1e-6)
fw.check_close("(b) div = 0 (rotation)", div_b + 1.0, 1.0, rtol=1e-6)
fw.check_close("(c) div = 0 (shear)", div_c + 1.0, 1.0, rtol=1e-6)
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

fw.show_field_slice(X, Y, Z, *Ac[:2], title="(c) shear flow: divergence zero", density=1.1)
plt.show()
```
:::

:::{admonition} Field (c) is the one that costs marks
:class: warning

Along the $x$-axis, field (c) rushes *outward*, away from the origin. It looks like a source. It is not:

$$ \nabla\cdot\mathbf{A} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(-y) = 1 - 1 = 0 $$

Put a small box at the origin. Fluid pours out through the left and right walls — and pours in through the top and bottom at exactly the same rate. The parcel of fluid is stretched into a different **shape**, but its **volume** never changes. Nothing is created.

*Arrows pointing apart* is not the same as *divergence*. Divergence is net flux through a closed surface, and outflow in one direction can be cancelled exactly by inflow in another. Field (b) is the easy version of this idea; field (c) is the one that catches people.
:::

### Task 8 — the divergence as a charge detector

Maxwell's first equation says

$$ \nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0} $$

which is a strong claim: **the divergence of $\mathbf{E}$ at a point tells you the charge density at that point and nothing else.** Wherever there is no charge, $\mathbf{E}$ is solenoidal, however dramatically its arrows spread out.

Test that pointwise on a real source. Not a point charge — that is an idealisation with infinite density at one location, and no grid can hold it. Take instead a charge **smeared over a finite blob**, which is what any actual charged object is:

$$ \rho(R) = \rho_0\,e^{-R^{2}/a^{2}}, \qquad a = 0.5\ \text{m} $$

Applying Gauss's law to a sphere of radius $R$ gives the field directly (bookwork — you do not need to do this integral now):

$$ E_R(R) = \frac{\rho_0}{\varepsilon_0 R^{2}}\left[\frac{a^{3}\sqrt{\pi}}{4}\operatorname{erf}\!\left(\frac{R}{a}\right) - \frac{a^{2}R}{2}e^{-R^{2}/a^{2}}\right] $$

```{code-cell} ipython3
from scipy.special import erf

a, rho0 = 0.5, 1e-9

# Task 8
#   1. rho = rho0 * exp(-r^2 / a^2) on the grid.
#   2. E_R from the formula above, using Rs in the denominators.
#   3. Turn the radial magnitude into components along a_R:
#      Ex_b = E_R * aRx, and likewise for y and z.
#   4. div_blob = divergence(...), and compare it against rho / epsilon_0
#      everywhere -- including inside the source.
#   5. Plot both, side by side, in the z = 0 plane:
#          fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
#          fw.show_scalar_slice(..., ax=axes[0], cmap="magma", title=...)

# Write your code here:



# --- self-check (leave this alone) ---
peak = np.nanmax(rho / epsilon_0)
err = np.nanmax(np.abs(div_blob[interior] - (rho / epsilon_0)[interior])) / peak
fw.check(f"div E = rho/eps0 pointwise (worst {err:.2%} of peak)", err < 0.05,
         "check the component construction Ex_b = E_R * aRx")
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

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
fw.show_scalar_slice(X, Y, Z, div_blob, ax=axes[0], cmap="magma",
                     title=r"measured $\nabla\cdot\mathbf{E}$")
fw.show_scalar_slice(X, Y, Z, rho / epsilon_0, ax=axes[1], cmap="magma",
                     title=r"actual $\rho/\varepsilon_0$")
plt.show()

print(f"peak of rho/eps0    : {np.nanmax(rho/epsilon_0):8.2f}")
print(f"peak of measured div: {np.nanmax(div_blob):8.2f}")
```
:::

:::{admonition} What you just did
:class: important

The two pictures are the same picture. You never told the code where the charge was — you handed it a *field*, differentiated it, and the charge distribution came back out. That is Gauss's law working as an instrument rather than a formula.

Notice also where the divergence is zero: everywhere outside the blob, where the field is still large and still spreading vigorously. **Strong field, zero divergence.** The two ideas are unrelated.
:::

---

## Part 5 — Flux, and the divergence theorem

Part 4 used the *differential* form of Gauss's law, which is local: it compares two numbers at the same point. The *integral* form is global, and connects a volume to the surface that encloses it:

$$ \oint_S \mathbf{E}\cdot d\mathbf{s} \;=\; \int_v \nabla\cdot\mathbf{E}\;dv \;=\; \frac{Q_{\text{enc}}}{\varepsilon_0} $$

The first equality is the **divergence theorem**, and it is pure vector calculus — true for any well-behaved vector field, charge or no charge. The second is the physics. Together they say something remarkable: measuring $\mathbf{E}$ on a closed surface tells you how much charge is inside, and *nothing whatever* about how that charge is arranged, or about any charge outside.

You will now evaluate all three quantities independently and see them agree.

Take $S$ to be a cube of half-width $h$ centred on the origin, with faces on grid planes. On the $+x$ face the outward normal is $+\hat{\mathbf{a}}_x$, so that face contributes $\int\!\!\int E_x\,dy\,dz$; on the $-x$ face the normal is $-\hat{\mathbf{a}}_x$ and the same integral enters with a minus sign. Six faces, three pairs.

### Task 9 — close the surface

```{code-cell} ipython3
# `fw.area_integral(F2, da, db)` integrates a 2-D array over the face it
# spans; `fw.volume_integral(F3, dx, dy, dz)` does the same over a box.
# `fw.box_indices(X, h)` gives the index range of the cube |x|,|y|,|z| <= h.
#
# Task 9  (using the blob field Ex_b, Ey_b, Ez_b from Task 8)
#   1. For h = 0.6, 1.0 and 1.4 m, get i0, i1 = fw.box_indices(X, h) and
#      s = slice(i0, i1 + 1).
#   2. Surface integral. The +x face is Ex_b[i1, s, s] and the -x face is
#      Ex_b[i0, s, s]; their contribution is the difference of the two area
#      integrals, with dy and dz as the spacings. Add the y and z pairs.
#      Wrap this in a function closed_box_flux(Ax, Ay, Az, half_width) --
#      the next section reuses it on a different field.
#   3. Volume integral of div_blob over the same cube: div_blob[s, s, s].
#   4. Enclosed charge: volume integral of rho over the same cube, then
#      divide by epsilon_0.
#   5. Print all three, in V*m, for each h. They should agree.

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
def closed_box_flux(Ax, Ay, Az, half_width):
    """Net outward flux of a vector field through a cube of half-width h."""
    i0, i1 = fw.box_indices(X, half_width)
    s = slice(i0, i1 + 1)
    return (
        fw.area_integral(Ax[i1, s, s], dy, dz) - fw.area_integral(Ax[i0, s, s], dy, dz)
        + fw.area_integral(Ay[s, i1, s], dx, dz) - fw.area_integral(Ay[s, i0, s], dx, dz)
        + fw.area_integral(Az[s, s, i1], dx, dy) - fw.area_integral(Az[s, s, i0], dx, dy)
    )


print(f"{'h [m]':>6} {'surface':>12} {'volume':>12} {'Q_enc/eps0':>12}")
for h in (0.6, 1.0, 1.4):
    i0, i1 = fw.box_indices(X, h)
    s = slice(i0, i1 + 1)
    surf = closed_box_flux(Ex_b, Ey_b, Ez_b, h)
    vol = fw.volume_integral(div_blob[s, s, s], dx, dy, dz)
    qenc = fw.volume_integral(rho[s, s, s], dx, dy, dz) / epsilon_0
    print(f"{h:6.1f} {surf:12.3f} {vol:12.3f} {qenc:12.3f}")

flux_1m = closed_box_flux(Ex_b, Ey_b, Ez_b, 1.0)
```
:::

:::{admonition} Three routes, one number
:class: important

The three columns are three genuinely different calculations. The first never looks inside the box — it only samples $\mathbf{E}$ on a surface. The second never looks at the surface — it differentiates the field throughout the interior. The third never looks at the field at all — it integrates the charge you put there. They agree to a fraction of a percent.

Notice how the number grows with $h$ and then stops: once the cube contains essentially all of the Gaussian blob, enlarging it further adds surface area but no charge, and the flux settles at $Q_{\text{total}}/\varepsilon_0$. Charge outside a closed surface contributes exactly nothing to the flux through it — the extra field lines it sends in through one wall come straight out through another.
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

Every box returns $Q/\varepsilon_0$. Yet the divergence is zero at every point you are able to measure, and the boxes have nothing in common except the origin.

So the entire source sits at a single point, and $\nabla\cdot\mathbf{E}$ there is not a large number — it is not a number at all. What $\rho$ has become is a **Dirac delta**: zero everywhere, infinite at one point, with a finite integral $q$. This is precisely the situation the integral form was made for, and the reason it survives where the differential form breaks down.

One more consequence, for later in the course. Another of Maxwell's equations is

$$ \nabla\cdot\mathbf{B} = 0 \qquad\Longleftrightarrow\qquad \oint_S \mathbf{B}\cdot d\mathbf{s} = 0 \ \ \text{for every closed } S $$

with no source term on the right at all. Run this measurement on a magnetic field, around any surface anywhere in the universe, and you get zero — there are no magnetic monopoles. Field lines of $\mathbf{B}$ never begin and never end.
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
| Electrostatics | $V$ [V] | $\mathbf{E} = -\nabla V$ | $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ |
| Gravitation | $\Phi$ [J/kg] | $\mathbf{g} = -\nabla \Phi$ | $\nabla\cdot\mathbf{g} = -4\pi G\rho_m$ |
| Heat conduction | $T$ [K] | $\mathbf{q} = -k\nabla T$ | $\nabla\cdot\mathbf{q} = 0$ (steady, no sources) |
| Groundwater flow | $h$ [m] | $\mathbf{q} = -K\nabla h$ | $\nabla\cdot\mathbf{q} = 0$ (steady, incompressible) |

The minus signs are all the same minus sign: heat flows from hot to cold, water flows from high head to low, a positive charge falls from high potential to low. Flow runs downhill, and the gradient points uphill.

The last two rows are why a solenoidal field matters so much in practice. $\nabla\cdot\mathbf{q} = 0$ in an aquifer is not an approximation of convenience — it is conservation of water written locally.

### What is still missing

Go back to field **(b)**, the rotation. Its divergence is zero everywhere, so by that measure it is indistinguishable from a field doing nothing at all. But it plainly *is* doing something — it circulates, and every streamline closes on itself.

Divergence cannot see circulation. The operator that can is the **curl**, the third of the three this chapter is named after.

Keep `fwtools.py` to hand: the later labs in this chapter reuse the same helpers and the same grid conventions.

### Homework

**Exercise A — a heat source in a room.** Replace the spherical blob with a flat rectangular heater, say $1.0 \times 0.6$ m in the $z = 0$ plane, built by superposing point sources over the rectangle exactly as you superposed two charges in Task 5. Then:

- Plot the isosurfaces. Close to the plate they should be rounded rectangles; far away they should become spheres. Why does the shape forget its source?
- Compute the heat flux $\mathbf{q} = -k\nabla T$ — the same minus sign, the same reason.
- Check that $\nabla\cdot\mathbf{q} \approx 0$ away from the heater, and that the closed-surface flux through a box containing the plate is *not* zero. State what each result means physically for a room at steady state.

**Exercise B — the $r^n$ family.** Using $\nabla g(r) = \dfrac{dg}{dr}\hat{\mathbf{a}}_R$, derive $|\nabla r| = 1$ and $|\nabla(1/r)| = 1/r^2$ on paper, then find which power $n$ in $r^{n}$ gives a field falling off as $1/r^{3}$.

**Exercise C — why $1/r^2$, and not any other power.** Compute the flux of $\hat{\mathbf{a}}_R/r^{n}$ through spheres of two different radii. Show that the flux is independent of radius only for $n = 2$, and connect that to the fact that we live in three dimensions. This is the deepest reason Coulomb's law has the exponent it has.
