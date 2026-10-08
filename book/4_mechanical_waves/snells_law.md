(subsec-basickinematics)=
# The interface: Snell's law, refraction and reflection

So far, we discussed waves in a material which everywhere had the same constant wave velocity. When we include a boundary between two different materials, some energy is bounced back, or reflected, and some energy is going through to the other medium. It is nice to perform Huygens' principle graphically on such a configuration to see how the wave field moves forward (propagates), especially into the second medium. From this picture, we could also derive the ray concept. In this discussion, we will only consider the notion of rays. A basic notion in the ray concept, is Snell's law. Snell's law is a fundamental relation in the seismic wave fields. It tells us the relation between angle of incidence of a wave and velocity in two adjacent layers (see {numref}`fig-snellslaw`).

```{figure} figures/snell.png
:name: fig-snellslaw
:width: 70%

Transmission through a boundary (for deriving Snell's law).
```

$AA'A''$ is part of a plane wave incident at angle $\theta_1$ to a plane interface between medium 1 of velocity $c_1,$ and medium 2 of velocity $c_2.$ Velocities $c_1$ and $c_2$ are constant. In a time $t$ the wave front $AA'$ moves to the position $BB'$ and the movement is normal to the wave front. Then, the time $t$ it takes to travel from $A'$ to $B'$ in medium 1 is equal to the time from $A$ to $B$ in medium 2, so

$$
t = \frac{A'B'}{c_1} = \frac{AB}{c_2}
$$

Considering the two triangles, this may be written as:

$$
t = \frac{AB' \sin \theta_1}{c_1} = \frac{AB' \sin \theta_2}{c_2}
$$

Hence,

$$
\frac{\sin \theta_1}{c_1} = \frac{\sin \theta_2}{c_2}
$$

which is Snell's law for transmission through a boundary between two layers with different velocities. So far, we have taken general velocities $c_1$ and $c_2$. However, in a solid, two velocities exist, namely P- and S-wave velocities. Generally, when a P-wave is incident on a boundary, it can transmit as a P-wave into the second medium, but also as a S-wave. So in the case of the latter, Snell's law reads:

$$
\frac{\sin \theta_P}{c_P} = \frac{\sin \theta_S}{c_S}
$$

where $c_P$ is the P-wave velocity, and $c_S$ the S-wave velocity. The same holds for reflection: a P-wave incident on the boundary generates a reflected P-wave and a reflected S-wave. Finally, the same holds for an incident S-wave: it generates a reflected P-wave, a reflected S-wave, a transmitted P-wave and a transmitted S-wave.

A special case of Snell's law is of interest in refraction prospecting. If the ray is critically refracted along the interface (that is, if $\theta_2 = 90^\circ$), we have

$$
\frac{\sin \theta_c}{c_1} = \frac{1}{c_2}
$$

where $\theta_c$ is known as the critical angle.

So far, we have looked at the basic notions of refraction and reflection at an interface. When we measure in the field, and there would be one boundary below it, we could observe several arrivals: a direct ray, a reflected ray, and a refracted ray. We will derive the arrival time of each ray as depicted in {numref}`fig-rays`.

```{figure} figures/rays.png
:name: fig-rays
:width: 80%

The paths of the direct, reflected and refracted rays.
```

The arrival time of the direct ray is very simple: it is the horizontal distance divided by the velocity of the wave, i.e.,:

$$
t = \frac{x}{c_1},
$$

so in a time-distance graph this is a linear event.

When we look at the reflected ray, we find that the angle of incidence is the same as the angle of reflection. This also follows from Snell's law: when the velocities are the same, the angles must also be the same. When we use Pythagoras' theorem, we obtain the following for the traveltime:

$$
t = \frac{ \left( 4z^2+x^2 \right)^{1/2} }{c_1}
$$

Squaring this equation:

$$
t^2 = \left( \frac{2z}{c_1} \right)^2 + \left( \frac{x}{c_1} \right)^2 ,
$$

or

$$
t^2 - \left( \frac{x}{c_1} \right)^2 = \left( \frac{2z}{c_1} \right)^2,
$$

so for a time-distance $(t-x)$ graph this is the equation of a hyperbola.

When we look at the refracted ray, the derivation is a bit more complicated. Take each ray element; therefore, take the paths $AB,$ $BC$ and $CD$ separately. Then, for the first element, as shown in {numref}`fig-rayelement`, we obtain the traveltime:

$$
\Delta t_1 = \frac{\Delta s_1 + \Delta s_2}{c_1} =
\frac{\Delta x_1 \sin \theta_c}{c_1} + \frac{z \cos \theta_c}{c_1}
$$

where $\theta_c$ is the critical angle.

