(app-elastic)=
# Appendix: strain, P- and S-waves

*In this appendix, strain for an elastic solid is explained. Together with the stress (discussed in the main text), it is used to derive the basic equations for P- and S-waves: the deformation equations and the equations of motion.*

## Strain

Strain is a geometrical quantity. It is a *relative* displacement under applied forces, i.e., it is a measure of deformation, normalized by its original size. As for stress, strain may be divided into normal strain and shear strain, depending on the type of force applied. For a normal strain in the deformation of a volume, the strain is simply the change of volume divided by its original volume, i.e.,:

$$
e_{\text{normal}} = \frac{\Delta V}{V}
$$

where $e$ is the strain, $\Delta V$ the change in volume and $V$ the original volume itself. This volume change was also used to derive the acoustic wave equation (see [the appendix on 1-D acoustic wave motion](./appendix_acoustic_1d.md)).

Let us now look at {numref}`fig-ap-straindispl`, where the displacement $\underline{u}$ is given for a point $\underline{x}$. Notice that the displacement is a function of $\underline{x}$, i.e., $\underline{u} = \underline{u} (\underline{x})$. When a force/stress is applied, we get a difference in displacement, described by:

$$
\begin{aligned}
\underline{u} (\underline{x}+ d\underline{x}) & \simeq
          \underline{u} (\underline{x}) +
  \frac{\partial \underline{u}}{\partial \underline{x} } d\underline{x} \\
   & = \underline{u} (\underline{x}) + d\underline{u}
\end{aligned}
$$

where the first term is a translation and the second term is the term associated with deformation, in accordance with the assumption of elasticity. Notice that the term $\partial \underline{u}/ \partial \underline{x}$ is a matrix since both $\underline{u}$ and $\underline{x}$ are vectors:

$$
  \frac{\partial \underline{u}}{\partial \underline{x} } =
  \begin{pmatrix}
    \frac{\partial u_x}{\partial x} & \frac{\partial u_x}{\partial y} &
                                      \frac{\partial u_x}{\partial z} \\
    \frac{\partial u_y}{\partial x} & \frac{\partial u_y}{\partial y} &
                                      \frac{\partial u_y}{\partial z} \\
    \frac{\partial u_z}{\partial x} & \frac{\partial u_z}{\partial y} &
                                      \frac{\partial u_z}{\partial z} \\
  \end{pmatrix}
$$

The term $\partial \underline{u}/ \partial \underline{x}$ can be written in a symmetric and anti-symmetric part:

$$
  \frac{\partial \underline{u}}{\partial \underline{x} } =
   \underline{\underline{e}} - \frac{1}{2} \underline{\underline{\xi}}
$$

in which the elements of $\underline{\underline{e}}$ and $\underline{\underline{\xi}}$ are:

$$
  e_{ij} = \frac{1}{2}
    \left( \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}
      \right)
$$ (eq:straindispl)

$$
 \xi_{ij} =
      \frac{\partial u_j}{\partial x_i} - \frac{\partial u_i}{\partial x_j}
$$

where $\underline{\underline{e}}$ is the so-called strain tensor, and $\underline{\underline{\xi}}$ represents rigid rotation.

```{figure} figures/straindispl.PNG
:name: fig-ap-straindispl
:width: 60%

Displacement field under presence of stress.
```

## Tensile stress and strain, and P-waves in a solid

P-waves are associated with tensile stresses, so therefore, we consider the tensile stress and strain for an infinitesimal rectangular parallelepiped as shown in {numref}`fig-ap-ptens`. The sizes of the parallelepipeds are given by $\Delta X, \Delta Y$ and $\Delta Z$, while the changes therein are given by $\delta U_x, \delta U_y$ and $\delta U_z$. We apply a tensile stress in the $x$-direction only. As was also given in the appendix on acoustic wave motion, Hooke's law states that a force needed to extend or compress a spring is linearly related to the length ($u$) of extension/compression of that spring, so $F = k u.$ Stress is force per unit area, and strain is relative displacement, so Hooke's law applied to our parallelepiped gives:

