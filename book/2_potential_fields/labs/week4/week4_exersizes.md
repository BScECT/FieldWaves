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

# Exercises Week 4

## Explore a spherical capacitor

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
