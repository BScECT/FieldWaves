# Postulating and Verifying Solutions to Laplace's Equation


Laplace's equation,

$$
\nabla^2 \Phi = 0,
$$

is a **partial differential equation (PDE)**: an equation that a function and its partial derivatives must satisfy. Unlike an algebraic equation, it does not determine a single value, and unlike an ordinary differential equation, the unknown is a function of several variables.

There are many functions that satisfy Laplace's equation. Finding the particular solution that describes a physical situation requires additional information about the geometry of the problem and the conditions at its boundaries.

Before developing systematic methods for solving PDEs, we will take a simpler approach: **postulate a physically plausible form for the potential and check whether it satisfies the equation**.

## A uniform gravitational field

Close to the surface of the Earth, and over sufficiently small distances, we often approximate the gravitational field as uniform,

$$
\vec{g} = -g\,\hat{z}.
$$

A potential corresponding to this field is

$$
\Phi(z)=gz,
$$

since

$$
\vec{g}=-\vec{\nabla}\Phi=-g\,\hat{z}.
$$

There is no mass in the region in which we are describing the field, so the potential should satisfy Laplace's equation. In Cartesian coordinates,

$$
\nabla^2\Phi
=
\frac{\partial^2\Phi}{\partial x^2}
+
\frac{\partial^2\Phi}{\partial y^2}
+
\frac{\partial^2\Phi}{\partial z^2}.
$$

For $\Phi=gz$, all three second derivatives vanish, and therefore

$$
\nabla^2\Phi=0.
$$

The familiar approximation of constant gravity near the Earth's surface is therefore consistent with Laplace's equation.

```{admonition} A solution belongs to a region
:class: important

The statement $\nabla^2\Phi=0$ does **not** mean that there are no masses producing the gravitational field. It means that there is no mass **in the region where we are solving the equation**.

The Earth's mass lies below us, while the potential in the space above the surface satisfies Laplace's equation.
```

## A gravity field that varies in space

A uniform gravitational field is a particularly simple case. Suppose instead that we postulate the potential

$$
\Phi(x,z)=A(x^2-z^2),
$$

where $A$ is a constant.

Does this represent a possible gravitational potential in a region containing no mass?

We can test the proposed solution directly:

$$
\frac{\partial^2\Phi}{\partial x^2}=2A,
$$

and

$$
\frac{\partial^2\Phi}{\partial z^2}=-2A.
$$

There is no dependence on $y$, so

$$
\nabla^2\Phi
=
2A-2A
=
0.
$$

The proposed potential is therefore a possible solution of Laplace's equation in a source-free region.

The corresponding gravitational field is

$$
\vec{g}
=
-\vec{\nabla}\Phi
=
-2Ax\,\hat{x}
+
2Az\,\hat{z}.
$$

Unlike the previous example, the gravitational field now changes with position even though there is no mass locally.

Such spatial variations of the gravitational field occur naturally when observing the field produced by distant masses. Locally, the first-order spatial variation of gravity is called a **gravity gradient** or **tidal field**.

```{exercise}
Verify that

$$
\Phi(x,z)=A(x^2+z^2)
$$

does *not* satisfy Laplace's equation.

What would Poisson's equation imply about the mass density in a region described by this potential?
```

## Superposition and perturbations

The examples above already give us more than two isolated solutions. Laplace's equation is **linear**: for any two functions $\Phi_1$ and $\Phi_2$ and any constants $a$ and $b$,

$$
\nabla^2\left(a\Phi_1+b\Phi_2\right)
=a\nabla^2\Phi_1+b\nabla^2\Phi_2.
$$

Therefore, if

$$
\nabla^2\Phi_1=0
\qquad\text{and}\qquad
\nabla^2\Phi_2=0,
$$

then

$$
\nabla^2\left(a\Phi_1+b\Phi_2\right)=0.
$$

This is the **principle of superposition**. Any linear combination of solutions is itself a solution. Even a single non-zero solution can be multiplied by infinitely many different constants, and combining different solutions produces still more possibilities. Laplace's equation therefore does not, by itself, select one potential from the infinitely many functions that satisfy it.

Superposition also gives us a useful physical interpretation of the previous example. In a small region near Earth's surface, we can neglect the curvature of Earth and take $z$ to be the local upward direction. The potential can then be written as a uniform background plus a smaller perturbation,

$$
\Phi_{\mathrm{total}}(x,z)
=gz+\delta\Phi(x,z),
$$

with gravity field

$$
\vec{g}_{\mathrm{total}}
=-g\,\hat{z}-\vec{\nabla}\delta\Phi.
$$

For example, $\delta\Phi=A(x^2-z^2)$ describes a local gravity gradient, or tidal perturbation, superimposed on the approximately uniform background field. The periodic gravity anomaly considered next will be interpreted in the same way: it is a perturbation caused by variations in the mass distribution, not the complete gravitational potential of Earth.

## Boundary conditions: selecting a physical solution

If Laplace's equation admits infinitely many solutions, what selects the one realized in a particular physical problem? We need to specify the **domain** in which we are solving the equation and provide information at its **boundaries**.

For a gravitational potential, we might know the value of the potential on a boundary, the component of the gravity field normal to that boundary, or how the potential behaves far from the sources. Such information is called a **boundary condition**. Together, the equation, domain, and boundary conditions define the physical problem:

$$
\boxed{
\text{differential equation}
+
\text{domain}
+
\text{boundary conditions}
\longrightarrow
\text{physical solution}.
}
$$

A proposed function that satisfies Laplace's equation is therefore only a possible solution. It becomes a solution to the physical problem only if it also satisfies the relevant boundary conditions.

## A periodic gravity anomaly

