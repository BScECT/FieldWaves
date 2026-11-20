# Propagation through media: response, delay and attenuation

Revised TeachBook structure for discussion, 15 November 2026. First draft implemented under `book/5_electromagnetic_waves/04_00_media_and_losses.md`, with four linked subsections. This document proposes the book development, main equations, student questions and visual elements. The outline below records the agreed development; the first teaching-text draft and embedded figures now exist.

## Main story

**A radar wave has reached the ground. The material responds to its electric and magnetic fields. That response changes the wave's wavelength, phase and amplitude; the changes tell us something about the material.**

The development is:

**material response → lossless propagation → delayed polarization and dielectric loss → attenuation and energy deposition → added conduction loss → conductive/diffusive limit → radar penetration.**

Dielectric loss is a central mechanism. Students should encounter a decaying wave with σ=0 before conductivity is added. A finite-conductivity conductor is one important lossy-medium limit, not the only explanation for attenuation.

Use linear, homogeneous, isotropic media, with real positive μ in the core. Fields vary along z, but start from vector Maxwell equations and explicitly simplify divergence/curl. Keep exp(+jωt), exp(−jkz), j, and the established convention of using context to distinguish phasors from real fields. Take the incident field just inside the material as given. Reflection on entry and exit belongs to the following section.

## 1. The medium responds: what do ε and μ describe?

**Story:** charges in matter can move a little, dipoles can reorient, and magnetic moments can respond. We describe their collective response without following every molecule.

Main relations:

$$
\vec D=\epsilon_0\vec E+\vec P,\qquad
\vec P=\epsilon_0\chi_e\vec E,\qquad
\epsilon=\epsilon_0(1+\chi_e),
$$

$$
\vec B=\mu_0(\vec H+\vec M)=\mu\vec H.
$$

Initially use instantaneous, real-valued response. Define P as dipole moment per unit volume, D in C/m², ε in F/m and μ in H/m. Material polarization P describes response of matter; wave polarization describes the trajectory of the real E-field tip. A short reminder should prevent the two uses of the word becoming mixed up.

Retrieve the capacitor: C=εA/d. At fixed voltage and geometry, the larger dielectric response requires more plate charge. This links the new material parameter to something already understood.

For soils, show solid grains, air and water in pores. Porosity, water content and mineral composition affect the effective permittivity. Water's permanent molecular dipoles are a useful physical explanation for its strong response. Mention that dissolved ions provide a separate conduction mechanism, developed later. Do not treat ε as a single constant for water at every frequency and temperature.

Keep μ in the mathematics, then choose μ≈μ₀ for the ordinary weakly magnetic materials used in the radar examples. This approximation does not cover every rock, mineral or frequency. Magnetic loss can also be described through complex μ, but it is outside the core examples.

**Student question:** why might two soils with different water contents have different radar travel times? This is a prediction to revisit after the propagation equations.

**Figure:** pore-space mixture and bound dipoles, with an explicit distinction from mobile ions.

## 2. A lossless material changes speed, wavelength and E/H

**Story:** changing the material does not automatically mean losing energy.

For real ε,μ, with σ=0, retrieve the harmonic Maxwell equations:

$$
\nabla\times\vec E=-j\omega\mu\vec H,\qquad
\nabla\times\vec H=j\omega\epsilon\vec E.
$$

Use the curl-curl identity and ∇·E=0 in the homogeneous charge-free bulk to recover

$$
\nabla^2\vec E+k^2\vec E=0,\qquad k^2=\omega^2\mu\epsilon.
$$

Reduce the proposed transverse field E=x̂E_x(z) only after displaying the vector relation. The familiar solution gives

$$
v_p=\frac{\omega}{k}=\frac{1}{\sqrt{\mu\epsilon}},\qquad
\lambda=\frac{2\pi}{k},\qquad
\eta=\frac{E_x}{H_y}=\sqrt{\frac{\mu}{\epsilon}}.
$$

For μ≈μ₀, v_p≈c/√ε_r. The source fixes temporal frequency; the material changes spatial frequency and wavelength. Retrieve H from the Cartesian curl at least once, not just from a supplied impedance formula.

**Student check:** with μ and source frequency fixed, quadruple ε. Speed, wavelength and impedance all halve. No attenuation has been introduced.

**Application:** a slower wave takes longer to reach a given depth. An incorrect assumed speed produces an incorrect radar depth estimate. Save reflection coefficients for the interface section.

## 3. A dielectric response can lag: complex ε before conduction

**Story:** bound charges and dipoles do not necessarily follow a changing field instantaneously. A dissipative lag can transfer energy to the material even when σ=0.

Write the phasor constitutive law

