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
  # This page is a workbook: its task cells contain `___` blanks that raise
  # NameError by design, and every later cell depends on variables those tasks
  # define. Executing it at build time would fail the build, so it is switched
  # off for this page alone -- the book-wide setting is untouched. Readers run
  # the code themselves with Live Code.
  execution_mode: 'off'
---

# Gradient and Divergence

:::{admonition} Computer lab
:class: note

A practical companion to the lecture notes on the gradient and the divergence. Here you build both operators yourself, in three dimensions, and look at what they do.
:::

## How this lab works

**You write the code.** Not one line at a time into someone else's function — you write the fields, the operators and the checks. Each task states a physical question, gives you the steps, and ends with a self-check you can run.

What we supply is the *plotting*, in a module called `fwtools`. Drawing a transparent isosurface in plotly is fiddly and teaches you nothing about electromagnetism, so that part is done for you. Your time goes on physics.

**Nine tasks, about ten minutes each.** After each one there is a dropdown solution. Open it *after* you have tried, or when you are stuck for more than a couple of minutes — being stuck on syntax is not the point of this lab.

**A running theme.** Watch for the moment in Part 2 where a single minus sign turns a piece of geometry into a piece of physics.

---

## Part 0 — Setup

Run these two cells. The first imports what we need; the second builds the cube of sample points that everything else lives on.

```{code-cell} ipython3
import sys, pathlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0

# Live Code runs Python in your browser, on Pyodide. Pyodide bundles numpy,
# scipy and matplotlib, but not plotly -- so fetch it when it is missing.
# Running locally, plotly is already installed and this branch never executes.
try:
    import plotly.io as pio
except ModuleNotFoundError:
    print("Fetching plotly. A few seconds, and only the first time...")
    import micropip
    await micropip.install("plotly")
    import plotly.io as pio

# plotly refuses to display a figure unless it can find nbformat >= 4.2, which
# it uses only to decide that it is running inside a notebook. Pyodide has no
# nbformat, so give it one.
try:
    import nbformat                                    # noqa: F401
except ModuleNotFoundError:
    import micropip, types
    try:
        await micropip.install("nbformat")
    except Exception:
        # nbformat pulls in jsonschema, which may not be installable here.
        # The version string is the only part plotly actually reads.
        _nb = types.ModuleType("nbformat")
        _nb.__version__ = "5.10.4"
        sys.modules["nbformat"] = _nb

# fwtools holds the plotting helpers. Where it sits depends on how you are
# running: your own folder in JupyterLab, or the browser's virtual filesystem
# under Live Code. Look in the likely places rather than assume.
for _p in (".", "week-01-Grad-Div", "/week-01-Grad-Div", "book/week-01-Grad-Div"):
    if (pathlib.Path(_p) / "fwtools.py").exists():
        sys.path.insert(0, _p)
        break
try:
    import fwtools as fw
except ModuleNotFoundError:
    from pyodide.http import pyfetch                     # Live Code only
    _r = await pyfetch("fwtools.py")                     # sits beside this page
    pathlib.Path("fwtools.py").write_bytes(await _r.bytes())
    import fwtools as fw

pio.renderers.default = "plotly_mimetype+notebook"

K = 1.0 / (4.0 * np.pi * epsilon_0)     # the Coulomb constant, 8.99e9 V*m/C
Q = 1e-9                                # 1 nC, a convenient test charge

print(f"epsilon_0 = {epsilon_0:.4e} F/m")
print(f"K         = {K:.4e} V*m/C")
```

```{code-cell} ipython3
X, Y, Z, dx, dy, dz = fw.make_grid_3d(n=61, L=2.0)

print(f"grid shape {X.shape},  spacing {dx:.4f} m,  {X.size:,} sample points")
print(f"X[i,j,k] = x[i]  ->  X[-1, 0, 0] = {X[-1, 0, 0]:.1f} m")
```

:::{admonition} Why `indexing='ij'`, and why you should care
:class: tip

`np.meshgrid` has two conventions. The default, `indexing='xy'`, puts **y on axis 0** — so `np.gradient` hands back the *y*-derivative first, and half of all numerical field bugs come from that one fact.

We use `indexing='ij'` instead, so axis 0 is x, axis 1 is y, axis 2 is z:

```python
dfdx, dfdy, dfdz = np.gradient(f, dx, dy, dz)     # in the order you expect
```