Now consider a more interesting problem. Imagine that the mass distribution below a locally flat reference surface at $z=0$ varies periodically in the $x$ direction. We might expect the resulting perturbation of the gravitational potential above it to have a similar horizontal variation.

Suppose that the anomaly at the reference surface is

$$
\delta\Phi(x,0)=A\cos(kx),
$$

and that its influence must vanish far above the source,

$$
\delta\Phi(x,z)\longrightarrow 0
\qquad\text{as}\qquad z\longrightarrow\infty.
$$

Let us therefore postulate

$$
\delta\Phi(x,z)
=
A e^{-\alpha z}\cos(kx),
$$

where $\alpha>0$ describes how rapidly the potential perturbation decreases with height. This proposed form already satisfies both boundary conditions. We have not yet shown, however, that it satisfies Laplace's equation.

```{admonition} Interpreting the wavenumber
:class: tip

The **wavenumber** $k$ measures how rapidly a periodic pattern varies in space. It is related to the horizontal wavelength by

$$
\lambda=\frac{2\pi}{k},
$$

so a large $k$ represents a short wavelength and a small $k$ a long wavelength.

In this static example, the sign of $k$ does not change the pattern because

$$
\cos(-kx)=\cos(kx).
$$

We can therefore choose $k>0$ without losing any possible solution. Later, when we describe travelling waves or use complex exponentials, the sign of the wavenumber will matter: together with the time dependence, it indicates the direction of propagation.
```

As you work more with the PDEs discussed in this course, you should come to expect exponentials, sines, and cosines to appear as building blocks of solutions. Here we have postulated such a combination and will now test it.

At this point we do **not** assume any relation between $k$ and $\alpha$.

The region above the mass distribution contains no mass, so the potential must satisfy

$$
\nabla^2\delta\Phi=0.
$$

```{exercise}
Derive the expression for the Laplacian of $\delta\Phi(x,z)$ and use Laplace's equation to show that, for $A \ne 0$,

$$\alpha^2=k^2.$$

```

Substitution into Laplace's equation gives

$$
\nabla^2\delta\Phi
=(\alpha^2-k^2)\delta\Phi
=0.
$$

For the non-trivial solution $A\ne0$, this requires

$$
\alpha^2=k^2.
$$

Because we chose both $\alpha>0$ and $k>0$,

$$
\boxed{\alpha=k}.
$$

Our proposed solution therefore becomes

$$
\boxed{
\delta\Phi(x,z)=A e^{-kz}\cos(kx)
}.
$$

This result has an important physical consequence. The horizontal wavelength is

$$
\lambda=\frac{2\pi}{k}.
$$

A short-wavelength variation has a large $k$ and therefore decays rapidly with height. A long-wavelength variation has a small $k$ and persists to much greater heights.

**Laplace's equation has linked the horizontal spatial scale of the gravity field to its vertical spatial scale.**

This explains an important property of gravity observations: fine-scale variations in the mass distribution become increasingly difficult to observe as the distance from the sources increases. A satellite at high altitude is therefore much more sensitive to large-scale variations of the Earth's gravity field than to small-scale variations.

This attenuation helped motivate the exceptionally low orbit of the **Gravity field and steady-state Ocean Circulation Explorer (GOCE)**. Its nominal science orbit was about $254\ \mathrm{km}$ above Earth, where short-wavelength variations remained stronger, but the residual atmosphere produced enough drag to threaten both the orbit and the very sensitive gravity measurements. GOCE combined a streamlined shape with a drag-free control system: an electric ion thruster continuously adjusted its thrust to compensate for the measured atmospheric drag {cite}`esa_goce_operations`.

```{admonition} A spatial transfer function
:class: tip

We can express the upward attenuation in the language of systems and signals. For one horizontal spatial frequency $k$, the potential anomaly at height $z$ is

$$
\delta\Phi(k,z)
=H_z(k)\,\delta\Phi(k,0),
$$

where

$$
\boxed{H_z(k)=e^{-kz}},
\qquad k>0.
$$

The function $H_z(k)$ is a **spatial transfer function**. It tells us how the amplitude of each horizontal spatial-frequency component changes between the reference surface and the observation height. Since $H_z(k)$ is close to one for small $k$ but rapidly approaches zero for large $k$, observing the field at altitude acts as a **spatial low-pass filter**: broad features pass more easily than fine details.

This is directly analogous to the frequency response of a system, which you may encounter in another course. There, a transfer function describes how different temporal frequencies are amplified or attenuated. Here the independent frequency variable is the spatial wavenumber $k$, measured in inverse metres, rather than a temporal frequency measured in hertz. Components of the gravity field and its gradients acquire additional factors of $k$ when we differentiate the potential, but they retain the same exponential attenuation with height.
```

```{admonition} More than gravity
:class: note

Laplace's equation is not specifically an equation of gravity. It appears whenever a potential-like quantity has no sources within the region under consideration.

For example, it describes the electric potential in a region without electric charge and the steady-state temperature in a region without heat sources.

The physical quantities are different, but the mathematical problem is the same:

$$
\nabla^2 u=0.
$$

This is one reason why learning how to reason about Laplace's equation is useful far beyond gravitational fields.
```

## What postulating has shown us

The examples above illustrate an important way of thinking about partial differential equations. We can propose a potential and substitute it into the governing equation to determine whether it is mathematically possible. Superposition then allows us to combine such solutions into richer fields.

The equation alone still permits infinitely many possibilities. The domain and boundary conditions supply the additional physical information needed to select among them. Later we will encounter systematic methods for constructing solutions from that information. For now, postulating and checking functions lets us begin to see how the equation constrains their possible form.
