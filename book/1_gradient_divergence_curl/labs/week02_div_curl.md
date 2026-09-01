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

The second of two labs on the operators of this chapter, following Lab 1 on series and the gradient. Each task states a physical question, gives the steps, and ends with a self-check you can run. Plotting is supplied in the module `fwtools`, so that your effort goes into the physics rather than into rendering transparent isosurfaces.
:::

## Learning objectives

By the end of this lab you should be able to:

- **Distinguish diverging arrows from non-zero divergence.** Compute $\nabla\cdot\boldsymbol{v}$, justify the result by flux rather than by algebra, and identify the only radial flow that is incompressible.
- **Use the divergence theorem as a measurement.** Verify $\oint_S\boldsymbol{v}\cdot\hat{\boldsymbol{n}}\,dS = \int_{\mathcal{D}} \nabla\cdot\boldsymbol{v}\,dV$ numerically, and account for what happens when the source shrinks to a point.

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

Read the definition on the left rather than the formula on the right: **treat $\boldsymbol{A}$ as a fluid velocity**, place a small box anywhere, and measure the net outflow through its walls per unit volume.

| $\nabla\cdot\boldsymbol{A}$ | Name | Picture |
| :---: | :--- | :--- |
| $> 0$ | **source** | a tap: more leaves than arrives |
| $< 0$ | **sink** | a drain: more arrives than leaves |
| $= 0$ | **solenoidal** | whatever flows in, flows out |

### Task 1 — the operator, and its independence of the origin

The operator is three lines, and they are given. One derivative along one axis per component: `np.gradient(Ax, dx, axis=0)` returns $\partial A_x/\partial x$ and nothing else, whereas asking for all three and discarding two costs three times the memory. The cross terms are not part of a divergence.

**The question is the one raised by the definition.** Flux per unit volume is measured around a point, so does the result depend on which point is called the origin? Take the outward flow $\boldsymbol{A} = \boldsymbol{r}$, whose divergence follows on paper as $1+1+1 = 3$, then shift the whole field so that it streams out of $(0.8, -0.4, 0.3)$. Predict the divergence before computing it.

```{code-cell} ipython3
# --- given ---
def divergence(Ax, Ay, Az, dx, dy, dz):
    return (np.gradient(Ax, dx, axis=0)
            + np.gradient(Ay, dy, axis=1)
            + np.gradient(Az, dz, axis=2))

# Task 1 -- two blanks. The same outward flow, seen from somewhere else.
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
Sx, Sy, Sz = X - x0, Y - y0, Z - z0
div_shifted = divergence(Sx, Sy, Sz, dx, dy, dz)
```
:::

:::{admonition} Why the answer had to be 3 either way
:class: tip

Moving the source changed every arrow in the box and changed the divergence nowhere. Differentiation removes the constant: $\partial(x - x_0)/\partial x = 1$ for any $x_0$.

The divergence is a **local** quantity: it is built from a limit taken around one point, so it depends on the field in a shrinking neighbourhood of that point and not on where the axes were placed. Every operator in this course has that property, and it is what makes $\nabla\cdot\boldsymbol{E} = \rho_v/\varepsilon_0$ a statement about places rather than about coordinate systems.
:::

### Task 2 — the only incompressible radial flow

Water of constant density flows outward from a source at the origin. Away from that source nothing is created or destroyed, so the flow is **incompressible**:

$$ \nabla\cdot\boldsymbol{v} = 0 \qquad \text{for } r \neq 0. $$

Constant density and a point source force the flow to be radial, $\boldsymbol{v} = f(r)\,\boldsymbol{r}$, and incompressibility then pins $f$ down completely:

$$ \nabla\cdot\boldsymbol{v} = 3f(r) + r\frac{df}{dr} = 0 \qquad\Longrightarrow\qquad f(r) = \frac{A}{r^{3}}. $$

Rather than assume this, test four candidates and let the divergence select.

