# Exercises: Dipoles, Cancellation and Earth's Field

These problems consolidate the completed magnetic-field sections. They emphasize reading vector expressions, recognizing cancellations, and distinguishing a governing equation from its boundary data. Begin with a prediction or sketch; use the folded hints and checks only after an attempt.

## 1. From an angular sketch to component graphs

A dipole at the origin has moment $\vec m=m\hat z$. At fixed radius $R$, revisit the right semicircle in the $x$–$z$ plane, with $\hat r=\sin\theta\,\hat x+\cos\theta\,\hat z$ and $0\leq\theta\leq\pi$. Define $B_*=\mu_0m/(4\pi R^3)$.

1. Explain physically why the dipole field is axially symmetric. Then use the vector formula to explain why its field arrows lie in a plane containing the moment axis. Are these the same statement?
2. Derive $B_x/B_*$ and $B_z/B_*$ from $3(\vec m\cdot\hat r)\hat r-\vec m$. Identify the scalar projection and the two vectors being added.
3. Sketch both normalized components **as functions of $\theta$**, from $0$ to $\pi$. Use the five angles in the earlier circle sketch as checkpoints. Relate each sign change to the direction of an arrow on that circle.
4. Find the two angles where $B_z=0$. Does the full field vanish there? Sketch its direction at both points.
5. Rotate your observation semicircle by a quarter-turn about $z$, into the positive-$y$ half of the $y$–$z$ plane. How do the Cartesian components change? Why does this agree with axial symmetry?
6. At radius $2R$, what changes in the component graphs if you keep the original normalization $B_*$? Would replacing $\hat r$ by the dimensional vector $\vec r$ in the original formula preserve its units?

```{admonition} Check
:class: dropdown

A circular current loop is unchanged by rotation about its moment axis; its dipole field shares that symmetry. Separately, the dipole formula combines only $\hat r$ and $\vec m$, leaving no component perpendicular to their plane. Axial symmetry alone would not exclude an azimuthal component.

The component curves are

$$
\frac{B_x}{B_*}=3\sin\theta\cos\theta=\frac32\sin(2\theta),
\qquad
\frac{B_z}{B_*}=3\cos^2\theta-1.
$$

The $x$ component is positive above the equator and negative below it. The $z$ component is positive near either pole and negative near the equator. It vanishes where $\cos\theta=\pm1/\sqrt3$, at about $54.7^\circ$ and $125.3^\circ$. There, $B_x/B_*=+\sqrt2$ and $-\sqrt2$, respectively: the field is horizontal, not zero.

After the quarter-turn, the previous $x$ component becomes the $y$ component; the new $x$ component is zero and $B_z$ is unchanged. The arrow rotates with the observation point, preserving its magnitude and orientation relative to the local radius.

At $2R$ the graphs, normalized by the original $B_*$, are reduced by a factor of eight. Their zero crossings and relative shapes are unchanged. A dimensional $\vec r$ cannot replace a unit vector without compensating distance factors. The dot product supplies angular scaling, the second unit vector supplies direction, and the prefactor supplies radial decay.
```

## 2. Curved field lines, local curl and a scalar potential

Compare (a) the entire exterior of an ideal infinitely long current-carrying wire and (b) the exterior of a sphere enclosing a compact current loop.

1. In each domain, what is the local curl of $\vec B$ under the magnetostatic vacuum approximation?
2. Can a closed path in the domain have nonzero circulation? Explain through Ampère's law and the domain geometry.
3. Where is a single-valued scalar magnetic potential guaranteed by the conditions discussed in the chapter?
4. Why does the shape of a curved field line not by itself determine the local curl?

```{admonition} Check
:class: dropdown

Both exterior fields are locally curl-free. In (a), a path linking the excluded wire has circulation $\mu_0I$, so a global single-valued scalar potential on that whole domain is impossible. In (b), every path can contract within the spherical exterior; the curl-free field has a scalar potential. Curl concerns infinitesimal circulation per area, not simply whether a drawn field line bends.
```

