# Lab 3: Gravity and Potential Fields (Solutions)

## Warm-ups

### 1. Equipotentials and field geometry
A probe measured the following gravitational potential in a region of space around an asteroid (in arbitrary units). a) Sketch the corresponding field lines.
b) On which side is the field strongest?
```{figure} figures/equipotentials_with_lines.jpg
:width: 95%
```

Approximate field lines are shown above. According to 
```{math}
\vec{g} = -\vec{\nabla}\Phi,
```
field lines are always perpendicular to the equipotentials. The field is stronger on the right-hand side where the gradient is steeper. (Note that this is an exaggeration, in real life the differences would not be very large). 



### 2. Conservative fields
A ball with mass $m$ is rolling on a frictionless surface. At point $P$ it has velocity $v_0$. What is the velocity at point $P'$ for cases a), b) and c)?
```{figure} figures/rolling_ball.png
:width: 50%
```
$v=v_0$ in all cases because gravity is a conservative field. The route from $P$ to $P'$ does not matter (ignoring friction, and assuming $v_0$ is enough to make it over the hill in case b)). 

### 3. Inside a hollow asteroid
A hollow, non-rotating asteroid is modelled as a thin uniform spherical shell of mass $M$ and radius $R$. A small loose pebble lies at rest inside the cavity at point $P$, closer to one side of the shell.
```{figure} figures/hollow_asteroid_spherical.png
:width: 35%
```
a) Will the pebble start to move toward the nearer wall? In which direction does the shell pull it?

b) Sketch the potential $\Phi(r)$ and the field strength $|\vec{g}|(r)$ as functions of the distance $r$ from the centre of the asteroid. Draw both inside the cavity ($r<R$) and outside the asteroid, up to a few times $R$. Take $\Phi \to 0$ at infinity.

c) The asteroid actually has the irregular shape shown below. The cavity is a sphere of radius $R$ centred at $O$, and the rock has the same uniform density everywhere. Would your answers to a) and b) change? Answer yes or no for each, and explain briefly.
```{figure} figures/irregular_asteroid.png
:width: 40%
```
 
a) No. The shell exerts no net pull anywhere inside it, so the pebble stays at rest. Draw a thin double cone through $P$: it cuts a small patch on the near side and a larger patch on the far side. The mass of each patch grows as the square of its distance from $P$, while its pull falls off as one over that distance squared, so the two pulls are equal and opposite. The nearer wall is closer, but it has less mass inside the cone. This exact cancellation relies on the inverse-square law. 
 
b)
```{figure} figures/hollow_asteroid_spherical_solution2.png
:width: 90%
```
```{math}
\Phi(r) =
\begin{cases}
-\dfrac{GM}{R}, & r < R, \\
-\dfrac{GM}{r}, & r > R,
\end{cases}
\qquad
|\vec{g}|(r) =
\begin{cases}
0, & r < R, \\
\dfrac{GM}{r^2}, & r > R.
\end{cases}
```
Inside, $\Phi$ is flat, so its slope, and therefore $\vec{g} = -\vec{\nabla}\Phi$, is zero. Outside, the shell acts as a point mass at the centre. The field strength jumps from $0$ to $GM/R^2$ at the shell; the potential is continuous.
 
c) Split the asteroid into two parts: a spherical shell centred at $O$ (inside the dashed circle) plus the extra material outside that shell.
```{figure} figures/irregular_asteroid_solution.png
:width: 40%
```
- a) **Yes.** The spherical shell still exerts no net pull in the cavity. The extra material, however, is not spherically symmetric, so its pulls do not cancel. The pebble starts to move toward the bulge on the left, which is *away* from its nearer wall: what matters is how the mass is distributed, not the distance to the nearest wall. The shell result requires spherical symmetry.
- b) **Yes.** Inside the cavity, $\vec{g} \neq \vec{0}$ and $\Phi$ is no longer constant: it varies from point to point. Outside, $\Phi$ and $\vec{g}$ depend on the direction as well as on the distance, so a single curve $\Phi(r)$ no longer describes them. Only far from the asteroid do they approach $-GM/r$ and $GM/r^2$, with $M$ the total mass.

