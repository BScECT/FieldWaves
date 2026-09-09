# Conservative Fields

In general, the line integral in {eq}`eq:work-integrated-work` could depend on the path followed between two points. A force field is called conservative when the work done by the field between two points does not depend on the path taken between them.

In other words, for any two paths $s_1$ and $s_2$ that start at the same point $P_0$ and end at the same point $P_1$,

$$
  \int_{s_1} \vec{F}\cdot\vec{ds}
  =
  \int_{s_2} \vec{F}\cdot\vec{ds}.
$$

Earth's gravitational field is an example of a conservative field: the work depends only on the starting and ending positions, not on the detailed route taken between them.

Path independence also means that the work around every closed path is zero. Go from $P_0$ to $P_1$ along one path and return along another. Reversing a path reverses the sign of its line integral; because the two forward paths give the same work, the outward and return contributions cancel:

$$
\oint\vec F\cdot\mathrm d\vec s=0.
$$

Conversely, if every closed-path integral vanishes, joining one path to the reverse of another shows that their work integrals agree. A single loop with nonzero work is therefore enough to disprove conservativeness.

<!-- Phil: I found this example quite confusing. Perhaps start with something easier? 
I also don't like how this solution mixes a circular parametrization with Cartesian unit vectors. -->



```{admonition} Exercise: a non-conservative field
Show that the two-dimensional vector field

$$
  \vec{F}(x,y) = -y\,\hat{x} + x\,\hat{y}
$$

is not conservative.

To do this, calculate the work done by the field around a circle of radius $R$ centered at the origin:

$$
  \vec{r}(\varphi) = R\cos\varphi\,\hat{x} + R\sin\varphi\,\hat{y},
  \qquad 0 \leq \varphi \leq 2\pi.
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
  -R\sin\varphi\,d\varphi\,\hat{x}
  +
  R\cos\varphi\,d\varphi\,\hat{y}.
$$

The field evaluated on the circle is

$$
  \vec{F}
  =
  -R\sin\varphi\,\hat{x}
  +
  R\cos\varphi\,\hat{y}.
$$

Therefore,

$$
  \vec{F}\cdot d\vec{s}
  =
  R^2\,d\varphi.
$$

The work around the closed path is

$$
  \oint \vec{F}\cdot d\vec{s}
  =
  \int_0^{2\pi} R^2\,d\varphi
  =
  2\pi R^2.
$$

This is not zero. A conservative field must have zero work around any closed path, so this field is not conservative.
```

## From work along a path to a function of position

Choose one reference point $P_0$ and **keep it fixed**. Path independence now lets us assign a single number to each endpoint $P$: the work done by the conservative force in reaching it from $P_0$,


$$
W(P_0,P) = \int_{P_0}^P \vec{F}(x,y,z) \cdot \vec{ds},
$$

This endpoint function is measured in joules. It exists because the work is independent of the route; for a general force field, specifying the endpoints alone would not determine the work. In the derivatives below, only the endpoint $P$ varies.

For a point displaced in the x-direction,

$$
W(P_0,P+\Delta x \cdot \hat{x}) = \int_{P_0}^{P+\Delta x \cdot \hat{x}} \vec{F}(x,y,z) \cdot \vec{ds}.
$$

Because the path does not matter, we can go first from $P_0$ to $P$ and from there to $P+\Delta x \cdot \hat{x}$, so we have

$$
W(P_0,P+\Delta x \cdot \hat{x}) = W(P_0,P) + W(P,P+\Delta x \cdot \hat{x}),
$$

or 

$$
W(P_0,P+\Delta x \cdot \hat{x}) - W(P_0,P) = W(P,P+\Delta x \cdot \hat{x}) = \int_{P}^{P+\Delta x \cdot \hat{x}} \vec{F}(x,y,z) \cdot \vec{ds}.
$$

If we go in a straight line to $P+\Delta x \cdot \hat{x}$, the path differential becomes 

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

Equation {eq}`eq:work_is_gradient_of_work` says that the force is the gradient of the endpoint function $W(P_0,P)$, with $P_0$ held fixed. The spatial variation of this scalar function determines the force vector at each point.

Conversely, if a force is the gradient of a single-valued scalar function throughout the domain, integrating along a path gives the difference of that function's endpoint values. Its work is therefore path independent. In the next section we give the endpoint function an energy interpretation, taking care with the sign.
