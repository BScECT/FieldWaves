# W2.3L2: tilted waves, polarization and the currents behind reflection

Date: 2026-11-24  
Status: revised lecture proposal; no new slides or activities generated.  
Format: two 45-minute blocks, with the break outside these 90 minutes.  
Starting point: Paco covered all 24 numbered slides of W2.3L1, with good timing.

This supersedes the 23 November ordering and the second-lecture route in [the earlier two-lecture plan](EMwaves_final_two_lectures_plan.md). Normal incidence, attenuation, tangential boundary conditions, reflection/transmission coefficients, power conservation and the soil-moisture activity are covered. Start by tilting the already familiar waves. Introduce the current source after the geometry and polarization are established.

## Main story and difficulty

**Tilt the wave, match the phase, project the fields. Then ask what current generates that reflected wave.**

The first block retains the Cartesian PDE/separation calculation, phase matching and H/V reflection. The second uses a phased current sheet to emit oblique H-polarized waves, then lets an incident wave drive the current required by a perfect conductor. The same tangential phase and magnetic-field projection appear in both blocks.

This is a manageable extension if the current-sheet calculation uses **H polarization only**. Put the sheet at z=0, direct the current along y and vary its phase along x. Its surface divergence is then zero, so no additional surface-charge calculation is needed. Keeping the old x-directed current while introducing x-dependent phase would bring in charge accumulation and V-polarized fields; leave that case aside.

The source emits two outgoing waves with the same tangential wavenumber and opposite normal components. They are mirror-related across the sheet; their full propagation vectors are not opposites when the tangential component is nonzero.

Keep j, exp(+jωt), peak-amplitude phasors and the book's H/V labels. The user's proposed exp(+jkx x) factor is valid; with this time convention and positive kx it selects propagation towards negative x. Use exp(−jk_parallel x) in the main calculation to follow the positive-x convention from the first block. Reversing its sign reverses the tangential propagation direction, without changing the cosine amplitude factors.

Use two lossless isotropic media for the first block. For the prescribed-source calculation, reset to the **same uniform lossless medium on both sides** to isolate what the sheet itself emits. Restrict the phased sheet to a real propagating normal wavenumber, |k_parallel|<k; exclude grazing incidence and evanescent cases from the lecture.

## First 45 minutes: tilted waves, matching phase and H/V


| Minutes | Topic and student work | Mathematical purpose |
| --- | --- | --- |
| 0–12 | **Board with student contributions:** tilt the wave in the xz plane and keep Cartesian derivatives. Try $E_y=U(z)e^{-jk_\parallel x}$, identify separation of variables, substitute into Helmholtz and obtain the ODE. Name kz²=km²−k_parallel² and interpret the exponential roots. | A second, spatial use of a familiar PDE technique. Make the coefficient definition explicit and recover the vector-wavenumber geometry. |
| 12–22 | Match phase along the whole interface. Use the phase activity briefly, then pairs find the transmitted direction for air to εr=4 at 30°. Write vector wavenumbers and check components/magnitudes. | A valid bulk wave can still fail the boundary. Recover known Snell/reflection laws from shared tangential wavenumber. |
| 22–30 | **Pairs, then feedback:** calculate the Cartesian curl of a supplied transmitted H-polarized field. Recover its magnetic field and check transversality with a dot product. | Practise partial derivatives, curl, signs and vector interpretation on an oblique field. |
| 30–40 | Show H and V field geometry. Use the preceding curl to obtain the H matching equations; provide the V equations. Identify where the cosines occur, then inspect supplied reflected-power curves. | Polarization dependence follows from tangential projections. Reuse the coefficient algebra instead of deriving two Fresnel formula sets. |
| 40–45 | Brief H/V check and transition: what source could generate a wave with this tangential phase? Explain that smooth-plane reflection is specular; off-nadir backscatter also depends on finite structure or roughness. | Consolidate the geometry, then give the current-sheet calculation a purpose. |

### Board calculation 1: a PDE technique with a purpose

For Ey(x,z), write the full Cartesian Laplacian, including the vanishing y derivative. Within medium m,

\[
\frac{\partial^2E_y}{\partial x^2}
+\underbrace{\frac{\partial^2E_y}{\partial y^2}}_{0}
+\frac{\partial^2E_y}{\partial z^2}+k_m^2E_y=0,
\qquad k_m=|\vec k_m|=\omega\sqrt{\mu_m\epsilon_m}.
\]

Try a separated product,

\[
E_y(x,z)=U(z)e^{-jk_\parallel x}.
\]

