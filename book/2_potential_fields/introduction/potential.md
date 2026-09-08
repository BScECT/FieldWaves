# Potential and Equipotential Surfaces

Path independence lets us describe a conservative force using a scalar function of position. We now connect that function to **potential energy**, then introduce gravitational **potential**, which is potential energy per unit mass. Keeping those quantities distinct will help us interpret both their units and their signs.

## From work to potential energy

In the previous section we fixed a reference point $P_0$ and defined

$$
W(P_0,P)=\int_{P_0}^{P}\vec F\cdot\mathrm d\vec s.
$$

This is the work done by the force, measured in joules. For a conservative force, define the potential-energy difference by

$$
U(P)-U(P_0)=-W(P_0,P).
$$

Positive work done by the conservative force corresponds to a decrease in potential energy. If this is the only force doing work, that decrease becomes an equal increase in kinetic energy. The minus sign expresses this energy balance.

Because $P_0$ is fixed, taking the gradient with respect to $P$ gives

$$
\vec\nabla U=-\vec\nabla W=-\vec F,
\qquad
\boxed{\vec F=-\vec\nabla U.}
$$

Only differences in $U$ have been specified. We may choose $U(P_0)=0$, in which case $U(P)=-W(P_0,P)$. Adding a constant to $U$ changes neither the work nor the force.

## Gravitational potential: energy per unit mass

A test mass $m$ in a prescribed gravitational field experiences $\vec F=m\vec g$. Its gravitational potential energy scales with $m$. To describe the source field independently of the test mass, define the **gravitational potential**

$$
\Phi=\frac{U}{m},
\qquad U=m\Phi.
$$

Thus $U$ has units of $\mathrm J$, while $\Phi$ has units of $\mathrm{J/kg}$. For a constant test mass, dividing $\vec F=-\vec\nabla U$ by $m$ gives

$$
\boxed{\vec g=-\vec\nabla\Phi.}
$$

The work done by gravity remains

$$
W(P_0,P)=m\int_{P_0}^{P}\vec g\cdot\mathrm d\vec s
=-m\bigl[\Phi(P)-\Phi(P_0)\bigr].
$$

The integral of $\vec g$ alone is **work per unit mass**, not work. Choosing $\Phi(P_0)=0$ gives $W(P_0,P)=-m\Phi(P)$. The minus sign means that the gravitational field points toward the steepest decrease in potential.

For example, near Earth's surface the gravitational potential can be written approximately as

$$
  \Phi(z) = gz,
$$

where $z$ is height, $g>0$ is treated as constant, and we choose zero potential at $z=0$. The gravitational field is then

$$
  \vec{g} = -\vec{\nabla} \Phi = -g\,\hat{z}.
$$

The corresponding force on a mass $m$ is $\vec{F}=-mg\,\hat{z}$, and the gravitational potential energy is $U=mgz$.

As a further example, consider the gravitational field of a point mass $M$ at the origin. We will derive this result later; for now, we postulate that the gravitational potential, choosing zero at infinity, is

$$
  \Phi(\vec{r}) = -\frac{GM}{|\vec{r}|}.
$$ (eq:point-mass-gravitational-potential)

The corresponding gravity field is

$$
  \vec{g}(\vec{r})
  = -\vec{\nabla}\Phi
  = -GM\frac{\vec{r}}{|\vec{r}|^3}.
$$ (eq:point-mass-gravity-field)

The vector $\vec{r}/|\vec{r}|^3$ combines the outward radial direction with an inverse-square magnitude, while the minus sign makes the field point inward, toward the mass. For a test mass $m$, the potential energy is $m\Phi$ and the gravitational force is $m\vec{g}$.

## Equipotential surfaces

<!-- Phil: a nice example here is a topographical map. Lines of constant elevation are equipotentials  -->

An **equipotential surface** is a surface on which the potential has the same value everywhere:

$$
  \Phi(x,y,z) = \mathrm{constant}.
$$

If a particle moves along an equipotential surface, then the change in potential is zero:

$$
  d\Phi = 0.
$$

Because the field is related to the gradient of the potential,

$$
  \vec{g} = -\vec{\nabla} \Phi,
$$

