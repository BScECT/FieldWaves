# Electromagnetic energy and the Poynting vector

Following the wave geometry in {doc}`03_01_waves_3d`, we now calculate energy density, energy flow and the effect of spreading.

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
\vec E(\vec r)=\hat yE_0e^{-j\vec k\cdot\vec r},\qquad k=\omega/c,
$$

with vector wavenumber

$$
\vec k=\frac{k}{\sqrt2}\hat x+\frac{k}{\sqrt2}\hat z,
\qquad \vec k\cdot\vec r=\frac{k(x+z)}{\sqrt2},
$$

Here $k=|\vec k|$ is the wavenumber (angular spatial frequency), $E_0$ is real, and the propagation direction is $\hat n=(\hat x+\hat z)/\sqrt2$.

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
\vec H=\frac{E_0}{\eta_0\sqrt2}(-\hat x+\hat z)e^{-j\vec k\cdot\vec r},
\qquad
\vec H^*=\frac{E_0}{\eta_0\sqrt2}(-\hat x+\hat z)e^{+j\vec k\cdot\vec r}.
$$

The opposite phase factors cancel, giving

$$
\vec E\times\vec H^*=\frac{E_0^2}{\eta_0\sqrt2}(\hat x+\hat z),
\qquad
\langle\vec S\rangle=\frac{E_0^2}{2\eta_0}\hat n,
\qquad
\langle u\rangle=\frac{\epsilon_0E_0^2}{2}.
$$

A common phase shift also cancels as $e^{j\phi}e^{-j\phi}=1$: it changes the timing of the oscillation, not its average energy transport. Without the conjugate we would retain $e^{-2j\vec k\cdot\vec r}$ and obtain a position-dependent result, even though this travelling plane wave has uniform average energy flux.
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

The amount of energy reaching a receiver is only part of the measurement: {doc}`03_03_polarization` examines how field orientation affects its response.

## Reading and sources

The field relations, polarization and energy calculations follow David H. Staelin’s [*Electromagnetics and Applications*, Chapter 2](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/MIT6_013S09_chap02.pdf), especially §§2.3.4 and 2.7.
