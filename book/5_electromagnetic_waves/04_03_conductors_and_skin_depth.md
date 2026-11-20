# Conductors, diffusion and skin depth

Bound-charge response is not the only way to remove energy from a wave. Mobile charge can travel through the material. Dissolved ions make this particularly relevant to pore water and seawater.

## Add a conduction current

Use the local form of Ohm's law,

$$
\vec J_c=\sigma\vec E,
$$

where conductivity $\sigma$ is in S/m. In this simple model it is real and nonnegative. Ampère–Maxwell becomes

$$
\nabla\times\vec H=\sigma\vec E+j\omega\epsilon_d\vec E
=j\omega\epsilon_{\mathrm{eff}}\vec E,
$$

$$
\boxed{\epsilon_{\mathrm{eff}}
=\epsilon_d-j\frac{\sigma}{\omega}
=\epsilon'-j\left(\epsilon''_d+\frac{\sigma}{\omega}\right).}
$$ (eq:em-media-effective-epsilon)

The physical mechanisms differ, but the harmonic calculation can collect them in one complex permittivity. Check the units of $\sigma/\omega$: they are F/m, just as required. When you use measured complex permittivity, check what it includes; adding conductivity again would count the same loss twice.

We do not need a second wave solution. Replace $\epsilon_d$ by $\epsilon_{\mathrm{eff}}$ in the previous equations:

$$
k^2=\omega^2\mu\epsilon_{\mathrm{eff}},\qquad
2\alpha\beta=\omega\mu(\omega\epsilon''_d+\sigma).
$$

The mean deposited power per unit volume is now

$$
\boxed{-\nabla\cdot\langle\vec S\rangle
=\underbrace{\frac{\omega\epsilon''_d}{2}|\vec E|^2}_{\text{dielectric heating}}
+\underbrace{\frac{\sigma}{2}|\vec E|^2}_{\text{Joule heating}}.}
$$ (eq:em-media-heating)

The factor $1/2$ uses our peak-amplitude phasors. It is the average of the squared real oscillation.

```{admonition} Add salt, then explain the equation
:class: question

Adding dissolved salt supplies mobile ions. Which term would you particularly expect to increase? Explain why this can reduce penetration even if the real permittivity changes relatively little. Then return to the wave activity and turn conduction on, initially keeping the dielectric parameters fixed.
```

## Is this a good conductor at this frequency?

Compare the sizes of the two terms in Ampère–Maxwell. Conduction dominates when

$$
\boxed{\sigma\gg\omega|\epsilon_d|.}
$$

For a dielectric background with small loss, the useful ratio is $\sigma/(\omega\epsilon')$. A material can be conduction-dominated at one frequency and not at another. “Good conductor” is a statement about a regime, not just a name on a material sample.

In this limit,

$$
k^2\approx-j\omega\mu\sigma.
$$

Since $(1-j)^2=-2j$, the root appropriate to a wave that decays into $z>0$ is

$$
\boxed{k\approx(1-j)\sqrt{\frac{\omega\mu\sigma}{2}},
\qquad \alpha\approx\beta\approx\sqrt{\frac{\omega\mu\sigma}{2}}.}
$$

Consequently, the **skin depth** is

$$
\boxed{\delta_E\approx\sqrt{\frac{2}{\omega\mu\sigma}}.}
$$ (eq:em-media-skin-depth)

The field falls to $1/e$ over one skin depth. This is a finite-conductivity result: there is a field and an induced current inside the material, and both decrease with depth.

```{admonition} Check the root and the scale
:class: question

1. Square the proposed $k$ and check the sign of its imaginary part.
2. Check the units of $\sqrt{2/(\omega\mu\sigma)}$.
3. With $\mu,\sigma$ fixed, what happens to skin depth if frequency is multiplied by four? What if conductivity is multiplied by four?
4. Is the field already zero at one skin depth? How much of its average power flux remains?
```

## We have seen the conductive limit before

For a moment, use a real, instantaneous, constant dielectric permittivity and ohmic conductivity. In the time domain,

$$
\nabla\times\vec E=-\mu\frac{\partial\vec H}{\partial t},\qquad
\nabla\times\vec H=\sigma\vec E+
\epsilon\frac{\partial\vec E}{\partial t}.
$$

Taking a curl of Faraday's law in the homogeneous charge-free bulk gives

$$
\boxed{\nabla^2\vec E
=\mu\epsilon\frac{\partial^2\vec E}{\partial t^2}
+\mu\sigma\frac{\partial\vec E}{\partial t}.}
$$ (eq:em-media-wave-diffusion)

The second time derivative is familiar from wave propagation; the first time derivative supplies damping. In the conduction-dominated regime we neglect the displacement term, leaving

$$
\boxed{\frac{\partial\vec E}{\partial t}
=\frac1{\mu\sigma}\nabla^2\vec E.}
$$

That is the {doc}`EM diffusion equation <../3_diffusion_fields/em_diffusion>`. Its diffusivity is $1/(\mu\sigma)$ in m$^2$/s. A more conductive material has a smaller diffusivity: changes spread into it more slowly. The wave and diffusion chapters are meeting again.

```{admonition} Let the terms tell you the regime
:class: question

For a harmonic field, compare the magnitudes of the two right-hand terms in the damped wave equation. Show that their ratio, conduction to displacement, is $\sigma/(\omega\epsilon)$.

Which limiting equation follows when this ratio is very small? Which follows when it is very large? Use the harmonic time factor to check that the diffusion equation gives $k^2=-j\omega\mu\sigma$.
```

```{admonition} Why use a real permittivity in that time-domain step?
:class: dropdown

A frequency-dependent $\epsilon_d(\omega)$ describes material memory. It cannot simply replace the constant $\epsilon$ in a time-domain equation. One way to retain that memory is to keep the polarization as a separate unknown. With $\vec D=\epsilon_0\vec E+\vec P$ and the same transverse, homogeneous bulk assumptions, the field equation is

$$
\nabla^2\vec E
=\mu\epsilon_0\frac{\partial^2\vec E}{\partial t^2}
+\mu\frac{\partial^2\vec P}{\partial t^2}
+\mu\sigma\frac{\partial\vec E}{\partial t},
$$

together with a response equation for $\vec P$, such as the relaxation model on the previous page. For harmonic fields, complex permittivity handles that additional response neatly. Our simple real-$\epsilon$ calculation isolates the wave-to-diffusion connection.
```

## Does a longer wavelength always penetrate further?

Within the good-conductor approximation and for fixed $\mu,\sigma$,

$$
\delta_E\propto f^{-1/2}\propto\sqrt{\lambda_0},
\qquad \lambda_0=\frac{c}{f}.
$$

This is a useful scaling, but it comes with assumptions. In the opposite limit of weak conduction and negligible dielectric loss, the relations for $\alpha,\beta$ give

$$
\beta\approx\omega\sqrt{\mu\epsilon'},\qquad
\alpha\approx\frac{\sigma}{2}\sqrt{\frac{\mu}{\epsilon'}}.
$$

For fixed material parameters, that attenuation is approximately independent of frequency. A relaxing dielectric has its own frequency-dependent losses. We therefore calculate $k(\omega)$ from the full material response when the conductor approximation does not apply. Let us use that idea on the materials we actually care about.
