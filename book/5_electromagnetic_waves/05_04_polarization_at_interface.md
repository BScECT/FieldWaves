# Polarization changes the reflected field

The phase matching in {doc}`05_03_oblique_incidence` determines where the waves go. Their amplitudes still have to satisfy the field boundary conditions. At oblique incidence, the field orientation now matters to those conditions.

We introduced polarization through the electric-field tip and antenna response in {doc}`03_03_polarization`. Here it changes the interaction with the material itself.

## Two orientations that make the calculation simple

Keep the $xz$ plane of incidence and the interface at $z=0$. For a horizontal ground surface, this is a vertical plane. We use the radar names:

- **Horizontal polarization (H):** the electric field is along $y$, perpendicular to the plane of incidence and parallel to the ground.
- **Vertical polarization (V):** the electric field lies in the vertical plane of incidence; the magnetic field is along $y$.

Both waves are transverse: $\vec E$ and $\vec H$ are perpendicular to their own propagation direction. For V polarization the electric field is generally tilted: it has both $x$ and $z$ components, rather than pointing along the vertical axis.

Electromagnetics books usually call these **TE/s** and **TM/p**, respectively, for this interface geometry. We acknowledge those names so you can recognize them elsewhere, but use **H and V** here. These labels describe electric-field polarization; H in an HH or HV radar channel is not the magnetic field $\vec H$.

Any incident transverse polarization can be resolved into these two components. Our planar, isotropic interface treats them separately, so linear superposition gives the response to their sum.

```{figure} figures/interface_hv_polarization.svg
:name: fig:em-interface-hv
:width: 80%
:alt: A red vertical plane of incidence intersects a blue horizontal interface. The incident electric-field directions are shown in blue for H polarization, perpendicular to the plane of incidence, and orange for V polarization, within that plane and perpendicular to the incident ray. Positive z points into the lower medium.

Two incident electric-field orientations for the same ray geometry. The red plane is the $xz$ plane of incidence; the blue surface is the interface at $z=0$. Positive $z$ points into medium 2. For H polarization, $\vec E_H$ points along $+y$, perpendicular to the plane of incidence ($E_\perp$). For V polarization, $\vec E_V$ lies in that plane ($E_\parallel$) and is perpendicular to $\vec k_i$. Here “parallel” refers to the **plane of incidence**, not to the propagation direction or the interface. The field arrows indicate the positive incident basis directions used below, not relative amplitudes. Adapted from the author's PPEO course figure.
```

## Work through horizontal polarization using the vector fields

Let $A$, $B$ and $C$ be electric-field amplitudes along the common $+\hat y$ axis. Write the incident, reflected and transmitted electric-field phasors explicitly as

$$
\begin{aligned}
\vec E_i(\vec r)&=\hat y\,A e^{-j\vec k_i\cdot\vec r},\\
\vec E_r(\vec r)&=\hat y\,B e^{-j\vec k_r\cdot\vec r},\\
\vec E_t(\vec r)&=\hat y\,C e^{-j\vec k_t\cdot\vec r}.
\end{aligned}
$$

Each electric field has **only a $y$ component**: $E_x=E_z=0$. All three propagation vectors lie in the $xz$ plane, so $\vec k\cdot\hat y=0$: the electric field is orthogonal to its own propagation direction. It is also parallel to the horizontal $xy$ interface at $z=0$. Thus the entire electric field is tangential to the interface; no projection factor is needed for electric-field matching.

At the boundary, phase matching gives all three waves the same factor $e^{-jk_\parallel x}$. Cancelling that common factor, tangential electric continuity gives

$$
A+B=C.
$$

For each plane wave, Faraday's law gives

$$
\vec H=\frac{\vec k\times\vec E}{\omega\mu}
=\frac{\hat k\times\vec E}{\eta}.
$$

This is the same cross product used for the diagonal plane wave in {doc}`03_01_waves_3d`. For example,

$$
(\hat x\sin\theta_i+\hat z\cos\theta_i)\times\hat y
=-\hat x\cos\theta_i+\hat z\sin\theta_i.
$$

Thus the tangential magnetic amplitudes are

$$
H_{i,x}=-\frac{A\cos\theta_i}{\eta_1},\quad
H_{r,x}=+\frac{B\cos\theta_i}{\eta_1},\quad
H_{t,x}=-\frac{C\cos\theta_t}{\eta_2}.
$$

With no free current sheet, their matching gives

$$
\frac{\cos\theta_i}{\eta_1}(A-B)
=\frac{\cos\theta_t}{\eta_2}C.
$$

Divide by $A$, defining $r_H=B/A$ and $t_H=C/A$:

$$
1+r_H=t_H,\qquad
\frac{\cos\theta_i}{\eta_1}(1-r_H)
=\frac{\cos\theta_t}{\eta_2}t_H.
$$

The normal-incidence algebra returns, with geometric projection factors. Solving gives

$$
\boxed{r_H=\frac{\eta_2\cos\theta_i-\eta_1\cos\theta_t}
{\eta_2\cos\theta_i+\eta_1\cos\theta_t},\qquad
 t_H=\frac{2\eta_2\cos\theta_i}
{\eta_2\cos\theta_i+\eta_1\cos\theta_t}.}
$$ (eq:em-interface-te)

These are **Fresnel coefficients** for horizontal polarization. At normal incidence the cosines become one, recovering the earlier result.

```{admonition} Check another Maxwell relation
:class: question

Use $H_z=(\sin\theta/\eta)E_y$ for each H-polarized wave. Show that normal $B=\mu H$ also matches when $A+B=C$ and the tangential wavenumbers match. Hint: $\mu\sin\theta/\eta=k_\parallel/\omega$.

This is a useful habit: after using enough conditions to determine the solution, check one that was not used in the calculation.
```

## Set up vertical polarization, then compare

For V polarization we must specify directions before giving signed coefficients. Choose the electric-field unit vectors

$$
\hat e_i=\hat x\cos\theta_i-\hat z\sin\theta_i,\quad
\hat e_r=\hat x\cos\theta_i+\hat z\sin\theta_i,\quad
\hat e_t=\hat x\cos\theta_t-\hat z\sin\theta_t.
$$

All three have a positive tangential $x$ component. Write their full electric amplitudes as $A$, $B$, $C$ again. The corresponding magnetic fields have amplitudes $+A/\eta_1$, $-B/\eta_1$ and $+C/\eta_2$ along $y$.

The matching equations are now

$$
(A+B)\cos\theta_i=C\cos\theta_t,\qquad
\frac{A-B}{\eta_1}=\frac{C}{\eta_2}.
$$

The cosine factors have moved because it is now the **electric** field that must be projected onto the interface. The result is

$$
\boxed{r_V=\frac{\eta_2\cos\theta_t-\eta_1\cos\theta_i}
{\eta_2\cos\theta_t+\eta_1\cos\theta_i},\qquad
 t_V=\frac{2\eta_2\cos\theta_i}
{\eta_2\cos\theta_t+\eta_1\cos\theta_i}.}
$$ (eq:em-interface-tm)

Here $t_V$ is the ratio of **full electric amplitudes**, not just tangential components. In particular, $(1+r_V)\cos\theta_i=t_V\cos\theta_t$. Some references choose the opposite reflected V-polarization basis direction and consequently write the opposite sign for $r_V$; the physical field is the same once that direction is included.

```{admonition} Let the vector directions do the work
:class: question

1. Check that $\hat e_i\cdot\vec k_i=0$ and calculate $\hat k_i\times\hat e_i$.
2. Repeat for the reflected wave. Explain the magnetic-field sign.
3. Solve the two V-polarization matching equations for $r_V$ and $t_V$.
4. Set both angles to zero and recover the normal-incidence coefficients.
```

## Compare power through the interface

Use the time-averaged Poynting vector again. Power crossing the interface depends on its **normal component**, as in the tilted-surface calculation in {doc}`03_02_energy_flow`. For either polarization,

$$
\boxed{\mathcal R=|r|^2,\qquad
\mathcal T=\frac{\eta_1\cos\theta_t}{\eta_2\cos\theta_i}|t|^2,\qquad
\mathcal R+\mathcal T=1.}
$$ (eq:em-interface-oblique-power)

These expressions apply to our lossless media and propagating waves, with $A$, $B$, $C$ the full electric amplitudes defined above. Comparing flux along each ray without the projection would miss the cosine ratio.

At normal incidence, H and V give the same response. At oblique incidence, their reflected-power curves generally differ. For ordinary nonmagnetic lossless dielectrics, V-polarized reflection can vanish at a particular angle, the **Brewster angle**. We can identify it from the zero in the numerator of $r_V$. Loss generally changes the zero into a minimum.

### Find the Brewster angle

Use the activity below to find the minimum before revealing its angle. Both curves show reflected **power**, so the sign of a field coefficient does not appear in the graph. The table checks the transmitted power independently for each polarization.

```{admonition} Predict, explore, then explain
:class: question

1. Start at normal incidence. Do H and V reflect the same fraction? Increase the angle: which curve reaches zero?
2. Find that minimum, reveal the Brewster angle, and use the button to go there exactly. Is the H reflection also zero? What is the sum $\theta_i+\theta_t$? Inspect the reflected and transmitted ray directions.
3. Change the material. How does the minimum move? Choose identical media: why is there now no unique angle of zero V reflection?
4. Select visible-light water. At its Brewster angle, compare upright and sideways polarizing sunglasses. Explain which reflected component each lens orientation passes.
```

