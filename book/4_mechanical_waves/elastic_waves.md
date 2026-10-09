# Wave fields in a solid: elastic (P and S) waves

## Stress

Here we define *stress*. Stress can be defined as the force per unit area exerted on a body across an imaginary surface (see also {numref}`fig-stressforce`). Since the dimension of stress is of a pressure, i.e., force per unit area, the quantities of stress are also given in the dimension of pressure, i.e., Pa. Therefore, the stress can be seen as the equivalent of pressure in an (elastic) solid. One can discern normal stress as the stress perpendicular to a surface, and shear stress as the one parallel to a surface. The normal stress is also called compressional or tensile stress. Since a stress can be in any direction to a surface, the stress can be decomposed into components perpendicular and parallel to the surface. This decomposition matrix is also called the stress tensor. In formula form, this can all be written as:

$$
  \frac{\underline{F}}{\Delta S} =
   \underline{\underline{\tau}} \, \underline{n}
$$

where $F$ is the force, $\Delta S$ is the surface, $\underline{\underline{\tau}}$ is the stress tensor and $\underline{n}$ is the vector normal to the surface $\Delta S$. When writing out the matrix of the stress, i.e., the stress tensor, in terms of the coordinates $x$, $y$ and $z$, we get:

$$
   \underline{\underline{\tau}} =
   \begin{pmatrix}
     \tau_{xx} & \tau_{xy} & \tau_{xz} \\
     \tau_{yx} & \tau_{yy} & \tau_{yz} \\
     \tau_{zx} & \tau_{zy} & \tau_{zz}
   \end{pmatrix}
$$

Some of these factors are visualized in {numref}`fig-tautensor`.

```{figure} figures/stressforce.PNG
:name: fig-stressforce
:width: 60%

Definition of stress for a force working on a surface $\Delta S$.
```

In order to see the equivalence with the acoustic case, consider the case where no shear stresses exist. Then the diagonal elements of the matrix are the only non-zero ones, and the stress matrix can be written as:

$$
   \underline{\underline{\tau}}_{\text{no-shear}} =
   \begin{pmatrix}
     -p &  0 & 0 \\
     0  & -p & 0 \\
     0  & 0  & -p
   \end{pmatrix}
$$

where $p$ is the pressure. Notice that there is a minus sign since commonly the positive sign for pressure is for a compressional force, while for stress it is for a tensile force.

```{figure} figures/tautensor.PNG
:name: fig-tautensor
:width: 60%

Definition of stress components for stresses working on an infinitesimal parallelepiped.
```

## P-waves in an elastic solid

For 1-D wave motion in the $x$-direction, Hooke's law gives for the plane tensile stress $\tau_{xx}$ (see [the appendix on strain, P- and S-waves](./appendix_strain_p_s.md)):

$$
 \frac{\partial \tau_{xx}}{\partial t} = (\lambda + 2\mu)
              \frac{\partial v_x}{\partial x}
$$

where $\lambda$ and $\mu$ are the so-called Lamé parameters. $\lambda$ is the first Lamé parameter, and $\mu$ is the shear modulus; in 3-D, $\lambda$ is related to the bulk modulus $K$ through $K = \lambda + (2/3)\mu$. This equation is called the deformation equation for a P-wave in an elastic solid. Note that this equation has the same form as the deformation equation for acoustic waves (see {eq}`eq:eqdeform`).

Then applying Newton's law gives an equation nearly equivalent to the one for the acoustic case, but now having tensile stress instead of pressure (see also [the appendix on strain, P- and S-waves](./appendix_strain_p_s.md)):

$$
\frac{\partial \tau_{xx}}{\partial x} = \rho \frac{\partial v_x}{\partial t}
$$

This is the equation of motion for a P-wave. Combining the deformation equation and the equation of motion gives, as for the acoustic case, the wave equation for the stress, assuming the density being constant:

$$
\frac{\partial^2 \tau_{xx}}{\partial x^2}
	- \frac{1}{c^2_P} \frac{\partial^2 \tau_{xx}}{\partial t^2} = 0
$$

where $c^2_P = (\lambda + 2\mu)/\rho$ is the squared P-wave velocity. This wave equation describes the wave propagation for P-waves in an elastic solid.

## S-waves in an elastic solid

Let us now consider shear stresses which, as we shall see, will result in a wave equation for S-waves. To that end, we consider 1-D displacement in the $z$-direction for a wave propagating in the $x$-direction for the 1-D shear motion. The equivalent of Hooke's law for shear stress results in (see [the appendix on strain, P- and S-waves](./appendix_strain_p_s.md)):

$$
 \frac{\partial \tau_{zx}}{\partial t} = \mu \frac{\partial v_z}{\partial x}
$$ (eq:deformS)

where $\tau_{zx}$ is the shear stress. This is the deformation equation for an S-wave.

Then applying Newton's law for a shear stress gives (see also [the appendix on strain, P- and S-waves](./appendix_strain_p_s.md)):

$$
  \frac{\partial \tau_{zx}}{\partial x} = \rho \frac{\partial v_z}{\partial t}
$$ (eq:eqmotionS)

which is the equation of motion for S-waves. Combining the deformation equation and the equation of motion gives the wave equation for the shear stress, assuming the density being constant:

$$
\frac{\partial^2 \tau_{zx}}{\partial x^2}
	- \frac{1}{c^2_S} \frac{\partial^2 \tau_{zx}}{\partial t^2} = 0
$$ (eq:waveqStau)

where $c^2_S = \mu / \rho$ is the squared S-wave velocity. This wave equation describes the wave propagation for S-waves in an elastic solid.

With respect to the (1-D) reflection coefficients for P- and S-waves at the boundary of two elastic solids: the derivations go similar as for the acoustic case, as worked out in the previous section:

- For P-waves, we require the continuity of the tensile stress $\tau_{xx}$ and the particle velocity $v_x$ at the interface, and
- For S-waves we require the continuity of the shear stress $\tau_{zx}$ and the particle velocity $v_z$ at the interface.

The resulting expressions for the reflection and transmission coefficient are the same as for the acoustic case, only now the velocities are for the elastic solid. (See the [*EXERCISES*](./exercises.md))
