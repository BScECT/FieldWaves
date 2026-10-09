# Wave fields in a fluid: acoustic (P) waves

With acoustic waves, we assume a fluid in which no shear forces exist, and therefore only P-waves exist. Since waves are physical phenomena, they should have a relation to basic physical laws. The two laws applicable are the conservation of mass and Newton's second law. These two have been used in [the appendix on 1-D acoustic wave motion](./appendix_acoustic_1d.md) to derive the two equations governing the wave motion due to a P-wave. There are some simplifying assumptions in the derivation, one of them being that we consider a 1-dimensional wave. When we denote $p$ as the pressure and $v_x$ as the particle velocity, the conservation of mass leads to:

$$
- \frac{1}{K} \frac{\partial p}{\partial t} = \frac{\partial v_x}{\partial x}
$$ (eq:eqdeform)

in which $K$ is called the bulk modulus. The other relation follows from an application of Newton's law:

$$
-\frac{\partial p}{\partial x} = \rho \frac{\partial v_x}{\partial t}
$$ (eq:eqmotion)

where $\rho$ denotes the mass density. This equation is called the equation of motion.

We are now going to combine these two equations. Therefore, we let the operator $\partial / \partial x$ work on the equation of motion:

$$
- \frac{\partial}{\partial x} \left( \frac{\partial p}{\partial x} \right)
 =
 \frac{\partial}{\partial x}
    \left( \rho \frac{\partial v_x}{\partial t} \right).
$$ (eq:diffeqmotion)

Now, assuming $\rho$ is constant, it can be taken in front of the $\partial / \partial x$ operator. And differentiations with respect to space $x$ and time $t$ are commutative, so:

$$
  \frac{\partial}{\partial x} \left( \frac{\partial v_x}{\partial t} \right)
  =
  \frac{\partial}{\partial t} \left( \frac{\partial v_x}{\partial x} \right).
$$ (eq:commut)

Now for $\partial v_x / \partial x$, the conservation of mass can be substituted in {eq}`eq:diffeqmotion` to give:

$$
   -\frac{\partial^2 p}{\partial x^2} = \rho
  \frac{\partial}{\partial t}
        \left( - \frac{1}{K} \frac{\partial p}{\partial t} \right).
$$

Rewriting gives us the 1-Dimensional wave equation:

$$
\frac{\partial^2 p}{\partial x^2}
	- \frac{1}{c^2} \frac{\partial^2p}{\partial t^2} = 0
$$

in which $c$ can be seen as the velocity of the wave, for which we have: $c = \sqrt{K/ \rho}$.

This is the basic wave equation for one-dimensional acoustic waves. Equally well, we can derive from the same two equations {eq}`eq:eqdeform` and {eq}`eq:eqmotion` (see also the [*EXERCISES*](./exercises.md)) that the particle velocity also satisfies the wave equation:

$$
\frac{\partial^2 v_x}{\partial x^2}
	- \frac{1}{c^2} \frac{\partial^2 v_x}{\partial t^2} = 0
$$ (eq:waveqacv)

where $c$ is the same as in the wave equation of the pressure.

Actually, the movie we showed before was generated using the above equations (but then discretized), so the equation of deformation {eq}`eq:eqdeform` and the equation of motion {eq}`eq:eqmotion`. It is shown again below.

```{video} figures/seismicwave_1layer_vz.mp4
:width: 80%
```