## Problems

### 4. Potential and work
Three identical point masses of $m=1000$ kg are in a line, separated by a distance $a/2$, where $a=5$ m. How much work must be done to move the centre mass from point $P$ to point $P'$, such that all three masses form an equilateral triangle? 
```{figure} figures/masses_triangle.png
:width: 50%
```

One way this can be solved by considering the work done by the gravitational force along the path, $W = \int_S \vec{F} \cdot d\vec{s}$. An easier approach is to simply consider the change in potential energy $\Delta U$ of the test mass between the two locations. For discrete point masses we can write:
```{math}
\Phi(r) = -G\sum_i \frac{M_i}{R_i}.
```

At point $P$ we have:
```{math}
\begin{aligned}
\Phi(P) &= \frac{-Gm}{a/2} + \frac{-Gm}{a/2} \\
        &= \frac{-4Gm}{a} 
\end{aligned}
```
At point $P'$ we have:
```{math}
\begin{aligned}
\Phi(P') &= \frac{-Gm}{a} + \frac{-Gm}{a} \\
         &= \frac{-2Gm}{a} 
\end{aligned} 
```

The mass is constant, so the work done is caused by the change in potential:
```{math}
\begin{aligned}
W = \Delta U    &= m\Delta\Phi \\
                &= m \left[ \frac{-2Gm}{a} - \frac{-4Gm}{a} \right] \\
                &= \frac{2Gmm}{a} \\
                &= \frac{2(6.67\cdot 10^{-11})(1000)(1000)}{(5)} \\
                &= \boxed{2.67 \cdot 10^{-5} \mathrm{J}}
\end{aligned}
```

### 5. Gauss's Law and divergence
A radial gravitational field distribution is given in spherical coordinates as
```{math}
\vec{g}(r) =
\begin{cases}
-\dfrac{8\pi G\rho_0}{3}r\,\hat{r}, & r \leq a, \\
-\dfrac{4\pi G\rho_0}{3}
\dfrac{r^3+a^3}{r^2}\,\hat{r}, & a \leq r \leq b, \\
-\dfrac{4\pi G\rho_0}{3}
\dfrac{a^3+b^3}{r^2}\,\hat{r}, & r > b, \\
\end{cases}
```
where $\rho_0$, $a$ and $b$ are constants.
(a) Determine the volumetric mass density, $\rho(r)$, in the entire region $(0 \leq r < \infty)$.
(b) Find the total mass, $M$, within a sphere of radius $r$ where $r > b$. 

(a) We use Gauss's Law in differential form to find the source mass distribution. 
```{math}
\vec{\nabla} \cdot \vec{g} = -4\pi G\rho.
```
In this case, the field has only a dependence on $r$ (spherical symmetry). Thus the divergence operator becomes:
```{math}
\vec{\nabla} \cdot \vec{g} = \frac{1}{r^2} \frac{\partial}{\partial r} (r^2 g)
```

In region $r \leq a$: 
```{math}
\begin{aligned}
-4\pi G\rho &= \frac{1}{r^2} \frac{\partial}{\partial r} (r^2 g) \\
       \rho &= \frac{-1}{4\pi G}\frac{1}{r^2} \frac{\partial}{\partial r} \left(r^2 \frac{-8\pi G\rho_0 r}{3} \right) \\
            &= \frac{-1}{4\pi G}\frac{1}{r^2} \left(-8\pi G\rho_0 r^2 \right) \\
            &= \boxed{2\rho_0}
\end{aligned}
```

