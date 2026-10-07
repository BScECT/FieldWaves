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

- **One kernel, three geometries.** A sheet, a wire and a point all produce $t^{-p}\exp(-\sigma\mu r^2/4t)$. Only $p$ changes, and it fixes when the field arrives. A loop is a superposition of these along four sides, so it has no single kernel, but its arrival still obeys the same $t_p$ with $p=5/2$.
- **Arrival time measures distance.** $t_p=\sigma\mu r^2/4p$ turns a recorded time into a depth, and the conductivity of the ground sets the clock.
- **The magnetic field becomes a potential field.** $(\nabla\times\boldsymbol H)_z=\sigma E_z$ while the field diffuses, and both sides die together.
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

```{figure} figures/setup_sheet.svg
:name: fig-lab6-sheet
:width: 85%

The model of this part. An infinite sheet of current switched on at $t=0$, in a uniform conductor, with receivers at three depths.
```

### Task 1 — when does the field arrive, and in what ground?

Setting $\partial_t\ln|E|=0$ is easier than differentiating $|E|$ itself and gives the same answer. With a prefactor $t^{-p}$,

$$ -\frac{p}{t} + \frac{\sigma\mu r^2}{4t^2} = 0 . $$

Solve it for $t$ and write the result once, as `t_peak(r, p, s)`.

**Predict** before running, and sketch it: on one logarithmic time axis, draw $|E_x|(t)$ at 100 m and at 1000 m, each scaled to its own peak. Are the two curves the same shape, or does the deeper one spread out? Shifted by what factor? Then rank the same receiver in three grounds, seawater at 4 S/m, saturated sediments at $10^{-2}$ S/m and crystalline basement at $10^{-4}$ S/m, by arrival time.

The second blank is the margin the diffusive approximation still has. Dropping $\varepsilon\,\partial_t\boldsymbol E$ is safe only while the peak arrives long after the charge relaxation time $\tau_r=\varepsilon/\sigma$. Write $t_p/\tau_r$ for the sheet in closed form, in terms of $z$ and $\sigma$, and watch what $\sigma$ does to it.

Dividing by the value at the shallowest depth cancels the common $t^{-1/2}$ and leaves the bare kernel $\exp(-\sigma\mu z^2/4t)$: how far the field has reached, not how strong it is. That ratio only climbs and saturates, so look for the shoulder at $1/\sqrt e$, not a maximum. A receiver keeps the $t^{-1/2}$, and there the arriving exponential and the decaying prefactor compete. That competition is what $t_p$ solves.

```{code-cell} ipython3
sigma_sheet, eps_r, I_sheet = 0.01, 10.0, 1.0   # sediments [S/m], relative permittivity, [A/m]
tau_r = eps_r * epsilon_0 / sigma_sheet         # charge relaxation time [s]

def E_sheet(z, t, s=sigma_sheet):
    """eq:ExtH -- the field of a current sheet switched on at t = 0 [V/m]."""
    return -I_sheet * np.sqrt(mu / (4*np.pi*s*t)) * np.exp(-s*mu*z**2 / (4*t))

def t_for_D(D, s):
    """When the diffusion distance sqrt(4t/(s*mu)) reaches D [s]. Used only to
    frame the figures, so that every axis follows the parameters you set."""
    return s * mu * D**2 / 4

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
t_grid = np.logspace(np.log10(t_for_D(z_grid[-1], sigma_sheet)) - 4,
                     np.log10(t_for_D(z_grid[-1], sigma_sheet)), 60)        # [s]
soak = np.array([np.abs(E_sheet(z_grid, tv)) / np.abs(E_sheet(z_grid[0], tv))
                 for tv in t_grid])
fw.show_profiles(z_grid, soak, t_grid, value_name="t", value_fmt="{:.2g}", unit=" s", log_x=True,
                 xlabel="depth z [m]", ylabel="|E<sub>x</sub>| / its value at the surface",
                 title="The field diffuses into the Earth", ylim=(0.0, 1.05))

# --- given: depth against time, with your arrival-time curve over it --------
fw.show_spacetime(z_grid, t_grid, soak, t_label="t [s]", x_label="depth z [m]",
                  c_label=r"$|E_x|$ / surface value", signed=False,
                  curve=(t_peak(z_grid, 0.5, sigma_sheet), z_grid),
                  curve_label=r"your $t_p(z)$", deeper_down=True,
                  title=r"$|E_x|$ against depth and time, with your $t_p(z)$ drawn over it")

# --- given: what a receiver records at three depths ------------------------
depths = [100.0, 300.0, 1000.0]                          # [m]
t_rec = np.logspace(np.log10(t_for_D(min(depths), sigma_sheet)) - 2,
                    np.log10(t_for_D(max(depths), sigma_sheet)) + 2, 3001)  # [s]
fw.show_records(t_rec, {f"z = {z:g} m": np.abs(E_sheet(z, t_rec)) / np.max(np.abs(E_sheet(z, t_rec)))
                        for z in depths},
                peaks={f"z = {z:g} m": (t_peak(z, 0.5, sigma_sheet), 1.0) for z in depths},
                t_label="t [s]", y_label=r"$|E_x|$ / peak value",
                title=f"Step response at depth, sigma = {sigma_sheet:g} S/m")

_zc = depths[1]
fw.check_scalar(f"t_p at {_zc:g} m against the peak of the record",
                t_peak(_zc, 0.5, sigma_sheet),
                t_rec[np.argmax(np.abs(E_sheet(_zc, t_rec)))], rtol=0.01, unit=" s")
```

