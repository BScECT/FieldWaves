(app-waveq1d)=
# Appendix: derivation of basic equations for 1-D acoustic wave motion

*In this appendix, the one-dimensional wave motion for an acoustic medium is derived, starting from the deformation law of Hooke and from conservation of momentum (Newton's Second Law). This results in the so-called deformation equation and the equation of motion for acoustic waves.*

## Derivation

Here we will derive the basic equations for wave motion in homogeneous media, using the conservation of momentum (Newton's second law) and the deformation law, known as Hooke's Law of elasticity. In this derivation, we consider a single cube of mass when it is subdued to a seismic disturbance (see {numref}`fig-cube`). This cube has a volume $\Delta V$ with sides $\Delta X, \Delta Y$ and $\Delta Z.$

```{figure} figures/fig_ap_ac_cube.png
:name: fig-cube
:width: 70%

A cube of mass, subjected to one-dimensional wave motion. Drawn line: original status. Dotted line: status after deformation.
```

We start with an elastic deformation of the cube, using Hooke's Law. This law states that the deformation force that works on a piece of material is linearly related to the extension of that piece. Applying this to our cube of mass, the deformation force gives a relative change in volume:

$$
p = -K \frac{dV}{\Delta V}
$$ (eq:hooke)

where the pressure $p$ is introduced as being the force per unit area, $K$ is called the bulk modulus, and the minus sign expresses that the pressure is opposite to the deformation direction. Now we assume that the volume change is only in one direction (1-dimensional) as shown in {numref}`fig-cube`, so then we get:

$$
\begin{aligned}
\frac{dV}{\Delta V} & =
	\frac{u_x(x+\Delta X)\Delta Y \Delta Z- u_x(x) \Delta Y \Delta Z}
             {\Delta X \Delta Y \Delta Z} \\
& = \frac{u_x(x+\Delta X) - u_x(x)}{\Delta X}
\end{aligned}
$$

where $u_x$ is the displacement in the $x$-direction. Using the situation that $\Delta X$ is rather small, we can approximate $u_x(x+\Delta X)$ by $u_x(x) + ( \partial u_x/\partial x ) \Delta X$; this then gives for Hooke's Law:

$$
p = -K \frac{\partial u_x}{\partial x}.
$$

Since we are finally interested in particle velocities rather than displacements (since geophones, seismic sensors on land, measure particle velocities), we differentiate both sides of Hooke's Law with respect to time $t$, and introduce $v_x = \partial u_x/\partial t$ to give:

$$
\boxed{
\frac{1}{K} \frac{\partial p}{\partial t} = - \frac{\partial v_x}{\partial x}
}
$$

This is the so-called deformation equation. It is one basic relation needed for describing one-dimensional wave motion.

The other relation is obtained via Newton's Law, applied to the volume $\Delta V$ with mass $M$ in the direction $x$, since we consider 1-dimensional motion:

$$
\begin{aligned}
F_x & = M \frac{\partial v_x}{\partial t} \\
    & = \rho \Delta V \frac{\partial v_x}{\partial t}
\end{aligned}
$$ (eq:newton)

where $F$ is the total force that works on the element $\Delta V$ that induces motion. Consider the total force that is working on the cube in the $x$-direction, through the pressures working on the sides with area $\Delta Y \Delta Z$:

$$
\begin{aligned}
F_x & = - [ p(x+\Delta X) - p(x) ]  \Delta S_x \\
    & = - \frac{p(x+\Delta X) - p(x)}{\Delta X}  \Delta V
\end{aligned}
$$

Using $p(x+\Delta X) \simeq p(x) + ( \partial p/\partial x ) \Delta X$ and combining it with Newton's Law as expressed in {eq}`eq:newton` gives:

$$
\boxed{
 - \frac{\partial p}{\partial x} = \rho \frac{\partial v_x}{\partial t}
}
$$

since $\Delta V$ cancels. This equation is called the equation of motion. It is the other basic relation (next to the deformation equation) needed to describe one-dimensional wave motion.
