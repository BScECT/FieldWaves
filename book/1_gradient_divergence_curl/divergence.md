# Divergence of a vector field

Now we introduce a vector field $\boldsymbol v(x,y,z,t)$ and consider the field inside a rectangular volume with sides $\mathrm{d}x,\mathrm{d}y,\mathrm{d}z$ that we can shrink to an infinitesimal cube. Let the left side be located at position $x$ and the right side at $x+\mathrm{d}x$.

If we consider $\boldsymbol v$ to be a fluid flow vector, we understand that the component $v_x$ is the flow in the $x$-direction, the component $v_y$ is the flow in the $y$-direction, and the component $v_z$ is the flow in the $z$-direction. The flow in the $x$-direction can flow in or out of the cube through faces perpendicular to the $x$-axis. Hence, the outward flow through the surface perpendicular to the $x$-axis at $x+\mathrm{d}x$ is given by $v_x(x+\mathrm{d}x,y,z,t)\,\mathrm{d}y\,\mathrm{d}z$, because $v_x(x+\mathrm{d}x,y,z,t)$ is the component of the flow perpendicular to that surface and $\mathrm{d}y\,\mathrm{d}z$ is the area of the surface through which it flows.

Then it is clear that the outward flow through the left side is $-v_x(x,y,z,t)\,\mathrm{d}y\,\mathrm{d}z$, and the minus sign comes from the fact that the outward unit normal there is in the $(-x)$-direction. This means that the total outward flow in the $x$-direction is given by

$$
\left[v_x(x+\mathrm{d}x,y,z,t) - v_x(x,y,z,t)\right]\mathrm{d}y\,\mathrm{d}z = \partial_x v_x\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z = \partial_x v_x\,\mathrm{d}V .
$$

We can combine this with the outward flow in the $y$- and $z$-directions to obtain $(\partial_x v_x + \partial_y v_y + \partial_z v_z)\,\mathrm{d}V$. This can be written as

$$
\mathrm{d}\Phi = (\nabla\cdot\boldsymbol v)\,\mathrm{d}V,
$$ (eq:flux)

where $\Phi$ is the total outward flux.

## Gauss' integral theorem

On the other hand, the outward flow can be generally described as $(\boldsymbol v\cdot\hat{\boldsymbol n})\hat{\boldsymbol n}$, because it describes the sum of normal components directed along the outward unit normal vector on the surface. The volume of the flow through the surface per unit time is then given by

$$
\Phi = \int_{\mathbb{S}}(\boldsymbol v\cdot\hat{\boldsymbol n})\,\mathrm{d}S .
$$ (eq:vflux)

Note that the single integration symbol represents here a surface, or two-dimensional, integral, which is short-hand notation for the double integration that must be carried out. This is indicated by the integration surface $\mathbb{S}$ as a subscript to the integral, so that no confusion occurs about the kind of integration that is meant.

This expression defines the **flux** $\Phi$ of the vector field $\boldsymbol v$ through the surface $\mathbb{S}$. The definition of a flux is not restricted to the flow of fluids. A flux can be computed for any vector field, such as the flux of the electric field through a surface.

The statements in {eq}`eq:flux` and {eq}`eq:vflux` describe the same flow and should be equal. Let us write {eq}`eq:flux` as a total volume derivative,

$$
\frac{\mathrm{d}\Phi}{\mathrm{d}V} = \nabla\cdot\boldsymbol v,
$$

and integrate it over the volume; we find

$$
\Phi = \int_{\mathbb{D}}(\nabla\cdot\boldsymbol v)\,\mathrm{d}V .
$$

Note that the single integration symbol represents here a volume, or three-dimensional, integral, which is short-hand notation for the triple integration that must be carried out. This is indicated by the integration volume $\mathbb{D}$ as a subscript to the integral, so that no confusion occurs about the kind of integration that is meant. We find then

$$
\int_{\mathbb{D}}(\nabla\cdot\boldsymbol v)\,\mathrm{d}V = \int_{\mathbb{S}}(\boldsymbol v\cdot\hat{\boldsymbol n})\,\mathrm{d}S .
$$ (eq:gauss)

We have just derived Gauss' integral theorem, or divergence theorem, and we found the physical interpretation of the divergence of a vector field:

:::{admonition} The divergence in words
:class: tip
The divergence of a vector field is the outward flux of the vector field per unit volume.
:::

## Incompressible flow