The same expression evaluated at three conductivities. $t_p$ is linear in $\sigma$ while $\tau_r=\varepsilon/\sigma$ is inverse in it, so those two move opposite ways and their ratio, the margin, carries $\sigma$ twice. A margin above about 100 is comfortable.

```{code-cell} ipython3
# --- given: one receiver at 300 m, three grounds ---------------------------
media = {"seawater, 4 S/m": 4.0,
         "saturated sediments, 1e-2 S/m": 0.01,
         "crystalline basement, 1e-4 S/m": 1e-4}
z_s = 300.0                                             # the receiver depth [m]
_tp_all = [t_peak(z_s, 0.5, sv) for sv in media.values()]
t_s = np.logspace(np.log10(min(_tp_all)) - 3, np.log10(max(_tp_all)) + 2, 900)

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
         np.isclose(peak_over_relax(z_s, 1e-3) / peak_over_relax(z_s, 1e-4), 100.0, rtol=1e-9),
         "the margin goes as sigma squared, not as sigma")
fw.check_scalar("the margin itself, against t_p and tau_r worked out separately",
                peak_over_relax(z_s, sigma_sheet),
                t_peak(z_s, 0.5, sigma_sheet) / (eps_r*epsilon_0/sigma_sheet), rtol=1e-6)
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

$$ E_z(\varrho,t) = -\frac{\mu I}{4\pi t}\exp\left(-\frac{\sigma\mu\varrho^2}{4t}\right),\qquad \varrho=\sqrt{x^2+y^2}. $$

Negative, as the sheet's field was: the current is switched on, and the field it drives in the ground opposes it. The chapter prints this one without the minus sign, which is a slip; the sheet's {eq}`eq:ExtH` carries it.

The kernel is the same as the sheet's. The prefactor is now $t^{-1}$, so $p=1$.

```{figure} figures/setup_wire.svg
:name: fig-lab6-wire
:width: 92%

The model of this part. The wire is a point in the plane you will plot, the electric field points out of that plane, and the magnetic field circles the wire within it.
```

### Task 2 — the field of the wire, and when it arrives

Write $E_z$. Then **predict**, before running: at the same distance, does the wire's field peak earlier or later than the sheet's, and by what factor?

The colour is logarithmic and rescaled frame by frame. The kernel falls off so steeply that one linear scale would leave a bright spot and an empty plane, and the level drops as $1/t$ across the run, so a fixed scale would lose the late frames.

```{code-cell} ipython3
sigma_wire, I_wire = 3.0, 1.0            # seawater [S/m], wire current [A]

# Task 2 -- one blank.
def E_wire(rho, t, s=sigma_wire):
    """E_z of an infinitely long wire with a step switch-on current [V/m].
    Prefactor t**(-1), times the kernel exp(-s*mu*rho**2/(4t)). Opposes the
    current, so it is negative."""
    return ___

# --- given: the field spreading out from the wire, on a logarithmic colour scale ---
n_w, half_w = 91, 50.0
x_w = np.linspace(-half_w, half_w, n_w)                    # [m]
X_w, Y_w = np.meshgrid(x_w, x_w, indexing="ij")            # F[ix, iy] sits at (x[ix], y[iy])
rho_w = np.hypot(X_w, Y_w)
rho_w[rho_w == 0] = x_w[1] - x_w[0]                        # keep the wire out of the formula
# from a fifth of the box to twice it: past that the picture is uniform colour
t_w = np.logspace(np.log10(t_for_D(half_w / 5, sigma_wire)),
                  np.log10(t_for_D(half_w * 2, sigma_wire)), 16)            # [s]

