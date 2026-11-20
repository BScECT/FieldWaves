# Waves in three dimensions

*From a satellite to a measurement on Earth*

A radar satellite sends a pulse towards the Earth and records the reflected signal. Between transmission and reception, several things happen: the wave travels, spreads out, encounters matter and returns to an antenna that responds to particular field orientations. Which parts of that journey explain the signal we measure?

We already have a useful starting point: a plane wave travelling along $z$. Now we connect that solution to a wave from a distant source, calculate the energy it carries and ask what a receiving antenna detects. The propagation calculations below use a charge-free, current-free vacuum, with $c=1/\sqrt{\mu_0\epsilon_0}$ and $\eta_0=\sqrt{\mu_0/\epsilon_0}$. Matter enters the story at the end, ready for the following sections.

```{figure} figures/follow_the_signal.svg
:name: fig:em-follow-the-signal
:width: 100%

Follow the signal: an outgoing wave spreads from a radar transmitter, interacts with the ground and scatters towards a receiver. The nearby transmitting and receiving satellites form a **bistatic** radar; both paths sample the same ground patch. The electric field is transverse: perpendicular to the direction of propagation. Bistatic radar also happens to be part of Paco's research, so there is a little personal bias in this choice of example.
```

## A wave from a source spreads out

For a source (think of our radar's antenna) at the origin, distance is

$$
r= |\vec r| =\sqrt{x^2+y^2+z^2}.
$$

Let us try a simple model of an outgoing spherical wave,

$$
\boxed{\psi(\vec r,t)=\frac{A}{r}F(t-r/c),\qquad r>0,}
$$

where $F$ is a dimensionless waveform, $A$ is a constant and $\psi$ is a scalar wave quantity. For now this is a scalar model: we have not yet specified the vector fields. We will come back to those; first, let us see whether the proposed waveform satisfies the wave equation. Keep following a feature: $t-r/c$ stays constant, so the feature moves outwards with speed $c$. At one time, all locations at the same distance from the source have the same waveform argument. The wavefronts are spheres.

The $1/r$ factor says that the amplitude decreases with distance. We will return to its physical meaning when we discuss energy. First, does this proposed wave actually satisfy the wave equation?

```{admonition} Retrieve the gradient
:class: question

Starting from the Cartesian definition of the gradient, show that

$$
\nabla r=\hat x\frac{x}{r}+\hat y\frac{y}{r}+\hat z\frac{z}{r}=\hat r.
$$

What does its direction mean? You should be able to see this without doing the calculation: stand somewhere away from the source. To increase your distance from it as quickly as possible, which way should you walk?

Next, differentiate the three components once more and show that $\nabla^2r=2/r$ for $r>0$.
```

For a function $g(r)$, the chain rule then gives

$$
\nabla g=g'(r)\nabla r,
\qquad
\nabla^2g=g''(r)|\nabla r|^2+g'(r)\nabla^2r
=g''(r)+\frac{2}{r}g'(r).
$$

Writing $g(r)$ tells us that the function depends only on distance: it has the same value everywhere on a sphere centred on the source. Here $r$ is itself a function of $x,y,z$. We used Cartesian derivatives to obtain these identities, but the identities are not restricted to Cartesian coordinates; we would get the same result in spherical coordinates.

The useful shortcut comes from the **radial symmetry**. The full three-dimensional Laplacian reduces to $g''(r)+2g'(r)/r$, not just $g''(r)$. We can work with derivatives with respect to distance without having to introduce a full spherical-coordinate calculation.

````{admonition} Check the spherical wave against the PDE
:class: dropdown

Primes on $F$ mean differentiation with respect to its full argument $t-r/c$. At fixed time,

$$
\frac{\partial\psi}{\partial r}
=-\frac{A}{r^2}F-\frac{A}{cr}F',
$$

$$
\frac{\partial^2\psi}{\partial r^2}
=\frac{2A}{r^3}F+\frac{2A}{cr^2}F'+\frac{A}{c^2r}F''.
$$

Now form $\partial^2\psi/\partial r^2+(2/r)\partial\psi/\partial r$. The terms containing $F$ and $F'$ cancel, leaving

$$
\nabla^2\psi=\frac{A}{c^2r}F''
=\frac{1}{c^2}\frac{\partial^2\psi}{\partial t^2}.
$$

The spreading factor and the travelling waveform work together to satisfy the PDE. The source at $r=0$ is outside this calculation.
````

This is an exact **scalar** wave solution away from the source. An electromagnetic wave also has vector directions and must satisfy all four Maxwell equations. An antenna's radiated field has a direction-dependent strength; in its radiation region, its leading electric and magnetic fields are transverse—perpendicular to the local propagation direction—and decrease as $1/r$ along a fixed direction. The scalar model captures the spreading and wavefront geometry without requiring us to derive an antenna's full field.

## A small part of a spherical wave looks planar

Place a receiver at $(0,0,R)$ and look at a small region around it. Describe a nearby point by its displacement $(\delta x,\delta y,\delta z)$ from the receiver:

$$
(x,y,z)=(0,0,R)+(\delta x,\delta y,\delta z)
=(\delta x,\delta y,R+\delta z).
$$

All three displacements are small compared with $R$. The distance from the source is therefore

$$
r=\sqrt{(\delta x)^2+(\delta y)^2+(R+\delta z)^2}.
$$

Remember the first-order Taylor approximation

$$
\sqrt{1+u}\approx 1+\frac{u}{2},\qquad |u|\ll1.
$$

To use it, factor out $R+\delta z$ from the square root:

$$
r=(R+\delta z)\sqrt{1+\frac{(\delta x)^2+(\delta y)^2}{(R+\delta z)^2}}
\approx R+\delta z+\frac{(\delta x)^2+(\delta y)^2}{2(R+\delta z)}.
$$

Since $|\delta z|\ll R$, we can also replace $R+\delta z$ by $R$ in the denominator of the small correction:

$$
\boxed{r\approx R+\delta z+\frac{(\delta x)^2+(\delta y)^2}{2R}.}
$$

Moving along the source–receiver direction changes the distance by $\delta z$. Moving sideways adds the smaller, quadratic correction: this is the wavefront curvature. If that correction has a negligible effect on the waveform, and $1/r$ hardly changes over our small region,

$$
\psi\approx\frac{A}{R}F\!\left(t-\frac{R}{c}-\frac{\delta z}{c}\right).
$$

That is our familiar plane waveform, with an amplitude $A/R$ and an arrival delay $R/c$. Locally it varies with $\delta z$, but not with $\delta x$ or $\delta y$. The whole wave has not become flat. We are examining a small patch of it.

### When does the phase notice the curvature?

The amplitude can look almost constant while the phase is already noticeably wrong. At radar wavelengths, even a small extra path length can be a substantial fraction of a wavelength. Let us check the two errors separately.

For this activity, put the origin at the centre of a horizontal ground patch, with $z$ upwards. The satellite is $30^\circ$ from zenith, at slant distance $R$. Along the ground, the exact source distance and its local plane-wave approximation are

$$
r(x)=\sqrt{R^2+2Rx\sin\theta+x^2},\qquad
r_{\mathrm{plane}}(x)=R+x\sin\theta,
\qquad\theta=30^\circ.
$$

The plane wave already includes the linear phase variation along the ground. We are testing the **curvature left over**, not pretending that the phase is the same everywhere on the surface. Relative to the field amplitude at the patch centre, the spherical amplitude is $R/r(x)$ and the plane-wave amplitude is $1$. The magnitude of the phase error is

$$
|\Delta\phi(x)|=\frac{2\pi}{\lambda}\big[r(x)-r_{\mathrm{plane}}(x)\big]
\approx\frac{kx^2\cos^2\theta}{2R}.
$$

```{admonition} Predict first, then move the controls
:class: question

1. Choose a shorter wavelength without changing the geometry. Which error changes, and why?
2. Double the ground patch width. Does the phase error roughly double or quadruple?
3. Double the source distance while keeping the patch and wavelength fixed. What happens to both errors?

At the starting settings, is nearly constant amplitude enough to justify treating the wave as planar?
```

```{raw} html
:file: interactives/wavefront_error_embed.html
```

At the starting settings ($R=800\ \mathrm{km}$, ground half-width $L=150\ \mathrm m$, $\lambda=3\ \mathrm{cm}$), the largest amplitude departure is only about $0.0094\%$, yet the phase error reaches about $2.2$ radians. The amplitude approximation looks excellent; the phase approximation does not. A shorter wavelength makes the phase more sensitive without changing the amplitude error at all. The dashed guide marks $\pi/4$ radians ($45^\circ$), which we use here as a working phase-error tolerance.

```{admonition} How small is a small patch?
:class: dropdown

For a harmonic wave, $F(t-r/c)=\cos(\omega t-kr)$ and $k=\omega/c$. Over a transverse patch of radius $L$, the neglected phase difference is approximately

$$
\Delta\phi\approx\frac{kL^2}{2R}.
$$

How small is small enough? That depends on the application and the accuracy we need. In our radar example we use $|\Delta\phi|<\pi/4$ ($45^\circ$) as a working tolerance, not a universal limit. Requiring the error to be much less than one radian is a stronger small-error condition, rather than a requirement for every useful plane-wave approximation. The acceptable amplitude variation also depends on what we are trying to measure. For a pulse, compare the neglected travel-time difference with the timescale of its features. Being small compared with $R$ is not always enough: a tiny path difference can still be many wavelengths. This patch-curvature test supplements the assumption that we are already in the source's radiation region.
```

## The direction of travel is not necessarily z

Our axes are a choice. A satellite signal can arrive diagonally relative to them. Let $\hat n$ be a unit vector pointing along propagation and let $\vec p$ be a constant electric-field amplitude vector. A plane waveform can be written

$$
\boxed{\vec E(\vec r,t)=\vec p\,F\!\left(t-\frac{\hat n\cdot\vec r}{c}\right).}
$$

The dot product $\hat n\cdot\vec r$ is distance along the propagation direction. At a fixed time, equal waveform arguments lie on planes perpendicular to $\hat n$.

For harmonic waves, we collect the propagation direction and wavenumber in the **vector wavenumber** (also called the wave vector):

$$
\boxed{\vec k=k\hat n,\qquad k=|\vec k|=\frac{2\pi}{\lambda}.}
$$

The wavenumber is the angular spatial frequency, in rad/m. Its vector form also tells us the direction of propagation. The field phasor becomes

$$
\vec E(\vec r)=\vec p\,e^{-j\vec k\cdot\vec r},\qquad
\vec k\cdot\vec r=k_xx+k_yy+k_zz.
$$

For the diagonal direction used below,

$$
\vec k=\frac{k}{\sqrt2}\hat x+\frac{k}{\sqrt2}\hat z,
\qquad\vec k\cdot\vec r=\frac{k(x+z)}{\sqrt2}.
$$

The dot product packages the same spatial phase in a form that works for any propagation direction. The common $e^{j\omega t}$ is still understood.


```{admonition} A diagonal wave: read it, then check it
:class: question

Take

$$
\hat n=\frac{\hat x+\hat z}{\sqrt2},\qquad\vec p=E_0\hat y,
\qquad\vec E=\hat yE_0F\!\left(t-\frac{x+z}{c\sqrt2}\right).
$$

1. Sketch a wavefront in the $xz$-plane and the electric-field direction. Which direction does a feature move? Check that $\vec E\cdot\hat n=0$: the field is transverse, meaning perpendicular to propagation.
2. Calculate $\partial^2E_y/\partial x^2$, $\partial^2E_y/\partial y^2$ and $\partial^2E_y/\partial z^2$. Check the wave equation. Why would keeping only the $z$ derivative now give the wrong answer?
3. Write the full Cartesian divergence of $\vec E$ and check that it is zero.
4. Calculate $\hat n\times\vec E$. Use it to propose the magnetic field, then check Faraday's law using the Cartesian curl.
```

For a vacuum plane wave the general field relation is

$$
\boxed{\vec p\cdot\hat n=0,\qquad
\vec H=\frac{1}{\eta_0}\hat n\times\vec E.}
$$

The field is transverse: $\vec E$ is perpendicular to the propagation direction $\hat n$. This is a statement about the wave, not about the ground or our choice of coordinate axes. The cross product gives the magnetic-field direction. For the diagonal example,

$$
\vec H=\frac{E_0}{\eta_0\sqrt2}(-\hat x+\hat z)
F\!\left(t-\frac{x+z}{c\sqrt2}\right).
$$

```{admonition} Check the derivatives
:class: dropdown

The dot-product check gives $\vec E\cdot\hat n=E_0F\,\hat y\cdot(\hat x+\hat z)/\sqrt2=0$. With primes denoting derivatives of $F$,

$$
\frac{\partial^2 E_y}{\partial x^2}
=\frac{\partial^2 E_y}{\partial z^2}
=\frac{E_0}{2c^2}F'',\qquad
\frac{\partial^2 E_y}{\partial y^2}=0.
$$

Their sum is $E_0F''/c^2$, as required. The divergence is

$$
\nabla\cdot\vec E
=\frac{\partial E_x}{\partial x}
+\frac{\partial E_y}{\partial y}
+\frac{\partial E_z}{\partial z}=0+0+0.
$$

Only $E_y$ is nonzero, but it varies with $x,z$, not $y$. Its curl is

$$
\nabla\times\vec E
=-\hat x\frac{\partial E_y}{\partial z}
+\hat z\frac{\partial E_y}{\partial x}
=\frac{E_0}{c\sqrt2}(\hat x-\hat z)F'
=-\mu_0\frac{\partial\vec H}{\partial t},
$$

where $\mu_0/\eta_0=1/c$. The other curl equation also holds because $1/(\eta_0c)=\epsilon_0$; both field divergences vanish.
```

### Passing one equation is not enough

Faraday's law links a circulating electric field to a changing magnetic field. But it is only one of the equations our proposed fields must satisfy.

```{admonition} A pair that passes Faraday's law — is it a vacuum wave?
:class: question

In the same charge-free, current-free vacuum, someone proposes

$$
\vec E=\hat xE_0F(t-2z/c),\qquad
\vec H=\hat y\frac{2E_0}{\eta_0}F(t-2z/c),
$$

with a nonconstant pulse waveform $F$.

1. What speed does the waveform suggest?
2. Show that $\nabla\times\vec E=-\mu_0\partial\vec H/\partial t$. Also check both divergences.
3. Now test $\nabla\times\vec H=\epsilon_0\partial\vec E/\partial t$. Where does the proposal fail?
4. Does the electric field satisfy the vacuum wave equation? Relate the result to the speed you found.
```

```{admonition} Check the proposed pair
:class: dropdown

The suggested speed is $c/2$. Faraday's law does hold:

$$
\nabla\times\vec E=-\hat y\frac{2E_0}{c}F'
=-\mu_0\frac{\partial\vec H}{\partial t}.
$$

Both divergences are zero. But the Ampère–Maxwell equation gives different answers on its two sides:

$$
\nabla\times\vec H=\hat x\frac{4E_0}{\eta_0c}F'
=\hat x\,4\epsilon_0E_0F',
\qquad
\epsilon_0\frac{\partial\vec E}{\partial t}
=\hat x\,\epsilon_0E_0F'.
$$

Similarly, $\nabla^2\vec E=\hat x(4E_0/c^2)F''$, whereas $\partial^2\vec E/\partial t^2/c^2=\hat x(E_0/c^2)F''$. A pulse with nonzero $F''$ fails the wave equation too. Faraday's law alone allowed us to choose an accompanying $H$ for the wrong speed; the remaining equations reject the pair.
```

We next calculate the energy transported by these fields in {doc}`03_02_energy_flow`.

## Reading and sources

The geometry of spherical and locally plane waves can be compared with TU Delft's open [*Interactive Optics*, “Basic Electromagnetic and Wave Optics”](https://interactivetextbooks.tudelft.nl/tn2421/content/Chap1_Basics/Basics_2022_01Clean.html).
