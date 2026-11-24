# Normal incidence: the familiar problem with electromagnetic fields

A flat interface separates medium 1, at $z<0$, from medium 2, at $z>0$. A plane wave arrives along $+z$, perpendicular to the interface. This is **normal incidence**.

```{admonition} Coordinate convention: positive z now points down
:class: note

For the horizontal ground interface, we now choose **positive $z$ downwards**, into medium 2, with $z=0$ at the surface. This reverses the upward-positive vertical coordinate used earlier in the book. The Cartesian axes still form a right-handed set.

This choice makes increasing $z$ increasing depth. With our unchanged time convention $e^{j\omega t}$, a downward-travelling wave has $k_z>0$ and retains the familiar spatial factor $e^{-jk_z z}$. Its phase is $\omega t-k_z z$: following a constant phase gives $dz/dt=\omega/k_z>0$, which now means motion downwards. An upward-travelling reflected wave has $k_z<0$, giving $e^{+j|k_z|z}$. The coordinate direction has changed; the propagation rule and the physics have not.
```

Begin with the lossless media from {doc}`04_01_material_response`:

$$
k_m=\omega\sqrt{\mu_m\epsilon_m},\qquad
\eta_m=\sqrt{\frac{\mu_m}{\epsilon_m}},\qquad m=1,2.
$$

The wavenumber $k_m$ tells us how phase changes per metre; impedance $\eta_m$ relates the electric and magnetic fields. They describe different aspects of the wave.

```{figure} figures/interface_normal_incidence.svg
:name: fig:em-interface-normal-geometry
:width: 100%
:alt: Two-dimensional normal-incidence geometry. The interface at z equals zero separates two media. Electric reference arrows lie along x in the page. Magnetic fields are shown by dots for out of the page and a cross for into the page. Incident and transmitted waves travel along positive z, while the reflected wave travels along negative z.

Normal incidence at $z=0$, viewed in the $xz$ plane. The electric fields lie in the page; dots and crosses indicate magnetic fields out of and into the page. The arrows specify reference orientations for the three waves, with $\vec E\times\vec H$ along their propagation directions. Their complex amplitudes carry any phase reversal. The waves are drawn separately so their directions can be read clearly.
```

## The wave equation allows both directions

For an electric field along $x$ with spatial variation only in $z$, the Helmholtz (wave) equation reduces to

$$
\frac{d^2E_x}{dz^2}+k_m^2E_x=0.
$$

As in {doc}`02_02_harmonic_waves`, both $e^{-jk_mz}$ and $e^{+jk_mz}$ solve this equation. In the first medium we can write

$$
E_{1x}=A e^{-jk_1z}+B e^{+jk_1z},\qquad
$$

where we anticipate a reflected wave. This follows from our physical intuition. Since the wave equation is linear and homogeneous (the zero term in the right hand) within the region of interest, the sum of two possible solutions is also a solution.

In the second medium we will only have a forward propagating term, even if the math would support the second term,
$$
E_{2x}=C e^{-jk_2z}.
$$ (eq:em-interface-normal-fields)

Here $A$ is the prescribed incident amplitude, while $B$ and $C$ are still unknown. 

Retrieve $\vec H$ from Faraday's law, rather than assigning its sign by eye. The Cartesian curl is

$$
\nabla\times\vec E=
\begin{pmatrix}
\partial E_z/\partial y-\partial E_y/\partial z\\
\partial E_x/\partial z-\partial E_z/\partial x\\
\partial E_y/\partial x-\partial E_x/\partial y
\end{pmatrix}
=\hat y\frac{dE_x}{dz}=-j\omega\mu\vec H.
$$

Consequently,

$$
H_{1y}=\frac{A e^{-jk_1z}-B e^{+jk_1z}}{\eta_1},\qquad
H_{2y}=\frac{C e^{-jk_2z}}{\eta_2}.
$$ (eq:em-interface-normal-h)

The minus sign in the reflected magnetic field follows from differentiating the opposite spatial phase. It also makes $\vec E_r\times\vec H_r^*$ point back towards $-z$.

```{admonition} Check the proposed fields
:class: question

Substitute each electric-field term into its Helmholtz equation. Then use its derivative to recover the corresponding magnetic field. If you change the propagation direction, which sign in the companion field must change? Compare with pressure and particle velocity in the acoustic reflection calculation.
```

## What must match at the boundary?

