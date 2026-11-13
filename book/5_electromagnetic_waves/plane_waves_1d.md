# One-dimensional plane electromagnetic waves

An Earth Observation (EO) radar sends out a pulse and listens for an echo. The echo arrives later because the electromagnetic disturbance needs time to travel. What exactly is travelling, and how do the electric and magnetic fields fit together?

## Changing fields sustain each other

Consider a region of vacuum with no charges and no currents. We describe the magnetic field by the **magnetic field strength** $\vec H$, in A/m, rather than the flux density $\vec B$ used in {doc}`history_maxwell`. In vacuum,

$$
\vec B=\mu_0\vec H.
$$

This is the same $\vec H$ as in the {doc}`electromagnetic diffusion chapter <../3_diffusion_fields/em_diffusion>`: the same magnetic field, described by a different quantity. In terms of $\vec E$ and $\vec H$, Maxwell's equations are

$$
\begin{aligned}
\vec\nabla\cdot\vec E&=0,
&\vec\nabla\times\vec E&=-\mu_0\frac{\partial\vec H}{\partial t},\\
\vec\nabla\cdot\vec H&=0,
&\vec\nabla\times\vec H&=\epsilon_0\frac{\partial\vec E}{\partial t}.
\end{aligned}
$$ (eq:em-plane-maxwell-vacuum)

The two divergence equations on the left say that this region contains no sources. The two curl equations on the right are the key to this whole chapter. Read them as sentences:

- **Faraday's law:** a magnetic field that changes in time comes with an electric field that varies in space.
- **Ampère–Maxwell law:** an electric field that changes in time comes with a magnetic field that varies in space.

So the change in time of each field is tied to the variation in space of the other. A changing $\vec H$ requires a spatially varying $\vec E$. If that $\vec E$ is also changing, it requires a spatially varying $\vec H$, and so on. Neither field can change on its own. This back-and-forth coupling is what allows a disturbance to travel, as we show next.

## Combining the curl equations gives a wave equation

We eliminate $\vec H$ from the two curl equations in three steps.

**1. Take the curl of Faraday's law.** For smooth fields we may swap the order of the space and time derivatives:

$$
\vec\nabla\times(\vec\nabla\times\vec E)=-\mu_0\frac{\partial}{\partial t}\left(\vec\nabla\times\vec H\right).
$$

**2. Substitute the Ampère–Maxwell law** for $\vec\nabla\times\vec H$:

$$
\vec\nabla\times(\vec\nabla\times\vec E)=-\mu_0\epsilon_0\frac{\partial^2\vec E}{\partial t^2}.
$$

The second time derivative appears because we have used both curl equations: a changing $\vec E$ is linked to $\vec H$, and that changing $\vec H$ is linked back to $\vec E$.

**3. Simplify the left-hand side.** The vector identity

$$
\vec\nabla\times(\vec\nabla\times\vec E)=\vec\nabla(\vec\nabla\cdot\vec E)-\nabla^2\vec E,
$$

together with Gauss's law $\vec\nabla\cdot\vec E=0$, leaves only $-\nabla^2\vec E$. Cancelling the minus signs gives

$$
\boxed{\nabla^2\vec E=\frac{1}{c^2}\frac{\partial^2\vec E}{\partial t^2},
\qquad c=\frac{1}{\sqrt{\mu_0\epsilon_0}}\simeq3.00\times10^8\ \mathrm{m/s}.}
$$ (eq:em-plane-wave-equation)

You have seen this derivation at the end of {doc}`history_maxwell`. The equation has the same structure as the {doc}`acoustic wave equation <../4_mechanical_waves/acoustic_waves>`; only the physical quantity and the speed have changed.

Pause on that speed. The constant $\epsilon_0$ describes the force between static charges, as in a charged capacitor; $\mu_0$ describes the force between wires carrying steady currents. Neither involves anything moving quickly, let alone light. Yet together they give $1/\sqrt{\mu_0\epsilon_0}\simeq3.00\times10^8\ \mathrm{m/s}$, the measured speed of light. The electric and magnetic properties of empty space set how fast an electromagnetic disturbance travels, just as the bulk modulus $K$ and the density $\rho$ set $c=\sqrt{K/\rho}$ for sound.

