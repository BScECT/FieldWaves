# Lab: Plane electromagnetic waves

:::{admonition} Pen-and-paper exercises
:class: note

These exercises accompany {doc}`../plane_waves_1d`, {doc}`../harmonic_waves` and {doc}`../radar_examples`. 
Use $c=3.00\times10^8\ \mathrm{m/s}$ and $\eta_0=\sqrt{\mu_0/\epsilon_0}\simeq377\ \Omega$ throughout.
:::


### 1. A C-band radar

The Sentinel-1 radar satellites transmit at $f=5.405\ \mathrm{GHz}$. Find the period $T$, the angular frequency $\omega$, the wavelength $\lambda$ and the wavenumber $k$ in vacuum, with units.

:::{admonition} Solution
:class: dropdown

$$
\begin{aligned}
T&=\frac{1}{f}\simeq1.85\times10^{-10}\ \mathrm{s}=0.185\ \mathrm{ns},\\
\omega&=2\pi f\simeq3.40\times10^{10}\ \mathrm{rad/s},\\
\lambda&=\frac{c}{f}\simeq5.55\ \mathrm{cm},\\
k&=\frac{2\pi}{\lambda}=\frac{\omega}{c}\simeq113\ \mathrm{rad/m}.
\end{aligned}
$$

The phase changes by about $113$ radians, or $18$ cycles, per metre along the propagation direction.
:::

### 2. Reading a phasor

Using the $e^{+i\omega t}$ convention, a harmonic field has phasor

$$
E_x(z)=3\,e^{i\pi/2}e^{-ikz}\ \mathrm{V/m}.
$$

(a) Write the physical field $E_x(z,t)$, and evaluate it at $z=0$.

(b) In which direction does the wave travel?

(c) Write the phasor of a wave with the same amplitude and phase at $z=0$, travelling in the opposite direction.

:::{admonition} Solution
:class: dropdown

(a) Multiply by $e^{i\omega t}$ and take the real part:

$$
E_x(z,t)=\operatorname{Re}\left\{3\,e^{i(\omega t-kz+\pi/2)}\right\}
=3\cos(\omega t-kz+\pi/2)=-3\sin(\omega t-kz)\ \mathrm{V/m}.
$$

At $z=0$, $E_x(0,t)=-3\sin\omega t\ \mathrm{V/m}$.

(b) Along $+z$: the phase $\omega t-kz$ stays constant when $z$ increases with $t$.

(c) $E_x(z)=3\,e^{i\pi/2}e^{+ikz}\ \mathrm{V/m}$.
:::

### 3. The magnetic field of a harmonic wave

A plane wave in vacuum has $\vec E=\hat x\,E_x$ with $E_x=E_0\cos(\omega t-kz)$. Its magnetic field is $\vec H=\hat y\,H_y(z,t)$, and the two are linked by

$$
\begin{aligned}
\frac{\partial E_x}{\partial z}&=-\mu_0\frac{\partial H_y}{\partial t},\\
\frac{\partial H_y}{\partial z}&=-\epsilon_0\frac{\partial E_x}{\partial t}.
\end{aligned}
$$

(a) Use the first equation to find $H_y$ in terms of $E_0$ and $\eta_0$. Show that $H_y$ is in phase with $E_x$, and that the ratio of their amplitudes is $\sqrt{\mu_0/\epsilon_0}$. Check that your answer satisfies the right-hand rule. 

(b) Substitute $E_x$ and $H_y$ into the second equation. Show that it is satisfied only if $k=\omega/c$.

:::{admonition} Solution with real fields
:class: dropdown

(a) Differentiate $E_x$ with respect to $z$, substitute it into the first equation, and integrate in time:

$$
\begin{aligned}
\frac{\partial E_x}{\partial z}&=-\mu_0\frac{\partial H_y}{\partial t},\\
\frac{\partial}{\partial z}\bigl[E_0\cos(\omega t-kz)\bigr]&=-\mu_0\frac{\partial H_y}{\partial t},\\
E_0k\sin(\omega t-kz)&=-\mu_0\frac{\partial H_y}{\partial t},\\
\frac{\partial H_y}{\partial t}&=-\frac{E_0k}{\mu_0}\sin(\omega t-kz),\\
H_y&=\frac{E_0k}{\mu_0\omega}\cos(\omega t-kz),\\
H_y&=\frac{E_0}{\eta_0}\cos(\omega t-kz).
\end{aligned}
$$

