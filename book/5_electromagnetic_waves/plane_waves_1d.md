# One-dimensional plane electromagnetic waves

An Earth Observation (EO) radar sends out a pulse and listens for an echo. The echo arrives later because the electromagnetic disturbance needs time to travel. What exactly is travelling? How do the electric and magnetic fields fit together? And why do radar people keep writing complex exponentials?

We can answer these questions with mathematics that is already familiar from mechanical waves. We will start with a waveform, and then we will move to sinusoidal functions. Throughout this section we consider propagation through vacuum. For many radar paths through air this is a useful first approximation; propagation through materials will come later.

## A familiar equation, with different fields

At the end of {doc}`history_maxwell`, Maxwell's equations gave us

$$
\nabla^2\vec E=\frac{1}{c^2}\frac{\partial^2\vec E}{\partial t^2},
\qquad c=\frac{1}{\sqrt{\mu_0\epsilon_0}}.
$$ (eq:em-plane-wave-equation)

Compare this with the {doc}`acoustic wave equation <../4_mechanical_waves/acoustic_waves>`. The mathematical structure is the same. We have changed the physical quantity and the propagation speed, but we have not changed the kind of equation.

In this section we keep things *simple* by letting the field depend only on one Cartesian spatial coordinate, $z$, as well as time. At a given time, the electric field is identical everywhere on any plane $z=\text{constant}$. This is a **uniform plane wave**. “One spatial dimension” describes how the field varies, not how many components a vector may have. So, in general, for the electric field we will have

$$
   \vec{E}(x,y,z,t) = \vec{E}(z,t) = E_x(z,t) \hat x + E_y(z,t) \hat y + E_z(z,t) \hat z.
$$

Since $\nabla^2$ and the time derivative are linear operators, the wave equation applies to the individual components, for example:

$$
  \nabla^2 E_x = \frac{1}{c^2}\frac{\partial^2 E_x}{\partial t^2}
$$

```{admonition} Read the geometry from the equation
:class: question

Write out $\nabla^2 E_x$ in Cartesian coordinates. Which terms vanish if $E_x$ depends only on $z$ and $t$? Does the subscript $x$ mean the field must vary with $x$?
```

For this geometry each component satisfies an equation of the form

$$
\frac{\partial^2 E_x}{\partial z^2}
=\frac{1}{c^2}\frac{\partial^2 E_x}{\partial t^2}.
$$

The component points along $x$; its variation is along $z$. Keep those two statements separate.

## A travelling waveform

Recall the {doc}`travelling-wave solutions <../4_mechanical_waves/wave_equation_solutions>` from mechanical waves. Let us try

$$
\vec E(z,t)=\hat x F(t-z/v),
$$ (eq:em-plane-trial)

where $F$ is a waveform with units of electric field, V/m. It might be a pulse with a clear beginning and end, or a smoother disturbance. The parameter $v>0$ is the speed we want to find.

The chain rule gives

$$
\frac{\partial E_x}{\partial t}=F'(t-z/v),
\qquad
\frac{\partial E_x}{\partial z}=-\frac{1}{v}F'(t-z/v),
$$

and therefore

$$
\frac{\partial^2 E_x}{\partial t^2}=F''(t-z/v),
\qquad
\frac{\partial^2 E_x}{\partial z^2}=\frac{1}{v^2}F''(t-z/v).
$$

A prime means differentiation with respect to the argument of $F$. Substitution in the wave equation shows that a general waveform works when $v=c$. The equation fixes the speed, while the waveform itself is set by how the wave is generated.

```{admonition} A closer look at the chain rule
:class: dropdown

Set $\tau=t-z/v$, so that $E_x=F(\tau)$. Then

$$
\frac{\partial\tau}{\partial t}=1,
\qquad
\frac{\partial\tau}{\partial z}=-\frac{1}{v}.
$$

The chain rule makes the two factors explicit:

$$
\frac{\partial E_x}{\partial t}
=\frac{dF}{d\tau}\frac{\partial\tau}{\partial t}=F'(\tau),
\qquad
\frac{\partial E_x}{\partial z}
=\frac{dF}{d\tau}\frac{\partial\tau}{\partial z}=-\frac{1}{v}F'(\tau).
$$

Differentiate once more in the same way. Each spatial derivative supplies a factor $-1/v$, giving $+1/v^2$ for the second spatial derivative.
```