E_frames = np.array([E_wire(rho_w, tv) for tv in t_w])
fw.show_map(x_w, x_w, E_frames, t_w, value_name="t", value_fmt="{:.2g}", unit=" s",
            x_label="x [m]", y_label="y [m]", c_label="log<sub>10</sub>(E<sub>z</sub> / max)",
            log_c=True, per_frame_scale=True, title="The electric field spreads out from the wire")

# --- given: three receivers, with your arrival times marked ----------------
dists = [0.36, 15.0, 30.0]                                 # [m]
d_mid = dists[1]
t_r = np.logspace(np.log10(t_for_D(min(dists), sigma_wire)) - 2,
                  np.log10(t_for_D(max(dists), sigma_wire)) + 3, 3001)      # [s]
fw.show_records(t_r, {f"{d:g} m": np.abs(E_wire(d, t_r)) / np.max(np.abs(E_wire(d, t_r))) for d in dists},
                peaks={f"{d:g} m": (t_peak(d, 1, sigma_wire), 1.0) for d in dists},
                t_label="t [s]", y_label=r"$|E_z|$ / peak value",
                title=f"The wire, sigma = {sigma_wire:g} S/m:"
                      f" close in, the field is already fading")

print(f"the sheet and the wire at the same {d_mid:g} m, in the same ground:")
print(f"   sheet, p = 1/2 : t_p = {t_peak(d_mid, 0.5, sigma_wire)*1e3:.3f} ms")
print(f"   wire,  p = 1   : t_p = {t_peak(d_mid, 1.0, sigma_wire)*1e3:.3f} ms")

_tpm = t_peak(d_mid, 1, sigma_wire)
fw.check_scalar(f"t_p at {d_mid:g} m against the peak of the record", _tpm,
                t_r[np.argmax(np.abs(E_wire(d_mid, t_r)))], rtol=0.01, unit=" s")
fw.check_scalar("the peak value, against -mu I / (4 pi t_p) times 1/e", E_wire(d_mid, _tpm),
                -mu*I_wire/(4*np.pi*_tpm)*np.exp(-1.0), rtol=0.01, unit=" V/m")
```

:::{admonition} Solution — Task 2
:class: dropdown

```python
def E_wire(rho, t, s=sigma_wire):
    return -mu * I_wire / (4*np.pi*t) * np.exp(-s*mu*rho**2 / (4*t))
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

# --- given: how far it still has to go, over five conductivities -----------
sigmas = np.array([0.01, 0.1, 1.0, 3.0, 10.0])             # [S/m]
# wide enough to show the 1/t tail for every curve, and no wider: far below this
# the exponential is zero to machine precision and nothing is left to plot
_a_lo = t_for_D(min(dists[1:]), sigmas.min())
_a_hi = t_for_D(max(dists[1:]), sigmas.max())
t_h = np.logspace(np.log10(_a_hi / 500), np.log10(_a_lo * 1e7), 400)        # [s]
gap = {f"{d:g} m": np.array([1.0 - H_over_static(d, t_h, sv) for sv in sigmas])
       for d in dists[1:]}
fw.show_profiles(t_h, gap, sigmas, value_name="&#963;", value_fmt="{:.3g}", unit=" S/m",
                 xlabel="t [s]", ylabel="1 &#8722; |H| / static value", log_x=True, log_y=True,
                 title="How far the magnetic field still has to go, against time")

# "early" and "late" written in terms of the problem, so the test survives a change
# of sigma_wire or of the distance: the field has spread a fifth of d_mid, then a hundred times it.
_early, _late = t_for_D(d_mid / 5, sigma_wire), t_for_D(d_mid * 100, sigma_wire)
fw.check("the ratio climbs from 0 at switch-on to 1 at late time",
         H_over_static(d_mid, _early) < 1e-6 and abs(H_over_static(d_mid, _late) - 1.0) < 1e-3,
         "it is exp(-a/t), not 1 - exp(-a/t): at t -> 0 there is no field yet")
# the shape alone does not pin the clock: a wrong factor in the exponent still
# climbs from 0 to 1. This fixes when, using the t_p you already wrote.
fw.check_scalar("|H| is at 1/e of static exactly at the wire's own peak time",
                H_over_static(d_mid, t_peak(d_mid, 1, sigma_wire)), np.exp(-1.0), rtol=1e-6)
```

:::{admonition} Solution — Task 3
:class: dropdown

```python
def H_over_static(rho, t, s=sigma_wire):
    return np.exp(-s*mu*rho**2 / (4*t))