Call this separation of variables, linking explicitly to the earlier heat-equation product solution. Here we choose a harmonic x factor; substituting and cancelling that nonzero factor gives

\[
U''+(k_m^2-k_\parallel^2)U=0.
\]

Now define the coefficient,

\[
\boxed{k_{zm}^2=k_m^2-k_\parallel^2},\qquad
U''+k_{zm}^2U=0.
\]

Ask for the exponential trial, its two roots and their directions. For the propagating case, the two factors are exp(∓jkzm z). Relate

\[
k_m^2=k_\parallel^2+k_{zm}^2
\]

to the components of the vector wavenumber. The material fixes km at this frequency; the interface fixes the common tangential component $k_\parallel$. Do not repeat the full general X(x)U(z) separation-constant proof; keep it available in the book if students ask why the product is useful.

### Phase matching: a boundary condition for every x

At z=0, each field contains its tangential factor exp(−jkx x). Constant amplitudes cannot fix different phase slopes. Thus

\[
\boxed{k_{i,x}=k_{r,x}=k_{t,x}=k_\parallel},
\qquad k_1\sin\theta_i=k_2\sin\theta_t.
\]

Angles are measured from the normal. The reflected wave keeps $k_\parallel$ and reverses its normal component. Refer to the previously derived acoustic angle laws; the new argument is phase matching along the whole boundary.

