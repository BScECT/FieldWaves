# Polarization and antenna response

After calculating {doc}`03_02_energy_flow`, we turn to the orientation of the electric field and how a receiving antenna responds to it.

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

The field relations, polarization and energy calculations follow David H. Staelin’s [*Electromagnetics and Applications*, Chapter 2](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/MIT6_013S09_chap02.pdf), especially §§2.3.4 and 2.7.

The NASA, ESA and JPL pages linked above provide application context.
