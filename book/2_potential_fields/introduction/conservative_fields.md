# Conservative Fields

In general, the line integral in {eq}`eq:work-integrated-work` could depend on the path followed between two points. A force field is called conservative when the work done by the field between two points does not depend on the path taken between them.

In other words, for any two paths $s_1$ and $s_2$ that start at the same point $P_0$ and end at the same point $P_1$,

$$
  \int_{s_1} \vec{F}\cdot\vec{ds}
  =
  \int_{s_2} \vec{F}\cdot\vec{ds}.
$$

Earth's gravitational field is an example of a conservative field: the work depends only on the starting and ending positions, not on the detailed route taken between them.

```{admonition} Exercise: a non-conservative field
Show that the two-dimensional vector field

$$
  \vec{F}(x,y) = -y\,\hat{x} + x\,\hat{y}
$$

is not conservative.

To do this, calculate the work done by the field around a circle of radius $R$ centered at the origin:

$$
  \vec{r}(\theta) = R\cos\theta\,\hat{x} + R\sin\theta\,\hat{y},
  \qquad 0 \leq \theta \leq 2\pi.
$$

1. Calculate the differential displacement $d\vec{s}$ along the circle.
2. Evaluate $\vec{F}\cdot d\vec{s}$ on the circle.
3. Compute the closed line integral

   $$
     \oint \vec{F}\cdot d\vec{s}.
   $$

4. Explain why your result shows that the field is not conservative.
```

```{dropdown} Solution
Along the circle,

$$
  d\vec{s}
  =
  -R\sin\theta\,d\theta\,\hat{x}
  +
  R\cos\theta\,d\theta\,\hat{y}.
$$

The field evaluated on the circle is

$$
  \vec{F}
  =
  -R\sin\theta\,\hat{x}
  +
  R\cos\theta\,\hat{y}.
$$

Therefore,

$$
  \vec{F}\cdot d\vec{s}
  =
  R^2\,d\theta.
$$

The work around the closed path is

$$
  \oint \vec{F}\cdot d\vec{s}
  =
  \int_0^{2\pi} R^2\,d\theta
  =
  2\pi R^2.
$$

This is not zero. A conservative field must have zero work around any closed path, so this field is not conservative.
```

```{admonition} Physical example: magnetic field around a wire
We will come back to magnetic fields later in the course, so for now we simply postulate the following result.

An infinitely long straight wire along the $z$ axis, carrying a steady current $I$, produces a magnetic field that circles around the wire:

$$
  \vec{B}(\rho) = \frac{\mu_0 I}{2\pi \rho}\,\hat{\phi}.
$$

Here $\rho$ is the distance from the $z$ axis. The direction $\hat{\phi}$ is the direction tangent to a circle around the wire. If you look along the positive $z$ direction, $\hat{\phi}$ points counterclockwise around the wire.

For a circular path of radius $\rho$ centered on the wire, the small displacement along the path is

$$
  d\vec{s} = \rho\,d\phi\,\hat{\phi}.
$$

Therefore,

$$
  \vec{B}\cdot d\vec{s}
  =
  \frac{\mu_0 I}{2\pi \rho}\,\hat{\phi}
  \cdot
  \rho\,d\phi\,\hat{\phi}
  =
  \frac{\mu_0 I}{2\pi}\,d\phi.
$$

Integrating once around the circle gives

$$
  \oint \vec{B}\cdot d\vec{s}
  =
  \int_0^{2\pi} \frac{\mu_0 I}{2\pi}\,d\phi
  =
  \mu_0 I.
$$

This result is not zero, so this magnetic field is not conservative. This equation is a preview of Ampere's law, which we will study properly when we discuss electromagnetic fields.
```

Let is now consider the work done by a conservative force field to go from $P_0$ to an arbitrary point $P$,

$$
W(P_0,P) = \int_{P_0}^P \vec{F}(x,y,z) \cdot \vec{ds},
$$

and to a point desplaced in the x-direction,

$$
W(P_0,P+\Delta x \cdot \hat{x}) = \int_{P_0}^{P+\Delta x \cdot \hat{x}} \vec{F}(x,y,z) \cdot \vec{ds}.
$$

Becase the path does not matter, we can go first from $P_0$ to $P$ and from there to $P+\Delta x \cdot \hat{x}$, so we have

$$
W(P_0,P+\Delta x \cdot \hat{x}) = W(P_0,P) + W(P,P+\Delta x \cdot \hat{x}),
$$

or 

$$
W(P_0,P+\Delta x \cdot \hat{x}) - W(P_0,P) = W(P,P+\Delta x \cdot \hat{x}) = \int_{P}^{P+\Delta x \cdot \hat{x}} \vec{F}(x,y,z) \cdot \vec{ds}.
$$

If we go in a straight line to $P+\Delta x \cdot \hat{x}$, the path diferencial becomes 

$$
\vec{ds} = dx\cdot \hat{x}.
$$

When we do the inner-product by the force field, 

$$
\vec{F}(x,y,z) = F_x(x,y,z) \hat{x} +  F_y(x,y,z) \hat{y} +  F_z(x,y,z) \hat{z},
$$ 

only the x component of the field matters (because $\hat{x}\cdot\hat{y} =  \hat{x}\cdot\hat{z} = 0$),

$$
\vec{F}(x,y,z) \cdot \vec{ds} = \vec{F}(x,y,z) \cdot dx \cdot \hat{x} = F_x(x,y,z) \cdot dx.
$$ 

So combining with the previous we have

$$
W(P_0,P+\Delta x \cdot \hat{x}) - W(P_0,P) = \int_{P}^{P+\Delta x \cdot \hat{x}} F_x(x,y,z)\,dx.
$$

Now we can go towards the partial derivative of the work with respect to $x$:

$$
\frac{\partial W}{\partial x}
=
\lim_{\Delta x \to 0}
\frac{W(P_0,P+\Delta x \cdot \hat{x}) - W(P_0,P)}{\Delta x}
=
\lim_{\Delta x \to 0}
\frac{1}{\Delta x}
\int_{P}^{P+\Delta x \cdot \hat{x}} F_x(x,y,z)\,dx
=
F_x(P).
$$

or, in a more compact form:

$$
\frac{\partial W}{\partial x} = F_x
$$

We could repeat the derivation for displacements in the y and z direction, respectively. Combining, we have

$$
\vec{\nabla} W = \vec{F}.
$$ (eq:work_is_gradient_of_work)

In *words*, {eq}`eq:work_is_gradient_of_work` tells us:

- The force field is the gradient of the work;
- The vector field, $\vec{F}$, is fully determined by the scalar field, $W$.

Any vector field that can be constructed as the gradient of a *work* function, i.e. by {eq}`eq:work_is_gradient_of_work`, is a **conservative field**..