(sec:opposing-dipoles)=
## 3. Cancel the dipole contribution: two opposing dipoles

Place an ideal magnetic dipole $+m\hat z$ at $z=s/2$ and an equal opposing dipole $-m\hat z$ at $z=-s/2$, with $m,s>0$. Consider points on the positive axis $z>s/2$. Each dipole is an idealization of a small current loop, with loop size much smaller than the distances being considered. Define $C=\mu_0m/(4\pi)$.

1. Sketch the two moments. What is their net magnetic dipole moment?
2. Using the single-dipole scalar potential, justify the axial expression

   $$
   \Psi(z)=C\left[\frac1{(z-s/2)^2}-\frac1{(z+s/2)^2}\right].
   $$

3. Before expanding, predict which leading powers cancel when $z\gg s$.
4. Set $\varepsilon=s/(2z)$. Use $(1\pm\varepsilon)^{-2}\approx1\mp2\varepsilon$ to find the first surviving potential term, including its coefficient.
5. Differentiate your far-field expression to find $B_z=-d\Psi/dz$. Why is an axial derivative sufficient for this component here?
6. Compare the decay with one dipole. What fraction remains when distance doubles in the far field?
7. If the two moments are not exactly equal and opposite, which contribution eventually dominates sufficiently far away?

```{admonition} Hint: the same cancellation, one level higher
:class: dropdown

Factor out $C/z^2$. Both remaining terms begin with 1, so their difference starts at order $s/z$. The extra inverse power comes from subtracting nearly equal contributions, not from changing the strength of either dipole.
```

```{admonition} Check and interpret
:class: dropdown

The total moment is zero. On the positive axis both observation directions relative to the sources are $+\hat z$, so the two potentials have opposite signs. Their leading terms give

$$
\Psi(z)\approx\frac{C}{z^2}\bigl[(1+2\varepsilon)-(1-2\varepsilon)\bigr]
=\frac{2Cs}{z^3},
\qquad B_z\approx\frac{6Cs}{z^4}.
$$

Along this axis, symmetry removes transverse components and $z$ is the displacement coordinate. We are calculating the axial field, not obtaining a general three-dimensional gradient from a one-dimensional restriction.

The potential now decays as $z^{-3}$ and the field as $z^{-4}$; doubling distance gives factors of $1/8$ and $1/16$. This is a **quadrupole** leading contribution, corresponding to degree two in the harmonic description. The full field has angular structure; the expressions above apply only on the stated axis.

If a nonzero net dipole moment remains, its $r^{-3}$ field eventually dominates the faster-decaying contribution. If $s=0$ and the moments cancel exactly, the ideal fields cancel everywhere away from the shared singular point.

An equal opposing pair of ideal electric dipoles follows the same calculation with $C=p/(4\pi\epsilon_0)$ and $V$ in place of $\Psi$.
```

## 4. Passing Laplace is not the same as matching Earth

Two candidate exterior potentials are

$$
\Psi_1=C\frac{\cos\theta}{r^2},\qquad
\Psi_2=2C\frac{\cos\theta}{r^2},\qquad r\geq a,
$$

with $C>0$. Both vanish at infinity and satisfy Laplace.

1. Find their radial boundary fields at $r=a$.
2. Can both describe the same nonzero radial boundary data everywhere on the sphere?
3. Does their coexistence contradict uniqueness?
4. Suppose a candidate fits the field at one observation point. What additional check is needed before invoking uniqueness?

```{admonition} Check
:class: dropdown

The radial fields are $2C\cos\theta/a^3$ and $4C\cos\theta/a^3$. They differ except where $\cos\theta=0$. They therefore do not satisfy the same full boundary condition, and uniqueness is not contradicted. A pointwise fit is insufficient: the equation, domain, sources and complete boundary data must agree.
```

## 5. Optional extension: which spatial detail survives at altitude?