We need conditions at $z=0$. These come from Maxwell's equations, using the integral form introduced in {doc}`01_history_maxwell`.

### Tangential electric field

Take a small rectangular loop straddling the interface, with two long sides of length $\ell$ parallel to $x$ and a small height $h$ along $z$. Faraday's law gives

$$
\oint\vec E\cdot d\vec\ell
=-j\omega\int\vec B\cdot\hat n_S\,dS.
$$

```{figure} figures/interface_tangential_e_loop.svg
:name: fig:em-interface-faraday-loop
:width: 100%
:alt: Two flat views of a narrow rectangular loop across an interface. Electric fields point tangentially on both sides. The loop's tangential length ell stays fixed while its normal width h shrinks, making the shaded area tend to zero. Dots show a magnetic field that remains finite through the page.

Shrink the normal width $h$ while keeping the tangential length $\ell$ fixed. The shaded area is $\ell h$, so $|\Phi_B|\leq B_{\max}\ell h\to0$ for a bounded magnetic field; $B_{\max}$ bounds its magnitude near the interface. The field itself need not vanish. Dots indicate magnetic field out of the page, and the loop arrows mark its clockwise traversal. $E_{1x}$ and $E_{2x}$ are the total tangential fields.
```

As $h$ tends to zero, the magnetic-flux term tends to zero for finite fields. The two short-side contributions also vanish. The two long sides remain, with opposite traversal directions. Thus

$$
E_{1x}(0)\ell-E_{2x}(0)\ell=0,
\qquad \boxed{E_{1x}(0)=E_{2x}(0).}
$$ (eq:em-interface-e-continuity)

This is continuity of the **tangential** electric field. It is the total field on each side that must match.

### Tangential magnetic field, with a possible sheet current

Now use an Ampère–Maxwell loop with its long sides parallel to $y$:

$$
\oint\vec H\cdot d\vec\ell
=\int\vec J_f\cdot\hat n_S\,dS
+j\omega\int\vec D\cdot\hat n_S\,dS.
$$

The displacement-flux term again vanishes with the loop area. A finite volume-current density also gives a vanishing contribution. A **surface current** can remain: a sheet carrying $\vec K$ has current per unit width, in A/m, so the loop can enclose $K_x\ell$ even as its height shrinks.

Choose the loop orientation with surface normal $+\hat x$. It gives

$$
H_{1y}(0)-H_{2y}(0)=K_x.
$$

In vector form, with $\hat n=\hat z$ pointing from medium 1 to medium 2,

$$
\boxed{\hat n\times(\vec H_2-\vec H_1)=\vec K.}
$$ (eq:em-interface-h-jump)

```{admonition} The Dirac delta comes back, now in space
:class: note

You met the Dirac delta as an ideal impulse in **Signals and Time Series**. We also used it for a spatial current sheet in {doc}`EM diffusion <../3_diffusion_fields/em_diffusion>`. Here the same mathematical construct gives a compact description of current concentrated at an interface.

In the perfect-conductor limit, the induced harmonic current is confined to the surface. Think of the current-carrying layer becoming thinner while its integrated current stays finite. At our plane $z=0$, write the **volume current density** as

$$
\boxed{\vec J_f(z)=\vec K\,\delta(z).}
$$

The delta acts on position rather than time. Its key property here is

$$
\int_{-h/2}^{h/2}\delta(z)\,dz=1
\qquad\text{for every }h>0.
$$

For the Ampère–Maxwell loop above, with surface normal $+\hat x$ and length $\ell$ along $y$, the enclosed current is therefore

$$
\int_S\vec J_f\cdot\hat n_S\,dS
=\int_0^\ell dy\int_{-h/2}^{h/2}K_x\delta(z)\,dz
=K_x\ell.
$$

It survives as $h\to0$, even though the loop area vanishes. This is why a sheet current can support a jump in tangential $\vec H$: its volume-density description is concentrated on the surface, rather than bounded throughout the shrinking area.

Check the units: $\vec K$ is in A/m and $\delta(z)$ has units $1/\mathrm m$, giving $\vec J_f$ in A/m$^2$. For a real conductor with finite {doc}`skin depth <04_03_conductors_and_skin_depth>`, the current is spread through a thin volume instead. The delta represents the ideal surface limit.
```

