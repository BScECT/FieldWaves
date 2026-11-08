# Plane waves in one spatial dimension — proposed section sequence

Date: 2026-11-08. Status: first book-section draft written on 2026-11-08; ready for joint review.
Target: `book/5_electromagnetic_waves/plane_waves_1d.md`.
Companion to `planning/EMwaves_TOC_proposal.md`; this develops its section 2 without replacing the overall chapter plan.

## Purpose and level

Explain how Maxwell's equations constrain an electromagnetic travelling waveform. Reuse the mechanical-wave mathematics rather than introducing it again as unfamiliar theory. Keep one direction of spatial variation, retain three-dimensional vectors, and introduce harmonic notation only after a pulse has a clear physical interpretation.

Suggested thread: a radar transmits a pulse and measures a delayed echo. Begin with propagation in vacuum, approximating a path through air where appropriate; connect two-way delay to radar range. Earth-observation radar is the primary application, reflecting the instructor’s background. GPR is a secondary bridge to the later section on materials. Transmission lines can first be motivated by the cable feeding a radar antenna; soil-moisture probes are an optional later example.

The derivations below record the planned sequence and sign checks. The first student-facing draft is now in the target book page; review notes are in `EMwaves_plane_waves_review.md`.

## 1. The equation we already know

Recall the historical section's result in vacuum:

$$
\nabla^2\vec E=\mu_0\epsilon_0\frac{\partial^2\vec E}{\partial t^2}.
$$

Compare it directly with the existing acoustic equation for pressure, then reduce spatial variation to z. Ask students which derivatives vanish and why. A uniform plane wave has the same field at every point of a plane perpendicular to z at a given time; its field vectors still live in three-dimensional space.

Use the existing mechanical-wave pages explicitly:

- `4_mechanical_waves/acoustic_waves.md`: coupled equations and scalar wave equation.
- `4_mechanical_waves/wave_equation_solutions.md`: the arbitrary functions f(t+x/c) and g(t−x/c).
- `4_mechanical_waves/impedance.md`: companion fields, impedance, Fourier convention and delay as phase.

Do not repeat the curl–curl derivation already in the historical section.

## 2. Recover an arbitrary travelling waveform

Choose a smooth function F, with units of electric field, and test

$$
\vec E(z,t)=\hat x F(\tau),\qquad \tau=t-z/v.
$$

The chain rule gives

$$
\frac{\partial^2 E_x}{\partial z^2}=\frac{1}{v^2}F''(\tau),\qquad
\frac{\partial^2 E_x}{\partial t^2}=F''(\tau).
$$

It therefore satisfies the vacuum wave equation when v=c=1/√(μ₀ε₀). F need not be sinusoidal. Plot a finite smooth pulse at two times; a feature at fixed τ moves toward increasing z. The corresponding backward solution has argument t+z/v.

A crucial transition: satisfying this wave equation is necessary, but the field pair must also satisfy all four Maxwell equations. A longitudinal candidate ẑF(t−z/v), for example, generally fails Gauss's law in a source-free region. Use this as a short student check rather than supplying every result.

## 3. From B to H, staying in vacuum

The diffusion chapter already uses H. Reconnect that notation:

$$
\vec B=\mu_0\vec H,\qquad \vec D=\epsilon_0\vec E.
$$

B is magnetic flux density (tesla); H is magnetic field strength (A/m). Keep the core derivation in vacuum: B=μ₀H and D=ε₀E. Introducing H does not require introducing material response. Use vacuum constants in the equations below and v=c. The later media section will replace them with material parameters and discuss when a lossless, nondispersive approximation is appropriate.

In a region with no free charge and no conduction or impressed current, the equations become

$$
\begin{aligned}
\vec\nabla\cdot\vec E&=0,&\vec\nabla\cdot\vec H&=0,\\
\vec\nabla\times\vec E&=-\mu_0\frac{\partial\vec H}{\partial t},&
\vec\nabla\times\vec H&=\epsilon_0\frac{\partial\vec E}{\partial t}.
\end{aligned}
$$

