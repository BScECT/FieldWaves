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

# Lab 6: Diffusive electromagnetic fields

:::{admonition} Computer lab
:class: note

A practical companion to the lecture on [electromagnetic diffusive field equations with a source](../em_diffusion.md). Each task states a physical question, gives the formula it rests on, and ends with a picture you can read the answer off.

Everything you write is plain NumPy, and every line that implements an equation names it in a comment. The module `fwtools` only draws: `fw.show_map` (a field over a plane, with a play button), `fw.show_isosurface` (a rotatable 3-D view), `fw.show_profiles`, `fw.show_spacetime` and `fw.show_records`. Every slider runs in the browser.
:::

## Learning objectives

- **One kernel, four geometries.** A sheet, a wire, a point and a loop all produce $t^{-p}\exp(-\sigma\mu r^2/4t)$. Only $p$ changes, and it fixes when the field arrives.
- **Arrival time measures distance.** $t_p=\sigma\mu r^2/4p$ turns a recorded time into a depth, and the conductivity of the ground sets the clock.
- **The magnetic field becomes a potential field.** $\nabla\times\boldsymbol H=-\sigma E_z$ while the field diffuses, and both sides die together.
- **A source forgets its shape.** Once the diffusion distance passes the size of the loop, the field no longer knows the loop was square.

---

## Part 0 — Setup

Run this once. It contains no physics: it fetches two packages the browser lacks and locates `fwtools`.

```{code-cell} ipython3
import sys, pathlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0, epsilon_0
from scipy.special import erf

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
mu = mu_0                      # rock and water are non-magnetic
# ---------------------------------------------------------------------------
print("ready")
```

---

## Part 1 — One dimension: a current sheet

A horizontal current sheet carrying $I$ per unit width is switched on at $t=0$. The field a distance $z$ from it is {eq}`eq:ExtH`,

$$ E_x(z,t) = -I\sqrt{\frac{\mu}{4\pi\sigma t}}\exp\left(-\frac{\sigma\mu z^2}{4t}\right),\qquad t>0 . $$

The exponential is the kernel of the heat equation with $\kappa$ replaced by $1/(\sigma\mu)$, so the field soaks into the ground as heat spreads along a wire. The prefactor falls as $t^{-1/2}$.

Every field in this lab has that form, $t^{-p}\exp(-\sigma\mu r^2/4t)$, with a different $p$. It is worth finding the peak time once, for any $p$.

### Task 1 — when does the field arrive, and in what ground?

Setting $\partial_t\ln|E|=0$ is easier than differentiating $|E|$ itself and gives the same answer. With a prefactor $t^{-p}$,

$$ -\frac{p}{t} + \frac{\sigma\mu r^2}{4t^2} = 0 . $$

Solve it for $t$ and write the result once, as `t_peak(r, p, s)`.

**Predict** before running: does a deeper receiver peak earlier or later, and by what power of $z$? Then the same receiver in three grounds, seawater at 4 S/m, saturated sediments at $10^{-2}$ S/m and crystalline basement at $10^{-4}$ S/m. Rank them by arrival time.

The second blank is the margin the diffusive approximation still has. Dropping $\varepsilon\,\partial_t\boldsymbol E$ is safe only while the peak arrives long after the charge relaxation time $\tau_r=\varepsilon/\sigma$. Write $t_p/\tau_r$ for the sheet in closed form, in terms of $z$ and $\sigma$, and watch what $\sigma$ does to it.

```{code-cell} ipython3
sigma_sheet, eps_r, I_sheet = 0.01, 10.0, 1.0   # sediments [S/m], relative permittivity, [A/m]
tau_r = eps_r * epsilon_0 / sigma_sheet         # charge relaxation time [s]

def E_sheet(z, t, s=sigma_sheet):
    """eq:ExtH -- the field of a current sheet switched on at t = 0 [V/m]."""
    return -I_sheet * np.sqrt(mu / (4*np.pi*s*t)) * np.exp(-s*mu*z**2 / (4*t))

# Task 1 -- two blanks.
def t_peak(r, p, s):
    """Time at which t**(-p) * exp(-s*mu*r**2/(4t)) is largest [s].
    Solve  -p/t + s*mu*r**2/(4*t**2) = 0  for t."""
    return ___

def peak_over_relax(z, s):
    """How many charge relaxation times the sheet's peak waits, t_p / tau_r.
    The sheet has p = 1/2, and tau_r = eps_r*epsilon_0/s."""
    return ___

# --- given: the field soaking downward. Drag the bar, or press play ---------
z_grid = np.linspace(1.0, 2000.0, 400)                   # depth [m]
t_grid = np.logspace(-6, -1.3, 60)                       # [s]
soak = np.array([np.abs(E_sheet(z_grid, tv)) / np.abs(E_sheet(1.0, tv)) for tv in t_grid])
fw.show_profiles(z_grid, soak, t_grid, value_name="t", value_fmt="{:.2g}", unit=" s",
                 xlabel="depth z [m]", ylabel="|E<sub>x</sub>| / its value at the surface",
                 title="The field diffuses into the Earth", ylim=(0.0, 1.05))

# --- given: depth against time, with your arrival-time curve over it --------
fw.show_spacetime(z_grid, t_grid, soak, t_label="t [s]", x_label="depth z [m]",
                  c_label=r"$|E_x|$ / surface value", signed=False,
                  curve=(t_peak(z_grid, 0.5, sigma_sheet), z_grid),
                  curve_label=r"your $t_p(z)$", deeper_down=True,
                  title=r"Deeper means later: does your curve follow the ridge?")

# --- given: what a receiver records at three depths ------------------------
t_rec = np.logspace(-6, -1, 3001)                        # [s]
depths = [100.0, 300.0, 1000.0]                          # [m]
fw.show_records(t_rec, {f"z = {z:g} m": np.abs(E_sheet(z, t_rec)) / np.max(np.abs(E_sheet(z, t_rec)))
                        for z in depths},
                peaks={f"z = {z:g} m": (t_peak(z, 0.5, sigma_sheet), 1.0) for z in depths},
                t_label="t [s]", y_label=r"$|E_x|$ / peak value",
                title=r"Step response at depth, $\sigma$ = 0.01 S/m")

fw.check_scalar("t_p at 300 m against the peak of the record",
                t_peak(300.0, 0.5, sigma_sheet),
                t_rec[np.argmax(np.abs(E_sheet(300.0, t_rec)))], rtol=0.01, unit=" s")
```