At an ordinary interface between our two lossless dielectrics there is no free current sheet, so $\vec K=0$ and tangential $\vec H$ is continuous. We will use the nonzero-current version in {doc}`05_02_conducting_reflection`.

```{admonition} Figure to develop — the magnetic-field loop
:class: note

Show the Ampère–Maxwell loop in the $yz$ plane. Mark traversal arrows, surface normal, $\ell$, $h$, and a possible $x$-directed sheet current. Use the Faraday-loop figure above as a visual counterpart, keeping the geometry consistent with the signs in the equations.
```

```{admonition} What about the divergence equations?
:class: dropdown

Small pillboxes, using Gauss's theorem, give

$$
\hat n\cdot(\vec B_2-\vec B_1)=0,\qquad
\hat n\cdot(\vec D_2-\vec D_1)=\sigma_f,
$$

where $\sigma_f$ is free surface charge density. These statements concern **normal** components. Our normal-incidence waves have electric and magnetic fields parallel to the interface, so their normal components vanish. We do not obtain two extra independent amplitude equations here. Later, at oblique incidence, checking these relations is useful.
```

## Reuse the acoustic calculation

Define electric-field amplitude coefficients $r=B/A$ and $t=C/A$. The two continuity conditions become

$$
1+r=t,\qquad \frac{1-r}{\eta_1}=\frac{t}{\eta_2}.
$$

We have already solved this system in {doc}`acoustic reflection and transmission <../4_mechanical_waves/reflection_transmission>`. Pressure and particle velocity have been replaced by tangential electric and magnetic fields; acoustic impedance $\rho c$ has been replaced by electromagnetic impedance $\eta$. The physical quantities and units differ, but the algebra is the same:

$$
\boxed{r=\frac{\eta_2-\eta_1}{\eta_2+\eta_1},\qquad
 t=\frac{2\eta_2}{\eta_2+\eta_1}.}
$$ (eq:em-interface-normal-coefficients)

If $\eta_1=\eta_2$, there is no reflected wave. If $r<0$, the reflected electric field has a phase shift of $\pi$ relative to the incident field at the interface. A negative coefficient does not mean negative energy.

```{admonition} Could we do without a reflected wave?
:class: question

Set $r=0$ in both matching equations. What condition must the impedances satisfy? Explain why solving the wave equation separately in both media is not enough to determine the physical solution.
```

```{admonition} A derivative can jump
:class: dropdown

Since $H_y=j(dE_x/dz)/(\omega\mu)$, the no-sheet-current boundary condition also says that $(1/\mu)dE_x/dz$ is continuous. The derivative itself is continuous only when the permeabilities are equal. This is familiar from earlier problems with differential equations in different materials: check the physical flux or field condition before assuming that derivatives match.
```

## Reflected field and reflected power

Return to {doc}`03_02_energy_flow`. With our peak-amplitude phasors,

$$
\langle\vec S\rangle=\frac12\operatorname{Re}\{\vec E\times\vec H^*\}.
$$

The incoming, reflected and transmitted fluxes are

$$
\langle S_{i,z}\rangle=\frac{|A|^2}{2\eta_1},\quad
\langle S_{r,z}\rangle=-\frac{|B|^2}{2\eta_1},\quad
\langle S_{t,z}\rangle=\frac{|C|^2}{2\eta_2}.
$$

Define positive reflected and transmitted **power fractions**:

$$
\boxed{\mathcal R=|r|^2,\qquad
\mathcal T=\frac{\eta_1}{\eta_2}|t|^2.}
$$ (eq:em-interface-normal-power)

For this lossless interface, substitution gives $\mathcal R+\mathcal T=1$. The impedance factor matters: squaring $t$ alone does not compare the power in different media.

As a simple air–ground model, take $\mu_1=\mu_2=\mu_0$, $\epsilon_1=\epsilon_0$ and $\epsilon_2=4\epsilon_0$. These are illustrative values. Then $\eta_2=\eta_1/2$, giving

$$
r=-\frac13,\qquad t=\frac23,\qquad
\mathcal R=\frac19,\qquad \mathcal T=\frac89.
$$

Increasing soil permittivity changes both propagation inside the ground and reflection at its surface. That is why the material response discussed in {doc}`04_01_material_response` matters to an echo before we even consider attenuation below the surface.

