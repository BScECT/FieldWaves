# A dielectric can dissipate energy

The previous material followed the electric field instantly and without loss. Real bound charges and dipoles can have a slower, dissipative response. We first study that effect with **zero conduction**, $\sigma=0$. 
<!-- A material does not have to conduct DC current to attenuate a radar wave. -->

## A lag written in complex numbers

For harmonic fields we can still relate the displacement and electric fields, but now through a complex permittivity:

$$
\vec D=\epsilon_d(\omega)\vec E,
\qquad
\boxed{\epsilon_d=\epsilon'-j\epsilon''_d.}
$$ (eq:em-media-dielectric-epsilon)

Both $\epsilon'$ and $\epsilon''_d$ are real, in F/m. The subscript $d$ reminds us that we are describing the dielectric response; we have not included conductivity. For the passive materials considered here, $\epsilon''_d\geq0$ with our $e^{j\omega t}$ convention. Another time convention changes the sign, not the physics.

The complex number describes a response amplitude and a phase difference, just as a complex electric-field component does. Here it says that the material response can lag the applied field.

````{admonition} A small response model with a useful lesson
:class: dropdown

Suppose one polarization contribution follows the simple relaxation law

$$
\tau\frac{\partial\vec P}{\partial t}+\vec P
=\epsilon_0\chi_s\vec E,
$$

where $\tau>0$ is a response time and $\chi_s>0$ is a susceptibility. For harmonic fields, replace the time derivative by $j\omega$:

$$
(1+j\omega\tau)\vec P=\epsilon_0\chi_s\vec E,
\qquad
\vec P=\frac{\epsilon_0\chi_s}{1+j\omega\tau}\vec E.
$$

Using $\vec D=\epsilon_0\vec E+\vec P$ gives

$$
\epsilon_d=\epsilon_0\left(1+\frac{\chi_s}{1+j\omega\tau}\right),
$$

so

$$
\frac{\epsilon'}{\epsilon_0}=1+\frac{\chi_s}{1+(\omega\tau)^2},
\qquad
\frac{\epsilon''_d}{\epsilon_0}=\frac{\chi_s\omega\tau}{1+(\omega\tau)^2}.
$$

A real time-domain equation has produced a complex frequency response. Rationalizing the denominator lets us read its physical meaning. What happens when $\omega\tau$ is much smaller than one, equal to one, or much larger than one?

This is a simple single-relaxation model, not a complete description of every soil or water sample. A more realistic model can include several response times and a faster background response. [Baker-Jarvis and Kim's NIST review](https://nvlpubs.nist.gov/nistpubs/jres/117/jres.117.001.pdf) discusses the underlying mechanisms.
````

```{figure} figures/media_dielectric_lag.svg
:name: fig:em-media-lag
:width: 100%

A simple relaxing polarization with $\chi_s=4$. Left: at $\omega\tau=1$, the polarization lags the electric field by $45^\circ$; each trace is normalized by its own peak. Right: the model changes both the real and imaginary parts of permittivity with frequency. The imaginary part is a loss factor, not imaginary matter.
```

To see where the loss appears, look at the term in Ampère–Maxwell:

$$
j\omega\vec D
=\underbrace{\omega\epsilon''_d\vec E}_{\text{in phase with }\vec E}
+\underbrace{j\omega\epsilon'\vec E}_{\text{in quadrature}}.
$$

Why does the phase of this term tell us about energy loss? The quantity $j\omega\vec D$ is the phasor of the **displacement-current density**, $\partial\vec D/\partial t$. It includes the motion of bound charges through $\partial\vec P/\partial t$, even though the conduction current is zero. To find the associated power per unit volume, we take the dot product of the real electric field with this real current density. This is the local version of multiplying voltage by current to find electrical power.

At a fixed position, consider a field along one direction and choose the time origin so that its real component is $E(t)=E_a\cos(\omega t)$, where $E_a$ is the local peak amplitude. The two terms above then give the displacement-current component

$$
J_D(t)=\omega\epsilon''_d E_a\cos(\omega t)
-\omega\epsilon' E_a\sin(\omega t).
$$

The first contribution is **in phase** with the field: both reverse sign together. Their product is $\omega\epsilon''_d E_a^2\cos^2(\omega t)$, which is non-negative for a passive material. Energy therefore flows from the field into the material during both halves of the cycle. Since the cycle average of $\cos^2(\omega t)$ is $1/2$, this contribution gives the average loss density

$$
\langle p_{\mathrm{loss}}\rangle
=\frac12\omega\epsilon''_d E_a^2
\qquad [\mathrm{W/m^3}].
$$

The second contribution is **in quadrature**, meaning $90^\circ$ out of phase with the field. Its power contribution is proportional to $-\cos(\omega t)\sin(\omega t)$: it is positive during some parts of the cycle and negative during others, with zero cycle average. This describes energy exchange that returns energy to the field, rather than a net loss over a complete cycle. Below we will recover the same average loss density from the decrease in the wave's energy flux.

The same response can change $\epsilon'$ with frequency. Different harmonic components then have different phase speeds: the medium is **dispersive**. Our phasor calculation treats one frequency at a time. A broadband pulse may change shape as its components acquire different phases and attenuations.

## What field can travel through this material?

Use the same homogeneous, linear, isotropic bulk geometry as before, with real $\mu$ and complex $\epsilon_d$. Maxwell's equations are

$$
\nabla\times\vec E=-j\omega\mu\vec H,
\qquad
\nabla\times\vec H=j\omega\epsilon_d\vec E.
$$

Taking a curl and using $\nabla\cdot\vec E=0$ gives

$$
\nabla\times(\nabla\times\vec E)
=-j\omega\mu(j\omega\epsilon_d\vec E)
=\omega^2\mu\epsilon_d\vec E,
$$

$$
\boxed{\nabla^2\vec E+k^2\vec E=0,
\qquad k^2=\omega^2\mu\epsilon_d.}
$$ (eq:em-media-helmholtz)

This is still a spatial PDE. For the proposed transverse field $\vec E=\hat xE_x(z)$, it reduces to an ODE:

$$
\frac{d^2E_x}{dz^2}+k^2E_x=0.
$$

Let us try the familiar exponential, now with a complex wavenumber:

$$
\boxed{k=\beta-j\alpha,\qquad
E_x(z)=E_0e^{-jkz}=E_0e^{-\alpha z}e^{-j\beta z}.}
$$ (eq:em-media-decaying-wave)

Restoring time and taking the real part, for real $E_0$,

$$
E_{x,\mathrm{real}}(z,t)=E_0e^{-\alpha z}\cos(\omega t-\beta z).
$$

The envelope decays, while a fixed phase still travels: $\omega t-\beta z$ remains constant along a crest. Thus

$$
\lambda=\frac{2\pi}{\beta},\qquad v_p=\frac{\omega}{\beta}.
$$

Here $\beta$ is the phase wavenumber in rad/m: it measures angular spatial frequency. $\alpha$ is the attenuation constant, often expressed in Np/m. Both have inverse-length dimensions.

```{admonition} Make the candidate satisfy the equation
:class: question

1. Differentiate $E_0e^{-jkz}$ twice and substitute it into the ODE.
2. Expand $(\beta-j\alpha)^2$ and compare real and imaginary parts with $\omega^2\mu(\epsilon'-j\epsilon''_d)$. Show that

$$
\beta^2-\alpha^2=\omega^2\mu\epsilon',\qquad
2\alpha\beta=\omega^2\mu\epsilon''_d.
$$

3. For a forward travelling wave with $\beta>0$ and dielectric loss $\epsilon''_d>0$, what sign must $\alpha$ have?
4. Have we used conductivity anywhere in this calculation?
```

### The differential equation does not choose the boundary behaviour

For $k\ne0$, the general solution is

$$
E_x(z)=Ae^{-jkz}+Be^{jkz}.
$$

When $\alpha>0$, the first term decays into $z>0$ and the second grows. Both satisfy the differential equation. For a passive semi-infinite material driven at $z=0$, boundedness as $z\to\infty$ removes the growing term. Specifying $E_x(0)=E_0$ then fixes $A$. This is the familiar job of boundary conditions: the PDE alone is not the complete problem. In the lossless limit, boundedness alone no longer distinguishes the two directions; we also specify that no wave arrives from infinity.

### Retrieve the magnetic field from curl

For our candidate field, write out the Cartesian curl before simplifying:

$$
\begin{aligned}
\nabla\times\vec E={}&
\hat x\left(\frac{\partial E_z}{\partial y}-\frac{\partial E_y}{\partial z}\right)\\
&+\hat y\left(\frac{\partial E_x}{\partial z}-\frac{\partial E_z}{\partial x}\right)\\
&+\hat z\left(\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial y}\right)\\
={}&-jkE_x\hat y.
\end{aligned}
$$

Faraday's law therefore requires

$$
\boxed{\vec H=\hat y\frac{k}{\omega\mu}E_x,
\qquad \eta=\frac{E_x}{H_y}=\frac{\omega\mu}{k}.}
$$ (eq:em-media-complex-impedance)

The field directions remain transverse, perpendicular to propagation, and mutually perpendicular for this uniform plane wave. But $E_x$ and $H_y$ need not have the same temporal phase: their ratio is complex.

```{admonition} One curl is not enough
:class: question

Use $\vec H=\hat yH_y(z)$ to calculate $\nabla\times\vec H$ from its Cartesian components. Check Ampère–Maxwell explicitly. Which relation between $k$ and the material response makes it work? Check both divergences too.
```

## Where does the wave's energy go?

Keep the conjugate in the Poynting vector:

$$
\langle\vec S\rangle=\frac12\operatorname{Re}\{\vec E\times\vec H^*\}
=\hat z\frac{\beta}{2\omega\mu}|E_0|^2e^{-2\alpha z}.
$$ (eq:em-media-decaying-flux)

Field amplitude decays as $e^{-\alpha z}$; average power flux decays as $e^{-2\alpha z}$. The area of our plane wave has not expanded. Energy is going into the material.

```{admonition} Read the divergence as an energy budget
:class: question

1. Write the full Cartesian divergence of $\langle\vec S\rangle$. Which terms vanish here?
2. Differentiate the remaining component and use $2\alpha\beta=\omega^2\mu\epsilon''_d$ to obtain

$$
\boxed{-\nabla\cdot\langle\vec S\rangle
=\frac{\omega\epsilon''_d}{2}|\vec E|^2.}
$$

3. Check that the right-hand side has units W/m$^3$. What does its sign mean?
4. Surround a slice $z_1<z<z_2$ by a box of cross-sectional area $A$. Use Gauss's theorem to show that the deposited power is $A[\langle S_z(z_1)\rangle-\langle S_z(z_2)\rangle]$.
```

The loss is dielectric heating. The in-phase response identified earlier now appears as a local energy budget.

```{admonition} Predict the field and the power
:class: question

Start with zero conductivity in the activity below. Increase dielectric loss: what changes in the envelope, spatial phase and power? Then make the dielectric loss zero as well. Does raising the real permittivity alone restore attenuation?

The plot length is a physical distance. Change it if many oscillations fit in the window; do not confuse moving the plot boundary with changing the material.
```

```{raw} html
:file: interactives/media_wave_embed.html
```

Conductivity is included as an optional control for the next page; it starts switched off. The activity holds $E_x(0)$ fixed and shows the energy flux relative to its value just inside the material. Surface transmission and spreading are not part of this comparison.

Define the **field attenuation depth**

$$
\boxed{\delta_E=\frac1\alpha.}
$$

At this distance the field amplitude is $1/e$ of its initial value, while the average flux is $1/e^2$. The one-way $1/e$ **power** depth is $1/(2\alpha)$. We will meet the same field depth as the conductor's skin depth.

The propagation framework follows [Ellingson's treatment of waves in lossy media](https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electromagnetics_II_(Ellingson)/03:_Wave_Propagation_in_General_Media) and [Staelin, section 9.2.4](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/MIT6_013S09_chap09.pdf). Our dielectric example keeps conductivity absent so that the two physical loss mechanisms remain visible.