```{code-cell} ipython3
# --- given: one receiver at 300 m, three grounds ---------------------------
media = {"seawater, 4 S/m": 4.0,
         "saturated sediments, 1e-2 S/m": 0.01,
         "crystalline basement, 1e-4 S/m": 1e-4}
z_s, t_s = 300.0, np.logspace(-8, 1, 900)

fw.show_records(t_s, {k: np.abs(E_sheet(z_s, t_s, sv)) / np.max(np.abs(E_sheet(z_s, t_s, sv)))
                      for k, sv in media.items()},
                peaks={k: (t_peak(z_s, 0.5, sv), 1.0) for k, sv in media.items()},
                t_label="t [s]", y_label="|E| / peak value",
                title=f"The same receiver at {z_s:.0f} m, in three grounds")

print(f"at z = {z_s:.0f} m\n")
print(f"{'ground':<30}{'t_p [s]':>11}{'tau_r [s]':>11}{'t_p / tau_r':>13}")
for k, sv in media.items():
    print(f"{k:<30}{t_peak(z_s, 0.5, sv):>11.3g}{eps_r*epsilon_0/sv:>11.3g}"
          f"{peak_over_relax(z_s, sv):>13.3g}")

fw.check("a tenfold drop in conductivity costs a hundredfold in margin",
         np.isclose(peak_over_relax(300.0, 1e-3) / peak_over_relax(300.0, 1e-4), 100.0, rtol=1e-9),
         "the margin goes as sigma squared, not as sigma")
```

:::{admonition} Solution — Task 1
:class: dropdown

```python
def t_peak(r, p, s):
    return s * mu * r**2 / (4 * p)

def peak_over_relax(z, s):
    return s**2 * mu * z**2 / (2 * eps_r * epsilon_0)
```
:::

:::{admonition} Depth maps onto arrival time, and conductivity sets the clock
:class: important dropdown

A layer ten times deeper answers a hundred times later: 63 µs at 100 m, 6.3 ms at 1 km, for $\sigma=0.01$ S/m. Your curve runs along the shoulder of the diffusing field, because $|E_x|$ has fallen to $1/\sqrt e$ of its surface value exactly where $t=\sigma\mu z^2/2$. Time-domain electromagnetic soundings rest on this: the later part of a record senses the deeper Earth.

At 300 m the peak arrives after 0.23 s in seawater, 0.57 ms in sediments and 5.7 µs in basement, a factor $4\times10^4$ from basement to seawater. That is exactly the ratio of the two conductivities, because $t_p=\sigma\mu z^2/2$ is linear in $\sigma$. A conductive ground holds the field up; a resistive one lets it through at once.

The margin behaves differently. $\tau_r=\varepsilon/\sigma$ grows as the ground becomes resistive while $t_p$ shrinks, so

$$ \frac{t_p}{\tau_r} = \frac{\sigma^2\mu z^2}{2\varepsilon} $$

carries $\sigma$ twice: $10^{10}$ in seawater, $6.4\times10^4$ in sediments, and **6.4** in basement. The diffusive approximation is comfortable in the first two and running out in the third, and it is the *resistive* ground that breaks it. Dropping $\varepsilon\,\partial_t\boldsymbol E$ was never a statement about depth. It is a statement about how fast charge can relax.
:::

---

## Part 2 — Two dimensions: an infinite wire

A long wire along $z$ carries a current switched on at $t=0$. Nothing depends on $z$, so the field lives in the $(x,y)$-plane: the electric field is $E_z$, perpendicular to that plane, and the magnetic field lies in it. This is the Transverse Electric mode of the lecture, and the chapter gives

