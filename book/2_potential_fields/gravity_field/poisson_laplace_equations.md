# Poisson's and Laplace's Equations

The continuous-density potential introduced in Equation {eq}`eq:continuous-mass-gravitational-potential`,

$$
\Phi(\vec{r})
=-G\int_V\frac{\rho(\vec{r'})}{|\vec{r}-\vec{r'}|}\,\mathrm{d}V'
$$

relates the gravitational potential at one point to the mass distribution throughout space. There is also a **local** relation between the potential and the density. This relation is Poisson's equation.

## The Laplacian

The Laplacian of a scalar field is the divergence of its gradient:

$$
\nabla^2\Phi
=\vec{\nabla}\cdot\left(\vec{\nabla}\Phi\right).
$$ (eq:scalar-laplacian-definition)

In Cartesian coordinates,

$$
\nabla^2\Phi
=\frac{\partial^2\Phi}{\partial x^2}
+\frac{\partial^2\Phi}{\partial y^2}
+\frac{\partial^2\Phi}{\partial z^2}.
$$ (eq:scalar-laplacian-cartesian)

The gradient measures how the potential changes in space. Taking its divergence asks whether those changes produce a net outward or inward flux around a point. The Laplacian therefore measures the local curvature of the potential field.

## A physical two-dimensional example

Consider an infinitely long cylinder of radius $R$ and uniform density $\rho_0$, aligned with the $z$-axis. The mass per unit length is

$$
\lambda=\pi R^2\rho_0.
$$

Because the source does not change along $z$, neither the potential nor the gravity field depends on $z$. The three-dimensional Laplacian therefore reduces exactly to

$$
\nabla^2\Phi
=\frac{\partial^2\Phi}{\partial x^2}
+\frac{\partial^2\Phi}{\partial y^2}.
$$ (eq:two-dimensional-laplacian)

This makes a cross-section through the cylinder a genuinely two-dimensional physical problem. Choosing the surface value $\Phi(R)=0$, the potential is

$$
\Phi(r)=
\begin{cases}
G\lambda\left(\dfrac{r^2}{R^2}-1\right), & 0\leq r\leq R,\\[6pt]
2G\lambda\ln\left(\dfrac{r}{R}\right), & r\geq R.
\end{cases}
$$ (eq:uniform-cylinder-potential)

Unlike the potential of a bounded mass, this potential cannot be chosen to vanish at infinity: an infinite cylinder has infinite total mass, and its exterior potential grows logarithmically. Only potential differences have physical significance.

The corresponding gravity field is directed towards the axis,

$$
\vec{g}(\vec{r})=
\begin{cases}
-\dfrac{2G\lambda}{R^2}\left(x\hat{x}+y\hat{y}\right), & r\leq R,\\[8pt]
-\dfrac{2G\lambda}{r^2}\left(x\hat{x}+y\hat{y}\right), & r\geq R.
\end{cases}
$$ (eq:uniform-cylinder-gravity)

```{figure} figures/uniform_cylinder_laplacian.png
:name: uniform-cylinder-laplacian
:width: 100%

Cross-section of a uniform infinite cylinder. Left: gravitational potential $\Phi$ and gravity field $\vec{g}=-\vec{\nabla}\Phi$. Arrow direction shows the inward attraction, while arrow length indicates field strength. Right: the two-dimensional Laplacian calculated numerically from the potential. It is $4\pi G\rho_0$ inside the matter and zero outside, apart from finite-grid smoothing near the boundary. The calculation is available in the accompanying {doc}`uniform_cylinder_laplacian` notebook.
```

The potential varies both inside and outside the cylinder, but its Laplacian distinguishes the two regions. Inside, where mass is present,

$$
\nabla^2\Phi=4\pi G\rho_0,
$$

whereas outside, where $\rho=0$, the positive and negative curvatures in different directions cancel and $\nabla^2\Phi=0$. The Laplacian is therefore not simply a measure of whether a surface is curved: it measures the **net** curvature obtained by adding the second derivatives in all coordinate directions.

## From gravitational flux to Poisson's equation

For any closed surface $S$, the gravitational flux depends on the mass enclosed by that surface:

$$
\oint_S \vec{g}\cdot\mathrm{d}\vec{A}
=-4\pi G M_{\mathrm{enc}}.
$$ (eq:gauss-law-gravity-integral)

The area vector $\mathrm{d}\vec{A}$ points outwards. Since gravity points towards positive mass, the flux is negative. Writing the enclosed mass as a volume integral and applying the divergence theorem gives

$$
\int_V \left(\vec{\nabla}\cdot\vec{g}\right)\mathrm{d}V
=-4\pi G\int_V\rho\,\mathrm{d}V.
$$

Because this relation holds for any volume $V$, the integrands must be equal:

$$
\vec{\nabla}\cdot\vec{g}
=-4\pi G\rho.
$$ (eq:gauss-law-gravity-differential)

Using $\vec{g}=-\vec{\nabla}\Phi$, we obtain

$$
-\vec{\nabla}\cdot\left(\vec{\nabla}\Phi\right)
=-4\pi G\rho,
$$

or

$$
\boxed{\nabla^2\Phi=4\pi G\rho.}
$$ (eq:gravitational-poisson-equation)

This is **Poisson's equation for gravity**. It says that mass density is the source of the gravitational potential. The positive sign on the right-hand side follows from our conventions $\Phi=-GM/r$ and $\vec{g}=-\vec{\nabla}\Phi$.

```{admonition} Reading the equation
:class: tip

Poisson's equation relates two quantities evaluated at the same position:

$$
\rho(\vec{r})
=\frac{1}{4\pi G}\nabla^2\Phi(\vec{r}).
$$

It can therefore be read in two directions. Given a density distribution and suitable boundary conditions, we can calculate the potential. Conversely, sufficiently detailed knowledge of the potential throughout a volume gives information about the density there. In practice, gravity is often measured only on or above Earth's surface, which makes the inverse problem much less direct.
```

## Laplace's equation in empty space

In a region containing no mass, $\rho=0$, and Poisson's equation reduces to

$$
\boxed{\nabla^2\Phi=0.}
$$ (eq:gravitational-laplace-equation)

This is **Laplace's equation**. A field satisfying Laplace's equation is called **harmonic**. The equation applies in any source-free region, even if masses outside that region produce a non-zero potential and gravity field within it.

For example, the potential outside a spherical body is

$$
\Phi(r)=-\frac{GM}{r}.
$$

For a spherically symmetric scalar field, the Laplacian is

$$
\nabla^2\Phi
=\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}
\left(r^2\frac{\mathrm{d}\Phi}{\mathrm{d}r}\right).
$$ (eq:radial-scalar-laplacian)

