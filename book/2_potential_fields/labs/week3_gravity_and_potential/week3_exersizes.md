# Lab 3: Gravity and Potential Fields

## Warm-ups

### 1. Equipotentials and field geometry
A probe measured the following gravitational potential in a region of space around an asteroid (in arbitrary units). a) Sketch the corresponding field lines.
b) On which side is the field strongest?
```{figure} figures/equipotentials.png
:width: 50%
```

### 2. Conservative fields
A ball with mass $m$ is rolling on a frictionless surface. At point $P$ it has velocity $v_0$. What is the velocity at point $P'$ for cases a), b) and c)?
```{figure} figures/rolling_ball.png
:width: 50%
```

### 3. Inside a hollow asteroid
A hollow, non-rotating asteroid is modelled as a thin uniform spherical shell of mass $M$ and radius $R$. A small loose pebble lies at rest inside the cavity at point $P$, closer to one side of the shell.
```{figure} figures/hollow_asteroid_spherical.png
:width: 35%
```
a) Will the pebble start to move toward the nearer wall? In which direction does the shell pull it?

b) Sketch the potential $\Phi(r)$ and the field strength $|\vec{g}|(r)$ as functions of the distance $r$ from the centre of the asteroid. Draw both inside the cavity ($r<R$) and outside the asteroid, up to a few times $R$. Take $\Phi \to 0$ at infinity.

c) The asteroid actually has the irregular shape shown below. The cavity is still a sphere of radius $R$ centred at $O$, and the rock has the same uniform density everywhere. Would your answers to a) and b) change? Answer yes or no for each, and explain briefly.
```{figure} figures/irregular_asteroid.png
:width: 40%
```

## Problems

### 4. Potential and work
Three identical point masses of $m=1000$kg are in a line, separated by a distance $a/2$, where $a=5$m. How much work must be done to move the centre mass from point $P$ to point $P'$, such that all three masses form an equilateral triangle? 
```{figure} figures/masses_triangle.png
:width: 50%
```

### 5. Gauss's Law and divergence
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

### 6. A conservative field: integrating around a rectangle
The potential of $\vec{F}$ is given by $\left(x^2+y^2\right)^{-1}$.

(a) Find $\vec{F}$.

(b) Describe the field lines of $\vec{F}$.

(c) Describe the equipotential surfaces of $\vec{F}$.

(d) Demonstrate by integration around the perimeter of a rectangle in the $x,y$ plane that $\vec{F}$ is conservative. Let the rectangle extend from $x_1$ to $x_2$ in the $x$ direction and from $y_1$ to $y_2$ in the $y$ direction, and let $x_1 > 0$.

### 7. Laplace equation and physical meaning

A thin metal plate is in steady-state thermal conduction. The thermal conductivity $k$ is constant, and there are no internal heat sources or sinks within the plate. The temperature distribution is proposed to be

```{math}

T(x,y)=T_0+A(x^2-y^2),

```

where $T_0$ and $A$ are constants.

(a) Show that the temperature distribution satisfies Laplace's equation,

```{math}

\nabla^2 T=0.

```

(b) Is the temperature uniform throughout the plate? Explain briefly.

(c) What does $\nabla^2T=0$ mean physically in this problem? Does it mean that there is no heat flow?

(d) The heat flux is given by Fourier's law,

```{math}

\vec{q}=-k\nabla T,

```

where $k$ is the thermal conductivity. Find $\vec{q}$ and describe its direction.