$$
\vec D=\epsilon_d(\omega)\vec E,\qquad
\epsilon_d=\epsilon'-j\epsilon''_d.
$$

Here ε′ and ε″_d are real, with ε″_d≥0 for passive electric loss under our exp(+jωt) convention. Both have units F/m. The subscript d identifies the dielectric response; conductivity has not been folded into it.

**Short worked model:** take one simple relaxing polarization contribution,

$$
\tau\frac{\partial\vec P}{\partial t}+\vec P
=\epsilon_0\chi_s\vec E.
$$

Students replace the time derivative by jω and obtain

$$
\vec P=\frac{\epsilon_0\chi_s}{1+j\omega\tau}\vec E,
\qquad
\epsilon_d=\epsilon_0\left(1+\frac{\chi_s}{1+j\omega\tau}\right).
$$

This deliberately simple model has one relaxation time and a vacuum background. It explains the mathematics; realistic material presets later use appropriate measured/modelled ε(ω), including faster response contributions. Do not present it as a complete soil or water model.

The response amplitude and phase depend on ωτ. Let students use the complex denominator to identify the lag and the sign of the imaginary part. A fully worked version can be an admonition, but the physical explanation of dielectric loss belongs in the main text.

**Where does the loss show up?** Ampère–Maxwell contains

$$
j\omega\vec D
=\omega\epsilon''_d\vec E+j\omega\epsilon'\vec E.
$$

The first contribution is in phase with E and takes positive average power. This gives meaning to ε″ rather than declaring that an imaginary number means loss. The same relaxing response also changes ε′ with frequency: this is a first concrete example of dispersion.

**Student check:** can a material with σ=0 still absorb an EM wave? Use this equation to explain the answer.

**Figure:** field and material response over time, or phasor arrows, showing the lag. Avoid implying a universal one-to-one energy-density formula involving ε′ in a dispersive medium.

## 4. The resulting wave attenuates: complex k, H and energy flux

**Story:** the material's complex response changes the spatial behaviour demanded by Maxwell's equations. Now demonstrate attenuation in the dielectric with σ=0.

The same curl calculation gives

$$
\nabla^2\vec E+k^2\vec E=0,\qquad
k^2=\omega^2\mu\epsilon_d.
$$

Write

$$
k=\beta-j\alpha,\qquad
\vec E(z)=\hat xE_0e^{-jkz}
=\hat xE_0e^{-\alpha z}e^{-j\beta z}.
$$

Restore exp(jωt) to read the physical oscillation. β is the spatial angular frequency, λ=2π/β and v_p=ω/β. α controls the envelope. Keep both positive for the ordinary passive travelling-wave examples.

**Student PDE check:** differentiate twice, substitute the candidate into Helmholtz and compare real and imaginary parts:

$$
\beta^2-\alpha^2=\omega^2\mu\epsilon',\qquad
2\alpha\beta=\omega^2\mu\epsilon''_d.
$$

This explicitly shows attenuation from dielectric loss alone. Give a candidate with the wrong sign of α and ask what its amplitude would do into the passive half-space. Supply any general complex square root computationally; students need not memorize nested radicals.

Retrieve H from the full Cartesian curl, setting absent components and transverse derivatives to zero:

$$
H_y=\frac{k}{\omega\mu}E_x,\qquad
\eta=\frac{\omega\mu}{k}.
$$

The fields remain transverse and mutually perpendicular for this uniform plane wave, but their real oscillations can have a relative phase. Complex impedance prepares the interface section without turning into a separate topic.

Return to the established phasor Poynting vector:

$$
\langle S_z\rangle=\frac12\operatorname{Re}\{E_xH_y^*\}
=\frac{\beta}{2\omega\mu}|E_0|^2e^{-2\alpha z}.
$$

**Divergence as a physical statement:** students differentiate the flux and use 2αβ=ω²με″_d to obtain

$$
\nabla\cdot\langle\vec S\rangle
=\frac{d\langle S_z\rangle}{dz}
=-\frac{\omega\epsilon''_d}{2}|\vec E|^2.
$$

The negative divergence is energy deposited per unit volume and time. Here it is dielectric heating, with no ohmic conduction. A plane wave is fading even though its wavefront area is not expanding.

Define the field attenuation depth δ_E=1/α. At that depth field amplitude is 1/e; one-way power is 1/e². The one-way 1/e power depth is 1/(2α). Call the general quantity field attenuation depth first, and connect it to the familiar conductor skin depth below.

## 5. Add conduction: a second mechanism in the same framework

**Story:** mobile charge provides another way to take energy from the wave. We can keep this mechanism separate physically while combining the algebra.