In region $a \leq r \leq b$: 
```{math}
\begin{aligned}
-4\pi G\rho &= \frac{1}{r^2} \frac{\partial}{\partial r} (r^2 g) \\
       \rho &= \frac{-1}{4\pi G}\frac{1}{r^2} \frac{\partial}{\partial r} \left(r^2 \frac{-4\pi G\rho_0}{3} \frac{r^3+a^3}{r^2} \right) \\
            &= \frac{-1}{4\pi G}\frac{1}{r^2} \left(-4\pi G\rho_0 r^2 \right) \\
            &= \boxed{\rho_0}
\end{aligned}
```

In region $r > b$: 
```{math}
\begin{aligned}
-4\pi G\rho &= \frac{1}{r^2} \frac{\partial}{\partial r} (r^2 g) \\
       \rho &= \frac{-1}{4\pi G}\frac{1}{r^2} \frac{\partial}{\partial r} \left(r^2 \frac{-4\pi G\rho_0}{3} \frac{a^3+b^3}{r^2} \right) \\
            &= \boxed{0} 
\end{aligned}
```

(b) The total mass, $M$, can be found in two ways; either by applying Gauss's Law to the external field ($r >$ b), or by simply integrating $\rho$ over the spherical volume:

Gauss's Law method:
```{math}
\oint \vec{g}\cdot d\vec{A} = -4\pi G M_\mathrm{enc}
```
in this case, 
```{math}
d\vec{A} = r^2\sin\theta d\theta d\phi \hat{r},
``` 
giving us:
```{math}
\begin{aligned}
M   &= \frac{-1}{4\pi G} \oint \frac{-4\pi G \rho_0}{3}\frac{a^3+b^3}{r^2}\hat{r} \cdot r^2\sin\theta d\theta d\phi \hat{r} \\
    &= \frac{\rho_0}{3}(a^3+b^3) \oint \sin\theta d\theta d\phi \\
    &= \frac{\rho_0}{3}(a^3+b^3) \int_0^{2\pi}\int_0^\pi \sin\theta d\theta d\phi \\
    &= \frac{\rho_0}{3}(a^3+b^3) 4\pi \\
&=\boxed{\frac{4\pi\rho_0}{3}(a^3+b^3)}
\end{aligned}
```

Integrating over volume method:
```{math}
\begin{aligned}
M   &= \iiint_V \rho(r) dV \\
    &= \int_0^{2\pi} \int_0^{\pi} \int_0^b \rho(r) r^2 \sin\theta dr d\theta d\phi \\
    &= 4\pi \int_0^b \rho(r) r^2 dr \\
    &= 4\pi \left[\int_0^a \rho(r) r^2 dr + \int_a^b \rho(r) r^2 dr \right] \\
    &= 4\pi \left[\int_0^a 2\rho_0 r^2 dr + \int_a^b \rho_0 r^2 dr \right] \\
    &= \frac{8\pi\rho_0}{3}a^3 + \frac{4\pi\rho_0}{3}(b^3-a^3) \\
&= \boxed{\frac{4\pi\rho_0}{3}(a^3+b^3)}
\end{aligned}
```

### 6. A conservative field: integrating around a rectangle

The potential of $\vec{F}$ is given by $\left(x^2+y^2\right)^{-1}$.

Note: This is an abstract conservative vector field; it is not intended to represent a gravitational field.

(a) Find $\vec{F}$.

(b) Describe the field lines of $\vec{F}$.

(c) Describe the equipotential surfaces of $\vec{F}$.

(d) Verify by integration around the perimeter of a rectangle in the $x,y$ plane that the circulation of $\vec{F}$ around this rectangle vanishes. Let the rectangle extend from $x_1$ to $x_2$ in the $x$ direction and from $y_1$ to $y_2$ in the $y$ direction, and let $x_1 > 0$.

(a) Write the potential as $\Phi = \left(x^2+y^2\right)^{-1}$ and use $\vec{F} = -\vec{\nabla}\Phi$. The partial derivatives of $\Phi$ are

