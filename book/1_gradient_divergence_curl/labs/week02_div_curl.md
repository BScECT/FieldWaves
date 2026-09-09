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

# Lab 2: Divergence and Curl

:::{admonition} Computer lab
:class: note

The second of two labs on this chapter's operators, following Lab 1 on series and the gradient. Parts 1 and 2 take the divergence, Part 3 the curl. Each task states a physical question, gives the steps, and ends with a self-check. Plotting is supplied in `fwtools`, so your effort goes into the physics.
:::

## Learning objectives

By the end of this lab you should be able to:

- **Distinguish diverging arrows from non-zero divergence.** Compute $\nabla\cdot\boldsymbol{v}$, justify it by flux rather than algebra, and identify the only incompressible radial flow.
- **Use the divergence theorem as a measurement.** Verify $\oint_S\boldsymbol{v}\cdot\hat{\boldsymbol{n}}\,dS = \int_{\mathcal{D}} \nabla\cdot\boldsymbol{v}\,dV$ numerically, and say what a closed surface can measure that a derivative at a point cannot.
- **Measure the curl as circulation per unit area.** Compute $\nabla\times\boldsymbol{v}$, separate rotation from the shape a streamline happens to make, and verify Stokes' theorem on a vortex with a core.

---

## Part 0 — Setup

Run this once. It contains no physics: it fetches two packages the browser lacks, locates `fwtools`, and defines the Coulomb constant.

```{code-cell} ipython3
# No physics above the k_e = ... line near the bottom.
import sys, pathlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0

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

### Carried over from Lab 1

The same cube of sample points, and the fields Lab 1 built on it. Nothing here is an
exercise: these are Lab 1's answers, given so that this notebook runs on its own.

```{code-cell} ipython3
n, L = 61, 2.0                          # odd n, so the origin is a sample point
axis = np.linspace(-L, L, n)            # one axis, shared by x, y and z
X, Y, Z = np.meshgrid(axis, axis, axis, indexing="ij")
dx = dy = dz = axis[1] - axis[0]

c = n // 2                              # index of the origin
# Mask reused by the self-checks. `interior` drops the two outermost cells,
# so comparisons exclude the six faces of the box, where sampling is worst
# and np.gradient has only one-sided neighbours.
interior = np.zeros(X.shape, dtype=bool)
interior[2:-2, 2:-2, 2:-2] = True

print(f"grid shape {X.shape},  spacing {dx:.4f} m,  {X.size:,} sample points")
print(f"X[i,j,k] = x[i]   ->   X[-1, 0, 0] = {X[-1, 0, 0]:.1f} m")
```

```{figure} figures/part0_interior_mask.svg
:name: fig-interior-mask
:width: 100%

What `interior` keeps, and why. On the six faces of the box `np.gradient` has no neighbour on one side, so it falls back to a one-sided difference that is first order instead of second. The mask drops two layers rather than one because several fields here are built with `np.gradient` and then differentiated again, and each differentiation carries the boundary error one cell further in.
```

```{code-cell} ipython3
# Lab 1, Tasks 3, 4, 6 and 7 -- given here, not set again.
def distance_to(X, Y, Z, x0=0.0, y0=0.0, z0=0.0):
    return np.sqrt((X - x0)**2 + (Y - y0)**2 + (Z - z0)**2)

r  = distance_to(X, Y, Z)                 # distance from the origin
rs = np.maximum(r, 1e-12)                 # 0/0 at the source is not a lesson
rhx, rhy, rhz = X / rs, Y / rs, Z / rs    # the outward unit radial vector

r_masked = np.where(r < 0.25, np.nan, r)  # the singularity kept off the grid
V = k_e * Q / r_masked                    # potential of the 1 nC point charge
_dVx, _dVy, _dVz = np.gradient(V, dx, dy, dz)
Ex, Ey, Ez = -_dVx, -_dVy, -_dVz          # E = -grad V

print(f"grid {X.shape},  spacing {dx:.4f} m")
print(f"|E| at (1,0,0) = {np.sqrt(Ex**2+Ey**2+Ez**2)[-1-15, c, c]:.3f} V/m")
```

---

## Part 1 — Divergence

The gradient takes a scalar and returns a vector. The divergence takes a vector field and returns a scalar:

$$ \nabla\cdot\boldsymbol{A} \;=\; \lim_{\Delta V \to 0}\frac{1}{\Delta V}\oint_S \boldsymbol{A}\cdot\hat{\boldsymbol{n}}\,dS \;=\; \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z} $$

Read the definition on the left, not the formula on the right: **treat $\boldsymbol{A}$ as a fluid velocity**, put a small box anywhere, and measure the net outflow through its walls per unit volume.

| $\nabla\cdot\boldsymbol{A}$ | Name | Picture |
| :---: | :--- | :--- |
| $> 0$ | **source** | a tap: more leaves than arrives |
| $< 0$ | **sink** | a drain: more arrives than leaves |
| $= 0$ | **solenoidal** | whatever flows in, flows out |

### Task 1 — the operator, and its independence of the origin

The operator is three lines, one derivative along one axis per component: `np.gradient(Ax, dx, axis=0)` returns $\partial A_x/\partial x$ and nothing else. The cross terms are not part of a divergence.

**The definition raises its own question.** Flux per unit volume is measured around a point, so does the answer depend on which point is called the origin? Take $\boldsymbol{A} = \boldsymbol{r}$, whose divergence is $1+1+1 = 3$ on paper, then shift the field so it streams out of $(0.8, -0.4, 0.3)$. Predict the divergence before computing it.

```{code-cell} ipython3
# Task 1
def divergence(Ax, Ay, Az, dx, dy, dz):
    return (np.gradient(Ax, dx, axis=0)
            + ___
            + ___)

# The same outward flow, seen from somewhere else.
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

:::{admonition} Solution — Task 1
:class: dropdown

```python
def divergence(Ax, Ay, Az, dx, dy, dz):
    return (np.gradient(Ax, dx, axis=0)
            + np.gradient(Ay, dy, axis=1)
            + np.gradient(Az, dz, axis=2))

Sx, Sy, Sz = X - x0, Y - y0, Z - z0
div_shifted = divergence(Sx, Sy, Sz, dx, dy, dz)
```
:::

:::{admonition} Why the answer had to be 3 either way
:class: tip

Moving the source changed every arrow and changed the divergence nowhere, because differentiation removes the constant: $\partial(x - x_0)/\partial x = 1$ for any $x_0$.

The divergence is **local**. It is built from a limit around one point, so it depends on the field in a shrinking neighbourhood and not on where the axes were put. Every operator in this course has that property, and it is what makes $\nabla\cdot\boldsymbol{E} = \rho_v/\varepsilon_0$ a statement about places rather than about coordinate systems.
:::

### Task 2 — the only incompressible radial flow

Water of constant density flows outward from a source at the origin. Away from that source nothing is created or destroyed, so the flow is **incompressible**, $\nabla\cdot\boldsymbol{v} = 0$ for $r \neq 0$. Constant density and a point source force it to be radial, $\boldsymbol{v} = f(r)\,\boldsymbol{r}$, and incompressibility then pins $f$ down:

$$ \nabla\cdot\boldsymbol{v} = 3f(r) + r\frac{df}{dr} = 0 \qquad\Longrightarrow\qquad f(r) = \frac{A}{r^{3}}. $$

Rather than take that on trust, put four radial fields through the operator and let the measurement pick the survivor. Each is $\boldsymbol{v} = f(r)\,\boldsymbol{r}$, and they differ only in the falloff $f$:

| $f(r)$ | the field it gives | why it is in the list |
| :--- | :--- | :--- |
| $\text{const}$ | $\boldsymbol{v} = \boldsymbol{r}$ | the anchor: Task 1 already measured its divergence as 3 |
| $1/r^{2}$ | $\hat{\boldsymbol{r}}/r$ | falls off, but too slowly |
| $1/r^{3}$ | $\hat{\boldsymbol{r}}/r^{2}$ | the one the algebra above predicts |
| $1/r^{4}$ | $\hat{\boldsymbol{r}}/r^{3}$ | falls off too steeply |

Three of them should show a divergence somewhere and one should not.

Raw divergences cannot be compared, because the four fields are not the same size: $f = 1/r^{4}$ returns a *smaller* $\lvert\nabla\cdot\boldsymbol{v}\rvert$ than $f = \text{const}$ does, and neither is divergence-free. "Is 0.36 small?" has no answer until it is small compared with something. That something is the size a derivative of the same field would have if nothing cancelled, and for $f(r)\boldsymbol{r}$ the only distance available is $r$ itself, which makes $\lvert\boldsymbol{v}\rvert/r$ the yardstick:

$$ \frac{\lvert\nabla\cdot\boldsymbol{v}\rvert}{\lvert\boldsymbol{v}\rvert/r} $$

**1 means the three terms did not cancel at all, 0 means they cancelled completely**, and the number is the same for a trickle and a torrent. The cell prints the raw divergence beside it so you can see why the raw column is unusable.

The $f = \text{const}$ row is known in advance: there $\lvert\boldsymbol{v}\rvert/r = 1$ and the ratio is just $\nabla\cdot\boldsymbol{r} = 3$, which is why the last self-check looks for 300%.

```{figure} figures/task2_test_band.svg
:name: fig-task2-band
:width: 92%

The band the median is taken over. Inside $r = 0.3$ the field is singular and those samples are masked. The outer limit at $r = 1.6$ keeps the band clear of the faces of the box, where `np.gradient` is worst; the corners lie well outside it. A median over what is left cannot be moved by a single bad sample.
```

