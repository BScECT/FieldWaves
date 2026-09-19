# From Currents to Magnetic Dipoles

Gravity and electrostatics began with sources that act as monopoles: a mass and an electric charge. Magnetism is different. We do not observe isolated magnetic charges, and electric currents make magnetic fields that circulate. Yet, sufficiently far from its source, the field of a small current loop has the same geometrical form as the field of an electric dipole. Our aim in this section is to understand how these statements fit together.

We work in vacuum with steady currents, so the magnetostatic form of Ampère's law applies. The constant $\mu_0$ is the vacuum permeability; the magnetic field $\vec B$ is measured in tesla ($\mathrm T$).

```{admonition} Keep this question in view
:class: important

We begin with a current, rather than assume a dipole potential: **magnetic fields are not generally irrotational**. Follow the wire example through circulation and curl, then ask what changes when we observe a compact current system from outside. The dipole and its scalar potential will follow from that choice of source and observation region.
```

## How does the field reveal itself?

A compass responds to the magnetic field by **turning**. Its needle is a small magnetic dipole: the field exerts a torque that tends to align it with the local field. An ordinary compass is constrained to turn horizontally, so it indicates the direction of the horizontal component of $\vec B$. A freely tilting needle can also reveal the field's inclination. We will define the magnetic dipole moment quantitatively below.

A test charge responds differently. The magnetic part of the force on a charge $q$ moving with velocity $\vec v$ is

$$
\vec F_{\mathrm B}=q\,\vec v\times\vec B.
$$

A stationary test charge therefore experiences no magnetic force, even where $\vec B$ is nonzero; it may still experience an electric force if an electric field is present. For a moving charge, the cross product makes the magnetic force perpendicular to its velocity:

$$
\vec F_{\mathrm B}\cdot\vec v=0.
$$

The magnetic force can deflect a particle without changing its kinetic energy. In particular, the circulation $\oint\vec B\cdot d\vec\ell$ is **not mechanical work**: $\vec B$ is not the force per unit charge. This distinction will matter when we introduce a scalar magnetic potential.

## Returning to the field around a wire

Consider an infinitely long wire carrying a steady current $I$ in the positive $z$ direction. In vacuum its magnetic field is

$$
\vec B(s)
=\frac{\mu_0I}{2\pi s}\,\hat\varphi,
$$ (eq:magnetic-field-straight-wire)

where $s$ is the perpendicular distance from the wire. The field is tangent to circles centred on the wire. Along a circular path $C$ of radius $s$,

$$
d\vec\ell=s\,d\varphi\,\hat\varphi,
$$

and therefore

$$
\oint_C\vec B\cdot d\vec\ell
=\int_0^{2\pi}
\frac{\mu_0I}{2\pi s}s\,d\varphi
=\mu_0I.
$$ (eq:wire-magnetic-circulation)

```{figure} figures/straight_wire_field.svg
:name: fig-magnetic-straight-wire
:width: 80%
:alt: Cross-section of a straight wire carrying current out of the page, surrounded by counterclockwise circular magnetic field lines. The field is tangent to a circular integration path.

Viewed along the wire, the right-hand rule gives counterclockwise field lines for a current directed out of the page. On a concentric circular path, the field is tangent everywhere and has constant magnitude, so its circulation is $2\pi sB=\mu_0I$.
```

This is not what happens for a static electric field or a gravity field. In those cases,

$$
\oint_C\vec E\cdot d\vec\ell=0,
\qquad
\oint_C\vec g\cdot d\vec\ell=0,
$$

for every closed path on which the fields are well defined. Their vanishing circulation allows us to describe them globally as gradients of scalar potentials.

For the magnetic field, Ampère's law in vacuum relates circulation around an oriented closed path $C$ to the **linked current**, $I_{\mathrm{linked}}$: the net electric current passing through a surface $S$ whose boundary is $C$.

$$
\boxed{
\oint_C\vec B\cdot d\vec\ell
=\mu_0 I_{\mathrm{linked}}.
}
$$ (eq:ampere-linked-current)

Introduce the **current density** $\vec J$, measured in $\mathrm{A\,m^{-2}}$. It points along conventional current; its normal component gives the current per unit area crossing a surface. Thus the linked current is