```{admonition} Use your intuition from mechanical waves
:class: question

For sound, the same two material properties $K$ and $\rho$ fix both the speed $c=\sqrt{K/\rho}$ and the {doc}`impedance <../4_mechanical_waves/impedance>` $\rho c=\sqrt{K\rho}$.

1. Combine $\mu_0$ and $\epsilon_0$ into a quantity with units of ohms. Evaluate it. What might it describe?
2. Inside a material, $\epsilon_0$ and $\mu_0$ are replaced by larger values $\epsilon$ and $\mu$. Would you expect light to travel faster or slower? The **refractive index** $n=c/v$ measures how much slower. Guess how $n$ depends on $\epsilon$ and $\mu$.
3. Could two materials have the same wave speed but different impedances? What would a wave notice at the boundary between them?
```

```{admonition} Now for the magnetic field
:class: question

Repeat the three steps, starting from the curl of the Ampère–Maxwell law. Which of Maxwell's equations do you substitute in step 2, and which in step 3? Show that $\vec H$ satisfies the same wave equation, with the same speed $c$.
```

Each field satisfies its own wave equation, but the two are not independent. The curl equations still link them: once $\vec E$ is known, $\vec H$ follows.

## A TEM wave travelling along z

The wave equation {eq}`eq:em-plane-wave-equation` allows many kinds of waves. For now we'll pick the simplest one, and write it in a notation that shows each choice we make.

**Choice 1: the wave travels along $z$, and it is uniform across every plane $z=\text{constant}$.** At any instant, the fields are the same everywhere on such a plane. This is a **uniform plane wave**. The fields depend only on $z$ and $t$, which we write as $(z,t)$, so every derivative with respect to $x$ or $y$ is zero.

**Choice 2: the fields are perpendicular to the propagation direction.** Neither $\vec E$ nor $\vec H$ has a $z$ component. This is a **transverse electromagnetic (TEM)** wave, the kind of wave that travels through vacuum.

**Choice 3: the $x$ axis points along $\vec E$.** We are free to orient the $x$ and $y$ axes this way.

Together, these choices give

$$
\boxed{\vec E=\hat x\,E_x(z,t).}
$$

Each part of this expression carries one piece of information:

| Notation | Meaning |
|---|---|
| $\hat x$ | the direction in which $\vec E$ points |
| $E_x$ | the size of $\vec E$ in V/m, with a sign: negative means pointing along $-x$ |
| $(z,t)$ | what $E_x$ depends on: position along $z$ and time, not $x$ or $y$ |

The field *points* along $x$ but *varies* along $z$. These are different directions, and the notation keeps them apart: the direction is in the unit vector, the variation is in the brackets.

```{admonition} Read the notation
:class: question

1. A field is written $\vec E=\hat y\,E_y(z,t)$. Which way does it point? Along which axis does it vary?
2. Is $\vec E=\hat z\,E_z(z,t)$ a TEM wave travelling along $z$?
3. Write the electric field of a TEM wave travelling along $x$, with $\vec E$ pointing along $z$.
```

### Where does the magnetic field point?

Faraday's law tells us. Because $E_x$ depends only on $z$ and $t$, the curl of $\vec E$ has a single term:

$$
\vec\nabla\times\vec E=\hat y\,\frac{\partial E_x}{\partial z}.
$$

Faraday's law sets this equal to $-\mu_0\,\partial\vec H/\partial t$, so the changing magnetic field points along $y$:

$$
\boxed{\vec H=\hat y\,H_y(z,t).}
$$

In the same way, $\vec\nabla\times\vec H=-\hat x\,\partial H_y/\partial z$, which points along $x$, as the Ampère–Maxwell law requires.

````{admonition} Check the curls
:class: dropdown

In Cartesian coordinates,

$$
\vec\nabla\times\vec E=
\hat x\left(\frac{\partial E_z}{\partial y}-\frac{\partial E_y}{\partial z}\right)
+\hat y\left(\frac{\partial E_x}{\partial z}-\frac{\partial E_z}{\partial x}\right)
+\hat z\left(\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial y}\right).
$$

With $E_y=E_z=0$ and no dependence on $x$ or $y$, only $\hat y\,\partial E_x/\partial z$ survives. For $\vec H=\hat y\,H_y(z,t)$, only the term $-\hat x\,\partial H_y/\partial z$ survives.
````

With these fields, the two vector curl equations of {eq}`eq:em-plane-maxwell-vacuum` become two scalar equations:

$$
\boxed{
\frac{\partial E_x}{\partial z}=-\mu_0\frac{\partial H_y}{\partial t},
\qquad
\frac{\partial H_y}{\partial z}=-\epsilon_0\frac{\partial E_x}{\partial t}.
}
$$ (eq:em-plane-coupled)