```{code-cell} ipython3
# The statistic, restated: |div v| / (|v|/r), median over the test band.
# The band avoids the source, where the field is singular, and the outer
# corners of the box, where np.gradient runs out of neighbours.

r_safe = np.where(r < 0.3, np.nan, r)
band_i = interior & (r > 0.6) & (r < 1.6)

# Task 2 -- three blanks, inside the loop.
results, raws = {}, {}
print(f"  {'f(r)':>7}  {'|div v|':>11}  {'|v|/r':>8}  {'ratio':>9}")
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
    raws[name] = np.nanmedian(np.abs(dv[band_i]))
    results[name] = np.nanmedian(np.abs(dv[band_i]) / scale)
    print(f"  {name:>7}  {raws[name]:11.4f}  {np.nanmedian(scale):8.4f}"
          f"  {results[name]:9.2%}")

# --- self-check (leave this alone) ---
fw.check(f"the raw column cannot rank these: 1/r^4 gives a smaller |div v| "
         f"({raws['1/r^4']:.3f}) than f = const ({raws['const']:.3f}), and "
         f"neither is divergence-free", raws["1/r^4"] < raws["const"])
fw.check(f"scale is one value per band point ({np.shape(scale)} vs "
         f"{np.shape(dv[band_i])})", np.shape(scale) == np.shape(dv[band_i]),
         "index it with [band_i] -- a whole-grid array or a single median "
         "both change the statistic being reported")
fw.check(f"1/r^3 is the divergence-free one ({results['1/r^3']:.2%})",
         results["1/r^3"] < 0.05)
fw.check("...and the other three are not",
         min(results[k] for k in ("const", "1/r^2", "1/r^4")) > 0.5)
fw.check(f"f = const reproduces Task 1's div(r) = 3 ({results['const']:.2%})",
         np.isclose(results["const"], 3.0, rtol=1e-3))
```

:::{admonition} Solution — Task 2
:class: dropdown

```python
    vx, vy, vz = f_r*X, f_r*Y, f_r*Z
    dv = divergence(*(np.nan_to_num(q) for q in (vx, vy, vz)), dx, dy, dz)
    scale = (np.sqrt(vx**2 + vy**2 + vz**2) / r_safe)[band_i]
```
:::

:::{admonition} Where the inverse-square law comes from
:class: important

Two candidates give almost exactly 100%, their three terms not cancelling at all, and the anchor gives its predicted 300%. One gives 0.66%. Only $f = A/r^{3}$ survives, and the raw column beside it would have told you none of this. It rewrites as

$$ \boldsymbol{v} = \frac{A}{r^{3}}\boldsymbol{r} = \frac{A}{r^{2}}\,\hat{\boldsymbol{r}}. $$

**This is the same $1/r^{2}$ used since Lab 1's Task 6**, here neither assumed nor tied to charge. It follows from conservation away from the source and the three-dimensionality of space: the surface of a sphere grows as $r^{2}$, so a fixed flux crossing it must thin as $1/r^{2}$. Coulomb's law, Newtonian gravity and this flow share an exponent for that one geometric reason.
:::

### Task 2, continued — a field with no source anywhere

That result carried a restriction: $\nabla\cdot\boldsymbol{v} = 0$ **for $r \neq 0$**, the origin excluded because that is where the water is injected. The next field admits no such exception. To first order the Earth's magnetic field is a **dipole**, a north and a south pole so close together that they coincide, and with moment $\boldsymbol{m}$,

$$ \boldsymbol{B} = \frac{3\boldsymbol{r}\,(\boldsymbol{r}\cdot\boldsymbol{m}) - r^{2}\boldsymbol{m}}{r^{5}}. $$

Take $\boldsymbol{m} = \hat{\boldsymbol{z}}$ on the cube above and measure the divergence with the same function. The Earth's own moment points roughly geographic south, which is why the magnetic pole in the Arctic is magnetically a **south** pole; reversing $\boldsymbol{m}$ reverses every arrow and leaves $\nabla\cdot\boldsymbol{B}$ unchanged.

```{code-cell} ipython3
# Task 2, continued -- fill in the three components.
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

:::{admonition} Solution — Task 2, continued
:class: dropdown

```python
Bx = 3*X*r_dot_m / r_safe**5
By = 3*Y*r_dot_m / r_safe**5
Bz = (3*Z*r_dot_m - r_safe**2) / r_safe**5
```
:::

:::{admonition} No magnetic monopoles
:class: important dropdown

Both fields are divergence-free over the region measured, but the statements differ. The flow needed an exclusion, because the origin is a tap. The dipole needs none: $\nabla\cdot\boldsymbol{B} = 0$ holds **everywhere, including at the source**, and no point can be excluded to reveal a magnet leaking field the way the tap leaks water. This is one of Maxwell's equations. Magnetic monopoles do not exist, and field lines of $\boldsymbol{B}$ never begin or end.

Both cells report the same scale-free measure, so the numbers are comparable. The dipole's 1.8% is worse than the radial flow's 0.66% because $\boldsymbol{B}$ falls off as $1/r^{3}$ rather than $1/r^{2}$, leaving a centred difference more curvature to miss. Part 2 builds the alternative, a closed surface integral, which never differentiates the field and so never pays that cost.

The second check matters too: $\boldsymbol{B}\cdot\boldsymbol{r}$ is negative somewhere, whereas the outward flow is never negative. The dipole points inward over part of space, which is the numerical signature of a field closing on itself.
:::

### Task 3 — three flows

Three velocity fields. For each: **sketch it, predict the sign of the divergence, then measure.** Record the predictions first, because the task is about the gap between intuition and the result.

| | Field $\boldsymbol{A}$ | What it looks like |
| :---: | :--- | :--- |
| **(a)** | $x\,\hat{\boldsymbol{x}} + y\,\hat{\boldsymbol{y}} + z\,\hat{\boldsymbol{z}}$ | outward flow in all directions |
| **(b)** | $-y\,\hat{\boldsymbol{x}} + x\,\hat{\boldsymbol{y}}$ | fluid rotating about the $z$-axis |
| **(c)** | $x\,\hat{\boldsymbol{x}} - y\,\hat{\boldsymbol{y}}$ | stretching along $x$, squeezing along $y$ |

```{code-cell} ipython3
# Record the predictions BEFORE running the next cell: +1 for a source,
# -1 for a sink, 0 for solenoidal. The next cell scores them.
predictions = {"a": ___, "b": ___, "c": ___}
```

```{code-cell} ipython3
# Task 3 -- six blanks: three fields, three divergences.
zero = np.zeros_like(X)
Aa = ___                                  # (a) outward flow, as a triple
Ab = ___                                  # (b) rotation about z
Ac = ___                                  # (c) stretch in x, squeeze in y

div_a = ___
div_b = ___
div_c = ___

# --- given: the three side by side, one shared scale, one colorbar ---
for name, d in [("(a) outward flow", div_a), ("(b) rotation", div_b),
                ("(c) straining flow", div_c)]:
    print(f"{name:20s} div = {d.mean():+.3f}")

fig, axes = plt.subplots(1, 3, figsize=(16, 4.6))
for ax_, (name, A, d) in zip(axes, [("(a) outward flow", Aa, div_a),
                                    ("(b) rotation", Ab, div_b),
                                    ("(c) straining flow", Ac, div_c)]):
    fw.show_field_slice(X, Y, Z, *A[:2], background=d, ax=ax_, density=1.1,
                        vmin=-3, vmax=3, colorbar=(ax_ is axes[-1]),
                        label=r"$\nabla\cdot\mathbf{A}$  [s$^{-1}$]", title=name)
plt.tight_layout()
plt.show()
# Examine (b) and (c) before reading the note below: both come out a uniform
# zero, for entirely different reasons.

# --- self-check (leave this alone) ---
# (a) has a non-zero answer, so a relative test works. (b) and (c) are exactly
# zero, and nothing can be measured relative to zero, so they get an absolute
# tolerance instead.
fw.check_close("(a) div = 3", div_a, 3.0, rtol=1e-6)
fw.check_abs("(b) div = 0 (rotation)", div_b, atol=1e-9)
fw.check_abs("(c) div = 0 (straining flow)", div_c, atol=1e-9)

for key, measured in (("a", div_a), ("b", div_b), ("c", div_c)):
    sign = int(np.sign(np.round(measured.mean(), 6)))
    verdict = "as predicted" if predictions[key] == sign else "NOT what you predicted"
    print(f"  ({key}) you said {predictions[key]:+d}, measured {sign:+d}  --  {verdict}")
```

:::{admonition} Solution — Task 3
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

:::{admonition} Field (c) is the trap
:class: warning

Along the $x$-axis, field (c) flows outward and looks like a source. It is not:

$$ \nabla\cdot\boldsymbol{A} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(-y) = 1 - 1 = 0 $$

Put a box at the origin: fluid leaves through the left and right walls and enters through the top and bottom at the same rate. The parcel changes **shape**, not **volume**. Diverging arrows are not divergence, and Task 5 measures the cancellation directly.
:::

### Task 4 — the divergence as a charge detector

Gauss's law, for a field in vacuum, says

$$ \nabla\cdot\boldsymbol{E} = \frac{\rho_v}{\varepsilon_0} $$

a strong claim: **the divergence of $\boldsymbol{E}$ at a point gives the charge density at that point and nothing else.** Where there is no charge, $\boldsymbol{E}$ is solenoidal however widely its arrows spread.

Test it pointwise, on a source a grid can hold. A point charge cannot serve, having infinite density at one location, so take a charge **spread over a finite blob**, which is what any real charged object is:

$$ \rho_v(r) = \rho_{v0}\,e^{-r^{2}/a^{2}}, \qquad \rho_{v0} = 10^{-9}\ \text{C/m}^3, \qquad a = 0.5\ \text{m} $$

Here $a$ is the **width of the blob**, not Lab 1's electrode separation; the code keeps them apart as `a` and `a_sep`. Integrating over a sphere of radius $r$ gives the charge enclosed:

$$ Q_{\text{enc}}(r) = \int_0^{r}\!\rho_v\,4\pi r'^{2}\,dr' = 4\pi\rho_{v0}\left[\frac{a^{3}\sqrt{\pi}}{4}\operatorname{erf}\!\left(\frac{r}{a}\right) - \frac{a^{2}r}{2}e^{-r^{2}/a^{2}}\right] $$

and Gauss's law, $E_r = Q_{\text{enc}}/4\pi\varepsilon_0r^{2}$, then gives the field, with the $4\pi$ cancelling:

$$ E_r(r) = \frac{\rho_{v0}}{\varepsilon_0 r^{2}}\left[\frac{a^{3}\sqrt{\pi}}{4}\operatorname{erf}\!\left(\frac{r}{a}\right) - \frac{a^{2}r}{2}e^{-r^{2}/a^{2}}\right] $$

Near the centre $Q_{\text{enc}}$ grows as $r^{3}$ while the surface grows as $r^{2}$, so $E_r \to \rho_{v0} r/3\varepsilon_0$: zero at the centre, rising linearly, peaking at $r \approx a$.

```{code-cell} ipython3
from scipy.special import erf

