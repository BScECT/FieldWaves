# Lab 3: Gravity and Potential Fields

## Warm-ups

### 1. Equipotentials and field geometry
A probe measured the following gravitational potential in a region of space around an asteroid (in arbitrary units). a) Sketch the corresponding field lines.
b) On which side is the field strongest?
```{figure} figures/equipotentials.png
:width: 50%
```

### 2. Conservative fields
A ball is rolling on a frictionless surface. At point $P$ it has velocity $v_0$. What is the velocity at point $P'$ for cases a), b) and c)?
```{figure} figures/rolling_ball.png
:width: 50%
```

## Problems

### 3. Potential and work
Three identical point masses of $m=1000$kg are in a line, separated by a distance $a/2$, where $a=5$m. How much work must be done to move the centre mass from point $P$ to point $P'$, such that all three masses form an equilateral triangle? 
```{figure} figures/masses_triangle.png
:width: 50%
```

### 4. Gauss's Law and divergence
A radial gravitational field distribution is given in spherical coordinates as
```{math}
\vec{g}(r) =
\begin{cases}
-\dfrac{8\pi G\rho_0}{3}r\,\hat{r}, & r \leq a, \\
-\dfrac{4\pi G\rho_0}{3}
\dfrac{r^3+b^3}{r^2}\,\hat{r},, & a \leq r \leq b, \\
-\dfrac{4\pi G\rho_0}{3}
\dfrac{a^3+b^3}{r^2}\,\hat{r}, & r \geq b, \\
\end{cases}
```
where $\rho_0$, $a$ and $b$ are constants.
(a) Determine the volumetric mass density, $\rho$, in the entire region $(0 \leq r \lt \infty)$.
(b) Find the total mass, $M$, within a sphere of radius $r$ where $r \gt b$. 