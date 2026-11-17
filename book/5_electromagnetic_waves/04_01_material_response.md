# What the medium does to the fields

A radar pulse enters dry sand, wetter soil or water. Its frequency was set by the transmitter, but its wavelength, travel time and amplitude need not remain the same. Before calculating those changes, we need to give the material a role in the equations.

## Charges can move without going very far

An electric field can displace bound positive and negative charge slightly relative to each other. Molecules with permanent electric dipoles, including water molecules, can also reorient. The material develops an electric dipole moment per unit volume, called its **polarization** $\vec P$.

We collect this response in the electric displacement field,

$$
\vec D=\epsilon_0\vec E+\vec P.
$$

For a simple linear, isotropic material whose response follows the field instantaneously,

$$
\vec P=\epsilon_0\chi_e\vec E,
\qquad
\boxed{\vec D=\epsilon\vec E,\qquad
\epsilon=\epsilon_0(1+\chi_e).}
$$ (eq:em-media-permittivity)

Here $\chi_e$ is the dimensionless electric susceptibility. Permittivity $\epsilon$ has units F/m; $\vec D$ and $\vec P$ have units C/m$^2$. The relative permittivity is defined as $\epsilon_r=\epsilon/\epsilon_0$.

```{admonition} Two uses of polarization
:class: note

**Material polarization** $\vec P$ describes the response of matter. **Wave polarization** describes the motion of the real electric-field tip, as in the previous section. The same word, two related but different jobs.
```

```{figure} figures/media_material_response.svg
:name: fig:em-media-response
:width: 100%

Three material responses to an electric field: bound-charge displacement, molecular dipole reorientation, and mobile-ion conduction. The first two contribute to dielectric response. Mobile charge adds conduction. A soil contains grains, pore air and pore water, so its bulk response depends on their mixture.
```

Permittivity is not just a new symbol to carry around. Recall the ideal parallel-plate capacitor:

$$
C=\frac{\epsilon A}{d},\qquad Q=CV.
$$

At the same voltage and geometry, a larger permittivity means more charge on the plates. The material responds, and that changes the relation between the free plate charge and the field.

For soil and rock, pore air, mineral grains and water all contribute to the effective response. Increasing water content often increases the bulk permittivity substantially. Porosity and mineral composition matter too, so a permittivity measurement gives us useful information about moisture, but not an unambiguous measurement of moisture all by itself. See [EM GeoSci's discussion of porosity and saturation](https://em.geosci.xyz/content/physical_properties/dielectric_permittivity/dielectric_permittivity_factors.html).

## And the magnetic response?

Magnetic moments in matter give a magnetization $\vec M$. We write

$$
\vec B=\mu_0(\vec H+\vec M),\qquad
\boxed{\vec B=\mu\vec H}
$$

for a linear isotropic magnetic response. Permeability $\mu$ has units H/m. We retain it in the equations, but use $\mu\approx\mu_0$ for the ordinary weakly magnetic materials in our radar examples. This approximation is useful, not universal: magnetic minerals can change the response.

For now, $\epsilon$ and $\mu$ are real, positive and approximately constant over the signal's frequency band. We also set the conductivity to zero. Let us see what changes even in this lossless case.

## A different medium, a different wavelength

Inside a homogeneous, charge-free material, the familiar phasor equations become

$$
\nabla\times\vec E=-j\omega\mu\vec H,
\qquad
\nabla\times\vec H=j\omega\epsilon\vec E,
\qquad
\nabla\cdot\vec E=0.
$$

The last relation follows from $\nabla\cdot\vec D=0$ and constant, nonzero $\epsilon$. Repeat the curl-curl calculation from the vacuum case, using
$\nabla\times(\nabla\times\vec E)=\nabla(\nabla\cdot\vec E)-\nabla^2\vec E$. It gives

$$
\nabla^2\vec E+k^2\vec E=0,
\qquad
\boxed{k^2=\omega^2\mu\epsilon.}
$$

For the forward travelling wave, choose the positive real $k$. Its phase is $\omega t-kz$. Following a crest therefore gives

$$
\boxed{v_p=\frac{\omega}{k}=\frac1{\sqrt{\mu\epsilon}},\qquad
\lambda=\frac{2\pi}{k}.}
$$ (eq:em-media-lossless-speed)

The transmitter fixes temporal frequency. The material changes the **wavenumber**, its angular spatial frequency: more cycles can fit into each metre, even though the number of cycles per second has not changed. For $\mu\approx\mu_0$,

$$
v_p\approx\frac{c}{\sqrt{\epsilon_r}}.
$$

The fields also have a different ratio. For $\vec E=\hat xE_0e^{-jkz}$, Faraday's law gives

$$
\vec H=\hat y\frac{k}{\omega\mu}E_0e^{-jkz},
\qquad
\boxed{\eta=\frac{E_x}{H_y}=\sqrt{\frac{\mu}{\epsilon}}.}
$$

This impedance will become useful when we put two materials next to each other.

```{admonition} Change the material, read the equations
:class: question

Keep $\mu$ and the transmitter frequency fixed, and multiply $\epsilon$ by four.

1. What happens to phase speed, wavelength and impedance?
2. Does the proposed field acquire any decay with $z$?
3. A pulse travels to a reflector and back in a nearly nondispersive material. If you use the vacuum speed to convert its travel time into depth, is the inferred depth too large or too small?

Use the equations to explain your answers. A larger permittivity alone does **not** mean stronger absorption.
```

For a homogeneous, nearly nondispersive material the round-trip time is approximately $T=2d/v_p$. This gives a first reason to care about the medium: a different propagation speed changes what a radar travel time means. Next, we let the material do more than slow the wave down.