$$
\boxed{
I_{\mathrm{linked}}=\int_S\vec J\cdot d\vec A,
\qquad d\vec A=\hat n\,dA,
\qquad \partial S=C.
}
$$ (eq:linked-current-density)

Here $\partial S=C$ means that $C$ bounds $S$. Curl your right-hand fingers along the direction of traversal of $C$; your thumb gives the positive surface normal. Current crossing along that normal counts positively, and current crossing against it counts negatively. The integral is a **signed sum**.

### From circulation to local curl

Recall **Stokes' theorem**, Eq. {eq}`eq:stokes` in the [chapter on curl](../../1_gradient_divergence_curl/curl.md): circulation around a curve equals the flux of the curl through a surface bounded by that curve. Combining it with Ampère's law gives

$$
\int_S(\vec\nabla\times\vec B)\cdot d\vec A
=\oint_C\vec B\cdot d\vec\ell
=\mu_0\int_S\vec J\cdot d\vec A.
$$

For a smooth current distribution, this holds for arbitrarily small surfaces with any orientation. The corresponding local relation is therefore

$$
\boxed{\vec\nabla\times\vec B=\mu_0\vec J.}
$$ (eq:ampere-differential-magnetostatic)

**Where current density is nonzero, the magnetostatic magnetic field has nonzero curl.** It cannot be written there as the gradient of a scalar. Outside the wire, $\vec J=0$ and the field is locally curl-free, but a path encircling the wire still has nonzero circulation. Thus we must consider the observation region as well as the local equation before claiming a single-valued potential.

This is the connection to carry forward: current density determines magnetic curl, just as charge density determines electric divergence. We will use it to decide where potential-field mathematics becomes available again.

```{admonition} Optional: the local step and its assumptions
:class: dropdown

Subtracting the two surface integrals gives

$$
\int_S(\vec\nabla\times\vec B-\mu_0\vec J)\cdot d\vec A=0.
$$

If a component of the continuous integrand were nonzero at a point, a sufficiently small surface with its normal in that direction would have a nonzero integral. Since the integral vanishes for every such surface, the vector integrand must vanish.

Stokes' theorem applies to a piecewise smooth oriented surface when the field is continuously differentiable in a neighbourhood of that surface. To derive the local equation inside a wire, consider a smooth current distribution in a wire of finite radius; do not apply the classical theorem across the singular axis of an ideal line current. The exterior straight-wire field used above remains a valid way to calculate circulation along a path outside the wire.

For uniform current density parallel to a wire, its perpendicular cross-section carries $I=JA_{\mathrm{wire}}$. More generally, $I=\int_{A_{\mathrm{wire}}}\vec J\cdot d\vec A$.
```

```{admonition} Optional: why the spanning surface does not matter
:class: dropdown

For steady currents, charge does not accumulate, so $\vec\nabla\cdot\vec J=0$. Consider two spanning surfaces $S_1$ and $S_2$ with the same boundary $C$, both oriented consistently with $C$. When they enclose a volume, $S_1$ and the oppositely oriented $S_2$ form its closed boundary. The divergence theorem gives

$$
\int_{S_1}\vec J\cdot d\vec A-\int_{S_2}\vec J\cdot d\vec A
=\int_V\vec\nabla\cdot\vec J\,dV=0.
$$

A flat disk and a curved spanning surface therefore give the same net linked current. The more general case can be treated by dividing the surfaces into pieces.
```

## Bending the wire into a loop

Now bend the current-carrying wire into a closed loop. A path threaded once around the wire has circulation $\mu_0I$, with its sign set by the orientation. A path spanning a surface with no net current crossing it has zero circulation. Neither statement tells us that the field vanishes along the path.

The phrase “inside the loop” can be misleading: Ampère's law counts the **signed current crossing a spanning surface**, not whether a path looks inside the coil in a drawing. The detailed geometry is explored in the optional panel below. Our next aim is to understand the field produced by the current loop when observed from far away.

````{admonition} Optional: linked paths and signed crossings
:class: dropdown

For a single current loop, the signed linking number counts the algebraic number of crossings of an oriented spanning surface. A crossing along the normal contributes $+I$; one against it contributes $-I$.

