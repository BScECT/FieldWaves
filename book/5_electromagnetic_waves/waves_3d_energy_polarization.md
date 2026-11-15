# From a satellite to a measurement on Earth

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

## The fields carry energy

A satellite uses electrical power to generate the transmit signal. Some of that energy reaches the ground, and a much smaller amount returns to a radar receiver. In the end, this energy will be competing with noise: we need to have enough energy in our radar echo to be able to detect it!

### Energy in the fields

It takes work to build an electric or magnetic field. That energy is stored in the field and can later be transferred to matter. In vacuum, the energy per unit volume is

$$
\boxed{u=\underbrace{\frac{\epsilon_0|\vec E|^2}{2}}_{u_E}
+\underbrace{\frac{\mu_0|\vec H|^2}{2}}_{u_H}}
\qquad[\mathrm{J/m^3}].
$$ (eq:em-3d-energy-density)

For now these are the real, instantaneous fields. Stronger fields contain more energy: doubling both field strengths quadruples the energy density. For a finite region, its field energy is $U=\int_Vu\,dV$. But having energy somewhere does not necessarily mean it is flowing anywhere. That is the next question.

### Energy flowing through space

The **Poynting vector** describes the energy flow:

$$
\boxed{\vec S=\vec E\times\vec H.}
$$ (eq:em-3d-poynting)

Here the fields are the **real, instantaneous fields**. Check the units:

$$
[\vec S]=\frac{\mathrm V}{\mathrm m}\frac{\mathrm A}{\mathrm m}
=\mathrm{W/m^2}.
$$

This is energy crossing unit area per unit time, with a direction. For a transverse vacuum plane wave,

$$
\vec S=\frac{1}{\eta_0}\vec E\times(\hat n\times\vec E)
=\frac{|\vec E|^2}{\eta_0}\hat n.
$$

The last step uses $\vec E\cdot\hat n=0$ and the vector triple-product identity. Energy travels along $\hat n$.

```{admonition} Energy density and energy flux
:class: question

For a travelling vacuum plane wave, use $|\vec E|=\eta_0|\vec H|$ to show that $u_E=u_H$, and hence $u=\epsilon_0|\vec E|^2$. Combine this with the expression for $\vec S$ to show that

$$
\boxed{\vec S=cu\,\hat n.}
$$

Check the units: energy density times speed gives energy flux. These are instantaneous quantities. In a linearly polarized travelling sinusoid, the electric and magnetic energy densities rise and fall together; energy does not alternate between them.
```

### Average energy flow using phasors

We have a convenient language for harmonic fields, so let us use it. In this calculation $\vec E(\vec r)$ and $\vec H(\vec r)$ are the **complex phasors**, with the common time factor $e^{j\omega t}$ understood. To see how their products work, write the real fields explicitly for a moment:

$$
\vec E_{\mathrm{real}}(\vec r,t)=\operatorname{Re}\{\vec E(\vec r)e^{j\omega t}\},
\qquad
\vec H_{\mathrm{real}}(\vec r,t)=\operatorname{Re}\{\vec H(\vec r)e^{j\omega t}\}.
$$

We want the average of $\vec E_{\mathrm{real}}\times\vec H_{\mathrm{real}}$. The key is a familiar trigonometric identity. For two real oscillations at the same frequency,

$$
a_{\mathrm{real}}=a_0\cos(\omega t+\alpha),\qquad
b_{\mathrm{real}}=b_0\cos(\omega t+\beta),
$$

$$
a_{\mathrm{real}}b_{\mathrm{real}}
=\frac{a_0b_0}{2}\big[\cos(\alpha-\beta)+\cos(2\omega t+\alpha+\beta)\big].
$$

The second term averages to zero over a period. With phasors $a=a_0e^{j\alpha}$ and $b=b_0e^{j\beta}$, this becomes

$$
\langle a_{\mathrm{real}}b_{\mathrm{real}}\rangle
=\frac{a_0b_0}{2}\cos(\alpha-\beta)
=\frac12\operatorname{Re}\{ab^*\}.
$$