a, rho_v0 = 0.5, 1e-9

# --- given: the charge density, and the field Gauss's law gives it ---
# The two bracketed terms nearly cancel for r << a, so the closed form loses
# accuracy below r ~ 1e-6 m. On this grid the only such sample is the origin,
# where the r-hat components are zero in any case.
rho_v = rho_v0 * np.exp(-r**2 / a**2)
E_r = rho_v0 / (epsilon_0 * rs**2) * (
    (a**3 * np.sqrt(np.pi) / 4) * erf(rs / a) - (a**2 * rs / 2) * np.exp(-rs**2 / a**2)
)

# Task 4 -- two blanks.
#   E_r is a radial MAGNITUDE. Give it a direction, then differentiate.
Ex_b, Ey_b, Ez_b = ___                    # components along (rhx, rhy, rhz)
div_blob = ___                            # your Task 1 operator

# --- given: the two pictures, forced onto one scale so they are comparable ---
hi = float(np.nanmax(rho_v / epsilon_0))
units = r"[V m$^{-2}$]"
fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))
fw.show_scalar_slice(X, Y, Z, div_blob, ax=axes[0], cmap="magma", label=units,
                     vmin=0, vmax=hi, title=r"measured $\nabla\cdot\mathbf{E}$")
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

:::{admonition} Solution — Task 4
:class: dropdown

```python
Ex_b, Ey_b, Ez_b = E_r * rhx, E_r * rhy, E_r * rhz
div_blob = divergence(Ex_b, Ey_b, Ez_b, dx, dy, dz)
```
:::

:::{admonition} What the two panels show
:class: important

The two panels show the same distribution, and the location of the charge was never supplied to the code: a field was differentiated, and the charge came back out. Note where the divergence vanishes, everywhere outside the blob, where the field is still large and still spreading. **Strong field, zero divergence.**
:::

### The same operator, a different formula

Everything so far used the Cartesian formula, because `np.gradient` differentiates along array axes. Flux per unit volume cannot depend on the choice of axes, so only the formula changes. The three coordinate systems are set out in full in the lecture notes on [coordinate systems](../coord_sys.md) and [divergence](../divergence.md); what matters here is what one of them buys.

Cylindrical $\varrho=\sqrt{x^2+y^2}$ is the distance from the $z$-axis, spherical $r=\sqrt{x^2+y^2+z^2}$ the distance from the origin, and the two are written differently to keep them apart.

Both fields built so far are spherically symmetric, $\boldsymbol{E} = E_r(r)\,\hat{\boldsymbol{r}}$ with no $\theta$ or $\phi$ dependence, so two of the three spherical terms vanish and the divergence reduces to one ordinary derivative along one line:

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

# --- given: the radial profile Task 4 asserted but never drew ---
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
print(f"       Cartesian, from Task 4: {cart_worst:.3%} and {cart_median:.4%}")
print(f"point: r^2 E_r varies by {np.ptp(r_line**2 * E_r_point):.1e} over the whole line")
print(f"       max |div E| = {np.abs(div_point_sph).max():.1e}  (round-off, not physics)")
```

:::{admonition} Why curvilinear coordinates are worth the trouble
:class: important

Same field, same operator, same answer, from a few hundred samples on a line rather than a quarter of a million in a cube, and several times more accurately.

For the point charge the gain is certainty rather than accuracy. $r^{2}E_r = Q/4\pi\varepsilon_0$ is a **constant**, so its derivative is analytically zero for every $r>0$: not 1% of something, but zero, in one line of algebra. What the cell prints is the precision with which double arithmetic subtracts two equal numbers, around $10^{-13}$. Cartesian coordinates could establish only that the divergence is small.

Matching the coordinates to the symmetry of the source replaces three noisy derivatives with one line of algebra. That is what the curvilinear formulae are for.
:::

---

## Part 2 — Flux, and the divergence theorem

Part 1 used the differential form of Gauss's law, which compares two numbers at one point. The integral form relates a volume to the surface enclosing it:

$$ \oint_S \boldsymbol{E}\cdot\hat{\boldsymbol{n}}\,dS \;=\; \int_{\mathcal{D}} \nabla\cdot\boldsymbol{E}\;dV \;=\; \frac{Q_{\text{enc}}}{\varepsilon_0} $$

with $S$ the closed surface, $\hat{\boldsymbol{n}}$ its outward unit normal, and $\mathcal{D}$ the volume it encloses.

The first equality is the **divergence theorem**, valid for any well-behaved field; the second is the physics. Together they say that measuring $\boldsymbol{E}$ on a closed surface gives the charge inside, and nothing about its arrangement or about charge outside.

Take $S$ to be a cube of half-width $h$ centred on the origin, faces on grid planes: six faces, three pairs.

### Task 5 — close the surface

Write that six-face sum as a function of the half-width $h$, then run it on the blob of Task 4, whose enclosed charge is already known two other ways. Three routes to one number is the point of the task.

```{figure} figures/task5_box_faces.svg
:name: fig-task5-faces
:width: 100%

The six faces, taken in pairs. Each pair contributes the face at `i1` minus the face at `i0`. The `i0` term is subtracted because its outward normal points backwards along the pinned axis while the array holds the forward component. The axis you pin to `i0` and `i1` is the axis whose spacing you leave out of `fw.area_integral`.
```

```{code-cell} ipython3
# `fw.area_integral(F2, da, db)` integrates a 2-D array over the face it
# spans; `fw.volume_integral(F3, dx, dy, dz)` does the same over a box.
# `fw.box_indices(X, h)` gives the index range of the cube |x|,|y|,|z| <= h.
#
# The x pair is written for you, and the figure above gives the other two,
# one panel per axis. The axis you pin to i0/i1 is the axis whose spacing you
# leave out.
# NOTE: this closes over X, dx, dy, dz from the cell above, so it is tied to
# this grid and is not a general-purpose function.

def closed_box_flux(Ax, Ay, Az, half_width):
    """Net outward flux through the cube |x|,|y|,|z| <= half_width."""
    i0, i1 = fw.box_indices(X, half_width)
    s = slice(i0, i1 + 1)
    flux_x = (fw.area_integral(Ax[i1, s, s], dy, dz)
              - fw.area_integral(Ax[i0, s, s], dy, dz))
    flux_y = ___
    flux_z = ___
    return flux_x + flux_y + flux_z


# --- given: three routes to the same number, and the Task 3 arbiter ---
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

# Task 3 settled by measurement rather than by argument. Both (b) and (c)
# appear to throw fluid outwards somewhere; a closed surface is the arbiter,
# and it differentiates nothing.
print(f"\nflux of (b), the rotation       : {closed_box_flux(-Y, X, zero, 1.0):+.2e}")
print(f"flux of (c), the straining flow : {closed_box_flux(X, -Y, zero, 1.0):+.2e}")

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

:::{admonition} Solution — Task 5
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

Three independent calculations, agreeing to a fraction of a percent. The first never examines the interior of the box, the second never examines the surface, the third never examines the field.

The result grows with $h$ and then stops: once the cube holds nearly all the charge, enlarging it adds surface but no charge. Charge outside a closed surface contributes nothing, because the field lines it sends in through one wall leave through another.
:::

Here the closed surface buys accuracy. In general it buys more. Concentrate the same charge onto a point and $\rho_v$ stops being a function, so $\nabla\cdot\boldsymbol{E}$ has no value there at all, which is why Task 4 gave its blob a width. The surface integral never visits the source and still returns the charge enclosed. Part 3 meets that case again, in a field whose source really is concentrated.

---

## Part 3 — Curl

Field **(b)**, the rotation, has zero divergence everywhere, yet it plainly circulates. The divergence cannot detect circulation. The operator that can is the **curl**, which takes a vector field and returns another vector field:

$$ \nabla\times\boldsymbol{v} \;=\; \hat{\boldsymbol{x}}\left(\partial_y v_z - \partial_z v_y\right) + \hat{\boldsymbol{y}}\left(\partial_z v_x - \partial_x v_z\right) + \hat{\boldsymbol{z}}\left(\partial_x v_y - \partial_y v_x\right) $$

There is no determinant to memorise. Each component pairs an even permutation of $(x,y,z)$ against an odd one, in three places at once: the direction, the differentiation, and the vector component. The $\hat{\boldsymbol{x}}$ term takes $(x,y,z)$ minus $(x,z,y)$, and the other two follow by advancing every letter one step, $x\to y\to z\to x$.

The [notes on the curl](../curl.md) derive what that means by walking a small rectangle and expanding each edge to first order. The result is the definition this part measures, **net circulation per unit area**:

$$ \hat{\boldsymbol{n}}\cdot\left(\nabla\times\boldsymbol{v}\right) \;=\; \lim_{S\to 0}\frac{\oint_{\boldsymbol{r}}\boldsymbol{\tau}\cdot\boldsymbol{v}\;dl}{A} $$

with $A$ the area of the open surface $S$ and $\hat{\boldsymbol{n}}$ its unit normal, oriented by the right-hand rule from the direction of travel $\boldsymbol{\tau}$. Part 1 built the divergence from flux through a closed surface; the curl is built from circulation around a closed curve, one dimension down.

### Task 6 — the operator, and the three flows again

Three lines, in the pattern of the formula above: `np.gradient(Az, dy, axis=1)` is $\partial_y v_z$, the array holding the $z$-component differentiated along the $y$-axis. Put the three fields of Task 3 through it, predicting all three first. Field (b) rotates rigidly about $z$ at $\omega = 1$ s$^{-1}$; fields (a) and (c) carry no rotation.

