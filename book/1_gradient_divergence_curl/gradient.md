# Gradient of a scalar field

Let us consider a scalar field, which is a function of the three spatial coordinates and possibly of time $t$. We write it as $p(x,y,z,t)$ in Cartesian coordinates. A scalar field quantity has a value represented by a single number at every point in space and at each time instant. You can think of the temperature in the room, or the air pressure in our atmosphere, or the density of mass inside the Earth.

Such fields possess iso-surfaces. An **iso-surface** is the collection of points in space where the field has a constant value. The gradient of the field quantity points perpendicular to that iso-surface. Let us investigate how that result is found. The gradient is a partial differential operator given by

$$
\nabla = \left(\begin{array}{c}
\dfrac{\partial}{\partial x} \\[2mm]
\dfrac{\partial}{\partial y} \\[2mm]
\dfrac{\partial}{\partial z}
\end{array}\right)
= \hat{\boldsymbol x}\frac{\partial}{\partial x} + \hat{\boldsymbol y}\frac{\partial}{\partial y} + \hat{\boldsymbol z}\frac{\partial}{\partial z}
= \hat{\boldsymbol x}\partial_x + \hat{\boldsymbol y}\partial_y + \hat{\boldsymbol z}\partial_z .
$$

We use the short-hand notation for each scalar partial derivative, e.g. $\partial_x$ for the derivative with respect to $x$. If we apply the gradient to the scalar field quantity $p(x,y,z,t)$ we obtain a vector field quantity that we can write as

$$
\nabla p(x,y,z,t) = \hat{\boldsymbol x}\,\partial_x p(x,y,z,t) + \hat{\boldsymbol y}\,\partial_y p(x,y,z,t) + \hat{\boldsymbol z}\,\partial_z p(x,y,z,t).
$$ (eq:gradp)

## The gradient of the distance function

To get an idea about what this implies, let us consider the position vector $\boldsymbol r$ introduced with the Cartesian reference frame. The vector $\boldsymbol r$ is the position vector of the point $(x,y,z)$ in space, which we write as

$$
\boldsymbol r = x\hat{\boldsymbol x} + y\hat{\boldsymbol y} + z\hat{\boldsymbol z},
$$

and its length is given by

$$
r = |\boldsymbol r| = \sqrt{x^2+y^2+z^2}.
$$

The iso-surface for $r$ has the shape of a spherical surface. We now evaluate each term in the gradient. We begin with the derivative with respect to the coordinate $x$ and obtain

$$
\begin{aligned}
\partial_x r &= \frac{1}{2}\frac{1}{\sqrt{x^2+y^2+z^2}}(2x), \\
             &= \frac{x}{\sqrt{x^2+y^2+z^2}}, \\
             &= \frac{x}{r}.
\end{aligned}
$$

We find similar results for the derivatives with respect to $y$ and $z$, and put them in the vector expression such that we end up with

$$
\begin{aligned}
\nabla r &= \hat{\boldsymbol x}\,\partial_x r(x,y,z) + \hat{\boldsymbol y}\,\partial_y r(x,y,z) + \hat{\boldsymbol z}\,\partial_z r(x,y,z), \\
         &= \frac{x\hat{\boldsymbol x} + y\hat{\boldsymbol y} + z\hat{\boldsymbol z}}{r}, \\
         &= \frac{\boldsymbol r}{r}.
\end{aligned}
$$ (eq:gradr)

From the final expression, we observe that the result is the normalised distance vector. This is what we call the outward unit normal to the spherical surface. It points away from the origin of the reference frame. The physical interpretation is that the gradient of the distance to the origin of the reference frame finds the direction in which the distance increases the most. The vector is placed perpendicular to the iso-surface of the function. We investigate whether this is a general property of the gradient.

Now let us take a different distance, namely relative to an arbitrary other point $\boldsymbol r'$ in space. In that case the displacement vector is given by

$$
\boldsymbol r-\boldsymbol r' = (x-x')\hat{\boldsymbol x} + (y-y')\hat{\boldsymbol y} + (z-z')\hat{\boldsymbol z},
$$

and the length of the vector is equal to the distance $d$ given by

