# From a satellite to a measurement on Earth — lecture plan

First proposal, 15 November 2026. Two 45-minute teaching blocks; the break is outside those 90 minutes. Proposed lecture code: **W2.2L1**, following the first plane-wave practice session. This is a teaching plan; no new slides are created yet.

Basis: the current TeachBook section `book/5_electromagnetic_waves/waves_3d_energy_polarization.md`, including the bistatic figure, both embedded activities, energy density, phasor power and polarization. This lecture selects a route through that material rather than working through every derivation on the page.

## The thread

A satellite sends a wave. What arrives at the ground, and what does an antenna measure?

The four stages are **a spreading wave → a local plane wave → energy arriving → a measured component**. Radar supplies the continuing source–ground–receiver picture. GNSS supplies a concrete reason to consider circular polarization. Keep Faraday rotation as a later destination, not another calculation in this lecture.

## What students should be able to do afterwards

1. Explain the local plane-wave approximation and judge its error against a stated phase tolerance, separately from amplitude error.
2. Read an oblique plane-wave expression and use Cartesian derivatives, divergence and curl to test it. Explain why passing Faraday's law alone is insufficient.
3. Distinguish stored energy density (J/m³), energy flux (W/m²) and power (W); explain geometrical spreading without confusing it with absorption.
4. Calculate average energy flux using peak-amplitude phasors: ⟨S⟩ = ½ Re{E × H*}. Explain the conjugate and the averaging factor.
5. Interpret linear/circular polarization from complex components and calculate an ideal linear receiver's voltage projection and average power.

The mathematical goal is to make the operators and complex expressions say something physical. Do fewer complete calculations together, and keep asking students to supply the next step.

## Block 1 — From the source to a local wave

| Time | Mode | Sequence and student contribution |
|---|---|---|
| 0–4 | Figure and discussion | Show the approved bistatic satellite figure. Trace transmission, propagation, interaction and reception. Ask: why have we been using plane waves if antennas are localized? Separate the propagation direction from E's direction. |
| 4–10 | Short board retrieval, then supplied result | Introduce ψ = (A/r)F(t−r/c), r = √(x²+y²+z²). Students identify constant-argument motion and spherical fronts. Give about 1 minute to retrieve ∇r; collect the geometric meaning. State the radial Laplacian and show the already-worked cancellation from the book, asking which terms disappear. The scalar wave equation is satisfied away from the source; vector EM fields still need Maxwell's equations. Leave the full differentiation for the book. |
| 10–22 | **Protected board sequence 1** | Derive the local plane approximation with small displacements (δx,δy,δz). Students identify the small quantity for √(1+u) ≈ 1+u/2 and predict the linear versus quadratic distance changes. About 2 minutes of this slot are for individual/pair attempts. End by identifying the curvature error in phase. |
| 22–28 | Prediction → error explorer → feedback | Use 30°-from-zenith geometry. Before touching controls, ask which error changes with wavelength. Change wavelength, then patch width; use distance only if time permits. Students explain the different responses. Compare the numerical errors, not the apparent heights of curves on different vertical scales. Use π/4 as the chosen tolerance, with application-dependent acceptability. |
| 28–40 | **Protected board sequence 2** | Turn the coordinate-axis wave into the diagonal wave E = ŷE₀F[t−(x+z)/(c√2)]. Give 3 minutes to sketch propagation, check E·n = 0 and find the two nonzero second derivatives. Build the Laplacian and full divergence together, then use the full Cartesian curl to recover H's direction. Keep equations beside the sketch. |
| 40–45 | Short diagnostic and feedback | Display the deliberately incorrect pair E = x̂E₀F(t−2z/c), H = ŷ(2E₀/η₀)F(t−2z/c). Give roughly 2 minutes to test the reduced curl relations, then assemble the result: Faraday passes, Ampère–Maxwell gives a factor-four mismatch. Ask what speed the expression claimed. The complete check is in the book. Close with: a candidate field has to satisfy the governing equations together. |

### Board sequence 1: zoom in without losing the geometry

Keep a sketch of the source, receiver at (0,0,R), and the small displacement visible. Write the actual nearby position first:

$$
(x,y,z)=(\delta x,\delta y,R+\delta z).
$$

Ask students to identify what is small before writing

$$
r=(R+\delta z)\sqrt{1+\frac{(\delta x)^2+(\delta y)^2}{(R+\delta z)^2}}.
$$

Retrieve the square-root Taylor approximation, then obtain

$$
r\approx R+\delta z+\frac{(\delta x)^2+(\delta y)^2}{2R}.
$$

Prompts while building it:

- If we move towards/away from the source, why does distance change to first order?
- If we move sideways, why is there no first-order distance change at the centre?
- Which term describes curvature? What do we discard to obtain a local plane wave?

End with ψ ≈ (A/R)F(t−R/c−δz/c). Emphasize the region over which it is approximately valid. For the activity, rotate the geometry and move the coordinate origin explicitly: the centre of the horizontal ground patch becomes x = z = 0.

