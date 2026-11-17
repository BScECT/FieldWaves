# Electromagnetic waves — proposed table of contents, iteration 1

Date: 2026-11-01  
Status: planning document for discussion; history, plane waves and energy/polarization have drafts. Media section has its first draft and embedded explorers (2026-11-15). Older session outlines below retain the initial proposal.  
Branch: `EMwaves`  
Placement: after Mechanical waves, before Miscellaneous.  
Book directory: `book/5_electromagnetic_waves/`

## Purpose and level

Support the original nine-session sequence. The historical and plane-wave sections have drafts and supporting material; the 3D-wave, energy and polarization section now also has a draft and embedded activities. The media section has a first draft, with the detailed outline in `planning/EMwaves_media_section_plan.md`; practice, interfaces and layers remain to be developed. This document records the overall scope for continued discussion.

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

## 7. Plane waves at an interface: scattering matrix

File: `interface_scattering.md` — session 7

- Begin with normal incidence between two lossless media and the mechanical-wave impedance analogy.
- Use tangential-field boundary conditions to derive reflected and transmitted electric-field amplitudes.
- Distinguish field-amplitude coefficients from power fractions; check energy conservation in the lossless case.
- Define incoming/outgoing amplitudes, reference directions and reference planes; organize the interface equations in a 2 × 2 scattering matrix.
- Optional extension: oblique incidence, Snell’s law and separate TE/TM polarizations after the normal-incidence foundation is secure.

## 8. Frequency response of layered media

File: `multilayer_frequency_response.md` — session 8

- Combine propagation through a finite layer with reflection and transmission at its boundaries.
- Explain multiple reflections and interference using travel times and phase before introducing matrix composition.
- Build from one slab to several layers; distinguish cascading scattering relations from ordinary multiplication of interface scattering matrices.
- Interpret reflected/transmitted amplitude and phase versus frequency, resonances and the effects of thickness, impedance contrast and loss.
- Connect a frequency response to a pulse response using the book’s existing Fourier convention.

## 9. Practice: interfaces and layered media

File: `practice_3.md` — session 9

- Calculate simple interface responses and interpret a slab’s frequency response.
- Predict how layer thickness, contrast and loss change interference features.
- Check limiting cases: matched media, vanishing layer thickness and lossless energy balance.
- Finish with an integrated interpretation task linking a measured response to a plausible layered model; detailed tasks remain to be agreed.

## Choices to review before drafting content

- **Difficulty:** is the mechanical-wave chapter an appropriate baseline? Use student evidence and the first practice session to calibrate the pace.
- **Interfaces:** proposed core is normal incidence; should oblique incidence and TE/TM become required?
- **Telegrapher’s equation:** proposed as a compact mathematical bridge, not a separate transmission-line course. How much circuit background is available?
- **3D waves:** proposed core includes arbitrary plane-wave direction and simple spreading, with full spherical-wave solutions optional.
- **Layering:** prioritize physical interpretation and a guided computational example; decide how much matrix algebra students must perform themselves.

## Authoring conventions for the next iteration

- Retain the mechanical-wave Fourier transform convention (forward transform with a negative exponential, reconstruction with a positive exponential; use `j` for EM, hence `exp(+jωt)` and forward propagation `exp(-jkz)`) and consistent forward propagation phases.
- Define symbols and units locally; show which geometry and material assumptions make each reduced equation valid.
- Separate essential reasoning from optional derivations; keep practice close to the preceding material.
- Revise this proposal and the heading-only scaffold together once the scope is agreed.