$$ E_z(\varrho,t) = \frac{\mu I}{4\pi t}\exp\left(-\frac{\sigma\mu\varrho^2}{4t}\right),\qquad \varrho=\sqrt{x^2+y^2}. $$

The kernel is the same as the sheet's. The prefactor is now $t^{-1}$, so $p=1$.

### Task 2 — the field of the wire, and when it arrives

Write $E_z$. Then **predict**, before running: at the same distance, does the wire's field peak earlier or later than the sheet's, and by what factor?

```{code-cell} ipython3
sigma_wire, I_wire = 3.0, 1.0            # seawater [S/m], wire current [A]

# Task 2 -- one blank.
def E_wire(rho, t, s=sigma_wire):
    """E_z of an infinitely long wire with a step switch-on current [V/m].
    Prefactor t**(-1), times the kernel exp(-s*mu*rho**2/(4t))."""
    return ___

# --- given: the field spreading out from the wire, on a logarithmic colour scale ---
n_w = 91
x_w = np.linspace(-50.0, 50.0, n_w)                        # [m]
X_w, Y_w = np.meshgrid(x_w, x_w, indexing="ij")            # F[ix, iy] sits at (x[ix], y[iy])
rho_w = np.hypot(X_w, Y_w)
rho_w[rho_w == 0] = x_w[1] - x_w[0]                        # keep the wire out of the formula
t_w = np.logspace(-4, 0, 16)                               # [s]

E_frames = np.array([E_wire(rho_w, tv) for tv in t_w])
fw.show_map(x_w, x_w, E_frames, t_w, value_name="t", value_fmt="{:.2g}", unit=" s",
            x_label="x [m]", y_label="y [m]", c_label="log<sub>10</sub>(E<sub>z</sub> / max)",
            log_c=True, per_frame_scale=True, title="The electric field spreads out from the wire")

# --- given: three receivers, with your arrival times marked ----------------
t_r = np.logspace(-6, 1, 3001)
dists = [0.36, 15.0, 30.0]                                 # [m]
fw.show_records(t_r, {f"{d:g} m": E_wire(d, t_r) / np.max(E_wire(d, t_r)) for d in dists},
                peaks={f"{d:g} m": (t_peak(d, 1, sigma_wire), 1.0) for d in dists},
                t_label="t [s]", y_label=r"$E_z$ / peak value",
                title=r"The wire, $\sigma$ = 3 S/m: close in, the field is already fading")

print(f"the sheet and the wire at the same 15 m, in the same ground:")
print(f"   sheet, p = 1/2 : t_p = {t_peak(15.0, 0.5, sigma_wire)*1e3:.3f} ms")
print(f"   wire,  p = 1   : t_p = {t_peak(15.0, 1.0, sigma_wire)*1e3:.3f} ms")

_tp15 = t_peak(15.0, 1, sigma_wire)
fw.check_scalar("t_p at 15 m against the peak of the record", _tp15,
                t_r[np.argmax(E_wire(15.0, t_r))], rtol=0.01, unit=" s")
fw.check_scalar("the peak value, against mu I / (4 pi t_p) times 1/e", E_wire(15.0, _tp15),
                mu*I_wire/(4*np.pi*_tp15)*np.exp(-1.0), rtol=0.01, unit=" V/m")
```

:::{admonition} Solution — Task 2
:class: dropdown

```python
def E_wire(rho, t, s=sigma_wire):
    return mu * I_wire / (4*np.pi*t) * np.exp(-s*mu*rho**2 / (4*t))
```
:::

### Task 3 — the magnetic field climbs to its static value

The wire's magnetic field circles it. Long after switch-on it must settle at the static result of the curl chapter, $\boldsymbol H = I\hat{\boldsymbol\varphi}/(2\pi\varrho)$. The chapter shows that it approaches that value through the same exponential that shapes $E_z$, with no power of $t$ in front:

$$ \frac{|\boldsymbol H|}{|\boldsymbol H|_{\text{static}}} = \exp\left(-\frac{\sigma\mu\varrho^2}{4t}\right),\qquad |\boldsymbol H|_{\text{static}} = \frac{I}{2\pi\varrho}. $$

Write that ratio. It runs from 0 at switch-on to 1 at late time, so the picture shows how far the field has got, not how strong it is.

Then move the conductivity slider on the second figure. **Predict** first: in which ground does the magnetic field reach its static value soonest?