For fluid flow under constant density and away from locations that have generated the flow, sometimes the approximation of the fluid to be incompressible can be made. Let the source or sink be located at $\boldsymbol r=\boldsymbol 0$. When the fluid is incompressible there cannot be any net outward flow, because what goes out on one side must come in on the other; otherwise the fluid would be compressible. We can state that

$$
\nabla\cdot\boldsymbol v = 0, \qquad \text{for } r\ne 0 .
$$

In a constant-density environment the flow field must be radial away from the source. Assuming the source is a volume injection at $\boldsymbol r=\boldsymbol 0$, we can write the field as

$$
\boldsymbol v = f(r)\,\boldsymbol r .
$$

The function $f(r)$ depends only on the radial distance $r=\sqrt{x^2+y^2+z^2}$. We can find $f(r)$ by requiring that the flow is divergence free,

$$
\nabla\cdot\boldsymbol v = 3f(r) + \boldsymbol r\cdot\nabla f(r) = 0, \qquad \text{for } r\ne 0 .
$$

This gives

$$
f(r) = \frac{A}{r^3},
$$ (eq:NF)

where $A$ is a constant that is determined by the source or sink.

## Electric potential, electric field, and electric current

The result above for fluid flow has an equivalent for the electric field and electric potential, which combines gradient and divergence. We start with the fact that for a constant current that is injected in a medium with constant resistivity $\rho$, we can write, for points away from the current injection point, that the electric field is divergence free,

$$
\nabla\cdot\boldsymbol E = 0 .
$$ (eq:divE)

The electric field can be written in terms of the gradient of an electric potential $V$ as

$$
\boldsymbol E(x,y,z) = -\nabla V(x,y,z).
$$ (eq:EgradV)

When we substitute this relation in {eq}`eq:divE`, we find the equation for the electric potential $V$ given by

$$
\nabla\cdot\nabla V = 0,
$$ (eq:laplV)

which written out in full gives

$$
\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}\right)V = 0 .
$$

The divergence of a gradient is known as the Laplacian and is a scalar second-order differential operator. The solution to such an equation, where the potential originates from a point source in the origin, is well known and can be written as

$$
V(x,y,z) = \frac{A}{r} + B,
$$ (eq:pot)

where the distance to the source is given by $r=\sqrt{x^2+y^2+z^2}$ and the constant $B$ can be taken zero by requiring that the potential goes to zero infinitely far away from the location of the source of the potential field.

To find the constant $A$ we need to find out the influence of the source we use to generate the electric potential. To do that we need the local version of Ohm's law, given by

$$
\boldsymbol J = \rho^{-1}\boldsymbol E,
$$ (eq:bJ)

in which $\boldsymbol J$ is the electric current density in A/m$^2$. Because a static electric field can be written as the gradient of the electric potential, this equation can be written as

$$
\boldsymbol J = -\rho^{-1}\nabla V .
$$ (eq:Ohm)

To find the constant $A$ we can think of a point at the origin where a current is injected. Because the spatial dependency of the potential is radial distance, the current will be distributed evenly in all directions. Therefore the surface of constant potential is a spherical surface, as can be seen from {eq}`eq:pot` as well when we find all the points where $V$ is constant. Only the current that is in the direction of the outward unit normal on any spherical surface can leave that surface, and hence we can write the total electric current leaving that surface (and hence going into the earth) as $I = 4\pi r^2\,\hat{\boldsymbol n}\cdot\boldsymbol J$, where $\hat{\boldsymbol n}$ is the outward directed unit normal on any spherical surface of constant potential and $4\pi r^2$ is the surface area of the sphere with radius $r$. We can use {eq}`eq:Ohm` to express the electric current density in terms of the electric potential and substitute the solution of the potential given in {eq}`eq:pot` to find

$$
I = 4\pi r^2\,\hat{\boldsymbol n}\cdot\boldsymbol J
  = -4\pi r^2 A\,\hat{\boldsymbol n}\cdot\nabla\frac{1}{\rho r}
  = 4\pi r^2 A\frac{\hat{\boldsymbol n}\cdot\boldsymbol r}{\rho r^3}
  = \frac{4\pi A}{\rho},
$$ (eq:Icur)

because $\hat{\boldsymbol n}=\boldsymbol r/r$ and $\hat{\boldsymbol n}\cdot\hat{\boldsymbol n}=1$. Therefore

$$
A = \frac{\rho I}{4\pi},
$$

and the electric potential is given by

$$
V(x,y,z) = \frac{\rho I}{4\pi r},
$$ (eq:dcVfull)

where the point of the current injection must be avoided, so $r>0$. The total current that is injected into the ground times the total resistance equals the electric potential, which is Ohm's law. The total resistance is given by the electric resistivity $\rho$ divided by $4\pi$ times the radial distance from the current injection point.