Two rules that follow, and that you will use in every task today:

1. **Always pass the spacings** `dx, dy, dz`. Leave them out and `np.gradient` assumes a spacing of 1, making every derivative wrong by a factor of 15.
2. **Derivatives come back in coordinate order.** No transposes, no surprises.
:::

---

## Part 1 — The distance function, and what its gradient is

Before any physics, one piece of pure geometry. The simplest scalar field there is:

$$ r(x,y,z) = \sqrt{(x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2} $$

*How far am I from that point?* One number at every location in space. No charge, no potential, no units of anything — just distance.

### Task 1 — build the distance field

```{code-cell} ipython3
# Task 1
#   The distance from every grid point to a source at (x0, y0, z0) is
#       r = sqrt( (x-x0)^2 + (y-y0)^2 + (z-z0)^2 )
#   Replace each ___ below. Note that X, Y, Z are whole arrays, so writing
#   (X - x0)**2 squares every point at once -- no loops anywhere today.
#
# Write your code here:

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
# Task 1 solution
def distance_to(X, Y, Z, x0=0.0, y0=0.0, z0=0.0):
    return np.sqrt((X - x0)**2 + (Y - y0)**2 + (Z - z0)**2)


r = distance_to(X, Y, Z)
```
:::

### What does this field look like?

A surface on which $r$ takes one fixed value is called an **isosurface**, or level set — the three-dimensional version of a contour line on a map. Draw a few, with transparency, so you can see through the outer ones to the inner ones.

```{code-cell} ipython3
fw.show_isosurfaces(X, Y, Z, r, levels=[0.5, 1.0, 1.5],
                    title="Isosurfaces of the distance function r")
```

**Drag the figure to rotate it.** They are spheres, nested inside one another — which is only to say that "all the points 1 metre from here" *is* a sphere. Nothing deeper than that. But it is worth seeing, because in a moment the gradient is going to be perpendicular to these surfaces, and that will not be a coincidence.

### Task 2 — the gradient of the distance

Now compute $\nabla r$. Before you run it, predict two things and write them down:

- **which way** do you expect the arrows to point?
- **how long** do you expect them to be?

```{code-cell} ipython3
# Task 2
#   np.gradient returns one array per axis. Because our grid uses
#   indexing='ij', they arrive in the order (d/dx, d/dy, d/dz) -- and you must
#   pass the three spacings, or every derivative is wrong by a factor of 15.
#
#   Fill in the blanks, then look hard at the printed magnitudes.
#
# Write your code here:

grx, gry, grz = np.gradient(___, ___, ___, ___)

grad_r_mag = np.sqrt(___ + ___ + ___)

for name, idx in [("(2,0,0)", (-1, c, c)), ("(0,2,0)", (c, -1, c))]:
    print(f"|grad r| at {name} = {grad_r_mag[idx]:.4f}")

# --- self-check (leave this alone) ---
band = (r > 0.4) & (r < 1.6)
fw.check_shape("grad r", grx, X.shape)
fw.check_close("|grad r| = 1 everywhere", grad_r_mag, 1.0, rtol=0.05, where=band)
```

:::{admonition} Solution — Task 2
:class: dropdown

```python
# Task 2 solution
grx, gry, grz = np.gradient(r, dx, dy, dz)
grad_r_mag = np.sqrt(grx**2 + gry**2 + grz**2)

for (i, j, k), name in [((-1, c, c), "(2,0,0)"), ((c, -1, c), "(0,2,0)")]:
    print(f"|grad r| at {name} = {grad_r_mag[i, j, k]:.4f}")
print(f"|grad r| median away from the origin = "
      f"{np.median(grad_r_mag[(r > 0.4) & (r < 1.6)]):.4f}")
```
:::

:::{admonition} The magnitude is 1. Everywhere.
:class: important

That is not a numerical accident, and it is worth a moment.

Walk one metre directly away from the source point. Your distance from it increases by exactly one metre. The steepest possible rate of change of $r$ is therefore $1$ metre per metre — a slope of 1 — no matter where you are standing.

So the gradient of the distance function is a **unit vector pointing radially outward**:

$$ \nabla r = \hat{\mathbf{a}}_R $$

This is the cleanest possible illustration of what a gradient *is*: the direction of steepest increase, with a length equal to that rate of increase. Here the direction is "away from the source" and the rate is 1.
:::

### Task 3 — see it

```{code-cell} ipython3
# Task 3
#   Draw the gradient field. Fill in the three components, then rotate the
#   figure and compare it with the isosurfaces above: every arrow should
#   pierce the spheres at a right angle.
#
# Write your code here:

fw.show_cones(X, Y, Z, ___, ___, ___, step=8,
              title="grad r -- unit vectors pointing away from the source")
```

:::{admonition} Solution — Task 3
:class: dropdown

```python
# Task 3 solution
fw.show_cones(X, Y, Z, grx, gry, grz, step=8,
              title="grad r -- unit vectors pointing away from the source")
```

The arrows are perpendicular to the spheres because moving *along* a sphere does not change $r$ at all. If a direction produces no change, the gradient has no component along it — so the gradient must be entirely perpendicular to the level surface. That argument works for every scalar field, not just this one.
:::

---

## Part 2 — Invert it, and watch the arrows turn round

Now the function the physics actually uses: not the distance, but **one over** the distance.

$$ f(r) = \frac{1}{r} $$

Same spheres as isosurfaces — $f$ is constant wherever $r$ is constant. But the *ordering* has been turned inside out: $f$ is now largest near the source and decays to nothing far away.

### Task 4 — the gradient of the inverse distance

```{code-cell} ipython3
# Task 4
#   Now the same two steps for f = 1/r. The masking line is given, because
#   dividing by zero at the origin is a detail rather than a lesson. The rest
#   is yours -- it is the same shape as Task 2.
#
#   1. Take the gradient of f. Call the components fx, fy, fz.
#   2. Build its magnitude, f_mag.
#   3. Print f_mag against 1/r^2 at r = 0.6, 1.0 and 1.5 m.
#   4. Predict the DIRECTION first, then draw it:
#          fw.show_cones(X, Y, Z, fx, fy, fz, step=8, normalise=True, title=...)
#
# Write your code here:

r_masked = np.where(r < 0.25, np.nan, r)
f = 1.0 / r_masked



# --- self-check (leave this alone) ---
interior = np.zeros_like(r, dtype=bool)
interior[2:-2, 2:-2, 2:-2] = True         # np.gradient is less accurate at the edges
outside = (r > 0.5) & interior
fw.check_close("|grad(1/r)| = 1/r^2", f_mag, 1.0 / r_masked**2, rtol=0.05, where=outside)
fw.check("grad(1/r) points inward at (1,0,0)", fx[-1 - 15, c, c] < 0)
```

:::{admonition} Solution — Task 4
:class: dropdown

```python
# Task 4 solution
r_masked = np.where(r < 0.25, np.nan, r)
f = 1.0 / r_masked

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

Nothing about space changed. What changed is **which way the function climbs**. $r$ grows as you move away, so $\nabla r$ points away. $1/r$ grows as you move *closer*, so $\nabla(1/r)$ points inward — steeply, as $1/r^2$, because $1/r$ climbs ever faster near the source.

A gradient always points along the direction of maximum increase of its own function. It knows nothing about sources, sinks, charges or fields; it only knows uphill.
:::

### Task 5 — from geometry to physics

Here is where the physics enters, and it enters as a single minus sign.

The electric potential of a point charge $q$ is the inverse-distance function with a constant in front:

$$ V(r) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r} $$

and the electric field is defined as

$$ \mathbf{E} = -\nabla V $$

You already know what $\nabla V$ does: it points *inward*, uphill towards the charge. The minus sign turns it round. **The field points downhill** — which is exactly what a positive test charge released from rest would do, running away from a positive source and losing potential energy as it goes.

```{code-cell} ipython3
# Task 5
#   The potential is given. Everything after it is yours.
#
#   1. Get E = -grad V. Call the components Ex, Ey, Ez.
#   2. Build E_mag, and compare it against the analytic K*Q/r^2 at a few radii.
#   3. Draw it with normalise=True and confirm it points OUTWARD for q > 0.
#
# Write your code here:

V = K * Q / r_masked



# --- self-check (leave this alone) ---
fw.check_close("|E| = q/(4 pi eps0 r^2)", E_mag, K * Q / r_masked**2,
               rtol=0.05, where=outside)
fw.check("E points outward at (1,0,0)", Ex[-1 - 15, c, c] > 0)
```

:::{admonition} Solution — Task 5
:class: dropdown

```python
# Task 5 solution
V = K * Q / r_masked

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

---

## Part 3 — Two sources: a source and a sink

One charge is symmetric enough to be boring. Put down two.

$$ V_{\text{total}} = \frac{1}{4\pi\varepsilon_0}\left(\frac{q_1}{r_1} + \frac{q_2}{r_2}\right) $$

This is **superposition**, and for the potential it is nothing more than adding two numbers at every point — because $V$ is a scalar. Adding the two *fields* instead would mean a vector sum at every point in the cube.

So the efficient route, and the reason the potential is worth defining at all, is: **add the potentials, then take one gradient at the very end.** The gradient is a linear operator, so this loses nothing.

### Task 6 — build a dipole

```{code-cell} ipython3
# Task 6
#   A source and a sink. The two masked distances are given; build the physics
#   on top of them.
#
#   1. Superpose the potentials: +Q at (-0.5, 0, 0) and -Q at (+0.5, 0, 0).
#      Call the result V_dip. Remember this is scalar addition -- just a sum.
#   2. Take ONE gradient, and negate it, to get Ex_d, Ey_d, Ez_d.
#   3. Draw the z = 0 plane:
#          fw.show_field_slice(X, Y, Z, Ex_d, Ey_d, background=V_dip,
#                              title=..., label="$V$ [V]")
#      That puts the potential lines (colour) and the field lines (streamlines)
#      on one picture. Follow it with plt.show().
#
# Write your code here:

r_plus = np.where(distance_to(X, Y, Z, -0.5, 0.0, 0.0) < 0.25, np.nan,
                  distance_to(X, Y, Z, -0.5, 0.0, 0.0))
r_minus = np.where(distance_to(X, Y, Z, +0.5, 0.0, 0.0) < 0.25, np.nan,
                   distance_to(X, Y, Z, +0.5, 0.0, 0.0))



# --- self-check (leave this alone) ---
mid = np.abs(X) < 1e-9                    # the plane x = 0, halfway between the charges
fw.check_shape("V_dip", V_dip, X.shape)
fw.check("V = 0 on the mid-plane",
         np.nanmax(np.abs(V_dip[mid])) < 1e-6 * np.nanmax(np.abs(V_dip)))
fw.check("E on the mid-plane points from + to -", np.nanmean(Ex_d[mid]) > 0)
```

:::{admonition} Solution — Task 6
:class: dropdown

```python
# Task 6 solution
r_plus = np.where(distance_to(X, Y, Z, -0.5, 0.0, 0.0) < 0.25, np.nan,
                  distance_to(X, Y, Z, -0.5, 0.0, 0.0))
r_minus = np.where(distance_to(X, Y, Z, +0.5, 0.0, 0.0) < 0.25, np.nan,
                   distance_to(X, Y, Z, +0.5, 0.0, 0.0))

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

That catches people out every year. The field is the *slope* of the potential, not its value. A landscape can be at sea level and still be steep.
:::

Now look at the same object in three dimensions. Positive and negative isosurfaces, drawn together and transparent:

```{code-cell} ipython3
lobe = np.nanpercentile(np.abs(V_dip), 97)
fw.show_isosurfaces(X, Y, Z, np.nan_to_num(V_dip), levels=[-lobe, -lobe/3, lobe/3, lobe],
                    colorscale="RdBu", opacity=0.3,
                    title="Equipotential surfaces of a dipole")
```

---

## Part 4 — Divergence: is anything being created here?

The gradient took a scalar and gave back a vector. The divergence goes the other way — hand it a vector field, get back a scalar:

$$ \nabla\cdot\mathbf{A} \;=\; \lim_{\Delta v \to 0}\frac{1}{\Delta v}\oint_S \mathbf{A}\cdot d\mathbf{s} \;=\; \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z} $$

**Think of $\mathbf{A}$ as the velocity of a fluid.** Draw a small box anywhere. Measure how much fluid flows out through its walls, subtract how much flows in, and divide by the volume of the box. That number is the divergence:

| $\nabla\cdot\mathbf{A}$ | Name | Picture |
| :---: | :--- | :--- |
| $> 0$ | **source** | a tap — more leaves than arrives |
| $< 0$ | **sink** | a drain — more arrives than leaves |
| $= 0$ | **solenoidal** | whatever flows in, flows out |

### Task 7 — write the divergence

```{code-cell} ipython3
# Task 7
#   Write divergence(Ax, Ay, Az, dx, dy, dz) returning dAx/dx + dAy/dy + dAz/dz.
#
#   You need one component from each of three np.gradient calls. Remember the
#   order: np.gradient(Ax, dx, dy, dz)[0] is dAx/dx, index [1] is dAx/dy, and
#   so on. You want [0] from the first, [1] from the second, [2] from the third.
#
# Write your code here:



# --- self-check (leave this alone) ---
# A = x a_x + y a_y + z a_z is the position vector itself. Its divergence is
# 1 + 1 + 1 = 3, everywhere -- work it out on paper and confirm.
fw.check_close("div of the position vector = 3",
               divergence(X, Y, Z, dx, dy, dz), 3.0, rtol=1e-6)
```

:::{admonition} Solution — Task 7
:class: dropdown

```python
# Task 7 solution
def divergence(Ax, Ay, Az, dx, dy, dz):
    dAx_dx = np.gradient(Ax, dx, dy, dz)[0]
    dAy_dy = np.gradient(Ay, dx, dy, dz)[1]
    dAz_dz = np.gradient(Az, dx, dy, dz)[2]
    return dAx_dx + dAy_dy + dAz_dz
```
:::

### Task 8 — three flows

Three velocity fields. For each one: **sketch it in your head, predict the sign of the divergence, then measure.** Write your predictions down before running anything — the point of this task is the gap between intuition and the answer.

| | Field $\mathbf{A}$ | What it looks like |
| :---: | :--- | :--- |
| **(a)** | $x\,\hat{\mathbf{a}}_x + y\,\hat{\mathbf{a}}_y + z\,\hat{\mathbf{a}}_z$ | flow rushing outward in all directions |
| **(b)** | $-y\,\hat{\mathbf{a}}_x + x\,\hat{\mathbf{a}}_y$ | fluid rotating about the $z$-axis |
| **(c)** | $x\,\hat{\mathbf{a}}_x - y\,\hat{\mathbf{a}}_y$ | stretching along $x$, squeezing along $y$ |

```{code-cell} ipython3
# Task 8
#   1. Build the three fields as triples of arrays. np.zeros_like(X) is a
#      useful zero component.
#   2. Compute the divergence of each with your Task 7 function, and print
#      the mean of each.
#   3. Draw field (c) in the z = 0 plane with fw.show_field_slice(...) and
#      look hard at it before reading the note below.
#
# Write your code here:



# --- self-check (leave this alone) ---
fw.check_close("(a) div = 3", div_a, 3.0, rtol=1e-6)
fw.check_close("(b) div = 0 (rotation)", div_b + 1.0, 1.0, rtol=1e-6)
fw.check_close("(c) div = 0 (shear)", div_c + 1.0, 1.0, rtol=1e-6)
```

:::{admonition} Solution — Task 8
:class: dropdown

```python
# Task 8 solution
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

*Arrows pointing apart* is not the same as *divergence*. Divergence is about net flux through a closed surface, and outflow in one direction can be cancelled exactly by inflow in another. Field (b) is the easy version of this idea; field (c) is the one that catches people.
:::

### Task 9 — the divergence as a charge detector

For the electric field, Maxwell's first equation says

$$ \nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0} $$

