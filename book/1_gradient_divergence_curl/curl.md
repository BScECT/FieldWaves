# Curl

The curl is a peculiar operator because it turns a vector field into another vector field. Often a determinant expression is used, but we can give it in terms of even and odd permutations of the triplet $(x,y,z)$, which is easy to remember. Let $\boldsymbol v(\boldsymbol r,t)$ be a continuously differentiable space-time function. Then

$$
\nabla\times\boldsymbol v = \hat{\boldsymbol x}(\partial_y v_z - \partial_z v_y) + \hat{\boldsymbol y}(\partial_z v_x - \partial_x v_z) + \hat{\boldsymbol z}(\partial_x v_y - \partial_y v_x).
$$ (eq:curl)

Notice that the three terms have the triplet pairs $(xyz)-(xzy)$, $(yzx)-(yxz)$, and $(zxy)-(zyx)$ in (1) direction, (2) differentiation, and (3) vector component. The first in each pair is an even permutation of $(xyz)$ and the second is an odd permutation. It can be seen that in each term the direction of the resulting vector $\boldsymbol w = \nabla\times\boldsymbol v$ is perpendicular both to the direction of differentiation and to the component of $\boldsymbol v$ that is being differentiated. The curl is interpreted as the rate of circulation of the vector field $\boldsymbol v$.

## The circulation integral

Let us first look at the situation of an elementary area with centre point $\boldsymbol r_p = \left(\tfrac{1}{2}\mathrm{d}x,\ \tfrac{1}{2}\mathrm{d}y,\ \tfrac{1}{2}\mathrm{d}z\right)$. The circulation integral for the path from $y=0$ to $y=\mathrm{d}y$ at $x=\tfrac{1}{2}\mathrm{d}x$ and $z=0$ is given by

$$
\int_{y=0}^{\mathrm{d}y} v_y\!\left(\tfrac{1}{2}\mathrm{d}x,\,y,\,0\right)\mathrm{d}l ,
$$

and completing the circulation for all four sides of the elementary area as shown in {numref}`fig-circulation`, we find

```{figure} figures/circulation.png
:name: fig-circulation
:width: 55%

Net circulation integral on a rectangle around the point $\boldsymbol r_p$.
```

$$
\begin{aligned}
\oint_{\boldsymbol r}\boldsymbol\tau\cdot\boldsymbol v\,\mathrm{d}l
&= \int_{y=0}^{\mathrm{d}y} v_y\!\left(\tfrac{1}{2}\mathrm{d}x,\,y,\,0\right)\mathrm{d}l
 + \int_{z=0}^{\mathrm{d}z} v_z\!\left(\tfrac{1}{2}\mathrm{d}x,\,\mathrm{d}y,\,z\right)\mathrm{d}l \\
&\quad - \int_{y=0}^{\mathrm{d}y} v_y\!\left(\tfrac{1}{2}\mathrm{d}x,\,y,\,\mathrm{d}z\right)\mathrm{d}l
 - \int_{z=0}^{\mathrm{d}z} v_z\!\left(\tfrac{1}{2}\mathrm{d}x,\,0,\,z\right)\mathrm{d}l ,
\end{aligned}
$$ (eq:circint)

where the symbol $\oint$ stands for a closed loop integral, $\boldsymbol\tau$ is the local unit tangent vector along the edges of $\mathbb{S}$, and $l$ is the arclength along the path.

Earlier we introduced the Taylor series expansion for a function in one variable, and we give it here for each vector component of $\boldsymbol v$ around the point $\boldsymbol r_p$,

$$
\begin{aligned}
v_x(\boldsymbol r) &= v_x(\boldsymbol r_p) + \partial_x v_x\left(x-\tfrac{1}{2}\mathrm{d}x\right) + \partial_y v_x\left(y-\tfrac{1}{2}\mathrm{d}y\right) + \partial_z v_x\left(z-\tfrac{1}{2}\mathrm{d}z\right) + \text{higher order terms}, \\
v_y(\boldsymbol r) &= v_y(\boldsymbol r_p) + \partial_x v_y\left(x-\tfrac{1}{2}\mathrm{d}x\right) + \partial_y v_y\left(y-\tfrac{1}{2}\mathrm{d}y\right) + \partial_z v_y\left(z-\tfrac{1}{2}\mathrm{d}z\right) + \text{higher order terms}, \\
v_z(\boldsymbol r) &= v_z(\boldsymbol r_p) + \partial_x v_z\left(x-\tfrac{1}{2}\mathrm{d}x\right) + \partial_y v_z\left(y-\tfrac{1}{2}\mathrm{d}y\right) + \partial_z v_z\left(z-\tfrac{1}{2}\mathrm{d}z\right) + \text{higher order terms},
\end{aligned}
$$