### Follow a feature, not a fixed position

Pick a recognizable feature of the pulse, such as its central peak. That feature corresponds to a particular argument $\tau_*$ of $F$. As it travels,

$$
\boxed{t-\frac{z}{v}=\tau_*\quad\text{stays constant}.}
$$ (eq:em-plane-feature)

If time increases by $\Delta t$, the feature must move by

$$
\Delta z=v\Delta t
$$

to keep the argument unchanged. This is why $F(t-z/v)$ travels towards increasing $z$. At a **fixed position**, on the other hand, the argument changes with time and we observe the waveform passing by.

```{figure} figures/plane_wave_pulse.png
:name: fig:em-plane-pulse
:width: 95%

Top: two spatial snapshots of an asymmetric pulse travelling along $+z$ at $v=c$. The marked peak keeps $t-z/c=0$. Bottom: the time record at $z=150\ \mathrm{m}$. Reading each graph from left to right, the shape is reversed: the sensor sees the steep front first, then the long tail.
```

Notice that the two kinds of graph read the waveform in opposite directions. At a fixed time, increasing $z$ makes $t-z/v$ **decrease**. At a fixed position, increasing $t$ makes it **increase**. The asymmetric pulse makes this visible: in a spatial snapshot its steep front is on the right, while the fixed sensor records a rapid rise followed by a long decay. The sensor encounters the right-hand side of the approaching pulse first.

```{admonition} Which way does it go?
:class: question

1. Follow a feature of $F(t+z/v)$. As time increases, must its position increase or decrease?
2. Two sensors are separated by $30\ \mathrm{m}$ along the propagation direction. What is the delay between their records in vacuum?
3. Sketch the time record at a fixed sensor from the spatial snapshot. Which side of the pulse arrives first? Explain the reversal using $t-z/v$.
```

A plane wave is an exact solution, but we would not generally expect an antenna somewhere to produce an infinite flat wavefront. Waves from a localized source spread out with curved fronts, more like expanding spherical shells. That is also an idealized picture: a real antenna does not radiate equally in every direction. Far enough from the source, a small patch of the curved front looks almost flat, and a plane wave becomes a useful local approximation.

```{admonition} How far is far? — optional
:class: dropdown

The region sufficiently far from an antenna is called its **far field**. Here the radiated field has the simple transverse-wave behaviour that we develop below, and we can use a plane wave over a small observation region.

For an antenna whose largest dimension is $D$, a commonly used estimate is

$$
R\gtrsim\frac{2D^2}{\lambda},
$$

where $R$ is distance from the antenna and $\lambda$ is the wavelength—the distance between successive crests of a harmonic wave. We also require $R\gg D$ and $R\gg\lambda$. These are practical conditions, not a sharp boundary where the physics suddenly changes.

Closer to the antenna, in the **near field**, the geometry and the relation between $\vec E$ and $\vec H$ can be more complicated. We will leave that for another day.

For the antenna-size criterion, see [Staelin, §11.1](https://www.ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/mit6_013_s09_coursetextbook.pdf#page=342).
```

## The magnetic field: switching from B to H

So far we have used $\vec B$, the magnetic flux density, measured in tesla. We now use the **magnetic field strength** $\vec H$, measured in A/m. In vacuum,

$$
\boxed{\vec B=\mu_0\vec H.}
$$

This is the same $H$ notation used in the {doc}`electromagnetic diffusion chapter <../3_diffusion_fields/em_diffusion>`. We are describing the same magnetic field using a different quantity; no extra physical field has appeared.

In a region without charges or currents, Maxwell's equations become

$$
\begin{aligned}
\vec\nabla\cdot\vec E&=0,
&\vec\nabla\cdot\vec H&=0,\\
\vec\nabla\times\vec E&=-\mu_0\frac{\partial\vec H}{\partial t},
&\vec\nabla\times\vec H&=\epsilon_0\frac{\partial\vec E}{\partial t}.
\end{aligned}
$$ (eq:em-plane-maxwell)

The wave equation came from these equations. We must still check that our proposed electric and magnetic fields satisfy the complete set.

## Which way do the fields point?

First consider the divergence equations. In Cartesian coordinates, the divergence of the electric field is