The star means **complex conjugate**. It changes the sign of the imaginary part, turning a sum of phases into the phase difference we need. Applying this to the component products in the cross product gives

$$
\boxed{\langle\vec S\rangle
=\frac12\operatorname{Re}\{\vec E\times\vec H^*\}.}
$$ (eq:em-3d-phasor-poynting)

There are three things to keep: the conjugate on $\vec H$, the real part, and the factor $1/2$. That factor belongs to our **peak-amplitude phasor convention**, not RMS amplitudes. This expression gives the time-averaged energy flux directly from the phasors; we can keep working in complex notation.

For a vacuum plane wave, $\vec H=(\hat n\times\vec E)/\eta_0$. Because $\hat n$ and $\eta_0$ are real,

$$
\vec E\times\vec H^*
=\frac{1}{\eta_0}\vec E\times(\hat n\times\vec E^*)
=\frac{\vec E\cdot\vec E^*}{\eta_0}\hat n.
$$

Here $\vec E\cdot\vec E^*=|E_x|^2+|E_y|^2+|E_z|^2$ is the squared magnitude of a complex vector. It is real and nonnegative. Consequently,

$$
\boxed{\langle\vec S\rangle
=\frac{\vec E\cdot\vec E^*}{2\eta_0}\hat n.}
$$

This also works for circular and elliptical polarization: the components can have different phases. For a linearly polarized wave with peak field amplitude $E_0$, it gives $\langle\vec S\rangle=E_0^2\hat n/(2\eta_0)$. Doubling the field amplitude quadruples the average flux. We call the magnitude of this average flux the **intensity**.

The same averaging rule gives the field energy density in vacuum:

$$
\langle u\rangle
=\frac{\epsilon_0}{4}\vec E\cdot\vec E^*
+\frac{\mu_0}{4}\vec H\cdot\vec H^*.
$$

For a travelling vacuum plane wave the two contributions are again equal, and $\langle\vec S\rangle=c\langle u\rangle\hat n$. Energy present and energy transported are two parts of the same picture.

```{admonition} Follow the energy with phasors
:class: question

For our diagonal wave, take the electric-field phasor

$$
\vec E(\vec r)=\hat yE_0e^{-jk(x+z)/\sqrt2},\qquad k=\omega/c,
$$

with real $E_0$ and propagation direction $\hat n=(\hat x+\hat z)/\sqrt2$.

1. Find $\vec H$ from $\hat n\times\vec E/\eta_0$, then write $\vec H^*$ explicitly.
2. Calculate $\vec E\times\vec H^*$ from its Cartesian components. What happens to the spatial phase factors?
3. Find $\langle\vec S\rangle$ and $\langle u\rangle$, and check that they satisfy $\langle\vec S\rangle=c\langle u\rangle\hat n$.
4. Add the same phase shift $\phi$ to both field phasors. Does the average energy flux change? What happens if $E_0$ doubles?
5. What spatial phase factor would remain if you accidentally used $\vec E\times\vec H$ instead? Why would that give the wrong average flux?
```

```{admonition} Check the conjugate and the direction
:class: dropdown

The magnetic-field phasor and its conjugate are

$$
\vec H=\frac{E_0}{\eta_0\sqrt2}(-\hat x+\hat z)e^{-jk(x+z)/\sqrt2},
\qquad
\vec H^*=\frac{E_0}{\eta_0\sqrt2}(-\hat x+\hat z)e^{+jk(x+z)/\sqrt2}.
$$

The opposite phase factors cancel, giving

$$
\vec E\times\vec H^*=\frac{E_0^2}{\eta_0\sqrt2}(\hat x+\hat z),
\qquad
\langle\vec S\rangle=\frac{E_0^2}{2\eta_0}\hat n,
\qquad
\langle u\rangle=\frac{\epsilon_0E_0^2}{2}.
$$

A common phase shift also cancels as $e^{j\phi}e^{-j\phi}=1$: it changes the timing of the oscillation, not its average energy transport. Without the conjugate we would retain $e^{-2jk(x+z)/\sqrt2}$ and obtain a position-dependent result, even though this travelling plane wave has uniform average energy flux.
```