Add J_c=σE:

$$
\nabla\times\vec H=(\sigma+j\omega\epsilon_d)\vec E
=j\omega\epsilon_{\rm eff}\vec E,
$$

$$
\boxed{\epsilon_{\rm eff}
=\epsilon_d-j\frac{\sigma}{\omega}
=\epsilon'-j\left(\epsilon''_d+\frac{\sigma}{\omega}\right).}
$$

Students factor jω and check units. Once σ/ω is included in ε_eff, it must not be added again as an independent conductivity term. A measured effective complex permittivity may already contain both loss mechanisms.

The propagation equations remain the same with ε_d replaced by ε_eff. There is no second plane-wave derivation:

$$
k^2=\omega^2\mu\epsilon_{\rm eff},\qquad
-\nabla\cdot\langle\vec S\rangle
=\frac12\left(\omega\epsilon''_d+\sigma\right)|\vec E|^2.
$$

This separates dielectric heating and Joule heating. Both can be important; neither is implied solely by a large ε′.

**Student question:** add salt to a water sample. Which response term would we particularly expect to change, and why? Do not claim that every other property remains exactly fixed.

## 6. Conductive dominance, diffusion and skin depth

**Story:** the good-conductor result is a limit of the general lossy-medium framework, and retrieves the earlier diffusion chapter.

Conduction dominates the dielectric current when

$$
\sigma\gg\omega|\epsilon_d|.
$$

For a weakly lossy dielectric background this reduces to the familiar comparison σ/(ωε′)≫1. Specify frequency: “good conductor” is a comparison between response terms, not just a permanent material label.

In this limit,

$$
k^2\approx-j\omega\mu\sigma,\qquad
k\approx(1-j)\sqrt{\frac{\omega\mu\sigma}{2}},
$$

$$
\alpha\approx\beta\approx\sqrt{\frac{\omega\mu\sigma}{2}},\qquad
\boxed{\delta_E\approx\sqrt{\frac{2}{\omega\mu\sigma}}.}
$$

Have students use (1−j)²=−2j to verify the root and choose the decaying solution.

**Time-domain connection:** in the simplified instantaneous real-ε, ohmic-σ model, curl-curl gives

$$
\nabla^2\vec E
=\mu\epsilon\frac{\partial^2\vec E}{\partial t^2}
+\mu\sigma\frac{\partial\vec E}{\partial t}.
$$

Neglecting displacement in the conductive regime retrieves

$$
\frac{\partial\vec E}{\partial t}
=\frac{1}{\mu\sigma}\nabla^2\vec E.
$$

Check diffusivity 1/(μσ) in m²/s. The frequency-dependent complex ε of a relaxing material cannot simply be inserted as a constant into that time-domain PDE; the polarization dynamics would have to be retained. The frequency-domain formulation handles that dependence naturally.

At fixed μ,σ within the conductor limit, δ_E∝f^(−1/2), or ∝√λ₀ with λ₀=c/f. This is a useful scaling, not a universal law of radar penetration. In the weak-conduction, negligible-dielectric-loss limit with fixed parameters, α≈(σ/2)√(μ/ε′) is approximately independent of frequency. In a relaxing dielectric, the material response introduces its own frequency dependence.

## 7. Read the Earth-material examples through these equations

Return to the opening question using three comparisons, not a catalogue of applications.

- **Dry/wetter soil:** water content changes effective ε and travel time; pore-water conduction, salinity, clay and dielectric loss can reduce penetration. Some wet soils are penetrable. Material composition and frequency matter.
- **Freshwater/seawater:** water's molecular response gives dielectric loss; dissolved ions add conduction. Suitable freshwater can be penetrated with GPR, including lake-bottom investigations, while conductive saline water and many microwave settings have shallow penetration. Do not explain water opacity only through conductivity or only through its large ε′.
- **Same material, different frequency:** evaluate the full complex k using stated ε(ω),σ,μ. Separate a fixed-parameter thought experiment from realistic measured/modelled material response. Do not apply the conductor square-root approximation to every radar band.

For a simple reflector at depth d, the down-and-back propagation factors are

$$
\frac{|E_{\rm echo}|}{|E_{\rm echo,no\ loss}|}=e^{-2\alpha d},\qquad
\frac{P_{\rm echo}}{P_{\rm echo,no\ loss}}=e^{-4\alpha d}.
$$

These isolate absorption along the same path. Actual sensing depth also depends on surface transmission, target contrast, scattering, spreading and noise. The next sections supply interface coefficients and layer interference.

Finish with the bridge: **η governs field matching; exp[−jk(ω)d] governs one-way propagation through a layer.** Together they will explain a measured frequency response.

## Optional ionosphere box

Supply the collisionless unmagnetized plasma model,

$$
\epsilon_r=1-\frac{\omega_p^2}{\omega^2},\qquad
k^2=\frac{\omega^2-\omega_p^2}{c^2}.
$$

Students examine the sign of k² and verify an oscillating or decaying solution. Below the cutoff, a single decaying field in a semi-infinite ideal plasma has zero average normal flux and no collisional heating: decay alone does not prove absorption. This makes a useful optional PDE/phasor exercise after the core distinction between material loss and propagation has become secure.

It is a simplified model, not a treatment of Earth's magnetic field, altitude profiles, GNSS group delay or Faraday rotation. Those effects can be later applications; no new tensor or group-velocity development is required here.

## Proposed figures and embedded explorations

1. **Material response:** bound polarization and pore-space mixture; then a time trace/phasor sketch giving the dielectric lag meaning.
2. **Decaying-wave interactive:** real E snapshot, envelope, H phase and mean power. Start with dielectric loss at σ=0, then add conductivity. An exploratory α/β mode can teach the exponent, but material mode should enforce k²=ω²με_eff. Keep amplitude/power scales fixed.
3. **Frequency/material interactive:** ε′ and ε″ alongside attenuation depth, with traceable material assumptions. Compare dielectric loss and conduction contributions; overlay the good-conductor approximation only where its assumptions hold. Include one-way versus round-trip attenuation.

Two integrated interactive elements are enough; put them directly in the TeachBook. These are placeholders for later implementation, not companion notebooks.

## Questions to weave through the text and later practice

- Predict how ε affects speed, wavelength and E/H before adding loss.
- Replace a time derivative by jω in the simple polarization response and interpret its phase.
- Check a decaying E/H pair against both Maxwell curls, not just Helmholtz.
- Recover spatial frequency and attenuation from phase/amplitude measurements at two depths, with phase wrapping specified.
- Use divergence of mean Poynting flux to distinguish material heating from geometrical spreading.
- Check attenuation factors for field, power and a round trip; test conductor and lossless limits.
- Explain why high permittivity alone does not establish strong attenuation, and why σ=0 does not establish a lossless dielectric.

## Literature and authoring basis

- [Ellingson, Electromagnetics Volume 2, chapter 3](https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electromagnetics_II_(Ellingson)/03:_Wave_Propagation_in_General_Media): wave equations, complex constitutive response, attenuated plane waves, energy flux and conductor limits. Our order makes dielectric loss explicit before adding conduction.
- [Staelin, Electromagnetics and Applications, §9.2.4 and §9.5.3](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/MIT6_013S09_chap09.pdf): complex wavenumber and the optional plasma extension.
- [Baker-Jarvis and Kim, NIST, 2012](https://nvlpubs.nist.gov/nistpubs/jres/117/jres.117.001.pdf): physical dielectric response, relaxation and distinct dissipation mechanisms. Background for authoring rather than required reading.
- [EM GeoSci: permittivity, porosity and saturation](https://em.geosci.xyz/content/physical_properties/dielectric_permittivity/dielectric_permittivity_factors.html): Earth-material interpretation. Translate all signs to our time convention; do not copy frequency-independent water values into every radar band.
- [EPA: waterborne GPR](https://www.epa.gov/environmental-geophysics/waterborne-ground-penetrating-radar): freshwater penetration and the importance of conductivity, with field examples.

Keep detailed α/β radicals, constitutive tensors, magnetic-loss models, a second transmission-line derivation and general dispersive energy-density formulas outside the core. The short relaxation model earns its place by explaining complex ε; it should not expand into a material-spectroscopy chapter.

## First implementation

Implemented on 15 November 2026 using the same numbered overview/subsection structure as the preceding 3D-wave section:

- `04_00_media_and_losses.md`: overview and navigation.
- `04_01_material_response.md`: physical meaning of ε and μ, soil mixture, lossless speed/wavelength/impedance.
- `04_02_lossy_dielectrics.md`: complex dielectric response, optional relaxation model, PDE and Maxwell checks, bounded solution, phasor flux and divergence/heating.
- `04_03_conductors_and_skin_depth.md`: added conduction, combined loss, conductor limit, time-domain diffusion retrieval.
- `04_04_radar_penetration.md`: material/frequency comparison, round-trip loss, inverse question, optional plasma exercise and bridge to interfaces.

Three editable SVG figures and two self-contained embedded explorers are included. Their generators are `scripts/plot_media.py` and `scripts/build_media_interactives.py`, with shared Python models in `scripts/media_models.py`. Presets are explicitly illustrative rather than measured fits. No companion notebook is required.
