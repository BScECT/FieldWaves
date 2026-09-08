# Potential Energy and Work

The electric field is conservative in electrostatics. The potential difference between two positions is therefore

$$
\boxed{
V(\vec r)-V(\vec r_0)
=-\int_{\vec r_0}^{\vec r}\vec E\cdot\mathrm d\vec s.
}
$$ (eq:electric-potential-difference)

This is the electrical counterpart of Equation {eq}`eq:gravity-potential-difference`. The line integral measures the work done by the field per unit positive test charge, with the sign reversed.

## Potential belongs to the field configuration

Electric potential has units

$$
1\ \mathrm V=1\ \mathrm{J\,C^{-1}}.
$$

It describes the source configuration and the chosen zero of potential. It does not depend on which test charge we later place at the observation point.

The electric potential energy of a test charge $q$ is

$$
\boxed{U=qV.}
$$ (eq:electric-potential-energy)

Consequently,

$$
\Delta U=q\,\Delta V,
\qquad
W_{\mathrm{field}}=-\Delta U=-q\,\Delta V.
$$ (eq:electric-work-energy)

This parallels gravitational potential energy,

$$
U_g=m\Phi,
\qquad
U_e=qV.
$$

The difference is that ordinary mass $m$ is positive, whereas $q$ can have either sign.

## Reading the signs

The electric field always points in the direction of decreasing electric potential because $\vec E=-\vec\nabla V$. A positive charge experiences a force along $\vec E$ and therefore tends to move toward lower $V$. A negative charge experiences a force opposite to $\vec E$ and tends to move toward higher $V$.

There is no contradiction: for a negative charge, increasing $V$ makes $U=qV$ more negative. Both signs of charge move spontaneously toward lower potential **energy**, even though they move in opposite directions relative to the electric potential.

Along an equipotential surface, $\Delta V=0$. The electric field is perpendicular to that surface and does no work on a charge displaced along it. This is the same geometrical relation developed in {doc}`../introduction/potential`.

```{admonition} Interpret before answering
:class: exercise

1. An electron moves spontaneously toward a region of higher $V$. Does its potential energy increase or decrease?
2. Two paths connect the same endpoints in a static electric field. What can you say about the work along the two paths?
3. If $V=0$ at one point, does a charge at that point necessarily have zero force?
4. If a charge moves along an equipotential, what are $\Delta V$, $\Delta U$, and the work done by the electric field?
```