This is the coupling from the start of this page, now for a single pair of components: the variation along $z$ of each field is tied to the change in time of the other. Differentiating the first equation with respect to $z$ and substituting the second, the wave equation reduces to

$$
\frac{\partial^2 E_x}{\partial z^2}=\frac{1}{c^2}\frac{\partial^2 E_x}{\partial t^2},
$$ (eq:em-plane-wave-1d)

and $H_y$ obeys the same equation. This means that to fully describe a TEM wave, we only need to write the equations for either the E or the H field! That saves us a bit of time and effort. 

### Solving the wave equation

Equation {eq}`eq:em-plane-wave-1d` is the **one-dimensional wave equation**: a linear, second-order partial differential equation in which the second derivative in space is proportional to the second derivative in time. It has exactly the form of the equation for acoustic pressure in {doc}`../4_mechanical_waves/acoustic_waves`, with $p$ replaced by $E_x$ and $x$ by $z$.

Let us try a sinusoid:

$$
E_x(z,t)=E_0\cos(\omega t-kz).
$$ (eq:em-plane-cos-trial)

Here $E_0$ is the amplitude in V/m, $\omega$ is the angular frequency in rad/s, and $k$, the **wavenumber**, is its counterpart in space, in rad/m: it says how quickly the phase changes per metre. Each time derivative brings out a factor $\omega$, and each derivative along $z$ a factor $k$:

$$
\frac{\partial^2 E_x}{\partial t^2}=-\omega^2E_x,
\qquad
\frac{\partial^2 E_x}{\partial z^2}=-k^2E_x.
$$

Substituting into the wave equation gives $-k^2E_x=-(\omega^2/c^2)E_x$. For this to hold at every position and time,

$$
\boxed{k=\frac{\omega}{c}.}
$$ (eq:em-plane-dispersion)

Any frequency is allowed; the wave equation only fixes how the spatial frequency (aka the wavenumber) $k$ is tied to the temporal frequency $\omega$.

**What does the solution look like?** At a fixed time, $E_x$ is a cosine in $z$, with crests a wavelength $\lambda=2\pi/k$ apart. At a fixed position, it oscillates in time with period $T=2\pi/\omega$. Now follow one crest. Its phase $\omega t-kz$ stays constant, so as time increases by $\Delta t$ the crest moves by $\Delta z$ with $\omega\Delta t-k\Delta z=0$:

$$
\frac{\Delta z}{\Delta t}=\frac{\omega}{k}=c.
$$

The whole pattern travels along $+z$ at the speed of light, as drawn in {numref}`fig:em-plane-tem`.

```{figure} figures/plane_wave_tem.png
:name: fig:em-plane-tem
:width: 85%

Snapshot of a sinusoidal TEM wave travelling along $+z$. The electric field (blue) points along $\pm x$ and the magnetic field (orange) along $\pm y$; both vary only along $z$. The fields, and the propagation direction, are mutually perpendicular. $\vec H$ is not drawn to scale relative to $\vec E$.
```

**Is the sinusoid the only solution?** No. Using $k=\omega/c$, our solution can be written as $E_0\cos\bigl(\omega(t-z/c)\bigr)$: it depends on $z$ and $t$ only through the combination $t-z/c$. Because the wave equation is linear, sums of solutions are also solutions. We may add sinusoids of different frequencies, with any amplitudes and phases, and every one of them travels at the same speed $c$. As you know from *Signals and Time Series*, such sums can build almost any signal $F(t)$. The result is a waveform $F(t-z/c)$ that travels along $+z$ without changing shape: the general travelling-wave solution you met for {doc}`acoustic waves <../4_mechanical_waves/wave_equation_solutions>`. The wave equation fixes the speed; the shape is set by the source. In practice, we will mostly work with a single sinusoid, and look at it more closely in {doc}`harmonic_waves`.

```{admonition} Follow the solution
:class: question

1. Follow a crest of $E_0\cos(\omega t+kz)$. Which way does it move, and how fast?
2. Two sensors, $30\ \mathrm{m}$ apart along $z$, record the same wave. What is the time delay between their records? Does it depend on the frequency?
3. Substitute $E_x=E_0\cos(\omega t-kz)$ into the first equation of {eq}`eq:em-plane-coupled` to find $H_y$. Are $E_x$ and $H_y$ in phase? How is the ratio of their amplitudes related to the quantity in ohms you found earlier?
```