Now suppose there is a surface at $z=0$ between non-conductive air and the conductive subsurface, and the injection point is at the surface $z=0$. In that case the current can only go into the ground below the surface, hence for $z>0$, and the relevant surface area is $2\pi r^2$, because the current is now distributed over the surface area of half a sphere. Therefore, anywhere in the half-space $z>0$ the electric potential is given by

$$
V(x,y,z) = \frac{\rho I}{2\pi r},
$$ (eq:dcVhf)

where again $r>0$.

You see that the electric potential depends on the value of the electric resistivity even though it does not occur in {eq}`eq:pot`. This is because the electric potential depends on the current strength, and that in turn depends on the resistivity of the ground through which this current must flow. When it is a constant it is merely a scaling parameter, but when it is a function of position it can become a complicated relation that must be found numerically.

### Two electrodes at the surface

{numref}`fig-dcpoth` and {numref}`fig-dcpotv` show a plot of the electric potential $V(x,y,z)$, for $z=0$ and for $y=0,\ z>0$ respectively. The arrows in the plots indicate the vector directions of the electric current. For this configuration we have the electric potential given by

$$
\begin{aligned}
V(x,y,z) &= V(x-a/2,y,z) - V(x+a/2,y,z), \\
V(x,y,z) &= \frac{\rho I}{2\pi}\left(\frac{1}{\sqrt{(x-a/2)^2+y^2+z^2}} - \frac{1}{\sqrt{(x+a/2)^2+y^2+z^2}}\right),
\end{aligned}
$$ (eq:Vpdp)

where the point $x=a/2$ is the point of current injection (current goes into the ground, also known as source) and the point $x=-a/2$ is the current extraction point (current goes out of the ground, also known as sink), for which reason the potential related to that location is negative.

```{figure} figures/dcpoth.png
:name: fig-dcpoth
:width: 75%

Electric potential difference and electric current density vectors on the ground surface $z=0$, with two electrodes at $x=-a/2$ and $x=a/2$. Distances are normalised to the electrode spacing $a$.
```

```{figure} figures/dcpotv.png
:name: fig-dcpotv
:width: 85%

Electric potential difference and electric current density vectors in the vertical cross-section $y=0,\ z>0$, with two electrodes at $x=-a/2$ and $x=a/2$. Distances are normalised to the electrode spacing $a$.
```

To make the current run in the subsurface, the two points must be connected to a current source above the ground through an electronically controlled connection with a battery or other charge-storage/current-producing device. This is because electric current can only run in closed loops. The total current running in the wire above the ground is distributed in the ground, and fractions of current run everywhere in the subsurface where the resistivity is finite.

## The magnetic dipole

Another example is the magnetic field of the Earth, which to first order is a dipole field. The source is therefore different from what we have seen in the fluid flow and electric potential problems. The Earth's magnetic field (to first order) is the field generated by a magnetic north pole and a magnetic south pole very close together. The dipole vector $\boldsymbol m$ points from the south pole of the dipole to the north pole, and its size is given by the strength of the dipole. The magnetic field $\boldsymbol B$ is given by

$$
\boldsymbol B = \frac{3\boldsymbol r(\boldsymbol r\cdot\boldsymbol m) - r^2\boldsymbol m}{r^5}.
$$ (eq:magB)

For this particular solution $\nabla\cdot\boldsymbol B = 0$ for all points in space, also at the source at $\boldsymbol r=\boldsymbol 0$.

## Exercises