$$
\vec\nabla\cdot\vec E
=\frac{\partial E_x}{\partial x}
+\frac{\partial E_y}{\partial y}
+\frac{\partial E_z}{\partial z}.
$$

Here all field components depend only on $z$ and $t$. Moving along $x$ or $y$ does not change them, so

$$
\vec\nabla\cdot\vec E
=\underbrace{\frac{\partial E_x}{\partial x}}_{0}
+\underbrace{\frac{\partial E_y}{\partial y}}_{0}
+\frac{\partial E_z}{\partial z}
=\frac{\partial E_z}{\partial z}.
$$

The transverse components $E_x$ and $E_y$ themselves can still be nonzero. Gauss's law now gives $\partial E_z/\partial z=0$. Applying the same reasoning to the magnetic field gives

$$
\vec\nabla\cdot\vec H
=\frac{\partial H_z}{\partial z}=0.
$$

The $z$ components cannot vary along $z$. The $z$ components of the two curl equations also give

$$
\frac{\partial H_z}{\partial t}=0,
\qquad
\frac{\partial E_z}{\partial t}=0.
$$

So these components can only be steady backgrounds. Leaving those backgrounds aside, the wave fields have no component along the propagation direction. They are **transverse**, as you have seen for shear waves, although there is no material displacement here.

Now choose $\vec E=\hat x E_x(z,t)$.

```{admonition} Let the curl tell us the direction
:class: question

Write out $\vec\nabla\times\vec E$ in Cartesian components. Which component survives? Use Faraday's law to identify the direction of the changing magnetic field.
```

````{admonition} Check your curl
:class: dropdown

The full expression is

$$
\vec\nabla\times\vec E=
\hat x\left(\frac{\partial E_z}{\partial y}-\frac{\partial E_y}{\partial z}\right)
+\hat y\left(\frac{\partial E_x}{\partial z}-\frac{\partial E_z}{\partial x}\right)
+\hat z\left(\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial y}\right).
$$

Only $\hat y\,\partial E_x/\partial z$ remains. Faraday's law therefore couples $E_x$ to $H_y$. With $\vec H=\hat y H_y(z,t)$, the two curl equations reduce to

$$
\boxed{
\frac{\partial E_x}{\partial z}=-\mu_0\frac{\partial H_y}{\partial t},
\qquad
\frac{\partial H_y}{\partial z}=-\epsilon_0\frac{\partial E_x}{\partial t}.
}
$$ (eq:em-plane-coupled)

Notice the minus sign in the second equation: the $x$ component of $\vec\nabla\times\vec H$ is $-\partial H_y/\partial z$.
````

For a forward waveform $E_x=F(t-z/c)$, the first equation becomes

$$
-\frac{1}{c}F'(t-z/c)
=-\mu_0\frac{\partial H_y}{\partial t}.
$$

Matching the time derivatives gives the companion wave field

$$
\boxed{\vec H(z,t)=\hat y\frac{F(t-z/c)}{\eta_0},
\qquad
\eta_0=\mu_0c=\sqrt{\frac{\mu_0}{\epsilon_0}}\simeq377\ \Omega.}
$$ (eq:em-plane-impedance)

An added steady field is again left aside. Substituting this pair into the other curl equation checks that the speed is indeed $c$.

The factor $\eta_0$ is the **wave impedance of vacuum**. Its units follow directly from $(\mathrm{V/m})/(\mathrm{A/m})=\Omega$. This should remind you of the {doc}`pressure–particle-velocity impedance <../4_mechanical_waves/impedance>`: the wave has two coupled fields, and their amplitudes are related.

For this wave, $\vec E$, $\vec H$ and the propagation direction are mutually perpendicular:

$$
\vec H=\frac{1}{\eta_0}\hat z\times\vec E.
$$

Sketch these three directions with your right hand. Both fields have the **same waveform at the same time**; one is not waiting for the other to catch up.

```{admonition} Reverse the wave
:class: question

Keep the electric field along $x$, but let $E_x=G(t+z/c)$. Substitute it into the coupled equations to determine $H_y$. What changes sign?
```

For waves travelling in both directions, superposition gives

$$
\begin{aligned}
E_x(z,t)&=F(t-z/c)+G(t+z/c),\\
H_y(z,t)&=\frac{1}{\eta_0}\bigl[F(t-z/c)-G(t+z/c)\bigr].
\end{aligned}
$$ (eq:em-plane-two-directions)