- One positive crossing gives circulation $\mu_0I$.
- No crossings give zero circulation.
- Two opposite crossings cancel, giving zero circulation.
- A path linking all $N$ turns of a coil in the positive sense gives circulation $\mu_0NI$.

```{figure} figures/loop_linked_paths.svg
:name: fig-magnetic-linked-paths
:width: 100%
:alt: Four panels show one positive current crossing, no crossing, two opposite crossings, and three positive crossings of an oriented disk.

Integration paths $C$ (blue) bound spanning disks $S$. The orange wire gives linked currents **(a)** $I$, **(b)** zero, **(c)** zero, and **(d)** $3I$. The disks are viewed face-on; dashed wire segments lie behind them. Coil turns are drawn separately; connecting wires and the return circuit are assumed not to cross $S$.
```

For the simple geometry in (c), the spanning surface can be deformed to avoid the wire, eliminating the pair of opposite crossings. In (a) and (d), no spanning surface can remove the net crossing count. Zero net current means zero circulation, not zero magnetic field.
````

## What does flux reveal?

Circulation measures how a field follows a closed path. **Flux** measures how much field crosses an oriented surface, which may be open or closed. Gauss's law concerns the special case of a **closed surface** bounding a volume. The two operations should not be confused.

For an electric dipole made from charges $+q$ and $-q$ with $q>0$, define the separation vector $\vec d$ to point from the negative charge to the positive charge. Its **electric dipole moment** is

$$
\vec p=q\vec d,\qquad [\vec p]=\mathrm{C\,m}.
$$

Any closed surface enclosing both charges contains zero net charge. Gauss's law therefore gives

$$
\oint_S\vec E\cdot d\vec A
=\frac{q+(-q)}{\epsilon_0}=0.
$$ (eq:electric-dipole-zero-flux)

This does not mean that the electric field vanishes. Electric field lines leave the positive charge and terminate on the negative charge. A smaller surface surrounding only one of the two charges would have nonzero electric flux.

For a magnetic field, the result is stronger:

$$
\boxed{
\oint_S\vec B\cdot d\vec A=0
}
\qquad\Longleftrightarrow\qquad
\boxed{
\vec\nabla\cdot\vec B=0.
}
$$ (eq:no-magnetic-monopoles)

The magnetic flux through **every** closed surface is zero. Magnetic field lines do not begin at a magnetic charge or end at an opposite one; they have no source or sink. For a circular current loop, the familiar returning field lines close through the loop; in more general fields, a field line need not form a closed curve. A surface enclosing a current loop has as much magnetic field entering it as leaving it.

```{figure} figures/electric_dipole_field.svg
:name: fig-electric-dipole-comparison
:width: 75%
:alt: Electric field lines around a positive charge above a negative charge. Arrows run from the positive to the negative charge, while the electric dipole moment points upward.

The **electric field** of two opposite charges in a plane containing the dipole axis. The dipole moment $\vec p$ points from $-q$ to $+q$, while field lines run from $+q$ to $-q$. A surface enclosing both charges has zero net flux, but a surface enclosing just one charge does not. Only representative field lines are shown.
```

## A current loop becomes a dipole

A planar current loop of area $A$ has magnetic dipole moment

$$
\boxed{
\vec m=IA\,\hat n,
}
$$ (eq:current-loop-magnetic-moment)

The moment has units $\mathrm{A\,m^2}$. Here $\hat n$ is fixed by the right-hand rule: curl the fingers of your right hand in the current direction and your thumb points along $\vec m$. For a compact coil with $N$ identical turns,

$$
\vec m=NIA\,\hat n.
$$

```{figure} figures/magnetic_dipole_field.svg
:name: fig-current-loop-dipole
:width: 75%
:alt: Magnetic field lines in a plane through the axis of a circular current loop viewed edge-on. The current leaves the page on the left and enters on the right. The field points upward through the loop and returns around its outside.

The **magnetic field** of a circular current loop, calculated from the Biot–Savart law. The wire intersects the plotted plane at the two orange symbols: $\odot$ denotes current out of the page and $\otimes$ current into it. Both the magnetic moment $\vec m$ and the field through the centre point upward. Field lines return around the outside without starting or ending on the wire. Far from the loop, this field approaches that of a point magnetic dipole. Line spacing is illustrative, not a calibrated measure of field strength.
```