```
:::

### Task 4 — while it diffuses, the magnetic field has curl

The chapter's two-dimensional equation that connects the fields to the source is $-\partial_xH_y+\partial_yH_x+\sigma E_z=0$ away from the wire, which is Ampère's law, $\nabla\times\boldsymbol H=\sigma\boldsymbol E$, in two dimensions. The curl of $\boldsymbol H$ is not an abstraction here: it is the electric field, times $\sigma$. As $E_z$ dies the curl dies with it, and the magnetic field becomes a potential field.

Write the $z$-component of the curl. The two derivatives of each component are already computed for you.

With no source this says $\partial_xH_y-\partial_yH_x=\sigma E_z$, and both sides are negative because $E_z$ is. Where the two pictures agree, the diffusing magnetic field is demonstrably not curl-free. Near the wire they will not agree, because a finite grid cannot follow $1/\varrho$.

```{code-cell} ipython3
# One instant, chosen so the field has spread about as far as the ring the check uses.
# That makes the accuracy below independent of sigma_wire.
r_ring = (0.4*half_w, 0.9*half_w)                           # the comparison ring [m]
t_c = t_for_D(np.mean(r_ring), sigma_wire)                  # [s]
dx = x_w[1] - x_w[0]
H_mag = I_wire / (2*np.pi*rho_w) * H_over_static(rho_w, t_c)
Hx_c, Hy_c = -Y_w/rho_w * H_mag, X_w/rho_w * H_mag          # [A/m]

dHx_dx, dHx_dy = np.gradient(Hx_c, dx, dx)                  # indexing='ij', so [0] is d/dx
dHy_dx, dHy_dy = np.gradient(Hy_c, dx, dx)

# Task 4 -- one blank: the z-component of the curl of H.
curl_z = ___

# --- given: the curl beside the electric field it equals -------------------
shown = rho_w > 7*dx                    # H goes as 1/rho, so the grid cannot follow it at the wire
fw.show_map(x_w, x_w, np.array([np.where(shown, curl_z, np.nan),
                                np.where(shown, sigma_wire*E_wire(rho_w, t_c), np.nan)]),
            ["curl of H", "sigma times E_z"], value_name="showing", value_fmt="{}",
            x_label="x [m]", y_label="y [m]", c_label="A/m&#178;",
            title=f"Two ways to the same picture, at t = {t_c*1e3:g} ms")

# The comparison is made on the outer ring, where the grid resolves 1/rho. Push t_c
# up and it will fail: the true curl is on its way to zero, and round-off takes over.
ring = (rho_w > r_ring[0]) & (rho_w < r_ring[1])
fw.check_close("the curl of H against sigma E_z, away from the wire",
               curl_z[ring], sigma_wire*E_wire(rho_w, t_c)[ring], rtol=0.05,
               hint="Ampere with no source: d_x H_y - d_y H_x = sigma E_z")
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

```{figure} figures/setup_ladder.svg
:name: fig-lab6-ladder
:width: 95%

The three models of this lab side by side. The source spreads over a plane, a cylinder or a sphere, which is the only thing that changes between them.
```

### Task 5 — the ladder

Write $G$. Your `t_peak` already covers it: the three geometries differ only in $p$, so at the same distance their peak times are in a fixed ratio. **Predict** that ratio before you run the last figure. Then one the formula does not hand you: which of the three records is the broadest on a logarithmic time axis, and which has the slowest tail? Say why before you look.