<!--

PREVIOUS VERSION, kept for reference while this page is reworked. Not rendered.

# One-dimensional plane electromagnetic waves

An Earth Observation (EO) radar sends out a pulse and listens for an echo. The echo arrives later because the electromagnetic disturbance needs time to travel. What exactly is travelling? How do the electric and magnetic fields fit together?

We can answer these questions with mathematics that is already familiar from mechanical waves. In this section we start with a general waveform; sinusoidal waves and complex notation follow in {doc}`harmonic_waves`. Throughout we consider propagation through vacuum. For many radar paths through air this is a useful first approximation; propagation through materials will come later.

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

If the source starts at $t=0$, a sensor at $z$ cannot see that onset until $t=z/c$. At the travelling onset, just as at any other marked feature, $t-z/c$ stays constant. In {doc}`radar_examples` we turn such a delay into a distance.

```{admonition} Follow the pulse
:class: tip

Before changing time, predict the new position of the marked peak. Use the controls below to move time forwards and backwards, and change the sensor position. Check the displayed value of $t-z/c$: does it change at the moving feature? What happens at a sensor that stays at one position? Compare the asymmetric shapes in the spatial snapshot and the time record.
```

```{raw} html
:file: interactives/pulse_embed.html
```

## Reading and sources

The time-domain-first approach follows David H. Staelin's open [*Electromagnetics and Applications*](https://www.ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/mit6_013_s09_coursetextbook.pdf), §§2.2–2.3. The derivations here use the geometry and notation chosen for this book.

REMOVED FROM "Solving the wave equation" (d'Alembert route with a pulse), 2026-11-11.

As there, the equation factorizes into two first-order parts:

$$
\left(\frac{\partial}{\partial z}-\frac{1}{c}\frac{\partial}{\partial t}\right)
\left(\frac{\partial}{\partial z}+\frac{1}{c}\frac{\partial}{\partial t}\right)E_x=0.
$$

Setting either factor to zero gives a one-way equation. The equation $\partial E_x/\partial z=-\frac{1}{c}\,\partial E_x/\partial t$ is solved by any function of $t-z/c$, and $\partial E_x/\partial z=+\frac{1}{c}\,\partial E_x/\partial t$ by any function of $t+z/c$. Because the wave equation is linear, we can add the two, giving the general solution

$$
\boxed{E_x(z,t)=F\!\left(t-\frac{z}{c}\right)+G\!\left(t+\frac{z}{c}\right).}
$$ (eq:em-plane-general-solution)

This is **d'Alembert's solution**. $F$ and $G$ are arbitrary functions with units of V/m: whatever shapes the sources produce.

```{admonition} Check by substitution
:class: dropdown

Set $\tau=t-z/c$, so that $E_x=F(\tau)$, and write $F'$ for $dF/d\tau$. Since $\partial\tau/\partial t=1$ and $\partial\tau/\partial z=-1/c$, the chain rule gives

$$
\frac{\partial^2 E_x}{\partial t^2}=F''(\tau),
\qquad
\frac{\partial^2 E_x}{\partial z^2}=\frac{1}{c^2}F''(\tau).
$$

So $\partial^2E_x/\partial z^2=(1/c^2)\,\partial^2E_x/\partial t^2$ for *any* twice-differentiable $F$. The same steps work for $G(t+z/c)$: the two factors $+1/c$ again multiply to $1/c^2$.
```

**What does the solution look like?** Take $F$ alone and follow one recognizable feature, such as its peak. That feature belongs to one particular value of the argument, so

$$
t-\frac{z}{c}=\text{constant}.
$$

If time increases by $\Delta t$, the feature must move by $\Delta z=c\,\Delta t$. The whole waveform slides along $+z$ at speed $c$ **without changing shape**. Likewise, $G(t+z/c)$ slides along $-z$. The wave equation fixes the speed, but it leaves the shape free: the shape is set by the source, such as a radar transmitter.

```{figure} figures/plane_wave_pulse.png
:name: fig:em-plane-pulse
:width: 95%

Top: two spatial snapshots of an asymmetric pulse $F(t-z/c)$ travelling along $+z$. The marked peak keeps $t-z/c=0$. Bottom: the time record at $z=150\ \mathrm{m}$. Reading each graph from left to right, the shape is reversed: the sensor sees the steep front first, then the long tail.
```

-->