Far from a loop whose dimensions are small compared with the observation distance $r$, the details of the wire become unimportant. The leading contribution to its field is

$$
\boxed{
\vec B(\vec r)
=\frac{\mu_0}{4\pi r^3}
\left[
3(\vec m\cdot\hat r)\hat r-\vec m
\right].
}
$$ (eq:magnetic-dipole-field-current-loop)

This is the magnetic dipole field. It decreases as $1/r^3$, faster than the $1/r^2$ field of an isolated electric charge or point mass.

Now compare it with the far field of an electric dipole with dipole moment $\vec p$:

$$
\vec E(\vec r)
=\frac{1}{4\pi\epsilon_0r^3}
\left[
3(\vec p\cdot\hat r)\hat r-\vec p
\right].
$$ (eq:electric-dipole-field-comparison)

The electric and magnetic dipole expressions have the same vector structure. To understand that shared pattern, we will read and sketch the magnetic expression, then transfer the result to the electric dipole. With the dipole at the origin, $\hat r=\vec r/r$ describes the observation direction and is dimensionless. The distance dependence is in the factor $r^{-3}$.

### Read the vector expression as instructions

Use the magnetic moment $\vec m$ for the construction below; replacing it by the electric moment $\vec p$ gives the same vector instructions. Focus on the bracket:

$$
3\underbrace{(\vec m\cdot\hat r)}_{\text{signed scalar projection}}
\underbrace{\hat r}_{\text{radial direction}}
-\underbrace{\vec m}_{\text{a second vector}}.
$$

The first occurrence of $\hat r$ is inside a dot product. It measures how strongly the moment points along the observation direction: $\vec m\cdot\hat r=m\cos\theta$, where $m=|\vec m|$. It changes the **signed size** of the first term, not its units. The second $\hat r$ turns this scalar into a radial vector. If the scalar is negative, this vector points inward. Finally, subtract $\vec m$ as a vector; the resulting field need not be radial.

### Predict the symmetry, then find it in the mathematics

Picture a circular current loop centred at the origin, with $\vec m=m\hat z$ and $m>0$. Rotate the loop about the $z$ axis. Its shape and current distribution are unchanged, so its magnetic field pattern must rotate into itself. There is no preferred azimuth around the axis. This is **axial symmetry**: the pattern repeats around the axis, although the field need not point along it. The ideal dipole inherits this symmetry. A loop of a different shape need not have this exact symmetry nearby, even though its leading dipole field does far away.

An electric pair with its two charges on the $z$ axis also stays unchanged when rotated about that axis. We therefore expect the same axial symmetry for its electric field, with $\vec p$ defining the axis.

The formula describes the same symmetry. At fixed $r$ and polar angle $\theta$, the projection $\vec m\cdot\hat r=m\cos\theta$ is independent of the azimuth $\varphi$. Rotating the observation point around $\vec m$ rotates $\hat r$ and the field arrow together, preserving the field's magnitude and its orientation relative to the local radial direction. The Cartesian components need not stay unchanged.

The formula tells us something else: $\vec B$ is a combination of $\hat r$ and $\vec m$, so it lies in the plane containing the observation point and the moment axis. For this dipole there is **no azimuthal field component**. This follows from the vector expression, not from axial symmetry alone. We can therefore study the field in any plane containing $\vec m$, then rotate that pattern around the axis to reconstruct the three-dimensional field.

### Build an angular sketch in the $x$–$z$ plane

Choose the $x$–$z$ plane and fix the observation distance at $r=R$, much farther from the origin than the size of the loop. First work on the half-plane $x\geq0$, where

$$
\hat r=\sin\theta\,\hat x+\cos\theta\,\hat z,
\qquad 0\leq\theta\leq\pi.
$$

Thus $\theta$ increases from the positive $z$ axis, through the positive $x$ axis, to the negative $z$ axis. Keeping $R$ fixed separates **changes with angle** from **decay with distance**.