```{code-cell} ipython3
# Task 6 -- two blanks. The x-component is given. Advance every letter one
# step, x -> y -> z -> x, in the direction, the differentiation and the
# component, and the other two lines write themselves.
def curl(Ax, Ay, Az, dx, dy, dz):
    cx = np.gradient(Az, dy, axis=1) - np.gradient(Ay, dz, axis=2)
    cy = ___
    cz = ___
    return cx, cy, cz

# --- given: the three fields of Task 3, through the new operator, and one
#     more. Field (d) is the same rigid rotation turned onto the y-axis, so
#     its curl is 2 y-hat: it is here to exercise the second line you wrote,
#     which the three planar fields above leave at zero whatever you put in it.
Ad = (Z, zero, -X)
curl_a, curl_b = curl(*Aa, dx, dy, dz), curl(*Ab, dx, dy, dz)
curl_c, curl_d = curl(*Ac, dx, dy, dz), curl(*Ad, dx, dy, dz)

for name, w in [("(a) outward flow", curl_a), ("(b) rotation about z", curl_b),
                ("(c) straining flow", curl_c), ("(d) rotation about y", curl_d)]:
    print(f"{name:22s} curl = ({w[0].mean():+.2f}, {w[1].mean():+.2f}, {w[2].mean():+.2f})")

fig, axes = plt.subplots(1, 3, figsize=(16, 4.6))
for ax_, (name, A, w) in zip(axes, [("(a) outward flow", Aa, curl_a),
                                    ("(b) rotation", Ab, curl_b),
                                    ("(c) straining flow", Ac, curl_c)]):
    fw.show_field_slice(X, Y, Z, *A[:2], background=w[2], ax=ax_, density=1.1,
                        vmin=-3, vmax=3, colorbar=(ax_ is axes[-1]),
                        label=r"$(\nabla\times\mathbf{A})_z$  [s$^{-1}$]", title=name)
plt.tight_layout()
plt.show()

# --- self-check (leave this alone) ---
# Each test reads the whole vector, not one component: a sign slip in `cy`
# leaves every planar field untouched and would otherwise pass unnoticed.
def _mag(w):
    return np.sqrt(w[0]**2 + w[1]**2 + w[2]**2)

fw.check_abs("(a) curl = 0 (outward flow)", _mag(curl_a), atol=1e-9)
fw.check_abs("(c) curl = 0 (straining flow)", _mag(curl_c), atol=1e-9)
fw.check_close("(b) curl = 2 z-hat", curl_b[2], 2.0, rtol=1e-6)
fw.check_abs("...and nothing along x or y",
             np.abs(curl_b[0]) + np.abs(curl_b[1]), atol=1e-9)
fw.check_close("(d) curl = 2 y-hat", curl_d[1], 2.0, rtol=1e-6,
               where=interior)
fw.check_abs("...and nothing along x or z",
             (np.abs(curl_d[0]) + np.abs(curl_d[2]))[interior], atol=1e-9)
```

:::{admonition} Solution — Task 6
:class: dropdown

```python
    cy = np.gradient(Ax, dz, axis=2) - np.gradient(Az, dx, axis=0)
    cz = np.gradient(Ay, dx, axis=0) - np.gradient(Ax, dy, axis=1)
```
:::

:::{admonition} Divergence and curl are independent, and field (c) is zero in both
:class: important dropdown

The three flows of Task 3 now carry two answers each, and neither constrains the other:

| | Field $\boldsymbol{A}$ | $\nabla\cdot\boldsymbol{A}$ | $\nabla\times\boldsymbol{A}$ |
| :---: | :--- | :---: | :---: |
| **(a)** | $x\,\hat{\boldsymbol{x}} + y\,\hat{\boldsymbol{y}} + z\,\hat{\boldsymbol{z}}$ | $3$ | $\boldsymbol{0}$ |
| **(b)** | $-y\,\hat{\boldsymbol{x}} + x\,\hat{\boldsymbol{y}}$ | $0$ | $2\,\hat{\boldsymbol{z}}$ |
| **(c)** | $x\,\hat{\boldsymbol{x}} - y\,\hat{\boldsymbol{y}}$ | $0$ | $\boldsymbol{0}$ |

"How much is created here" and "how much does this spin here" are separate measurements. Field (c) answers zero to both and is still not the zero field: it stretches a parcel along $x$ and squeezes it along $y$ at equal rates, changing shape while conserving volume and orientation. Deformation is the third thing a flow can do, and neither operator reports it.

For rigid rotation at angular velocity $\boldsymbol{\omega}$ the curl is $2\boldsymbol{\omega}$ whatever the axis, which is why (b) returns $2\hat{\boldsymbol{z}}$ and (d) returns $2\hat{\boldsymbol{y}}$. In fluid mechanics $\nabla\times\boldsymbol{v}$ is the **vorticity**, twice the local angular velocity of a parcel.
:::

### Task 7 — closed streamlines are not curl

Task 3 established that arrows spreading apart do not make a divergence. The same error has the same shape here: **the picture a streamline makes says nothing about the curl.** Two fields settle it, with the rotation of Task 6 as a control, both written on the cylindrical $\varrho = \sqrt{x^2+y^2}$ rather than the spherical $r$ of Parts 1 and 2.

| | Field | Streamlines |
| :---: | :--- | :--- |
| **rotation** | $\omega\,\varrho\,\hat{\boldsymbol{\phi}} \;=\; -y\,\hat{\boldsymbol{x}} + x\,\hat{\boldsymbol{y}}$ | concentric circles |
| **shear** | $\sigma\,y\,\hat{\boldsymbol{x}}$ | straight lines, all parallel to $x$ |
| **line vortex** | $\dfrac{\Gamma_0}{2\pi\varrho}\hat{\boldsymbol{\phi}} \;=\; \Gamma_0\dfrac{-y\,\hat{\boldsymbol{x}} + x\,\hat{\boldsymbol{y}}}{2\pi\varrho^{2}}$ | concentric circles |

with $\omega = 1$ s$^{-1}$, shear rate $\sigma = 1$ s$^{-1}$ and $\Gamma_0 = 2\pi$ m$^2$/s, so all three curls come out in s$^{-1}$ and one colour scale serves the row.

The shear is the water beside a riverbank: further out it runs faster, but every parcel travels in a straight line and none goes round anything. The line vortex circles the axis exactly as the rotation does, and falls off as $1/\varrho$. Predict the sign of $(\nabla\times\boldsymbol{v})_z$ for each, then measure.

```{code-cell} ipython3
# +1 for anticlockwise rotation, -1 for clockwise, 0 for none.
curl_predictions = {"rotation": ___, "shear": ___, "line vortex": ___}
```

```{code-cell} ipython3
# --- given: distance from the z-axis, and a test region that avoids it ---
varrho = np.sqrt(X**2 + Y**2)
varrho_s = np.maximum(varrho, 1e-12)      # the axis kept out of the denominators
ring = interior & (varrho > 0.4) & (varrho < 1.6)

# Task 7 -- two blanks, one field each. Both lie in the z = 0 plane, so the
# third component of each is `zero`. Take Gamma_0 / 2*pi = 1, as above.
A_shear = ___                             # y x-hat, as a triple
A_vortex = ___                            # (-Y, X) / varrho_s**2, as a triple

# --- given ---
curl_shear = curl(*A_shear, dx, dy, dz)
curl_vortex = curl(*A_vortex, dx, dy, dz)

# Reported as the scale-free ratio Task 2 built for the divergence, with the
# distance from the AXIS in place of the distance from the origin: the size of
# the curl against |v|/varrho, the size a derivative of this field would have
# if nothing cancelled. Same reasoning, same reading: 1 means no cancellation.
v_mag = np.sqrt(A_vortex[0]**2 + A_vortex[1]**2)
vortex_ratio = np.median(np.abs(curl_vortex[2][ring]) / (v_mag / varrho_s)[ring])
measured = {"rotation": curl_b[2].mean(), "shear": curl_shear[2][ring].mean(),
            "line vortex": curl_vortex[2][ring].mean()}
print(f"rotation    : curl_z = {measured['rotation']:+.3f} s^-1")
print(f"shear       : curl_z = {measured['shear']:+.3f} s^-1")
print(f"line vortex : |curl_z| / (|v|/varrho) = {vortex_ratio:.2%}  (zero, to grid error)")
# The vortex is zero only to grid error, so the score needs a deadband:
# anything under 5% of the largest curl in the row counts as no rotation.
deadband = 0.05 * max(abs(v) for v in measured.values())
for key, got in measured.items():
    sign = 0 if abs(got) < deadband else int(np.sign(got))
    verdict = "as predicted" if curl_predictions[key] == sign else "NOT what you predicted"
    print(f"  {key:12s} you said {curl_predictions[key]:+d}, measured {sign:+d}  --  {verdict}")

# The vortex is singular on the z-axis. What the operator returns on the few
# cells around it is the grid's difficulty and not the field's, so those cells
# are left blank rather than allowed to dominate the panel.
shown = np.where(varrho < 0.3, np.nan, curl_vortex[2])

fig, axes = plt.subplots(1, 3, figsize=(16, 4.6))
panels = [("rotation", Ab, curl_b[2]), ("shear", A_shear, curl_shear[2]),
          ("line vortex", A_vortex, shown)]
for ax_, (name, A, w) in zip(axes, panels):
    fw.show_field_slice(X, Y, Z, *A[:2], background=w, ax=ax_, density=1.1,
                        vmin=-3, vmax=3, colorbar=(ax_ is axes[-1]),
                        label=r"$(\nabla\times\mathbf{v})_z$  [s$^{-1}$]", title=name)
plt.tight_layout()
plt.show()

# --- self-check (leave this alone) ---
fw.check_close("shear: curl = -1 z-hat, although nothing goes round",
               curl_shear[2][ring], -1.0, rtol=1e-6)
fw.check(f"line vortex: curl = 0, although everything goes round ({vortex_ratio:.2%})",
         vortex_ratio < 0.05)
fw.check("...and it really does circle the axis: v has no radial component",
         np.max(np.abs((A_vortex[0]*X + A_vortex[1]*Y)[ring])) < 1e-12)
```

:::{admonition} Solution — Task 7
:class: dropdown

```python
A_shear = (Y, zero, zero)
A_vortex = (-Y / varrho_s**2, X / varrho_s**2, zero)
```
:::