## Spreading is not absorption

Power crossing a surface is a flux integral:

$$
P=\int_A\langle\vec S\rangle\cdot\hat n_A\,dA.
$$

Here $\hat n_A$ is the surface normal; it need not be the propagation direction $\hat n$. For an ideal isotropic radiator, surround the source by a sphere. The flux is radial and has the same magnitude everywhere on that sphere, so

$$
P=4\pi r^2\langle S_r\rangle.
$$

If no power is absorbed between spheres, the same total power crosses each one. Therefore

$$
\boxed{\langle S_r\rangle\propto r^{-2},\qquad
E_{\rm amplitude}\propto r^{-1}.}
$$

This explains the amplitude factor in our spherical-wave model. A real antenna directs more power towards some angles than others, but along a fixed direction in its radiation region the same range scaling applies. The power is distributed over a larger area; it has not disappeared into the medium.

```{admonition} Use Gauss's theorem again
:class: question

For a source-free, lossless shell between two spheres, suppose the time-averaged energy balance is $\nabla\cdot\langle\vec S\rangle=0$. Use Gauss's theorem to explain why the power leaving the outer sphere equals the power entering the shell through the inner sphere. Pay attention to the outward normal of the shell on its inner boundary.

If the distance doubles, what happens to intensity, field amplitude and total power crossing a complete sphere?
```

### Power arriving on a tilted surface

For approximately uniform flux over a flat surface of area $A$,

$$
P_A=A\langle\vec S\rangle\cdot\hat n_A
=A\langle S\rangle\cos\alpha,
$$

where the normal is chosen so that this crossing power is positive. The angle $\alpha$ is between propagation and that normal. A surface presented edge-on intercepts little power; one perpendicular to propagation intercepts the most. This geometry also matters for solar energy arriving on a ground surface or solar panel. Absorbed power additionally depends on what the surface reflects or transmits.

<!--
```{admonition} Figure placeholder — the same beam, different collecting area
:class: note

Parallel energy-flow arrows crossing a flat patch in two orientations. Mark the area $A$, the surface normal and projected area $A\cos\alpha$. Keep electric-field orientation out of this drawing so that it does not get confused with antenna polarization below.
```
-->

```{admonition} Optional derivation — local energy conservation
:class: dropdown

Use the real, instantaneous fields and their energy density $u$ introduced above.

Use the vector identity

$$
\nabla\cdot(\vec E\times\vec H)
=\vec H\cdot(\nabla\times\vec E)
-\vec E\cdot(\nabla\times\vec H).
$$

Substituting the two vacuum curl equations gives

$$
\nabla\cdot\vec S
=-\mu_0\vec H\cdot\frac{\partial\vec H}{\partial t}
-\epsilon_0\vec E\cdot\frac{\partial\vec E}{\partial t}
=-\frac{\partial u}{\partial t}.
$$

Thus

$$
\boxed{\frac{\partial u}{\partial t}+\nabla\cdot\vec S=0.}
$$

A net outward energy flux decreases the energy stored in a volume. For a periodic steady state, the time average of $\partial u/\partial t$ is zero, giving the averaged balance used above. Later, absorption will introduce energy transferred from the field to matter.
```

## An antenna responds to field orientation

Two waves can carry the same average energy flux in the same direction, yet produce different signals in a receiver. We keep using complex phasors for harmonic fields, with $e^{j\omega t}$ understood. An ideal short linear receiving antenna responds to the electric field along its axis $\hat a$: its **voltage phasor** is proportional to

$$
\vec E\cdot\hat a.
$$

The antenna axis is a real unit vector. This projection gives a complex amplitude, so it keeps both the strength and phase of the received signal. With the same receiver and impedance conditions, average received power is proportional to