```{admonition} From vector instructions to a field sketch
:class: exercise

1. Draw a circle of radius $R$ centred at the dipole, with $z$ upward and $x$ to the right. Draw $\vec m$ at the origin. Mark the five points on the right semicircle at $\theta=0,\pi/4,\pi/2,3\pi/4,\pi$.
2. At each point, first calculate the signed scalar $s=\vec m\cdot\hat r$. On a separate small construction sketch, add the vectors $3s\hat r$ and $-\vec m$ head to tail. Which occurrence of $\hat r$ sets the signed size, and which sets the radial direction?
3. Transfer each resulting field arrow to its observation point on the circle. Use **one common arrow scale**: the factor $\mu_0/(4\pi R^3)$ is the same at every point. Compare axial, equatorial and oblique arrows. Do not join the arrow tips: the circle samples the field and is not itself a field line.
4. Imagine rotating the right semicircle and all its field arrows by half a turn about $z$. Complete the left semicircle. Which Cartesian component changes sign? Then describe what a full rotation produces in three dimensions.
5. Draw a second observation circle of radius $2R$. At corresponding angles, which arrow directions change and what happens to their lengths? Explain how your two sketches separate angular structure from radial decay.
6. Return to the electric dipole expression, with $\vec p=p\hat z$. Can you reuse the arrow pattern? Identify what must change in the overall scale and what remains the same. For a finite charge pair, how large must $R$ be compared with the charge separation?
```

```{admonition} Check the sketch and read the pattern
:class: dropdown

Let $B_* = \mu_0m/(4\pi R^3)$. The vector instructions give

$$
\frac{\vec B(R,\theta)}{B_*}
=3\cos\theta\bigl(\sin\theta\,\hat x+\cos\theta\,\hat z\bigr)-\hat z
=3\sin\theta\cos\theta\,\hat x+(3\cos^2\theta-1)\hat z.
$$

Use these values to check your arrows:

| $\theta$ | $B_x/B_*$ | $B_z/B_*$ |
|---|---|---|
| $0$ | $0$ | $2$ |
| $\pi/4$ | $3/2$ | $1/2$ |
| $\pi/2$ | $0$ | $-1$ |
| $3\pi/4$ | $-3/2$ | $1/2$ |
| $\pi$ | $0$ | $2$ |

On the negative axis, keep both minus signs: $(\vec m\cdot\hat r)\hat r=(-m)(-\hat z)=m\hat z$. The axial field points along $+\hat z$ at both ends: outward at the positive end and inward at the negative end. Its magnitude is twice the equatorial magnitude. At the oblique points the first contribution is radial, but the final field is not.

A half-turn about $z$ maps the right semicircle to the left, reversing $B_x$ while preserving $B_z$. A full rotation sweeps out a sphere of observation points and their field arrows. Repeating at other radii describes the external dipole field throughout space. At $2R$, every arrow has the same direction as at the corresponding point on $R$, but one eighth of its length.

For the electric dipole, use $E_*=p/(4\pi\epsilon_0R^3)$ in place of $B_*$. The table then gives $E_x/E_*$ and $E_z/E_*$ without changing any entries. For two separated charges this is a far-field approximation, requiring $R$ much larger than their separation.
```

### The same dipole pattern, different sources

The sketch lets us interpret the comparison between the **electric and magnetic dipole fields** above. With their moments pointing along the same axis, both have the same angular pattern: the axial field is twice as strong as the equatorial field at the same radius, and the field at a fixed angle decreases as $r^{-3}$. Replacing $\mu_0m/(4\pi)$ by $p/(4\pi\epsilon_0)$ changes the overall scale, while preserving the arrow directions and relative lengths.

This shared dipole pattern describes the leading far field of both the charge pair and the current loop. It does not make their sources interchangeable. Returning to the flux argument, we can summarize the distinction:

| Electric dipole | Magnetic dipole |
|---|---|
| Two separated charges, $+q$ and $-q$ | A closed electric current |
| Field lines begin and end on charges | Field lines have no sources or sinks |
| A surface around one charge can have nonzero flux | Every closed surface has zero magnetic flux |
| $\vec\nabla\cdot\vec E=\rho_q/\epsilon_0$ | $\vec\nabla\cdot\vec B=0$ |

Close to the sources, the distinction becomes visible again. Near either electric charge, that charge's field dominates; near the current loop, the field depends on the wire's size and shape. Neither exact near field is described by the ideal dipole expression. Far away, the dipole moment captures their leading spatial pattern. This is why we can use the same mathematical description for Earth's large-scale internal magnetic field without imagining two magnetic charges or a literal permanent bar magnet inside Earth.