```{figure} figures/task7_carousel_gondola.svg
:name: fig-task7-wheel
:width: 100%

One paddle wheel, four moments of a single lap, with one blade marked in red. The first two panels carry the *same* circular streamline and opposite answers, so the path cannot be what the curl is measuring. The third has no circular path at all and a non-zero curl.
```

:::{admonition} Going round is not the same as turning
:class: warning

Drop a small paddle wheel into each flow, mark one blade, and watch **the blade** rather than the path the wheel travels.

**Rigid rotation is a carousel.** The wheel is carried round, and the marked blade keeps the same face to the centre. After one lap it has turned once, exactly as a horse bolted to a merry-go-round comes back facing the way it set off. It goes round *and* turns, and $\nabla\times\boldsymbol{v} = 2\omega$.

**The line vortex is a Ferris wheel.** The wheel travels the same circular path, and the marked blade comes back pointing the direction it started. A Ferris-wheel gondola goes right round and stays upright the whole way. It goes round *without* turning, and $\nabla\times\boldsymbol{v} = \boldsymbol{0}$.

Those two have identical streamlines, so the streamline cannot be what is being measured.

**The shear turns the wheel with no circular path at all.** Above the axis the water runs to the right and below it to the left, so the upper blades are pushed one way and the lower blades the other. The wheel turns clockwise at half a radian per second while every parcel of water travels in a straight line.

The cylindrical formula separates the two contributions. For a field $v_\phi(\varrho)\,\hat{\boldsymbol{\phi}}$ with no radial component,

$$ (\nabla\times\boldsymbol{v})_z = \frac{1}{\varrho}\frac{d\left(\varrho\, v_\phi\right)}{d\varrho} \;=\; \underbrace{\frac{v_\phi}{\varrho}}_{\text{orbit}} \;+\; \underbrace{\frac{dv_\phi}{d\varrho}}_{\text{shear}} $$

The **orbit** term is the carousel: a wheel carried round a circle of radius $\varrho$ at speed $v_\phi$ turns once per lap, forwards, at $v_\phi/\varrho$. The **shear** term is the blades: when the inner blade sits in faster water than the outer one, $dv_\phi/d\varrho$ is negative and the wheel is twisted backwards. Put the two fields through it:

| | orbit $v_\phi/\varrho$ | shear $dv_\phi/d\varrho$ | sum |
| :--- | :---: | :---: | :---: |
| rigid rotation, $v_\phi = \omega\varrho$ | $+\omega$ | $+\omega$ | $2\omega$ |
| line vortex, $v_\phi = \Gamma_0/2\pi\varrho$ | $+\Gamma_0/2\pi\varrho^{2}$ | $-\Gamma_0/2\pi\varrho^{2}$ | $0$ |

In the vortex the inner fluid runs faster by exactly the amount needed to twist the wheel backwards once per lap, cancelling the forward turn the orbit gives it. The two terms cancel at $v_\phi \propto 1/\varrho$ and at no other falloff. Their *mean* is the local angular velocity, which is where Task 6's factor of two comes from.

That single surviving field, $\boldsymbol{H} = \dfrac{I}{2\pi\varrho}\hat{\boldsymbol{\phi}}$, is the magnetic field around a straight wire carrying a current $I$. Its curl is zero at every point outside the wire, and the current is still there. The end of this part explains how both can be true.
:::

### Task 8 — circulation per unit area, and Stokes' theorem

A real vortex has a core. Stirred coffee, a tornado and the vortex trailing from a wing all rotate almost rigidly near the axis and fall off as $1/\varrho$ far from it, because viscosity spreads the vorticity over a finite radius $b$. The **Lamb–Oseen vortex** is the exact solution, with $b^{2} = 4\nu t$ in a fluid of kinematic viscosity $\nu$:

$$ v_\phi(\varrho) = \frac{\Gamma}{2\pi\varrho}\left(1 - e^{-\varrho^{2}/b^{2}}\right), \qquad \Gamma = 1\ \text{m}^2\text{/s}, \qquad b = 0.5\ \text{m}. $$

Inside the core this is $\Gamma\varrho/2\pi b^{2}$, the rigid rotation of Task 6; outside it is $\Gamma/2\pi\varrho$, the irrotational vortex of Task 7. Its vorticity is a Gaussian blob:

$$ (\nabla\times\boldsymbol{v})_z = \frac{1}{\varrho}\frac{d}{d\varrho}\left(\varrho\,v_\phi\right) = \frac{\Gamma}{\pi b^{2}}\,e^{-\varrho^{2}/b^{2}} $$

the same shape as Task 4's blob of charge, with $\Gamma$ in the part of $Q$. The rest of the task is Part 2 one dimension down: a closed curve instead of a closed surface, circulation instead of flux, and **Stokes' theorem** instead of the divergence theorem,

$$ \oint_{\boldsymbol{r}}\boldsymbol{\tau}\cdot\boldsymbol{v}\;dl \;=\; \int_{\boldsymbol{r}\in S}\hat{\boldsymbol{n}}\cdot\left(\nabla\times\boldsymbol{v}\right)dS $$

```{figure} figures/task8_loop_edges.svg
:name: fig-task8-loop
:width: 100%

The rectangle `loop_circulation` walks, and the four terms it sums. Each edge carries the slice the code reads along it, the direction of travel, the spacing that scales it, and the sign it enters with. Only the perimeter samples enter this sum. The interior belongs to the other side of Stokes' theorem, which `curl_flux` integrates over the same rectangle.
```

```{code-cell} ipython3
Gamma, b_core = 1.0, 0.5          # circulation [m^2/s], core radius b [m]

# --- given: the vortex, and the vorticity it should have ---
_swirl = np.where(varrho < 1e-8, Gamma / (2*np.pi*b_core**2),
                  Gamma / (2*np.pi*varrho_s**2) * (1 - np.exp(-varrho**2/b_core**2)))
oseen = (-Y * _swirl, X * _swirl, zero)   # v_phi phi-hat, in Cartesian components
w_exact = Gamma / (np.pi * b_core**2) * np.exp(-varrho**2 / b_core**2)
curl_oseen = curl(*oseen, dx, dy, dz)

# Task 8 -- two blanks, one per side of Stokes' theorem.
#
# LEFT SIDE. Walk the four edges of a rectangle in the z = 0 plane once
# counter-clockwise, so the right-hand rule puts the unit normal along +z-hat,
# and add up the component of the field along the direction of travel. The
# figure above names the four edges, the slice read along each one, and the
# sign it enters with. The two edges walked backwards enter negatively, exactly
# as the inward faces did in Task 5. The x pair is written for you.

def loop_circulation(Ax, Ay, x0, x1, y0, y1):
    """Counter-clockwise circulation of (Ax, Ay) round a rectangle in z = 0."""
    ix0, ix1 = [int(np.argmin(np.abs(axis - q))) for q in (x0, x1)]
    iy0, iy1 = [int(np.argmin(np.abs(axis - q))) for q in (y0, y1)]
    sx, sy, k = slice(ix0, ix1 + 1), slice(iy0, iy1 + 1), fw.z0_index(Z)
    along_x = (fw.line_integral(Ax[sx, iy0, k], dx)
               - fw.line_integral(Ax[sx, iy1, k], dx))
    along_y = ___
    return along_x + along_y


# RIGHT SIDE. n-hat is +z-hat, so only the z-component of the curl crosses the
# rectangle. Integrate it over the flat patch the same indices span: one call
# to fw.area_integral, on the z = 0 plane, with spacings dx and dy.

def curl_flux(x0, x1, y0, y1):
    """Flux of the vorticity through the same rectangle: Stokes' right side."""
    ix0, ix1 = [int(np.argmin(np.abs(axis - q))) for q in (x0, x1)]
    iy0, iy1 = [int(np.argmin(np.abs(axis - q))) for q in (y0, y1)]
    return ___


# --- given: the limit in the definition, run as a measurement. Every side
#     below is a whole number of grid spacings, so each loop is the one asked
#     for rather than the nearest one the grid happens to be able to draw.
def curl_z_area(A, x0, x1, y0, y1):
    """Circulation per unit area round the same rectangle."""
    return loop_circulation(A[0], A[1], x0, x1, y0, y1) / ((x1 - x0) * (y1 - y0))

w_centre = curl_oseen[2][c, c, fw.z0_index(Z)]
print(f"vorticity at the origin: measured {w_centre:.4f} s^-1, "
      f"exact {Gamma/(np.pi*b_core**2):.4f} s^-1")
print(f"the whole Gaussian, worst error "
      f"{np.abs(curl_oseen[2] - w_exact)[interior].max()/w_exact.max():.2%} of peak\n")
print(f"{'side [m]':>9} {'samples/edge':>13} {'circulation':>13} {'C/A':>9}"
      f" {'C/A / measured':>15}")
for m in (18, 9, 6, 3, 2, 1):
    h = m * dx
    print(f"{2*h:9.4f} {2*m+1:13d} {loop_circulation(*oseen[:2], -h, h, -h, h):13.5f}"
          f" {curl_z_area(oseen, -h, h, -h, h):9.4f}"
          f" {curl_z_area(oseen, -h, h, -h, h)/w_centre:15.4f}")

# --- given: Stokes' theorem on five rectangles, two of them off-centre ---
rects = [("centred, side 0.8", (-0.4, 0.4, -0.4, 0.4)),
         ("centred, side 2.0", (-1.0, 1.0, -1.0, 1.0)),
         ("centred, side 3.2", (-1.6, 1.6, -1.6, 1.6)),
         ("off-centre, over the core", (-0.2, 1.4, -0.6, 1.0)),
         ("off to one side", (0.4, 1.6, -0.6, 0.6))]
print(f"\n  {'rectangle':<26} {'circulation':>12} {'flux of curl':>13} {'apart':>8}")
for name, lim in rects:
    C, S = loop_circulation(*oseen[:2], *lim), curl_flux(*lim)
    print(f"  {name:<26} {C:12.5f} {S:13.5f} {abs(C - S)/abs(C):8.2%}")
print(f"\n  all the vorticity there is: Gamma = {Gamma:.4f} m^2/s")

fig, axes = plt.subplots(1, 3, figsize=(16, 4.2))
fw.show_field_slice(X, Y, Z, *oseen[:2], background=curl_oseen[2], ax=axes[0],
                    density=1.2, vmin=0, vmax=1.3, levels=14, cmap="inferno",
                    symmetric=False, stream_color="w",
                    label=r"$(\nabla\times\mathbf{v})_z$  [s$^{-1}$]",
                    title="the vortex, over its vorticity")
prof = np.linspace(1e-3, 2.0, 400)
axes[1].plot(prof, Gamma/(2*np.pi*prof)*(1 - np.exp(-prof**2/b_core**2)), "k", lw=1.8,
             label=r"$v_\phi(\varrho)$")
axes[1].plot(prof, Gamma*prof/(2*np.pi*b_core**2), "C1--", lw=1.2,
             label=r"core: $\Gamma\varrho/2\pi b^2$")
axes[1].plot(prof, Gamma/(2*np.pi*prof), "C2:", lw=1.4, label=r"outside: $\Gamma/2\pi\varrho$")
axes[1].set_ylim(0, 0.25); axes[1].set_title(r"rigid inside the core, $1/\varrho$ outside")
axes[1].set_xlabel(r"$\varrho$ [m]"); axes[1].set_ylabel(r"$v_\phi$ [m s$^{-1}$]")

# the claim under test, drawn: measured vorticity against the exact Gaussian
k0 = fw.z0_index(Z)
axes[2].plot(X[:, c, k0], w_exact[:, c, k0], "k", lw=2.4, alpha=0.35, label="exact")
axes[2].plot(X[:, c, k0], curl_oseen[2][:, c, k0], "C3", lw=1.2, label="measured")
axes[2].set_ylim(0, 1.45); axes[2].set_title("vorticity along $y = 0$")
axes[2].set_xlabel("$x$ [m]"); axes[2].set_ylabel(r"$(\nabla\times\mathbf{v})_z$ [s$^{-1}$]")
for ax_ in axes[1:]:
    ax_.axvline(b_core, color="C0", lw=1, alpha=0.6)
    ax_.grid(alpha=0.3); ax_.legend(fontsize=8)
axes[1].annotate(r"$\varrho = b$", (b_core + 0.05, 0.02), color="C0", ha="left")
plt.tight_layout()
plt.show()

# --- self-check (leave this alone) ---
_h = 6 * dx
fw.check_scalar("Stokes: circulation = flux of the curl through the loop",
                loop_circulation(*oseen[:2], -_h, _h, -_h, _h),
                curl_flux(-_h, _h, -_h, _h), rtol=0.01, unit=" m^2/s")
fw.check_scalar("...and again on a rectangle that is not centred on the vortex",
                loop_circulation(*oseen[:2], -0.2, 1.4, -0.6, 1.0),
                curl_flux(-0.2, 1.4, -0.6, 1.0), rtol=0.01, unit=" m^2/s")
_small = curl_z_area(oseen, -dx, dx, -dx, dx)
fw.check(f"circulation per unit area -> the vorticity at the centre "
         f"({_small:.4f} against {w_centre:.4f} s^-1)",
         abs(_small - w_centre) < 0.01 * abs(w_centre))
_wide = loop_circulation(*oseen[:2], -1.6, 1.6, -1.6, 1.6)
fw.check(f"a loop well outside the core collects all of Gamma "
         f"({_wide:.4f} of {Gamma:.4f} m^2/s)", abs(_wide - Gamma) < 0.01 * Gamma)
```