```{code-cell} ipython3
# Task 3 -- one blank.
def H_over_static(rho, t, s=sigma_wire):
    """|H| divided by its static value. Dimensionless, 0 at switch-on and 1 at late time."""
    return ___

# --- given: the magnetic field filling in, with its direction ---------------
H_frames = np.array([H_over_static(rho_w, tv) for tv in t_w])
Hx_dir = np.broadcast_to(-Y_w / rho_w, (len(t_w),) + rho_w.shape)   # the unit vector phi-hat
Hy_dir = np.broadcast_to( X_w / rho_w, (len(t_w),) + rho_w.shape)
fw.show_map(x_w, x_w, H_frames, t_w, arrows=(Hx_dir, Hy_dir), arrow_every=10,
            value_name="t", value_fmt="{:.2g}", unit=" s", zmin=0.0, zmax=1.0,
            x_label="x [m]", y_label="y [m]", c_label="|H| / static value",
            title="The magnetic field is already circular. It is only filling in")

# --- given: how far it still has to go, in three grounds -------------------
t_h = np.logspace(-5, 2, 400)
sigmas = np.array([0.01, 0.1, 1.0, 3.0, 10.0])             # [S/m]
gap = {f"{d:g} m": np.array([1.0 - H_over_static(d, t_h, sv) for sv in sigmas])
       for d in (15.0, 30.0)}
fw.show_profiles(t_h, gap, sigmas, value_name="&#963;", value_fmt="{:.3g}", unit=" S/m",
                 xlabel="t [s]", ylabel="1 &#8722; |H| / static value", log_x=True, log_y=True,
                 title="The distance still to go falls as 1/t, and a conductive ground is slower")

fw.check("the ratio climbs from 0 at switch-on to 1 at late time",
         H_over_static(15.0, 1e-5) < 1e-6 and abs(H_over_static(15.0, 1e2) - 1.0) < 1e-3,
         "it is exp(-a/t), not 1 - exp(-a/t): at t -> 0 there is no field yet")
```

:::{admonition} Solution — Task 3
:class: dropdown

```python
def H_over_static(rho, t, s=sigma_wire):
    return np.exp(-s*mu*rho**2 / (4*t))
```
:::

### Task 4 — while it diffuses, the magnetic field has curl

The second of the chapter's two-dimensional equations is $\partial_xH_y-\partial_yH_x+\sigma E_z=0$ away from the wire. The curl of $\boldsymbol H$ is not an abstraction here: it is the electric field, times $-\sigma$. As $E_z$ dies the curl dies with it, and the magnetic field becomes a potential field.

Write the $z$-component of the curl. The two derivatives of each component are already computed for you.

```{code-cell} ipython3
t_c = 1e-3                                                  # one instant [s]
dx = x_w[1] - x_w[0]
H_mag = I_wire / (2*np.pi*rho_w) * H_over_static(rho_w, t_c)
Hx_c, Hy_c = -Y_w/rho_w * H_mag, X_w/rho_w * H_mag          # [A/m]

dHx_dx, dHx_dy = np.gradient(Hx_c, dx, dx)                  # indexing='ij', so [0] is d/dx
dHy_dx, dHy_dy = np.gradient(Hy_c, dx, dx)

# Task 4 -- one blank: the z-component of the curl of H.
curl_z = ___

# --- given: the curl beside the electric field it equals -------------------
shown = rho_w > 8.0                     # H goes as 1/rho, so the grid cannot follow it at the wire
fw.show_map(x_w, x_w, np.array([np.where(shown, curl_z, np.nan),
                                np.where(shown, -sigma_wire*E_wire(rho_w, t_c), np.nan)]),
            ["curl of H", "minus sigma times E_z"], value_name="showing", value_fmt="{}",
            x_label="x [m]", y_label="y [m]", c_label="A/m&#178;",
            title=f"Two ways to the same picture, at t = {t_c*1e3:g} ms")

# The comparison is made on the outer ring, where a 1.1 m grid resolves 1/rho.
ring = (rho_w > 20.0) & (rho_w < 45.0)
fw.check_close("the curl of H against minus sigma E_z, away from the wire",
               curl_z[ring], -sigma_wire*E_wire(rho_w, t_c)[ring], rtol=0.05,
               hint="eq:TEEy with no source: d_x H_y - d_y H_x + sigma E_z = 0")
```

:::{admonition} Solution — Task 4
:class: dropdown

```python
curl_z = dHy_dx - dHx_dy
```
:::

:::{admonition} The wire answers twice as fast as the sheet, and the curl dies with the electric field
:class: important dropdown

At 15 m in seawater the sheet peaks at 0.42 ms and the wire at 0.21 ms, a factor of two, because $t_p=\sigma\mu r^2/4p$ and $p$ went from $1/2$ to $1$. A steeper prefactor pulls the peak earlier: the field is being drained faster, so the moment at which arrival stops winning over decay comes sooner.

The two magnetic pictures say different things. The map never changes shape, because the direction $\hat{\boldsymbol\varphi}$ is circular from the first instant and only the amount fills in. What takes time is the *amount*, and the second figure shows how far there is still to go. Expanding the exponential for $t\gg\sigma\mu\varrho^2/4$,

$$ 1 - \exp\left(-\frac{\sigma\mu\varrho^2}{4t}\right) \approx \frac{\sigma\mu\varrho^2}{4t}, $$

so the gap closes as $1/t$, which is the straight line of slope $-1$ on the logarithmic axes. A conductive ground is slower, and doubling the distance costs a factor of four in waiting.

The curl map is the electric field map, rescaled. That is {eq}`eq:TEEy` read as a picture, and it is the sharpest statement of what makes a diffusive field different from a static one: the static magnetic field of the curl chapter is curl-free outside the wire, and this one is not, for exactly as long as there is an electric field to drive it. Let $t$ run on and both die, which is why the chapter says the magnetic field becomes a potential field at infinite time.
:::

