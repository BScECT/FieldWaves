# Coordinate systems

Three-dimensional space can be built from many frames of reference, but here it is built from the rectangular, cylindrical and spherical coordinate systems.

- The **rectangular** (Cartesian) coordinate system is characterised by the three base vectors $\hat{\boldsymbol x},\hat{\boldsymbol y},\hat{\boldsymbol z}$ with coordinates and ranges $-\infty<x<\infty$, $-\infty<y<\infty$, $-\infty<z<\infty$, length elements $\mathrm{d}x,\mathrm{d}y,\mathrm{d}z$, and all three coordinate surfaces are planes.
- The **cylindrical** coordinate system is characterised by the base vectors $\hat{\boldsymbol\varrho},\hat{\boldsymbol\phi},\hat{\boldsymbol z}$ with coordinates and ranges $0<\varrho<\infty$, $0<\phi<2\pi$, $-\infty<z<\infty$, length elements $\mathrm{d}\varrho,\ \varrho\,\mathrm{d}\phi,\ \mathrm{d}z$. The coordinate surfaces for constant $\phi$ and for constant $z$ are planes, while the surface of constant $\varrho$ has a cylindrical shape.
- The **spherical** coordinate system is characterised by the base vectors $\hat{\boldsymbol r},\hat{\boldsymbol\phi},\hat{\boldsymbol\theta}$ with coordinates and ranges $0<r<\infty$, $0<\phi<2\pi$, $0<\theta<\pi$, length elements $\mathrm{d}r,\ r\sin(\theta)\,\mathrm{d}\phi,\ r\,\mathrm{d}\theta$. The coordinate surface for constant $r$ is a sphere, for constant $\phi$ a plane, and for constant $\theta$ a cone.

:::{admonition} A note on the radial symbol
:class: note
The cylindrical radial coordinate is written here as $\varrho$ and the spherical one as $r$. Both measure a distance from an axis or from a point, but they are *not* the same quantity: $\varrho=\sqrt{x^2+y^2}$ while $r=\sqrt{x^2+y^2+z^2}$, so that $r=\sqrt{\varrho^2+z^2}$. In the figures below, and in some textbooks, the cylindrical radius is also drawn as $r$. Keeping the two apart from the start avoids a great deal of confusion later, when the gradient and the divergence are written out in both systems.
:::

Physical measurements take place in space-time, and the physical quantities that are described in classical physics are tensor functions of space and time. The time coordinate is indicated by the symbol $t$. The derivative of a differentiable function $f(\boldsymbol r,t)$ with respect to the time coordinate is given by

$$
\partial_t f(\boldsymbol r,t) = \frac{\partial f(\boldsymbol r,t)}{\partial t},
$$

where it is understood that the subscript $t$ is reserved for indicating time.

## Cartesian reference frame

Tensor calculus has been developed as the mathematical vehicle to describe macroscopic physical phenomena. It is a direct consequence of the postulate of continuum physics that all quantities occurring in the laws of macroscopic physics are geometric objects and therefore they are tensor quantities. Tensor calculus prescribes the rules for algebraic manipulations on tensors and how to apply the rules of differentiation and integration to tensors. The corresponding notation is known as the subscript notation. Because the subscript notation is not the generally used notation, here the vector notation is used.

The Cartesian reference frame in three-dimensional Euclidean space is the set of base vectors $\{\hat{\boldsymbol x},\hat{\boldsymbol y},\hat{\boldsymbol z}\}$. The base vectors are of unit length each and in the given order they form a right-handed system. We can write the position vector $\boldsymbol r$ as the linear combination of the base vectors,

$$
\boldsymbol r = x\hat{\boldsymbol x} + y\hat{\boldsymbol y} + z\hat{\boldsymbol z}.
$$

It is customary in the Earth Sciences to let the positive $\hat{\boldsymbol z}$-axis point downward, as depicted in {numref}`fig-cartframe`.

```{figure} figures/Cartframe.png
:name: fig-cartframe
:width: 60%

The Cartesian reference frame, its base vectors, and a resulting vector to denote a point in space.
```

### Distance and the scalar product

The distance between any two points with position vectors $\boldsymbol r$ and $\boldsymbol r'$ is given by the scalar product of the distance vector,