the gravitational force is normal to a regular equipotential surface wherever the field is nonzero. For a test mass $m$, a displacement tangent to it gives

$$
\mathrm dW=\vec F\cdot\mathrm d\vec s
=-m\vec\nabla\Phi\cdot\mathrm d\vec s
=-m\,\mathrm d\Phi=0.
$$

Gravity therefore does no work along the surface. Other forces acting on the particle may still do work.

```{admonition} Key idea
Field lines point in the direction of steepest decrease of the potential. Equipotential surfaces are perpendicular to those field lines.
```

````{prf:example} Topographic maps
A topographic contour joins points of equal elevation. In the near-surface approximation $\Phi=gz$ with constant $g$, it also joins points of equal gravitational potential. The contour traces where a horizontal equipotential surface meets the terrain; it is not the whole three-dimensional surface.

For contours drawn at equal elevation intervals, close spacing on the map means that elevation, and therefore potential, changes rapidly with horizontal position **along the terrain**. It indicates a steep slope. It does not imply that gravity is stronger there: in this approximation the three-dimensional field is the same $-g\hat z$ everywhere.

More generally, equal-potential intervals divided by the distance between neighbouring equipotential surfaces, measured in the normal direction, estimate $|\vec\nabla\Phi|$. Close spacing of those surfaces then indicates a stronger field. Distinguish this from the spacing of terrain contours on a map.

```{figure} figures/topographic_map.jpg
Topographic contours describe elevation on the terrain. Their spacing indicates slope; horizontal equipotential planes in the uniform-gravity approximation remain equally spaced for equal potential intervals.
```

Why can a steep hillside and a flat plain have the same gravitational field strength, even though their map contours look very different?
````

## A preview: circulation need not represent work

Our route to potential began with a force and its work. Line integrals also describe other vector fields, but their physical meaning depends on which field is being integrated. The following example illustrates that distinction.

```{admonition} Physical example: magnetic field around a wire
We will come back to magnetic fields later in the course, so for now we simply postulate the following result.

An infinitely long straight wire along the $z$ axis, carrying a steady current $I$, produces a magnetic field that circles around the wire:

$$
  \vec{B}(s) = \frac{\mu_0 I}{2\pi s}\,\hat{\varphi}.
$$

Here $s$ is the distance from the $z$ axis. The direction $\hat{\varphi}$ is tangent to a circle around the wire. Viewed from the positive $z$ axis looking toward the origin, $\hat{\varphi}$ points counterclockwise around the wire; the formula assumes current in the positive $z$ direction.

For a circular path of radius $s$ centered on the wire, the small displacement along the path is

$$
  d\vec{\ell} = s\,d\varphi\,\hat{\varphi}.
$$

Therefore,

$$
  \vec{B}\cdot d\vec{\ell}
  =
  \frac{\mu_0 I}{2\pi s}\,\hat{\varphi}
  \cdot
  s\,d\varphi\,\hat{\varphi}
  =
  \frac{\mu_0 I}{2\pi}\,d\varphi.
$$

Integrating once around the circle gives

$$
  \oint \vec{B}\cdot d\vec{\ell}
  =
  \int_0^{2\pi} \frac{\mu_0 I}{2\pi}\,d\varphi
  =
  \mu_0 I.
$$

This nonzero circulation means that this magnetic field cannot be written globally as the gradient of a single-valued scalar potential in the region surrounding the wire. This equation is a preview of Ampere's law, which we will study properly when we discuss electromagnetic fields.

**This line integral is not mechanical work.** A magnetic field exerts the Lorentz force

$$
\vec F_B=q\vec v\times\vec B
$$

on a charge moving with velocity $\vec v$. This force is perpendicular to $\vec v$, so its instantaneous power is

$$
P_B=\vec F_B\cdot\vec v
=q(\vec v\times\vec B)\cdot\vec v=0.
$$

The magnetic field can change the direction of a charged particle's motion, but it cannot change its kinetic energy by itself. There is therefore no possibility of extracting endless mechanical work from the nonzero value of $\oint\vec B\cdot d\vec\ell$: the circulation characterizes the geometry and sources of $\vec B$, not an energy gained by a particle going around the loop.
```
