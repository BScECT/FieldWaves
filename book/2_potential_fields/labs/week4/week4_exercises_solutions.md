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
## 1. Explore a spherical capacitor

Between the shells the region is free space, so the potential obeys Laplace's equation. With spherical symmetry this reduces to the radial form used in the {doc}`week 4 quiz <week4_quiz>`, whose solution is $V(r) = A + B/r$. The two constants follow from the boundary conditions $V(R_E)=0$ and $V(R_I)=V_o$:
```{math}
\boxed{B = \frac{V_o}{1/R_I - 1/R_E}}, \qquad \boxed{A = -\frac{B}{R_E}},
\qquad
V(r) = V_o\,\frac{1/R_E - 1/r}{1/R_I - 1/R_E}.
```
The field between the shells is radial,
```{math}
\vec{E} = -\vec{\nabla}V = -\frac{\partial V}{\partial r}\hat{r} = \boxed{\frac{B}{r^2}\,\hat{r}}.
```
Because the outer shell is at the higher potential, $B<0$: the field points radially **inward**, i.e. downward at the ground, in agreement with the fair-weather field of Exercise 2.

**1. Reproduce the quiz numbers.** With $R_E = 6370\ \mathrm{km}$, $R_I = 6470\ \mathrm{km}$ and $V_o = 100\ \mathrm{kV}$,
```{math}
\frac{1}{R_I}-\frac{1}{R_E} = \frac{R_E-R_I}{R_I R_E} = -2.427\cdot 10^{-9}\ \mathrm{m^{-1}},
```
```{math}
B = \frac{10^{5}}{-2.427\cdot 10^{-9}} = \boxed{-4.12\cdot 10^{13}\ \mathrm{V\,m}},
\qquad
A = -\frac{B}{R_E} = \boxed{6.47\cdot 10^{6}\ \mathrm{V}},
```
matching parts (b) and (d) of the quiz. At $50\ \mathrm{km}$ altitude, $r = 6420\ \mathrm{km}$:
```{math}
\vec{E} = \frac{B}{r^2}\hat{r} = \frac{-4.12\cdot 10^{13}}{(6.42\cdot 10^6)^2}\hat{r}
= \boxed{-1.00\ \mathrm{V/m}\ \hat{r}},
```
a field of $1.00\ \mathrm{V/m}$ pointing towards the Earth, as in part (e).

```{note}
The explorer reports $B$ in $\mathrm{V\,km}$, because it works with radii in kilometres: it shows $-4.12\cdot 10^{10}\ \mathrm{V\,km}$, which is the same number as $-4.12\cdot 10^{13}\ \mathrm{V\,m}$.
```

**2. Move the outer shell farther away.** Writing the gap as $d = R_I - R_E$,
```{math}
B = \frac{V_o}{1/R_I - 1/R_E} = -\,\frac{V_o R_E R_I}{d},
```
so $|B|$ **shrinks** as $R_I$ grows at fixed $V_o$, and with it the field at any fixed radius. Numerically, at the Earth's surface: $1.02\ \mathrm{V/m}$ for $d = 100\ \mathrm{km}$, $0.52\ \mathrm{V/m}$ for $200\ \mathrm{km}$, $0.12\ \mathrm{V/m}$ for $1000\ \mathrm{km}$. The field is not fixed by $V_o$ alone because the field is the *rate* at which the potential changes with distance, and the same $100\ \mathrm{kV}$ is now spread over a thicker gap. For a thin gap, $d \ll R_E$, the shells are almost parallel plates and
```{math}
|\vec{E}| \approx \frac{V_o}{d} = \frac{10^5\ \mathrm{V}}{10^5\ \mathrm{m}} = 1\ \mathrm{V/m},
```
which is why the answer to question 1 came out so close to $1\ \mathrm{V/m}$. As $R_I\to\infty$ the field does not vanish but tends to that of an isolated charged sphere, $|B| \to V_o R_E$.