```{code-cell} ipython3
sigma_pt = 0.01                                             # sediments [S/m]

# Task 5 -- one blank.
def G_point(R, t, s=sigma_pt):
    """eq:G3D -- the impulse response in three dimensions [1/(m s)]."""
    return ___

# --- given: a rotatable view of the field at one instant -------------------
# The box is sized from the field, so changing t_show rescales both together:
# the shell keeps its size on screen and the axis numbers change instead.
t_show = 1.0e-3                                             # [s]
D_show = np.sqrt(4*t_show / (sigma_pt*mu))                  # how far it has spread [m]
g_xy = np.linspace(-1.8*D_show, 1.8*D_show, 32)             # the box follows the field
g_z = np.linspace(0.0, 1.8*D_show, 32)                      # depth [m]
GX, GY, GZ = np.meshgrid(g_xy, g_xy, g_z, indexing="ij")
G_vol = G_point(np.sqrt(GX**2 + GY**2 + GZ**2), t_show)
fw.show_isosurface(g_xy, g_xy, g_z, G_vol, levels=(0.08, 0.25, 0.6), opacity=0.32,
                   c_label="G", z_label="depth z [m]",
                   title=f"The point source at t = {t_show*1e3:g} ms. Drag to rotate")

# --- given: the three geometries at the same distance, same ground ---------
r0 = 300.0                                                  # [m]
t_l = np.logspace(np.log10(t_for_D(r0, sigma_pt)) - 2,
                  np.log10(t_for_D(r0, sigma_pt)) + 2, 4001)                # [s]
ladder = {"sheet,  p = 1/2": np.abs(E_sheet(r0, t_l, sigma_pt)),
          "wire,   p = 1  ": np.abs(E_wire(r0, t_l, sigma_pt)),
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
# integrate out to ten diffusion distances, where the Gaussian has nothing left
_R = np.linspace(1e-3, 10*D_show, 60000)                    # a radial grid [m]
fw.check_scalar("the integral of G over all space, which fixes the constant in front",
                np.sum(G_point(_R, t_show) * 4*np.pi*_R**2) * (_R[1] - _R[0]),
                1.0 / (sigma_pt*mu), rtol=0.01, unit=" m^2/s")
```

:::{admonition} Solution — Task 5
:class: dropdown

```python
def G_point(R, t, s=sigma_pt):
    return np.sqrt(s*mu) / (4*np.pi*t)**1.5 * np.exp(-s*mu*R**2 / (4*t))
```
:::

:::{admonition} The ladder, and why the sphere answers first
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

```{figure} figures/setup_loop.svg
:name: fig-lab6-loop
:width: 88%

The model of this part, and the two planes you will cut through it. The current runs clockwise from vertex 1 to vertex 4, seen from above with $z$ pointing down.
```

### Task 6 — the loop forgets its shape

Fill in the brace of $E_y$. Each of the three figures that follow then asks you one question, posed just above it.

Integrating the point response along the four sides leaves a Gaussian across each pair of parallel wires and an error function along them. In the vertical plane through the middle of the loop you see the two segments that run along $y$, entering with opposite signs because they carry opposite currents.

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
x_L = np.linspace(-3*Lx, 3*Lx, n_L)                         # three loop widths either way [m]
z_L = np.linspace(0.0, 3*Lx, n_L)
XZ_x, XZ_z = np.meshgrid(x_L, z_L, indexing="ij")
# from when the field has spread a tenth of the loop to when it has spread ten times it
t_L = np.logspace(np.log10(t_for_D(Lx/10, sigma_loop)),
                  np.log10(t_for_D(Lx*10, sigma_loop)), 16)                 # [s]

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

The diffusion distance $D=\sqrt{4t/\sigma\mu}$ is the only length the field itself carries. Holding it against $L_x$ is what decides whether the pattern still remembers the shape of its source.

**Question 1.** Drag the slider, which carries $D$. At which $D$ does the square stop looking square? Compare it with $L_x$.

```{code-cell} ipython3
# --- given: the plane at 10 m depth, seen from above. Arrows give direction ---
z_xy = 10.0                                                 # the depth of this slice [m]
# its own narrower grid: the question is about the shape of the loop, and at
# three loop widths either way the square is only a dozen pixels across
x_xy = np.linspace(-1.5*Lx, 1.5*Lx, n_L)                    # [m]
XY_x, XY_y = np.meshgrid(x_xy, x_xy, indexing="ij")
EE = [E_loop(XY_x, XY_y, z_xy, tv) for tv in t_L]
mag = np.array([np.hypot(ex, ey) for ex, ey in EE])
# the slider carries D, not t, because the question is about D against Lx
fw.show_map(x_xy, x_xy, mag, D_of(t_L),
            arrows=(np.array([e[0] for e in EE]), np.array([e[1] for e in EE])),
            arrow_every=10, log_c=True, per_frame_scale=True, y_down=True,
            value_name="D", value_fmt="{:.0f}", unit=f" m  (Lx = {Lx:g} m)",
            x_label="x [m]", y_label="y [m]", c_label="log<sub>10</sub>(|E| / max)",
            title=f"At z = {z_xy:g} m, seen from above")

print(f"{'t [ms]':>9}{'D [m]':>9}{'D / Lx':>9}")
for tv in t_L[::3]:
    print(f"{tv*1e3:>9.3g}{D_of(tv):>9.1f}{D_of(tv)/Lx:>9.2f}")
```

Now time is held fixed and depth is stepped instead, with one colour scale shared by every frame so they can be compared directly.