:::{admonition} Solution — Task 8
:class: dropdown

```python
# in loop_circulation, the left side:
    along_y = (fw.line_integral(Ay[ix1, sy, k], dy)
               - fw.line_integral(Ay[ix0, sy, k], dy))

# in curl_flux, the right side:
    return fw.area_integral(curl_oseen[2][ix0:ix1+1, iy0:iy1+1, fw.z0_index(Z)],
                            dx, dy)
```
:::

:::{admonition} The same theorem, one dimension down
:class: important dropdown

Read the first table downwards. As the loop shrinks the area falls faster than the circulation, and the ratio climbs from 0.137 at side 2.4 m to 0.908 at side 0.4 m and 0.996 at the smallest: the limit in the definition, evaluated rather than asserted. The comparison is against the **measured** 1.2620 s$^{-1}$ rather than the exact 1.2732, so the last 0.9% is grid error, not a failure of the limit.

Read the second table across. On all five rectangles, two of them off-centre, the two sides of Stokes' theorem agree to better than 1%: a few parts in $10^{5}$ on the largest, worst on the smallest, which is only 13 samples across. Size sets the accuracy, not placement, and it is the same second-order error Task 5 measured. The left side never looks inside the loop, the right side never looks at the boundary.

| | Divergence theorem | Stokes' theorem |
| :--- | :--- | :--- |
| Boundary integral | flux through a closed **surface** | circulation round a closed **curve** |
| Interior integral | $\nabla\cdot\boldsymbol{v}$ over the enclosed **volume** | $\hat{\boldsymbol{n}}\cdot(\nabla\times\boldsymbol{v})$ over the enclosed **area** |
| Source it counts | $Q_{\text{enc}}/\varepsilon_0$ | $\Gamma$, or the enclosed current |

The largest loop returns 0.9999 of $\Gamma$, as the largest box of Task 5 recovered 99.95% of the blob's charge. Enlarging a loop that already encloses all the vorticity adds nothing, for the same reason charge outside a closed surface contributes nothing.
:::

### The wire, and Ampère's law

Shrink the core to nothing, $b\to 0$, and $v_\phi$ becomes the irrotational $\Gamma/2\pi\varrho$ of Task 7 at every radius, with all the vorticity compressed onto the axis. The Gaussian collapses to a **Dirac delta**: zero everywhere, undefined on the axis, finite integral all the same. It is the object Task 4 stepped around by giving its charge a width.

That field is the magnetic field of a straight wire carrying a current $I$ along $\hat{\boldsymbol{z}}$, and **Ampère's law** relates them, in the two forms Stokes' theorem connects:

$$ \nabla\times\boldsymbol{H} = \boldsymbol{J} \qquad\Longleftrightarrow\qquad \oint_{\boldsymbol{r}}\boldsymbol{\tau}\cdot\boldsymbol{H}\;dl = I_{\text{enc}} $$

`loop_circulation` walks counter-clockwise in the $z=0$ plane, so $\hat{\boldsymbol{n}} = \hat{\boldsymbol{z}}$ and a positive answer means current towards the reader.

```{code-cell} ipython3
I_wire = 1.0                              # current along +z, in amperes
Hx, Hy = -Y * I_wire / (2*np.pi*varrho_s**2), X * I_wire / (2*np.pi*varrho_s**2)

print(f"  {'loop':<28} {'oint tau.H dl [A]':>18}")
for name, lim in [("encloses the wire, side 0.8", (-0.4, 0.4, -0.4, 0.4)),
                  ("encloses the wire, side 2.0", (-1.0, 1.0, -1.0, 1.0)),
                  ("encloses the wire, side 3.2", (-1.6, 1.6, -1.6, 1.6)),
                  ("encloses it, lopsidedly    ", (-0.4, 1.6, -1.0, 0.6)),
                  ("misses the wire            ", (0.4, 1.6, -0.6, 0.6)),
                  ("misses it, and is large    ", (0.2, 1.8, -1.8, 1.8))]:
    print(f"  {name:<28} {loop_circulation(Hx, Hy, *lim):18.5f}")
print(f"\n  current actually in the wire: {I_wire:.5f} A")
```

:::{admonition} A loop that encloses nothing measurable
:class: important dropdown

Every loop enclosing the wire returns $I$ to better than two parts in a thousand, at any size and wherever it is centred. Every loop missing it returns at most $4\times10^{-4}$ A, which against 1 A is zero. The circulation counts what passes through the loop and nothing else, exactly as the closed surface of Part 2 counted the charge inside and nothing else.

Now put that beside Task 7. At every point these loops pass through $\nabla\times\boldsymbol{H} = 0$, and the loop integral is 1 A regardless. There is no contradiction: Stokes' theorem equates the circulation to the flux of $\boldsymbol{J}$ through the loop, and $\boldsymbol{J}$ is zero over the whole interior except one line, where it is infinite. The integral form survives that delta and the differential form does not, which is the difficulty Part 2 named at the end. A real wire has a finite radius and a finite $\boldsymbol{J}$, and then both forms hold everywhere, exactly as once Task 4 gave its charge a width.
:::

### Why the electric fields had a potential

$\boldsymbol{E} = -\nabla V$ was written in Lab 1 without asking whether an arbitrary vector field can be written that way. The rotation, the shear and the vortex above cannot. The curl is the test:

$$ \nabla\times\left(\nabla p\right) = \boldsymbol{0} \qquad \text{for every twice-differentiable } p $$

because each component subtracts a pair of mixed second derivatives, $\partial_x\partial_y p - \partial_y\partial_x p$, and mixed partials commute. Run the two electric fields of this notebook through the curl.

```{code-cell} ipython3
E_point = tuple(np.nan_to_num(q) for q in (Ex, Ey, Ez))   # built as -grad V
curl_point = curl(*E_point, dx, dy, dz)
curl_blob = curl(Ex_b, Ey_b, Ez_b, dx, dy, dz)            # built from E_r(r) r-hat

shell = interior & (r > 0.5) & (r < 1.6)
for name, w, A in [("point charge, from -grad V", curl_point, E_point),
                   ("blob, from the analytic E_r", curl_blob, (Ex_b, Ey_b, Ez_b))]:
    # index first: |E| is zero inside the mask, and 0/0 there would warn
    wm = np.sqrt(w[0]**2 + w[1]**2 + w[2]**2)[shell]
    Am = (np.sqrt(A[0]**2 + A[1]**2 + A[2]**2) / rs)[shell]
    print(f"  {name:28s} median |curl E| / (|E|/r) = {np.median(wm / Am):.2e}")

# The circulation, on the blob field, which carries no mask for a loop to cross.
# Reported against the natural scale for a voltage here: the strongest field on
# the grid, carried along one metre of path.
scale_V = float(np.max(np.sqrt(Ex_b**2 + Ey_b**2 + Ez_b**2)))
print(f"\n  {'loop':<20} {'circulation of E':>18} {'/ (|E|max x 1 m)':>18}")
for name, lim in [("centred, side 2.0", (-1.0, 1.0, -1.0, 1.0)),
                  ("off-centre", (-0.2, 1.4, -0.6, 1.0)),
                  ("off to one side", (0.4, 1.6, -0.6, 0.6))]:
    circ = loop_circulation(Ex_b, Ey_b, *lim)
    print(f"  {name:<20} {circ:+15.2e} V {abs(circ)/scale_V:18.1e}")
print(f"\n  the same square, side 2.0, on the wire above: "
      f"{loop_circulation(Hx, Hy, -1.0, 1.0, -1.0, 1.0):.3f} A")
```