---

## Part 3 — Three dimensions, and one law for all of them

A point source in three dimensions has the impulse response {eq}`eq:G3D`,

$$ G(R,t) = \frac{(\sigma\mu)^{1/2}}{[4\pi t]^{3/2}}\exp\left(-\frac{\sigma\mu R^2}{4t}\right). $$

Same kernel again. The prefactor is $t^{-3/2}$, so $p=3/2$.

### Task 5 — the ladder

Write $G$. Your `t_peak` already covers it: the three geometries differ only in $p$, so at the same distance their peak times are in a fixed ratio. **Predict** that ratio before you run the last figure.

```{code-cell} ipython3
sigma_pt = 0.01                                             # sediments [S/m]

# Task 5 -- one blank.
def G_point(R, t, s=sigma_pt):
    """eq:G3D -- the impulse response in three dimensions [1/m]."""
    return ___

# --- given: a rotatable view of the field at one instant -------------------
# Change t_show and run the cell again to watch the shell move outward.
t_show = 1.0e-3                                             # [s]
g_xy = np.linspace(-400.0, 400.0, 32)                       # [m]
g_z = np.linspace(0.0, 800.0, 32)                           # depth [m]
GX, GY, GZ = np.meshgrid(g_xy, g_xy, g_z, indexing="ij")
G_vol = G_point(np.sqrt(GX**2 + GY**2 + GZ**2), t_show)
fw.show_isosurface(g_xy, g_xy, g_z, G_vol, levels=(0.08, 0.25, 0.6), opacity=0.32,
                   c_label="G", z_label="depth z [m]",
                   title=f"The point source at t = {t_show*1e3:g} ms. Drag to rotate")

# --- given: the three geometries at the same distance, same ground ---------
r0 = 300.0                                                  # [m]
t_l = np.logspace(-6, -1, 4001)
ladder = {"sheet,  p = 1/2": np.abs(E_sheet(r0, t_l, sigma_pt)),
          "wire,   p = 1  ": E_wire(r0, t_l, sigma_pt),
          "point,  p = 3/2": G_point(r0, t_l)}
fw.show_records(t_l, {k: v / np.max(v) for k, v in ladder.items()},
                peaks={k: (t_peak(r0, p, sigma_pt), 1.0)
                       for k, p in zip(ladder, (0.5, 1.0, 1.5))},
                t_label="t [s]", y_label="field / its own peak",
                title=f"The same {r0:.0f} m in the same ground, three geometries")

print(f"{'geometry':<12}{'p':>6}{'t_p [ms]':>12}{'ratio':>8}")
for name, p in zip(("sheet", "wire", "point"), (0.5, 1.0, 1.5)):
    tp = t_peak(r0, p, sigma_pt)
    print(f"{name:<12}{p:>6}{tp*1e3:>12.3f}{tp/t_peak(r0, 1.5, sigma_pt):>8.1f}")

fw.check_scalar("the point source peaks at sigma mu R^2 / 6",
                t_peak(r0, 1.5, sigma_pt), t_l[np.argmax(G_point(r0, t_l))],
                rtol=0.01, unit=" s")
_R = np.linspace(0.5, 6000.0, 60000)                        # a radial grid [m]
fw.check_scalar("the integral of G over all space, which fixes the constant in front",
                np.sum(G_point(_R, 1e-3) * 4*np.pi*_R**2) * (_R[1] - _R[0]),
                1.0 / (sigma_pt*mu), rtol=0.01, unit=" m/S")
```

:::{admonition} Solution — Task 5
:class: dropdown

```python
def G_point(R, t, s=sigma_pt):
    return np.sqrt(s*mu) / (4*np.pi*t)**1.5 * np.exp(-s*mu*R**2 / (4*t))
```
:::

:::{admonition} Six, three, two
:class: important dropdown

$$ t_p = \frac{\sigma\mu r^2}{4p}:\qquad \frac{\sigma\mu r^2}{2},\quad \frac{\sigma\mu r^2}{4},\quad \frac{\sigma\mu r^2}{6} $$

for $p=\tfrac12,1,\tfrac32$. The three peak times are in the ratio **6 : 3 : 2**, whatever the distance and whatever the ground, because the kernel is identical and only the prefactor differs. At 300 m in sediments that is 0.57 ms, 0.28 ms and 0.19 ms.

The reason is worth saying in words. The exponential is the arrival: it rises from nothing as the diffusing field reaches $r$, and it does not care about the geometry. The prefactor is the decay: it is how fast the energy is spreading out, over a line, a cylinder or a sphere. The peak is where the two balance, so a geometry that spreads faster peaks earlier. The sphere spreads fastest, and answers first.

The three-dimensional amplitude falls as $1/R^3$: double the distance and the peak is eight times smaller, against four for the wire and two for the sheet. Volume is expensive.
:::

---

## Part 4 — A loop on the surface

