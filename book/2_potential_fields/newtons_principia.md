# Newton's Principia

In 1687, Isaac Newton published the *Philosophiae Naturalis Principia Mathematica*, usually called the *Principia*. It marks a key moment in the history of physics: Newton showed that the motion of objects on Earth and the motion of planets in the sky could be described by the same mathematical laws. At that time, Kepler's laws provided strong empirical evidence for the regularity of planetary motion, but the physical principles needed to explain that regularity were still missing.

Johannes Kepler had summarized planetary motion in three empirical laws. These laws described what the planets do, but not why they move that way. Newton's decisive step was to connect the observed motion to a law of force.

```{note}
Kepler's three laws are included here only for historical completeness:

1. Planets move around the Sun in ellipses, with the Sun at one focus.
2. The line from the Sun to a planet sweeps out equal areas in equal times.
3. The square of a planet's orbital period is proportional to the cube of the semi-major axis of its orbit ($T^2 \propto a^3$).
```

```{figure} figures/principia_book1_plate6_figure1.png
:name: principia-book1-plate6-figure1
:width: 70%

Newton's diagram for Book I, Plate 6, Figure 1 of Andrew Motte's 1729 English translation of the *Principia*. It is part of Newton's geometric treatment of motion under a force directed toward a centre. Source: Wikimedia Commons, public domain.
```

An important clue was already available. Christiaan Huygens had analysed uniform circular motion and related it to an acceleration directed toward the centre. In modern notation, the magnitude of this centripetal acceleration is

$$
a_c = \frac{v^2}{r} = \frac{4\pi^2 r}{T^2}.
$$

For a circular orbit, the orbital radius is also its semi-major axis. Combining this result with Kepler's third law, $T^2 \propto r^3$, gives

$$
  a_c \propto \frac{1}{r^2}.
$$

The acceleration required to keep a planet in a circular orbit therefore decreases with the square of its distance from the Sun. This argument does not yet establish universal gravitation, and real planetary orbits are elliptical, but it reveals the inverse-square dependence that Newton would develop much more fully.

In 1684, shortly before writing the *Principia*, Newton set out an early version of this connection in *De Motu Corporum in Gyrum* (*On the Motion of Bodies in an Orbit*). There he studied motion under centripetal forces and related laws of force to the orbits they produce. In the *Principia*, he developed these ideas into a much broader account of motion and universal gravitation.

Newton's formulation differs from the way we write the law today. The *Principia* expresses the inverse-square character of gravity geometrically and relates gravitational attraction to the amount of matter in the interacting bodies, but it does not introduce the modern gravitational constant $G$. In modern scalar notation, the magnitude of the gravitational force between two point masses is

$$
  F = G\frac{Mm}{r^2}.
$$

Here $M$ and $m$ are the two masses, $r$ is the distance between them, and $G$ is the gravitational constant. This compact equation is a later formulation of Newton's physical idea. It gives only the magnitude of the force; its direction must be included separately.

If we place the mass $M$ at the origin, the force on a mass $m$ at position $\vec{r}$ is

$$
  \vec{F}(\vec{r}) = -G\frac{Mm}{r^2}\hat{r}.
$$ (eq:two-body-gravity-force)

The minus sign tells us that the force points opposite to $\hat{r}$: gravity pulls the mass inward, toward the origin. Equation {eq}`eq:two-body-gravity-force` is already a field description. At every point in space, it tells us what force would act on the mass $m$ if it were placed there. Equivalently, we can define the gravitational field $\vec{g}=\vec{F}/m$, which does not depend on the chosen test mass.

The *Principia* was written mostly in the language of geometry, not in the modern vector-calculus notation we use today. In this course we will translate Newton's physical idea into the language of fields:

- a force field assigns a vector to each point in space;
- work is obtained by integrating the force along a path;
- for gravity, that work depends only on the starting and ending positions;
- this allows us to describe the field using a scalar potential.

This provides a bridge from Newton's mechanics to potential fields. The physics begins with forces and motion, while the mathematics leads us toward line integrals, gradients, and scalar functions.