:::{admonition} Why voltage is a number and not a route
:class: important dropdown

Both fields report zero curl, thirteen orders of magnitude apart, and the gap is in how each was built. `Ex, Ey, Ez` came out of `-np.gradient(V)`, and the curl subtracts the same centred differences in the opposite order, so the stencil obeys the identity as strictly as the algebra does and nothing survives but floating-point ordering, around $10^{-16}$. The blob field was built from the analytic $E_r(r)$ and never passed through a numerical gradient, so it shows the 0.6% a centred difference costs on this grid. Neither number measures the physics; both are consistent with the statement being tested.

The circulations say the same on a closed curve: a few parts in $10^{4}$ of the natural voltage scale, dropping to round-off on the centred loop, whose symmetry cancels it exactly. Put the last line beside them. Same integrator, same grid, same loop, and the wire returns a full ampere.

Zero circulation is what makes potential usable. Carrying a charge round a circuit costs no net work, so the work between two points is independent of the route and one number can be attached to each point. That number is $V$.

Two restrictions, both already demonstrated in Part 3.

**Zero curl gives a potential only where the region has no holes.** The wire is the exception: $\nabla\times\boldsymbol{H} = \boldsymbol{0}$ everywhere outside it, and $\oint\boldsymbol{\tau}\cdot\boldsymbol{H}\,dl = I \neq 0$. A loop encircling the axis cannot be shrunk to a point without crossing the current, so no single-valued potential for $\boldsymbol{H}$ exists out there. Around a point charge the punctured space *is* simply connected, and $V$ survives.

**$\nabla\times\boldsymbol{E} = \boldsymbol{0}$ holds in electrostatics.** When $\boldsymbol{B}$ changes with time, $\nabla\times\boldsymbol{E} = -\partial\boldsymbol{B}/\partial t$, the circulation is no longer zero, and that circulation is the voltage a generator produces. $V$ alone stops being enough, which is where the course goes next.
:::

---

## Closing

The chain built across the two labs, in one line:

$$ \rho_v \;\longrightarrow\; V \;\xrightarrow{\ -\nabla\ }\; \boldsymbol{E} \;\xrightarrow{\ \nabla\cdot\ }\; \rho_v/\varepsilon_0, \qquad \nabla\times\boldsymbol{E} = \boldsymbol{0} $$

with the last statement the licence for the arrow labelled $-\nabla$: only a curl-free field has a potential to recover.

- **Gradient.** Scalar in, vector out. Points along steepest increase, normal to the level surfaces, length equal to the rate of increase.
- **Divergence.** Vector in, scalar out. Net flux per unit volume: what is created at a point, and nothing else.
- **Curl.** Vector in, vector out. Net circulation per unit area about the axis its own direction gives: local rotation, not the shape of a streamline.

Each of the last two comes with an integral theorem, and each replaces a derivative that fails at a singular source with an integral that does not. The point charge and the current-carrying wire are the same difficulty met twice.

### The same three operators, elsewhere in ECT

Electrostatics is a convenient place to learn these, not the only place to use them. The machinery of these two labs applies unchanged to every row:

| System | Potential | Field | Source equation |
| :--- | :--- | :--- | :--- |
| Electrostatics | $V$ [V] | $\boldsymbol{E} = -\nabla V$ &nbsp; [V/m] | $\nabla\cdot\boldsymbol{E} = \rho_v/\varepsilon_0$ |
| Gravitation | $\Phi$ [J/kg] | $\boldsymbol{g} = -\nabla \Phi$ &nbsp; [m/s$^2$] | $\nabla\cdot\boldsymbol{g} = -4\pi G\rho_m$ |
| Heat conduction | $T$ [K] | $\boldsymbol{q}_T = -k\nabla T$ &nbsp; [W/m$^2$] | $\nabla\cdot\boldsymbol{q}_T = 0$ (steady, no sources) |
| Groundwater flow | $h$ [m] | $\boldsymbol{q}_h = -K\nabla h$ &nbsp; [m/s] | $\nabla\cdot\boldsymbol{q}_h = 0$ (steady, incompressible) |

with $G$ the gravitational constant, $\rho_m$ the mass density, $k$ the thermal conductivity and $K$ the hydraulic conductivity. The minus signs are one minus sign: flow runs downhill, and the gradient points uphill.

Every field there is a gradient wherever $k$ and $K$ are constant, so none can circulate. Let $K$ vary, as in any real aquifer, and $\nabla\times\boldsymbol{q}_h = -\nabla K\times\nabla h$ need not vanish. The fields that circulate are the ones with no potential to be had:

| Field | Circulation equation | What sets it |
| :--- | :--- | :--- |
| Magnetic field $\boldsymbol{H}$ [A/m] | $\nabla\times\boldsymbol{H} = \boldsymbol{J}$ | the current threading the loop |
| Fluid velocity $\boldsymbol{v}$ [m/s] | $\nabla\times\boldsymbol{v} = \boldsymbol{\omega}_v$ | shear at a boundary, and rotation of the Earth |
| Electric field, unsteady | $\nabla\times\boldsymbol{E} = -\partial\boldsymbol{B}/\partial t$ | a magnetic field that changes with time |

with $\boldsymbol{\omega}_v = 2\boldsymbol{\omega}$ the vorticity of Task 6. The first row is Ampère's law in the static limit; Maxwell's added $\partial\boldsymbol{D}/\partial t$ is why light exists. The third is Faraday's law. Those two with the source equations of Parts 1 and 2 are Maxwell's four.

### Formative assessment — Chapters 1 and 2

Not graded, and not handed in. It exists so you can find out what you do not yet know, while there is still time to fix it. Allow about **45 minutes**.

#### Part A — six questions, no code

Handed out at the start of the session.

#### Part B — a buried heating panel

Continue with your Part A answers in mind. A rectangular electrical heating element, $1.0 \times 0.6$ m, is buried in soil and dissipates $P = 100$ W. Nothing here has been solved for you; the tools are the ones you built.

A steady point source of power $P$ in a medium of conductivity $k$ raises the temperature above ambient by $P/4\pi k r$, the same $1/r$ used throughout these labs. Split the panel into $N = 20\times12$ sub-sources sharing the power equally, and superpose:

$$ T(\boldsymbol{r}) = \frac{P}{4\pi k N}\sum_{i=1}^{N}\frac{1}{\lvert\boldsymbol{r}-\boldsymbol{r}_i\rvert}, \qquad P = 100\ \text{W}, \qquad k_{\text{soil}} = 1.5\ \text{W m}^{-1}\text{K}^{-1} $$

Check the dimensions before you code: $[P]/[k] = \text{m}\cdot\text{K}$, divided by a distance, so $T$ comes out in kelvin. A formula that does not reduce to kelvin has an error in it.

```{code-cell} ipython3
# --- given: the panel, and the grid it sits on (the cube from Part 0) ---
P_heat, k_soil = 100.0, 1.5               # W, and W/m/K for soil
panel_x = np.linspace(-0.5, 0.5, 20)      # sub-source positions, in the z = 0 plane
panel_y = np.linspace(-0.3, 0.3, 12)
N_sub = panel_x.size * panel_y.size

# B1 -- two blanks, inside the loop. `d_min` records how close each grid point
# comes to the nearest sub-source; the mask below uses it.
T_sum = np.zeros_like(X)
d_min = np.full(X.shape, np.inf)
for x0 in panel_x:
    for y0 in panel_y:
        d = ___                           # distance from (x0, y0, 0) to every grid point
        d_min = np.minimum(d_min, d)
        T_sum += 1.0 / np.maximum(d, 1e-12)
T_panel = ___                             # the prefactor, applied once at the end

# --- given: the panel is a set of singularities, so keep a shell around it ---
T_panel = np.where(d_min < 0.15, np.nan, T_panel)
print(f"{N_sub} sub-sources, each {P_heat/N_sub:.3f} W")
print(f"T ranges {np.nanmin(T_panel):.2f} to {np.nanmax(T_panel):.2f} K above ambient")

# --- self-check (leave this alone) ---
fw.check_shape("T has the shape of the grid", T_panel, X.shape)
_i1 = int(np.argmin(np.abs(axis - 1.0)))
fw.check_scalar("1 m directly above the centre of the panel", T_panel[c, c, _i1],
                5.007, rtol=0.01, unit=" K")
fw.check("...and the prefactor was applied, not left out",
         np.nanmax(T_panel) < 100.0)
```

Heat flows down the temperature gradient, the same minus sign and the same reason as $\boldsymbol{E} = -\nabla V$:

$$ \boldsymbol{q}_T = -k\nabla T \qquad [\text{W m}^{-2}] $$

At steady state, away from the panel, nothing creates or destroys heat, so $\boldsymbol{q}_T$ should be solenoidal there. It is also a gradient, so its curl should vanish.