```{math}
\frac{\partial\Phi}{\partial x} = -\frac{2x}{\left(x^2+y^2\right)^2}, \qquad
\frac{\partial\Phi}{\partial y} = -\frac{2y}{\left(x^2+y^2\right)^2}, \qquad
\frac{\partial\Phi}{\partial z} = 0.
```

Therefore

```{math}
F_x = \frac{2x}{\left(x^2+y^2\right)^2}, \qquad F_y = \frac{2y}{\left(x^2+y^2\right)^2}, \qquad F_z = 0,
\qquad
\boxed{\vec{F} = \frac{2\left(x\,\hat{x} + y\,\hat{y}\right)}{\left(x^2+y^2\right)^2}}
```

With $s = \sqrt{x^2+y^2}$, the distance from the $z$-axis, the magnitude is

```{math}
|\vec{F}| = \frac{2\sqrt{x^2+y^2}}{\left(x^2+y^2\right)^2} = \frac{2s}{s^4} = \frac{2}{s^3}.
```

(b) A field line is a curve whose direction at every point matches $\vec{F}$. In the $x,y$-plane, the direction of a curve is given by its slope, $dy/dx$. The direction of the vector $\vec{F} = (F_x, F_y)$ is also a slope ("rise over run"), namely $F_y/F_x$. For the curve to follow the field, the two slopes must be equal:

```{math}
\underbrace{\frac{dy}{dx}}_{\text{slope of the curve}} = \underbrace{\frac{F_y}{F_x}}_{\text{slope of the field}}
```

Equivalently, a small step $(dx, dy)$ along the field line must point in the same direction as $\vec{F}$, so its components are in the same ratio:

```{math}
\frac{dy}{dx} = \frac{F_y}{F_x}.
```

This is a differential equation, and its solutions are the field lines.

$\vec{F}$ is parallel to $x\,\hat{x} + y\,\hat{y}$, which points directly away from the $z$-axis. The field lines follow the direction of $\vec{F}$, so in a plane $z = $ constant

```{math}
\frac{dy}{dx} = \frac{F_y}{F_x} = \frac{y}{x}
\quad\Rightarrow\quad
\frac{dy}{y} = \frac{dx}{x}
\quad\Rightarrow\quad
\boxed{y = Cx}
```

The field lines are **straight radial lines in planes $z = $ constant, directed outward from the $z$-axis**. The field becomes weaker as $1/s^3$ away from the axis, and it is undefined on the $z$-axis itself.

```{figure} figures/conservativefield_lines_ex6.png
:width: 80%
```

(c) An equipotential surface is where $\Phi$ has a constant value $\Phi_0$:

```{math}
\frac{1}{x^2+y^2} = \Phi_0 \quad\Rightarrow\quad x^2+y^2 = \frac{1}{\Phi_0}.
```

In a plane $z = $ constant this is a circle around the $z$-axis. There is no restriction on $z$, so the circle extends along the $z$-direction: the equipotential surfaces are **circular cylinders $x^2+y^2 = $ constant around the $z$-axis**.

The gradient of $\Phi$ is perpendicular to any surface of constant $\Phi$, and $\vec{F} = -\vec{\nabla}\Phi$. The field is therefore normal to the cylinders: the radial field lines cross them at right angles.

(d) Along the path, a small displacement is $d\vec{s} = dx\,\hat{x} + dy\,\hat{y}$, so

```{math}
\vec{F}\cdot d\vec{s} = F_x\,dx + F_y\,dy.
```

- On a horizontal side, $dy = 0$, so only $F_x\,dx$ contributes.

- On a vertical side, $dx = 0$, so only $F_y\,dy$ contributes.

Go around the rectangle counterclockwise, as in the figure. The condition $x_1 > 0$ keeps the rectangle away from the $z$-axis, where $\vec{F}$ is undefined, so every integral exists.

