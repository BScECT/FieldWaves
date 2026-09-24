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
---
# Lab 4: Electrostatic and Magnetic Fields (Solutions)
## 1. Warm-up: charges in the fair-weather field
 
On a clear day, the air above flat, open ground carries a downward electric field (W4L1, slides 16–17):
```{math}
\vec{E} \approx -E_0\,\hat{z}, \qquad E_0 \approx 100\ \mathrm{V/m}, \qquad V(z) = E_0 z \quad \text{with } V(0) = 0.
```
Cosmic rays continuously ionise the air, producing free electrons and positive ions such as $\mathrm{N_2^+}$. Wind also lifts charged mineral dust from deserts into the atmosphere. Use $e = 1.602\cdot 10^{-19}\ \mathrm{C}$, $g = 9.81\ \mathrm{m/s^2}$ and $1\ \mathrm{eV} = 1.602\cdot 10^{-19}\ \mathrm{J}$ (the energy an elementary charge gains across $1\ \mathrm{V}$).
 
(a) Sketch the equipotentials and field lines for $0 \leq z \leq 10\ \mathrm{m}$. What is the potential at $z = 2\ \mathrm{m}$?
 
(b) An electron ($q=-e$) and an $\mathrm{N_2^+}$ ion ($q=+e$) are each moved from the ground to $z = 10\ \mathrm{m}$. For each, find $\Delta V$, $\Delta U$ (in J and in eV) and the work done by the field, $W_\mathrm{field}$.
 
(c) Both particles are released from rest. Which one accelerates upward? In which direction does the resulting electric current flow?
 
(d) A Saharan dust grain (radius $1\ \mu\mathrm{m}$, density $2650\ \mathrm{kg/m^3}$) carries a negative charge. How many excess electrons does it need for the electric force to balance gravity? Does the answer depend on its height in this model?
 
(e) You are standing on the ground and are about $2\ \mathrm{m}$ tall. Is there a $200\ \mathrm{V}$ potential difference between your head and your feet? Sketch how the equipotentials change around you. *Hint:* you are a conductor connected to the ground (W4L1, slide 14).
 
**(a)** The equipotentials are horizontal planes spaced evenly: every metre up adds $100\ \mathrm{V}$. The field lines are vertical, point downward and are equally spaced, so the field is uniform. At head height,
```{math}
V(2\ \mathrm{m}) = E_0 z = (100)(2) = \boxed{200\ \mathrm{V}}.
```
The potential increases upward, while $\vec{E}$ points down, from high to low potential.
 
**(b)** The potential difference does not depend on the test charge:
```{math}
\Delta V = V(10\ \mathrm{m}) - V(0) = \boxed{1000\ \mathrm{V}}.
```
Using $\Delta U = q\Delta V$ and $W_\mathrm{field} = -\Delta U$ (W4L1, slide 13):
 
| | $q$ | $\Delta U$ | $W_\mathrm{field}$ |
|---|---|---|---|
| electron | $-e$ | $-1.60\cdot 10^{-16}\ \mathrm{J} = -1000\ \mathrm{eV}$ | $+1.60\cdot 10^{-16}\ \mathrm{J}$ |
| $\mathrm{N_2^+}$ ion | $+e$ | $+1.60\cdot 10^{-16}\ \mathrm{J} = +1000\ \mathrm{eV}$ | $-1.60\cdot 10^{-16}\ \mathrm{J}$ |
 
Moving up the electron *loses* potential energy, because the field does positive work on it. The ion *gains* potential energy, because the field works against the motion. Same $\Delta V$, opposite energies.
 
**(c)** The force is $\vec{F} = q\vec{E} = q(-E_0\hat{z})$.
- Electron: $\vec{F} = (-e)(-E_0\hat{z}) = +eE_0\hat{z} = +1.6\cdot 10^{-17}\ \mathrm{N}\,\hat{z}$. It **accelerates upward**, toward lower potential energy.
- Ion: $\vec{F} = -eE_0\hat{z}$. It accelerates downward.
Positive charge moving down and negative charge moving up both give a **downward** current. This is the small fair-weather current of the global atmospheric electrical circuit, which flows downward through fair-weather regions because air is a poor, but not perfect, insulator. Thunderstorms help maintain the potential difference between the upper atmosphere and the ground that drives it (W4L1, slide 16).
 
**(d)** The mass of the grain is
```{math}
m = \tfrac{4}{3}\pi a^3 \rho = \tfrac{4}{3}\pi (10^{-6})^3 (2650) = 1.11\cdot 10^{-14}\ \mathrm{kg}.
```
A negative charge feels an upward force (see (c)), so it can balance gravity when $|q|E_0 = mg$:
```{math}
|q| = \frac{mg}{E_0} = \frac{(1.11\cdot 10^{-14})(9.81)}{100} = 1.09\cdot 10^{-15}\ \mathrm{C},
\qquad N = \frac{|q|}{e} \approx \boxed{6.8\cdot 10^{3}\ \text{electrons}}.
```
In this model, $\vec{E}$ is uniform, so the answer **does not depend on height**. The linear potential is only valid near the ground (W4L1, slide 17). In real dust storms, the field near the ground can be much stronger than $E_0$, so far less charge is needed.
 
