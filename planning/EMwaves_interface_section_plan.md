# Plane waves at an interface: reflection and transmission

Date: 2026-11-21  
Status: first TeachBook draft implemented on 2026-11-21. Conducting reflection is the worked extension; finite-object scattering is a conceptual application. Normal-incidence and current-sheet figures, the shrinking Faraday loop, and embedded soil-moisture/conductor activities are implemented; remaining visual proposals await joint development. Slides are not part of this draft.

## Story and scope

A radar wave reaches a change in material. How much continues, how much comes back, and what can that tell us about the material? The central physical thread is **field induces current → current generates field → the generated field contributes to reflection and transmission**. Work this out for a conducting sheet, connect it to planar-interface results and polarization, then illustrate how the same idea produces a radar echo from a finite object.

The mathematical thread is **solutions in each homogeneous region → superposition → interface and incoming-wave conditions → amplitudes → physical checks**. The new work is using Maxwell's equations at an interface, matching phase along a boundary and keeping track of vector directions. Normal-incidence coefficient algebra and the geometric derivation of Snell's law have already been covered in mechanical waves and should not be taught again.

Use harmonic fields with the common time factor exp(+jωt), forward propagation exp(−jkz), and no phasor tildes. Begin with linear, isotropic, lossless media, with positive real ε and μ. Loss can return in a short connection to the preceding section. Oblique incidence in absorbing media is outside the core.

This revises the original planning: oblique incidence and polarization remain core; the conducting-sheet calculation is the selected worked extension. A finite object provides a visual application without a radiation-theory derivation. Finite-slab interference, general multilayers and scattering matrices are deferred. The interface material shares the remaining teaching time with the unfinished complex-permittivity-to-attenuation derivation; protect student working time before adding optional topics.

## What we reuse from mechanical waves

