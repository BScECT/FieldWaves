# Poisson's and Laplace's Equations

The continuous-density potential introduced in Equation {eq}`eq:continuous-mass-gravitational-potential`,

$$
\Phi(\vec{r})
=-G\int_V\frac{\rho(\vec{r'})}{|\vec{r}-\vec{r'}|}\,\mathrm{d}V'
$$

relates the gravitational potential at one point to the mass distribution throughout space. If we were merely interested in Earth's gravity field, we could now make the problem harder by considering a non-spherical Earth. We could start with an ellipsoid, use some trigonometric relations and use series expansions and patiently develop a fairly complex and accurate model of the gravity field. Instead of that, what we will do now is do introduce mathematical tools that allow us to set up the equations from which we can solve a general gravity (or another conservative potential fiedl): the Poisson's and Laplace's equations. The Poisson equation gives us the set of Partial Differential Equations (PDEs) describing the **local** relation between the potential and the mass-density. The Laplace equation describes the special case at points where the mass density is zero.

## The Laplacian

The Laplacian of a scalar field is, by definition, the divergence of its gradient:

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

```{admonition} Laplacian in spherical and cylindrical coordinates
:class: note

In spherical coordinates $(r,\theta,\varphi)$, where $\theta$ is the polar angle measured from the positive $z$-axis and $\varphi$ is the azimuthal angle,

$$
\begin{aligned}
\nabla^2\Phi
={}&\frac{1}{r^2}\frac{\partial}{\partial r}
\left(r^2\frac{\partial\Phi}{\partial r}\right)\\
&+\frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}
\left(\sin\theta\frac{\partial\Phi}{\partial\theta}\right)
+\frac{1}{r^2\sin^2\theta}\frac{\partial^2\Phi}{\partial\varphi^2}.
\end{aligned}
$$

For a spherically symmetric potential, $\Phi=\Phi(r)$, the angular derivatives vanish and only the radial term remains:

$$
\nabla^2\Phi
=\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}
\left(r^2\frac{\mathrm{d}\Phi}{\mathrm{d}r}\right).
$$

In cylindrical coordinates $(s,\varphi,z)$, where $s$ is the perpendicular distance from the $z$-axis,

$$
\nabla^2\Phi
=\frac{1}{s}\frac{\partial}{\partial s}
\left(s\frac{\partial\Phi}{\partial s}\right)
+\frac{1}{s^2}\frac{\partial^2\Phi}{\partial\varphi^2}
+\frac{\partial^2\Phi}{\partial z^2}.
$$

If the potential is rotationally symmetric and does not vary along the axis, as for the infinite-cylinder example, $\Phi=\Phi(s)$ and

$$
\nabla^2\Phi
=\frac{1}{s}\frac{\mathrm{d}}{\mathrm{d}s}
\left(s\frac{\mathrm{d}\Phi}{\mathrm{d}s}\right).
$$

The symbol $s$ is used here for cylindrical radius to avoid confusing it with the mass density $\rho$.
```

The gradient measures how the potential changes in space. Taking its divergence asks whether those changes produce a net outward or inward flux around a point. The Laplacian therefore measures the local curvature of the potential field.

## A physical two-dimensional example

Consider an infinitely long cylinder of radius $R$ and uniform density $\rho_0$, aligned with the $z$-axis. The mass per unit length is

$$
\lambda=\pi R^2\rho_0.
$$

Because the source does not change along $z$, neither the potential nor the gravity field depends on $z$, which implies that al partial derivatives with respect to $z$ are zero. The three-dimensional Laplacian therefore reduces  to

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

Let us first return to the exterior of a spherically symmetric body. On a spherical surface $S_r$ of radius $r>R$, the gravity field is

$$
\vec{g}=-\frac{GM}{r^2}\hat{r}.
$$

To picture the flux, imagine covering the spherical surface with a mosaic of very small patches. Attach an arrow to each patch that points perpendicular to the surface and out of the sphere. This is the area vector

$$
\mathrm{d}\vec{A}=\hat{r}\,\mathrm{d}A.
$$

Its direction describes the orientation of the patch, while its length represents the patch area. The dot product $\vec{g}\cdot\mathrm{d}\vec{A}$ measures how much of the gravity field passes through that patch. A field pointing straight out gives positive flux, a field pointing straight in gives negative flux, and a field tangent to the surface gives no flux because it does not cross the surface.

```{figure} figures/gravitational_flux_surface_patch.svg
:name: gravitational-flux-surface-patch
:width: 92%

A two-dimensional slice through the spherical surface. The highlighted arc represents a small surface patch. Its area vector $\mathrm{d}\vec{A}$ is perpendicular to the surface and points outwards, while the gravity field $\vec{g}$ points inwards towards the mass. The vectors are antiparallel, so $\vec{g}\cdot\mathrm{d}\vec{A}<0$: gravity enters rather than leaves the enclosed volume.
```

For the spherical surface, every area arrow points outwards and every gravity arrow points directly inwards. The two vectors are antiparallel at every patch, so

$$
\vec{g}\cdot\mathrm{d}\vec{A}
=-\frac{GM}{r^2}\,\mathrm{d}A.
$$

The total flux is obtained by adding the contributions from all the small patches:

$$
\begin{aligned}
\oint_{S_r}\vec{g}\cdot\mathrm{d}\vec{A}
&=-\frac{GM}{r^2}\oint_{S_r}\mathrm{d}A\\
&=-\frac{GM}{r^2}\left(4\pi r^2\right)\\
&=-4\pi GM.
\end{aligned}
$$ (eq:spherical-gravitational-flux)

```{admonition} Visualizing the cancellation
:class: tip

Imagine inflating the spherical surface like a transparent balloon while leaving the mass at its centre. As the radius increases, each gravity arrow becomes shorter as $1/r^2$. At the same time, a fixed cone drawn from the centre intercepts a patch whose area grows as $r^2$.

If the cone subtends a small solid angle $\mathrm{d}\Omega$, the patch area is

$$
\mathrm{d}A=r^2\,\mathrm{d}\Omega.
$$

The flux through that patch is therefore

$$
\mathrm{d}\mathcal{F}
=-\frac{GM}{r^2}\mathrm{d}A
=-GM\,\mathrm{d}\Omega.
$$

The field has become weaker, but it acts across a proportionally larger patch. Each cone carries the same flux through every concentric sphere. The complete sphere contains a total solid angle of $4\pi$, giving $\mathcal{F}=-4\pi GM$.
```

The flux is consequently independent of the radius of the spherical surface. For a concentric surface inside a spherically symmetric body, the same calculation applies with $M$ replaced by the enclosed mass $M_{\mathrm{enc}}(r)$.

This result is more general than the spherical calculation suggests. For any closed surface $S$, of any shape, the net gravitational flux depends only on the total mass enclosed by that surface:

$$
\oint_S \vec{g}\cdot\mathrm{d}\vec{A}
=-4\pi G M_{\mathrm{enc}}.
$$ (eq:gauss-law-gravity-integral)

This is **Gauss's law for gravity**. One way to visualize the generalization is to imagine deforming the transparent spherical balloon into an irregular closed shape without moving it across the mass. The gravity arrows are no longer perpendicular to every patch, and their strengths vary across the surface. However, the dot product automatically counts only the component crossing each patch. The same cones from the mass now meet tilted patches at different distances, but their total solid angle remains $4\pi$, so the total flux does not change.

Mass inside the surface therefore contributes a net inward flux. A mass outside the surface produces no net flux: its field enters the volume through some patches and leaves through others, and those contributions cancel. Because gravitational fields obey superposition, the result extends from individual point masses to arbitrary mass distributions. The area vector $\mathrm{d}\vec{A}$ always points outwards, so the inward flux produced by positive mass is negative.

### The divergence theorem

Before writing another equation, let us start with the physical idea. Imagine surrounding a region with a closed, transparent boundary and observing a net flux passing out through it. That flux cannot simply appear at the boundary: it must emerge from somewhere inside the enclosed volume. Conversely, if more field enters than leaves, something inside behaves as a sink.

Recall from the earlier chapter on [gradient, divergence, and curl](../../1_gradient_divergence_curl/intro.md) that the divergence $\vec{\nabla}\cdot\vec{u}$ measures this local balance for a vector field $\vec{u}$:

- positive divergence means that, locally, more field leaves than enters, like a source;
- negative divergence means that more field enters than leaves, like a sink;
- zero divergence means that there is no net production or absorption at that point.

Now imagine dividing the complete volume into many tiny cells. The divergence in each cell tells us its small net outward flux. When we add the fluxes from all cells, every shared internal face appears twice: flux leaving one cell enters its neighbour through the same face. These internal contributions cancel pair by pair. Only the flux through the outer boundary remains.

This is the idea expressed mathematically by the **divergence theorem**. For any sufficiently smooth vector field $\vec{u}$ in a volume $V$ bounded by the closed surface $S=\partial V$,

$$
\boxed{
\oint_{\partial V}\vec{u}\cdot\mathrm{d}\vec{A}
=\int_V\vec{\nabla}\cdot\vec{u}\,\mathrm{d}V.
}
$$ (eq:divergence-theorem)

The left-hand side measures the net outward flux through the boundary. The right-hand side adds up all the local sources and sinks inside the volume. The equality follows from the cancellation of the internal faces: all net flux crossing the outer boundary must be accounted for by the divergence somewhere inside.

For gravity, positive mass behaves as a **sink** of the gravity field rather than a source: the field arrows converge towards the mass. We should therefore expect $\vec{\nabla}\cdot\vec{g}$ to be negative wherever positive mass density is present.

Applying the divergence theorem to the gravity field gives

$$
\oint_{\partial V}\vec{g}\cdot\mathrm{d}\vec{A}
=\int_V\vec{\nabla}\cdot\vec{g}\,\mathrm{d}V.
$$

Gauss's law supplies the value of the surface integral, while the enclosed mass can be written as

$$
M_{\mathrm{enc}}=\int_V\rho\,\mathrm{d}V.
$$

Combining these relations gives

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

For example, the potential outside a spherically symmetric body is

$$
\Phi(r)=-\frac{GM}{r}.
$$

Because of the spherical symmetry it is natural to evaluate its Laplacian in spherical coordinates, which reduces to

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