**3. Increase $V_o$ toward 200 kV.** Both $A$ and $B$ are proportional to $V_o$, so at every radius
```{math}
|\vec{E}| = \frac{|B|}{r^2} \propto V_o .
```
The relationship is **linear**: doubling $V_o$ from $100$ to $200\ \mathrm{kV}$ doubles the field at $50\ \mathrm{km}$ altitude from $1.00$ to $2.00\ \mathrm{V/m}$. This is a direct consequence of Laplace's equation being linear, so scaling the boundary values scales the whole solution.

**4. Move the probe outside $R_I$ and inside $R_E$.** Outside the outer shell the explorer shows $V = V_o$ and $E = 0$: the two shells carry equal and opposite charges, so any sphere enclosing both contains zero net charge and Gauss's law gives no flux, hence no field. Inside the inner shell $V = 0$ and $E = 0$, as in the interior of any conductor in electrostatic equilibrium. In both regions the potential is constant, consistent with each shell being an equipotential surface: the entire field lives in the gap between them.

```{code-cell} ipython3
import numpy as np

R_E, R_I, V_o = 6370e3, 6470e3, 100e3          # m, m, V

B = V_o / (1 / R_I - 1 / R_E)
A = -B / R_E
r = 6420e3                                      # 50 km altitude
print(f"A = {A:.3e} V,  B = {B:.3e} V m,  E(50 km) = {B / r**2:+.2f} V/m")
print(f"thin-gap estimate V_o/d = {V_o / (R_I - R_E):.2f} V/m")

for R in (6470e3, 6570e3, 7370e3):              # question 2: a thicker gap
    b = V_o / (1 / R - 1 / R_E)
    print(f"  d = {(R - R_E)/1e3:6.0f} km -> |E| at the ground = {abs(b)/R_E**2:.3f} V/m")

# self-check against the quiz
assert np.isclose(B, -4.12e13, rtol=1e-3) and np.isclose(A, 6.47e6, rtol=1e-3)
assert np.isclose(B / r**2, -1.00, atol=5e-3)
print("Matches the quiz values for A, B and E(50 km).")
```

## 2. Charges in the fair-weather field
 
On a clear day, the air above flat, open ground carries a downward electric field (W4L1, slides 16–17):
```{math}
\vec{E} \approx -E_0\,\hat{z}, \qquad E_0 \approx 100\ \mathrm{V/m}, \qquad V(z) = E_0 z \quad \text{with } V(0) = 0.
```
Cosmic rays continuously ionise the air, producing free electrons and positive ions such as $\mathrm{N_2^+}$. Wind also lifts charged mineral dust from deserts into the atmosphere. Use $e = 1.602\cdot 10^{-19}\ \mathrm{C}$, $g = 9.81\ \mathrm{m/s^2}$ and $1\ \mathrm{eV} = 1.602\cdot 10^{-19}\ \mathrm{J}$ (the energy an elementary charge gains across $1\ \mathrm{V}$).
 
Parts (a)–(d) of this exercise are question 2 of the {doc}`week 4 quiz <week4_quiz>`. Work through them first; the Python cell and the explorer below let you check those answers and extend them to part (e).
 
(e) In the undisturbed fair-weather field, the potential difference between $z=0$ and $z=2\ \mathrm{m}$ is $200\ \mathrm{V}$ (quiz part (a)). You are standing on the ground and are about $2\ \mathrm{m}$ tall. Is there a $200\ \mathrm{V}$ potential difference between your head and your feet? Sketch how the equipotentials change around you and explain your reasoning. *Hint:* you are a conductor connected to the ground (W4L1, slide 14).
 
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
 
### Check your answers with Python
 
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
The upper panel shows the field strength $|\vec{E}|/E_0$ in colour, the equipotentials in white (every $E_0\cdot 1\ \mathrm{m}$), the field lines in grey, and the force $\vec{F} = q\vec{E}$ on the test charge as an arrow. The lower panel shows $V(z)$ and $U(z)/e$ along the vertical line through the test charge.
 
1. With $a = 0$, move the test charge up and down. Check your answers to (a) and (b).
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