```{code-cell} ipython3
# The measure reported by the loop below:
#
#       |div v| / (|v| / r),  median over the test band
#
# |v|/r is the natural size of a derivative of v, so the ratio is a pure
# number: 1 means "as large as a derivative of this field could be".

r_safe = np.where(r < 0.3, np.nan, r)
band_i = interior & (r > 0.6) & (r < 1.6)

# Task 2 -- three blanks, inside the loop.
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

One candidate gives 300%, two give almost exactly 100%, and one gives 0.66%. Only $f = A/r^{3}$ survives, as the algebra predicts.

The 300% is not an accident. For $f = \text{const}$ the field is the position vector, $\boldsymbol{v} = \boldsymbol{r}$, whose divergence Task 1 measured as exactly 3, while $\lvert\boldsymbol{v}\rvert/r = 1$, so the ratio must be 3. The surviving case rewrites as

$$ \boldsymbol{v} = \frac{A}{r^{3}}\boldsymbol{r} = \frac{A}{r^{2}}\,\hat{\boldsymbol{r}}. $$

**This is the same $1/r^{2}$ used since Lab 1's Task 6.** Here it was not assumed and no charge was mentioned; it follows from conservation away from the source together with the three-dimensionality of space. The surface of a sphere grows as $r^{2}$, so a fixed flux crossing it must thin as $1/r^{2}$.

Coulomb's law, Newtonian gravity and this flow share an exponent for that one geometric reason.
:::

### Task 2, continued — a field with no source anywhere

Note the restriction on that result: $\nabla\cdot\boldsymbol{v} = 0$ **for $r \neq 0$**. The origin must be excluded, because that is where the water is injected; a closed surface around it would find the tap.

The next field admits no such exception. To first order the Earth's magnetic field is a **dipole**: a north and a south pole so close together that they coincide. With dipole moment $\boldsymbol{m}$,

$$ \boldsymbol{B} = \frac{3\boldsymbol{r}\,(\boldsymbol{r}\cdot\boldsymbol{m}) - r^{2}\boldsymbol{m}}{r^{5}}. $$

Take $\boldsymbol{m} = \hat{\boldsymbol{z}}$ on the cube set up above, where $z$ points up, and measure the divergence with the same function.

The Earth's own moment points roughly geographic south, which is why the magnetic pole in the Arctic is magnetically a **south** pole and attracts the north end of a compass needle. Reversing $\boldsymbol{m}$ reverses every arrow below and leaves $\nabla\cdot\boldsymbol{B}$ unchanged.

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
:class: important

Both fields are divergence-free over the region measured, but the two statements differ.

The flow required an exclusion: $\nabla\cdot\boldsymbol{v} = 0$ away from the origin, because the origin is a tap. The dipole requires none, and $\nabla\cdot\boldsymbol{B} = 0$ holds **everywhere in space, including at the source**. No point can be excluded to reveal a magnet leaking field the way the tap leaks water. This is one of Maxwell's equations: magnetic monopoles do not exist, and field lines of $\boldsymbol{B}$ never begin or end but close on themselves.

Two remarks on the numbers. Both cells report the same scale-free measure, so the results are directly comparable. The dipole's 1.8% is worse than the radial flow's 0.66%, not because the physics is less secure but because $\boldsymbol{B}$ falls off as $1/r^{3}$ rather than $1/r^{2}$, leaving a centred difference more curvature to miss. Part 2 tests the same claim far below 2% by putting a closed surface around the dipole instead of differentiating it.

The second check is also informative: $\boldsymbol{B}\cdot\boldsymbol{r}$ is negative somewhere, whereas the outward flow of Task 2 is never negative. The dipole points inward over part of space; it returns. That is the numerical signature of a field closing on itself.
:::

### Task 3 — three flows

Three velocity fields. For each one: **sketch it, predict the sign of the divergence, then measure.** Record the predictions first; the task is about the gap between intuition and the result.

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

Along the $x$-axis, field (c) flows outward and resembles a source. It is not:

$$ \nabla\cdot\boldsymbol{A} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(-y) = 1 - 1 = 0 $$

Place a box at the origin: fluid leaves through the left and right walls and enters through the top and bottom at exactly the same rate. The parcel changes **shape**, not **volume**.

Diverging arrows are not divergence. Outflow in one direction can be cancelled exactly by inflow in another. Task 5 puts a closed surface around this field and measures the cancellation directly.
:::

### Task 4 — the divergence as a charge detector

Gauss's law, for a field in vacuum, says

$$ \nabla\cdot\boldsymbol{E} = \frac{\rho_v}{\varepsilon_0} $$

which is a strong claim: **the divergence of $\boldsymbol{E}$ at a point gives the charge density at that point and nothing else.** Where there is no charge, $\boldsymbol{E}$ is solenoidal, however widely its arrows spread.

Test that pointwise, on a source a grid can hold. A point charge cannot serve: it has infinite density at one location. Take instead a charge **distributed over a finite blob**, which is what any real charged object is:

$$ \rho_v(r) = \rho_{v0}\,e^{-r^{2}/a^{2}}, \qquad \rho_{v0} = 10^{-9}\ \text{C/m}^3, \qquad a = 0.5\ \text{m} $$

Here $a$ is the **width of the blob**. In Lab 1's Task 9 the same letter denoted an electrode separation, the second symbol these two labs overload, after $\rho$. The code keeps them apart as `a` here and `a_sep` there; in algebra only the context distinguishes them.

Integrating over a sphere of radius $r$ gives the charge it encloses:

$$ Q_{\text{enc}}(r) = \int_0^{r}\!\rho_v\,4\pi r'^{2}\,dr' = 4\pi\rho_{v0}\left[\frac{a^{3}\sqrt{\pi}}{4}\operatorname{erf}\!\left(\frac{r}{a}\right) - \frac{a^{2}r}{2}e^{-r^{2}/a^{2}}\right] $$

and Gauss's law, $E_r = Q_{\text{enc}}/4\pi\varepsilon_0r^{2}$, then gives the field, with the $4\pi$ cancelling:

$$ E_r(r) = \frac{\rho_{v0}}{\varepsilon_0 r^{2}}\left[\frac{a^{3}\sqrt{\pi}}{4}\operatorname{erf}\!\left(\frac{r}{a}\right) - \frac{a^{2}r}{2}e^{-r^{2}/a^{2}}\right] $$

One check: near the centre $Q_{\text{enc}}$ grows as $r^{3}$ while the surface grows as $r^{2}$, so $E_r \to \rho_{v0} r/3\varepsilon_0$, zero at the centre, rising linearly, and peaking at $r \approx a$.

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

The two panels show the same distribution. The location of the charge was never supplied to the code: a field was differentiated, and the charge distribution came back out.

Note where the divergence vanishes: everywhere outside the blob, where the field is still large and still spreading. **Strong field, zero divergence**: the two quantities are unrelated.
:::

### The same operator, a different formula

Everything so far used the Cartesian formula, because `np.gradient` differentiates along array axes. The divergence is flux per unit volume, a physical quantity that cannot depend on the choice of axes. Only the formula changes:

| | Gradient $\nabla T$ | Divergence $\nabla\cdot\boldsymbol{A}$ |
| :--- | :--- | :--- |
| Cartesian $(x,y,z)$ | $\dfrac{\partial T}{\partial x}\hat{\boldsymbol{x}} + \dfrac{\partial T}{\partial y}\hat{\boldsymbol{y}} + \dfrac{\partial T}{\partial z}\hat{\boldsymbol{z}}$ | $\dfrac{\partial A_x}{\partial x} + \dfrac{\partial A_y}{\partial y} + \dfrac{\partial A_z}{\partial z}$ |
| Cylindrical $(\varrho,\phi,z)$ | $\dfrac{\partial T}{\partial \varrho}\hat{\boldsymbol{\varrho}} + \dfrac{1}{\varrho}\dfrac{\partial T}{\partial \phi}\hat{\boldsymbol{\phi}} + \dfrac{\partial T}{\partial z}\hat{\boldsymbol{z}}$ | $\dfrac{1}{\varrho}\dfrac{\partial (\varrho v_\varrho)}{\partial \varrho} + \dfrac{1}{\varrho}\dfrac{\partial v_\phi}{\partial \phi} + \dfrac{\partial v_z}{\partial z}$ |
| Spherical $(r,\phi,\theta)$ | $\dfrac{\partial T}{\partial r}\hat{\boldsymbol{r}} + \dfrac{1}{r}\dfrac{\partial T}{\partial \theta}\hat{\boldsymbol{\theta}} + \dfrac{1}{r\sin\theta}\dfrac{\partial T}{\partial \phi}\hat{\boldsymbol{\phi}}$ | $\dfrac{1}{r^{2}}\dfrac{\partial (r^{2}v_r)}{\partial r} + \dfrac{1}{r\sin\theta}\dfrac{\partial (v_\theta \sin\theta)}{\partial \theta} + \dfrac{1}{r\sin\theta}\dfrac{\partial v_\phi}{\partial \phi}$ |

Cylindrical $\varrho=\sqrt{x^2+y^2}$ is the distance from the $z$-axis; spherical $r=\sqrt{x^2+y^2+z^2}$, used throughout this lab, is the distance from the origin. They are written differently precisely to keep them apart.

One reading note: the spherical coordinates are named $(r,\phi,\theta)$, but the terms in the row above are listed as $r$, then $\theta$, then $\phi$, the order in which the scale factors $(1,\ r,\ r\sin\theta)$ are derived. The order of terms in a sum is immaterial.

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

Same field, same operator, same answer, obtained from a few hundred samples on a line rather than a quarter of a million in a cube, and several times more accurately.

For the point charge the gain is certainty rather than accuracy. $r^{2}E_r = Q/4\pi\varepsilon_0$ is a **constant**, so its derivative is analytically zero for every $r>0$: not 1% of something, but zero, in one line of algebra. What the cell prints is the precision with which double arithmetic subtracts two equal numbers, around $10^{-13}$, or exactly $0$ when the cancellation is exact. Changing `dr` moves that last digit; it does not move the algebra. Cartesian coordinates could establish only that the divergence is small.

Matching the coordinates to the symmetry of the source replaces three noisy numerical derivatives with one line of algebra. That is the purpose of the second and third rows of the table.
:::

---

## Part 2 — Flux, and the divergence theorem

Part 1 used the differential form of Gauss's law, which compares two numbers at one point. The integral form relates a volume to the surface enclosing it:

$$ \oint_S \boldsymbol{E}\cdot\hat{\boldsymbol{n}}\,dS \;=\; \int_{\mathcal{D}} \nabla\cdot\boldsymbol{E}\;dV \;=\; \frac{Q_{\text{enc}}}{\varepsilon_0} $$

with $S$ the closed surface, $\hat{\boldsymbol{n}}$ its outward unit normal, and $\mathcal{D}$ the volume it encloses.

The first equality is the **divergence theorem**, pure vector calculus, valid for any well-behaved field. The second is the physics. Together they state that measuring $\boldsymbol{E}$ on a closed surface gives the charge inside, and nothing about its arrangement or about any charge outside.

Take $S$ to be a cube of half-width $h$ centred on the origin, faces on grid planes. On the $+x$ face the outward normal is $+\hat{\boldsymbol{x}}$, so it contributes $\int\!\!\int E_x\,dy\,dz$; on the $-x$ face the normal is $-\hat{\boldsymbol{x}}$ and the same integral enters negatively. Six faces, three pairs.

### Task 5 — close the surface

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

Three independent calculations. The first never examines the interior of the box, the second never examines the surface, and the third never examines the field. They agree to a fraction of a percent.

The result grows with $h$ and then stops: once the cube holds nearly all the charge, enlarging it adds surface but no charge. Charge outside a closed surface contributes exactly nothing, because the field lines it sends in through one wall leave through another.
:::

### Shrinking the source to a point

Run the same surface integral on the point-charge field of Lab 1's Task 7, whose divergence could not be measured at the origin because the singularity had to be masked.

Rearranged, Gauss's law turns the flux into a **charge meter**: $Q_{\text{enc}} = \varepsilon_0 \oint_S \boldsymbol{E}\cdot\hat{\boldsymbol{n}}\,dS$. Weigh the charge inside each box in coulombs and compare it with the 1 nC placed there.

```{code-cell} ipython3
print("box half-width      charge it finds")
for h in (0.6, 1.0, 1.4):
    Q_found = epsilon_0 * closed_box_flux(Ex, Ey, Ez, h)
    print(f"   {h:.1f} m           {Q_found * 1e12:8.2f} pC")