**Question 2.** Before you run it, write down with a neighbour what each of you expects to change as $z$ grows: the brightness, the width of the pattern, the direction of the arrows, or the position of the maximum. You will disagree about at least one of those. Run the cell, then settle it from {eq}`eq:Eyloop` rather than from the picture.

```{code-cell} ipython3
# --- given: the same instant, at a depth you choose -------------------------
t_fix = 3e-4                                                # [s]
# depths spaced against the diffusion distance, so the frames always span the drop
# and stay inside the colour floor of 1e-4 that show_map clips at
z_try = np.round(D_of(t_fix) * np.array([0.0, 0.6, 1.2, 1.8, 2.4]))         # depth [m]
deep = np.array([np.hypot(*E_loop(XY_x, XY_y, zv, t_fix)) for zv in z_try])
fw.show_map(x_xy, x_xy, deep, z_try, value_name="z", value_fmt="{:.0f}", unit=" m",
            log_c=True, per_frame_scale=False, y_down=True,
            x_label="x [m]", y_label="y [m]", c_label="log<sub>10</sub>(|E| / max)",
            title=f"The same instant, t = {t_fix*1e3:g} ms, at {len(z_try)} depths")

print(f"at t = {t_fix*1e3:g} ms the diffusion distance is D = {D_of(t_fix):.0f} m\n")
print(f"{'depth [m]':>11}{'|E| / its surface value':>26}")
for zv in z_try:
    f = np.exp(-zv**2 / D_of(t_fix)**2)
    print(f"{zv:>11.0f}{f:>26.4f}")
```

Nested surfaces of constant $|\boldsymbol E|$ on a cube around the loop, so the interior stays visible. The box is sized from $D$ and keeps framing the field at whatever instant you set.

**Question 3.** Rotate it, then set `t_3d = 3e-4` and run again. What has happened to the loop relative to the field it is driving?

