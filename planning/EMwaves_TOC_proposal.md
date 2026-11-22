# Electromagnetic waves — proposed table of contents, iteration 1

Date: 2026-11-01  
Status: planning document for discussion; history, plane waves and energy/polarization have drafts. Media section has its first draft and embedded explorers (2026-11-15). The interface section has a first draft (2026-11-21); several figures and embedded activities are now implemented, with further visual proposals still to develop. Earlier session outlines retain the initial schedule where indicated.  
Branch: `EMwaves`  
Placement: after Mechanical waves, before Miscellaneous.  
Book directory: `book/5_electromagnetic_waves/`

## Purpose and level

Support the original nine-session sequence. The historical and plane-wave sections have drafts and supporting material; the 3D-wave, energy and polarization section now also has a draft and embedded activities. The media section has a first draft, with the detailed outline in `planning/EMwaves_media_section_plan.md`; the interface section now has a first draft, with practice questions and proposed visuals. General multilayer development is deferred. This document records the overall scope for continued discussion.

Use familiar mechanical-wave ideas as the starting point: travelling disturbances, wave speed, phase, impedance, reflection and transmission. Introduce each new EM idea through a physical picture, a simple geometry and then equations. Keep core derivations in Cartesian coordinates with one direction of spatial variation. Put longer vector derivations and additional generality in optional material if needed.

The existing book already introduces electrostatics and magnetostatics, charge continuity and the displacement-current preview (`2_potential_fields/magnetic_field/currents_and_waves.md`), followed by EM diffusion (`3_diffusion_fields/em_diffusion.md`). Revisit these selectively rather than assuming students can immediately use the full formalism. Mechanical waves already covers Fourier conventions, acoustic impedance and interface coefficients; these provide the main mathematical bridge. Its suitability for the students remains to be checked, not assumed.

## Proposed chapter introduction

File: `intro.md`

- Where EM waves fit after static fields, diffusive fields and mechanical waves.
- Short prerequisite recap: wave speed, wavelength, frequency, phase and impedance; meaning of divergence and curl in pictures.
- Road map and a compact notation guide; distinguish electric field, magnetic flux density and magnetic field strength.

## 1. From electrostatics to Maxwell’s equations

File: `history_maxwell.md` — session 1

- A selective experimental story: Coulomb and electric sources; Ørsted/Ampère and currents; Faraday and induction; Maxwell’s synthesis and Hertz’s wave experiments.
- Revisit the charging capacitor and charge conservation to motivate displacement current.
- Read the four Maxwell equations physically; connect integral statements to local statements without making a full vector-calculus derivation a prerequisite.
- Changing electric and magnetic fields permit propagation through a source-free region; preview the predicted wave speed and the connection to light.

## 2. Plane waves in one spatial dimension

File: `plane_waves_1d.md` — session 2

Detailed sequence proposed on 2026-11-08: [Plane-wave section plan](EMwaves_plane_waves_section_plan.md), including arbitrary waveforms, transverse fields, finite travel time, H notation, phasors and the lossless telegrapher's equations.

- A plane wave varies along one coordinate while its electric and magnetic fields point in transverse directions in 3D space.
- Reduce Maxwell’s curl equations to two coupled scalar equations for a homogeneous, linear, isotropic, source-free, lossless medium.
- Derive the scalar wave equation; reuse forward/backward travelling solutions and harmonic waves from mechanical waves.
- Compare pressure/particle velocity with electric/magnetic fields: coupled equations, propagation speed, impedance and direction-dependent signs.
- Introduce the telegrapher’s equations through voltage/current on a transmission line; map their mathematical structure to the EM field equations. Keep the lossless bridge compact; the revised media plan does not require a second transmission-line derivation.

## 3. Practice: Maxwell’s equations and plane waves

File: `practice_1.md` — session 3

- Interpret field directions and identify propagation direction.
- Calculate speed, wavelength, phase delay and the companion magnetic or electric field.
- Compare mechanical, field and transmission-line descriptions using the same travelling-wave reasoning.
- Diagnose common mistakes: transverse direction versus variation direction, sign conventions and field units.

## 4. Waves in three dimensions, energy and polarization

File: `waves_3d_energy_polarization.md` — session 4

- Extend plane-wave propagation to an arbitrary direction using the wave vector and phase surfaces.
- Distinguish a plane wave in 3D space from a spreading wave from a localized source; introduce spherical spreading qualitatively and through inverse-square intensity.
- Introduce the Poynting vector as energy flux, its direction, units and time average for harmonic waves.
- Explore linear, circular and elliptical polarization through the electric-field tip at a fixed location.
- Optional: a fuller energy-conservation derivation and polarization handedness conventions.

## 5. Propagation through lossless and lossy media

Current overview: `book/5_electromagnetic_waves/04_00_media_and_losses.md` — session 5 in the original schedule.

Revised TeachBook proposal, 2026-11-15: [Detailed structure, story and equations](EMwaves_media_section_plan.md). A first draft now follows this outline, with four linked subsection pages, three figures and two embedded explorers.