```{raw} html
:file: interactives/fresnel_polarization_embed.html
```

For distinct nonmagnetic, lossless media, the zero of $r_V$ and Snell's law give

$$
\tan\theta_B=\frac{n_2}{n_1},\qquad
\theta_B+\theta_t=90^\circ,
\qquad n_m=\sqrt{\epsilon_{r,m}}.
$$

Thus the reflected and transmitted rays are perpendicular at this angle. The V-polarized wave is fully transmitted in this ideal model, while H reflection remains. If the two media are identical, both reflected components vanish at every angle: there is no special Brewster angle.

### Why polarizing sunglasses suppress glare

Sunlight is approximately unpolarized: it carries equal average power in two independent transverse polarization components. Reflection from a horizontal water surface treats those components differently. Near the Brewster angle, little V power is reflected, so the glare is predominantly H polarized, with its electric field parallel to the water surface. At the ideal Brewster angle, the reflected V component vanishes altogether.

**Polarizing sunglasses** usually have a transmission axis aligned with the V direction for this viewing geometry. They pass that component and block H, removing much of the glare. Rotating the lens by $90^\circ$ reverses the selection and makes the glare brighter. Ordinary tinted sunglasses reduce both components without this directional selection. The same reflection argument is discussed in [Fitzpatrick's Fresnel treatment](https://farside.ph.utexas.edu/teaching/315/Waveshtml/node59.html).

The activity makes this quantitative. Let $I_i$ be the total incident sunlight intensity and let the ideal polarizer's transmission axis make an angle $\alpha$ with the reflected V direction. Projection onto that axis, followed by squaring, gives

$$
\frac{I_{\mathrm{eye}}}{I_i}
=\frac12\left(\mathcal R_H\sin^2\alpha
+\mathcal R_V\cos^2\alpha\right).
$$

The factor $1/2$ assigns half the incident intensity to each polarization. Their average powers add because the components of unpolarized light are not phase locked. At $\alpha=0$, only V passes; at $\alpha=90^\circ$, only H passes. This reuses the antenna-projection idea from {doc}`03_03_polarization`.

For visible light, water has $n\approx1.333$, giving $\theta_B\approx53.1^\circ$. This optical index must not be confused with the much larger radar-frequency permittivity used in our earlier water examples. Real rough surfaces and imperfect polarizers generally leave some residual glare.

## What does a radar measure?

The H and V components are the basis for radar channels such as HH and VV: the first letter gives transmitted polarization, and the second gives received polarization, as in {doc}`03_03_polarization`.

A radar can change its transmitted polarization and obtain a different reflected signal from the same material. This gives the orientation discussion in {doc}`03_03_polarization` a second role: polarization affects both target interaction and receiver response.

A perfectly smooth plane reflects specularly. At oblique incidence that reflected ray does not return to a radar at the transmitter position. Real off-nadir radar backscatter depends on roughness and target geometry as well as material response. The Fresnel coefficients are an ingredient in that interpretation. In {doc}`05_05_finite_object_scattering` we use the current picture to see how a finite target can send energy back.

### Fresnel coefficients inside scattering models

The Fresnel coefficients are also building blocks in many models of scattering from complex surfaces, including rough soil and the sea. One example is the **Kirchhoff, or tangent-plane, approximation**: approximate the surface near each point by its local tangent plane, and use the Fresnel response at the local incidence angle to estimate the surface fields. These fields then supply the radiation calculation for the scattered wave. [Voronovich's introduction to the tangent-plane approximation](https://repository.library.noaa.gov/view/noaa/31125) describes this construction.

Different surface slopes give different local angles and H/V directions. Contributions reaching a receiver also have different propagation phases, so we must combine their fields before calculating power. Surface-height and slope statistics then help predict the average scattering. Fresnel coefficients supply the material and polarization response; surface geometry supplies additional directional and interference effects.

This explains why permittivity and polarization still matter to a radar echo from an irregular surface. It also explains why a plane-interface reflectance alone is not a backscatter model. Roughness relative to wavelength, shadowing and multiple scattering determine which approximation is useful. A single-plane Brewster zero need not survive that combination of local angles and fields.

## Reading and sources

The s/p construction and Fresnel relations can be compared with [TU Delft's *Interactive Optics*, reflection and transmission at an interface](https://interactivetextbooks.tudelft.nl/tn2421/content/Chap1_Basics/Basics_2022_01Clean.html#reflection-and-transmission-at-an-interface). Keep track of each source's time convention and electric-field basis when comparing signed coefficients.