```{admonition} Read the source and the field
:class: exercise

1. Why does zero electric flux through a surface enclosing an electric dipole not imply $\vec E=\vec 0$ on that surface?
2. How is zero magnetic flux through every closed surface a stronger statement?
3. Which properties of a small current loop remain visible far away, and which details disappear into the dipole approximation?
```


## Outside the currents: the same scalar-potential language

For the electric dipole, we already know another way to describe the field: add the two charge potentials and take the negative gradient. Can we also describe the magnetic dipole pattern we have just sketched with a scalar potential? The current loop's nonzero magnetic circulation means we must first specify where that description is valid.

Imagine a sphere of radius $R_s$ enclosing the complete current system, whether a small coil or the internal sources of Earth's field. Consider its field only in the exterior domain $r>R_s$, using the magnetostatic vacuum approximation. There are no currents belonging to this model in the exterior, so

$$
\vec\nabla\times\vec B_{\mathrm{int}}=\vec 0.
$$

The exterior of a sphere in **three dimensions** is simply connected: every closed path can be contracted to a point while remaining outside the sphere. A path that appears to surround Earth in a flat drawing can move out of that plane. Thus the domain permits a single-valued scalar potential:

$$
\boxed{\vec B_{\mathrm{int}}=-\vec\nabla\Psi_m.}
$$ (eq:magnetic-scalar-potential-convention)

Combine this with $\vec\nabla\cdot\vec B_{\mathrm{int}}=0$ and we obtain

$$
\boxed{\nabla^2\Psi_m=0,\qquad r>R_s.}
$$ (eq:magnetic-exterior-laplace)

We have arrived at the same Laplace equation used for gravity and electrostatics. The sources are different, but the strategy carries over: propose a potential, recover the field from its gradient, and check the equation and boundary conditions. We can therefore describe the dipole field we have just met by a scalar potential, before specializing to Earth.

This is a model of the **internal-source contribution**, not a claim that the actual space outside Earth contains no currents. Ionospheric and magnetospheric currents contribute additional fields to measurements. We keep those contributions separate when introducing the core dipole model.

### What does this potential mean?

Our convention is $\vec B=-\vec\nabla\Psi_m$, so $\Psi_m$ has units of **tesla-metres**, $\mathrm{T\,m}$. Adding a constant leaves the field unchanged. Unlike electric potential $V$, however, $\Psi_m$ is **not potential energy per unit charge**. It is a scalar representation of the magnetic field in the chosen domain; its gradient supplies direction and magnitude. The magnetic force on a moving test charge still requires $q\vec v\times\vec B$. A compass can experience a torque, but that does not turn $\Psi_m$ into its mechanical potential energy.

```{admonition} Optional: why the wire example is different
:class: dropdown

Outside an ideal straight wire, $\vec J=\vec0$ and $\vec\nabla\times\vec B=\vec0$, yet a path encircling the wire has circulation $\mu_0I$. Such a path cannot contract to a point without crossing the excluded wire. A single-valued scalar potential cannot describe the field throughout that entire domain.

Zero curl is a local statement. Simple connectedness is a sufficient additional condition for a globally single-valued potential. The spherical exterior used for the internal Earth model has this property; the exterior of an infinitely long wire does not.

As a check, sketch one path linking a current-carrying wire and another spanning a current-free surface. What circulation does Ampère's law assign to each?
```

```{admonition} Optional: a different potential convention
:class: dropdown

Some texts define a scalar potential for $\vec H$, rather than $\vec B$. In vacuum, $\vec B=\mu_0\vec H$. If $\vec H=-\vec\nabla V_m$, then our convention gives $\Psi_m=\mu_0V_m$, up to a constant. The units and prefactors therefore differ. Always check which field the negative gradient represents.
```

## The scalar potential of the dipole we just met

Choose zero potential at infinity. The ideal electric and magnetic dipole potentials are

$$
\boxed{V_{\mathrm{dip}}(\vec r)=\frac{1}{4\pi\epsilon_0}
\frac{\vec p\cdot\hat r}{r^2},\qquad
\Psi_{m,\mathrm{dip}}(\vec r)=\frac{\mu_0}{4\pi}
\frac{\vec m\cdot\hat r}{r^2}.}
$$ (eq:paired-dipole-potentials)