```{figure} figures/rectangle_conservative.png
:width: 55%
```

Each integral uses the antiderivative $\int \dfrac{2u\,du}{(u^2+c^2)^2} = -\dfrac{1}{u^2+c^2}$.

Bottom side, $y = y_1$, from $x_1$ to $x_2$:

```{math}
I_1 = \int_{x_1}^{x_2} \frac{2x\,dx}{\left(x^2+y_1^2\right)^2} = \left[-\frac{1}{x^2+y_1^2}\right]_{x_1}^{x_2} = \frac{1}{x_1^2+y_1^2} - \frac{1}{x_2^2+y_1^2}
```

Right side, $x = x_2$, from $y_1$ to $y_2$:

```{math}
I_2 = \int_{y_1}^{y_2} \frac{2y\,dy}{\left(x_2^2+y^2\right)^2} = \frac{1}{x_2^2+y_1^2} - \frac{1}{x_2^2+y_2^2}
```

Top side, $y = y_2$, from $x_2$ back to $x_1$:

```{math}
I_3 = \int_{x_2}^{x_1} \frac{2x\,dx}{\left(x^2+y_2^2\right)^2} = \frac{1}{x_2^2+y_2^2} - \frac{1}{x_1^2+y_2^2}
```

Left side, $x = x_1$, from $y_2$ back to $y_1$:

```{math}
I_4 = \int_{y_2}^{y_1} \frac{2y\,dy}{\left(x_1^2+y^2\right)^2} = \frac{1}{x_1^2+y_2^2} - \frac{1}{x_1^2+y_1^2}
```

Adding the four sides:

```{math}
\begin{aligned}
\oint \vec{F}\cdot d\vec{s} = I_1 + I_2 + I_3 + I_4
={}& \left(\frac{1}{x_1^2+y_1^2} - \frac{1}{x_2^2+y_1^2}\right)
+ \left(\frac{1}{x_2^2+y_1^2} - \frac{1}{x_2^2+y_2^2}\right) \\
&+ \left(\frac{1}{x_2^2+y_2^2} - \frac{1}{x_1^2+y_2^2}\right)
+ \left(\frac{1}{x_1^2+y_2^2} - \frac{1}{x_1^2+y_1^2}\right) \\
={}& 0.
\end{aligned}
```

Every term appears once with a plus sign and once with a minus sign, so

```{math}
\boxed{\oint \vec{F}\cdot d\vec{s} = 0}
```

This explicit calculation verifies that the circulation around this rectangle vanishes: the contributions from the four sides cancel.

The zero result is expected because the field is generated by the potential $\Phi$. Along any path from $A$ to $B$,

```{math}
\int_A^B \vec{F}\cdot d\vec{s} = \Phi(A) - \Phi(B),
```

and for a closed path $A = B$, so the integral is zero. Each $I_k$ above has exactly this form: the potential at the start of the side minus the potential at its end.

*Alternative check.* Since $\vec{F} = -\vec{\nabla}\Phi$, we must have $\vec{\nabla}\times\vec{F} = \vec{0}$ wherever $\Phi$ is smooth, which is everywhere except on the $z$-axis.

### 7. Laplace equation and physical meaning
A thin metal plate is in steady-state thermal conduction. The thermal conductivity $k$ is constant, and there are no internal heat sources or sinks within the plate. The temperature distribution is proposed to be
```{math}
T(x,y)=T_0+A(x^2-y^2),
```
where $T_0$ and $A$ are constants.

(a) Show that the temperature distribution satisfies Laplace's equation, $\nabla^2 T = 0$.

(b) Is the temperature uniform throughout the plate? Explain briefly.

(c) What does $\nabla^2T=0$ mean physically in this problem? Does it mean that there is no heat flow?

(d) The heat flux is given by Fourier's law, $\vec{q}=-k\vec{\nabla}T$, where $k$ is the thermal conductivity. Find $\vec{q}$ and describe its direction.
 