print(f"\n   actually there   {Q * 1e12:8.2f} pC")

# The shell between the 0.6 m and 1.4 m boxes holds no charge. Weigh it: what
# enters the small box must leave the large one, so the difference of the two
# fluxes is the charge in between.
Q_shell = epsilon_0 * (closed_box_flux(Ex, Ey, Ez, 1.4)
                       - closed_box_flux(Ex, Ey, Ez, 0.6))
print(f"\ncharge in the shell between them: {Q_shell * 1e12:+.2f} pC "
      f"({abs(Q_shell) / Q:.2%} of the charge at the centre)")
```

:::{admonition} Where did the charge go?
:class: important

Every box weighs the same 1 nC to a fraction of a percent, and the shell between two of them weighs nothing. All the charge lies in the only region common to every box: the origin.

The whole source therefore sits at one point, where $\nabla\cdot\boldsymbol{E}$ is not a large number but undefined: $\rho_v$ has become a **Dirac delta**, zero everywhere, infinite at one point, with finite integral $Q$. The integral form survives exactly where the differential form fails.

The same statement for magnetism carries no source term at all:

$$ \nabla\cdot\boldsymbol{B} = 0 \qquad\Longleftrightarrow\qquad \oint_S \boldsymbol{B}\cdot\hat{\boldsymbol{n}}\,dS = 0 \ \ \text{for every closed } S $$

The measurement returns zero around any closed surface anywhere: there are no magnetic monopoles, and field lines of $\boldsymbol{B}$ never begin or end.
:::

### The dipole, exactly

Task 2 measured $\nabla\cdot\boldsymbol{B} = 0$ for the Earth's dipole and returned 1.8%, which is grid error rather than physics. The same claim can be tested without differentiating: put a closed surface around the dipole and weigh what crosses it.

One warning before reading the numbers. A box centred on the origin is too easy a test for this dipole: with $\boldsymbol{m} = \hat{\boldsymbol{z}}$, $B_x$ and $B_y$ are odd in $z$ and $B_z$ is even, so on a $z$-symmetric box the faces cancel in pairs before any physics enters. An off-centre box is the honest test, and the cell below runs both.

```{code-cell} ipython3
r_dot_m = Z
Bx = 3*X*r_dot_m / r_safe**5
By = 3*Y*r_dot_m / r_safe**5
Bz = (3*Z*r_dot_m - r_safe**2) / r_safe**5