which is the Taylor series expansion to first order. Substituting these results in {eq}`eq:circint` leads to

$$
\oint_{\boldsymbol r}\boldsymbol\tau\cdot\boldsymbol v\,\mathrm{d}l = (\partial_y v_z - \partial_z v_y)\,\mathrm{d}y\,\mathrm{d}z + \text{higher order terms}.
$$

Similarly, the net circulation integral for the elementary surface area perpendicular to the $\hat{\boldsymbol y}$-axis is $(\partial_z v_x - \partial_x v_z)\,\mathrm{d}x\,\mathrm{d}z$, and the net circulation integral for the elementary surface area perpendicular to the $\hat{\boldsymbol z}$-axis is $(\partial_x v_y - \partial_y v_x)\,\mathrm{d}x\,\mathrm{d}y$.

For this reason, the physical interpretation of the curl is the net circulation per unit of surface area at the point $\boldsymbol r_p$, and it can be expressed as

$$
\hat{\boldsymbol n}\cdot(\nabla\times\boldsymbol v) = \lim_{S\rightarrow 0}\frac{\oint_{\boldsymbol r}\boldsymbol\tau\cdot\boldsymbol v\,\mathrm{d}l}{A},
$$ (eq:circ1)

in which

$$
A = \int_{\boldsymbol r\in\mathbb{S}}\mathrm{d}S
$$

is the surface area of the surface $\mathbb{S}$.

:::{admonition} The curl in words
:class: tip
The curl of a vector field is the net circulation of that field per unit of surface area, and it points along the normal of the surface for which that circulation is largest.
:::

## Stokes' integral theorem

The unit normal $\hat{\boldsymbol n}$ in {eq}`eq:circ1` is the normal vector to the surface area $\mathbb{S}$ and is oriented to the side of advance of a right-hand screw as it is turned in the direction of $\boldsymbol\tau$ around the boundary of $\mathbb{S}$. This leads to Stokes' integral theorem, given by

$$
\oint_{\boldsymbol r}\boldsymbol\tau\cdot\boldsymbol v\,\mathrm{d}l = \int_{\boldsymbol r\in\mathbb{S}}\hat{\boldsymbol n}\cdot(\nabla\times\boldsymbol v)\,\mathrm{d}S .
$$ (eq:stokes)

## Exercises

1. Use Stokes' theorem to evaluate $\oint_{\boldsymbol r}\boldsymbol\tau\,\mathrm{d}l$, where $\boldsymbol\tau$ is the unit tangent along the closed boundary of the area $\mathbb{S}$. The integration runs in the direction of circulation that forms a right-handed system with the unit normal vector on $\mathbb{S}$.
2. Show that when $\boldsymbol v(\boldsymbol r) = \boldsymbol a\,p(\boldsymbol r)$, where $\boldsymbol a$ is an arbitrary constant vector and $p(\boldsymbol r)$ is a continuously differentiable scalar function, Stokes' integral theorem gives

    $$
    \oint_{\boldsymbol r}\boldsymbol\tau\,p\,\mathrm{d}l = \int_{\boldsymbol r\in\mathbb{S}}(\hat{\boldsymbol n}\times\nabla)p\,\mathrm{d}S,
    $$

    which is Stokes' theorem for the gradient.
3. Show that when $\boldsymbol v(\boldsymbol r) = \boldsymbol a\times\boldsymbol w(\boldsymbol r)$, where $\boldsymbol a$ is an arbitrary constant vector and $\boldsymbol w(\boldsymbol r)$ is a continuously differentiable vector function, Stokes' integral theorem gives

    $$
    \oint_{\boldsymbol r}\boldsymbol\tau\times\boldsymbol w\,\mathrm{d}l = \int_{\boldsymbol r\in\mathbb{S}}(\hat{\boldsymbol n}\times\nabla)\times\boldsymbol w\,\mathrm{d}S .
    $$
4. Ampère's law is given by $\nabla\times\boldsymbol H = \boldsymbol J$, which states that the electric current is equal to the curl of the magnetic field. Convert this to integral form using Stokes' theorem, by using a flat surface $\mathbb{S}$ and choosing a unit normal vector $\hat{\boldsymbol n}$ on $\mathbb{S}$. You should find

    $$
    \oint_{\boldsymbol r}\boldsymbol H\cdot\boldsymbol\tau\,\mathrm{d}l = \int_{\boldsymbol r\in\mathbb{S}}\hat{\boldsymbol n}\cdot\boldsymbol J\,\mathrm{d}S .
    $$

    Show in which direction the unit tangent vector $\boldsymbol\tau$ is circulating at the boundary of $\mathbb{S}$, and in which direction through the surface a positive current should run.
