# Oblique incidence: phase must match along the interface

The wave now arrives at an angle. The interface is still $z=0$, and we choose the **plane of incidence** as the $xz$ plane: it contains the incoming propagation direction and the interface normal. Keep the downward-positive $z$ convention introduced in {doc}`05_01_normal_incidence`: the incident and transmitted waves have positive $k_z$, while the reflected wave has negative $k_z$. All angles below are measured from the normal.

We already know Snell's law from {doc}`mechanical waves <../4_mechanical_waves/snells_law>`. We will recover it by asking whether the fields can satisfy Maxwell's boundary conditions everywhere along the interface. That gives the familiar result another meaning.

## Tilt the wave, keep the Cartesian derivatives

Recall the vector wavenumber from {doc}`03_01_waves_3d`. A plane wave has spatial factor

$$
e^{-j\vec k\cdot\vec r},\qquad
\vec k\cdot\vec r=k_xx+k_zz
$$

for propagation in the $xz$ plane. The wavenumber $k=|\vec k|$ is an angular spatial frequency; its components describe phase variation along the coordinate axes.

In medium $m$, we write the **wavenumber magnitude** as

$$
\boxed{k_m=|\vec k|=\omega\sqrt{\mu_m\epsilon_m}=\frac{\omega}{v_m}.}
$$

Here $m=1,2$ labels the medium. At a fixed frequency, the material fixes this magnitude. Tilting the wave changes its components, while $k_m$ stays the same.

Start with an electric field along $y$. There is no $y$ dependence, so the full Cartesian Helmholtz equation becomes

$$
\frac{\partial^2E_y}{\partial x^2}
+\underbrace{\frac{\partial^2E_y}{\partial y^2}}_{0}
+\frac{\partial^2E_y}{\partial z^2}+k_m^2E_y=0.
$$

We now try **separation of variables**: write the solution as a product of factors that each depend on just one coordinate. We used the same idea in {doc}`the heat equation <../3_diffusion_fields/heat_equation_1d>`, with $T(x,t)=f(x)g(t)$. Here we separate two spatial coordinates instead. For a specified tangential wavenumber $k_\parallel$, try

$$
E_y(x,z)=U(z)e^{-jk_\parallel x}.
$$

```{admonition} A PDE technique: separate the variables
:class: dropdown

Start a little more generally with $E_y(x,z)=X(x)U(z)$. Substituting this product into the Helmholtz equation and dividing out $XU$ gives

$$
\frac{X''(x)}{X(x)}+\frac{U''(z)}{U(z)}+k_m^2=0.
$$

The first ratio depends only on $x$, while the second depends only on $z$. For the equality to hold for every $x$ and $z$, each ratio must be constant. Choose

$$
\frac{X''}{X}=-k_\parallel^2.
$$

One corresponding factor is $X(x)=e^{-jk_\parallel x}$: it describes the oscillatory phase variation we want along the interface. What remains is an ODE for $U(z)$, which we obtain explicitly below.

Separation of variables is one approach to try when solving PDEs. Our uniform planar geometry makes it particularly useful. A separated product gives a building block; linearity lets us add such solutions when a more general field is needed.
```

The two nonzero derivatives are

$$
\frac{\partial^2E_y}{\partial x^2}=-k_\parallel^2Ue^{-jk_\parallel x},\qquad
\frac{\partial^2E_y}{\partial z^2}=U''e^{-jk_\parallel x}.
$$

Substitution leaves

$$
U''+(k_m^2-k_\parallel^2)U=0.
$$

The coefficient multiplying $U$ is constant within each medium. To recognize the familiar form of this ODE, we give that coefficient a name: **define** $k_{zm}^2=k_m^2-k_\parallel^2$. Then

$$
\boxed{k_{zm}^2=k_m^2-k_\parallel^2,\qquad
U''+k_{zm}^2U=0.}
$$ (eq:em-interface-oblique-ode)

Its solutions have factors $e^{\mp jk_{zm}z}$, so $k_{zm}$ describes phase variation in the normal, $z$ direction. For a propagating wave we take its positive value; the two signs in the exponential select propagation towards $+z$ or $-z$.

```{admonition} A familiar second-order ODE
:class: note

This is an equation you learned to solve in the first year. For $U''+k_{zm}^2U=0$, try an exponential $U=e^{sz}$. Differentiating twice and substituting gives

$$
(s^2+k_{zm}^2)e^{sz}=0
\quad\Longrightarrow\quad s^2+k_{zm}^2=0
\quad\Longrightarrow\quad s=\pm jk_{zm}.
$$

For our propagating case, $k_{zm}>0$, the two roots give two independent solutions. Their general combination is

$$
\boxed{U(z)=C_+e^{-jk_{zm}z}+C_-e^{+jk_{zm}z}.}
$$

You may remember writing this as a combination of sine and cosine. Euler's formula connects the two forms; the complex exponentials make propagation directions easier to read.

Put back the $x$ dependence:

$$
E_y(x,z)=C_+e^{-j(k_\parallel x+k_{zm}z)}
+C_-e^{-j(k_\parallel x-k_{zm}z)}.
$$

With our time factor $e^{j\omega t}$, the first term travels towards $+z$ and the second towards $-z$. These are the plane-wave solutions used below. The two integration constants are their complex amplitudes; the boundary conditions and the prescribed incoming wave determine them.
```

We can now read the definition geometrically:

