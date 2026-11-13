# Lab: Plane electromagnetic waves

:::{admonition} Pen-and-paper exercises
:class: note

These exercises accompany {doc}`../plane_waves_1d`, {doc}`../harmonic_waves` and {doc}`../radar_examples`. 
Use $c=3.00\times10^8\ \mathrm{m/s}$ and $\eta_0=\sqrt{\mu_0/\epsilon_0}\simeq377\ \Omega$ throughout.
:::


### 1. A C-band radar

The Sentinel-1 radar satellites transmit at $f=5.405\ \mathrm{GHz}$. Find the period $T$, the angular frequency $\omega$, the wavelength $\lambda$ and the wavenumber $k$ in vacuum, with units.


### 2. Reading a phasor

Using the $e^{+i\omega t}$ convention, a harmonic field has phasor

$$
E_x(z)=3\,e^{i\pi/2}e^{-ikz}\ \mathrm{V/m}.
$$

(a) Write the physical field $E_x(z,t)$, and evaluate it at $z=0$.

(b) In which direction does the wave travel?

(c) Write the phasor of a wave with the same amplitude and phase at $z=0$, travelling in the opposite direction.


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


### 4. Measuring ground motion with radar phase

A radar satellite operating at $5.405\ \mathrm{GHz}$ observes a point on the ground at a slant range of $R=850\ \mathrm{km}$. Treat the path as vacuum.

(a) Find the round-trip delay of the echo.

(b) How many wavelengths fit into the round trip? Why is the absolute phase of a single echo not useful on its own for finding $R$?

(c) Between two passes of the satellite, the ground moves $3\ \mathrm{mm}$ away from the radar along the line of sight. Using the round-trip factor $e^{-i2k\Delta R}$, find the change in echo phase.

(d) What line-of-sight displacement changes the phase by exactly $2\pi$? What does this mean when you interpret a measured phase change?


### 5. Is it a TEM wave?

For each field below, decide whether it is a valid electric field for a TEM wave in source-free vacuum travelling along $z$. Justify each answer briefly.

(a) $\vec E=\hat x\,E_0\cos(\omega t-kz)$

(b) $\vec E=\hat x\,E_0\exp\left[-\left(\dfrac{t-z/c}{\tau}\right)^2\right]$

(c) $\vec E=\hat x\,E_0\cos(\omega t-2\omega z/c)$

(d) $\vec E=\hat z\,E_0\cos(\omega t-kz)$

For (b), find the times at which the peak of the pulse passes $z=300\ \mathrm{m}$ and $z=600\ \mathrm{m}$.