$$
e_{xx} = \frac{\partial u_x}{\partial x} = \frac{\delta U_x}{\Delta X} =
       \frac{1}{E} \tau_{xx}
$$

where $\tau_{xx}$ is the tensile stress and $e_{xx}$ the tensile strain in the $x$-direction, and $E$ is called Young's modulus. When applying a tensile stress, the size in the perpendicular directions $y$ and $z$ *decreases*, i.e., a lateral contraction occurs. This is quantified by the so-called Poisson's ratio, via:

$$
\begin{aligned}
e_{yy} & = \frac{\partial u_y}{\partial y} = \frac{\delta U_y}{\Delta Y} =
            - \sigma e_{xx} \\
e_{zz} & = \frac{\partial u_z}{\partial z} = \frac{\delta U_z}{\Delta Z} =
            - \sigma e_{xx}
\end{aligned}
$$

We can follow the same procedure for a tensile stress in the $y$- and $z$-directions with tensile strains $e_{yy}$ and $e_{zz}$, giving totally:

$$
  \begin{pmatrix}
    e_{xx} \\ e_{yy} \\ e_{zz}
  \end{pmatrix}
  = \frac{1}{E}
  \begin{pmatrix}
    1       & -\sigma & -\sigma \\
    -\sigma & 1       & -\sigma \\
    -\sigma & -\sigma & 1
  \end{pmatrix}
  \begin{pmatrix}
    \tau_{xx} \\ \tau_{yy} \\ \tau_{zz}
  \end{pmatrix}
$$ (eq:etau)

```{figure} figures/ptens.PNG
:name: fig-ap-ptens
:width: 60%

Infinitesimal rectangular parallelepiped deformed by tensile stress.
```

So far, we have written down the basic expressions, but they are not in the desired form: we want to have a form in which the partial derivatives of the particle displacements are given (and not strains), and we want to have the stress on the left-hand side of the equation and the strains/particle-displacements on the right-hand side. To address the first issue, we have:

$$
  \begin{pmatrix}
    e_{xx} \\ e_{yy} \\ e_{zz}
  \end{pmatrix}
  =
  \begin{pmatrix}
    \frac{\partial u_x}{\partial x} \\
    \frac{\partial u_y}{\partial y} \\
    \frac{\partial u_z}{\partial z}
  \end{pmatrix}
$$

To address the second issue, we have to invert the matrix in {eq}`eq:etau`. Since the inverted matrix has terms that are not very simple, the so-called Lamé parameters are introduced:

$$
\begin{aligned}
    \lambda & = \frac{\sigma E}{ (1-2\sigma)(1+\sigma)} \\
    \mu     & = \frac{E}{2 (1+\sigma)}
\end{aligned}
$$

where $\mu$ is known as the shear modulus. Using these, we then get:

$$
  \begin{pmatrix}
    \tau_{xx} \\ \tau_{yy} \\ \tau_{zz}
  \end{pmatrix}
  =
  \begin{pmatrix}
    \lambda + 2\mu & \lambda        & \lambda        \\
    \lambda        & \lambda + 2\mu & \lambda        \\
    \lambda        & \lambda        & \lambda + 2\mu
  \end{pmatrix}
  \begin{pmatrix}
    \frac{\partial u_x}{\partial x} \\
    \frac{\partial u_y}{\partial y} \\
    \frac{\partial u_z}{\partial z}
  \end{pmatrix}
$$

This is the desired expression that we will use next.

Let us now derive the equations necessary to describe 1-D wave motion of a P-wave, travelling in the $x$-direction. To that end, consider {numref}`fig-ap-pblock`, in which again an infinitesimal block with size $\Delta X$, $\Delta Y$ and $\Delta Z$ is given. The mass $\Delta M$ of the little block is given by $\rho \Delta X \Delta Y  \Delta Z$. We initiate a plane displacement field with displacements in the $x$-direction only (and therefore there is no contraction $\sigma$ for this 1-D case):

$$
   \underline{u} (x,y,z,t) =
   \begin{pmatrix}
     u_x(x,t) \\ 0 \\ 0
   \end{pmatrix}
$$

