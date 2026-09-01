# Density Anomalies and Gravity Observations

Poisson's equation connects the gravitational potential to the local mass density,

$$
\nabla^2\Phi=4\pi G\rho.
$$

Together with superposition, it also gives us a convenient way to construct potentials for bodies that are less symmetric than a complete sphere. We will use this to move from idealized density distributions towards a simple gravity-observation problem.

## An off-centre spherical cavity

Consider a uniform sphere of radius $R$ and density $\rho_0$, centred at the origin. A spherical cavity of radius $a$ is centred at the position $\vec d$, with

$$
|\vec d|+a<R,
$$

so that the cavity lies entirely inside the original sphere. For an observation point $\vec r$, define its distance from the centre of the cavity as

$$
s=|\vec r-\vec d|.
$$

We will reuse the potential of a uniform sphere. For a sphere of radius $b$, density $\rho$, and distance $s$ from its centre, with the potential chosen to vanish at infinity,

$$
\Phi_b(s;\rho)=
\begin{cases}
-2\pi G\rho\left(b^2-\dfrac{s^2}{3}\right), & s<b,\\[6pt]
-\dfrac{G M_b}{s}, & s\geq b,
\end{cases}
\qquad
M_b=\frac{4}{3}\pi b^3\rho.
$$ (eq:uniform-sphere-potential-general-centre)

```{admonition} Guided exercise: construct the cavity
:class: exercise

Rather than starting a new volume integral, construct the cavity using the principle of superposition.

1. Begin with the complete sphere of density $\rho_0$. What additional spherical density distribution, centred at $\vec d$, must you add so that the total density is zero for $s<a$?

2. Let $I_R(\vec r)$ equal one inside the original sphere and zero outside, and define $I_a(\vec r-\vec d)$ similarly for the cavity. Write the physical density $\rho(\vec r)$ in terms of these indicator functions.

3. Using Equation {eq}`eq:uniform-sphere-potential-general-centre`, write the potential as the superposition of two sphere potentials. The second sphere is a mathematical device for removing mass; the physical density in the cavity is zero, not negative.

4. Apply the Laplacian and use its linearity to verify Poisson's equation separately:

   - inside the cavity, $s<a$;
   - inside the material but outside the cavity;
   - outside the complete sphere.

5. Inside the cavity, both sphere potentials take their interior quadratic form. Show that their quadratic terms combine to give

   $$
   \vec g_{\mathrm{cavity}}
   =-\frac{4\pi G\rho_0}{3}\,\vec d.
   $$

   Is the field inside the off-centre cavity zero? Does it vary with position inside the cavity?
```

```{dropdown} Check the construction

The removed material can be represented by adding a sphere with density $-\rho_0$. The density and potential are therefore

$$
\rho(\vec r)
=\rho_0 I_R(\vec r)
-\rho_0 I_a(\vec r-\vec d)
$$

and

$$
\boxed{
\Phi(\vec r)
=\Phi_R(|\vec r|;\rho_0)
-\Phi_a(|\vec r-\vec d|;\rho_0)
}.
$$ (eq:off-centre-cavity-potential)

Consequently,

$$
\nabla^2\Phi
=4\pi G\rho_0
\left[I_R(\vec r)-I_a(\vec r-\vec d)\right]
=4\pi G\rho(\vec r).
$$

Inside the cavity the two contributions to the Laplacian cancel. In the remaining material only the complete-sphere contribution remains, while outside both spheres each contribution satisfies Laplace's equation.

Within the cavity,

$$
\vec\nabla\Phi
=\frac{4\pi G\rho_0}{3}
\left[\vec r-(\vec r-\vec d)\right]
=\frac{4\pi G\rho_0}{3}\vec d,
$$

so $\vec g=-\vec\nabla\Phi$ is uniform and points opposite to $\vec d$. The field vanishes only for a concentric cavity, $\vec d=\vec 0$.
```

## Different anomalies, the same exterior field

Now replace the empty cavity by a spherical region in which the density is increased from $\rho_0$ to $\rho_0+\Delta\rho$. Relative to the uniform background sphere, this region is a **density anomaly** with density contrast $\Delta\rho$ and anomalous mass

$$
\Delta M=\frac{4}{3}\pi a^3\Delta\rho.
$$ (eq:spherical-anomaly-mass)

The total potential is

$$
\Phi(\vec r)
=\Phi_R(|\vec r|;\rho_0)
+\delta\Phi(\vec r),
$$

where

$$
\delta\Phi(\vec r)
=\Phi_a(|\vec r-\vec d|;\Delta\rho).
$$

At every point outside the anomalous sphere, $s>a$, its potential and field are

$$
\boxed{
\delta\Phi(\vec r)=-\frac{G\Delta M}{|\vec r-\vec d|}
}
$$ (eq:spherical-density-anomaly-exterior-potential)

and

$$
\boxed{
\delta\vec g(\vec r)
=-G\Delta M
\frac{\vec r-\vec d}{|\vec r-\vec d|^3}
}.
$$ (eq:spherical-density-anomaly-exterior-field)