B = tuple(np.nan_to_num(q) for q in (Bx, By, Bz))
v = tuple(np.nan_to_num(q / r_safe**3) for q in (X, Y, Z))

# --- given: the same surface integral over any grid-aligned box, centred
#     on the origin or not. Same six faces, same three pairs as Task 5.
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

The radial flow returns $4\pi$ through every surface, whatever its size: there is a tap at the origin, and every box finds the same one, as every box found the same 1 nC above.

The dipole returns **nothing** through any of them. On the three centred boxes the result is zero to machine precision, but the warning above applies: those boxes cancel the field against itself by symmetry and could return nothing else. The off-centre boxes are the measurement that counts, and they return $-2.5\times10^{-3}$ and $-2.2\times10^{-4}$. Compare the adjacent column: the same integrator, on the same grid, misses $4\pi$ by $6.8\times10^{-3}$ on the radial flow. **The flux of the dipole is zero to better than the accuracy this method achieves on anything.**

The two divergence-free fields are therefore different statements. The flow has a tap that can be located by shrinking a surface onto it; the dipole has nothing to locate, at any size or placement of the surface. This is $\nabla\cdot\boldsymbol{B} = 0$ in the form that admits no exception, and it is why the integral form is worth constructing: it settles the question at the source, where the differential form had to be masked.
:::