## The extended spherical Earth

Equation {eq}`eq:two-body-gravity-force` describes the force between two *point masses*. It seems reasonable to approximate an extended body as a point when we observe it from a distance much greater than its size. It is far less obvious that the same expression should apply close to the body, for example to a satellite in low Earth orbit.

We can formulate the extended-body problem by dividing the Earth into infinitesimal mass elements and adding their contributions. Let $\vec{r}$ be the position at which we evaluate the force, let $\vec{r'}$ locate a mass element inside the Earth, and let $\rho(\vec{r'})$ be the mass density there. Since $dm'=\rho(\vec{r'})\,dV'$, the total force on a test mass $m$ is

$$
\vec{F}(\vec{r})
=
-Gm
\int_V \rho(\vec{r'}) \frac{\vec{r}-\vec{r'}}{|\vec{r}-\vec{r'}|^3}\,dV'.
$$ (eq:extended-body-gravity-force)

Each element pulls the test mass toward $\vec{r'}$. The integral appears straightforward, but evaluating it directly for every point outside an extended body can be a substantial calculation. We will come back to the problem described by Equation {eq}`eq:extended-body-gravity-force` later in the course.

Dividing by the mass $m$ of the object being pulled by the Earth gives us a relation between the mass distribution of the Earth, $\rho(\vec{r'})$, and the gravitational vector field, $\vec{g}(\vec{r})$. This is an example of a **forward problem**:

$$
\rho(\vec{r'}) \quad \longrightarrow \quad \vec{g}(\vec{r}).
$$

Given a distribution of mass, we calculate the gravity field that it produces. In Earth science, however, we are often interested in the opposite direction. We can measure the gravity field, while the distribution of mass inside the Earth is not directly observable from those measurements. This leads to the **inverse problem**:

$$
\vec{g}(\vec{r}) \quad \longrightarrow \quad \rho(\vec{r'}).
$$

This direction is considerably more difficult. In general, many — if not most — inverse problems do not have a unique solution: different distributions of mass may produce the same observations.

```{admonition} Reading the mathematics
:class: tip

The geometric factor

$$
\frac{\vec{r}-\vec{r'}}{|\vec{r}-\vec{r'}|^3}
$$

may look unfamiliar, but we have already encountered the same construction. Since

$$
\hat{r}=\frac{\vec{r}}{|\vec{r}|},
$$

the point-mass force in Equation {eq}`eq:two-body-gravity-force` can also be written as

$$
\vec{F}(\vec{r})
=
-GMm\frac{\vec{r}}{|\vec{r}|^3}.
$$

The numerator supplies the direction, while the combination of numerator and denominator gives the inverse-square dependence. The extended-body expression uses exactly the same idea, but replaces $\vec{r}$ by the separation vector $\vec{r}-\vec{r'}$.

Try to read this new expression as a sentence:

- What point does $\vec{r}$ represent?
- What point does $\vec{r'}$ represent?
- From which point to which point does $\vec{r}-\vec{r'}$ point?
- Why does the denominator contain the third power of the distance, even though gravity is an inverse-square law?
- What role does the minus sign in front of the integral play?

Hint: introduce $\vec{R}=\vec{r}-\vec{r'}$ and compare the resulting expression directly with the point-mass force above. The goal is not only to manipulate the expression, but to read it as a compact description of the geometry and physics.
```

This was not merely a modern technical detail. The inverse-square law describes attraction between point masses, but the Earth, Moon, Sun, and planets are extended bodies. To apply his theory of gravitational attraction to real celestial bodies, Newton therefore had to determine how the attraction of an extended spherical body relates to the inverse-square law for individual particles.

In Book I, Section XII of the *Principia*, entitled *Of the attractive forces of spherical bodies*, Newton begins with a thin, uniform spherical shell and proves two remarkable results.

**Proposition 70.** A body located anywhere inside a uniform spherical shell experiences no net gravitational attraction from the shell.

This is not obvious. Away from the centre, the nearest part of the shell is closer and therefore pulls more strongly per unit mass. Newton showed geometrically that this is exactly compensated by the greater amount of material contributing from the more distant side.

**Proposition 71.** For a body located outside a uniform spherical shell, the gravitational attraction is exactly the same as if the entire mass of the shell were concentrated at its centre.

The importance of these results goes beyond a single shell. A spherically symmetric body whose density may vary with radius can be regarded as a collection of concentric uniform shells. Their contributions add, so outside a spherical Earth the gravitational field is

$$
\vec{g}(\vec{r})
=
-\frac{GM}{r^2}\,\hat{r},
\qquad r>R,
$$

exactly as if the entire mass of the Earth were concentrated at its centre.

Thus, treating the Earth as a point mass is not merely an approximation that improves with distance. Outside a perfectly spherically symmetric Earth, it is an exact consequence of the inverse-square law. This result justifies the gravitational field used in the examples that follow and gives us a concrete setting in which to introduce work and potential.

## Example: gravity inside and outside a thick shell

Consider a uniform spherical shell with inner radius $R_i$, outer radius $R_o$, density $\rho$, and total mass $M$. By symmetry, its gravitational field must be radial. Newton's shell results also tell us that only matter at radii smaller than the observation point contributes to the field there. The enclosed mass is therefore

$$
M_{\mathrm{enc}}(r)
=
\begin{cases}
0, & 0 \leq r < R_i,\\[4pt]
\dfrac{4\pi\rho}{3}\left(r^3-R_i^3\right), & R_i \leq r \leq R_o,\\[6pt]
M, & r>R_o.
\end{cases}
$$

The gravitational field follows immediately:

$$
\vec{g}(\vec{r})
=
-G\frac{M_{\mathrm{enc}}(r)}{r^2}\hat{r}.
$$

```{figure} figures/spherical_shell_field.png
:name: thick-spherical-shell-field
:width: 100%

The gravitational field of a uniform thick spherical shell. The field vanishes throughout the empty cavity, grows as progressively more mass is enclosed within the shell material, and decreases as $1/r^2$ outside the shell. Arrow direction and colour represent the direction and magnitude of $\vec{g}$. The figure is generated in the accompanying {doc}`spherical_shell_gravity` notebook.
```

The zero field in the cavity is especially striking: it holds everywhere inside the cavity, not only at its centre. Outside the shell, the field depends on the total mass $M$ but not on how that mass is distributed with radius, provided the distribution remains spherically symmetric.

### What if the mass distribution is not spherical?

To break the symmetry, imagine moving part of the shell's mass into two compact concentrations. In the example below, $0.82M$ remains in the uniform shell, while point-like masses $0.11M$ and $0.07M$ are placed at different locations within it. The total mass is still $M$, so any difference in the measured field must come from its distribution rather than its total amount.

```{figure} figures/spherical_shell_disturbance.png
:name: disturbed-spherical-shell-field
:width: 100%

A uniform shell and a disturbed shell with the same total mass. The disturbance changes both the direction and magnitude of the field. Measurements on a circle outside the shell acquire angle-dependent radial and tangential components; a uniform spherical shell would instead produce a constant radial component and no tangential component. The disturbances are intentionally exaggerated to make the effect visible. The figure is generated in the accompanying {doc}`spherical_shell_gravity` notebook.
```

The shell theorem no longer applies to the complete disturbed distribution. The field is not a function of $r$ alone, and knowing the total mass is not sufficient to predict it at finite distances. Conversely, variations in gravity measured at different positions can reveal departures from spherical symmetry and provide information about how mass is distributed.

There is an important limit to this conclusion. Far from any bounded mass distribution, the leading contribution approaches the field of a point mass containing the total mass, while the signatures of its internal structure become progressively weaker. Measurements made closer to the source retain more spatial detail, but they still do not generally determine a unique mass distribution without additional assumptions or information. This is precisely the promise and the difficulty of the inverse problem introduced above: gravity anomalies can constrain a hidden mass distribution without uniquely revealing it.