Use [Make the phases meet](https://bscect.github.io/FieldWaves/main/5_electromagnetic_waves/05_03_oblique_incidence.html#make-the-phases-meet), with the [local standalone activity](../book/5_electromagnetic_waves/interactives/phase_matching.html) as fallback. Compare the matched case with a deliberately wrong transmitted angle. Both trial waves keep the correct bulk wavenumber magnitude, but the wrong angle fails the all-x boundary check. Agreement at the origin is insufficient.

One activity comparison is enough; protect the following written task.

### Student calculation: write and check a tilted field

Air to ε₂=4ε₀, both μ=μ₀, incidence at 30°. Supply k₁ and ask for the dimensionless vector components:

\[
\vec k_i=k_1\left(\frac12\hat x+\frac{\sqrt3}{2}\hat z\right),\qquad
\vec k_r=k_1\left(\frac12\hat x-\frac{\sqrt3}{2}\hat z\right),
\]

\[
\vec k_t=k_1\left(\frac12\hat x+\frac{\sqrt{15}}{2}\hat z\right),
\qquad \theta_t=\sin^{-1}(1/4)\simeq14.5^\circ.
\]

Check shared tangential components and magnitudes k₁, k₁, 2k₁. Then provide

\[
\vec E_t=\hat y C e^{-j(k_\parallel x+k_{z2}z)}
\]

and ask students to start with the Cartesian curl, rather than immediately quoting a vector-wave rule:

\[
\nabla\times\vec E_t
=-\hat x\frac{\partial E_{ty}}{\partial z}
+\hat z\frac{\partial E_{ty}}{\partial x}
=j(k_{z2}\hat x-k_\parallel\hat z)E_{ty}.
\]

Faraday then gives

\[
\boxed{\vec H_t=\frac{E_{ty}}{\omega\mu_2}
(-k_{z2}\hat x+k_\parallel\hat z).}
\]

Check kt·Ht=0 and explain that transverse means perpendicular to propagation. If the class needs support, supply the two nonzero derivative terms and ask them to complete the signs and dot product. Differentiating spatial phase multiplies each plane-wave term by its own wavevector; the sum of incident and reflected fields has no single wavevector.

### Polarization: let the projections explain the difference

For a horizontal surface, the incidence plane is vertical. Define:

- **H polarization:** E along y, perpendicular to the incidence plane and parallel to the ground.
- **V polarization:** E in the xz incidence plane, tilted so it remains perpendicular to its own propagation direction. V does not mean E points purely vertically.

Acknowledge TE/s and TM/p once. Keep H/V as the working labels; distinguish the H polarization label from the magnetic field H.

Use the same full electric amplitudes A,B,C and the book's reflected basis convention. Students have just obtained the needed magnetic projection for H polarization:

\[
A+B=C,\qquad
\frac{\cos\theta_i}{\eta_1}(A-B)
=\frac{\cos\theta_t}{\eta_2}C.
\]

Provide the V counterpart:

\[
(A+B)\cos\theta_i=C\cos\theta_t,\qquad
\frac{A-B}{\eta_1}=\frac{C}{\eta_2}.
\]

Ask where the cosines moved and which field is being projected. There is no need to solve both systems afresh. Show a supplied H/V reflected-power plot for the same nonmagnetic, lossless material pair. Ask for agreement at normal incidence and the different behaviour at oblique incidence. A visible V minimum can be named Brewster's angle in passing, without deriving another formula.

For reference, power through the interface uses the normal Poynting component:

\[
\mathcal R=|r|^2,\qquad
\mathcal T=\frac{\eta_1\cos\theta_t}{\eta_2\cos\theta_i}|t|^2.
\]

Let students identify the cosine as a dot product with the interface normal. Do not turn this into an additional full power derivation. The required comparison is reflected power; this transmission relation can remain reference material if time is tight.

TeachBook support: [oblique incidence](../book/5_electromagnetic_waves/05_03_oblique_incidence.md) and [H/V reflection](../book/5_electromagnetic_waves/05_04_polarization_at_interface.md).


## Second 45 minutes: a phased current generates the oblique reflected wave

| Minutes | Topic and student work | Mathematical purpose |
| --- | --- | --- |
| 0–6 | Add a surface current to the familiar boundary conditions. Use the Ampère–Maxwell loop to obtain the H jump. Briefly write J=Kδ(z). | A localized source can survive a shrinking-area integral. Retrieve circulation, cross products and the spatial delta. |
| 6–18 | **Board with student contributions:** prescribe a y-directed sheet current with x-dependent phase. Reuse the first block's separated plane waves and Cartesian curl. Choose outgoing normal components and derive the common emitted amplitude. | The source fixes tangential phase; the bulk PDE fixes normal variation; the jump condition fixes amplitude. Only one cosine projection is new relative to normal incidence. |
| 18–29 | **Pairs, then feedback:** illuminate a perfect conductor with an oblique H-polarized wave. Find the sheet current that makes total tangential E vanish. Check which magnetic components add and which cancel, and verify reflected power. | Superposition and boundary conditions determine the induced current. A vanishing tangential E can coexist with finite current. |
| 29–37 | Briefly restore finite conductivity. Use the existing conductor activity at normal incidence as a checkpoint: identify finite surface field and energy deposited within the skin layer. The oblique finite-sheet formula is available if useful. | Reuse attenuation and energy accounting without starting another impedance derivation. Keep thin-sheet transmission distinct from a thick conductor's absorption. |
| 37–41 | Flexible consolidation, or a short radar connection: a spatial phase gradient selects a direction of emission. A finite antenna or target complicates the geometry but keeps the field/current/field story. | Explain the purpose of the phased sheet. Keep this a picture and interpretation, not a new radiation calculation. |
| 41–45 | Exit questions and discussion. | Check the phase/current/field chain and close with a completed calculation. |

### The source and the two outgoing fields

After the delta/jump reminder, prescribe the **surface-current phasor**

\[
\boxed{\vec K(x)=\hat yK_0e^{-jk_\parallel x}},\qquad [K_0]=\mathrm{A/m}.
\]

The common time factor remains exp(+jωt). An external source maintains this current; no incident waves are present yet. The current direction is y, while its relative phase varies with x. Those are different aspects of a vector field; phase variation along x does not mean the current flows along x.

The field must carry the same tangential phase to satisfy the source condition for every x. Reuse

\[
k_z^2=k^2-k_\parallel^2,\qquad k_z>0,
\qquad k_\parallel=k\sin\theta,\quad k_z=k\cos\theta.
\]

Select outgoing waves, with a common electric amplitude As fixed by tangential E continuity:

\[
\vec E_+=\hat yA_s e^{-j(k_\parallel x+k_zz)},\qquad z>0,
\]

\[
\vec E_-=\hat yA_s e^{-j(k_\parallel x-k_zz)},\qquad z<0.
\]

Their vector wavenumbers are

\[
\vec k_\pm=k_\parallel\hat x\pm k_z\hat z.
\]

Students have already calculated the needed Cartesian curl in the first block. Reuse its result while asking them to check the changed normal-component sign:

\[
\vec H_+=\frac{A_s}{\omega\mu}
(-k_z\hat x+k_\parallel\hat z)e^{-j(k_\parallel x+k_zz)},
\]

\[
\vec H_-=\frac{A_s}{\omega\mu}
(k_z\hat x+k_\parallel\hat z)e^{-j(k_\parallel x-k_zz)}.
\]

At z=0, impose

\[
\hat z\times(\vec H_+-\vec H_-)=\vec K.
\]

The normal H components cancel in the difference; the tangential components give

\[
-\frac{2k_zA_s}{\omega\mu}=K_0,
\]

\[
\boxed{A_s=-\frac{\omega\mu}{2k_z}K_0
=-\frac{\eta}{2\cos\theta}K_0.}
\]

We have the normal-incidence result with the magnetic-field cosine projection included. Its factor two still comes from the two outgoing waves in identical surrounding media. At θ=0 the original −ηK₀/2 result returns, with the electric/current axis rotated to y.

Ask for one Poynting-vector direction and the normal-incidence limit. If time permits, check normal B continuity from the equal normal H components. Do not calculate every Maxwell relation again.

### Student task: the current required by a perfect conductor

Send an H-polarized incident wave towards z=0 from z<0:

\[
\vec E_i=\hat yE_i e^{-j(k_\parallel x+k_zz)}.
\]

For a uniform conductor the induced sheet current has the same x-dependent phase. At the surface, factor out this common phase and write the full amplitude equality:

\[
\boxed{E_{\rm sheet}=E_i+E_{\rm emitted}
=E_i-\frac{\eta K_0}{2\cos\theta}.}
\]

Give the perfect-conductor condition Esheet=0 and ask pairs to find K₀ and the reflected field. Then ask them to check the magnetic components. The target results are

\[
\boxed{K_0=\frac{2\cos\theta}{\eta}E_i,\qquad A_s=-E_i.}
\]

The backward emitted wave is the reflected wave,

\[
\boxed{\vec E_r=-\hat yE_i e^{-j(k_\parallel x-k_zz)}.}
\]

It keeps the tangential phase and reverses the normal propagation component: exactly the reflection law from the first block. The emitted forward field cancels the mathematical continuation of the incident wave in z>0. Their total there is zero; the continuation is a superposition construction, not a physical wave penetrating a perfect conductor.

Using the first block's field relation, the exterior surface components satisfy

\[
H_{x,\rm total}(0)=-\frac{2\cos\theta}{\eta}E_i e^{-jk_\parallel x},
\qquad H_{z,\rm total}(0)=0.
\]

The tangential magnetic contributions add, while the normal contributions cancel. The jump condition therefore gives the same surface current. Incident and reflected normal power fluxes have equal magnitudes |Ei|²cosθ/(2η), so R=1. The ideal conductor absorbs no power even though it carries a finite current.

Use θ=30° if numbers help: K₀=√3 Ei/η. The normal-incidence limit is 2Ei/η. Keep Ei as the full H-polarized electric amplitude throughout this comparison.

This is the required source/reflection calculation. It does not require solving a finite-conductivity half-space or introducing both current-sheet polarizations.

### Finite conductance: a short extension, not a second required derivation

If useful, restore the same surrounding medium on both sides and a freestanding conducting sheet with K₀=Gs Esheet. The solved amplitudes are

\[
E_{\rm sheet}=\frac{2\cos\theta}{2\cos\theta+\eta G_s}E_i,
\qquad
K_0=\frac{2G_s\cos\theta}{2\cos\theta+\eta G_s}E_i.
\]

They recover the previous perfect-conductor limit as Gs→∞. This gives a controlled explanation of Esheet→0 with K remaining finite. Supply these expressions if needed; the classroom algebra task can remain the PEC cancellation/check above.

For this thin sheet only,

\[
r=-\frac{\eta G_s}{2\cos\theta+\eta G_s},\qquad
t=\frac{2\cos\theta}{2\cos\theta+\eta G_s},
\]

\[
\mathcal R=|r|^2,\qquad \mathcal T=|t|^2,\qquad
\mathcal A=\frac{4\eta G_s\cos\theta}{(2\cos\theta+\eta G_s)^2}.
\]

These power fractions compare normal fluxes; both outgoing directions have the same |cosθ| and the same surrounding η. As an optional numerical check, ηGs=2cosθ gives r=−1/2, t=1/2 and R=T=1/4, A=1/2. Do not derive all these relations in the core route.

For a thick conductor, current is spread through a skin layer. K=∫J dz is then an integrated volume current at finite conductivity, rather than a literal delta sheet. Do not use Gs=σh with its full thickness. Entering power is deposited as heat; it is not transmitted out of a far face of a half-space.

### Existing activities and what changes for the later slide draft

The [phase-matching activity](https://bscect.github.io/FieldWaves/main/5_electromagnetic_waves/05_03_oblique_incidence.html#make-the-phases-meet) is used in block 1 as planned.

The existing [conductor activity](https://bscect.github.io/FieldWaves/main/5_electromagnetic_waves/05_02_conducting_reflection.html#make-the-conductor-better) is a **normal-incidence** model. Use it as the θ=0 checkpoint and for the brief thick-conductor heating demonstration. Its current/E axis is x; at normal incidence a rotation of the tangential axes gives the equivalent y-current case used here. Do not present its unchanged geometry or current normalization as if it simulated nonzero incidence angle. A later oblique extension would need its projection factors and normal power-flux normalization updated. No activity code is changed by this planning task.

The source diagrams also need adaptation: the existing normal-incidence sheet uses x-directed current and E; this calculation uses y-directed current/E, x-dependent phase, and H in the xz plane. Keep a flat xz view, show y with dot/cross symbols or a clearly labelled colour-coded component, and draw both outgoing tilted wavefronts with shared tangential phase. Do not merely tilt the old propagation arrow while leaving the current/field directions unchanged.

A useful illustration would show the phase of K_y along the sheet and the two emitted plane-wave fronts. It gives the cosine projection a geometric meaning and connects phase gradients to antenna steering. A real finite array generates a beam with diffraction; the infinite sheet is the idealization used for this calculation. A full animation or array theory is optional later work.

TeachBook support: [conducting reflection](../book/5_electromagnetic_waves/05_02_conducting_reflection.md), [oblique incidence](../book/5_electromagnetic_waves/05_03_oblique_incidence.md), [H/V reflection](../book/5_electromagnetic_waves/05_04_polarization_at_interface.md), and [skin depth](../book/5_electromagnetic_waves/04_03_conductors_and_skin_depth.md). The lecture deliberately combines these in a different order without changing the book itself.

## Closing checks

Give about two minutes individually, then discuss:

1. What fixes the magnitude of the wavevector, and what fixes its tangential component?
2. For the y-directed current with x-dependent phase, what field direction and polarization do we get?
3. At an H-polarized perfect reflector, which magnetic components add and which cancel? Can a zero tangential electric field coexist with finite current?

Finish with the same method in two settings: the bulk PDE fixes allowed fields, boundary/source conditions select and join them, and the Poynting vector checks energy flow. A prescribed source and an induced current use the same mathematics with different conditions determining the current.

## Pacing and reserve material

Aim for around 24 numbered frames, matching the successful pace of W2.3L1, with two reserve slides. Protect the first block's written curl task and the second block's PEC cancellation/current check. Keep real conductors and finite-sheet algebra short enough to let both calculations reach a conclusion.

If time is tight, supply the transmitted vector components in block 1, show one H/V power comparison, and give the already-derived H relation for the current sheet. The phased-sheet/PEC construction remains worthwhile; repeating all Cartesian derivatives in both blocks does not.

Reserve choices:

- The finite-Gs oblique-sheet numerical check above, if the main current calculation goes quickly.
- A finite-wire closing picture linking the incident-field projection, induced current and directional backscatter. Use [the book's finite-object discussion](../book/5_electromagnetic_waves/05_05_finite_object_scattering.md); do not derive a radiation integral.

Leave V-polarized phased-sheet sources, their associated surface-charge calculation, evanescent/grazing cases, general surface-impedance derivations, multilayers and a Brewster-angle derivation outside the lecture core.

### Optional author check: the source as an inhomogeneous PDE

For this divergence-free y current, the combined electric field can be written

\[
E_y=A_s e^{-jk_\parallel x}e^{-jk_z|z|}.
\]

Its normal derivative jumps by −2jkz As exp(−jk_parallel x). Consequently,

\[
(\nabla^2+k^2)E_y
=j\omega\mu K_0 e^{-jk_\parallel x}\delta(z).
\]

The homogeneous Helmholtz equation is recovered off the sheet, and its source strength gives the same As. This is a useful consistency check and a connection to earlier source-driven PDEs, not required new distributional differentiation for the students.

## Literature supporting the phased-sheet construction

[MIT, Haus and Melcher, *Electromagnetic Fields and Energy*, §12.6, Example 12.6.2](https://web.mit.edu/6.013_book/www/chapter12/12.6.html) treats a travelling-wave TE current sheet, product solutions and outgoing oblique waves. Its coordinate axes differ; the lecture calculation above relabels them to the book's xz incidence plane and y-polarized E.

[Berkeley EECS 117, Lecture 24, pp. 16–17](https://rfic.eecs.berkeley.edu/courses/ee117/pdf/lecture24.pdf#page=17) relates tangential TE field components through η/cosθ. We obtain the same projection directly from the Cartesian curl rather than require a new impedance definition.
