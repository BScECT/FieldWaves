# Potential and Equipotential Surfaces

For a conservative field, the field can be described using a scalar function. This scalar function is called a **potential**.

The central idea is that instead of describing the vector field directly, we can describe a scalar field whose spatial changes determine the vector field.

<!-- Phil: this sction is mixing the definitions of potential and potential energy together. 
I think electrical potential is an easy example to consider as well, because everyone knows what voltage is.  -->

## Potential

In the previous section we introduced the work function $W(P_0,P)$. For a conservative field, the work between two points is independent of the path:

$$
  W(P_0,P) = \int_{P_0}^{P} \vec{g}\cdot\vec{ds}.
$$

This motivates describing the field with a scalar potential. We define the potential $\Phi$ by

$$
  \vec{g} = -\vec{\nabla} \Phi.
$$

Equivalently, choosing the reference point so that $\Phi(P_0)=0$, the work done by the field is

$$
  W(P_0,P) = -\Phi(P).
$$

For a gravitational field, $\Phi$ is the gravitational potential energy per unit mass. The corresponding force on a mass $m$ is therefore

$$
  \vec{F} = m\vec{g} = -m\vec{\nabla} \Phi.
$$

The minus sign means that the gravitational field points in the direction where the potential decreases most rapidly. The associated gravitational potential energy is $U=m\Phi$.

For example, near Earth's surface the gravitational potential can be written approximately as

$$
  \Phi(z) = gz,
$$

where $z$ is height. The gravitational field is then

$$
  \vec{g} = -\vec{\nabla} \Phi = -g\,\hat{z}.
$$

The corresponding force on a mass $m$ is $\vec{F}=-mg\,\hat{z}$, and the gravitational potential energy is $U=mgz$.

As a further example, consider the gravitational field of a point mass $M$ at the origin. We will derive this result later; for now, we postulate that the gravitational potential per unit mass is

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

the force is perpendicular to the equipotential surface. Motion along the surface is sideways relative to the force, so the force does no work for a displacement along that surface.

```{admonition} Key idea
Field lines point in the direction of steepest decrease of the potential. Equipotential surfaces are perpendicular to those field lines.
```

```{prf:example} Topographic maps
A common analogy for equipotentials are topographic maps. Lines indicate constant elevation, and therefore, constant gravitational potential. 
Consider: if you see many equipotiential lines spaced close together, what is this saying about the field? What does it mean if they are spaced far apart? 

```{figure} figures/topographic_map.jpg
```
``` 