Taking their negative gradients gives the two vector fields above. These are **two descriptions of the same dipole**, not additional source models. For finite charge pairs or current loops, these are leading far-field approximations; an ideal point dipole is singular at the origin.

Align the polar axis with $\vec m$. Then

$$
\Psi_{m,\mathrm{dip}}=\frac{\mu_0m}{4\pi}\frac{\cos\theta}{r^2}.
$$

We can check the connection using the spherical gradient. With $C=\mu_0m/(4\pi)$,

$$
-\vec\nabla\Psi_{m,\mathrm{dip}}
=-\frac{\partial\Psi_{m,\mathrm{dip}}}{\partial r}\hat r
-\frac1r\frac{\partial\Psi_{m,\mathrm{dip}}}{\partial\theta}\hat\theta
=\frac{C}{r^3}\bigl(2\cos\theta\,\hat r+\sin\theta\,\hat\theta\bigr).
$$

To recognize the original vector formula, resolve the fixed moment into the local basis:
$\vec m=m\cos\theta\,\hat r-m\sin\theta\,\hat\theta$. Substituting it into $3(\vec m\cdot\hat r)\hat r-\vec m$ gives exactly these same radial and angular contributions. The compact vector formula and the component formula speak the same language in different coordinates.

## Why does a dipole decay faster?

Two actual electric charges make the cancellation visible. Write $k_{\mathrm e}=1/(4\pi\epsilon_0)$. Put $+q$ at $z=d/2$ and $-q$ at $z=-d/2$, with $q,d>0$, so $\vec p=qd\hat z$. At a point on the positive axis, $z=r>d/2$, their exact potential is

$$
V(r)=k_{\mathrm e}q\left(\frac{1}{r-d/2}-\frac{1}{r+d/2}\right)
=\frac{k_{\mathrm e}qd}{r^2-d^2/4}.
$$ (eq:charge-pair-axial-potential)

Far away, $r\gg d$, the two distances are almost equal. Each contribution separately is approximately $\pm k_{\mathrm e}q/r$: those leading terms **cancel**. Their smaller difference remains:

$$
V(r)\approx\frac{k_{\mathrm e}p}{r^2},
\qquad E_z=-\frac{dV}{dr}\approx\frac{2k_{\mathrm e}p}{r^3}.
$$

The extra decay is not caused by the charges becoming weaker. It arises because their effects become more nearly equal and opposite as the observation distance increases. Close to either charge, that charge dominates and its local inverse-distance potential and inverse-square field are apparent again.

```{admonition} Optional: read the cancellation in every direction
:class: dropdown

For $r\gg d$, first-order expansion gives

$$
\frac{1}{|\vec r\mp\vec d/2|}
\approx\frac1r\pm\frac{\vec d\cdot\hat r}{2r^2}.
$$

Subtracting removes the common $1/r$ term and leaves $\vec d\cdot\hat r/r^2$. Multiplication by $k_{\mathrm e}q$ recovers $V_{\mathrm{dip}}=k_{\mathrm e}(\vec p\cdot\hat r)/r^2$.

The angular factor matters: the potential is exactly zero on the equatorial plane of an equal opposite pair, although the field there is not zero. Compare decay along a direction where the quantity being plotted is nonzero.
```

For magnetism, this is an analogy for the **external pattern**, not evidence for two physical magnetic charges. A localized current system has no magnetic monopole contribution. Its first possible surviving term is a dipole, with $r^{-2}$ potential and $r^{-3}$ field. If its net dipole moment also cancels, still faster decay is possible.

Explore {doc}`dipole_explorer` to separate the individual contributions and their sum. Then try {ref}`the opposing-dipoles exercise <sec:opposing-dipoles>`: can the same cancellation argument remove the dipole term too?

## Carry this potential into the Earth model

The next section does not introduce a new kind of potential. It uses the dipole expression above with a strength and orientation chosen for Earth's dominant internal field. Writing

$$
B_0a^3=\frac{\mu_0m}{4\pi}
$$

turns it into $\Psi_m=B_0a^3\cos\theta/r^2$. In {doc}`dipole_model` we check that this same potential satisfies Laplace, recover its field, and ask whether it matches Earth's surface boundary data.