In the 30° activity the local plane already includes the linear ground phase slope:

$$
r_{\rm plane}=R+x\sin\theta,\qquad
r-r_{\rm plane}\approx\frac{x^2\cos^2\theta}{2R}.
$$

Here θ = 30° is the source's zenith angle. It is a different angle from the receiving-antenna azimuth used later. Do not spend the activity slot deriving the rotated formula again; identify its meaning from the geometry.

At R = 800 km, ground half-width 150 m and λ = 3 cm, the maximum amplitude departure is about 0.0094%, while phase error is about 2.2 rad. Ask students whether amplitude constancy alone is enough. The answer depends on the measurement and chosen error budget; π/4 is this example's working tolerance.

### Board sequence 2: let the derivatives describe the wave

Write the three-dimensional Laplacian before simplifying. Keep the field's direction separate from the directions of variation:

$$
\nabla^2E_y=
\frac{\partial^2E_y}{\partial x^2}
+\frac{\partial^2E_y}{\partial y^2}
+\frac{\partial^2E_y}{\partial z^2}.
$$

Students should obtain two contributions E₀F''/(2c²), which add to the required E₀F''/c². Then expand divergence: E has only a y component, but that component is independent of y. It is transverse because E·n = 0, not because it happens to point along a coordinate axis.

For curl, write the full Cartesian expression, then cross out absent components and zero derivatives. Obtain

$$
\nabla\times\vec E=
\frac{E_0}{c\sqrt2}(\hat x-\hat z)F',\qquad
\vec H=\frac{E_0}{\eta_0\sqrt2}(-\hat x+\hat z)F.
$$

Recover H from Faraday and check its direction against n × E. For the correct travelling-wave pair, briefly identify the other Maxwell constraints; do not imply Faraday established everything. The following counterexample makes that distinction concrete.

## Block 2 — From field energy to a received signal

| Time | Mode | Sequence and student contribution |
|---|---|---|
| 0–9 | **Protected board sequence 3** | Introduce energy stored in fields, u = ε₀E²/2 + μ₀H²/2, and distinguish this from flux S = E × H. Check units. Give 2 minutes to use E = η₀H to show equal electric/magnetic contributions and u = ε₀E². Together obtain S = cu n. For a travelling sinusoid the two contributions rise and fall together. |
| 9–14 | Geometry, flux and conservation | Return to the spreading fronts: P = ∮⟨S⟩·n_A dA. Students explain why the same power crosses larger enclosing spheres in a lossless region. Recover intensity ∝ r⁻² and amplitude ∝ r⁻¹. For a real directional antenna this range scaling applies along a fixed radiation direction. Retrieve Gauss's theorem verbally; leave the full shell and local-conservation proofs in the book. |
| 14–26 | **Protected board sequence 4** | Derive average power using phasors. Average a product of two real sinusoids, identify the surviving phase difference and express it as ½ Re{ab*}. Apply componentwise to obtain ½ Re{E × H*}. Give 2 minutes to conjugate H for the diagonal phasor and cancel spatial phases. Use feedback to connect this to uniform average power and to show a common phase shift cannot change that power. |
| 26–32 | Short board construction and prediction | Write E_linear = E₀x̂e⁻ʲᵏᶻ and E_circular = E₀(x̂+jŷ)e⁻ʲᵏᶻ/√2. Ask students what j means as a relative phase and sketch the real tip path at one point. Check E·E* = E₀² for both. Introduce the receiving voltage phasor q = (E/E₀)·a and power ratio |q|². |
| 32–40 | Prediction → polarization explorer → feedback | Use the three experiments below. Keep the average-power scale and incident intensity fixed. Ask students to explain each outcome from the dot product and phasor, rather than narrating slider motion. |
| 40–45 | Individual exit check and close | Give 2–3 minutes for the three questions below; discuss or collect responses. Reconnect the radar picture: later materials/interfaces will alter amplitude, phase and polarization. GNSS provides the circular-signal comparison; Faraday rotation remains a future application. |

### Board sequence 3: stored energy is not energy flux

Start with a physical question: a static electric field can store energy even when there is no magnetic field and S = 0. What does that tell us about the difference between energy present and energy transported?

Supply the vacuum energy-density formula; no capacitor or inductor derivation in this lecture. Let students derive the plane-wave consequences rather than supplying all of them at once:

$$
u_E=u_H,\qquad u=\epsilon_0|\vec E|^2,
\qquad \vec S=\frac{|\vec E|^2}{\eta_0}\hat n=cu\hat n.
$$

These are real instantaneous fields. Introduce the phasor averages explicitly in the next sequence. Keep the units J/m³, W/m² and W in a small persistent corner of the board; have students name the surface integral that connects flux to power.

### Board sequence 4: discover why the conjugate is needed

Begin with a = a₀eʲᵅ, b = b₀eʲᵝ and their real oscillations. Provide the product-to-sum identity if recall stalls; the learning target is what survives averaging and how the conjugate encodes it.