### Where do the 1% errors come from?

Every derivative on this page is a centred difference, accurate to $O(\Delta x^{2})$: halving the spacing should reduce the error by four. Confirm it. The study is a single loop.

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

Compare each ratio with the square of the spacing ratio: $1.5^2 = 2.25$ from $n=21$ to $31$, $1.33^2 = 1.78$ from $31$ to $41$, and $1.5^2 = 2.25$ from $41$ to $61$.

The 1.06% in Task 4 is therefore not noise to be tolerated but a predictable quantity that can be reduced at a known cost, and the choice of $n = 61$ in Lab 1 can now be audited rather than assumed.
:::

---

## Part 3 — Curl

Return to field **(b)**, the rotation. Its divergence is zero everywhere, so by that measure it is indistinguishable from a field doing nothing. It nevertheless circulates, and every streamline closes on itself.

The divergence cannot detect circulation. The operator that can is the **curl**, the third of the three operators this chapter is named after.

:::{admonition} Exercises to follow
:class: note

The computer exercises for the curl are not drafted yet. They will build on the circulation
integral and Stokes' theorem, using field **(b)** of Task 3 as the first test case.
:::

---

## Closing

The chain built in this lab, in one line:

$$ \rho_v \;\longrightarrow\; V \;\xrightarrow{\ -\nabla\ }\; \boldsymbol{E} \;\xrightarrow{\ \nabla\cdot\ }\; \rho_v/\varepsilon_0 $$