which is a strong claim: **the divergence of $\mathbf{E}$, evaluated at a point, tells you the charge density at that point and nothing else.** Where there is no charge, $\mathbf{E}$ is solenoidal, however dramatically its arrows spread out.

Let us check that, pointwise, on a real source. Not a point charge — a point charge is a mathematical idealisation with infinite density at one location, and no grid can represent that. Instead take a charge **smeared over a finite blob**, which is what any actual charged object is:

$$ \rho(R) = \rho_0\,e^{-R^{2}/a^{2}}, \qquad a = 0.5\ \text{m} $$

Applying Gauss's law to a sphere of radius $R$ gives the field directly (you do not need to do this integral now — it is bookwork):

$$ E_R(R) = \frac{\rho_0}{\varepsilon_0 R^{2}}\left[\frac{a^{3}\sqrt{\pi}}{4}\operatorname{erf}\!\left(\frac{R}{a}\right) - \frac{a^{2}R}{2}e^{-R^{2}/a^{2}}\right] $$

```{code-cell} ipython3
from scipy.special import erf

a, rho0 = 0.5, 1e-9

# Task 9
#   1. Build rho = rho0 * exp(-r^2 / a^2) on the grid.
#   2. Build the radial field magnitude E_R from the formula above. Use
#      Rs = np.maximum(r, 1e-9) in the denominators -- there is no singularity
#      in this problem, but 0/0 at the exact centre still needs care.
#   3. Turn it into components: Ex_b = E_R * X/Rs, and likewise for y and z.
#   4. Take the divergence with your Task 7 function, and compare it against
#      rho / epsilon_0 -- everywhere, including inside the blob.
#   5. Plot both, side by side, in the z = 0 plane.
#
# Write your code here:



# --- self-check (leave this alone) ---
peak = np.nanmax(rho / epsilon_0)
err = np.nanmax(np.abs(div_blob[interior] - (rho / epsilon_0)[interior])) / peak
fw.check(f"div E = rho/eps0 pointwise (worst {err:.2%} of peak)", err < 0.05,
         "check the component construction Ex = E_R * X/Rs")
```