The last step uses $k=\omega/c$, so that $\mu_0\omega/k=\mu_0c=\eta_0$. We leave aside the constant of integration, which would be a steady field and not part of the wave. $H_y$ has the same argument as $E_x$, so the two are in phase. Where $E_x>0$, $H_y>0$ as well, and $\hat x\times\hat y=\hat z$: $\vec E$, $\vec H$ and the propagation direction form a right-handed set. The amplitude ratio is

$$
\frac{E_0}{H_0}=\frac{\mu_0\omega}{k}=\mu_0c=\frac{\mu_0}{\sqrt{\mu_0\epsilon_0}}=\sqrt{\frac{\mu_0}{\epsilon_0}}=\eta_0\simeq377\ \Omega.
$$

(b) Substitute $E_x$ and the result of (a) into the second equation. Both sides are proportional to $\sin(\omega t-kz)$, so they are equal at every $z$ and $t$ only if their coefficients are equal:

$$
\begin{aligned}
\frac{\partial H_y}{\partial z}&=-\epsilon_0\frac{\partial E_x}{\partial t},\\
\frac{\partial}{\partial z}\left[\frac{E_0k}{\mu_0\omega}\cos(\omega t-kz)\right]&=-\epsilon_0\frac{\partial}{\partial t}\bigl[E_0\cos(\omega t-kz)\bigr],\\
\frac{E_0k^2}{\mu_0\omega}\sin(\omega t-kz)&=\epsilon_0\omega E_0\sin(\omega t-kz),\\
k^2&=\mu_0\epsilon_0\omega^2,\\
k&=\frac{\omega}{c}
\end{aligned}
$$

:::

:::{admonition} Solution with phasors
:class: dropdown

Write each field as a phasor times $e^{i\omega t}$, so that every time derivative becomes a factor $i\omega$. The coupled equations become

$$
\begin{aligned}
(-ik) E_x &= -\mu_0 (i\omega) H_y,\\
(-ik) H_y &= -\epsilon_0 (i\omega) E_x.
\end{aligned}
$$

(a) The wave $E_0\cos(\omega t-kz)$ has phasor $E_x(z)=E_0e^{-ikz}$. The first equation gives

$$
\begin{aligned}
-ikE_x&=-i\omega\mu_0H_y,\\
H_y&=\frac{k}{\omega\mu_0}E_x, \\
H_y&=\frac{E_0 k}{\mu_0 \omega}e^{-ikz}, \\
H_y&=\frac{E_0}{\eta_0}e^{-ikz}.
\end{aligned}
$$

(b) Substituting the result of (a) into the second equation gives

$$
\begin{aligned}
(-ik)H_y &= -\epsilon_0 (i\omega) E_x,\\
k\left(\frac{E_0 k}{\mu_0\omega} e^{-ikz}\right) &= \epsilon_0 \omega E_0 e^{-ikz},\\
k^2 &= \mu_0 \epsilon_0 \omega^2,\\
k &= \frac{\omega}{c}
\end{aligned}
$$

**What became simpler?** Each derivative became a multiplication, by $i\omega$ in time or $\mp ik$ in space. Solving the differential equation no longer requires integrating!
:::

### 4. Measuring ground motion with radar phase

A radar satellite operating at $5.405\ \mathrm{GHz}$ observes a point on the ground at a slant range of $R=850\ \mathrm{km}$. Treat the path as vacuum.

(a) Find the round-trip delay of the echo.

(b) How many wavelengths fit into the round trip? Why is the absolute phase of a single echo not useful on its own for finding $R$?

(c) Between two passes of the satellite, the ground moves $3\ \mathrm{mm}$ away from the radar along the line of sight. Using the round-trip factor $e^{-i2k\Delta R}$, find the change in echo phase.

(d) What line-of-sight displacement changes the phase by exactly $2\pi$? What does this mean when you interpret a measured phase change?

:::{admonition} Solution
:class: dropdown

(a)

$$
\Delta t=\frac{2R}{c}=\frac{2\times850\times10^3\ \mathrm{m}}{3.00\times10^8\ \mathrm{m/s}}\simeq5.67\ \mathrm{ms}.
$$

(b) With $\lambda\simeq5.55\ \mathrm{cm}$, $2R/\lambda\simeq3.1\times10^7$ wavelengths. The phase only tells us where we are within one cycle; it cannot count the whole cycles. A change in $R$ of a few millimetres already changes the phase noticeably. 

(c) A change $\Delta R$ changes the round-trip phase by