```{code-cell} ipython3
# --- given: the loop in three dimensions. Drag to rotate --------------------
t_3d = 3e-5                                                 # [s]
# wide enough for the loop, and for the field once it has spread past it
half3 = max(1.8*Lx/2, 1.5*D_of(t_3d))                       # [m]
g3 = np.linspace(-half3, half3, 36)
gz3 = np.linspace(0.0, half3, 36)                           # depth [m]
L3x, L3y, L3z = np.meshgrid(g3, g3, gz3, indexing="ij")
E3x, E3y = E_loop(L3x, L3y, L3z, t_3d)
loop_wire = ([-Lx/2, Lx/2, Lx/2, -Lx/2, -Lx/2],
             [-Ly/2, -Ly/2, Ly/2, Ly/2, -Ly/2], [0, 0, 0, 0, 0])
fw.show_isosurface(g3, g3, gz3, np.hypot(E3x, E3y), levels=(0.06, 0.18, 0.45), opacity=0.3,
                   wire=loop_wire, wire_name="the loop", c_label="|E| [V/m]",
                   z_label="depth z [m]",
                   title=f"t = {t_3d*1e3:g} ms:  D = {D_of(t_3d):.0f} m,  "
                         f"D / Lx = {D_of(t_3d)/Lx:.2f}")

fw.check("the field opposes the source current over the x = +Lx/2 wire",
         E_loop(Lx/2, 0.0, z_xy, t_3d)[1] < 0 < E_loop(-Lx/2, 0.0, z_xy, t_3d)[1],
         "the current there runs in +y, so an opposing field has E_y < 0")
# A square loop is unchanged by exchanging x and y, and the circulation reverses
# under that exchange, so E_y(x, y) = -E_x(y, x). This catches an erf bracket left
# running over the wrong coordinate, which the sign check above does not.
_q = np.array([-1.6, -0.4, 0.0, 0.7, 2.4]) * Lx
_QX, _QY = np.meshgrid(_q, _q, indexing="ij")
fw.check_close("E_y(x, y) against -E_x(y, x), which a square loop must satisfy",
               Ey_loop(_QX, _QY, z_xy, t_3d), -Ex_loop(_QY, _QX, z_xy, t_3d), rtol=1e-9,
               hint="the erf bracket of E_y must run over y, as its exponentials run over x")
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

:::{admonition} What time does to the pattern, and what depth does
:class: important dropdown

**The square survives while $D$ is small.** At $t=0.01$ ms, $D=10$ m against a 100 m loop and the four wires are separate bright lines. By $t=0.1$ ms, $D=33$ m, and the pattern is already round. The loop stops looking square at about $D\approx L_x/3$, which is $t\approx\sigma\mu L_x^2/36$, here 0.1 ms. After that no measurement can tell this loop from a round one of the same area. A source forgets its shape once the field has diffused further than the source is big, and this is the same blurring that merged two Gaussians in the last lab.

**Depth only dims it.** Put $z$ into {eq}`eq:Eyloop` and the depth appears as $\exp[-(x_m^2+z^2)/D^2]$, which factors into $\exp(-z^2/D^2)$ times the surface expression, identically for both components. So

$$ \boldsymbol E(x,y,z,t) = \exp\left(-\frac{z^2}{D^2}\right)\boldsymbol E(x,y,0,t). $$

Going deeper multiplies the whole picture by one number. It does not blur it, does not rotate it, does not change which way the arrows point. The frames of the depth figure are the same image at different brightnesses, and the printed column is that one factor.

That factor is the whole of depth sounding. At $t=0.3$ ms, $D=56$ m, so 50 m down you still have 46% of the surface field and 200 m down you have $3.5\times10^{-6}$ of it. You can only see about as deep as $D$, and $D$ grows as $\sqrt t$. To look twice as deep you must wait four times as long, which is Part 1's $t_p\propto z^2$ arriving from the other direction.

**The arrows oppose the current.** Over the wire at $x=+L_x/2$ the current runs in $+\hat{\boldsymbol y}$ and $E_y$ is negative. The switched-on current drives a field that opposes it, which is Lenz's law seen in a conductor.
:::

---

## Part 5 — Designing a sounding

You now have everything a time-domain electromagnetic survey rests on. This part asks you to put it together. Answer the four questions first, from the formulas and not from a new calculation, then run the cell.

1. A target lies 400 m down in ground of conductivity $10^{-2}$ S/m. Roughly when does the response from that depth arrive? Which $p$ did you put into `t_peak`, and does the choice matter at the factor-of-two level?
2. Your recording window is 20 µs to 10 ms. Which of the three grounds of Part 1 puts a 400 m target inside that window?
3. You have two loops, 50 m and 400 m on a side. The target is 400 m down. Which do you choose, and what decides it: the loop size, or the time you record for?
4. The field at the target is $\exp(-z^2/D^2)$ of its surface value. Below which amplitude would you say the target is not being illuminated at all, and what does that make the deepest usable depth?

Question 3 is the one worth arguing about, because the intuitive answer is wrong and nothing on the page has told you otherwise yet. Commit to a loop before you run the second cell, which measures both.

Everything here is $\exp(-z^2/D^2)$ at the target depth, with $D$ built from each ground's conductivity, against time. A target is worth looking for where that curve is still high inside the window you can actually record in.

```{code-cell} ipython3
# --- given: the window, the ground and the depth, all on one picture -------
z_target = 400.0                                            # [m]
t_win = (2e-5, 1e-2)                                        # the recording window [s]
_tp_t = [t_peak(z_target, 0.5, sv) for sv in media.values()]
t_d = np.logspace(min(np.log10(min(_tp_t)), np.log10(t_win[0])) - 2,
                  max(np.log10(max(_tp_t)), np.log10(t_win[1])) + 2, 2001)

fig, ax = plt.subplots(figsize=(8.2, 3.6))
for k, (name, sv) in enumerate(media.items()):
    ax.plot(t_d, np.exp(-z_target**2 * sv * mu / (4*t_d)), color=f"C{k}", lw=2, label=name)
    ax.axvline(t_peak(z_target, 0.5, sv), color=f"C{k}", ls=":", lw=1.2)
ax.axvspan(*t_win, color="0.85", zorder=0, label="recording window")
ax.axhline(1/np.e, color="k", lw=0.8, ls="--")
ax.text(0.01, 1/np.e + 0.02, "z = D", fontsize=8, transform=ax.get_yaxis_transform())
ax.set_xscale("log"); ax.set_xlabel("t [s]")
ax.set_ylabel(f"illumination at {z_target:.0f} m,  exp(-z²/D²)")
ax.set_title(f"Which ground puts a {z_target:.0f} m target inside the window?")
ax.grid(alpha=0.3); ax.legend(fontsize=8, loc="upper left")
plt.show()

print(f"a target at {z_target:.0f} m, window {t_win[0]*1e6:.0f} us to {t_win[1]*1e3:.0f} ms\n")
print(f"{'ground':<30}{'t_p [s]':>11}{'in window?':>12}"
      f"{f'illum. at {t_win[1]*1e3:g} ms':>18}")