Consequently, for $r>R$,

$$
\nabla^2\left(-\frac{GM}{r}\right)
=\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}
\left[r^2\frac{\mathrm{d}}{\mathrm{d}r}
\left(-\frac{GM}{r}\right)\right]
=\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}(GM)
=0.
$$

The potential is not constant and the gravity field is not zero, yet Laplace's equation is satisfied because there is no mass in the exterior region. For a point mass, the origin itself must be excluded from this calculation: that is precisely where the source is located and where $-GM/r$ is singular.

## Checking the uniform sphere

Inside the uniform sphere, Equation {eq}`eq:uniform-sphere-potential` gives

$$
\Phi(r)
=-\frac{GM}{2R}\left(3-\frac{r^2}{R^2}\right).
$$

Applying the radial Laplacian gives

$$
\begin{aligned}
\nabla^2\Phi
&=\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}
\left(r^2\frac{GM}{R^3}r\right)\\
&=\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}
\left(\frac{GM}{R^3}r^3\right)
=\frac{3GM}{R^3}.
\end{aligned}
$$

Using $M=4\pi\rho_0R^3/3$, this becomes

$$
\nabla^2\Phi=4\pi G\rho_0,
$$

as required by Poisson's equation. The same potential therefore satisfies Poisson's equation inside the matter and Laplace's equation outside it.

At the surface of an ordinary body with a finite density, $\Phi$ and the normal component of $\vec{g}$ remain continuous, although the second derivatives of $\Phi$ need not be continuous. This is why the uniform-sphere solutions join continuously at $r=R$. An idealized infinitely thin surface layer requires more care because it concentrates mass directly on the boundary.

## Why these equations are useful

The integral formulation adds the contribution from every mass element directly. Poisson's and Laplace's equations offer a different strategy: solve a differential equation in each region and use physical boundary conditions to connect the solutions. Typically, we specify that

- $\Phi$ approaches zero far from a bounded mass distribution;
- $\Phi$ remains finite wherever there is no point-like source;
- $\Phi$ is continuous across material boundaries;
- the resulting field $\vec{g}=-\vec{\nabla}\Phi$ has the required symmetry and boundary behaviour.

This approach becomes especially powerful for layered bodies and for regions where the density vanishes. Much of the difficulty shifts from carrying out a volume integral to finding the solution of a differential equation that satisfies the geometry and boundary conditions.

```{admonition} Exercise: identifying the governing equation
:class: exercise

Consider the uniform thick shell from the previous section.

1. State whether $\Phi$ satisfies Poisson's equation or Laplace's equation in the cavity, in the shell material, and outside the shell.
2. The gravity field vanishes in the cavity. What does this imply about the potential there?
3. Explain why the potential in the cavity need not be zero.
4. Use Equation {eq}`eq:radial-scalar-laplacian` to show that the most general spherically symmetric solution of Laplace's equation is

   $$
   \Phi(r)=A+\frac{B}{r}.
   $$

5. Which value of $B$ is allowed in a source-free region containing the centre? Which value of $A$ is allowed in an exterior region where $\Phi\rightarrow0$ at infinity?
```