$$
\Delta\phi=-2k\,\Delta R=-\frac{4\pi\,\Delta R}{\lambda}
=-\frac{4\pi\times3.0\times10^{-3}\ \mathrm{m}}{5.55\times10^{-2}\ \mathrm{m}}
\simeq-0.68\ \mathrm{rad}\approx-39^\circ.
$$

The sign follows from $e^{-i2k\Delta R}$: moving away makes the phase more negative. 

(d) $|\Delta\phi|=2\pi$ when $\Delta R=\lambda/2\simeq2.8\ \mathrm{cm}$. Displacements that differ by a multiple of $\lambda/2$ give the same measured phase. A phase change of $39^\circ$ could therefore also mean $3.0\ \mathrm{mm}+2.8\ \mathrm{cm}$, and so on. Extra information is needed to choose between them, such as the assumption that the ground moves smoothly in time and space.
:::

### 5. Is it a TEM wave?

For each field below, decide whether it is a valid electric field for a TEM wave in source-free vacuum travelling along $z$. Justify each answer briefly.

(a) $\vec E=\hat x\,E_0\cos(\omega t-kz)$

(b) $\vec E=\hat x\,E_0\exp\left[-\left(\dfrac{t-z/c}{\tau}\right)^2\right]$

(c) $\vec E=\hat x\,E_0\cos(\omega t-2\omega z/c)$

(d) $\vec E=\hat z\,E_0\cos(\omega t-kz)$

For (b), find the times at which the peak of the pulse passes $z=300\ \mathrm{m}$ and $z=600\ \mathrm{m}$.

:::{admonition} Solution
:class: dropdown

(a) **Valid.** This is the standard harmonic plane wave. Substitute $E_x$ into the one-dimensional wave equation and take the second derivatives:

$$
\begin{aligned}
\frac{\partial^2 E_x}{\partial z^2}&=\frac{1}{c^2}\frac{\partial^2 E_x}{\partial t^2},\\
\frac{\partial^2}{\partial z^2}\bigl[E_0\cos(\omega t-kz)\bigr]&=\frac{1}{c^2}\frac{\partial^2}{\partial t^2}\bigl[E_0\cos(\omega t-kz)\bigr],\\
-k^2E_0\cos(\omega t-kz)&=-\frac{\omega^2}{c^2}E_0\cos(\omega t-kz),\\
k^2&=\frac{\omega^2}{c^2}.
\end{aligned}
$$

This holds at every $z$ and $t$ provided $k=\omega/c$, that is, when $k$ is the vacuum wavenumber for the frequency $\omega$. The field points along $x$ and varies only along $z$, so it is transverse and $\vec\nabla\cdot\vec E=\partial E_x/\partial x=0$. Its magnetic field is $\vec H=\hat y\,E_x/\eta_0$, as found in question 3.

```{figure} figures/q5a_harmonic_snapshot.png
:width: 70%

$E_x$ along $z$ at $t=0$ and a quarter period later. In that time the whole pattern moves a quarter wavelength along $+z$.
```

(b) **Valid.** The field depends on $z$ and $t$ only through $t-z/c$, so it solves the wave equation for any pulse width $\tau$, and it is transverse. Its magnetic field is again $\vec H=\hat y\,E_x/\eta_0$. The peak has $t-z/c=0$, so it passes $z=300\ \mathrm{m}$ at $t=1.0\ \mu\mathrm{s}$ and $z=600\ \mathrm{m}$ at $t=2.0\ \mu\mathrm{s}$.

```{figure} figures/q5b_pulse_snapshot.png
:width: 70%

$E_x$ along $z$ at $t=1\ \mu\mathrm{s}$ and $t=2\ \mu\mathrm{s}$, drawn for $\tau=0.1\ \mu\mathrm{s}$. The pulse keeps its shape as it travels $300\ \mathrm{m}$ along $+z$ in $1\ \mu\mathrm{s}$.
```

(c) **Not valid.** Substituting into the wave equation gives $-k^2E_x=-(\omega^2/c^2)E_x$ with $k=2\omega/c$, that is $4\omega^2/c^2=\omega^2/c^2$, which is false. The pattern would travel at $\omega/k=c/2$, which would imply the wave is moving at half the speed of light, which is impossible in a vacuum (possible in a medium with refractive index 2). 

(d) **Not valid.** The field points along the propagation direction, so it is longitudinal, not transverse. Its divergence $\partial E_z/\partial z=E_0k\sin(\omega t-kz)$ is not zero, so it breaks Gauss's law in a region without charges. This type of wave can exist in an environment containing free charges, such as plasma. 
:::
