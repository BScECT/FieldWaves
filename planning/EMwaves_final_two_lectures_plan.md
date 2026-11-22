# Final two electromagnetic-wave lectures: attenuation and reflection

Date: 2026-11-22  
Status: proposal for discussion; no new slide decks generated.  
Format: two lectures, each with two 45-minute blocks, following the earlier lecture format.

## Recommended route

**Lecture 1: why a wave fades, and what survives a radar round trip.**  
**Lecture 2: why a boundary produces a return field, and how currents generate reflection.**

Treat the TeachBook as a resource with optional depth. The classroom route should give students time to complete a few reasoning chains, explain them and check their results. Finish with normal-incidence reflection and the conducting-current story as the protected core. Oblique phase matching and H/V dependence form a short, flexible ending if the class is ready.

Starting point: material response and complex permittivity have been introduced, but the calculation showing how complex permittivity produces attenuation has not been worked through. Do not repeat the relaxation-model derivation.

The mathematical thread is **read an equation → use the geometry → propose a solution → differentiate and check → apply physical boundary conditions → interpret a measured quantity**. Revisit full vector expressions selectively, then let the students perform the reductions. Use j and the established exp(+jωt) convention throughout.

## What students should leave able to do

- Read E₀ exp[−(α+jβ)z] as attenuation plus spatial phase; check it against the one-dimensional Helmholtz equation and select the physically appropriate solution.
- Relate field amplitude to mean power with phasors, including the conjugate, and distinguish one-way from round-trip loss.
- Check whether candidate fields satisfy both the bulk equation and normal-incidence boundary conditions. Obtain the companion H field, recognize the acoustic matching system, and check the power fractions.
- Explain how an incident field drives a current and the current generates the reflected field. Explain a vanishing surface electric field with a finite integrated current, and account for energy absorbed in a finite-conductivity conductor.

If time permits, also recover the already familiar Snell relation from phase matching and explain qualitatively why H and V reflection differ. Full oblique Fresnel derivations are not part of this proposed classroom core.

## Lecture 1: a fading wave and a radar echo

### First 45 minutes: turn complex permittivity into a wave we can read

| Minutes | Work | Purpose |
| --- | --- | --- |
| 0–7 | Recall what ε′ and ε″ describe. Ask students to identify time frequency, spatial frequency and amplitude in a supplied harmonic field. | Retrieve material response and the phasor language without repeating the relaxation model. |
| 7–20 | **Board:** start from the homogeneous Helmholtz equation. Write the Cartesian Laplacian and reduce it for E = x̂ Eₓ(z). Try E₀ exp(−jkz), differentiate twice and substitute. Then write k = β−jα and expand the exponential. | One complete PDE-to-ODE-to-solution chain, with the geometry doing the simplification. Recall the earlier curl-curl derivation rather than repeating it. |
| 20–33 | **Students, then discussion:** expand (β−jα)², compare real and imaginary parts with ω²μ(ε′−jε″), and determine the sign of α for a forward passive wave. Check a supplied numerical root rather than calculating a complex square root from scratch. | Practise complex algebra as a description of phase and loss. Explain why the bulk ODE alone also permits another solution. |
| 33–45 | Use the existing media-wave activity to distinguish wavelength, envelope and moving phase. **Board/class:** recover H from the surviving Cartesian curl component. | Reinforce β as the phase wavenumber and α as an inverse attenuation length; E and H remain coupled. |

Core equations:

\[
\frac{d^2E_x}{dz^2}+k^2E_x=0,\qquad k^2=\omega^2\mu\epsilon,
\]

\[
k=\beta-j\alpha,\qquad E_x=E_0e^{-\alpha z}e^{-j\beta z},
\]

\[
\beta^2-\alpha^2=\omega^2\mu\epsilon',\qquad
2\alpha\beta=\omega^2\mu\epsilon'',\qquad
H_y=\frac{k}{\omega\mu}E_x.
\]

A manageable check uses εᵣ = 3.99−0.40j and a proposed k/k₀ = 2−0.10j. Students square the proposed root, identify α and β, and explain the sign of the spatial envelope. At 100 MHz, k₀ ≈ 2.10 rad/m. Supply this value so the task stays focused on meaning and algebra.

TeachBook support: [lossy dielectrics](../book/5_electromagnetic_waves/04_02_lossy_dielectrics.md), with the phasor and plane-wave sections available for review.

### Second 45 minutes: follow the energy back to the receiver

