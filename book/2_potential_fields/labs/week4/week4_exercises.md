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
  # Workbook page: code cells contain `___` blanks by design, so the page is
  # not executed at build time. Students run it themselves with Live Code.
  execution_mode: 'off'
---
# Lab 4: Electrostatic and Magnetic Fields

## Warm-ups

### 1. Charges in the fair-weather field

On a clear day, the air above flat, open ground carries a downward electric field (W4L1, slides 16–17):
```{math}
\vec{E} \approx -E_0\,\hat{z}, \qquad E_0 \approx 100\ \mathrm{V/m}, \qquad V(z) = E_0 z \quad \text{with } V(0) = 0.
```
Cosmic rays continuously ionise the air, producing free electrons and positive ions such as $\mathrm{N_2^+}$. Wind also lifts charged mineral dust from deserts into the atmosphere. Use $e = 1.602\cdot 10^{-19}\ \mathrm{C}$, $g = 9.81\ \mathrm{m/s^2}$ and $1\ \mathrm{eV} = 1.602\cdot 10^{-19}\ \mathrm{J}$ (the energy an elementary charge gains across $1\ \mathrm{V}$).
 
(a) Sketch the equipotentials and field lines for $0 \leq z \leq 10\ \mathrm{m}$. What is the electric potential $V$ at $z = 2\ \mathrm{m}$, given the reference $V(0) = 0$ ?
 
(b) An electron ($q=-e$) and an $\mathrm{N_2^+}$ ion ($q=+e$) are each moved from the ground to $z = 10\ \mathrm{m}$. For each, find $\Delta V$, $\Delta U$ (in J and in eV) and the work done by the field, $W_\mathrm{field}$.
 
(c) Both particles are released from rest. Which one accelerates upward? In which direction does the resulting current flow?
 
(d) A Saharan dust grain (radius $1\ \mu\mathrm{m}$, density $2650\ \mathrm{kg/m^3}$) carries a negative charge. How many excess electrons does it need for the electric force to balance gravity? Does the answer depend on its height in this model?
 
(e) In the undisturbed fair-weather field, the potential difference between $z=0$ and $z=2\ \mathrm{m}$  is $200\ \mathrm{V}$. Now consider a person standing on the ground, approximated as a conductor connected to the ground. Would there be a $200\ \mathrm{V}$ potential difference between their feet and head? Sketch the equipotentials around the person and explain your reasoning. *Hint:* you are a conductor connected to the ground (W4L1, slide 14).
 
### Check your answers with Python
 
Fill in the blanks (`___`) and run the cell to check your numbers for (a), (b) and (d).
 
```{code-cell} ipython3
import numpy as np
 
e  = 1.602e-19     # elementary charge [C]
E0 = 100.0         # fair-weather field strength [V/m]
g  = 9.81          # gravitational acceleration [m/s^2]
 
def V_fair(z):
    """Fair-weather potential above flat ground, V(0) = 0."""
    return ___
 
# (b), (c): move each particle from z = 0 to z = 10 m
dV = V_fair(10.0) - V_fair(0.0)
for name, q in [("electron", -e), ("N2+ ion ", +e)]:
    dU = ___                 # change in potential energy [J]
    W  = ___                 # work done by the field [J]
    Fz = ___                 # z-component of F = qE, with E = -E0 z_hat [N]
    print(f"{name}: dV = {dV:.0f} V, dU = {dU:+.2e} J = {dU/e:+.0f} eV, "
          f"W_field = {W:+.2e} J, F_z = {Fz:+.1e} N")
 
# (d): dust grain levitated by the fair-weather field
a_d, rho_d = 1e-6, 2650.0    # radius [m], density [kg/m^3]
m_d = ___                    # mass of the grain [kg]
q_d = ___                    # charge magnitude for |qE| = mg [C]
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
 