The vacuum constants are spatially uniform. The wave speed remains v=c=1/√(μ₀ε₀).

## 4. Let Maxwell determine the field geometry and impedance

For fields depending only on z and t, Gauss's laws give ∂E_z/∂z=∂H_z/∂z=0. The z components of the curl equations also give ∂E_z/∂t=∂H_z/∂t=0. Thus the longitudinal components can only be uniform static backgrounds. Set those backgrounds to zero when discussing the wave disturbance: the wave fields are transverse.

Choose the simplest transverse electric field, E=x̂E_x(z,t). The full Cartesian curl reduces to the coupled pair

$$
\frac{\partial E_x}{\partial z}=-\mu_0\frac{\partial H_y}{\partial t},\qquad
\frac{\partial H_y}{\partial z}=-\epsilon_0\frac{\partial E_x}{\partial t}.
$$

Have students obtain at least one of these from the full curl. Avoid presenting a special simplified operator for them to memorize.

For E_x=F(t−z/v), substitution into the first equation determines the companion field, after removing a static background:

$$
\vec H(z,t)=\hat y\frac{F(t-z/v)}{\eta},\qquad
\eta=\mu_0 v=\sqrt{\mu_0/\epsilon_0}.
$$

The other equation checks the speed. Explain the distinction: the directions are perpendicular, but their signed amplitudes have the same waveform and timing. The instantaneous vectors satisfy H=(ẑ×E)/η for this forward wave; E×H points along +z. Save energy flux for its planned section.

For a backward wave the companion H changes sign relative to E. A useful final statement is

$$
E_x=F(t-z/v)+G(t+z/v),\qquad
H_y=\frac{F(t-z/v)-G(t+z/v)}{\eta}.
$$

Do not use E_x/H_y=η for an arbitrary incident-plus-reflected field. The simple impedance relation belongs to each travelling constituent.

**Scope:** a uniform travelling plane wave is an exact ideal solution in source-free vacuum. It also approximates radiation locally in suitable far-field regions, where curvature and amplitude variation across the observation region are small. Far field is not an additional requirement for the ideal solution itself. Orthogonality of E, H and propagation applies to a single travelling plane wave here; avoid asserting it for every superposition, near field, anisotropic medium or guided mode.

## 5. Can everything change everywhere at once?

Place the question before the explanation:

> Suppose both fields have the same values everywhere in a source-free homogeneous region, but vary with time: E=x̂f(t) and H=ŷg(t). Can they satisfy Maxwell's equations?

Both curls vanish, so both time derivatives must vanish. This geometry permits constant fields, but not simultaneous spatially uniform time variation. Explicitly assume spatial uniformity of both fields; uniformity of E alone does not force curl H to vanish.

Now use the forward-wave relation H_y=E_x/η in the reduced curl equation:

$$
\frac{\partial E_x}{\partial z}+
\frac{1}{v}\frac{\partial E_x}{\partial t}=0.
$$

Along z=z₀+v(t−t₀), the total derivative of E_x is zero. Equivalently, a boundary waveform E_x(0,t)=F(t) in a half-space, with no incoming wave from large z, gives E_x(z,t)=F(t−z/v). If F starts at t=0 and the region is initially undisturbed, the onset reaches z after z/v.

This is the precise finite-travel-time argument. Specify the boundary/initial conditions and one-way choice; the local equations also admit incoming waves, and a pre-existing oscillation throughout space is not the same thing as an instantaneous response to a newly switched source. Avoid saying that E and H alternately create one another in time: they are coupled fields, in phase for this travelling-wave solution.

**Why check Maxwell rather than only the wave equation?** A spatially uniform component a+bt satisfies the second-order wave equation, yet the proposed pair of spatially uniform fields violates the first-order curl equations if either slope is nonzero. This is an optional instructor observation, not required extra algebra for students.

## 6. Harmonic waves and complex fields

Specialize the established waveform:

$$
E_x(z,t)=E_0\cos(\omega t-kz+\phi),\qquad
k=\omega/v=2\pi/\lambda.
$$

Relate period, wavelength and the motion of a constant phase. Then use Euler's identity to package amplitude and phase:

$$
E_x(z,t)=\operatorname{Re}\{E_x(z)e^{i\omega t}\},\qquad
E_x(z)=E_0e^{i\phi}e^{-ikz}.
$$

Demonstrate the payoff immediately: time differentiation becomes multiplication by iω; forward propagation over d becomes multiplication by exp(−ikd). Compare the calculation with differentiating a cosine with an arbitrary phase.

Use the book's existing Fourier convention throughout: forward transform exp(−iωt), reconstruction exp(+iωt). Distinguish a one-frequency phasor from the full Fourier spectrum of a pulse. Phasor equations include

$$
\vec\nabla\times\vec E=-i\omega\mu_0\vec H,\qquad
\vec\nabla\times\vec H=i\omega\epsilon_0\vec E.
$$

Do not use tildes in the student text. Explain once that a complex representative and its real physical field should formally have distinct symbols, then use the same E and H symbols. Distinguish full harmonic fields from their phasors by their arguments and context. The intended message is that complex amplitudes are the standard working language for harmonic EM problems. Physical time-domain fields are real; pulse calculations remain useful in the time domain. Linearity permits frequency components to be solved separately and recombined. Defer nonlinear operations such as time-averaged power to the Poynting-vector section, where complex conjugation needs explanation.

Suggested check: derive the sign of the spatial phase for a backward wave and explain why a delay produces a negative phase with this convention.

## 7. A familiar structure: pressure and velocity, E and H

Put the coupled acoustic and electromagnetic equations side by side. With matching coordinate orientation:

$$
\begin{array}{c|c}
\text{Acoustics}&\text{Electromagnetism}\\ \hline
\partial p/\partial z=-\rho\,\partial u/\partial t
&\partial E_x/\partial z=-\mu_0\,\partial H_y/\partial t\\
\partial u/\partial z=-(1/K)\,\partial p/\partial t
&\partial H_y/\partial z=-\epsilon_0\,\partial E_x/\partial t\\
c_{\rm ac}=\sqrt{K/\rho}&v=1/\sqrt{\mu_0\epsilon_0}\\
Z_{\rm ac}=\rho c_{\rm ac}&\eta=\sqrt{\mu_0/\epsilon_0}
\end{array}
$$

Here u is acoustic particle velocity, to distinguish it from EM propagation speed v. The correspondence is mathematical; acoustic pressure is scalar and its particle motion is longitudinal, while the EM fields considered here are transverse. This prepares the later interface chapter without deriving reflection coefficients yet.

## 8. Telegrapher's equations: the same waves on a line

Keep this compact and connected to fields. Introduce an ideal parallel-plate line: separation d along x, width w along y, propagation along z, and negligible fringing (w≫d). With consistent positive voltage and conductor-current directions,

$$
V=dE_x,\qquad I=wH_y.
$$

Multiplying the two reduced Maxwell equations by d and w gives

$$
\frac{\partial V}{\partial z}=-L'\frac{\partial I}{\partial t},\qquad
\frac{\partial I}{\partial z}=-C'\frac{\partial V}{\partial t},
\qquad L'=\mu_0 d/w,\quad C'=\epsilon_0 w/d.
$$

L' is inductance per length (H/m); C' is capacitance per length (F/m). These are the lossless telegrapher's equations. Eliminating I gives

$$
\frac{\partial^2 V}{\partial z^2}=L'C'\frac{\partial^2 V}{\partial t^2},\qquad
v_{\rm line}=1/\sqrt{L'C'},\qquad Z_0=\sqrt{L'/C'}.
$$

For this ideal geometry, v_line=v and Z₀=ηd/w. Although both impedances have units of ohms, line impedance also contains geometry. Define V as a transverse voltage at fixed z; do not suggest that a single electrostatic scalar potential describes the entire time-dependent field.

