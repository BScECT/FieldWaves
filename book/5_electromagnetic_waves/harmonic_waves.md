# Harmonic waves and complex notation

In {doc}`plane_waves_1d` we found that a sinusoid $E_0\cos(\omega t-kz)$ solves the wave equation provided $k=\omega/c$, and that sums of such sinusoids give travelling waves of any shape. We now look more closely at a single sinusoid, and introduce the complex notation that radar engineers and electromagnetics textbooks use almost everywhere.

## Harmonic waves: frequency in time and in space

Now we are going to consider sinusoidal signals. As you know from *Signals and Time Series*, most signals of interest can be built from a summation of cosines and sines. Moreover, in many cases, most of the analysis of interest can be done considering a **monochromatic** wave, i.e. a cosine or a sine at a single frequency. We choose a particular waveform:

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
\cos\theta=\operatorname{Re}\{e^{j\theta}\}.
$$

Using $j$ for the imaginary unit, $j^2=-1$, we can represent the same harmonic field by the complex expression

$$
\boxed{E_x(z,t)=E_0e^{j(\omega t-kz+\phi)}.}
$$ (eq:em-plane-harmonic-complex)

Formally, the measurable field is the **real part** of this expression. In practice, we will use the same symbol and treat harmonic fields as complex-valued, remembering to take the real part when we want the physical field. This is standard working practice in electromagnetics; getting comfortable with it will make the subject much easier.

We can also separate out the time dependence:

$$
E_x(z,t)=E_x(z)e^{j\omega t},\qquad
E_x(z)=E_0e^{j\phi}e^{-jkz}.
$$

The time-independent complex amplitude $E_x(z)$ is called a **phasor**. It stores both amplitude and phase. To recover the physical field, use $\operatorname{Re}\{E_x(z)e^{j\omega t}\}$. Using the same symbol is slightly ambiguous, but the context tells us which representation we mean.

### Simplifying derivatives using phasors

For a harmonic field,

$$
\frac{\partial\vec E}{\partial t}=j\omega\vec E,
$$

and for a wave travelling along $+z$,

$$
\frac{\partial\vec E}{\partial z}=-jk\vec E.
$$

Differentiation becomes multiplication. Maxwell's curl equations, written for the phasors, are then

$$
\vec\nabla\times\vec E=-j\omega\mu_0\vec H,
\qquad
\vec\nabla\times\vec H=j\omega\epsilon_0\vec E.
$$ (eq:em-plane-phasor-maxwell)

The curl still has its geometric meaning. Complex notation handles the harmonic time dependence; it does not replace vector calculus.

Our choice of $e^{+j\omega t}$ agrees with the {doc}`Fourier convention used for mechanical waves <../4_mechanical_waves/impedance>`. With this convention, a forward-travelling wave has $e^{-jkz}$. Changing convention is possible, but changing it halfway through a calculation is asking for trouble.

### What about a radar pulse?

A radar usually transmits a short pulse, not an endless sinusoid. A pulse is not a single harmonic wave, but, as we saw in {doc}`plane_waves_1d`, Fourier analysis lets us build it from harmonic components with different frequencies, amplitudes and phases. Because Maxwell's equations are linear, we can solve for those components separately and add them afterwards. This is why harmonic solutions are useful even when the radar transmits a pulse.

```{admonition} Turn up the spatial frequency
:class: tip

Change the temporal frequency and compare the time trace with the spatial snapshot below. Predict what will happen to the spacing between crests before moving the slider. Watch $\omega$, $k$, $T$ and $\lambda$ together. Increasing frequency changes how many oscillations fit into a second and a metre; in vacuum it does not change the speed.
```

```{raw} html
:file: interactives/frequency_embed.html
```