:::{admonition} Solution — Task 9
:class: dropdown

```python
# Task 9 solution
Rs = np.maximum(r, 1e-9)
rho = rho0 * np.exp(-r**2 / a**2)

E_R = rho0 / (epsilon_0 * Rs**2) * (
    (a**3 * np.sqrt(np.pi) / 4) * erf(Rs / a) - (a**2 * Rs / 2) * np.exp(-Rs**2 / a**2)
)
Ex_b, Ey_b, Ez_b = E_R * X / Rs, E_R * Y / Rs, E_R * Z / Rs

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

The two pictures are the same picture. You never told the code where the charge was — you handed it a *field*, took derivatives of it, and the charge distribution came back out.

That is Gauss's law working as an instrument rather than a formula. And notice where the divergence is zero: everywhere outside the blob, where the field is still large and still spreading vigorously. Strong field, zero divergence. The two ideas are unrelated.

One more consequence, for later in the course. Another of Maxwell's equations is

$$ \nabla\cdot\mathbf{B} = 0 $$

with no source term on the right at all. Run this same measurement on a magnetic field, anywhere in the universe, and you get zero — there are no magnetic monopoles. Field lines of $\mathbf{B}$ never begin and never end.
:::

---

## Closing

Today's chain, in one line:

$$ \rho \;\longrightarrow\; V \;\xrightarrow{\ -\nabla\ }\; \mathbf{E} \;\xrightarrow{\ \nabla\cdot\ }\; \rho/\varepsilon_0 $$

- **Gradient** — scalar in, vector out. Points along steepest increase, perpendicular to the level surfaces.
- **Divergence** — vector in, scalar out. Measures what is being created, and nothing else.

### What is still missing

Go back to field **(b)**, the rotation. Its divergence is zero everywhere, so by that measure it is indistinguishable from a field doing nothing whatsoever. But it plainly *is* doing something — it circulates, and every streamline closes on itself.

Divergence cannot see circulation. The operator that can is the **curl** — the third of the three operators this chapter is named after.

Keep `fwtools.py` to hand: the later labs in this chapter reuse the same helpers and the same grid conventions.

### Homework

**Exercise A — a heat source in a room.** Replace the spherical blob with a **square** one: a flat rectangular heater, say $1.0 \times 0.6$ m in the $z=0$ plane. Build its temperature field by superposing point sources over a grid of positions covering the rectangle, exactly as you superposed two charges in Task 6. Then:

- Plot the isosurfaces. Close to the heater they should be rounded rectangles; far away they should become spheres. Why?
- Heat flux is $\mathbf{q} = -k\nabla T$ — the same minus sign, the same reason. Compute it.
- Check that $\nabla\cdot\mathbf{q} \approx 0$ away from the heater. What does that statement mean physically, in a room at steady state?

**Exercise B — where does the $1/r$ come from?** Task 2 showed $|\nabla r| = 1$ and Task 4 showed $|\nabla(1/r)| = 1/r^2$. Using $\nabla g(r) = \dfrac{dg}{dr}\hat{\mathbf{a}}_R$, derive both on paper, and then work out which power $n$ in $r^{n}$ would make the field fall off as $1/r^{3}$.
