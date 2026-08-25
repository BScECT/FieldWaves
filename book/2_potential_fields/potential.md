# Potential and Equipotential Surfaces

For a conservative field, the work done between two points can be described using a scalar function. This scalar function is called a **potential**.

The central idea is that instead of describing the vector field directly, we can describe a scalar field whose spatial changes determine the vector field.

## Potential

In the previous section we introduced a work function $W(P_0,P)$ and found that, for a conservative force field,

$$
  \vec{F} = \vec{\nabla} W.
$$

In many physical problems we define the potential $\Phi$ with the opposite sign:

$$
  \Phi = -W.
$$

With this convention, the force field is

$$
  \vec{F} = -\vec{\nabla} \Phi.
$$

The minus sign has an important physical meaning: the force points in the direction where the potential decreases most rapidly.

For example, near Earth's surface the gravitational potential energy of a mass $m$ can be written approximately as

$$
  \Phi(z) = mgz,
$$

where $z$ is height. The gravitational force is then

$$
  \vec{F} = -\vec{\nabla} \Phi = -mg\,\hat{z}.
$$

The force points downward, toward lower gravitational potential energy.

## Equipotential surfaces

An **equipotential surface** is a surface on which the potential has the same value everywhere:

$$
  \Phi(x,y,z) = \mathrm{constant}.
$$

If a particle moves along an equipotential surface, then the change in potential is zero:

$$
  dV = 0.
$$

Because the force is related to the gradient of the potential,

$$
  \vec{F} = -\vec{\nabla} \Phi,
$$

the force is perpendicular to the equipotential surface. Motion along the surface is sideways relative to the force, so the force does no work for a displacement along that surface.

```{admonition} Key idea
Field lines point in the direction of steepest change of the potential. Equipotential surfaces are perpendicular to those field lines.
```
