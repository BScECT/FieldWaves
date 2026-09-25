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

# Lab 4: Electrostatic and Magnetic Fields

## 1. Explore a spherical capacitor

Two concentric conducting shells with free space between them, an **inner shell** of radius $R_E=6370\ \text{km}$ (the Earth) held at $V=0$, and an **outer shell** of radius $R_I$ (the ionosphere) held at $V=V_o$, is the same setup as the Earth-ionosphere model in the {doc}`week 4 quiz <week4_quiz>`. Between the shells, the potential takes the form

```{math}
V(r) = A + \frac{B}{r}, \qquad R_E \le r \le R_I,
```

with $A$ and $B$ fixed entirely by the two boundary conditions $V(R_E)=0$ and $V(R_I)=V_o$. Inside the inner shell $V=0$ (it is a conductor), and outside the outer shell $V=V_o$ with $\vec E = 0$ (the shells enclose zero net charge together).

Use the sliders below to change the outer radius $R_I$ (km) and the outer voltage $V_o$ (kV, 0 to 200), and watch $V(r)$ and $E(r)=-dV/dr$ update. **The radial axis in the plots is not to scale**: the gap between the shells (tens to thousands of km) is stretched for readability against Earth's 6370 km radius.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import numpy as np

def solve_coefficients(r_inner, r_outer, v_outer):
    """Solve A, B given V(r_inner) = 0 and V(r_outer) = v_outer."""
    b = v_outer / (1.0 / r_outer - 1.0 / r_inner)
    a = -b / r_inner
    return a, b

def potential(r, r_inner, r_outer, v_outer):
    a, b = solve_coefficients(r_inner, r_outer, v_outer)
    r = np.asarray(r, float)
    v = np.full_like(r, v_outer, dtype=float)
    between = (r >= r_inner) & (r <= r_outer)
    v[between] = a + b / r[between]
    v[r < r_inner] = 0.0
    return v

def field(r, r_inner, r_outer, v_outer):
    """E(r) = -dV/dr = B / r**2 between the shells, else zero."""
    _, b = solve_coefficients(r_inner, r_outer, v_outer)
    r = np.asarray(r, float)
    e = np.zeros_like(r, dtype=float)
    between = (r >= r_inner) & (r <= r_outer)
    e[between] = b / r[between] ** 2
    return e

# Boundary conditions and the field-potential relation, checked at an example (r_i, r_o, V_o).
r_i, r_o, v_o = 6370.0, 6470.0, 1.0e5
np.testing.assert_allclose(potential(r_i, r_i, r_o, v_o), 0.0, atol=1e-9)
np.testing.assert_allclose(potential(r_o, r_i, r_o, v_o), v_o)
r_mid = 0.5 * (r_i + r_o)
eps = 1e-3
numeric_e = -(potential(r_mid + eps, r_i, r_o, v_o) - potential(r_mid - eps, r_i, r_o, v_o)) / (2 * eps)
np.testing.assert_allclose(numeric_e, field(r_mid, r_i, r_o, v_o), rtol=1e-6)
print("Boundary conditions and E = -dV/dr checks passed.")
```

```{code-cell} ipython3
:tags: [remove-input]

# The HTML contains all controls and drawing code, with no external dependencies.
# An iframe keeps the explorer independent of the page styles.
import html as html_module
from pathlib import Path
from IPython.display import display

for _candidate in (
    Path("spherical_capacitor_lab.html"),
    Path("book/2_potential_fields/labs/week4/spherical_capacitor_lab.html"),
):
    if _candidate.exists():
        explorer_html = _candidate.read_text()
        break
else:
    from pyodide.http import pyfetch
    _r = await pyfetch("spherical_capacitor_lab.html")
    explorer_html = (await _r.bytes()).decode()

display({"text/html": '<iframe title="Interactive spherical capacitor explorer" '
             'style="width:100%;height:680px;border:0" '
             'sandbox="allow-scripts" srcdoc="' + html_module.escape(explorer_html, quote=True)
             + '"></iframe>'}, raw=True)