This extension practices powers and ratios using a supplied rule; no knowledge of spherical-harmonic functions is required. For an internal-source contribution of degree $\ell$, the field amplitude at radius $r$ is proportional to $r^{-(\ell+2)}$.

1. Compare degrees one and two at $r=2a$, assuming equal surface amplitudes. Relate degree two to the opposing-dipoles exercise.
2. At height $500\,\mathrm{km}$ above a sphere with $a=6371\,\mathrm{km}$, compare degree one and degree ten.
3. Does a high-degree residual uniquely identify a crustal source?

```{admonition} Check
:class: dropdown

At $2a$, the remaining fractions are $1/8$ and $1/16$. At 500 km they are approximately $0.80$ for degree one and $0.40$ for degree ten. Spatial degree describes a pattern, not a unique physical source: core and crustal contributions can overlap in spatial scale.
```

## 6. A force can change direction without changing speed

In a uniform field $\vec B=B\hat z$, a proton and an electron initially move with the same velocity $v\hat x$. Neglect electric fields and collisions, and assume both particles are nonrelativistic.

1. Sketch each initial force. Compare its magnitude for the two particles.
2. Which trajectory has the smaller gyroradius? Use $m_{\mathrm p}/m_{\mathrm e}\approx1836$.
3. Does the field do more work on the particle with the tighter orbit?
4. Explain why the resulting local circles cannot by themselves predict whether particles approaching Earth reach the atmosphere.

```{admonition} Check
:class: dropdown

The forces have equal magnitudes $evB$ and opposite directions: $-\hat y$ for the proton and $+\hat y$ for the electron. The electron's radius is about 1836 times smaller. Magnetic work is zero for both. Entry into Earth's surroundings depends on the particle trajectory through a spatially varying field and on the global geometry; the uniform-field approximation is local.
```

## 7. From a magnetized volume to its distant field

A cube of side $10\,\mathrm m$ has uniform prescribed magnetization $\vec M=10^3\hat z\,\mathrm{A/m}$. Its centre is the origin. Take $\mu_0/(4\pi)\approx10^{-7}\,\mathrm{T\,m/A}$.

1. Find its net magnetic moment, including units.
2. Estimate the axial magnetic field at $(0,0,1000\,\mathrm m)$ using the dipole approximation. Why is that approximation reasonable here?
3. Would the same approximation be reliable one metre above the cube's top face? Which expression would retain the source geometry there?
4. Suppose half the cube is magnetized in the opposite direction with equal magnitude. Which part of the distant field must disappear, and what need not vanish?

```{admonition} Check
:class: dropdown

The volume is $10^3\,\mathrm{m^3}$, so the moment is $10^6\hat z\,\mathrm{A\,m^2}$. At 1000 m the axial field is approximately $2\times10^{-10}\hat z\,\mathrm T=0.2\hat z\,\mathrm{nT}$. The observation distance is much larger than the source dimensions. Near the cube, use the distributed-magnetization integral rather than a single point dipole. Equal opposing halves have zero net moment, removing the dipole term; spatially varying higher-order fields can remain.
```

## 8. Three different uses of divergence and curl

Decide whether each claim is correct, and explain the physical distinction behind your answer.

1. “A steady current has zero divergence, so its magnetic field must have zero curl.”
2. “If current enters a capacitor plate without leaving it, electric charge is being destroyed.”
3. “Outside a sphere containing a localized steady current system, that system's magnetic field can be represented by a scalar potential.”
4. “An electromagnetic wave needs a nonzero charge density at every point through which it passes.”

```{admonition} Check
:class: dropdown

Only statement 3 is correct under the magnetostatic vacuum approximation used here. In 1, $\vec\nabla\cdot\vec J=0$ does not imply $\vec J=0$, and Ampère's law gives $\vec\nabla\times\vec B=\mu_0\vec J$. In 2, charge accumulates on the plate, consistent with the continuity equation. In 3, the spherical exterior is current-free and simply connected. In 4, time-dependent electric and magnetic fields can have nonzero curl even in charge-free vacuum; local charge accumulation is not required for propagation.
```