The simple amplitude ratio applies to each travelling wave separately. The ratio of the total fields need not be $\eta_0$, something that will matter when reflected waves enter the picture.

## Why does a change need time to travel?

Could we simply have the electric and magnetic fields change everywhere at once?

```{admonition} Try the idea in Maxwell's equations
:class: question

Suppose $\vec E=\hat x f(t)$ and $\vec H=\hat y g(t)$, with both fields independent of position in a source-free region. Evaluate their curls. What do Maxwell's equations then say about $f$ and $g$?
```

Both curls are zero, so both time derivatives must be zero. Uniform steady fields are possible; this proposed uniform time variation is not. A changing wave field needs spatial variation as well.

For a wave travelling in the positive $z$ direction, substitute $H_y=E_x/\eta_0$ into Faraday's law:

$$
\frac{\partial E_x}{\partial z}
=-\frac{1}{c}\frac{\partial E_x}{\partial t}.
$$ (eq:em-plane-one-way)

Read this as a sentence: **a spatial change and a time change are linked by the propagation speed**. It is the same first-order structure encountered for mechanical waves.

Suppose a source at $z=0$ imposes the waveform $F(t)$, the region ahead is initially undisturbed, and there is no wave coming back towards the source. Then

$$
E_x(z,t)=F(t-z/c).
$$

If the source starts at $t=0$, a sensor at $z$ cannot see that onset until $t=z/c$. At the travelling onset, just as at any other marked feature, $t-z/c$ stays constant.

### Radar: a delay becomes a distance

For a radar receiving an echo from a stationary target, the pulse travels out and back. Approximating the path by vacuum,

$$
\Delta t=\frac{2R}{c},\qquad
\boxed{R=\frac{c\Delta t}{2}.}
$$

Here $R$ is the distance along the line of sight, or **slant range**. At $R=600\ \mathrm{km}$, the round-trip time is about $4\ \mathrm{ms}$. We will deal with what creates an echo later; for now, its travel time already tells us something useful.

Ground-penetrating radar uses the same basic idea below the surface. There, turning a delay into a depth also requires knowing the propagation speed in the ground. That is one reason to study materials later.

```{admonition} Follow the pulse
:class: tip

Before changing time, predict the new position of the marked peak. Use the controls below to move time forwards and backwards, and change the sensor position. Check the displayed value of $t-z/c$: does it change at the moving feature? What happens at a sensor that stays at one position? Compare the asymmetric shapes in the spatial snapshot and the time record.
```

```{raw} html
:file: interactives/pulse_embed.html
```

## Harmonic waves: frequency in time and in space

Now we are going to consider sinusoidal signals. As you know *Signals and Time Series*, most signals of interest can be build from a sumation of cosines and sines. Moreover, in many cases, most of the analysis of interest can be done considering a **monochromatic** wave, i.e. a cosine or a singe at a single frequency. We  choose a particular waveform:

$$
E_x(z,t)=E_0\cos(\omega t-kz+\phi).
$$ (eq:em-plane-harmonic-real)

At one position this is an oscillation in time. At one time it is an oscillation in space. The two frequencies are

$$
\omega=2\pi f=\frac{2\pi}{T},\qquad
\boxed{k=\frac{2\pi}{\lambda}.}
$$

The **wavenumber $k$ is angular spatial frequency**: phase change per metre, measured in rad/m. It plays the same role for position that $\omega$ plays for time. If we count whole cycles rather than radians, the spatial frequency is $1/\lambda$, just as ordinary temporal frequency is $f=1/T$.

| | Time, at fixed position | Space, at fixed time |
|---|---|---|
| One full cycle | Period $T$ in s | Wavelength $\lambda$ in m |
| Cycles per unit | $f=1/T$ in Hz | $1/\lambda$ in cycles/m |
| Radians per unit | $\omega=2\pi f$ in rad/s | $k=2\pi/\lambda$ in rad/m |

For example, a wavelength of $3\ \mathrm{cm}$ means about $33$ cycles per metre, or $k\simeq209\ \mathrm{rad/m}$. Moving $1\ \mathrm{cm}$ along a snapshot changes the phase by one third of a cycle: $2\pi/3$ radians in magnitude. A larger wavenumber means more closely spaced oscillations, not a faster wave.