$$
\boxed{|\vec E\cdot\hat a|^2.}
$$

For a linearly polarized wave with phasor $\vec E=\hat xE_0e^{-jkz}$ and antenna axis $\hat a=\hat x\cos\theta+\hat y\sin\theta$,

$$
\vec E\cdot\hat a=E_0\cos\theta\,e^{-jkz},
\qquad
|\vec E\cdot\hat a|^2=E_0^2\cos^2\theta.
$$

Relative to the aligned receiver, the average received power is therefore reduced by the factor $\cos^2\theta$. This is **polarization mismatch**: rotating the receiver changes its signal even though the incident wave has not changed.

```{admonition} Same incident wave, different receiver
:class: question

Use the linearly polarized wave and antenna axis above, with real $E_0$.

1. Calculate the receiver's voltage phasor, apart from its proportionality constant, at $0^\circ$, $45^\circ$ and $90^\circ$.
2. Find the corresponding power fractions relative to an aligned receiver. Why do we square the magnitude of the phasor rather than just square the phasor?
3. Has the incident time-averaged Poynting vector changed when we rotate the receiver?
```

There are two different projections in this section. The surface integral projects **energy flux onto a surface normal**. The antenna response projects **electric field onto an antenna axis**. Their cosine factors describe different physical operations.

## The electric-field tip need not follow a line

Our examples so far have a fixed electric-field axis: they are **linearly polarized**. But two transverse components can have different phases. For propagation along $+z$, write the phasor

$$
\boxed{\vec E(z)=\left(\hat x A+\hat y B e^{j\delta}\right)e^{-jkz},}
$$

where $A,B$ are real, nonnegative component amplitudes and $\delta$ is their relative phase. The common factor $e^{-jkz}$ describes propagation; the vector in brackets describes the polarization. A phase factor multiplying the whole vector shifts the timing, but does not change the polarization.

To draw what the electric field actually does, take the real part after restoring $e^{j\omega t}$:

$$
\vec E_{\mathrm{real}}(z,t)
=\operatorname{Re}\{\vec E(z)e^{j\omega t}\}
=\hat x A\cos\psi+\hat y B\cos(\psi+\delta),
\qquad\psi=\omega t-kz.
$$

At one fixed position, watch the tip of this real vector as time passes:

- For $\delta=0$, both components vary together. The tip moves along a line, which need not coincide with an axis. A phase difference of $\pi$ also gives a line.
- For $A=B$ and $\delta=\pi/2$, the phasor is $A(\hat x+j\hat y)e^{-jkz}$ and the tip moves around a circle. This is **circular polarization**. Changing $+j$ to $-j$ reverses the rotation.
- More generally, the tip traces an ellipse: **elliptical polarization**. Linear and circular cases are special cases.

The electric field still lies in the transverse plane, perpendicular to propagation. Its tip rotating at one location is not a particle travelling along the propagation direction.

The phasor also makes the average energy flux straightforward:

$$
\vec E\cdot\vec E^*=A^2+B^2,
\qquad
\boxed{\langle\vec S\rangle=\frac{A^2+B^2}{2\eta_0}\hat z.}
$$

Changing the relative phase changes the tip path but, with $A,B$ fixed, does not change the total average energy flux of this vacuum plane wave. The response of a particular receiver can still change: it depends on the projected phasor.

### Try a different receiving antenna orientation

Start with the circular signal, as a GNSS-like example, and an ideal linear receiving antenna. The incident average intensity stays fixed when switching between linear and circular signals. The angle $\beta$ tilts the antenna axis relative to propagation; $\theta$ rotates it around that direction.

```{admonition} Predict, then try
:class: question

1. Keep the antenna transverse ($\beta=90^\circ$) and rotate it. How do received voltage and average power change for a linear signal? For a circular signal?
2. Point the antenna axis along propagation ($\beta=0^\circ$). Explain the result using $\vec E\cdot\hat a$.
3. Compare the displayed voltage phasor with the real voltage trace. Which part describes amplitude, and which part shifts the oscillation in time?
```

