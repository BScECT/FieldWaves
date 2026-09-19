# Magnetic Forces and Earth's Protective Field

We have described Earth's field with a potential and its gradient. Return now to a physical question: what does that field do to a charged particle arriving from space? This brings us back to the cross product and to the distinction between changing a velocity's **direction** and changing its **magnitude**.

## Read the Lorentz force

The **Lorentz force** on a particle of charge $q$ is

$$
\vec F=q\left(\vec E+\vec v\times\vec B\right).
$$ (eq:lorentz-force-full)

The electric contribution acts even on a stationary charge. The magnetic contribution depends on motion and is perpendicular to both $\vec v$ and $\vec B$. For positive $q$, use the right-hand rule for $\vec v\times\vec B$; negative $q$ reverses the force.

To isolate magnetic deflection, first neglect electric forces, collisions and gravity, and take a locally uniform, steady field. Decompose the velocity into parts parallel and perpendicular to the field:

$$
\vec v=\vec v_{\parallel}+\vec v_{\perp},
\qquad
\vec F_{\mathrm B}=q\,\vec v_{\perp}\times\vec B.
$$

The parallel motion is unaffected. The perpendicular motion is continually turned. A particle moving exactly along the field has no magnetic force, even if the field is strong.

```{admonition} Sketch the force before the trajectory
:class: exercise

Draw a local field $\vec B=B\hat z$ pointing out of the page and an initial velocity $\vec v=v\hat x$ pointing right. Sketch the initial magnetic force for a positive charge and for a negative charge. Then draw the first part of each trajectory. What changes if the initial velocity is instead along $\hat z$?
```

```{admonition} Check
:class: dropdown

Since $\hat x\times\hat z=-\hat y$, the positive charge initially turns downward and the negative charge upward. In this uniform field their perpendicular trajectories are circles, traversed in opposite senses. Motion purely along $\hat z$ remains straight.
```

## Deflection without magnetic work

The instantaneous rate of work by the magnetic force is

$$
\frac{dK}{dt}=\vec F_{\mathrm B}\cdot\vec v
=q(\vec v\times\vec B)\cdot\vec v=0.
$$

The particle keeps its speed while its direction changes. It can therefore miss Earth without first losing its kinetic energy. This is the physical distinction between deflecting a particle and absorbing it.

For a nonrelativistic particle of mass $m_{\mathrm p}$, the perpendicular motion supplies its own familiar interpretation: the magnetic force provides centripetal acceleration. Equating their magnitudes gives

$$
|q|v_{\perp}B=\frac{m_{\mathrm p}v_{\perp}^2}{r_{\mathrm g}},
\qquad
r_{\mathrm g}=\frac{m_{\mathrm p}v_{\perp}}{|q|B}.
$$ (eq:particle-gyroradius)

The **gyroradius** $r_{\mathrm g}$ is smaller for a stronger field and larger for greater perpendicular momentum at fixed charge. Adding constant parallel motion turns the circular path into a helix. The particle trajectory is not itself a magnetic field line.

```{admonition} A local scale estimate
:class: exercise

A proton has $m_{\mathrm p}=1.67\times10^{-27}\,\mathrm{kg}$ and $q=1.60\times10^{-19}\,\mathrm C$. Take $v_{\perp}=10^6\,\mathrm{m\,s^{-1}}$ and a uniform field $B=30\,\mu\mathrm T$. Estimate its gyroradius. How does it change if $B$ is halved? What must be true about the field's variation across the orbit for this local calculation to be useful?
```

```{admonition} Check and limit the interpretation
:class: dropdown

The radius is about $350\,\mathrm m$; halving $B$ doubles it. The field should vary little over an orbit. This is a local estimate at an Earth-like field strength, not a calculation of whether an incoming proton reaches the ground. The actual field strength and direction vary along its trajectory.

For relativistic particles the momentum replaces $m_{\mathrm p}v_{\perp}$: $r_{\mathrm g}=p_{\perp}/(|q|B)$. Here $p_{\perp}$ denotes particle momentum, not the electric dipole moment used earlier.
```

## What protection does Earth receive?

The solar wind carries charged particles, and energetic particle radiation also comes from solar events and from outside the Solar System. Earth's **magnetosphere** alters which particles can reach its surroundings. Solar-wind interactions compress the field on the Sun-facing side and stretch it into a tail, so the large-scale outer field is more complicated than our isolated core dipole {cite}`nasa_space_radiation_environment`.

Magnetic deflection provides part of Earth's protection; the atmosphere absorbs and interacts with much of the particle radiation that gets through. Protection is incomplete: some particles penetrate, and others become trapped in the radiation belts {cite}`nasa_space_radiation_environment,nasa_radiation_protection_mars`. Strong fields do not guarantee exclusion of every particle; momentum, direction and the global field geometry matter.

```{admonition} Charged particles and electromagnetic radiation
:class: note

The mechanism here acts on **charged particles**. It does not directly block sunlight, ultraviolet light or X-rays through $q\vec v\times\vec B$: photons have no electric charge. Also, magnetic force does no work, but electric fields present in the magnetosphere can change particle energies. Our local magnetic-only calculation isolates one part of a coupled physical system.
```

The reusable mathematics is the connection between a cross product, perpendicular force and turning motion. The scalar magnetic potential helps us calculate $\vec B$ in suitable regions; the Lorentz force tells us how a moving charge responds to that field.