A real transmitter is a loop, not an infinite wire. A square loop of side $L_x=L_y=100$ m lies on the surface and its current is switched on at $t=0$. Integrating the three-dimensional Green's function along the four segments gives {eq}`eq:Exloop` and {eq}`eq:Eyloop`:

$$ E_y(\boldsymbol r,t) = -\frac{\mu}{8\pi t}\left\{\exp\left(-\frac{x_m^2+z^2}{D^2}\right) - \exp\left(-\frac{x_p^2+z^2}{D^2}\right)\right\}\left[\mathrm{erf}\left(\frac{y_p}{D}\right) - \mathrm{erf}\left(\frac{y_m}{D}\right)\right] $$

with $x_p=x+L_x/2$, $x_m=x-L_x/2$, and the **diffusion distance**

$$ D = \sqrt{\frac{4t}{\sigma\mu}} , $$

which is how far the field has spread by time $t$. The two exponentials are the two segments that run along $y$, at $x=\pm L_x/2$. They carry opposite currents, so they enter with opposite signs, and that difference is the only part you have to write.

### Task 6 — the loop forgets its shape

Fill in the brace of $E_y$. Then read three things off the pictures.

1. Run the time slider on the $(x,y)$ view. At which $D$ does the square stop looking square? Compare $D$ with $L_x$.
2. Move the depth slider on the third figure. **Predict first** what going deeper does to the picture, then check. The answer is not what most people expect.
3. Rotate the 3-D view.

```{code-cell} ipython3
sigma_loop, Lx, Ly = 0.3, 100.0, 100.0          # [S/m], loop sides [m]

def D_of(t, s=sigma_loop):
    """The diffusion distance [m]: how far the field has spread by time t."""
    return np.sqrt(4*t / (s*mu))

def Ex_loop(x, y, z, t, s=sigma_loop):
    """eq:Exloop -- given, as the pattern to follow [V/m]."""
    D = D_of(t, s)
    xp, xm = x + Lx/2, x - Lx/2                 # to the two segments that run along y
    yp, ym = y + Ly/2, y - Ly/2                 # to the two segments that run along x
    return (-mu / (8*np.pi*t)
            * (np.exp(-(yp**2+z**2)/D**2) - np.exp(-(ym**2+z**2)/D**2))
            * (erf(xp/D) - erf(xm/D)))

# Task 6 -- one blank. eq:Eyloop is eq:Exloop with x and y exchanged, except
# that the two exponentials come in the opposite order, because the two
# segments at x = +-Lx/2 carry opposite currents.
def Ey_loop(x, y, z, t, s=sigma_loop):
    """eq:Eyloop [V/m]."""
    D = D_of(t, s)
    xp, xm = x + Lx/2, x - Lx/2
    yp, ym = y + Ly/2, y - Ly/2
    return ___

def E_loop(x, y, z, t, s=sigma_loop):
    """Both horizontal components, as a pair."""
    return Ex_loop(x, y, z, t, s), Ey_loop(x, y, z, t, s)

# --- given: the vertical plane through the middle of the loop --------------
n_L = 91
x_L = np.linspace(-300.0, 300.0, n_L)                       # [m]
z_L = np.linspace(0.0, 300.0, n_L)
XZ_x, XZ_z = np.meshgrid(x_L, z_L, indexing="ij")
t_L = np.logspace(-5, -1, 16)                               # [s]

xz = np.array([E_loop(XZ_x, 0.0, XZ_z, tv)[1] for tv in t_L])
fw.show_map(x_L, z_L, xz, t_L*1e3, value_name="t", value_fmt="{:.3g}", unit=" ms",
            x_label="x [m]", y_label="depth z [m]", c_label="E<sub>y</sub> [V/m]",
            per_frame_scale=True, y_down=True, equal_aspect=False,
            title="Two lobes of opposite sign, over the two wires, moving apart and down")
```

The same field, finely sampled, from the lecturer's own script. It runs over 200 instants instead of the 16 on your slider.

```{video} figures/ELoopwsxz.mp4
:width: 80%
```

```{code-cell} ipython3
# --- given: the plane at 10 m depth, seen from above. Arrows give direction ---
XY_x, XY_y = np.meshgrid(x_L, x_L, indexing="ij")
EE = [E_loop(XY_x, XY_y, 10.0, tv) for tv in t_L]
mag = np.array([np.hypot(ex, ey) for ex, ey in EE])
fw.show_map(x_L, x_L, mag, t_L*1e3,
            arrows=(np.array([e[0] for e in EE]), np.array([e[1] for e in EE])),
            arrow_every=10, log_c=True, per_frame_scale=True, y_down=True,
            value_name="t", value_fmt="{:.3g}", unit=" ms",
            x_label="x [m]", y_label="y [m]", c_label="log<sub>10</sub>(|E| / max)",
            title="At z = 10 m: watch the square become a circle")

print(f"{'t [ms]':>9}{'D [m]':>9}{'D / Lx':>9}")
for tv in (1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 5e-3):
    print(f"{tv*1e3:>9.3g}{D_of(tv):>9.1f}{D_of(tv)/Lx:>9.2f}")
```