```{figure} figures/rayelement.png
:name: fig-rayelement
:width: 60%

An element of the ray with critical incidence.
```

We can also do this for the paths $BC$ and $CD$, and we obtain the total time as:

$$
\begin{aligned}
t & = \Delta t_1 + \Delta t_2 + \Delta t_3 \\
  & = \frac{\Delta x_1 \sin \theta_c}{c_1} + \frac{z \cos \theta_c}{c_1}
        + \frac{\Delta x_2}{c_2} +
        \frac{\Delta x_3 \sin \theta_c}{c_1} + \frac{z \cos \theta_c}{c_1}
\end{aligned}
$$

where $\Delta x_2 = BC$ and $\Delta x_3$ is the horizontal distance between $C$ and $D$. When we now use Snell's law, i.e., $\sin \theta_c /c_1=1/c_2,$ in terms with $\Delta x_1$ and $\Delta x_3,$ then we can add all the terms with $1/c_2,$ using $x = \Delta x_1 + \Delta x_2 + \Delta x_3$ to obtain:

$$
t = \frac{x}{c_2} + \frac{2z \cos \theta_c}{c_1}
$$ (eq:trefract)

We recognize this equation as the equation of a straight line when $t$ is considered as a function of the distance $x,$ the line along which we do our wavefield measurements.

We have now derived the equations for the three rays, and we can plot their travel times as a function of distance $x$. This is done in {numref}`fig-raytimes`. This picture is important. When we measure seismic data in the field, the characteristics in this plot can be observed most of the time.

We considered travel times, but they are a result of a seismic wave field propagating in the subsurface. To get an idea of how a wave moves, we consider the movie below. A seismic source initiates a seismic wave at the top and the wave propagates outward (on a circle, for a homogeneous medium). Then later the wave encounters a boundary at which part of the wave is reflected and part of it is transmitted into the lower medium. There it travels with a higher speed; it can be seen that the wave travels faster along the boundary there. Then, part of it is diffracted back into the first medium (quite faint): that is the head wave, or critically refracted ray.

```{video} figures/seismicwave_1layer_vz.mp4
:width: 80%
```

```{figure} figures/raytimes.png
:name: fig-raytimes
:width: 60%

Time-distance $(t,x)$ curve for the direct, reflected and refracted rays.
```

Based on this figure, we can specify better when we can expect reflections or refractions. In refraction seismics we are interested in the critically refracted waves, and then only in the travel times. This means that we can only observe the traveltimes well if it is not masked by reflections and/or direct waves, which means that we must measure at a relatively large distance with respect to the depth of interest. This is different for reflection seismics. There, the reflections will always be masked by refractions and/or direct waves, but there are ways to enhance the reflections. What we are interested in is the arrival at relatively small offsets, thus distances of the sound source to the detector, which are small with respect to the depth we are interested in.

Before discussing any more differences between the refraction method and the reflection method, we would like to discuss the amplitude effects at the boundary. Let us first introduce the acoustic impedance, which is the product of the density $\rho$ with the wave velocity $c,$ i.e., $\rho c.$ When a ray encounters a boundary, some wavefield energy will be reflected back, and some will be transmitted to the next layer. The amount of energy reflected back is characterized by the reflection coefficient $R$:

$$
R = \frac{\rho_2 c_2 - \rho_1 c_1}{\rho_2 c_2 + \rho_1 c_1}
$$

That this is the case, will be derived from basic physical principles in a later section on wave theory ([](./reflection_transmission.md)). Obviously, the larger the impedance contrast between two layers, the higher the amplitude of the reflected wave. Notice that it is the impedance contrast that determines whether energy is reflected back or not; it may happen that the velocities and densities are different between two layers, but that the impedances are (nearly) the same. In that case, we will not see a reflection. We can now state another difference between refraction and reflection seismics. With refraction seismics we are only interested in traveltimes of the waves, so this means that we are interested in contrasts in velocities. This is different in reflection seismics. Then we are interested in the amplitude of the waves, and we will only measure an amplitude if there is a contrast in acoustic impedance in the subsurface.

Finally, we tabulate the most important differences between reflection and refraction seismic in {numref}`tab-diffref`.

```{list-table} Important differences between refraction and reflection seismics.
:name: tab-diffref
:header-rows: 1

* - **REFRACTION SEISMICS**
  - **REFLECTION SEISMICS**
* - Based on contrasts in: seismic wave speed $(c)$
  - Based on contrasts in: seismic wave impedances $(\rho c)$
* - Material property determined: wave speed only
  - Material properties determined: wave speed and wave impedance
* - Only traveltimes used
  - Traveltimes and amplitudes used
* - Source-receiver distances large compared to investigation depth
  - Source-receiver distances small compared to investigation depth
```