```{admonition} Exercise: indistinguishable spherical anomalies
:class: exercise

Consider two spherical anomalies with the same centre $\vec d$ but different radii $a_1$ and $a_2$.

1. Find the relation between $\Delta\rho_1$, $a_1$, $\Delta\rho_2$, and $a_2$ that gives both anomalies the same $\Delta M$.
2. Show that their potentials and gravity fields are identical at every point outside both anomalies.
3. Explain why measurements made outside the body cannot distinguish between these two density-radius combinations.
4. Could a measurement made inside one of the anomalous spheres distinguish them? Use Poisson's equation to support your answer.
```

This is a first example of **non-uniqueness** in gravity inversion: distinct density models can produce identical observations. The conclusion here is exact because the anomalies are spherical, have the same centre, and are observed from outside. For arbitrary disturbances, equal total mass alone is not sufficient to guarantee identical exterior fields; their geometry and distribution can contribute additional spatial structure.

## Coding exercise: observing the anomaly from different heights

We will now examine a spherical density anomaly buried at depth $D$ below Earth's surface. Since every observation point is outside the anomaly, Equation {eq}`eq:spherical-density-anomaly-exterior-field` tells us that only its anomalous mass $\Delta M$ and centre matter.

Place the anomaly beneath the point $\theta=0$ at

$$
\vec d=(0,R_{\mathrm E}-D),
$$

and place observations along a circular track at height $h$,

$$
\vec r(\theta,h)
=(R_{\mathrm E}+h)
\left(\sin\theta,\cos\theta\right).
$$

The radial unit vector is $\hat r=\vec r/|\vec r|$. We will compare the downward radial anomaly

$$
\delta g_{\mathrm{down}}
=-\delta\vec g\cdot\hat r
$$ (eq:downward-radial-gravity-anomaly)

at the surface, at a GOCE-like low-Earth orbit of $254\ \mathrm{km}$, and at a higher orbit.

````{admonition} Write and investigate the model
:class: exercise

Complete the function below and use it to calculate $\delta g_{\mathrm{down}}$ along the observation track. One microgal is $10^{-8}\ \mathrm{m\,s^{-2}}$.

```python
import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11          # m^3 kg^-1 s^-2
R_E = 6.371e6            # m
depth = 100e3            # m below the surface
delta_mass = 1.0e15      # kg

theta = np.deg2rad(np.linspace(-10, 10, 501))
heights = [0.0, 254e3, 500e3]


def downward_radial_anomaly(theta, height, delta_mass, depth):
    """Return the downward radial gravity anomaly in m/s^2."""
    orbit_radius = R_E + height

    # Construct the observation positions r(theta, height).
    # Construct the anomaly centre d.
    # Evaluate delta_g using Eq. (spherical-density-anomaly-exterior-field).
    # Project delta_g onto the local downward direction.
    raise NotImplementedError


distance_along_surface_km = R_E * theta / 1e3

for height in heights:
    anomaly = downward_radial_anomaly(
        theta, height, delta_mass, depth
    )
    plt.plot(
        distance_along_surface_km,
        anomaly / 1e-8,
        label=f"h = {height / 1e3:.0f} km",
    )

plt.xlabel("Distance from point above anomaly (km)")
plt.ylabel(r"Downward radial anomaly ($\mu$Gal)")
plt.legend()
plt.grid(True)
plt.show()
```

Use your results to answer the following questions:

1. How do the peak amplitude and horizontal width of the anomaly change with observation height?
2. Directly above the anomaly, show that the magnitude of the field is

   $$
   |\delta\vec g|=\frac{G|\Delta M|}{(D+h)^2}.
   $$

   Use this result to check the central value returned by your code.
3. By what factor is the central anomaly reduced between the surface and the GOCE-like orbit?
4. Choose two radius-density combinations with the same $\Delta M$. Confirm numerically that their exterior gravity curves overlap.
5. Repeat the calculation for several depths $D$. Which anomalies are most strongly affected by increasing the observation height?
````

````{dropdown} Hints for the implementation

Store the observation positions as an array with one row for each value of $\theta$. If `r` contains those positions and `d` is the anomaly centre, then

```python
separation = r - d
distance = np.linalg.norm(separation, axis=1)
```

The factor $|\vec r-\vec d|^3$ must be applied once for every observation point. `distance[:, None]` can be used to make a one-dimensional array broadcast across the two vector components.

To calculate the radial projection, construct `r_hat` and take a row-by-row dot product. For example, `np.sum(delta_g * r_hat, axis=1)` evaluates the dot product for every row.
````

The loss of amplitude and broadening of the anomaly with increasing height are the spatial-domain manifestation of the upward-continuation transfer function introduced in the previous section. Flying lower preserves more of the short-scale gravity signal, but, as GOCE demonstrated, it also makes atmospheric drag a much more serious engineering constraint {cite}`esa_goce_operations`.