**(e)** No. Your body is a conductor connected to the ground, so in electrostatic equilibrium it is an equipotential with $V = 0$ (W4L1, slides 14–15). Charge redistributes (negative charge gathers near your head) until the field inside you vanishes. That is why you feel nothing.
 
The equipotentials that would have crossed your body are pushed up and over it. They crowd together above your head and spread apart near your feet. The field is therefore **stronger above you** and weaker close to your feet. For the grounded hemisphere in the explorer, the field at the top is
```{math}
\vec{E}(0,0,a) = -E_0\left[1 - 1 + 3\right]\hat{z} = -3E_0\,\hat{z},
```
three times the fair-weather value, whatever the size of the object. With the outward normal $\hat{z}$ at the top and $E_{\perp,\mathrm{outside}}=\sigma_q/\epsilon_0$ (W4L1, slide 15), the induced surface charge there is
```{math}
\sigma_q = \epsilon_0 E_{\perp,\mathrm{outside}} = -3\epsilon_0E_0 \approx -2.7\cdot 10^{-9}\ \mathrm{C/m^2},
```
three times the fair-weather ground value $\sigma_q=-\epsilon_0E_0\approx-8.9\cdot 10^{-10}\ \mathrm{C/m^2}$. The same effect concentrates the field on trees, masts and mountain tops. It is why lightning rods are placed on the highest point, and why St Elmo's fire glows at mast tips during thunderstorms.
 
The potential of the hemisphere is the uniform field plus a dipole term $-E_0 a^3 z/r^3$. The hemisphere and its mirror image below the ground together form a full sphere, which is the same kind of dipole construction as the image charge in W4L1, slide 24.
 
### Python check
 
```{code-cell} ipython3
import numpy as np
 
e  = 1.602e-19     # elementary charge [C]
E0 = 100.0         # fair-weather field strength [V/m]
g  = 9.81          # gravitational acceleration [m/s^2]
 
def V_fair(z):
    """Fair-weather potential above flat ground, V(0) = 0."""
    return E0 * z
 
# (b), (c): move each particle from z = 0 to z = 10 m
dV = V_fair(10.0) - V_fair(0.0)
for name, q in [("electron", -e), ("N2+ ion ", +e)]:
    dU = q * dV              # change in potential energy [J]
    W  = -dU                 # work done by the field [J]
    Fz = q * (-E0)           # z-component of F = qE, with E = -E0 z_hat [N]
    print(f"{name}: dV = {dV:.0f} V, dU = {dU:+.2e} J = {dU/e:+.0f} eV, "
          f"W_field = {W:+.2e} J, F_z = {Fz:+.1e} N")
 
# (d): dust grain levitated by the fair-weather field
a_d, rho_d = 1e-6, 2650.0    # radius [m], density [kg/m^3]
m_d = 4/3 * np.pi * a_d**3 * rho_d
q_d = m_d * g / E0
print(f"m = {m_d:.2e} kg, |q| = {q_d:.2e} C = {q_d/e:.0f} excess electrons")
 
# self-check
assert np.isclose(V_fair(2.0), 200.0), "V(2 m) should be 200 V"
assert np.isclose(q_d / e, 6.8e3, rtol=0.02), "check the mass or the force balance"
print("Self-check passed.")
```
 
The explorer below shows the fair-weather field over flat ground. You can add a grounded conducting hemisphere of radius $a$, a crude model of a person, a tree or a small hill. Its potential is
```{math}
V(\vec{r}) = E_0 z\left(1 - \frac{a^3}{r^3}\right), \qquad z \geq 0,\ r \geq a.
```
The left panel shows the field strength $|\vec{E}|/E_0$ in colour, the equipotentials in white (every $E_0\cdot 1\ \mathrm{m}$), the field lines in grey, and the force $\vec{F} = q\vec{E}$ on the test charge as an arrow. The right panel shows $V(z)$ and $U(z)/e$ along the vertical line through the test charge.
 