In that case, Hooke's law gives $\tau_{xx} = (\lambda + 2\mu)\partial u_x/\partial x$. As for the acoustic case, we are finally interested in particle velocities rather than displacements (since geophones measure particle velocities), we differentiate both sides of Hooke's law with respect to time $t$, and introduce $v_x = \partial u_x/\partial t$ to give:

$$
\boxed{
  \frac{ \partial \tau_{xx} }{\partial t} = (\lambda + 2 \mu)
                                            \frac{ \partial v_x }{\partial x}
}
$$

Note that this equation has the same shape as the equation for acoustic waves, i.e.,

$$
  - \frac{ \partial p }{\partial t} = K \frac{ \partial v_x }{\partial x}
$$

```{figure} figures/pblock.PNG
:name: fig-ap-pblock
:width: 60%

Infinitesimal rectangular block under plane stress, used for deriving basic equations for P-wave motion.
```

This equation alone does not describe wave motion; to that end we need to apply Newton's law as well. Referring to {numref}`fig-ap-pblock`, the force is, in terms of stress:

$$
  F_x = \Delta Y \Delta Z [ \tau_{xx}(x+\Delta X) - \tau_{xx}(x) ]
$$

and the force is given as mass times acceleration, i.e.:

$$
  F_x = \Delta M \frac{\partial^2 u_x}{\partial t^2}.
$$

Equalizing these forces gives:

$$
 \frac{ \tau_{xx}(x+\Delta X) - \tau_{xx}(x) }{\Delta X}
  =
  \frac{\Delta M}{\Delta X \Delta Y \Delta Z}
      \frac{\partial^2 u_x}{\partial t^2}
$$

or, since $\tau_{xx}(x+\Delta X) \simeq \tau_{xx}(x) + ( \partial \tau_{xx}/\partial x ) \Delta X$:

$$
 \frac{ \partial \tau_{xx} }{\partial x}
  =
  \rho \frac{\partial^2 u_x}{\partial t^2}.
$$

Again, we need to introduce the particle velocity for the displacement, giving:

$$
\boxed{
  \frac{ \partial \tau_{xx} }{\partial x} =
  \rho \frac{\partial v_x}{\partial t}.
}
$$

This is the other desired equation, the equation of motion for P-waves. As expected, this equation has the same shape as the one for acoustic waves:

$$
  - \frac{ \partial p }{\partial x}
  =
  \rho \frac{\partial v_x}{\partial t}.
$$

## Shear stress and strain, and S-waves in a solid

S-waves are associated with shear stresses. We will follow the same line of derivation as for the P-waves but then with shear stresses: consider the shear stress and strain for an infinitesimal rectangle, deformed into a parallelogram (2D) as shown in {numref}`fig-ap-stens`, with sizes $\Delta X$ and $\Delta Z$. Let us first consider the left-hand figure (a), with $\tau_{xz}$. The shear modulus $\mu$ is defined as the constant that relates the stress and displacement, in this case as:

$$
  \tau_{xz} = \mu \frac{\delta U_x}{\Delta Z}
$$

which is the shear equivalent of Hooke's law for elastic deformation. Since the associated strain $e_{xz}$ was defined as $(1/2) ( \partial u_z/\partial x + \partial u_x/\partial z)$ (see {eq}`eq:straindispl`), which for the parallelogram becomes:

$$
   e_{xz} = \frac{1}{2} \frac{\delta U_x}{\Delta Z},
$$

the stress-strain relationship for shear deformation becomes:

$$
  \tau_{xz} = 2 \mu e_{xz}.
$$

```{figure} figures/stens.PNG
:name: fig-ap-stens
:width: 70%

Infinitesimal rectangle deformed to parallelogram by shear stress.
```

This was the analysis for shear deformation in the horizontal direction, but deformation can also take place in the vertical direction, as shown in {numref}`fig-ap-stens`(b). In that case we have for the stress and strain:

$$
\begin{aligned}
   \tau_{zx} & = \mu \frac{\delta U_z}{\Delta X}  \\
   e_{zx}    & = \frac{1}{2} \frac{\delta U_z}{\Delta X}      \\
   \tau_{zx} & = 2 \mu e_{zx}.