```{raw} html
:file: interactives/polarization_embed.html
```

```{admonition} Read the phasor, sketch the field
:class: question

Compare

$$
\vec E_1=A(\hat x+\hat y)e^{-jkz},\qquad
\vec E_2=A(\hat x+j\hat y)e^{-jkz}.
$$

1. Restore the time factor and take the real part. Sketch both tip paths at $z=0$.
2. Calculate $\vec E_1\cdot\vec E_1^*$ and $\vec E_2\cdot\vec E_2^*$. Do the waves have the same average energy flux?
3. For the circular case, calculate $|\vec E_{\mathrm{real}}(0,t)|^2$. Does its instantaneous energy flux oscillate like that of the linear case? Distinguish this real-field calculation from the phasor magnitude in question 2.
4. With receiver axis $\hat a=\hat x\cos\theta+\hat y\sin\theta$, show that the circular wave gives projected phasor $A(\cos\theta+j\sin\theta)e^{-jkz}$. What happens to its magnitude and phase as the receiver rotates?

A circular wave with component amplitude $A$ has the same average intensity as a linear wave with peak vector magnitude $\sqrt2 A$.
```

## From orientation to information about the Earth

A radar antenna can transmit one linear polarization and receive either that polarization or the perpendicular one. In radar labels such as VV and VH, the first letter specifies transmitted orientation and the second received orientation. Here H and V name horizontal and vertical polarization; H does not mean the magnetic field $\vec H$.

The returned polarization depends on the interaction with the target. Vegetation, surface geometry and material properties can change the relative components of the scattered field. Different channels therefore provide different information about the same scene. NASA's [NISAR polarimetry introduction](https://science.nasa.gov/mission/nisar/polarimetry/) illustrates this connection; a channel is not a unique label for one land-cover type.

<!--
```{admonition} Figure placeholder — one scene, two radar polarization channels
:class: note

A sourced pair of radar images of the same area in co- and cross-polarized channels, with a simple orientation sketch. Ask students which features change contrast and what extra information the second channel might contain. Interpretation should remain qualitative until scattering has been introduced.
```
-->

GNSS gives circular polarization a practical role: its transmitted signals use right-hand circular polarization, with receivers designed for that signal ([ESA Navipedia](https://gssc.esa.int/navipedia/index.php/Antennas)). The circular construction above is enough to understand what that means; naming the rotation sense requires an explicit viewing convention, which we will introduce when needed.

These signals also pass through the ionosphere. Later we can return to **Faraday rotation**: in Earth's magnetic field, different phase accumulation of two circular components can rotate a linearly polarized wave. That links propagation back to Earth's magnetic field and makes phase differences physically useful. An ideal circular wave has no fixed linear axis to rotate in this sense; circular polarization avoids this particular orientation-mismatch effect, not all ionospheric effects. See the short [JPL Faraday-rotation explanation](https://descanso.jpl.nasa.gov/propagation/PropagationDatabaseV6/Faraday.htm).

We now have a way to follow a wave from a source to a receiver: travel time and wavefront geometry describe its arrival; the Poynting vector describes energy transport; polarization and the receiver determine which field components are measured. Next comes the ground itself: how do material properties change propagation, and how do interfaces generate the return signal?

## Reading and sources

The geometry of spherical and locally plane waves can be compared with TU Delft's open [*Interactive Optics*, “Basic Electromagnetic and Wave Optics”](https://interactivetextbooks.tudelft.nl/tn2421/content/Chap1_Basics/Basics_2022_01Clean.html). The plane-wave field relations, polarization and energy calculations follow the standard framework in David H. Staelin's [*Electromagnetics and Applications*, Chapter 2](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/MIT6_013S09_chap02.pdf), especially §§2.3.4 and 2.7. The worked Cartesian checks and the deliberately incorrect field pair use this book's notation and geometry. The NASA, ESA and JPL pages linked above supply application context.