$$
\langle a_{\rm real}b_{\rm real}\rangle
=\frac{a_0b_0}{2}\cos(\alpha-\beta)
=\frac12\operatorname{Re}\{ab^*\}.
$$

Ask: why not ab? Why does the term oscillating at 2ω disappear? Then write

$$
\boxed{\langle\vec S\rangle
=\tfrac12\operatorname{Re}\{\vec E\times\vec H^*\}.}
$$

Use peak-amplitude phasors, j for the imaginary unit, and no tildes. The phasors omit the common eʲωᵗ factor. In the diagonal-wave check, conjugating H reverses the sign of its spatial phase, so the propagation factors cancel:

$$
e^{-jk(x+z)/\sqrt2}e^{+jk(x+z)/\sqrt2}=1.
$$

The result is ⟨S⟩ = E₀² n/(2η₀). Ask what an extra common phase would do. If time permits, retrieve the average energy density from the same averaging rule, giving ⟨S⟩ = c⟨u⟩n. The general average-density formula is available in the book; it need not become another full derivation.

## The polarization activity: three experiments, not an open-ended demonstration

Use the embedded activity from the TeachBook, initially paused. Define the two antenna angles from the controls: β is angle to propagation; θ is rotation around it. This θ is unrelated to the incidence angle in the earlier activity.

1. **Linear signal, transverse antenna.** Start aligned along x, ask what a 90° turn will do, then use the y preset. Power goes from 100% to zero. Connect the voltage factor cos θ to the power factor cos²θ.
2. **Circular signal, transverse antenna.** Switch polarization at fixed incident intensity. Predict the outcome of the same rotation. Power stays at 50% of the aligned-linear reference; the voltage phasor phase and trace shift. Play briefly, then pause to inspect the real field and q. This is an ideal linear receiving antenna, not a full model of a conventional circularly polarized GNSS receiver antenna.
3. **Antenna along propagation.** Ask before using the longitudinal preset. Both signal types give zero because E has no longitudinal component. The dot product is the explanation; no new antenna-pattern formula is needed.

The 1/√2 normalization of the circular field is essential: switching signal type must not silently double incident intensity. Do not attempt a complete taxonomy of ellipses or right/left conventions. Recognize elliptical polarization as the general case, with the book providing the construction.

## Exit check

Give a normalized circular field phasor (x̂+jŷ)/√2 travelling along +z, with the common propagation factor understood.

1. An ideal linear receiver points along z. What does it receive, and why?
2. It points along x, then rotates to y. Does average power change? Does the received voltage phasor change?
3. When the distance from a localized radiator doubles along a fixed radiation direction in a lossless region, what happens to field amplitude and intensity? Has energy been absorbed?

Instructor checks: zero longitudinal projection; equal power in x and y with a quarter-cycle phase difference; amplitude halves, intensity quarters, and spreading distributes power over more area. Use difficulties to select the following practice questions.

## Protecting the time for board work

The four protected sequences occupy **45 minutes**: 12 + 12 + 9 + 12, including their student attempts. The plan also reserves short attempts, predictions, activity feedback and an individual exit check. These are not 90 minutes of lecturer algebra.

Organize the board into a persistent geometry/key-relations area and an active calculation area. Start a derivation from a picture and a question. Let students suggest the next derivative, phase factor or projection before writing it. Keep long worked answers off the screen while students are trying the corresponding step. Slides should hold diagrams, prompts, supplied formulas and final results rather than duplicate each board line.

Prepare static activity snapshots as fallback: phase error versus tiny amplitude error; linear aligned/crossed; circular transverse; longitudinal antenna. Open both activities before class to avoid losing the prediction window to navigation.

## Deliberate scope limits and recovery plan

Keep outside the core lecture:

- Full spherical-wave derivative cancellation and derivation of the radial Laplacian. One PDE check is supplied and interpreted; the diagonal wave is the substantial student check.
- Full local Poynting theorem derivation, complex reactive-power theory, and radiation pressure.
- A separate worked tilted collecting-surface problem. The surface-normal projection is stated; contrast it briefly with antenna-axis projection.
- Jones/Stokes formalisms, ellipse parameters, handedness conventions, antenna gain/effective aperture, the radar equation and plasma derivations.
- Any return to transmission-line algebra.

If block 1 runs slowly, shorten the spherical-wave check to its physical reading plus final PDE result; then reduce the error explorer to the wavelength prediction and its default numerical comparison. Keep the Taylor explanation, diagonal Cartesian check and the Faraday counterexample. The latter can be completed with its Faraday result supplied and students testing Ampère–Maxwell only.

If block 2 runs slowly, supply the inverse-square result after the conservation question and omit the optional average-energy-density formula. Keep the phasor-conjugate derivation and all three polarization outcomes. Reduce the animation time, not the prediction/debrief. Preserve at least the first two exit questions.

The first practice/formative session after this lecture should revisit the complete incorrect-pair calculation, a phasor cross product, receiver projections and the distinction between spreading and absorption. If students cannot reliably interpret the dot and cross products, use that evidence to simplify the next media section rather than adding algebra.