```{code-cell} ipython3
# B2 -- three blanks. Reuse the operators you wrote: `divergence` from Task 1
# and `curl` from Task 6. Both need arrays without NaN, so pass them through
# np.nan_to_num first, as Task 2 did for the dipole.
qx, qy, qz = ___                          # Fourier's law, as three arrays
q_T = tuple(np.nan_to_num(v) for v in (qx, qy, qz))
div_q = ___
curl_q = ___

# --- given: both reported scale-free, against |q|/d, exactly as Task 2 and
#     Task 7 did. `far` is the region well clear of the panel.
far = interior & (d_min > 0.6)
q_mag = np.sqrt(q_T[0]**2 + q_T[1]**2 + q_T[2]**2)
yardstick = (q_mag / np.maximum(d_min, 1e-12))[far]
curl_mag = np.sqrt(curl_q[0]**2 + curl_q[1]**2 + curl_q[2]**2)
print(f"  |div q| / (|q|/d), away from the panel : "
      f"{np.median(np.abs(div_q[far]) / yardstick):.3%}")
print(f"  |curl q| / (|q|/d)                     : "
      f"{np.median(curl_mag[far] / yardstick):.2e}")

# --- self-check (leave this alone) ---
fw.check(f"q points away from the panel, so heat flows outward "
         f"({np.median((q_T[0]*X + q_T[1]*Y + q_T[2]*Z)[far]):+.3f})",
         np.median((q_T[0]*X + q_T[1]*Y + q_T[2]*Z)[far]) > 0)
fw.check(f"no heat is created away from the panel "
         f"({np.median(np.abs(div_q[far]) / yardstick):.2%})",
         np.median(np.abs(div_q[far]) / yardstick) < 0.05)
fw.check(f"and the flux of a gradient cannot circulate "
         f"({np.median(curl_mag[far] / yardstick):.1e})",
         np.median(curl_mag[far] / yardstick) < 1e-10)
```

The divergence is zero away from the panel, so it says nothing about how strong the panel is. Put a closed surface around it instead; `closed_box_flux` from Task 5 works unchanged.

```{figure} figures/b3_nested_boxes.svg
:name: fig-b3-boxes
:width: 88%

The two surfaces of B3, seen in section. Each is a closed box centred on the panel, and the second blank asks what the region between them contains.
```

```{code-cell} ipython3
# B3 -- two blanks. Both are one call to `closed_box_flux` from Task 5, which
# works here unchanged: it takes the three components and a half-width.
#
# FIRST BLANK, inside the loop. q_T is a heat flux density in W/m^2, so its
# integral over a closed surface is already a power in watts. No conversion
# factor belongs on this line; adding one is the way to get it wrong.
powers = {}
print("  box half-width      power it finds")
for h in (1.0, 1.4):
    powers[h] = ___                       # net outward heat flow through |x|,|y|,|z| <= h
    print(f"     {h:.1f} m            {powers[h]:8.3f} W")
print(f"\n     actually buried  {P_heat:8.3f} W")

# SECOND BLANK. The shell between those two boxes holds no part of the panel,
# so nothing in it generates heat. Weigh it. Whatever enters across the inner
# surface must leave across the outer one, so the power generated in between is
# the difference of the two fluxes you already have. One line, no new function.
power_shell = ___

print(f"\n  generated in the shell between them: {power_shell:+.3f} W, "
      f"{abs(power_shell)/P_heat:.3%} of the panel")

# The same box at h = 0.6 m returns 84.3 W. Its faces pass 0.1 m from the edge
# of the panel, inside the shell that was masked out above; np.nan_to_num then
# integrated the deleted samples as zeros. With no mask it returns 100.2 W.
# Question B5 asks what the general rule is.

# --- self-check (leave this alone) ---
fw.check_scalar("closed-surface flux of q = the power buried inside",
                powers[1.0], P_heat, rtol=0.01, unit=" W")
fw.check(f"...and a larger box finds the same power, not more "
         f"({powers[1.4] - powers[1.0]:+.3f} W between them)",
         abs(powers[1.4] - powers[1.0]) < 0.01 * P_heat)
fw.check(f"the shell between the two boxes generates nothing ({power_shell:+.3f} W)",
         abs(power_shell) < 0.01 * P_heat)
```

The closed surface weighed the panel without differentiating anything. Stokes' theorem asks the other question: run a loop instead of a surface, and see whether the heat flux circulates.

```{figure} figures/b4_loops_and_mask.svg
:name: fig-b4-loops
:width: 96%

The three rectangles, in the plane $z = 0$. Two of them stay clear of the masked shell. The third has an edge running straight through it, and the thick segment marks where. Compare the three numbers the cell prints against this picture before answering B5.5.
```

```{code-cell} ipython3
# B4 -- one blank, which serves all three loops. `loop_circulation` from Task 8
# works unchanged: it takes the two in-plane components and the four edges
# x0, x1, y0, y1 of a rectangle in the z = 0 plane, walked counter-clockwise.
#
# Read each answer against the scale printed first, not as a bare number: a
# circulation of 1e-16 W/m means nothing until you know what 1 would mean.
q_scale = np.nanmax(np.sqrt(q_T[0]**2 + q_T[1]**2 + q_T[2]**2))   # W/m, one metre of path
loops = [("encircling the panel", (-1.2, 1.2, -1.2, 1.2)),
         ("off to one side", (0.8, 1.6, -0.4, 0.4)),
         ("crossing the mask", (-0.2, 1.4, -0.6, 1.0))]
circ = {}

print(f"  strongest |q| carried along 1 m of path: {q_scale:.3f} W/m\n")
print(f"  {'loop':<22} {'circulation':>13} {'flux of curl':>14} {'C / scale':>11}")
for name, lim in loops:
    circ[name] = ___                      # circulation of q_T round this rectangle
    ix0, ix1 = [int(np.argmin(np.abs(axis - q))) for q in lim[:2]]
    iy0, iy1 = [int(np.argmin(np.abs(axis - q))) for q in lim[2:]]
    flux = fw.area_integral(curl_q[2][ix0:ix1+1, iy0:iy1+1, fw.z0_index(Z)], dx, dy)
    print(f"  {name:<22} {circ[name]:>13.3e} {flux:>14.3e} "
          f"{abs(circ[name])/q_scale:>11.2e}")

# --- self-check (leave this alone) ---
fw.check(f"a gradient field does not circulate, even round the source "
         f"({circ['encircling the panel']:+.2e} W/m)",
         abs(circ["encircling the panel"]) < 1e-9 * q_scale)
fw.check(f"...nor round a loop that encloses nothing "
         f"({circ['off to one side']:+.2e} W/m)",
         abs(circ["off to one side"]) < 1e-9 * q_scale)
fw.check_scalar("the third loop, the one whose edge crosses the masked shell (B5.5)",
                circ["crossing the mask"], -0.0697, rtol=0.03, unit=" W/m")
```

:::{admonition} Why this field has a potential, and the wire's has none
:class: important

Two of the three loops return round-off, below $10^{-14}$ W/m against a scale of 35.5 W/m. The heat flux cannot circulate: it is $-k\nabla T$, and a gradient has no curl. That is the argument that made $V$ possible, so $\boldsymbol{q}_T$ has a potential too, and it is a quantity you have already computed. It is $T$.

The wire in Part 3 is also curl-free at every point, and its loop returns a full ampere. The difference is the region, not the field: the soil around the panel is simply connected, so any loop can be shrunk to a point without leaving the region where $\nabla\times\boldsymbol{q}_T = \boldsymbol{0}$, and Stokes' theorem forces the circulation to zero. Around the wire no such shrinking is possible.

The third loop returns $-0.070$ W/m, $2\times10^{-3}$ of the scale where the other two are below $10^{-16}$ of it. Its edge is the only one running through the masked shell.
:::

Far from the panel its shape should stop mattering. Test that against the single term a point source would give.

```{code-cell} ipython3
# --- given: the panel against one point source of the same total power ---
print(f"  {'distance':>10} {'along x':>10} {'along z':>10} {'point source':>14} {'spread':>8}")
for d_ in (0.8, 1.2, 1.6):
    i = int(np.argmin(np.abs(axis - d_)))
    T_x, T_z = T_panel[i, c, c], T_panel[c, c, i]
    print(f"  {d_:8.1f} m {T_x:9.3f} K {T_z:9.3f} K "
          f"{P_heat/(4*np.pi*k_soil*d_):13.3f} K {abs(T_x-T_z)/T_x:8.1%}")

# The blank shell in both panels is the masked region, 0.15 m around the
# panel. Its outline in the plan view is the panel's own shape.
fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.6))
fw.show_field_slice(X, Y, Z, q_T[0], q_T[2], background=T_panel, ax=axes[0],
                    plane="y", density=1.2, vmin=0, vmax=15, levels=16,
                    cmap="inferno", symmetric=False, stream_color="w",
                    label="$T$ above ambient  [K]", title="vertical section, $y = 0$")
fw.show_field_slice(X, Y, Z, q_T[0], q_T[1], background=T_panel, ax=axes[1],
                    plane="z", density=1.2, vmin=0, vmax=15, levels=16,
                    cmap="inferno", symmetric=False, stream_color="w",
                    label="$T$ above ambient  [K]", title="plan view, $z = 0$")
plt.tight_layout()
plt.show()
```

:::{admonition} B5. Five questions on what you just measured
:class: tip

Answer these in writing.

1. The closed surface returned 100.05 W and the divergence returned zero everywhere you could measure it. Both are correct. What does each one tell you that the other cannot?
2. The $h = 0.6$ m box returns 84.3 W with the mask in place and 100.2 W without it. State the general rule this illustrates about masked samples and surface integrals.
3. `curl_q` came back at $10^{-15}$ rather than at the fraction of a percent `div_q` shows. Why is it so much smaller, and is that a better measurement or a different kind of statement?
4. In the plan view the isotherms near the panel are rounded rectangles and far away they are circles, and the table shows the difference between the two directions falling from 19% to 5%. What has been lost, and what does that have to do with truncating a series?
5. Two loops returned round-off, below $10^{-14}$ W/m; the third, whose edge runs through the masked shell, returned $-0.070$ W/m. Say what that number measures. Question 2 makes the same point for a closed surface: state the rule once, covering a line integral and a surface integral together.
:::

:::{admonition} B6. The number that is wrong
:class: tip

Everything above was computed in soil, $k = 1.5$ W m⁻¹K⁻¹, giving $+5.0$ K one metre above the panel. Re-run it for the same panel hanging in **air**, $k_{\text{air}} = 0.026$ W m⁻¹K⁻¹. Nothing needs recomputing: $T \propto 1/k$, so the answer is $5.0 \times 1.5/0.026$.

The arithmetic is right and the answer is absurd. Identify the assumption that failed. Two are worth naming.
:::