```{figure} figures/plane_wave_spatial_frequency.png
:name: fig:em-plane-spatial-frequency
:width: 95%

A harmonic wave viewed in time at one position (left) and in space at one time (right). Here $f=100\ \mathrm{MHz}$, $T=10\ \mathrm{ns}$, $\lambda\simeq3\ \mathrm{m}$ and $k\simeq2.09\ \mathrm{rad/m}$. These are two ways of looking at the same wave.
```

Follow a crest. Its phase stays constant:

$$
\omega t-kz+\phi=\text{constant}.
$$

For changes along that crest, $\omega\Delta t-k\Delta z=0$, and hence

$$
\frac{\Delta z}{\Delta t}=\frac{\omega}{k}=c,
\qquad
\boxed{\omega=ck.}
$$

This is the harmonic version of keeping $t-z/c$ constant. Frequency and wavenumber are linked by the propagation speed: $c=f\lambda$.

```{admonition} Read a wave as a sentence
:class: question

A vacuum wave has $E_x=E_0\cos(2\pi\,10^8t-kz)$, using seconds and metres.

1. Find $f$, $T$, $\lambda$ and $k$, with units.
2. How much does its phase change over half a wavelength at one instant?
3. What changes if the sign before $kz$ becomes positive?
4. If the frequency doubles in vacuum, what happens to $k$, $\lambda$ and the speed?
```

## Complex fields: the usual working language

Keeping track of amplitudes and phases with cosines soon gets tiresome. Euler's identity gives us a more convenient language:

$$
\cos\theta=\operatorname{Re}\{e^{i\theta}\}.
$$

We can represent the same harmonic field by the complex expression

$$
\boxed{E_x(z,t)=E_0e^{i(\omega t-kz+\phi)}.}
$$ (eq:em-plane-harmonic-complex)

Formally, the measurable field is the **real part** of this expression. In practice, we will use the same symbol and treat harmonic fields as complex-valued, remembering to take the real part when we want the physical field. This is standard working practice in electromagnetics; getting comfortable with it will make the subject much easier.

We can also separate out the time dependence:

$$
E_x(z,t)=E_x(z)e^{i\omega t},\qquad
E_x(z)=E_0e^{i\phi}e^{-ikz}.
$$

The time-independent complex amplitude $E_x(z)$ is called a **phasor**. It stores both amplitude and phase. To recover the physical field, use $\operatorname{Re}\{E_x(z)e^{i\omega t}\}$. Using the same symbol is slightly ambiguous, but the context tells us which representation we mean.

### What do we gain?

For a harmonic field,

$$
\frac{\partial\vec E}{\partial t}=i\omega\vec E,
$$

and for a wave travelling along $+z$,

$$
\frac{\partial\vec E}{\partial z}=-ik\vec E.
$$

Differentiation becomes multiplication. Maxwell's curl equations, written for the phasors, are then

$$
\vec\nabla\times\vec E=-i\omega\mu_0\vec H,
\qquad
\vec\nabla\times\vec H=i\omega\epsilon_0\vec E.
$$ (eq:em-plane-phasor-maxwell)

The curl still has its geometric meaning. Complex notation handles the harmonic time dependence; it does not replace vector calculus.

There is a second payoff. Delaying a harmonic signal by $\Delta t$ multiplies it by

$$
e^{-i\omega\Delta t}.
$$

A one-way propagation distance $R$ therefore contributes $e^{-ikR}$. For a radar echo, the round-trip propagation contributes $e^{-i2kR}$, in addition to the target's own scattering response. Now a phase factor is a compact way of describing a journey.

Our choice of $e^{+i\omega t}$ agrees with the {doc}`Fourier convention used for mechanical waves <../4_mechanical_waves/impedance>`. With this convention, a forward-travelling wave has $e^{-ikz}$. Changing convention is possible, but changing it halfway through a calculation is asking for trouble.

### What about the pulse we started with?

A pulse is not a single harmonic wave. Fourier analysis lets us build it from harmonic components with different frequencies, amplitudes and phases. Because Maxwell's equations are linear, we can solve for those components separately and add them afterwards. This is why harmonic solutions are useful even when the radar transmits a pulse.