$$
d(x-x',y-y',z-z') = |\boldsymbol r-\boldsymbol r'| = \sqrt{(x-x')^2+(y-y')^2+(z-z')^2}.
$$

Similar to the previous result, we now find

$$
\begin{aligned}
\nabla|\boldsymbol r-\boldsymbol r'| &= \hat{\boldsymbol x}\,\partial_x d + \hat{\boldsymbol y}\,\partial_y d + \hat{\boldsymbol z}\,\partial_z d, \\
&= \frac{(x-x')\hat{\boldsymbol x} + (y-y')\hat{\boldsymbol y} + (z-z')\hat{\boldsymbol z}}{|\boldsymbol r-\boldsymbol r'|},
\end{aligned}
$$

which we write in vector form as

$$
\nabla|\boldsymbol r-\boldsymbol r'| = \frac{\boldsymbol r-\boldsymbol r'}{|\boldsymbol r-\boldsymbol r'|}.
$$ (eq:gradd)

We find again an outward unit vector, pointing away from the point at $\boldsymbol r'$ and perpendicular to the spherical iso-surface.

## The total derivative and the direction of steepest increase

Now let us consider a field quantity $p(x,y,z,t)$ and assume we analyse this function for a single moment in time. The gradient of this function is expressed in {eq}`eq:gradp`. Let $\mathrm{d}p$ be the change in $p$ from a point $\boldsymbol r$ to another point $\boldsymbol r'$, which means that $p(\boldsymbol r)=p$ and $p(\boldsymbol r')=p+\mathrm{d}p$. We do not specify where $\boldsymbol r$ and $\boldsymbol r'$ are located, and they can be on different iso-surfaces or on the same one.

The change in $p$ due to a displacement in the $x$-direction from $\boldsymbol r$ to $\boldsymbol r'$ is given by $(\partial p/\partial x)\mathrm{d}x$, while keeping $y$ and $z$ constant. Similarly, the changes in $p$ due to displacements in the $y$- and $z$-directions are given by $(\partial p/\partial y)\mathrm{d}y$ and $(\partial p/\partial z)\mathrm{d}z$. Hence, the change in $p$ along the vector from $\boldsymbol r$ to $\boldsymbol r'$ is

$$
\mathrm{d}p = \partial_x p\,\mathrm{d}x + \partial_y p\,\mathrm{d}y + \partial_z p\,\mathrm{d}z.
$$

We can write this expression as a scalar product of two vectors,

$$
\mathrm{d}p = \left(\hat{\boldsymbol x}\partial_x p + \hat{\boldsymbol y}\partial_y p + \hat{\boldsymbol z}\partial_z p\right)\cdot\left(\hat{\boldsymbol x}\,\mathrm{d}x + \hat{\boldsymbol y}\,\mathrm{d}y + \hat{\boldsymbol z}\,\mathrm{d}z\right),
$$

where the symbol $\cdot$ is used to denote scalar multiplication of two vectors. We recognise this expression as

$$
\mathrm{d}p = (\nabla p)\cdot\mathrm{d}\boldsymbol r.
$$

Suppose there is an angle $\psi$ between the two vectors, then

$$
\mathrm{d}p = |\nabla p|\,|\mathrm{d}\boldsymbol r|\cos(\psi) = |\nabla p|\,\mathrm{d}r\cos(\psi),
$$

and we can write the total derivative with respect to $r$ as

$$
\frac{\mathrm{d}p}{\mathrm{d}r} = |\nabla p|\cos(\psi).
$$ (eq:totder)

The left-hand side of {eq}`eq:totder` means the rate of change along the path from $\boldsymbol r$ to $\boldsymbol r'$, as indicated by $r$. The right-hand side shows that this can never be larger than the magnitude of the gradient of $p$. We conclude that the rate of change is equal to the magnitude of the gradient only if the point $\boldsymbol r'$ is located along the resulting vector after taking the gradient of $p$, because then $\psi=0$. For all other locations the rate of change is less. We have seen this when we evaluated the gradient of the distance function $r$.

Now we have found that the magnitude of the gradient of a scalar field quantity is equal to the maximum rate of change of that field quantity with respect to position. What is left is direction, which is relatively easy to understand. It is clear that when the point $\boldsymbol r'$ is on the same iso-surface as the point $\boldsymbol r$, the rate of change is zero. We investigate differentials, which means we look at points $\boldsymbol r'$ that approach the point $\boldsymbol r$. The rate of change of the function $p$ is maximal when the point $\boldsymbol r'$ moves away in the direction perpendicular to the iso-surface. If there is a part of the path from $\boldsymbol r$ to $\boldsymbol r'$ that has a component along the iso-surface, there is no change along that part of the path, which would reduce the rate of change. Hence, the gradient results in a vector that points along the unit normal of the iso-surface in the direction where the rate is positive. We can express this as

$$
\nabla p(x,y,z,t) = |\nabla p(x,y,z,t)|\,\hat{\boldsymbol n},
$$

where $\hat{\boldsymbol n}$ is the unit normal vector on the iso-surface pointing to the positive rate of change.

:::{admonition} The gradient in words
:class: tip
The gradient of any scalar field quantity $p(x,y,z,t)$ finds the direction in which the scalar quantity increases the most, for a fixed moment in time, and its magnitude is that maximum rate of increase.
:::

## The gradient in curvilinear coordinates

Earlier we introduced the spherical and cylindrical coordinate systems. We had to look at the rotation matrices between the coordinate systems to be able to move back and forth. It is now time to generalise our notation of the gradient such that it can be used in spherical and cylindrical coordinate systems as well. Let us write

$$
\nabla p(x,y,z,t) = \sum_{i=1}^{3}\frac{1}{c_i}\frac{\partial p}{\partial x_i}\hat{\boldsymbol e}_i .
$$ (eq:gradgen)

In this expression the coefficients $c_i$ are scale factors, the coordinates are $(x_1,x_2,x_3)$, and both depend on the coordinate system we want to do our analysis in. The base vectors $(\hat{\boldsymbol e}_1,\hat{\boldsymbol e}_2,\hat{\boldsymbol e}_3)$ were introduced with the coordinate systems, and we use them here again, but we make them depend on the coordinate system as well.

In the Cartesian frame these would be $(x_1,x_2,x_3)=(x,y,z)$, $(c_1,c_2,c_3)=(1,1,1)$ and $(\hat{\boldsymbol e}_1,\hat{\boldsymbol e}_2,\hat{\boldsymbol e}_3)=(\hat{\boldsymbol x},\hat{\boldsymbol y},\hat{\boldsymbol z})$. Now, in spherical coordinates, we already know all the ingredients, so we can fill them in. We find $(x_1,x_2,x_3)=(r,\theta,\phi)$, $(c_1,c_2,c_3)=(1,r,r\sin(\theta))$ and $(\hat{\boldsymbol e}_1,\hat{\boldsymbol e}_2,\hat{\boldsymbol e}_3)=(\hat{\boldsymbol r},\hat{\boldsymbol\theta},\hat{\boldsymbol\phi})$. Substituting these in {eq}`eq:gradgen` results in

$$
\nabla p(r,\theta,\phi) = \frac{\partial p}{\partial r}\hat{\boldsymbol r} + \frac{1}{r}\frac{\partial p}{\partial\theta}\hat{\boldsymbol\theta} + \frac{1}{r\sin(\theta)}\frac{\partial p}{\partial\phi}\hat{\boldsymbol\phi}.
$$ (eq:gradsph)

## Exercises

1. Evaluate $\nabla|\boldsymbol r|^{-1}$, $\nabla|\boldsymbol r|^{-n}$, $\nabla|\boldsymbol r-\boldsymbol r'|^{-1}$, and $\nabla\left(|\boldsymbol r-\boldsymbol a|^{-1} - |\boldsymbol r+\boldsymbol a|^{-1}\right)$, with $\boldsymbol a=(1,0,0)$. For each result, plot several iso-surfaces and plot the vectors that correspond to the gradients.
2. Instead of taking the gradient with respect to the point $\boldsymbol r$, we can take it with respect to $\boldsymbol r'$, which we write as $\nabla' = \hat{\boldsymbol x}\partial_{x'} + \hat{\boldsymbol y}\partial_{y'} + \hat{\boldsymbol z}\partial_{z'}$. Evaluate $\nabla'|\boldsymbol r-\boldsymbol r'|^{-1}$ and express it in terms of $\nabla|\boldsymbol r-\boldsymbol r'|^{-1}$.
3. We have seen that the outward unit normal of a spherical surface around the point $\boldsymbol r'$ is given by $\hat{\boldsymbol n} = \nabla|\boldsymbol r-\boldsymbol r'| = (\boldsymbol r-\boldsymbol r')/|\boldsymbol r-\boldsymbol r'|$. Use your understanding of the property of the gradient to explain why $\hat{\boldsymbol n}\cdot\nabla|\boldsymbol r-\boldsymbol r'|^{-1}<0$ for $\boldsymbol r\ne\boldsymbol r'$.
4. What is the relation between $A_r,A_\phi,A_\theta$ introduced in the exercises on coordinate systems and the scale factors $c_i$ here?
5. Determine the expression for the gradient in cylindrical coordinates. You can use the coordinates $(\varrho,\phi,z)$ to avoid confusion with the three-dimensional radius $r$ that is used in spherical coordinates and represents the distance between two points in 3D space in general. In cylindrical coordinates $r=\sqrt{\varrho^2+z^2}$.
