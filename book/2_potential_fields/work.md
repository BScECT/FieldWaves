# Work

As you should recall from previous courses, the work performed by a force is given by the product of the force applied on an object and the distance traveled by the object in the direction of the force (assuming the force is constant for now). For a force pointing in the $\hat{x}$ direction and a displacement $\Delta x$ also in the $x$ direction, the work would be given by

$$
  W = F_x \cdot \Delta x
$$

This, of course, doesn't work for a non constant field and an arbitrary trajectory. What we can do in this case is consider the small increment of work associated to a small, differential, segment of the trajectory

$$
  dW = \vec{F}(x,y,z) \cdot \vec{ds}.
$$

```{admonition} Example: differential work
For a small displacement in the $\hat{x}$ direction, the displacement vector is

$$
  \vec{ds} = dx \, \hat{x}.
$$

If the force is $\vec{F} = F_x \hat{x}$ at that point, then the differential work is

$$
  dW = \vec{F} \cdot \vec{ds} = F_x \, dx.
$$

For example, if $F_x = 4~\mathrm{N}$ and $dx = 0.01~\mathrm{m}$, then

$$
  dW = 4 \times 0.01 = 0.04~\mathrm{J}.
$$
```

The total work can be calculated integrating $dW$ following the trajectory of the path:

$$
  W = \int_s dW = \int_s \vec{F}(x,y,z) \cdot \vec{ds}
$$

```{admonition} Example: work in Earth's gravity field
Consider a spacecraft of mass $m$ moving from Earth's surface to a circular orbit at radius $r_o$. Earth's gravitational force is radial:

$$
  \vec{F}_g(r) = -\frac{GMm}{r^2}\hat{r},
$$

where $M$ is Earth's mass and $G$ is the gravitational constant. A small displacement in spherical coordinates can be written as

$$
  \vec{ds} = dr\,\hat{r} + r\,d\theta\,\hat{\theta}
  + r\sin\theta\,d\phi\,\hat{\phi}.
$$

The differential work done by gravity is therefore

$$
  dW_g = \vec{F}_g \cdot \vec{ds}
       = -\frac{GMm}{r^2}dr.
$$

Only the radial displacement $dr$ contributes. Sideways motion along a circular path has $dr = 0$, so gravity does no work during that part of the motion.

The work done by gravity from Earth's radius $R_E$ to the orbit radius $r_o$ is

$$
  W_g = \int_{R_E}^{r_o} -\frac{GMm}{r^2}\,dr
      = GMm\left(\frac{1}{r_o} - \frac{1}{R_E}\right).
$$

The negative sign tells us that gravity removes energy as the spacecraft moves outward. The external work needed to lift it slowly to orbit is the opposite:

$$
  W_{\mathrm{ext}} = GMm\left(\frac{1}{R_E} - \frac{1}{r_o}\right).
$$
```

```{figure} figures/earth_gravity_work.png
:name: earth-gravity-work-paths
:width: 100%

Several paths from the same starting point $P_0$ to the same endpoint $P_1$ in Earth's gravity field. The cumulative line integral differs along the way, but all paths end at the same value because the gravitational field is conservative.
```