\end{aligned}
$$

The deformations as shown in {numref}`fig-ap-stens`(a) and (b) are actually deformations with a rigid-body rotation where $e_{xz} \neq e_{zx}$. We are interested in the deformation which show no rigid-body rotation, as shown in {numref}`fig-ap-stens`(c). For no rigid-body rotation $\xi_{xz}=0$, so:

$$
   \frac{\partial u_x}{\partial z} = \frac{\partial u_z}{\partial x},
   \qquad \text{or} \qquad
   \frac{\delta U_x}{\Delta Z} = \frac{\delta U_z}{\Delta X},
$$

We then have:

$$
   e_{xz} = e_{zx},
$$

and therefore:

$$
   \tau_{xz} = \tau_{zx}.
$$

Similarly, for no rigid-body rotation in 3-D:

$$
\begin{aligned}
   e_{xy}    & = e_{yx} \\
   e_{yz}    & = e_{zy} \\
   \tau_{xy} & = \tau_{yx} \\
   \tau_{yz} & = \tau_{zy}
\end{aligned}
$$

Let us now derive the equations necessary to describe 1-D wave motion of an S-wave, travelling in the $x$-direction (as for the P-wave). To that end, consider {numref}`fig-ap-sblock` in which again an infinitesimal block with size $\Delta X$, $\Delta Y$ and $\Delta Z$ and mass $\Delta M = \rho \Delta X \Delta Y  \Delta Z$ is given. We initiate a plane displacement field, giving displacements in the $z$-direction only (for P-waves they were in the $x$-direction only):

$$
   \underline{u} (x,y,z,t) =
   \begin{pmatrix}
     0 \\ 0 \\ u_z(x,t)
   \end{pmatrix}
$$

This means that there are no tensile stresses (since $u_z = u_z(x,t)$ only), and the other shear stresses $\tau_{xy}$ and $\tau_{yz}$ are zero. The shear equivalent of Hooke's law gives:

$$
  \tau_{zx} = 2\mu e_{zx} = 2\mu \cdot \frac{1}{2} \left(
     \frac{\partial u_z}{\partial x} + \frac{\partial u_x}{\partial z} \right)
   = \mu \frac{\partial u_z}{\partial x}
$$

As for P-waves, in order to introduce the particle velocity $v_z$, we differentiate both sides with respect to time $t$ and take the particle velocity as $v_z = \partial u_z/\partial t$ to give:

$$
\boxed{
  \frac{\partial \tau_{zx}}{\partial t} = \mu \frac{\partial v_z}{\partial x}.
}
$$

This is the desired expression for the deformation.

```{figure} figures/sblock.PNG
:name: fig-ap-sblock
:width: 60%

Infinitesimal rectangular block under plane stress, used for deriving basic equations for S-wave motion.
```

As before, this equation alone does not describe wave motion since we need to apply Newton's law as well. Referring to {numref}`fig-ap-sblock`, the force is, in terms of stress:

$$
  F_z = \Delta Y \Delta Z [ \tau_{zx}(x+\Delta X) - \tau_{zx}(x) ]
$$

and the force is given as mass times acceleration, i.e.:

$$
  F_z = \Delta M \frac{\partial^2 u_z}{\partial t^2}.
$$

Equalizing these forces gives:

$$
 \frac{ \tau_{zx}(x+\Delta X) - \tau_{zx}(x) }{\Delta X}
  =
  \frac{\Delta M}{\Delta X \Delta Y \Delta Z}
      \frac{\partial^2 u_z}{\partial t^2}
$$

or, since $\tau_{zx}(x+\Delta X) \simeq \tau_{zx}(x) + ( \partial \tau_{zx}/\partial x ) \Delta X$:

$$
 \frac{ \partial \tau_{zx} }{\partial x}
  =
  \rho \frac{\partial^2 u_z}{\partial t^2}.
$$

Again, we need to introduce the particle velocity via the displacement, giving:

$$
\boxed{
  \frac{ \partial \tau_{zx} }{\partial x} =
  \rho \frac{\partial v_z}{\partial t}.
}
$$

This is the other desired equation, the equation of motion for S-waves.