| Minutes | Work | Purpose |
| --- | --- | --- |
| 0–12 | **Board with student contributions:** factor the spatial dependence out of ½ Re(E × H*). Show why the mean flux has exp(−2αz), while the field envelope has exp(−αz). Interpret the decreasing flux as energy deposited in the material. | Reuse cross products, conjugation and energy conservation. No new derivation of the full Poynting theorem. |
| 12–25 | **Paired radar/GPR problem:** calculate field and power factors after one attenuation depth, then after the down-and-back path to the same reflector. Discuss what has been held fixed in this comparison. | Distinguish field, power and two-way propagation. Keep this as one coherent example. |
| 25–35 | Add conduction through ε_eff = ε_d−jσ/ω. Give the good-conductor skin-depth limit and ask students to predict its change when frequency or conductivity is multiplied by four. | Connect the new result to earlier EM diffusion. Keep the derivation and material-spectrum detail optional. |
| 35–40 | One application contrast: dry versus wetter ground. Separate loss during propagation from the still-unanswered question of reflection at entry. | Give the next lecture a clear purpose. Avoid a tour of several soil/water models. |
| 40–45 | **Exit questions:** choose the decaying solution; distinguish field and power attenuation; explain why a return path compounds loss. | Check confidence before moving to interfaces. |

Core energy results:

\[
\langle\vec S\rangle=\tfrac12\operatorname{Re}\{\vec E\times\vec H^*\},\qquad
\langle S_z(z)\rangle=\langle S_z(0)\rangle e^{-2\alpha z},
\]

\[
\frac{|E_{\rm echo}|}{|E_{\rm echo,no\ loss}|}=e^{-2\alpha d},\qquad
\frac{P_{\rm echo}}{P_{\rm echo,no\ loss}}=e^{-4\alpha d}.
\]

Skin depth is a short application of the conductive limit, not a second wave-propagation course. If the first block takes longer, this ten-minute segment is the first material to compress. Retain the distinction between dielectric loss and conduction: attenuation does not require σ ≠ 0.

Use the existing [media-wave activity](../book/5_electromagnetic_waves/interactives/media_wave.html) and the [round-trip figure/text](../book/5_electromagnetic_waves/04_04_radar_penetration.md). One activity explored carefully is enough here.

## Lecture 2: boundaries, currents and the return field

### First 45 minutes: match fields at normal incidence

| Minutes | Work | Purpose |
| --- | --- | --- |
| 0–5 | Retrieve the acoustic reflection problem. Ask which quantities must be replaced by E, H and η. | Reuse known algebra; avoid a fresh derivation of the same coefficient formulas. |
| 5–18 | **Board:** use the shrinking Faraday loop to obtain tangential E continuity. Use an Ampère–Maxwell loop to obtain the tangential H condition, including a possible sheet current. Spend a short moment on J = Kδ(z), linking Signals and Time Series and EM diffusion. | Practise circulation, normals, finite integrals and the role of source conditions. The loop area vanishes, while a delta-sheet current can survive integration. |
| 18–28 | **Students:** two proposed forward waves solve their own bulk equations and match E, but fail H. Find the companion fields, diagnose the failure and repair the solution with a reflected wave. | A complete solution check, using vector calculus and boundary conditions. |
| 28–35 | Recall r and t from the acoustic matching system. Convert them into power fractions and check conservation for one material pair. | Distinguish signed field amplitudes from positive power fractions. |
| 35–42 | Use the moisture-driven field-matching activity. Predict the change after rain, then inspect E/H continuity and reflected power. | Link material response to temporal echo variation at a fixed boundary. |
| 42–45 | Debrief: which part came from the PDE, which from the boundary conditions, and which from energy accounting? | Consolidate the method rather than add another formula. |

Use ε₂ = 4ε₀ and μ₁ = μ₂ = μ₀ for the worked check. The corrected solution has r = −1/3 and t = 2/3; the power fractions are 1/9 and 8/9. These simple numbers leave room to interpret the field directions and signs.

Core results:

\[
E_{1t}=E_{2t},\qquad \hat n\times(\vec H_2-\vec H_1)=\vec K,
\]

\[
r=\frac{\eta_2-\eta_1}{\eta_2+\eta_1},\qquad
\mathcal R=|r|^2,\qquad \mathcal T=\frac{\eta_1}{\eta_2}|t|^2.
\]

Support: [normal incidence](../book/5_electromagnetic_waves/05_01_normal_incidence.md) and the [moisture activity](../book/5_electromagnetic_waves/interactives/interface_fields.html).

### Second 45 minutes: the current generates the reflected field