1. With $a = 0$, move the test charge up and down. Check your answers to (a) and (b).
2. Switch between the electron and the ion. Which quantities change, and which stay the same? (W4L1, slide 9)
3. Set $a = 1\ \mathrm{m}$. Where do the equipotentials crowd together? Read $|\vec{E}|$ just above the top of the object and near its base. Use this to check your sketch for (e).
```{code-cell} ipython3
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
 
def fair_weather(x, z, E0, a):
    """Fair-weather field over flat ground with a grounded conducting hemisphere
    of radius a at the origin (a crude person, tree or hill; a = 0: flat ground).
        V = E0 z (1 - a^3/r^3),   z >= 0,  r = sqrt(x^2 + z^2) >= a
    Returns V [V], Ex, Ez [V/m] in the plane y = 0."""
    x, z = np.asarray(x, float), np.asarray(z, float)
    if a == 0:
        return E0 * z, 0 * x, -E0 + 0 * x
    r = np.maximum(np.hypot(x, z), 1e-9)
    k = a**3 / r**3
    V  = E0 * z * (1 - k)
    Ex = -E0 * 3 * a**3 * x * z / r**5
    Ez = -E0 * (1 - k + 3 * a**3 * z**2 / r**5)
    inside = r < a                                   # inside the conductor
    V  = np.where(inside, 0.0, V)
    Ex = np.where(inside, np.nan, Ex)
    Ez = np.where(inside, np.nan, Ez)
    return V, Ex, Ez
 
def explore(E0=100, a=0.0, charge="electron (−e)", x_p=3.0, z_p=4.0):
    sign = -1 if charge.startswith("electron") else +1
    col  = "tab:blue" if sign < 0 else "tab:red"
    x = np.linspace(-8, 8, 321); z = np.linspace(0, 10, 201)
    X, Z = np.meshgrid(x, z)
    V, Ex, Ez = fair_weather(X, Z, E0, a)
 
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(11, 4.6), layout="constrained",
                                  gridspec_kw=dict(width_ratios=(1.7, 1)))
    # left: |E|/E0 in colour, equipotentials in white, field lines in grey
    pc = ax.pcolormesh(X, Z, np.hypot(Ex, Ez) / E0, cmap="magma", vmin=0, vmax=3,
                       shading="auto")
    ax.contour(X, Z, V, levels=np.linspace(0, 10 * E0, 11)[1:], colors="w", linewidths=0.8)
    ax.streamplot(x, z, Ex, Ez, color="0.75", density=1.1, linewidth=0.7, arrowsize=0.8)
    if a > 0:
        t = np.linspace(0, np.pi, 100)
        ax.fill(a * np.cos(t), a * np.sin(t), color="0.35", zorder=3)
    ax.axhline(0, color="k", lw=2)
    fig.colorbar(pc, ax=ax, shrink=0.85, label=r"$|\vec{E}|\,/\,E_0$")
 
    # test charge and its force F = qE (arrow length proportional to |F|)
    Vp, Exp, Ezp = [float(v) for v in fair_weather(x_p, z_p, E0, a)]
    if np.hypot(x_p, z_p) >= a:
        s = 1.2 / E0
        ax.plot(x_p, z_p, "o", ms=10, color=col, mec="k", zorder=5)
        ax.annotate("", xy=(x_p + s * sign * Exp, z_p + s * sign * Ezp), xytext=(x_p, z_p),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=2.5), zorder=6)
        ax.set_title(f"V = {Vp:.0f} V,   U = {sign * Vp:+.0f} eV,   "
                     f"|E| = {np.hypot(Exp, Ezp):.0f} V/m", fontsize=10)
    else:
        ax.set_title("test charge is inside the conductor", fontsize=10)
    ax.set_xlabel("x [m]"); ax.set_ylabel("z [m]")
    ax.set_xlim(-8, 8); ax.set_ylim(-0.3, 10); ax.set_aspect("equal")
 
    # right: V(z) and U(z)/e along the vertical line through the test charge
    zz = np.linspace(0, 10, 400)
    Vz = fair_weather(np.full_like(zz, x_p), zz, E0, a)[0]
    ax2.plot(Vz, zz, "k", lw=2, label="V(z)   [V]")
    ax2.plot(sign * Vz, zz, color=col, lw=2, ls="--",
             label=f"U(z)/e for q = {'−e' if sign < 0 else '+e'}   [eV]")
    ax2.plot([Vp, sign * Vp], [z_p, z_p], "o", color="0.3")
    ax2.axvline(0, color="0.6", lw=0.8)
    ax2.set_xlim(-10.5 * E0, 10.5 * E0); ax2.set_ylim(0, 10)
    ax2.set_xlabel("V [V]   or   U/e [eV]"); ax2.set_ylabel("z [m]")
    ax2.set_title(f"Profile along x = {x_p:.1f} m", fontsize=10)
    ax2.legend(loc="upper left", fontsize=8, frameon=False)
    plt.show()
 
style = {"description_width": "150px"}
widgets.interact(
    explore,
    E0=widgets.FloatSlider(value=100, min=50, max=300, step=10, style=style,
                           description="E₀ [V/m]", continuous_update=False),
    a=widgets.FloatSlider(value=0.0, min=0.0, max=3.0, step=0.25, style=style,
                          description="object radius a [m]", continuous_update=False),
    charge=widgets.ToggleButtons(options=["electron (−e)", "N₂⁺ ion (+e)"],
                                 description="test charge", style=style),
    x_p=widgets.FloatSlider(value=3.0, min=-7.5, max=7.5, step=0.25, style=style,
                            description="charge x [m]", continuous_update=False),
    z_p=widgets.FloatSlider(value=4.0, min=0.25, max=9.75, step=0.25, style=style,
                            description="charge z [m]", continuous_update=False),
);
```
 