(a) In the two-dimensional plate the Laplacian is
```{math}
\nabla^2T = \frac{\partial^2T}{\partial x^2} + \frac{\partial^2T}{\partial y^2}.
```
Differentiating $T = T_0 + A(x^2-y^2)$ once, and remembering that $T_0$ and $A$ are constants,
```{math}
\frac{\partial T}{\partial x} = \frac{\partial}{\partial x}\left[T_0 + A(x^2-y^2)\right] = 2Ax,
\qquad
\frac{\partial T}{\partial y} = \frac{\partial}{\partial y}\left[T_0 + A(x^2-y^2)\right] = -2Ay.
```
Differentiating a second time,
```{math}
\frac{\partial^2T}{\partial x^2} = \frac{\partial}{\partial x}\left(2Ax\right) = 2A,
\qquad
\frac{\partial^2T}{\partial y^2} = \frac{\partial}{\partial y}\left(-2Ay\right) = -2A.
```
Adding the two second derivatives,
```{math}
\nabla^2T = 2A + (-2A) = \boxed{0}
```
The proposed temperature distribution therefore satisfies Laplace's equation.
 
(b) No. The temperature depends on position through the term $A(x^2-y^2)$, so it varies across the plate. A uniform temperature would require the much stronger condition $\vec{\nabla}T = \vec{0}$. The gradient describes how $T$ changes from one point to another, while the Laplacian describes its curvature. Here the two curvatures, $+2A$ and $-2A$, cancel, giving a zero Laplacian even though the temperature varies throughout the plate.
 
(c) In steady state, with constant $k$ and a heat production $H$ per unit volume,
```{math}
k\nabla^2T + H = 0.
```
Here $H=0$, so $\nabla^2T=0$. Physically, no heat is produced or absorbed inside the plate: whatever flows into a small region also flows out of it,
```{math}
\vec{\nabla}\cdot\vec{q} = -k\nabla^2T = 0.
```
This does **not** mean that there is no heat flow. Heat enters through one part of the boundary and leaves through another; only $\vec{\nabla}T=\vec{0}$ would give $\vec{q}=\vec{0}$.
The same holds for gravity: in a region without mass $\nabla^2\Phi = 0$, yet $\vec{g}$ can be large there, because the masses lie outside the region.
 
(d) The temperature gradient is
```{math}
\vec{\nabla}T = \frac{\partial T}{\partial x}\hat{x} + \frac{\partial T}{\partial y}\hat{y} = 2Ax\,\hat{x} - 2Ay\,\hat{y},
```
and substituting it into Fourier's law gives
```{math}
\begin{aligned}
\vec{q} &= -k\vec{\nabla}T \\
        &= -k\left(2Ax\,\hat{x} - 2Ay\,\hat{y}\right) \\
        &= \boxed{-2kAx\,\hat{x} + 2kAy\,\hat{y}}
\end{aligned}
```
The heat flux points **opposite to the temperature gradient**, in the direction of decreasing temperature. For example, taking $A>0$: where $x>0$ we have $q_x = -2kAx < 0$, so heat flows in the negative $x$ direction, toward the $y$ axis; where $y>0$ we have $q_y = 2kAy > 0$, so heat flows in the positive $y$ direction, away from the $x$ axis.

```{figure} figures/plate_heat_flux.png
:width: 45%
```
The isotherms $x^2-y^2=$ constant are hyperbolas, and the flux crosses them at right angles, running from the warmer parts of the plate to the cooler ones. The flux vanishes only at the origin, where $\vec{\nabla}T=\vec{0}$.
The flux is generally non-zero even though the Laplacian is zero:
```{math}
\boxed{\nabla^2T = 0 \quad\not\Rightarrow\quad \vec{q} = \vec{0}}
```
Laplace's equation therefore describes a **source-free region**, not a region with uniform temperature or zero heat flow.
 