The existing [acoustic reflection and transmission section](../book/4_mechanical_waves/reflection_transmission.md) already obtains the two matching equations, the impedance coefficients and the sign change in the reflected companion field. The [Snell's law section](../book/4_mechanical_waves/snells_law.md) already derives the angle relation geometrically.

| Already encountered | Role here |
| --- | --- |
| Incident, reflected and transmitted harmonic waves | Recall the geometry without rebuilding the travelling-wave notation. |
| Pressure and particle velocity matching | Map to tangential E and H; derive why these are the EM matching conditions. |
| Acoustic impedance ρc and the coefficient algebra | Replace the physical impedance by η = √(μ/ε); reuse the result. |
| Geometric Snell's law | Recall the result, then show how boundary phase matching produces the same law. |

Keep this bridge short. Ask students to make the correspondences rather than repeating a worked acoustic derivation with different letters. The same equations describe different physical quantities; the impedances have different units.

## 1. Why an interface makes an echo

- Connect an acoustic reflection at a material boundary to a radar reflection at an air–ground or internal subsurface boundary.
- Separate **reflection at the boundary** from **attenuation during propagation**. A weak subsurface echo can have either cause, and generally both.
- Introduce the idealization: homogeneous half-spaces separated by z = 0, with medium 1 at z < 0 and medium 2 at z > 0.
- Introduce the source picture: an incident field drives a response in the material, and that response emits an additional field. In a conductor the response includes mobile-charge currents; in a dielectric it includes the polarization currents encountered in the media section.
- Pose the question: can an incident wave and a transmitted wave alone satisfy all the conditions at the interface?

**Figure:** one clear normal-incidence geometry, with incident/reflected/transmitted propagation arrows and E/H directions. Reuse it through the normal-incidence discussion.

**Student prompt:** which parts of the acoustic calculation should carry over, and which physical conditions still need justification?

## 2. Normal incidence: familiar algebra, electromagnetic boundary conditions

### 2.1 The bulk equations allow more than one wave

Recall, in each medium,

\[
\frac{d^2E_x}{dz^2}+k_m^2E_x=0,
\qquad k_m^2=\omega^2\mu_m\epsilon_m.
\]

Write the allowed fields, with prescribed incident amplitude A:

\[
E_{1x}=Ae^{-jk_1z}+Be^{+jk_1z},\qquad
E_{2x}=Ce^{-jk_2z}.
\]

There is no wave incident from deep inside medium 2. This is information about the physical problem, not a consequence of the differential equation alone.

Recover the companion magnetic field from Faraday's law. Let students establish the reflected-wave sign:

\[
H_{1y}=\frac{Ae^{-jk_1z}-Be^{+jk_1z}}{\eta_1},\qquad
H_{2y}=\frac{Ce^{-jk_2z}}{\eta_2},
\qquad \eta_m=\sqrt{\frac{\mu_m}{\epsilon_m}}.
\]

### 2.2 Which fields must match, and why?

- Apply the integral curl equations to a small rectangular loop straddling the interface. Shrink its height and identify which integrals remain.
- Obtain tangential E continuity and the general magnetic-field jump n̂ × (H₂ − H₁) = K from the two small-loop arguments. With no free surface-current sheet, tangential H is continuous; the nonzero-K case will drive the conducting-sheet example. Assume finite fields on the two sides.
- Explain that the conditions apply to the **total** field on each side.
- Briefly locate the normal-component conditions from the two divergence laws. At normal incidence these fields have no normal components, so they add no independent amplitude equations here.

This is the main new derivation at normal incidence. It revisits circulation, orientation, limiting arguments and the relation between integral and differential statements.

### 2.3 Reuse the acoustic result

Recognize the familiar system, with r = B/A and t = C/A:

\[
1+r=t,\qquad \frac{1-r}{\eta_1}=\frac{t}{\eta_2}.
\]

Recall its solution rather than working through the same algebra again:

\[
r=\frac{\eta_2-\eta_1}{\eta_2+\eta_1},\qquad
t=\frac{2\eta_2}{\eta_2+\eta_1}.
\]

**Checks:** matched impedances; sign of r for air entering a higher-permittivity nonmagnetic dielectric; impossibility of satisfying both conditions with r = 0 unless the impedances match.

**Optional mathematical remark:** the second condition can also be written as continuity of (1/μ)dE_x/dz. The derivative itself need not be continuous when μ changes. This connects to earlier piecewise differential-equation problems.

## 3. Conducting reflection: field induces current, current generates field

Work out the link between a current source and its emitted electromagnetic waves, then let an incident wave drive that source. Keep the geometry one-dimensional so students can concentrate on curl, source conditions, superposition and the total field.

### 3.1 A prescribed sheet current radiates two outgoing waves

Put an infinite sheet at z = 0 in an otherwise uniform lossless medium with impedance η. Specify a harmonic surface current K = K₀ x̂, measured in A/m. There are no incoming waves in this first problem.

- Use symmetry and the outgoing-wave condition to propose E along x and outgoing plane waves on both sides.
- Obtain the corresponding H fields from the curl equation or the plane-wave cross product, keeping track of the opposite propagation directions.
- Apply the jump condition established with the small Ampère-Maxwell loop:

\[
\hat z\times(\vec H_2-\vec H_1)=\vec K.
\]

- Combine this with tangential E continuity. The emitted field is

\[
E_x^{\rm emitted}(z)=-\frac{\eta K_0}{2}e^{-jk|z|}.
\]

The PDE is homogeneous away from the sheet; the source enters through the magnetic-field jump. No delta functions or radiation integrals are required. Students should verify the wave equation on each side, calculate the curl to check H and then check the source condition. Tangential H is not continuous across this sheet.

### 3.2 An incident wave drives the current that generates its reflection

Add a normally incident wave with electric amplitude Eᵢ. Model a thin resistive sheet with real surface conductance G in siemens and the sheet law K₀ = G E_sheet. The driving field is the total tangential field at the sheet, including its emitted contribution:

\[
E_{\rm sheet}=E_i-\frac{\eta K_0}{2},\qquad
K_0=G E_{\rm sheet}.
\]

Solving this short self-consistency problem gives

\[
r=-\frac{\eta G}{2+\eta G},\qquad
t=\frac{2}{2+\eta G}.
\]

The backward emitted wave is the reflected wave. The forward emitted wave combines with the incident wave to give transmission. This makes the superposition tangible.

The cleanest stopping point is the perfectly conducting limit: r → −1, t → 0, K₀ → 2Eᵢ/η. A finite current remains while the total electric field at the surface tends to zero. Recover the same surface current from the tangential magnetic field.

Use finite G to distinguish reflected, transmitted and absorbed power in section 4. The perfectly conducting limit is the main physical endpoint; finding the absorption maximum is optional.

**Figure/interactive:** show the incident field, the two waves emitted by the sheet and their sum. In the perfect-conductor limit, the fields cancel on the transmitted side while the reflected wave remains on the incident side. Keep vector directions visible.

## 4. Reflected field is not reflected power

- Apply the already introduced phasor Poynting vector, 〈S〉 = ½ Re(E × H*), to the three travelling waves.
- Distinguish field coefficients r and t from power fractions:

\[
\mathcal R=|r|^2,\qquad
\mathcal T=\frac{\eta_1}{\eta_2}|t|^2,
\qquad \mathcal R+\mathcal T=1
\]

for real positive impedances. Interpret the reflected flux direction correctly.

- Give one compact, idealized air–ground example: μ₁ = μ₂ = μ₀ and ε₂ = 4ε₀ yield r = −1/3, t = 2/3, reflected power 1/9 and transmitted power 8/9. These are illustrative material values.
- Change ε₂ and ask students to predict the trend before calculating. Connect material response to a measurable echo.
- Brief connection to loss: the same amplitude matching uses complex η. For lossless medium 1 and absorbing medium 2, power entering at z = 0 is subsequently attenuated with depth. Do not reuse the real-impedance power formula unchanged for complex η.

- For the resistive sheet, compare incoming and outgoing fluxes with the mean sheet heating ½G|E_sheet|² per unit area. In the perfectly conducting limit the power is reflected, even though the surface current remains finite.

**Student prompt:** can a transmitted electric-field coefficient exceed one while conserving energy? What else controls the flux?

**Interactive idea, shared with section 2:** vary the impedance contrast; display the real instantaneous E and H fields, continuity at the boundary, and separate reflected/transmitted power fractions. Include incident-only and total-field views.

## 5. Oblique incidence: matching phase along the interface

### 5.1 Tilt the wave, keeping Cartesian coordinates

Use the xz plane as the plane of incidence; measure all angles from the normal. Write the three fields using exp(−j k·r). Recall that k is the wavenumber, an angular spatial frequency, while the vector k also specifies direction.

Return explicitly to the two-dimensional Helmholtz equation. For the TE electric component, write

\[
E_y(x,z)=U(z)e^{-jqx}.
\]

Students differentiate with respect to x and z to obtain

\[
U''+(k_m^2-q^2)U=0,\qquad
k_{zm}^2=k_m^2-q^2.
\]

This shows how the same bulk PDE constrains the tangential and normal spatial frequencies. It also prepares the later polarization calculation.

### 5.2 The boundary conditions hold everywhere along the boundary

At z = 0, the incident, reflected and transmitted phases must match for every x and time t. For this stationary planar interface, the waves share ω and the tangential wavenumber q:

\[
q=k_1\sin\theta_i=k_1\sin\theta_r=k_2\sin\theta_t.
\]

Recover the already familiar results:

\[
\theta_r=\theta_i,\qquad
\frac{\sin\theta_i}{v_1}=\frac{\sin\theta_t}{v_2}.
\]

Do not repeat the acoustic triangle construction. The new insight is that Snell's law is what allows the fields to satisfy the boundary conditions along an entire interface.

**Figure or interactive:** wavefronts crossing a boundary, with their matching spacing along it. A deliberately inconsistent transmitted angle makes the boundary mismatch visible.

**Student prompt:** why could fields match at one point on the boundary and still fail to be a solution?

## 6. Polarization now changes the answer

### 6.1 Two useful orientations

- Define TE/s: E perpendicular to the plane of incidence; TM/p: E in that plane.
- Draw E, H and k for both cases. Emphasize that both are transverse waves: the fields are perpendicular to their own propagation direction.
- A general incident polarization can be resolved into these two components. An isotropic planar interface treats them separately.

### 6.2 The same boundary conditions, different geometric projections

- Work through TE in detail, using H = (k × E)/(ωμ). Let students evaluate the cross product and identify the tangential component.
- Match the tangential fields and obtain

\[
r_{\rm TE}=\frac{\eta_2\cos\theta_i-\eta_1\cos\theta_t}
{\eta_2\cos\theta_i+\eta_1\cos\theta_t}.
\]

- Set up TM with a labelled vector diagram and give the resulting coefficient, leaving its algebra as a short guided exercise. Use a consistent electric-field basis so both coefficients recover the same normal-incidence sign.
- Compare reflected **power** curves for TE and TM. Identify their equality at normal incidence and their different angular behavior. Name the TM reflection minimum/Brewster angle when it appears; a separate derivation of its closed form is optional.
- For transmission, compare the normal component of the Poynting vector, not just the magnitude of the flux along each ray.

**Authoring note on TM notation:** define reflected electric-field directions before giving signed amplitudes. With amplitudes based on the common tangential electric direction,

\[
r_{\rm TM}=\frac{\eta_2\cos\theta_t-\eta_1\cos\theta_i}
{\eta_2\cos\theta_t+\eta_1\cos\theta_i}.
\]

For tangential-field transmission coefficients t∥ = 1 + r; the full TM electric amplitude additionally includes the ratio cos θᵢ/cos θₜ. This convention must be stated once to avoid sign or projection ambiguities.

**Interactive:** angle and permittivity controls, linked geometry and TE/TM reflected-power curves. Mark the current angle and retain the normal-incidence limit.

### 6.3 What this means for radar

Connect TE/TM to horizontal/vertical polarization for the chosen horizontal-interface geometry. Changing the transmit polarization can change the reflected signal from the same material.

A smooth plane produces specular reflection. Away from normal incidence, a monostatic radar return also depends on roughness and geometry; the Fresnel result is a building block for that interpretation, not a complete backscatter model. Keep this to a concise figure caption or paragraph.

## 7. A finite object sends a scattered field back to the radar

### 7.1 Apply the source picture without deriving a finite-object solution

Use a short, slender conducting wire in a plane incident wave. The object's dimensions are small compared with the wavelength. An electric field component along the wire drives an oscillating current and charge redistribution, which produces a scattered field. Present this as a short electric-dipole illustration; the finite-object current distribution and radiation formula are supplied by the model, not derived as required theory.

For illustration, describe the dipole response by p = α∥(Eᵢ · û)û, where û is the wire axis. The response coefficient sets the strength and phase; choosing it is part of the illustrative model. Do not present a prescribed-current animation as a solved quantitative scattering problem for an arbitrary metal object. The worked sheet problem has already established that the material responds to its total local field.

### 7.2 Show the emitted field and its link to polarization

A linked figure or animation should show:

- the incident plane wave and its electric-field direction;
- the finite wire, with oscillating current arrows and changing end charges;
- the scattered field with outgoing curved wavefronts and directional amplitude;
- a marked backscatter direction toward the radar, alongside the other observation directions;
- a view of the scattered field alone and, if useful, an overlay of incident plus scattered fields.

Use a normalized dipole radiation model for the scattered field away from the object. Its amplitude falls as 1/r; its directional intensity is proportional to sin²θ, where θ is measured from the wire axis, and the radiated electric field is transverse to the observation direction. Label the displayed quantity explicitly: an electric-field component, field magnitude or intensity. Avoid using equal-amplitude spherical rings to imply isotropic radiation.

Rotate the wire relative to the incident electric field. In the ideal longitudinal-dipole model, alignment gives strong excitation and an orthogonal wire gives none; a real finite-width conductor also has a weaker transverse response. This directly connects polarization to the current that can be driven and the resulting radar signal.

The displayed radiation field is a far-field illustration. Keep the immediate neighborhood of the object outside that approximation rather than extending its 1/r formula through the wire. No near-field derivation, vector-potential treatment, antenna impedance or radar-cross-section formalism is required.

### 7.3 Interpret the difference from a plane reflector

An infinite planar sheet produces plane outgoing waves; a finite object produces a directional scattered field. Some of that field can travel back to a radar. Call it the **scattered field**, and call the component returning to the radar **backscatter**. This carries the conductor-reflection intuition to finite targets without implying that every object behaves as a small flat mirror.

**Student prompts:** what changes when the wire rotates while the incident wave is fixed? Is the scattered field equally strong in every direction? How should field amplitude and power change with observation distance? Which of these predictions can be connected to material already covered?

## 8. Practice and consolidation

Distribute short tasks through the section, then finish with one guided problem:

1. Given candidate fields, verify the bulk equation, propagation directions and interface conditions; find a missing amplitude or sign.
2. For the current sheet, evaluate the curl on each side, check the magnetic-field jump and calculate the emitted amplitudes. Then impose K = G E_sheet and take the good-conductor limit.
3. For an oblique wave, obtain the transmitted vector wavenumber and check its tangential component and bulk dispersion relation.
4. Predict which polarization reflects more strongly at a specified angle using the coefficient curves; use the finite-wire illustration to explain how polarization can affect a radar echo.

Prioritize complete reasoning chains for interface matching and current-generated fields. Full TM coefficient elimination, a Brewster-angle derivation, total internal reflection and evanescent waves can remain optional. The finite-object illustration tests interpretation rather than a new radiation derivation. Finite-slab frequency response and general multilayer matrices are deferred.

## Proposed book organization

Follow the preceding sections with a short overview and linked pages:

- Overview: motivation and the short acoustic bridge.
- Normal incidence and electromagnetic boundary conditions.
- Conducting reflection through current-generated fields.
- Energy balance and the air–ground/conducting-sheet examples.
- Oblique incidence and phase matching.
- Polarization-dependent reflection.
- Finite-object scattering as a short visual application, either within the polarization page or on a compact final page.
- Practice, if a separate page is useful; otherwise place the questions with their topics.

The book TOC now contains the overview and six subsection pages listed below. The old interface/scattering and practice heading-only placeholders were replaced; the multilayer placeholder remains hidden. Energy balance is kept with the corresponding dielectric-interface and conducting-sheet calculations.

## Literature and links

- Existing TeachBook mechanical-wave sections linked above supply the acoustic coefficient calculation and geometric Snell result; refer students back to these instead of duplicating them.
- [Ellingson, Electromagnetics II, section 5.1](https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electromagnetics_II_(Ellingson)/05:_Wave_Reflection_and_Transmission/5.01:_Plane_Waves_at_Normal_Incidence_on_a_Planar_Boundary): reference for normal-incidence field matching and coefficients.
- [TU Delft, Interactive Optics, Reflection and Transmission at an Interface](https://interactivetextbooks.tudelft.nl/tn2421/content/Chap1_Basics/Basics_2022_01Clean.html#reflection-and-transmission-at-an-interface): reference for vector geometry, phase matching and the separate s/p calculations. Its stated emphasis on understanding the derivation rather than memorizing Fresnel formulas fits this course. The broader optics scope is not the required syllabus here.

- [Feynman Lectures II, section 20–1](https://www.feynmanlectures.caltech.edu/II_20.html#Ch20-S1): current sheets and outgoing waves.
- [MIT electromagnetism notes, sections 13.8 and 13.10](https://web.mit.edu/viz/EM/visualizations/notes/modules/emwaves.pdf): dipole radiation, sheet radiation and conductor reflection through induced currents.
- [Feynman Lectures II, section 21–4](https://www.feynmanlectures.caltech.edu/II_21.html#Ch21-S4): oscillating-dipole fields as background for the finite-object illustration.

The proposed reuse of acoustics, the radar thread, the balance of worked and guided derivations, and the finite-wire illustration are course-specific teaching choices.

## First draft files and visual proposals

- `05_00_interfaces.md`: overview and explicit acoustic/material-response links.
- `05_01_normal_incidence.md`: bulk solutions, small-loop boundary derivations, acoustic coefficient recall and Poynting balance. Proposed normal-incidence geometry, two shrinking loops, and a field-matching explorer.
- `05_02_conducting_reflection.md`: prescribed sheet current, outgoing fields, induced-current self-consistency, perfect-conductor limit and sheet heating. Proposed source-sheet drawing and an incident/emitted/total-field explorer.
- `05_03_oblique_incidence.md`: Cartesian Helmholtz reduction, phase matching and recovery of Snell's law. Proposed wavefront/phase-matching activity, including an inconsistent-angle mode.
- `05_04_polarization_at_interface.md`: TE worked derivation, TM setup and supplied result, full-amplitude conventions, normal flux and radar interpretation. Proposed vector diagrams and TE/TM angle curves.
- `05_05_finite_object_scattering.md`: short-wire current/charge response and qualitative radar application, with an optional supplied dipole field to interpret. Proposed normalized wire-rotation/scattered-field activity. No finite-object radiation derivation.
- `05_06_practice.md`: guided bulk/boundary checks, an optional active-sheet extension and an oblique-field problem, with dropdown result checks.

The normal-incidence interface geometry, shrinking Faraday loop and soil-moisture field-matching activity are implemented; other figures and widgets remain to be developed. Use embedded activities in the TeachBook; no companion notebooks. Prioritize the loop geometry, sheet-superposition animation and polarization diagrams before adding further visual material.

## Draft validation

The staged Jupyter Book build succeeds. The new pages have no reported Sphinx warnings; existing warnings concern earlier content and Git metadata in the staging copy. All 93 internal article links and equation-reference fragments in the new pages resolve. Independent vector boundary-system calculations check the TE/TM coefficients, normal Maxwell conditions and energy balance; additional checks cover conducting-sheet source/material conditions, absorbing-half-space power and the supplied dipole angular projection. Notebook execution and external tooltip lookups were disabled only in the validation copy. The normal-incidence geometry and shrinking Faraday loop have since been implemented; other proposed figures and widgets remain unimplemented.

## Interface geometry implemented 2026-11-22

`figures/interface_normal_incidence.svg` is embedded on the normal-incidence page: a flat xz view, electric vectors in the page, magnetic vectors represented with dot/cross symbols, and propagation arrows consistent with E × H. Its labelled groups and text remain editable in an SVG editor.

For the later oblique-incidence geometry, Paco supplied `/Users/paco/Documents/TEACHING/PPEO/Figures/W1_EM/PlaneBoundary.svg` as a possible source to copy and adapt. It has been inspected and left unchanged.

## Tangential electric-field loop implemented 2026-11-22

`figures/interface_tangential_e_loop.svg` is embedded beside the Faraday-law limit. Two flat xz panels show the total tangential electric fields, clockwise loop traversal, fixed tangential length ell and decreasing normal width h. The magnetic-field symbols stay unchanged while the shaded area shrinks; the caption states the finite-field flux bound. The Ampère–Maxwell loop remains a separate proposed figure.

## Moisture-driven field-matching activity implemented 2026-11-22

`interactives/interface_fields.html` and its embedded form are generated by `scripts/build_interface_interactive.py`. The main control is volumetric water content, bounded by fixed porosity 0.45. A three-phase square-root permittivity mixing model uses mineral 5, water 80 and air 1. The nonmagnetic, lossless example at 300 MHz isolates material-dependent normal-incidence reflection. These are illustrative choices, distinct from the earlier penetration presets.

The linked electric and magnetic plots show the total air field and transmitted soil field, with optional incident/reflected components and fixed amplitude scales. Controls include carrier phase and play/pause. Power fractions satisfy conservation. Before-rain, after-rain and drying presets plus a day slider illustrate slower temporal variation: a supplied wetting ramp and exponential drying sequence. This is a sequence of steady harmonic states, not a transient rainfall simulation or a prediction of off-nadir radar backscatter.

Validation uses offline JavaScript control tests, independent mixture/impedance calculations and direct time averaging at 30 material/position combinations. The canvas draw commands were rendered to PNG for inspection. This does not constitute a live-browser layout test.

## Current-sheet figures implemented 2026-11-22

`figures/current_sheet_emission.svg` shows the prescribed positive x-directed current, equal negative x electric amplitudes on both sides, opposite magnetic directions and outward propagation. `figures/current_sheet_driven.svg` shows incident illumination and the total local electric field driving the current, with a separate vector-addition panel for incident plus emitted fields. Both use the established flat xz view, editable SVG labels and dot/cross magnetic symbols. They are embedded beside the corresponding source and self-consistency arguments. The sheet-superposition animation is now included in the conductor activity described below.

## Conductor activity and separation-of-variables reminder implemented 2026-11-22

`interactives/conductor_reflection.html` and its embedded form are generated by `scripts/build_conductor_interactive.py`. Thin-sheet mode varies real Gs; conducting-half-space mode varies bulk conductivity and calculates exact complex k and surface impedance at 100 MHz, with vacuum background permittivity and permeability. Both hold incident peak E at 1 V/m. Fixed-scale plots show the surface field approaching zero and the depth-integrated current approaching 2Ei/eta0, together with spatial fields and optional incident/current-generated contributions.

The power explanation is initially hidden. Students first account for missing power, then reveal sheet absorption curves or the half-space depth plot of decreasing flux and accumulated Joule heating. Questions distinguish the surface field from the exterior standing wave, the finite integrated current from the local volume density, and transmission through a thin sheet from absorption in a thick conductor. The half-space current is calculated as the integral of sigma E through depth; it is not imposed as a literal finite-conductivity surface-current jump.

Validation includes 45 independent Python complex-root/interface cases, matching conditions, total flux and integrated Joule-heating checks, source-field superposition, controls, limiting cases, phase invariance, animation/visibility pause and reset. Canvas draw commands were rendered for inspection; live browser layout was not tested.

The oblique-incidence page now explicitly identifies separation of variables, links to its earlier heat-equation use, and explains the product X(x)U(z), separation constant and choice of the tangential exponential. Existing surrounding text is retained.


## Phase-matching activity implemented 2026-11-22

`interactives/phase_matching.html` and its embedded form are generated by `scripts/build_phase_matching_interactive.py`. Equal-scale wavefronts and boundary-phase traces compare the matched transmitted angle with a deliberately incorrect trial angle. All trial vectors retain the correct bulk wavenumber magnitude; only matching tangential components satisfies the boundary along its full extent. Material, incidence angle, trial angle, phase and reflected fronts are controlled. Questions distinguish bulk and boundary checks, pointwise and whole-interface matching, normal incidence and polarization independence. Offline JavaScript checks cover angles, dispersion, phase agreement, clipping geometry and controls; canvas commands were rendered for inspection. Live browser layout was not tested.

## Polarization terminology and classroom selection

The authored section and practice use radar horizontal (H) and vertical (V) polarization, acknowledging TE/s and TM/p once. The earlier planning terminology above maps to H and V respectively for the stated geometry.

The [final two-lecture proposal](EMwaves_final_two_lectures_plan.md) selects a smaller classroom core from this book section: attenuation, normal-incidence matching and current-generated reflection, with phase matching and H/V as a flexible ending. Full oblique algebra and finite-object radiation remain optional reading.