```{code-cell} ipython3
# --- given: the same instant, at a depth you choose -------------------------
t_fix = 3e-4                                                # [s]
z_try = np.array([0.0, 50.0, 100.0, 200.0, 400.0])          # depth [m]
deep = np.array([np.hypot(*E_loop(XY_x, XY_y, zv, t_fix)) for zv in z_try])
fw.show_map(x_L, x_L, deep, z_try, value_name="z", value_fmt="{:.0f}", unit=" m",
            log_c=True, per_frame_scale=False, y_down=True,
            x_label="x [m]", y_label="y [m]", c_label="log<sub>10</sub>(|E| / max)",
            title=f"The same instant, t = {t_fix*1e3:g} ms, at five depths")

print(f"at t = {t_fix*1e3:g} ms the diffusion distance is D = {D_of(t_fix):.0f} m\n")
print(f"{'depth [m]':>11}{'|E| / its surface value':>26}")
for zv in z_try:
    f = np.exp(-zv**2 / D_of(t_fix)**2)
    print(f"{zv:>11.0f}{f:>26.4f}")
```

```{code-cell} ipython3
# --- given: the loop in three dimensions. Drag to rotate --------------------
t_3d = 3e-5                                                 # [s]
g3 = np.linspace(-180.0, 180.0, 36)                         # [m]
gz3 = np.linspace(0.0, 180.0, 36)                           # depth [m]
L3x, L3y, L3z = np.meshgrid(g3, g3, gz3, indexing="ij")
E3x, E3y = E_loop(L3x, L3y, L3z, t_3d)
loop_wire = ([-Lx/2, Lx/2, Lx/2, -Lx/2, -Lx/2],
             [-Ly/2, -Ly/2, Ly/2, Ly/2, -Ly/2], [0, 0, 0, 0, 0])
fw.show_isosurface(g3, g3, gz3, np.hypot(E3x, E3y), levels=(0.06, 0.18, 0.45), opacity=0.3,
                   wire=loop_wire, wire_name="the loop", c_label="|E| [V/m]",
                   z_label="depth z [m]",
                   title=f"t = {t_3d*1e3:g} ms, so D = {D_of(t_3d):.0f} m. The loop is still square")

fw.check("the field opposes the source current over the x = +Lx/2 wire",
         E_loop(Lx/2, 0.0, 10.0, 3e-5)[1] < 0 < E_loop(-Lx/2, 0.0, 10.0, 3e-5)[1],
         "the current there runs in +y, so an opposing field has E_y < 0")
```

:::{admonition} Solution — Task 6
:class: dropdown

```python
def Ey_loop(x, y, z, t, s=sigma_loop):
    D = D_of(t, s)
    xp, xm = x + Lx/2, x - Lx/2
    yp, ym = y + Ly/2, y - Ly/2
    return (-mu / (8*np.pi*t)
            * (np.exp(-(xm**2+z**2)/D**2) - np.exp(-(xp**2+z**2)/D**2))
            * (erf(yp/D) - erf(ym/D)))
```
:::

:::{admonition} Time changes the shape. Depth does not
:class: important dropdown

**The square survives while $D$ is small.** At $t=0.01$ ms, $D=10$ m against a 100 m loop and the four wires are separate bright lines. By $t=0.1$ ms, $D=33$ m, and the pattern is already round. The loop stops looking square at about $D\approx L_x/3$, which is $t\approx\sigma\mu L_x^2/36$, here 0.1 ms. After that no measurement can tell this loop from a round one of the same area. A source forgets its shape once the field has diffused further than the source is big, and this is the same blurring that merged two Gaussians in the last lab.

**Depth only dims it.** Put $z$ into {eq}`eq:Eyloop` and the depth appears as $\exp[-(x_m^2+z^2)/D^2]$, which factors into $\exp(-z^2/D^2)$ times the surface expression, identically for both components. So

$$ \boldsymbol E(x,y,z,t) = \exp\left(-\frac{z^2}{D^2}\right)\boldsymbol E(x,y,0,t). $$

Going deeper multiplies the whole picture by one number. It does not blur it, does not rotate it, does not change which way the arrows point. The five frames of the depth figure are the same image at five brightnesses, and the printed column is that one factor.

That factor is the whole of depth sounding. At $t=0.3$ ms, $D=56$ m, so 50 m down you still have 46% of the surface field and 200 m down you have $3.5\times10^{-6}$ of it. You can only see about as deep as $D$, and $D$ grows as $\sqrt t$. To look twice as deep you must wait four times as long, which is Part 1's $t_p\propto z^2$ arriving from the other direction.

**The arrows oppose the current.** Over the wire at $x=+L_x/2$ the current runs in $+\hat{\boldsymbol y}$ and $E_y$ is negative. The switched-on current drives a field that opposes it, which is Lenz's law seen in a conductor.
:::

---

## Part 5 — Designing a sounding

You now have everything a time-domain electromagnetic survey rests on. This part asks you to put it together. Answer the four questions first, from the formulas and not from a new calculation, then run the cell.