- **Gradient.** Scalar in, vector out. Points along steepest increase, normal to the level surfaces, with length equal to the rate of increase.
- **Divergence.** Vector in, scalar out. Net flux per unit volume, which measures what is created at a point and nothing else.

### The same two operators, elsewhere in ECT

Electrostatics is a convenient place to learn this pair, not the only place to use it. Each row below gives a potential, its gradient, and a statement about sources. The numerical machinery written in this lab applies unchanged to all of them:

| System | Potential | Field | Source equation |
| :--- | :--- | :--- | :--- |
| Electrostatics | $V$ [V] | $\boldsymbol{E} = -\nabla V$ &nbsp; [V/m] | $\nabla\cdot\boldsymbol{E} = \rho_v/\varepsilon_0$ |
| Gravitation | $\Phi$ [J/kg] | $\boldsymbol{g} = -\nabla \Phi$ &nbsp; [m/s$^2$] | $\nabla\cdot\boldsymbol{g} = -4\pi G\rho_m$ |
| Heat conduction | $T$ [K] | $\boldsymbol{q}_T = -k\nabla T$ &nbsp; [W/m$^2$] | $\nabla\cdot\boldsymbol{q}_T = 0$ (steady, no sources) |
| Groundwater flow | $h$ [m] | $\boldsymbol{q}_h = -K\nabla h$ &nbsp; [m/s] | $\nabla\cdot\boldsymbol{q}_h = 0$ (steady, incompressible) |

with $k$ the thermal conductivity [W m$^{-1}$ K$^{-1}$] and $K$ the hydraulic conductivity [m/s].

The minus signs are all the same minus sign: heat flows from hot to cold, water flows from high head to low, a positive charge falls from high potential to low. Flow runs downhill, and the gradient points uphill.

The last two rows show why solenoidal fields matter in practice. $\nabla\cdot\boldsymbol{q} = 0$ in an aquifer is not an approximation of convenience; it is conservation of water written locally.

### Homework

The exercises in the lecture notes are the written homework. Below is the lab's computational extension, which carries the same two operators into a different physical system.

**A heat source in a room.** Replace the spherical blob with a flat rectangular heater, $1.0 \times 0.6$ m in the $z = 0$ plane. A steady point source of power $P$ in a medium of conductivity $k$ raises the temperature above ambient by $P/4\pi k r$, the same $1/r$ used throughout this lab. Split the plate into $N = 20 \times 12$ sub-sources, give each an equal share $P/N$ of the power, and superpose them as two charges were superposed in Lab 1's Task 8:

$$ T(\boldsymbol{r}) = \frac{P}{4\pi k N}\sum_{i=1}^{N} \frac{1}{\lvert \boldsymbol{r} - \boldsymbol{r}_i \rvert}, \qquad P = 100\ \text{W}, \qquad k_{\text{air}} = 0.026\ \text{W m}^{-1}\text{K}^{-1}. $$

Check the dimensions before coding: $[P]/[k] = \text{W}/(\text{W m}^{-1}\text{K}^{-1}) = \text{m}\cdot\text{K}$, divided by a distance, so $T$ comes out in kelvin. A temperature formula that does not reduce to kelvin contains an error. Then:

- Plot the isosurfaces. Close to the plate they should be rounded rectangles; far away they should become spheres. Explain why the shape loses the imprint of its source.
- Compute the heat flux $\boldsymbol{q}_T = -k\nabla T$, with the same minus sign and the same reason as $\boldsymbol{E} = -\nabla V$.
- Check that $\nabla\cdot\boldsymbol{q}_T \approx 0$ away from the heater, and that the closed-surface flux through a box containing the plate is *not* zero. State what each result means physically for a room at steady state, and which of the two fields in Task 2 the heater resembles.
- **Then examine the number.** One metre from a 100 W panel this model predicts about $+290$ K above ambient, a room at 300 °C. The arithmetic is correct, so the physics is wrong. Identify the failed assumption; two are worth naming, namely what actually transports heat through air, and where this solution places the walls of the room. Re-running with $k = 1.5$ W m⁻¹K⁻¹, the conductivity of soil, gives $+5$ K: the same equations now describe a buried heating element, a problem that pure conduction does solve.
