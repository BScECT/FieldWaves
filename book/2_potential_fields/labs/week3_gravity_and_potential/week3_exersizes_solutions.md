# Lab 3: Gravity and Potential Fields (Solutions)

## Warm-ups

### 1. Equipotentials and field geometry
A probe measured the following gravitational potential in a region of space around an asteroid. a) Sketch the corresponding field lines.
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
A ball is rolling on a frictionless surface. At point $P$ it has velocity $v_0$. What is the velocity at point $P'$ for cases a), b) and c)?
```{figure} figures/rolling_ball.png
:width: 50%
```
$v=v_0$ in all cases because gravity is a conservative field. The route from $P$ to $P'$ does not matter (ignoring friction, and assuming $v_0$ is enough to make it over the hill in case b)). 

## Problems

### 3. Potential and work
Three identical point masses of $m=1000$kg are in a line, separated by a distance $a/2$, where $a=5$m. How much work must be done to move the centre mass from point $P$ to point $P'$, such that all three masses form an equilateral triangle? 
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

### 4. Gauss's Law and divergence
A radial gravitational field distribution is given in spherical coordinates as
```{math}
\vec{g}(r) =
\begin{cases}
-\dfrac{8\pi G\rho_0}{3}r\,\hat{r}, & r \leq a, \\
-\dfrac{4\pi G\rho_0}{3}
\dfrac{r^3+b^3}{r^2}\,\hat{r}, & a \leq r \leq b, \\
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
In this case, the field has only a dependance on $r$ (spherical symmetry). Thus the divergence operator becomes:
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
       \rho &= \frac{-1}{4\pi G}\frac{1}{r^2} \frac{\partial}{\partial r} \left(r^2 \frac{-4\pi G\rho_0}{3} \frac{r^3+b^3}{r^2} \right) \\
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