$$
k_m^2=k_\parallel^2+k_{zm}^2.
$$

The squared magnitude of the vector wavenumber is the sum of its squared tangential and normal components. The two-dimensional PDE has become an ODE once we specify the tangential variation, and the bulk equation determines the remaining normal wavenumber.

## Match an entire boundary

Allow for incident, reflected and transmitted plane waves. At $z=0$ their spatial factors reduce to

$$
e^{-jk_{i,x}x},\qquad e^{-jk_{r,x}x},\qquad e^{-jk_{t,x}x}.
$$

The boundary conditions must hold for **every $x$**, at every time. Matching at one point is not enough. Constant amplitudes cannot repair different phase slopes along the boundary. For our stationary, uniform, linear interface, the coupled waves therefore share temporal frequency and tangential wavenumber:

$$
\boxed{\omega_i=\omega_r=\omega_t,\qquad
k_{i,x}=k_{r,x}=k_{t,x}=k_\parallel.}
$$ (eq:em-interface-phase-matching)

The interface fixes the shared tangential variation; the bulk equation fixes the allowed normal variation in each material. Together they give

$$
\begin{aligned}
\vec k_i&=k_\parallel\hat x+k_{z1}\hat z,\\
\vec k_r&=k_\parallel\hat x-k_{z1}\hat z,\\
\vec k_t&=k_\parallel\hat x+k_{z2}\hat z.
\end{aligned}
$$

We take the positive real roots $k_{z1}$ and $k_{z2}$ here, so the transmitted wave propagates into medium 2. In this part of the discussion both media are lossless and the transmitted wave is propagating.

### Make the phases meet

Use the boundary as a test of the proposed wave directions. The activity compares **unit phase factors**: their amplitudes are set to one, so we can concentrate on spatial phase matching. The actual field amplitudes, including reflection phase shifts, are handled in the next section.

```{admonition} Predict, try an angle, then check the boundary
:class: question

1. Start with the matched waves. Compare the crest intersections just either side of $z=0$. How does their spacing relate to the tangential wavenumber?
2. Try $\theta_t=\theta_i$ while the media have different permittivities. The proposed transmitted wave still has the right wavenumber magnitude in its medium. Why does it nevertheless fail the boundary test?
3. Choose the transmitted angle yourself and try to align the wavefronts. Can agreement at $x=0$ tell you whether the whole boundary matches? Use the lower plot as well as the geometry.
4. Match the phases, then increase $\epsilon_{r2}$ at fixed incident angle. Predict what happens to $k_2$, its normal component and the transmitted angle. Which component must stay unchanged?
5. Add the reflected wavefronts. Check their tangential component and normal-component sign. Then try normal incidence: what happens to phase variation along the boundary?
6. Play the animation. Do changing crest positions alter the wavenumber-matching condition? Would switching between H and V polarization change this phase condition for our isotropic media?
```

```{raw} html
:file: interactives/phase_matching_embed.html
```

The geometry uses equal spatial scales along $x$ and $z$. A manual angle can look nearly right on a finite drawing; the exact condition for the whole interface remains equality of the tangential wavenumbers. We have recovered the directions from the bulk equation and the boundary phase test. Next, we match the amplitudes.

## Snell's law, now as a boundary condition

Since $k_x=k\sin\theta$,

$$
k_1\sin\theta_i=k_1\sin\theta_r=k_2\sin\theta_t.
$$

Consequently,

$$
\boxed{\theta_r=\theta_i,\qquad
\frac{\sin\theta_i}{v_1}=\frac{\sin\theta_t}{v_2}.}
$$ (eq:em-interface-snell)

These are the reflection law and Snell's refraction law already obtained geometrically in mechanical waves. Here they follow from satisfying the boundary conditions along a whole plane. A slower transmitted wave has a larger wavenumber, so preserving $k_\parallel$ bends its propagation towards the normal.

```{admonition} Read the geometry from the equation
:class: question

A wave enters a nonmagnetic dielectric with $\epsilon_2=4\epsilon_0$ from air at $\theta_i=30^\circ$.

1. Find $k_2/k_1$ and the transmitted angle.
2. Write all three vector wavenumbers in terms of $k_1$. Check their magnitudes and tangential components.
3. For the transmitted field $\vec E_t=\hat y C e^{-j\vec k_t\cdot\vec r}$, calculate the Cartesian curl and obtain $\vec H_t$ from Faraday's law.
4. Verify that $\vec k_t\cdot\vec H_t=0$. Interpret this dot product physically.
```

The common time factor still turns time differentiation into multiplication by $j\omega$ for the **whole harmonic field**. Spatial differentiation becomes multiplication by $-j\vec k$ separately for each plane-wave term. The incident-plus-reflected field has two vector wavenumbers; it cannot be assigned just one.

If $k_\parallel>k_2$, {eq}`eq:em-interface-oblique-ode` gives $k_{z2}^2<0$. A real transmitted angle then no longer describes the solution. This is the route to total internal reflection and evanescent fields, related to the sign-of-$k^2$ discussion in {doc}`04_04_radar_penetration`. We leave that extension aside here.

## Reading and sources

See [TU Delft's *Interactive Optics*, reflection and transmission at an interface](https://interactivetextbooks.tudelft.nl/tn2421/content/Chap1_Basics/Basics_2022_01Clean.html#reflection-and-transmission-at-an-interface) for the vector geometry and phase-matching construction. We retain the Fourier convention already used throughout this book.