```{admonition} Predict the change
:class: question

1. Replace $\epsilon_2=4\epsilon_0$ by $9\epsilon_0$, keeping $\mu_2=\mu_0$. Predict whether reflection increases before calculating it.
2. Check $\mathcal R+\mathcal T=1$ in both cases.
3. Could $t$ exceed one for another impedance contrast? Would that necessarily violate energy conservation?
```

### Match the fields by changing soil moisture

Suppose a radar visits the same patch of ground before and after rain. The boundary has not moved, but water has replaced some pore air. The soil's permittivity changes, so its impedance and the reflected amplitude change too. This gives an echo a way to vary over time without anything moving.

The activity below connects the material mixture from {doc}`04_01_material_response` to the matching equations. Change the **volumetric water content**, meaning water volume divided by total soil volume. Keep an eye on both electric and magnetic fields: each must match across the interface, even as their amplitudes and wavelengths change.

```{admonition} Predict, then wet the soil
:class: question

1. Increase water content. What should happen to $\epsilon_r$, $\eta_2$, $k_2$ and the wavelength in the soil? Use their equations to explain the connections.
2. Compare the reflected power before and after rain. Has the interface moved? Does energy conservation still hold?
3. Turn on the incident and reflected components. Why does the reflected contribution have opposite signs in the electric and magnetic plots?
4. Change oscillation phase. Which quantities oscillate, and which power fractions stay constant? Then change the visit day: what is changing on this much slower time scale?
```

```{raw} html
:file: interactives/interface_fields_embed.html
```

```{admonition} How does water content become permittivity?
:class: dropdown

We supply a simple three-component mixing model. Let porosity $\phi$ be the fraction of the soil occupied by pores, and let $\theta_v$ be volumetric water content. The volume fractions of mineral, water and air are $1-\phi$, $\theta_v$ and $\phi-\theta_v$, respectively. Thus $0\leq\theta_v\leq\phi$. Equivalently, $\theta_v=\phi S_w$ if $S_w$ is the fraction of pore volume filled with water.

The model averages the square roots of the relative permittivities:

$$
\sqrt{\epsilon_{r,\mathrm{soil}}}
=(1-\phi)\sqrt{\epsilon_{r,\mathrm{mineral}}}
+\theta_v\sqrt{\epsilon_{r,\mathrm{water}}}
+(\phi-\theta_v)\sqrt{\epsilon_{r,\mathrm{air}}}.
$$

The activity uses $\phi=0.45$, mineral relative permittivity 5, water 80 and air 1. These are illustrative choices. See [EM GeoSci's porosity and saturation model](https://em.geosci.xyz/content/physical_properties/dielectric_permittivity/dielectric_permittivity_factors.html) for this mixing relation. Here we keep the medium lossless and nonmagnetic at a fixed frequency of 300 MHz, so the activity isolates reflection and wavelength changes. The dry/wet presets in the earlier penetration activity are separate illustrative material examples.

The day sequence is also supplied: wetting is followed by exponential drying. Each visit represents a separate steady harmonic solution. The wave animation shows the carrier cycle within one such solution; it does not simulate the transient response to rain.
```

This plane-interface reflection is a useful ingredient in interpreting temporal changes in radar echoes. Off-nadir radar backscatter also depends on roughness, vegetation and viewing geometry, as we discuss in {doc}`05_04_polarization_at_interface`. Here those changes stay outside the model so we can follow the material effect clearly.

For an absorbing second medium the same amplitude matching uses complex $k_2$ and $\eta_2$, with the decaying transmitted solution chosen as in {doc}`04_02_lossy_dielectrics`. The power entering it is computed from the Poynting vector; the real-impedance expression for $\mathcal T$ must be replaced by $\eta_1\operatorname{Re}(1/\eta_2)|t|^2$. That entering power can then be absorbed with depth. Reflection and absorption are different parts of the story.

## Reading and sources

For the normal-incidence interface calculation, see [Ellingson, *Electromagnetics II*, §5.1](https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electromagnetics_II_(Ellingson)/05:_Wave_Reflection_and_Transmission/5.01:_Plane_Waves_at_Normal_Incidence_on_a_Planar_Boundary). The acoustic calculation linked above supplies the algebra we reuse here.

For the delta-function description of a current sheet and its connection to a field jump, see [W. C. Chew's electromagnetic field theory notes, Lecture 4, §4.3.3](https://engineering.purdue.edu/wcchew/ece604f19/Lecture%20Notes/Lect4.pdf#page=9).