| Minutes | Work | Purpose |
| --- | --- | --- |
| 0–15 | **Board:** an imposed current sheet emits to both sides. Recover the companion H signs, apply the jump condition and obtain E_emitted = −ηK/2. Then let the total field drive the current: E_sheet = E_i + E_emitted and K = G_s E_sheet. | One new electromagnetic calculation, built from the boundary condition just established. Keep the factor of two and the field directions visible. |
| 15–27 | **Predict in pairs, then use the conductor activity:** make the sheet increasingly conducting. Explain the finite current as the surface field tends to zero. Switch briefly to the thick conductor and ask where the unreflected power goes before revealing the depth/heat plot. | Connect surface response, skin depth and energy conservation. Do not derive the full finite-conductivity half-space current integral or surface-impedance formula in class. |
| 27–40 | **Flexible slot:** if the core is secure, use phase matching to recover Snell's law in about eight minutes, followed by one H/V reflection comparison in about five. Otherwise spend the slot on supported normal-incidence/current practice and questions. | Preserve confidence and completion of the core. The flexible material can be read in the book. |
| 40–45 | **Exit questions:** does E_surface → 0 force K → 0? Does a valid bulk wave automatically satisfy the boundary? Where can non-reflected power go? | A final check on the physical and mathematical story. |

The core current chain is

\[
E_{\rm emitted}=-\frac{\eta K}{2},\qquad
E_{\rm sheet}=E_i+E_{\rm emitted},\qquad
K=G_sE_{\rm sheet},
\]

\[
E_{\rm sheet}\longrightarrow0,\qquad
K\longrightarrow\frac{2E_i}{\eta}
\quad\text{as the sheet becomes perfectly conducting}.
\]

Make clear that the surface electric field tends to zero; the exterior standing-wave field need not vanish everywhere. For the thick conductor, current is integrated through the skin layer and the entered power is deposited as heat. This is an interpretation of the preceding theory, not another long derivation.

Support: [conducting reflection and questions](../book/5_electromagnetic_waves/05_02_conducting_reflection.md) and the [conductor activity](../book/5_electromagnetic_waves/interactives/conductor_reflection.html).

### What to do in the flexible ending

For Snell's law, use the [phase-matching activity](../book/5_electromagnetic_waves/interactives/phase_matching.html): compare a matched transmitted angle with θ_t = θ_i for different materials. Keep the origin matched, then show the mismatch elsewhere along the interface. Read the shared tangential wavenumber from

\[
k_1\sin\theta_i=k_2\sin\theta_t.
\]

This is a new explanation of a result already known from acoustics. Refer to separation of variables if helpful; the full X(x)U(z) derivation and ODE refresher can remain supporting reading. Do not make the class repeat the whole calculation to reach an already familiar angle law.

For H/V, use one vector sketch and one supplied reflected-power plot. Explain that field orientation changes the tangential projections and therefore the reflected amplitude. Use radar H/V labels, acknowledging TE/s and TM/p once. Both polarizations obey the same phase-matching law in the isotropic media used here. No memorization or full derivation of the two Fresnel coefficient sets is required in this proposal.

The finite-wire example can supply a closing picture if there is spare time; its dipole formula is not part of the lecture route.

## Explicit omissions from the lecture route

- Re-deriving the material relaxation model.
- General closed forms for α and β, or a complex-square-root exercise from scratch.
- Full Poynting-theorem derivation and a second derivation of the diffusion equation.
- Detailed frequency-dependent soil/water models or a soil-moisture retrieval algorithm.
- Full H/V Fresnel algebra, Brewster-angle derivation, total internal reflection and evanescent-wave development.
- Finite-object radiation derivation, current-distribution integrals or radar-cross-section formalism.
- Finite slabs, multilayer frequency responses and matrix methods.

These topics can remain in the TeachBook as optional depth. Their presence does not make them required classroom content.

## Pacing and assessment safeguards

Protect the paired tasks and exit questions. If the class needs more time, remove optional coverage rather than the opportunity to finish a solution. In lecture 1, compress skin-depth/material comparison first. In lecture 2, use the entire flexible slot for practice before cutting the boundary/current reasoning.

Suggested assessed core: verify a supplied exponential solution; read α, β and units; distinguish field/power and one-way/round-trip loss; retrieve H from a simple Cartesian curl; check and repair a normal-incidence boundary solution; interpret the finite-current limit and the energy budget. Supply coefficients or short relations where recalling them is not the learning objective.

Use roughly 12–15 substantive frames per lecture, including prompts and board stops. Keep figures large and the board calculations legible. The book supplies worked detail; the slides should leave space for students to construct the argument with the teacher.
