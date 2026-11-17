# How far into the Earth can radar see?

We now have the ingredients to interpret a field travelling inside a material: real permittivity changes its phase behaviour, dielectric response can dissipate energy, and mobile charges can add conduction loss. Let us return to soil and water.

## The same signal, different ground

**Dry sand and soil** can have small losses, allowing useful radar penetration. Add water and the effective permittivity usually increases, changing the speed and radar travel time. Conductive pore water and dielectric loss can also reduce the signal that survives the journey. Salinity and clay content can matter greatly. “Wetter” is useful information, but it is not a complete material model.

**Water is not one universal opaque material.** At suitable GPR frequencies, freshwater can be penetrated well enough to investigate lake-bottom sediments. Saline water supplies much more conduction, while the molecular dielectric response adds frequency-dependent loss in both cases. Many microwave radar measurements of water consequently sample a shallow surface region. Large $\epsilon'$ by itself does not explain this: it is the loss terms that remove energy. [EPA's waterborne GPR examples](https://www.epa.gov/environmental-geophysics/waterborne-ground-penetrating-radar) show the freshwater case in practice.

```{admonition} Predict before changing the frequency
:class: question

1. With the same dielectric response, add conductivity. Which curve in the activity should change most at low frequencies?
2. Can a zero-conductivity relaxing dielectric still attenuate strongly at higher frequencies?
3. Compare the exact attenuation depth with the good-conductor approximation. Where is the approximation justified?
4. Change the assumed reflector depth. Why does an apparently modest one-way loss become much more serious for an echo?
```

```{raw} html
:file: interactives/media_penetration_embed.html
```

The presets are **illustrative material examples**, not site measurements. The soil examples use a constant real permittivity and dielectric loss ratio over the displayed band. The water-like examples use a single relaxation and fixed conductivity. Their parameters are shown in the activity. They reproduce useful mechanisms and comparisons; a quantitative survey needs a suitable measured or calibrated material model, including temperature and salinity where relevant.

For actual microwave water properties, [Meissner and Wentz (2004)](https://images.remss.com/papers/rsspubs/Meissner_TGRS_2004_dielectric.pdf) develop a temperature- and salinity-dependent model using two dielectric relaxations. We deliberately use a simpler model here so that the equations remain visible.

## The echo has to make it back

For a homogeneous path to a reflector at depth $d$, a wave experiences the absorption factor $e^{-\alpha d}$ on the way down and again on the way back. Relative to an otherwise identical lossless path,

$$
\boxed{\frac{|E_{\mathrm{echo}}|}{|E_{\mathrm{echo,no\ loss}}|}
=e^{-2\alpha d},\qquad
\frac{P_{\mathrm{echo}}}{P_{\mathrm{echo,no\ loss}}}=e^{-4\alpha d}.}
$$ (eq:em-media-round-trip)

At one field attenuation depth, $d=1/\alpha$, the returning field has the absorption factor $e^{-2}\approx0.14$ and its power the factor $e^{-4}\approx0.018$. The wave did not stop at that depth. It simply has much less energy left for the receiver.

The reference comparison holds transmission, reflection and geometry fixed to isolate absorption. A real radar also has surface reflection, target contrast, spreading, scattering and receiver noise to contend with. **Attenuation depth is a material scale, not a promise about how deep a radar will see.**

```{figure} figures/media_round_trip.svg
:name: fig:em-media-round-trip
:width: 100%

Absorption on a homogeneous down-and-back path. The field has accumulated $e^{-\alpha d}$ at the reflector and $e^{-2\alpha d}$ after return. Squaring gives the corresponding power factors. Surface transmission, reflector strength and geometric spreading are held outside this comparison.
```

```{admonition} Read a material from two field measurements
:class: question

At one frequency, the complex fields at two depths separated by $L$ have ratio

$$
\frac{E_x(z+L)}{E_x(z)}=a\,e^{-j\phi},\qquad 0<a<1.
$$

Assume a single forward wave and that $\phi$ is its correctly unwrapped positive phase lag.

1. Find $\alpha$ and $\beta$ from $a,\phi,L$.
2. Form $k=\beta-j\alpha$ and recover $\epsilon_{\mathrm{eff}}$ if $\mu$ is known.
3. Can this one-frequency result distinguish dielectric loss from conductivity without further information?

This is a small inverse problem: the equations turn measured amplitude and phase into a statement about the material.
```

```{admonition} Check the inverse calculation
:class: dropdown

The amplitude ratio gives $a=e^{-\alpha L}$, while the phase lag is $\phi=\beta L$. Hence

$$
\alpha=-\frac{\ln a}{L},\qquad
\beta=\frac{\phi}{L},\qquad
\epsilon_{\mathrm{eff}}=\frac{(\beta-j\alpha)^2}{\omega^2\mu}.
$$

The imaginary part provides the combined loss $\epsilon''_d+\sigma/\omega$, not its two contributions separately. A raw measured phase is known only modulo $2\pi$; unwrapping or additional information is needed to infer $\beta$ uniquely.
```

## An optional look upwards: the ionosphere

The medium need not be below our feet. Satellite signals also pass through a plasma containing free electrons. For a simple collisionless, unmagnetized plasma, suppose its relative permittivity is

$$
\epsilon_r(\omega)=1-\frac{\omega_p^2}{\omega^2},\qquad
k^2=\frac{\omega^2-\omega_p^2}{c^2},
$$

where $\omega_p$ is the plasma frequency, set by electron density. We supply this model rather than derive it here; see [Staelin, section 9.5.3](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/MIT6_013S09_chap09.pdf).

```{admonition} Does decay always mean absorption?
:class: dropdown

Above $\omega_p$, $k^2>0$ permits an oscillating propagating wave. Below $\omega_p$, write

$$
k=-j\kappa,\qquad \kappa=\frac{\sqrt{\omega_p^2-\omega^2}}{c}>0.
$$

In a semi-infinite plasma, the bounded solution is $E_x=E_0e^{-\kappa z}$. It decays, yet this ideal model has no collisional heating. Recover

$$
H_y=-j\frac{\kappa}{\omega\mu_0}E_x.
$$

The fields are in quadrature, and $\operatorname{Re}\{E_xH_y^*\}=0$: this single evanescent solution carries no average power into the plasma. Check the ODE and this flux yourself. We exclude the exact cutoff from these two cases.

Decay alone does not establish absorption. In our ordinary lossy travelling waves, the decreasing nonzero energy flux identified the deposited power. Here the sign of $k^2$ and the field relation describe a different behaviour.
```

Relating this model to GNSS timing would also require discussing pulse or group delay along the signal path. Faraday rotation requires Earth's magnetic field, which this scalar model omits. We leave those applications for later.

## Ready to put materials next to each other

We have treated the field just inside a homogeneous material as given. Two quantities are now ready for the next step:

$$
\eta=\frac{\omega\mu}{k},\qquad e^{-jk(\omega)d}.
$$

The impedance enters field matching at an interface. The exponential describes one-way propagation through a layer of thickness $d$. Combining them will let us ask which echoes return, how layers interfere, and what their frequency response tells us about the ground.