A small distributed circuit can be a supporting sketch. Do not make a second independent circuit derivation, Smith charts or terminations part of this section. Mention resistance and leakage as later additions, keeping their equations and attenuation in `media_and_losses.md` as planned.

## Earth, Climate and Technology connections

Use Earth-observation radar as the recurring application, with GPR as a later connection:

- **Radar pulse and range:** for an idealized monostatic radar with a stationary target and propagation approximated by vacuum, a pulse echo has a round-trip delay Δt=2R/c. For a stipulated slant range of 600 km, the delay is approximately 4 ms. Use this to connect a delayed waveform with an observable. No reflection-coefficient derivation is needed yet: stipulate an echo and follow its travel time. Clarify that slant range is not necessarily platform altitude.
- **Radar phase:** for a harmonic component, a one-way delay contributes exp(−ikR), and round-trip propagation contributes exp(−i2kR), apart from the target’s scattering phase. This gives complex notation an immediate purpose. Detailed scattering, Doppler, SAR and interferometry can wait; the section should first build confidence with delay and phase.
- **Transmission lines in the radar system:** a pulse also takes time to travel along the antenna feed cable. Use the ideal vacuum-filled parallel-plate line for the field-to-line derivation; do not model the actual cable dielectric yet.
- **GPR, as a bridge to materials:** after the vacuum argument is secure, explain that the same travel-time reasoning will support subsurface measurements, once the propagation speed in the ground is known. EPA describes GPR pulse and travel-time measurements [3]. Move the numerical ε=9ε₀ example to the later media section rather than introducing it into the core derivation.
- **Optional later application:** soil-moisture TDR connects guided-wave travel time to material permittivity and water content [4]. It supports the media section but is not the organizing example here.

Avoid presenting conductive-ground diffusion as a slightly slower version of an undistorted wave. Explicitly reconnect with the earlier diffusion chapter and say that conductivity and dispersion determine when this section's approximation is useful.

## Proposed scope for the book section

Core: the waveform check; transverse geometry; companion H and impedance; uniform-field counterexample; finite delay; harmonic/phasor notation; a compact transmission-line bridge. Place a short student question at each of these transitions, with expandable worked answers where helpful.

Use three explanatory figures when drafting: a pulse at two positions/times; the three orthogonal directions with constant-value planes; and the parallel-plate geometry linked to a short line segment. No polarization taxonomy, full radiation-zone derivation, power calculation, interface coefficients or lossy propagation derivation yet. Those already have homes later in the chapter.

The section is dense for one two-block session if every derivation is done by the instructor. Protect the waveform, vector-component and delay checks as student work; make any full circuit derivation optional. Complex notation should be familiar from mechanics, but its sign and physical meaning still deserve explicit attention.

## Open sources to follow

1. David H. Staelin, *Electromagnetics and Applications* (MIT), §§2.2–2.3 for time-domain waves and harmonic notation; §7.1 and §8.1 for transmission-line fields and transients. [Open textbook](https://www.ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/mit6_013_s09_coursetextbook.pdf). Its time-domain-first ordering is particularly suitable here. The detailed sequence and student tasks above are our proposed adaptation.
2. Hermann A. Haus and James R. Melcher, *Electromagnetic Fields and Energy*, Chapter 14, especially §§14.1–14.3. [Open chapter and contents](https://ocw.mit.edu/courses/res-6-001-electromagnetic-fields-and-energy-spring-2008/pages/chapter-14/). A complementary structural reference connecting one-dimensional fields with distributed lines; use selectively at this student level.
3. US EPA, [Ground Penetrating Radar](https://www.epa.gov/environmental-geophysics/ground-penetrating-radar-gpr).
4. USDA NRCS, *Soil Survey Manual* (2017), Chapter 6, discussion of time-domain reflectometry. [Open chapter](https://www.nrcs.usda.gov/sites/default/files/2022-09/SSMch6.pdf).