- Thread: a radar wave enters the ground. Material response changes phase, amplitude and energy flux, and these changes carry information about the material.
- Give ε and μ physical meaning through bound polarization, dipoles and magnetic response. Connect to the capacitor and soil's solid/air/water mixture; distinguish material polarization from wave polarization.
- Recover lossless speed, wavelength and impedance before adding loss. Large ε alone does not imply attenuation.
- Introduce delayed dielectric polarization and ε_d=ε′−jε″_d before conductivity. A short relaxation model connects a real response law to complex ε. Explicitly demonstrate loss and attenuation with σ=0.
- Verify the dielectric wave with k=β−jα; recover H from curl and mean Poynting flux from the conjugated cross product. Use its divergence to identify dielectric heating. Distinguish field and power attenuation depths.
- Then add mobile-charge conduction as a second mechanism: ε_eff=ε_d−jσ/ω. Include each loss once and use the same propagation equations.
- Retrieve diffusion and skin depth as the conduction-dominated limit. State the frequency-dependent assumptions; the conductor square-root scaling is not universal.
- Apply the full model to soils, freshwater/seawater and changing frequency. Include down-and-back echo attenuation without identifying it with a complete depth-of-investigation model.
- Optional plasma exercise: sign of k², propagation versus evanescence, and decay without absorption. Keep magnetized-plasma/Faraday-rotation and group-delay developments outside the core.
- Bridge to interfaces and layers through η and exp[−jk(ω)d]. Replace the original return to lossy telegrapher algebra with Earth-material interpretation and energy checks.

## 6. Practice and formative assessment

File: `practice_2_assessment.md` — session 6

- Consolidate propagation direction, energy flux, polarization and attenuation.
- Interpret plots and compare lossless, weakly lossy and conductive examples.
- Use short conceptual and numerical questions to reveal whether students can connect physical pictures, equations and units.
- Use the results to decide what needs revisiting before interfaces; assessment tasks and feedback remain to be designed.

## 7. Plane waves at an interface: reflection and transmission

Overview: `book/5_electromagnetic_waves/05_00_interfaces.md`. Detailed plan: [Interface section plan](EMwaves_interface_section_plan.md). First draft added 2026-11-21.

- Explicitly reuse the acoustic reflection-coefficient algebra and previously derived Snell's law; do not repeat their original derivations.
- Derive electromagnetic boundary conditions from Maxwell's integral equations. Check bulk solutions, companion magnetic fields and power balance at normal incidence.
- Work out conducting reflection through the thread **field drives current → current generates field**: prescribed current sheet, outgoing waves, total-field Ohm's law, reflection/transmission, perfect-conductor limit and sheet heating.
- For oblique waves, reduce the Cartesian Helmholtz PDE with a tangential phase factor and recover Snell's law through phase matching along the whole interface.
- Derive horizontal-polarization (H) matching, supply and exercise the vertical-polarization (V) counterpart, and interpret polarization-dependent reflected power. Define full electric amplitudes and vector basis directions consistently.
- Apply the source picture to a short conducting wire using a supplied dipole illustration. Introduce scattered field/backscatter and link current excitation, spreading and receiver projection. A finite-object radiation derivation is outside the core.
- Normal-incidence/current-sheet figures and embedded soil-moisture, conductor and phase-matching activities are implemented. Further visual proposals remain to develop together.

## 8. General layered media deferred

The remaining teaching time is allocated to unfinished attenuation reasoning and the interface/current-scattering material above. Finite-slab frequency response, general multilayer systems and scattering matrices are deferred. They are not required to complete the current story.

## 9. Practice: interfaces and current-generated fields

Draft: `book/5_electromagnetic_waves/05_06_practice.md`, together with questions throughout the section.

- Verify the bulk equation and interface conditions independently; repair a missing reflected wave.
- Compute companion magnetic fields and interpret their signs and units.
- Check a current-sheet source condition and use the total-field material law. An externally driven sheet is an optional extension.
- Use phase matching and Cartesian curls for an oblique field; compare H/V powers and check limits.
- Interpret the finite-wire illustration through projections, current excitation and spreading, without requiring a new radiation derivation.

## Choices to review before drafting content

- **Difficulty:** is the mechanical-wave chapter an appropriate baseline? Use student evidence and the first practice session to calibrate the pace.
- **Interfaces:** protect normal-incidence and current-generated reflection in class. Oblique phase matching and H/V dependence are a flexible ending; the full algebra remains supporting book material.
- **Telegrapher’s equation:** proposed as a compact mathematical bridge, not a separate transmission-line course. How much circuit background is available?
- **3D waves:** proposed core includes arbitrary plane-wave direction and simple spreading, with full spherical-wave solutions optional.
- **Current-generated fields:** the conducting-sheet calculation is the worked extension. Finite-object scattering remains a supplied visual model; multilayers are deferred.

## Authoring conventions for the next iteration

- Retain the mechanical-wave Fourier transform convention (forward transform with a negative exponential, reconstruction with a positive exponential; use `j` for EM, hence `exp(+jωt)` and forward propagation `exp(-jkz)`) and consistent forward propagation phases.
- Define symbols and units locally; show which geometry and material assumptions make each reduced equation valid.
- Separate essential reasoning from optional derivations; keep practice close to the preceding material.
- Keep this proposal, the detailed section plans and the book navigation consistent as drafts are revised.

## Proposed route for the final two lectures

See [Final two lectures: attenuation and reflection](EMwaves_final_two_lectures_plan.md). This classroom selection protects attenuation, normal-incidence matching and current-generated reflection. Snell/H/V form a flexible ending; the book retains optional depth.
