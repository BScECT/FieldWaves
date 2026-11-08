# Electromagnetic waves — proposed table of contents, iteration 1

Date: 2026-11-01  
Status: overall TOC proposal for discussion; the historical section and plane-wave section have first drafts; the other sections are heading-only placeholders (updated 2026-11-08).  
Branch: `EMwaves`  
Placement: after Mechanical waves, before Miscellaneous.  
Book directory: `book/5_electromagnetic_waves/`

## Purpose and level

Support the nine upcoming sessions in their proposed order. The historical section now has a first book-section draft, with separate teaching notes in `planning/EMwaves_history_lecture_notes.md`. The plane-wave section now has a first draft, embedded interactive explorations and review notes in `planning/EMwaves_plane_waves_review.md`. The chapter introduction and remaining seven section pages contain titles only. This document records the proposed overall scope for continued discussion.

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
- Introduce the telegrapher’s equations through voltage/current on a transmission line; map their mathematical structure to the EM field equations. Start lossless and return to loss terms in section 5.

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

## 5. Lossless and lossy media

File: `media_and_losses.md` — session 5

- Physical roles of permittivity, permeability and conductivity; specify the simple material assumptions used throughout.
- Distinguish phase change from amplitude decay; introduce attenuation, phase constant and complex impedance through a travelling harmonic wave.
- Connect conduction and displacement currents to the earlier EM-diffusion chapter; distinguish wave-like and diffusion-dominated regimes.
- Interpret penetration/skin depth and energy dissipation with simple examples.
- Return to the telegrapher’s equation with loss terms; separate attenuation from dispersion.

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

- Retain the mechanical-wave Fourier transform convention (forward transform with `exp(-iωt)`, reconstruction with `exp(+iωt)`) and consistent forward propagation phases.
- Define symbols and units locally; show which geometry and material assumptions make each reduced equation valid.
- Separate essential reasoning from optional derivations; keep practice close to the preceding material.
- Revise this proposal and the heading-only scaffold together once the scope is agreed.