$$
d(\boldsymbol r,\boldsymbol r') = \left[(\boldsymbol r-\boldsymbol r')\cdot(\boldsymbol r-\boldsymbol r')\right]^{1/2} = |\boldsymbol r-\boldsymbol r'|,
$$

where the scalar product of two vectors $\boldsymbol a$ and $\boldsymbol b$ is given by

$$
\boldsymbol a\cdot\boldsymbol b = a_x b_x + a_y b_y + a_z b_z .
$$

The notation for the scalar product is a dot between the two vectors, for which reason it is also known as the dot product. The scalar product of two vectors multiplies the lengths of the two vectors and scales the result by the cosine of the angle $\phi$ between these vectors, hence

$$
\boldsymbol a\cdot\boldsymbol b = |\boldsymbol a||\boldsymbol b|\cos(\phi).
$$

### Translation and rotation

Translation and rotation of the vector $\boldsymbol r$ are linear transformations, and the resulting vector $\boldsymbol r'$ is obtained from $\boldsymbol r$ by

$$
\boldsymbol r' = \hat{\boldsymbol e}_x(x-\lambda_x) + \hat{\boldsymbol e}_y(y-\lambda_y) + \hat{\boldsymbol e}_z(z-\lambda_z).
$$

Since distance should be invariant under rotation, only orthogonal tensors $\{\hat{\boldsymbol e}_x,\hat{\boldsymbol e}_y,\hat{\boldsymbol e}_z\}$ describe a rotation, and when these vectors have unit amplitude they span a base for the new frame of reference, in which case they are orthonormal vectors.

```{figure} figures/rotCartframe.png
:name: fig-rotcartframe
:width: 60%

The translation and rotation of the Cartesian reference frame.
```

### The vector product

Any two non-parallel vectors span a plane, and the direction perpendicular to that plane is obtained by the so-called vector product of these two vectors. It is written as

$$
\boldsymbol a\times\boldsymbol b = \hat{\boldsymbol x}(a_y b_z - a_z b_y) + \hat{\boldsymbol y}(a_z b_x - a_x b_z) + \hat{\boldsymbol z}(a_x b_y - a_y b_x),
$$

and the notation is to use a cross between the vectors, for which reason it is also known as the cross product. The geometrical interpretation is that the new vector has a length equal to the area spanned by the two vectors $\boldsymbol a$ and $\boldsymbol b$, and is directed perpendicular to the plane containing the two vectors according to the right-hand rule, hence

$$
\boldsymbol c = \boldsymbol a\times\boldsymbol b = |\boldsymbol a||\boldsymbol b|\sin(\phi)\,\hat{\boldsymbol n},
$$

where $\hat{\boldsymbol n}$ is the unit vector in the direction of $\boldsymbol c$, as depicted in {numref}`fig-crossprod`. This implies that the cross-product rule does not commute, hence

$$
\boldsymbol a\times\boldsymbol b \ne \boldsymbol b\times\boldsymbol a,
\qquad
\boldsymbol a\times\boldsymbol b = -\,\boldsymbol b\times\boldsymbol a .
$$

```{figure} figures/crossprod.png
:name: fig-crossprod
:width: 35%

The vector product of the two vectors $\boldsymbol a$ and $\boldsymbol b$ results in the vector $\boldsymbol c$ that is perpendicular to the plane containing the two vectors, according to the right-hand rule. The length of $\boldsymbol c$ is equal to the grey coloured area, which is the parallelogram spanned by the two vectors.
```

Because the vector product creates a coordinate system when applied to any two non-parallel vectors, it can also be used to create the base vectors of the right-handed Cartesian reference frame:

$$
\hat{\boldsymbol z} = \hat{\boldsymbol x}\times\hat{\boldsymbol y},
\qquad
\hat{\boldsymbol y} = \hat{\boldsymbol z}\times\hat{\boldsymbol x},
\qquad
\hat{\boldsymbol x} = \hat{\boldsymbol y}\times\hat{\boldsymbol z}.
$$

## Curvilinear coordinate systems

Apart from the Cartesian reference frame, which is a rectangular coordinate system, two coordinate systems are often employed that use curved base vectors. One is the cylindrical coordinate system and the other is the spherical coordinate system. The point shown in {numref}`fig-cartframe` is depicted in cylindrical and spherical coordinate systems in {numref}`fig-cylsphere`.

In a **cylindrical** coordinate system a point in 3D space is specified by its coordinates $(\varrho,\phi,z)$, where $\phi$ is measured from the $x$-axis perpendicular to the $(x,z)$-plane, which is then a plane of constant $\phi$. Hence, the curved base vector $\hat{\boldsymbol\phi}$ lies in the $(x,y)$-plane. The surface of constant $\varrho$ is the boundary surface of the cylinder, which is the cylindrical $(\phi,z)$-surface, and the plane of constant $z$ is the circular cross-section of the cylinder, which is the $(\varrho,\phi)$-plane.

In a **spherical** coordinate system a point in 3D space is specified by its coordinates $(r,\phi,\theta)$, where $\phi$ is measured from the $x$-axis to the projection of the point onto the $(x,y)$-plane. The plane of constant $\phi$ is the $(r,\theta)$-plane. The surface of constant $r$ is the boundary surface of the ball with radius $r$, which is the spherical $(\phi,\theta)$-surface, and the surface of constant $\theta$ is the conical cross-section of the ball with radius $r$, whose intersection with the spherical surface is a circle; this is the $(r,\phi)$-surface.

From these descriptions the coordinate values are easily transformed to the rectangular coordinate system from the cylindrical and spherical coordinate systems and vice versa, as shown in {numref}`tab-coord-transform`. Note that the radial vectors $\hat{\boldsymbol\varrho}$ and $\hat{\boldsymbol r}$ in the cylindrical and spherical coordinate systems are **not** the same.

```{figure} figures/cylsphere.png
:name: fig-cylsphere
:width: 100%

The Cartesian reference frame together with the cylindrical (left) and spherical (right) coordinate systems, their base vectors, and a resulting vector to denote a point in space. In the figure the cylindrical radius is drawn as $r$; in the text it is written $\varrho$.
```

```{list-table} Spatial coordinate transformations.
:header-rows: 1
:name: tab-coord-transform

* - Cylindrical to rectangular
  - Spherical to rectangular
* - $x = \varrho\cos(\phi)$
  - $x = r\cos(\phi)\sin(\theta)$
* - $y = \varrho\sin(\phi)$
  - $y = r\sin(\phi)\sin(\theta)$
* - $z = z$
  - $z = r\cos(\theta)$
* - **Rectangular to cylindrical**
  - **Rectangular to spherical**
* - $\varrho = \sqrt{x^2+y^2},\quad \varrho\ge 0$
  - $r = \sqrt{x^2+y^2+z^2},\quad r\ge 0$
* - $\phi = \mathrm{atan}(y/x),\quad -\pi<\phi\le\pi$
  - $\phi = \mathrm{atan}(y/x),\quad -\pi<\phi\le\pi$
* - $z = z$
  - $\theta = \mathrm{atan}\!\left(\dfrac{\sqrt{x^2+y^2}}{z}\right),\quad 0\le\theta\le\pi$
```

To cover the full range $-\pi<\phi\le\pi$, the two-argument arctangent $\mathrm{atan2}(y,x)$ must be used, because $\mathrm{atan}(y/x)$ alone cannot distinguish the second and third quadrants from the fourth and first. The same holds for $\theta$, where the sign of $z$ decides between the upper and lower hemisphere.

The rectangular components $v_x,v_y,v_z$ of a vector function $\boldsymbol v$ at a point $\boldsymbol r$ with spherical components $v_r,v_\phi,v_\theta$ are given by

$$
\begin{aligned}
v_x &= v_r\cos(\phi)\sin(\theta) - v_\phi\sin(\phi) + v_\theta\cos(\phi)\cos(\theta), \\
v_y &= v_r\sin(\phi)\sin(\theta) + v_\phi\cos(\phi) + v_\theta\sin(\phi)\cos(\theta), \\
v_z &= v_r\cos(\theta) - v_\theta\sin(\theta).
\end{aligned}
$$ (eq:sph2cart-components)

In these relations the direction cosines occur from projections of spherical coordinates to rectangular coordinates. Projections are described by scalar products, hence the direction cosines are the results of the scalar products of the base vectors in two different coordinate systems. All direction cosines between the three coordinate systems are given in {numref}`tab-direction-cosines`. The upper-right diagonal entries are left empty and return as an exercise below.

```{list-table} Direction cosines from base vector scalar products. Columns 1–3 are the Cartesian base vectors, columns 4–6 the cylindrical ones, and columns 7–9 the spherical ones; the rows follow the same order. Entries above the diagonal are left open (see the exercises).
:header-rows: 1
:name: tab-direction-cosines

* -
  - $\hat{\boldsymbol x}$
  - $\hat{\boldsymbol y}$
  - $\hat{\boldsymbol z}$
  - $\hat{\boldsymbol\varrho}$
  - $\hat{\boldsymbol\phi}$
  - $\hat{\boldsymbol z}$
  - $\hat{\boldsymbol r}$
  - $\hat{\boldsymbol\phi}$
  - $\hat{\boldsymbol\theta}$
* - $\hat{\boldsymbol x}$
  - $1$
  - –
  - –
  - –
  - –
  - –
  - –
  - –
  - –
* - $\hat{\boldsymbol y}$
  - $0$
  - $1$
  - –
  - –
  - –
  - –
  - –
  - –
  - –
* - $\hat{\boldsymbol z}$
  - $0$
  - $0$
  - $1$
  - –
  - –
  - –
  - –
  - –
  - –
* - $\hat{\boldsymbol\varrho}$
  - $\cos(\phi)$
  - $\sin(\phi)$
  - $0$
  - $1$
  - –
  - –
  - –
  - –
  - –
* - $\hat{\boldsymbol\phi}$
  - $-\sin(\phi)$
  - $\cos(\phi)$
  - $0$
  - $0$
  - $1$
  - –
  - –
  - –
  - –
* - $\hat{\boldsymbol z}$
  - $0$
  - $0$
  - $1$
  - $0$
  - $0$
  - $1$
  - –
  - –
  - –
* - $\hat{\boldsymbol r}$
  - $\cos(\phi)\sin(\theta)$
  - $\sin(\phi)\sin(\theta)$
  - $\cos(\theta)$
  - $\sin(\theta)$
  - $0$
  - $\cos(\theta)$
  - $1$
  - –
  - –
* - $\hat{\boldsymbol\phi}$
  - $-\sin(\phi)$
  - $\cos(\phi)$
  - $0$
  - $0$
  - $1$
  - $0$
  - $0$
  - $1$
  - –
* - $\hat{\boldsymbol\theta}$
  - $\cos(\phi)\cos(\theta)$
  - $\sin(\phi)\cos(\theta)$
  - $-\sin(\theta)$
  - $\cos(\theta)$
  - $0$
  - $-\sin(\theta)$
  - $0$
  - $0$
  - $1$
```

The vector $\boldsymbol v$ is expressed in spherical coordinates as

$$
\boldsymbol v = v_r\hat{\boldsymbol r} + v_\phi\hat{\boldsymbol\phi} + v_\theta\hat{\boldsymbol\theta}.
$$

## Exercises

1. What is the length of the vector function $\boldsymbol v$?
2. Show that $\hat{\boldsymbol x} = \partial\boldsymbol r/\partial x$.
3. A two-dimensional rectangle in the plane $z=0$ is spanned by the two vectors $\boldsymbol d_x = d_x\hat{\boldsymbol x}$ and $\boldsymbol d_y = d_y\hat{\boldsymbol y}$, where $d_x$ and $d_y$ are the lengths in the $x$- and $y$-directions, respectively, and $\hat{\boldsymbol n}$ is the unit normal on the rectangle pointing in the positive $z$-direction. Give a geometrical interpretation of the product $\hat{\boldsymbol n}\cdot(\boldsymbol d_x\times\boldsymbol d_y)$.
4. A three-dimensional rectangle, a brick, with dimensions $d_x,d_y,d_z$ is spanned by the three vectors $\boldsymbol d_x = d_x\hat{\boldsymbol x}$, $\boldsymbol d_y = d_y\hat{\boldsymbol y}$ and $\boldsymbol d_z = d_z\hat{\boldsymbol z}$. Give a geometrical interpretation of the product $\boldsymbol d_x\cdot(\boldsymbol d_y\times\boldsymbol d_z)$.
5. Consider a smooth surface $\mathbb{S}$ with unique unit normal vector $\hat{\boldsymbol n}$. Show that any vector quantity $\boldsymbol H$ can be composed as $\boldsymbol H = (\hat{\boldsymbol n}\cdot\boldsymbol H)\hat{\boldsymbol n} + (\hat{\boldsymbol n}\times\boldsymbol H)\times\hat{\boldsymbol n}$ and give a geometric interpretation of the two terms.
6. A smooth surface $\mathbb{S}$ has a unique unit normal vector $\hat{\boldsymbol n}$. Decompose the gradient operator into a part tangential and a part normal to the surface $\mathbb{S}$.
7. Use the same reasoning as in the exercise above and find $\hat{\boldsymbol r} = A_r\,\partial\boldsymbol r/\partial r$, $\hat{\boldsymbol\phi} = A_\phi\,\partial\boldsymbol r/\partial\phi$, and $\hat{\boldsymbol\theta} = A_\theta\,\partial\boldsymbol r/\partial\theta$. Carry out the differentiations and find the coefficients $(A_r,A_\phi,A_\theta)$ by requiring that these vectors have unit length. These results should lead to an expression for the unit vectors of the spherical coordinate system in Cartesian coordinates.
8. The upper right-hand side of the matrix of {numref}`tab-direction-cosines` is left empty. The $3\times3$ block in the bottom-left corner of the table relates the unit vectors of the spherical reference frame to those of the Cartesian reference frame. Suppose we write this as

    $$
    \left(\begin{array}{c} \hat{\boldsymbol r} \\ \hat{\boldsymbol\phi} \\ \hat{\boldsymbol\theta}\end{array}\right)
    = \mathsf{R}\left(\begin{array}{c} \hat{\boldsymbol x} \\ \hat{\boldsymbol y} \\ \hat{\boldsymbol z}\end{array}\right),
    $$ (eq:sphCar)

    $$
    \mathsf{R} = \left(\begin{array}{ccc}
    \cos(\phi)\sin(\theta) & \sin(\phi)\sin(\theta) & \cos(\theta) \\
    -\sin(\phi) & \cos(\phi) & 0 \\
    \cos(\phi)\cos(\theta) & \sin(\phi)\cos(\theta) & -\sin(\theta)
    \end{array}\right).
    $$

    Show that

    $$
    \left(\begin{array}{c} \hat{\boldsymbol x} \\ \hat{\boldsymbol y} \\ \hat{\boldsymbol z}\end{array}\right)
    = \mathsf{R}^{t}\left(\begin{array}{c} \hat{\boldsymbol r} \\ \hat{\boldsymbol\phi} \\ \hat{\boldsymbol\theta}\end{array}\right),
    $$

    where $\mathsf{R}^{t}$ denotes the transpose of $\mathsf{R}$. Then show that $\mathsf{R}\mathsf{R}^{t} = \mathsf{I}$, where $\mathsf{I}$ is the $3\times3$ unit matrix, implying that the transpose of $\mathsf{R}$ is equal to its inverse. This follows from the fact that $\mathsf{R}$ is a matrix of orthonormal vectors and is therefore an orthonormal matrix.
9. Give explicit expressions for the base vectors of the spherical reference frame by carrying out the matrix-vector multiplication of {eq}`eq:sphCar`. Notice that all three base vectors depend on both angles. This implies that the base vectors are not constant but depend on position! The spherical reference frame is not an inertial frame.
10. Carry out the following differentiations: $\partial\hat{\boldsymbol r}/\partial\theta$, $\partial\hat{\boldsymbol\theta}/\partial\theta$, $\partial\hat{\boldsymbol\phi}/\partial\theta$ and $\partial\hat{\boldsymbol r}/\partial\phi$, $\partial\hat{\boldsymbol\theta}/\partial\phi$, $\partial\hat{\boldsymbol\phi}/\partial\phi$.