1. A target lies 400 m down in ground of conductivity $10^{-2}$ S/m. Roughly when does the response from that depth arrive? Which of Part 1's three formulas did you use, and does the choice matter at the factor-of-two level?
2. Your recording window is 10 µs to 10 ms. Which of the three grounds of Part 1 puts a 400 m target inside that window?
3. You have two loops, 50 m and 400 m on a side. The target is 400 m down. Which do you choose, and what decides it: the loop size, or the time you record for?
4. The field at the target is $\exp(-z^2/D^2)$ of its surface value. Below which amplitude would you say the target is not being illuminated at all, and what does that make the deepest usable depth?

```{code-cell} ipython3
# --- given: the window, the ground and the depth, all on one picture -------
z_target = 400.0                                            # [m]
t_win = (1e-5, 1e-2)                                        # the recording window [s]
t_d = np.logspace(-7, 1, 2001)

fig, ax = plt.subplots(figsize=(8.2, 3.6))
for k, (name, sv) in enumerate(media.items()):
    ax.plot(t_d, np.exp(-z_target**2 * sv * mu / (4*t_d)), color=f"C{k}", lw=2, label=name)
    ax.axvline(t_peak(z_target, 0.5, sv), color=f"C{k}", ls=":", lw=1.2)
ax.axvspan(*t_win, color="0.85", zorder=0, label="recording window")
ax.axhline(1/np.e, color="k", lw=0.8, ls="--")
ax.text(1.3e-7, 1/np.e*1.1, "z = D", fontsize=8)
ax.set_xscale("log"); ax.set_xlabel("t [s]")
ax.set_ylabel(f"illumination at {z_target:.0f} m,  exp(-z²/D²)")
ax.set_title("Which ground puts a 400 m target inside the window?")
ax.grid(alpha=0.3); ax.legend(fontsize=8, loc="upper left")
plt.show()

print(f"a target at {z_target:.0f} m, window {t_win[0]*1e6:.0f} us to {t_win[1]*1e3:.0f} ms\n")
print(f"{'ground':<30}{'t_p [s]':>11}{'in window?':>12}{'illum. at 10 ms':>18}")
for name, sv in media.items():
    tp = t_peak(z_target, 0.5, sv)
    lit = np.exp(-z_target**2 * sv * mu / (4*t_win[1]))
    print(f"{name:<30}{tp:>11.3g}{'yes' if t_win[0] < tp < t_win[1] else 'no':>12}{lit:>18.3g}")
```

:::{admonition} Answers
:class: dropdown

**1.** $t_p=\sigma\mu z^2/2 = 1.0$ ms for the sheet. The wire gives 0.50 ms and the point source 0.34 ms. The choice changes the answer by a factor of three at most, and a survey design is not accurate to a factor of three anyway, so any of them sets the scale. What matters is $t\sim\sigma\mu z^2$, not the number in the denominator.

**2.** Sediments, at 1.0 ms, sit comfortably inside. Seawater peaks at 0.40 s, forty times beyond the end of the window: the window closes long before the response from 400 m arrives. Basement peaks at 10 µs, at the very start of the window, where a real transmitter is still switching off and the useful signal is buried in the turn-off transient. Only the middle ground is workable, and that is typical.

**3.** The time you record for. Depth of investigation is set by $D=\sqrt{4t/\sigma\mu}$, which contains no loop size at all. The loop controls how much signal you get and how far the near-field pattern reaches, not how deep you see. A bigger loop is still worth having, because the amplitude you are fighting to detect is tiny, but you cannot buy depth with it. You buy depth with late time and a quiet receiver.

**4.** Any threshold in the range 1% to 10% gives nearly the same rule, because the Gaussian is so steep. Taking $1/e$ gives $z_{\max}=D=\sqrt{4t/\sigma\mu}$ exactly, which is the standard definition of the diffusion depth. With the 10 ms end of the window in sediments, $D=564$ m, so a 400 m target is at $\exp(-0.50)=0.60$ of the surface field and is well illuminated. In seawater the same 10 ms gives $D=28$ m and the target is at $\exp(-200)$, which is nothing at all.
:::

:::{admonition} What this lab was about
:class: important dropdown

One kernel, $\exp(-\sigma\mu r^2/4t)$, appeared in every part. It came from the heat equation last week with $\kappa$ replaced by $1/(\sigma\mu)$, and the only thing that changed from a sheet to a wire to a point was the power of $t$ in front, which is a statement about geometry and not about electromagnetism.

From that one kernel came three results a geophysicist uses directly. Arrival time measures distance, $t_p=\sigma\mu r^2/4p$. Depth of investigation is the diffusion distance, $z\approx D=\sqrt{4t/\sigma\mu}$, and it is bought with time rather than with equipment. And a source is blurred into a point once $D$ exceeds its size, which is why the shape of a transmitter stops mattering, and also why deep structure is always seen blurred.

The magnetic field made the fourth point. For as long as the electric field is there, $\nabla\times\boldsymbol H=-\sigma E_z$ is not zero, and the magnetic field is not a potential field. It becomes one only in the limit, which is where the magnetostatics of the earlier chapters lives.
:::