```

### Explore, predict, explain

1. **Reproduce the quiz numbers.** Set $R_I = 6470$ km (100 km altitude) and $V_o = 100$ kV, matching the week 4 quiz. Read off $A$ and $B$, and compare them to the closed-form expressions you derived by hand. Then check the field at 50 km altitude (probe $r=6420$ km) against your answer to part (e).
2. **Move the outer shell farther away.** Keep $V_o$ fixed and increase $R_I$. Does $|B|$ grow or shrink? Explain why the field between the shells changes even though $V_o$ has not.
3. **Increase $V_o$ toward 200 kV.** What happens to the field magnitude at a fixed altitude? Is the relationship linear?
4. **Move the probe outside $R_I$ and inside $R_E$.** Confirm that $V$ is constant and $E=0$ in both regions, consistent with each shell being an equipotential conductor.

## 2. Charges in the fair-weather field

On a clear day, the air above flat, open ground carries a downward electric field (W4L1, slides 16–17):
```{math}
\vec{E} \approx -E_0\,\hat{z}, \qquad E_0 \approx 100\ \mathrm{V/m}, \qquad V(z) = E_0 z \quad \text{with } V(0) = 0.
```
Cosmic rays continuously ionise the air, producing free electrons and positive ions such as $\mathrm{N_2^+}$. Wind also lifts charged mineral dust from deserts into the atmosphere. Use $e = 1.602\cdot 10^{-19}\ \mathrm{C}$, $g = 9.81\ \mathrm{m/s^2}$ and $1\ \mathrm{eV} = 1.602\cdot 10^{-19}\ \mathrm{J}$ (the energy an elementary charge gains across $1\ \mathrm{V}$).
 
Parts (a)–(d) of this exercise are question 2 of the {doc}`week 4 quiz <week4_quiz>`. Work through them first; the Python cell and the explorer below let you check those answers and extend them to part (e).
 
(e) In the undisturbed fair-weather field, the potential difference between $z=0$ and $z=2\ \mathrm{m}$ is $200\ \mathrm{V}$ (quiz part (a)). You are standing on the ground and are about $2\ \mathrm{m}$ tall. Is there a $200\ \mathrm{V}$ potential difference between your head and your feet? Sketch how the equipotentials change around you and explain your reasoning. *Hint:* you are a conductor connected to the ground (W4L1, slide 14).
 
### Check your answers with Python
 
Fill in the blanks (`___`) and run the cell to check your numbers for parts (a), (b) and (d) of the quiz.
 
```{code-cell} ipython3
:tags: [skip-execution]

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
The upper panel shows the field strength $|\vec{E}|/E_0$ in colour, the equipotentials in white (every $E_0\cdot 1\ \mathrm{m}$), the field lines in grey, and the force $\vec{F} = q\vec{E}$ on the test charge as an arrow. The lower panel shows $V(z)$ and $U(z)/e$ along the vertical line through the test charge.
 
1. With $a = 0$, move the test charge up and down. Check your answers to quiz parts (a) and (b).
2. Switch between the electron and the ion. Which quantities change, and which stay the same? (W4L1, slide 9)
3. Set $a = 1\ \mathrm{m}$. Where do the equipotentials crowd together? Read $|\vec{E}|$ just above the top of the object and near its base. Use this to check your sketch for (e).

```{code-cell} ipython3
:tags: [remove-input]

# The HTML contains all controls and drawing code, with no external dependencies.
# An iframe keeps the explorer independent of the page styles.
import html as html_module
from pathlib import Path
from IPython.display import display

for _candidate in (
    Path("fair_weather_lab.html"),
    Path("book/2_potential_fields/labs/week4/fair_weather_lab.html"),
):
    if _candidate.exists():
        explorer_html = _candidate.read_text()
        break
else:
    from pyodide.http import pyfetch
    _r = await pyfetch("fair_weather_lab.html")
    explorer_html = (await _r.bytes()).decode()

display({"text/html": '<iframe title="Interactive fair-weather field explorer" '
             'style="width:100%;height:820px;border:0" '
             'sandbox="allow-scripts" srcdoc="' + html_module.escape(explorer_html, quote=True)
             + '"></iframe>'}, raw=True)
```
