# Beyond the Dipole: Adding Simple Patterns

The dipole potential satisfies Laplace's equation, but its surface pattern is too simple to match all the boundary data. How can we add detail while keeping the equation we have already checked?

```{admonition} What to take from this page
:class: important

**You do not need to learn spherical harmonics in this part of the course.** You do not need their general formulas, to derive them, or to calculate their coefficients. The name below identifies a tool used by geophysicists.

The idea to understand is familiar: **add simple patterns to describe a more complicated one**. Connect this to superposition, the linearity of Laplace's equation, and the loss of fine spatial detail with observation height. The formula details are optional.
```

## The same idea as a Fourier series

In a Fourier series, we represent a complicated signal by adding sine and cosine patterns with different weights. For a pattern on a sphere, we can make a similar construction using building blocks that depend on the two surface angles. These angular building blocks are called **spherical harmonics**.

You have already used one: the dipole's $\cos\theta$ pattern in coordinates aligned with its moment. The next figure shows that pattern, a rotated version of it, and two examples with finer spatial structure. The label **degree** distinguishes families of patterns; higher degrees allow finer structure. There is no need to learn the functions behind the labels.

```{figure} figures/spherical_harmonic_patterns.svg
:name: fig-magnetic-harmonic-patterns
:width: 100%
:alt: Four maps illustrate the dipole angular pattern, a rotated dipole pattern, and two patterns with finer spatial structure.

Look at the patterns rather than memorize their labels. The two upper panels are differently oriented dipole patterns. The lower panels illustrate additional spatial detail. Colours show signed angular amplitude, not measurements. Each family contains more possibilities than shown here.
```

## Why adding patterns preserves the equation

Each angular pattern is paired with a radial dependence so that the resulting potential satisfies Laplace's equation outside the sources. Once we have two such potentials, the familiar linearity rule tells us

$$
\nabla^2(\Psi_1+\Psi_2)
=\nabla^2\Psi_1+\nabla^2\Psi_2=0.
$$

We can therefore change their weights and add further contributions to improve the boundary match, while continuing to satisfy the same field equation. This is the purpose of the expansion: it gives us more spatial freedom than one dipole. It does not introduce a new magnetic field law.

The available patterns must also respect the physics. A $1/r$ potential would produce a radial inverse-square field with nonzero net magnetic flux. It is excluded because we have no magnetic monopoles. The dipole is the first **allowed** decaying contribution; if its moment cancels, the leading surviving contribution can decay faster.

## What survives at satellite altitude?

We already saw that cancellation makes dipole fields decay faster than monopole fields, and that cancelling dipoles can produce still faster decay. The same progression appears in the spatial expansion: **finer internal-source patterns attenuate faster with height** than broad ones.

```{figure} figures/magnetic_harmonic_attenuation.svg
:name: fig-magnetic-harmonic-attenuation
:width: 85%
:alt: Normalized field amplitudes decrease with height; the dipole curve falls more slowly than curves representing finer spatial patterns.

Every curve starts at the same normalized surface amplitude. Degree one is the dipole; the other curves represent finer patterns. Read the relative attenuation: the curves do not compare the initial strengths of actual sources.
```

```{admonition} Read the graph and explain the physics
:class: exercise

1. At 500 km, which curve retains the greatest fraction of its surface amplitude?
2. If a broad and a finer contribution start with equal amplitudes, which becomes relatively more prominent at altitude?
3. Why might observations closer to the ground reveal detail that is hard to recover from satellites? Connect your explanation to the gravity example of short horizontal wavelengths attenuating with height.
```

Broad patterns remain relatively prominent at altitude, while fine detail becomes harder to recover. The residual we plotted for Earth tells us that more patterns are needed, but it does not uniquely identify their sources. Non-dipole structure can come from the core itself, and crustal fields also span a range of spatial scales {cite}`igrf14_limitations`.

These attenuation statements concern sources **inside** the reference sphere, observed in the current-free exterior. Sources outside the observation region require a different radial description. The physical model and observation region still matter.

````{admonition} Optional reference: the formulas behind the patterns
:class: dropdown

This material is available for curiosity and later reference. It is not needed to complete the main reading or the graph exercise above.

For an internal source, one decaying exterior potential term can be written as

$$
\Psi_\ell(r,\theta,\varphi)
=a\,c_\ell\left(\frac{a}{r}\right)^{\ell+1}Y_\ell(\theta,\varphi),
\qquad \ell=1,2,3,\ldots.
$$ (eq:magnetic-harmonic-radial-form)

$Y_\ell$ denotes one dimensionless angular pattern of degree $\ell$, and $c_\ell$ sets its amplitude in tesla. There are several independent patterns at each degree; that extra index is suppressed here. The potential has units $\mathrm{T\,m}$. For $\ell=1$, choosing $Y_1=\cos\theta$ and $c_1=B_0$ gives our dipole potential.

An axisymmetric degree-two example is

$$
\Psi_2=\frac{C_2}{2r^3}(3\cos^2\theta-1),
$$

with $C_2$ in $\mathrm{T\,m^4}$. Its radial and angular Laplacian contributions cancel, just as they do for the dipole.

Taking a gradient introduces one further inverse power of distance, so a degree-$\ell$ field scales as $r^{-(\ell+2)}$. Its remaining amplitude fraction at height $h$ is

$$
\left(\frac{a}{a+h}\right)^{\ell+2}.
$$ (eq:magnetic-harmonic-height-ratio)

For $a=6371.2\,\mathrm{km}$ and $h=500\,\mathrm{km}$, this fraction is about $0.80$ for the dipole and $0.40$ for degree ten. These are the values behind the graph; understanding the pattern of attenuation does not require learning this general expression.
````