```{admonition} Turn up the spatial frequency
:class: tip

Change the temporal frequency and compare the time trace with the spatial snapshot below. Predict what will happen to the spacing between crests before moving the slider. Watch $\omega$, $k$, $T$ and $\lambda$ together. Increasing frequency changes how many oscillations fit into a second and a metre; in vacuum it does not change the speed.
```

```{raw} html
:file: interactives/frequency_embed.html
```

## The same mathematics on a transmission line

The pulse also needs time to travel through the cable feeding a radar antenna. We can understand this using the same field equations, with **voltage and current** taking the roles of our two coupled quantities.

Consider two ideal conducting plates, separated by a distance $d$ along $x$, wide along $y$, and extending along $z$. Let their width be $w\gg d$, so we can neglect fields near the side edges. Between them we use the same transverse fields $E_x(z,t)$ and $H_y(z,t)$.

```{figure} figures/plane_wave_parallel_plates.png
:name: fig:em-plane-line
:width: 85%

Cross-section of an ideal parallel-plate line, looking along $+z$. The electric field points across the gap. The magnetic field runs across the width. The conductor current $I$ is positive along $+z$ on the lower plate; the upper plate carries the return current. The geometry is schematic.
```

Define the voltage across the gap at a given $z$, and the current along the lower plate, by

$$
V(z,t)=dE_x(z,t),\qquad I(z,t)=wH_y(z,t).
$$

The first relation comes from integrating the electric field across the gap. The second comes from Ampère's law around the plate, neglecting edge fields. We now multiply the coupled field equations by $d$ and $w$:

$$
\frac{\partial V}{\partial z}
=-\frac{\mu_0d}{w}\frac{\partial I}{\partial t},
\qquad
\frac{\partial I}{\partial z}
=-\frac{\epsilon_0w}{d}\frac{\partial V}{\partial t}.
$$

The geometry gives two parameters,

$$
L'=\frac{\mu_0d}{w}\quad[\mathrm{H/m}],\qquad
C'=\frac{\epsilon_0w}{d}\quad[\mathrm{F/m}],
$$

the **inductance per unit length** and **capacitance per unit length**. Here the prime means “per unit length”, not a derivative. Our equations become the **lossless telegrapher's equations**:

$$
\boxed{
\frac{\partial V}{\partial z}=-L'\frac{\partial I}{\partial t},
\qquad
\frac{\partial I}{\partial z}=-C'\frac{\partial V}{\partial t}.
}
$$ (eq:em-plane-telegrapher)

Differentiate the first equation with respect to $z$ and substitute the second. For constant line parameters,

$$
\frac{\partial^2 V}{\partial z^2}=L'C'\frac{\partial^2 V}{\partial t^2}.
$$

Another wave equation! Its speed and forward-wave voltage–current ratio are

$$
v_{\mathrm{line}}=\frac{1}{\sqrt{L'C'}},\qquad
Z_0=\sqrt{\frac{L'}{C'}}.
$$

For these vacuum-filled plates, $v_{\mathrm{line}}=c$ and $Z_0=\eta_0d/w$. Both $Z_0$ and $\eta_0$ have units of ohms, but the line impedance also depends on geometry. Real cables contain other materials and have losses; we will return to those effects later.

```{admonition} Recognize the structure
:class: question

Compare the telegrapher's equations with the coupled equations for $E_x,H_y$, and with the earlier equations for acoustic pressure and particle velocity. Which quantities play corresponding mathematical roles? Which physical directions are different?
```

We now have three settings—acoustics, unguided electromagnetic waves and transmission lines—with a common mathematical structure. Two coupled first-order equations give a wave equation; a waveform travels with a definite speed; and an impedance relates its two quantities. Recognizing that structure lets us reuse what we already know.

## Reading and sources

The time-domain-first approach follows David H. Staelin's open [*Electromagnetics and Applications*](https://www.ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/mit6_013_s09_coursetextbook.pdf), §§2.2–2.3; §7.1 develops the transmission-line connection. The derivations here use the geometry and notation chosen for this book. A complementary treatment of one-dimensional waves and lines is Haus and Melcher's [*Electromagnetic Fields and Energy*, Chapter 14](https://ocw.mit.edu/courses/res-6-001-electromagnetic-fields-and-energy-spring-2008/pages/chapter-14/).
