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

```{admonition} Figure to develop — two polarizations, the same rays
:class: note

Use side-by-side H and V polarization drawings with identical incident, reflected and transmitted directions. Show $\vec E$, $\vec H$ and the interface normal, using clear into/out-of-page symbols. Mark the components tangential to the interface. The electric-field basis directions must agree with the signed amplitudes below.
```

## Work through horizontal polarization using the vector fields

Let $A$, $B$ and $C$ be electric-field amplitudes along the common $+\hat y$ axis. At the boundary, tangential electric continuity gives

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

At normal incidence, H and V give the same response. At oblique incidence, their reflected-power curves generally differ. For ordinary nonmagnetic lossless dielectrics, V-polarized reflection can vanish at a particular angle, the **Brewster angle**. We can identify it from the zero in the numerator of $r_V$; deriving a separate angle formula is optional. Loss generally changes the zero into a minimum.

```{admonition} Interactive activity to develop — polarization and incidence angle
:class: note

Control the incidence angle and relative permittivity, initially with $\mu_1=\mu_2=\mu_0$ and incidence from air into a higher-permittivity lossless medium. Show linked ray/field geometry and H/V reflected-power curves. Mark the current angle and check $\mathcal R+\mathcal T=1$. Ask students to predict the normal-incidence limit and find the V-polarization reflection minimum.
```

## What does a radar measure?

The H and V components are the basis for radar channels such as HH and VV: the first letter gives transmitted polarization, and the second gives received polarization, as in {doc}`03_03_polarization`.

A radar can change its transmitted polarization and obtain a different reflected signal from the same material. This gives the orientation discussion in {doc}`03_03_polarization` a second role: polarization affects both target interaction and receiver response.

A perfectly smooth plane reflects specularly. At oblique incidence that reflected ray does not return to a radar at the transmitter position. Real off-nadir radar backscatter depends on roughness and target geometry as well as material response. The Fresnel coefficients are an ingredient in that interpretation. In {doc}`05_05_finite_object_scattering` we use the current picture to see how a finite target can send energy back.

## Reading and sources

The s/p construction and Fresnel relations can be compared with [TU Delft's *Interactive Optics*, reflection and transmission at an interface](https://interactivetextbooks.tudelft.nl/tn2421/content/Chap1_Basics/Basics_2022_01Clean.html#reflection-and-transmission-at-an-interface). Keep track of each source's time convention and electric-field basis when comparing signed coefficients.