1. If $(\boldsymbol v\cdot\hat{\boldsymbol n})\hat{\boldsymbol n}$ in {eq}`eq:vflux` is the fraction of $\boldsymbol v$ that leaves the volume $\mathbb{D}$ through the surface $\mathbb{S}$, what is the fraction of the flow that does not leave the volume $\mathbb{D}$?
2. Carry out the differentiations to show that the expression for $f(r)$ in {eq}`eq:NF` is correct.
3. The total current that can be injected into the ground must run in a cable from the source (battery and signal conditioner) to the ground. Once it is in the ground it is free to go anywhere, but the total volume integral must remain equal to the current that runs in the cable, because of the continuity of electric current. We have used the symbol $I$ to denote the total current, and in {eq}`eq:Icur` you have seen a sequence of expressions that resulted in finding the unknown coefficient $A$.

    Another way of finding this result is by observing that the electric potential is the solution of {eq}`eq:laplV` under the condition that a current is injected at the origin. Hence the actual problem is obtained if you take the divergence of both sides of {eq}`eq:Ohm`. This results in $\nabla\cdot\boldsymbol E = \rho\,\nabla\cdot\boldsymbol J$. Integrate both sides of this equation over a spherical volume with fixed radius $r$ and use Gauss' theorem to show that

    $$
    -\int_{\mathbb{S}}\hat{\boldsymbol n}\cdot(\nabla V)\,\mathrm{d}S = \rho\int_{\mathbb{S}}\hat{\boldsymbol n}\cdot\boldsymbol J\,\mathrm{d}S .
    $$ (eq:fluxintE)

    The right-hand side is a constant, because it is equal to the total current $I$ that comes from the source and runs in the cable, and therefore it must run out across any spherical surface around the current injection point. Hence, we find

    $$
    \int_{\mathbb{S}}\hat{\boldsymbol n}\cdot(\nabla V)\,\mathrm{d}S = -\rho I .
    $$

    Substitute the solution proposed for $V$ of {eq}`eq:pot` with $B=0$ in this equation to verify that $A=\rho I/(4\pi)$.
4. Evaluate the gradient of the potential expressed in {eq}`eq:Vpdp` and give the expression for the electric current density in the ground at and below the ground surface. Write a Python script that computes the electric potential and the electric current density on the ground surface and in a vertical cross-section, and reproduce the plots of {numref}`fig-dcpoth` and {numref}`fig-dcpotv`. Normalise distance to the electrode spacing $a$ and avoid the points $x=\pm a/2$. You can choose any colour map you like for the potential and choose a contrasting colour for the arrows representing the current lines and directions.
5. The electric field associated with the electric potential given in {eq}`eq:Vpdp` can be evaluated by taking the gradient of the potential, because of {eq}`eq:EgradV`. Give an argument why the flux integral of the electric field $\int_{\mathbb{S}}\hat{\boldsymbol n}\cdot\boldsymbol E\,\mathrm{d}S = 0$ for every closed and piecewise smooth surface that does not include the current injection and extraction points $x=\pm a/2$.
6. Verify that the magnetic field expressed in {eq}`eq:magB` is divergence free for all points in space.
7. Show that the divergence of a vector field in cylindrical and in spherical coordinates is given by

    $$
    \begin{aligned}
    \nabla\cdot\boldsymbol v(\varrho,\phi,z) &= \frac{1}{\varrho}\left[\partial_\varrho(\varrho v_\varrho) + \partial_\phi v_\phi\right] + \partial_z v_z, \\
    \nabla\cdot\boldsymbol v(r,\phi,\theta) &= \frac{1}{r^2}\partial_r(r^2 v_r) + \frac{1}{r\sin(\theta)}\left[\partial_\theta(\sin(\theta)v_\theta) + \partial_\phi v_\phi\right].
    \end{aligned}
    $$

    Please remember that in cylindrical coordinates $\varrho=\sqrt{x^2+y^2}$ and in spherical coordinates $r=\sqrt{x^2+y^2+z^2}$!
8. Consider a general flow field $\boldsymbol v(\boldsymbol r) = \left(v_x(y,z),\,v_y(x,z),\,v_z(x,y)\right)$ flowing in an open space containing a closed surface $\mathbb{S}$. Evaluate the flux integral $\int_{\mathbb{S}}\hat{\boldsymbol n}\cdot\boldsymbol v\,\mathrm{d}S$.
9. Show that when $\boldsymbol v(\boldsymbol r) = \boldsymbol a\,p(\boldsymbol r)$, where $\boldsymbol a$ is an arbitrary constant vector and $p(\boldsymbol r)$ is a continuously differentiable scalar function, Gauss' integral theorem gives

    $$
    \int_{\mathbb{S}}p\,\hat{\boldsymbol n}\,\mathrm{d}S = \int_{\mathbb{D}}\nabla p\,\mathrm{d}V,
    $$

    which is Gauss' theorem for the gradient.
10. Show that when $\boldsymbol v(\boldsymbol r) = \boldsymbol a\times\boldsymbol w(\boldsymbol r)$, where $\boldsymbol a$ is an arbitrary constant vector and $\boldsymbol w(\boldsymbol r)$ is a continuously differentiable vector function, Gauss' integral theorem gives

    $$
    \int_{\mathbb{S}}\hat{\boldsymbol n}\times\boldsymbol w\,\mathrm{d}S = \int_{\mathbb{D}}\nabla\times\boldsymbol w\,\mathrm{d}V,
    $$

    which is Gauss' theorem for the curl.
