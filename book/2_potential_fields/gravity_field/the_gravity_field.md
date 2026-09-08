# The Gravity Field

Let us start by recalling that the gravitational force between two point masses is

$$
\vec{F}(\vec{r})
=-G\frac{Mm}{|\vec{r}-\vec{r'}|^3}(\vec{r}-\vec{r'})
=-G\frac{Mm}{|\vec{r}-\vec{r'}|^2}\hat{R}.
$$ (eq:two-body-gravity-general-origin)

Here $G$ is the gravitational constant ($G=6.6743\times10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}$), $M$ is the source mass at position $\vec{r'}$, and $m$ is the test mass at position $\vec{r}$. We have introduced the separation vector and its unit vector,

$$
\vec{R}=\vec{r}-\vec{r'},
\qquad
\hat{R}=\frac{\vec{R}}{|\vec{R}|}.
$$ (eq:gravity-separation-vector)

```{figure} figures/point_mass_gravity_geometry.svg
:name: point-mass-gravity-geometry
:width: 95%

Geometry of the gravitational interaction between a source mass $M$ at $\vec{r'}$ and a test mass $m$ at $\vec{r}$. The separation vector $\vec{R}=\vec{r}-\vec{r'}$ points from $M$ toward $m$, while the gravitational force on $m$ points in the opposite direction, back toward $M$. Copies of the unit vector $\hat{R}$ are drawn at $m$ and at the arbitrary coordinate origin $O$ to emphasize that a vector may be translated without changing its magnitude or direction.
```

The vector $\hat{R}$ points from the source mass $M$ toward the test mass $m$. The minus sign in Equation {eq}`eq:two-body-gravity-general-origin` therefore makes the gravitational force point back toward the source mass.

Dividing the force by the test mass gives the gravity field produced by $M$:

$$
\vec{g}(\vec{r})
=\frac{\vec{F}(\vec{r})}{m}
=-G\frac{M}{|\vec{r}-\vec{r'}|^3}(\vec{r}-\vec{r'}).
$$ (eq:point-mass-gravity-general-origin)

```{admonition} Interpreting the mathematics
:class: tip

Although $\vec{r}$ and $\vec{r'}$ depend on where we place the coordinate origin, the gravity field depends only on their difference. If we translate the origin by a constant vector $\vec{a}$, the two position vectors become

$$
\vec{r}_{\mathrm{new}}=\vec{r}-\vec{a},
\qquad
\vec{r'}_{\mathrm{new}}=\vec{r'}-\vec{a}.
$$

Their difference is unchanged:

$$
\vec{r}_{\mathrm{new}}-\vec{r'}_{\mathrm{new}}
=(\vec{r}-\vec{a})-(\vec{r'}-\vec{a})
=\vec{r}-\vec{r'}.
$$

The choice of origin is therefore irrelevant to the physical separation between the masses and to the force between them.

It is also worth reading carefully how the two forms of the force in Equation {eq}`eq:two-body-gravity-general-origin` are related. A unit vector is obtained by dividing a vector by its magnitude:

$$
\hat{R}=\frac{\vec{R}}{|\vec{R}|}.
$$

Consequently,

$$
\frac{1}{|\vec{R}|^2}\hat{R}
=\frac{1}{|\vec{R}|^2}\frac{\vec{R}}{|\vec{R}|}
=\frac{\vec{R}}{|\vec{R}|^3}.
$$

The final denominator contains a third power because the numerator is a vector with magnitude $|\vec{R}|$. The complete expression still has an inverse-square magnitude: one factor of $|\vec{R}|$ supplies direction through the unit vector, while the remaining two describe how the field strength decreases with distance.
```

For a spherical Earth and assuming that the density depends only on the distance to its center, the near-surface gravitational acceleration is given by

$$
g = \frac{GM_{\mathrm E}}{R_{\mathrm E}^2} \approx 9.8\,\mathrm{m\,s^{-2}}
$$

for an Earth mass $M_{\mathrm E}\approx5.97\times10^{24}\,\mathrm{kg}$ and a mean Earth radius $R_{\mathrm E}\approx6.37\times10^6\,\mathrm{m}$. The unit **gal** ($\mathrm{Gal}$) is named in honour of Galileo and is commonly used for gravity measurements and anomalies, usually as the milligal ($\mathrm{mGal}$) or microgal ($\mathrm{\mu Gal}$). One gal is

$$
1\,\mathrm{Gal}=1\,\mathrm{cm\,s^{-2}}=10^{-2}\,\mathrm{m\,s^{-2}}\approx10^{-3}g.
$$

In 1798, Henry Cavendish used a torsion balance to measure the very small gravitational attraction between lead spheres. His original aim was to determine the mean density of the Earth, but the experiment can be expressed in modern terms as an early determination of $G$ {cite}`nist_measure_strength_gravity`. Subsequent measurements established that $g$ varies with location. Its smooth, large-scale variation with latitude reflects both Earth's oblate shape and the centrifugal effect of its rotation. Geodesists describe this expected variation using a reference ellipsoid. Differences between observed gravity and the corresponding reference value are **gravity anomalies**; these residual variations contain information about topography and subsurface mass-density variations and also contribute to the determination of the geoid {cite}`noaa_geoid_modeling`.

## Gravitational potential and superposition

We introduced the gravitational potential of a point mass earlier in Equation {eq}`eq:point-mass-gravitational-potential`. Placing a source mass $M_1$ at an arbitrary position $\vec{r'}_1$, rather than at the origin, gives the gravitational potential per unit mass

$$
\Phi_1(\vec{r})
=-\frac{G M_1}{|\vec{r}-\vec{r'}_1|},
$$ (eq:point-mass-potential-general-origin)

where we have chosen $\Phi_1\rightarrow 0$ as $|\vec{r}|\rightarrow\infty$.

For a conservative gravity field, the potential difference between two points is

$$
\Phi(\vec{r})-\Phi(\vec{r}_0)
=-\int_{\vec{r}_0}^{\vec{r}}\vec{g}\cdot\mathrm{d}\vec{s}.
$$ (eq:gravity-potential-difference)

Suppose now that two point masses produce fields $\vec{g}_1$ and $\vec{g}_2$. Since integration is a linear operation,

$$
-\int_{\vec{r}_0}^{\vec{r}}(\vec{g}_1+\vec{g}_2)\cdot\mathrm{d}\vec{s}
=-\int_{\vec{r}_0}^{\vec{r}}\vec{g}_1\cdot\mathrm{d}\vec{s}
-\int_{\vec{r}_0}^{\vec{r}}\vec{g}_2\cdot\mathrm{d}\vec{s}.
$$

The potential of the combined field is therefore the sum of the two individual potentials, up to an additive constant. Choosing zero potential at infinity gives

$$
\Phi(\vec{r})
=-G\left(
\frac{M_1}{|\vec{r}-\vec{r'}_1|}
+\frac{M_2}{|\vec{r}-\vec{r'}_2|}
\right).
$$ (eq:two-point-mass-gravitational-potential)

The gradient is also linear. The gravity field obtained from this potential is therefore

$$
\begin{aligned}
\vec{g}(\vec{r})
&=-\vec{\nabla}\Phi(\vec{r}) \\
&=-G\left[
M_1\frac{\vec{r}-\vec{r'}_1}{|\vec{r}-\vec{r'}_1|^3}
+M_2\frac{\vec{r}-\vec{r'}_2}{|\vec{r}-\vec{r'}_2|^3}
\right].
\end{aligned}
$$ (eq:two-point-mass-gravity-field)

This is the **superposition principle**: each source contributes independently to the potential and to the gravity field. The gravitational force on a test mass $m$ is then $\vec{F}=m\vec{g}$.

The same reasoning extends to a continuous mass distribution. We divide the source into infinitesimal masses $\mathrm{d}m'=\rho(\vec{r'})\,\mathrm{d}V'$, where $\rho(\vec{r'})$ is the mass density and the prime indicates a source position. Replacing the discrete sum by an integral gives

$$
\Phi(\vec{r})
=-G\int_V
\frac{\rho(\vec{r'})}{|\vec{r}-\vec{r'}|}\,\mathrm{d}V'.
$$ (eq:continuous-mass-gravitational-potential)

Taking its gradient gives the corresponding gravity field,

$$
\vec{g}(\vec{r})
=-G\int_V \rho(\vec{r'})
\frac{\vec{r}-\vec{r'}}{|\vec{r}-\vec{r'}|^3}\,\mathrm{d}V'.
$$ (eq:continuous-mass-gravity-field)

This is the gravity-field form of the extended-body force introduced in Equation {eq}`eq:extended-body-gravity-force`: dividing that force by the test mass leaves a field determined by the location and density of all the source mass. For a bounded distribution, the expressions above use the natural convention that the potential approaches zero infinitely far from the source.