for name, sv in media.items():
    tp = t_peak(z_target, 0.5, sv)
    lit = np.exp(-z_target**2 * sv * mu / (4*t_win[1]))
    print(f"{name:<30}{tp:>11.3g}{'yes' if t_win[0] < tp < t_win[1] else 'no':>12}{lit:>18.3g}")
```

Now the loop itself, the one you built in Part 4, at two sizes. Both are placed over the same target in the same ground, so the only thing different is the side length.

```{code-cell} ipython3
# --- given: a 50 m loop and a 400 m loop over the same target --------------
_t_scan = np.logspace(-5, -1, 400)                          # [s]
_Lx0, _Ly0 = Lx, Ly                                         # keep your Part 4 loop
for _L in (50.0, 400.0):
    Lx = Ly = _L                                            # E_loop reads these
    _E = np.array([np.hypot(*E_loop(100.0, 0.0, z_target, tv, s=0.01)) for tv in _t_scan])
    print(f"L = {_L:3.0f} m:  peak |E| = {_E.max():.2e} V/m  at t = {_t_scan[_E.argmax()]*1e3:5.2f} ms,"
          f"  D there = {np.sqrt(4*_t_scan[_E.argmax()]/(0.01*mu)):.0f} m")
Lx, Ly = _Lx0, _Ly0

print(f"\nthe loop's own arrival, t_p with p = 5/2 at R = sqrt(100^2 + {z_target:.0f}^2):"
      f" {t_peak(np.hypot(100.0, z_target), 2.5, 0.01)*1e3:.2f} ms")
```

:::{admonition} Answers
:class: dropdown

**1.** $t_p=\sigma\mu z^2/4p$. The sheet's $p=1/2$ gives 1.0 ms, the wire 0.50 ms, the point source 0.34 ms, and the loop's $p=5/2$ gives 0.20 ms. A survey uses a loop, so 0.2 ms is the honest number, but any of them sets the scale: the spread is a factor of five across geometries that differ completely. What matters is $t\sim\sigma\mu z^2$, not the number in the denominator.

**2.** Sediments, at 1.0 ms, sit comfortably inside, and the printed table says so. Seawater peaks at 0.40 s, forty times beyond the end of the window: the window closes long before the response from 400 m arrives. Basement peaks at 10 µs, which is before the window opens, so its response from 400 m is already over by the time the first sample is taken. Only the middle ground is workable, and that is typical.

**3.** The time you record for. Depth of investigation is set by $D=\sqrt{4t/\sigma\mu}$, which contains no loop size at all, and the cell shows it: both loops peak at the same instant, and the diffusion distance there is the same. What the 400 m loop buys is amplitude, a factor of about 60 at the target, which decides whether you can detect the response rather than how deep it comes from. A bigger loop is worth having for exactly that reason, and for no other. You buy depth with late time and a quiet receiver.

**4.** Any threshold in the range 1% to 10% gives nearly the same rule, because the Gaussian is so steep. Taking $1/e$ gives $z_{\max}=D=\sqrt{4t/\sigma\mu}$ exactly, which is the standard definition of the diffusion depth. Read the two ends of the window off the printed column. At the 1.0 ms peak in sediments $D=564$ m, so the 400 m target sits at $\exp(-0.50)=0.60$ of the surface field; by the 10 ms end of the window $D$ has grown to 1784 m and the target is at 0.95, which is what the table prints. In seawater 10 ms gives only $D=89$ m and the target is at $2\times10^{-9}$, which is nothing at all. Illumination is not what limits you in sediments; signal strength is.
:::

:::{admonition} What this lab was about
:class: important dropdown

One kernel, $\exp(-\sigma\mu r^2/4t)$, appeared in every part. It came from the heat equation last week with $\kappa$ replaced by $1/(\sigma\mu)$, and the only thing that changed from a sheet to a wire to a point was the power of $t$ in front, which is a statement about geometry and not about electromagnetism.

From that one kernel came three results a geophysicist uses directly. Arrival time measures distance, $t_p=\sigma\mu r^2/4p$. Depth of investigation is the diffusion distance, $z\approx D=\sqrt{4t/\sigma\mu}$, and it is bought with time rather than with equipment. And a source is blurred into a point once $D$ exceeds its size, which is why the shape of a transmitter stops mattering, and also why deep structure is always seen blurred.

The magnetic field made the fourth point. For as long as the electric field is there, $(\nabla\times\boldsymbol H)_z=\sigma E_z$ is not zero, and the magnetic field is not a potential field. It becomes one only in the limit, which is where the magnetostatics of the earlier chapters lives.
:::
