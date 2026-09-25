# Quiz Week 4 (Solutions)


## 1. Earth-ionosphere system
The Earth-ionosphere system can be modeled in a simple way by assuming the Earth to be a perfectly conducting sphere of radius $R_E$, surrounded by a thin, perfectly conducting spherical shell with radius $R_I = R_E + 100\ \text{km}$, with free space between them. The surface of the Earth has a potential $\Phi(r=R_E)=0\ \text{V}$, and the ionosphere has potential $\Phi(r=R_I)=V_I$.

```{figure} figures/simple_ionosphere.png
:width: 35%
```

(a) Write the equation you would use to determine the potential in the region $R_E < r < R_I$ in the simplest form possible given the information provided. 

Since the region between the Earth and ionosphere is modeled as free space, we use Laplace's equation:
```{math}
\nabla^2\Phi = 0.
```
The problem has spherical symmetry (there is no dependance on $\phi$ or $\theta$). Thus the equation reduces to
```{math}
\boxed{\frac{\partial}{\partial r} \left( r^2 \frac{\partial \Phi}{\partial r} \right) = 0}
```

(b) Assume the solution for the potential has the form
```{math}
\Phi(r) = A + \frac{B}{r}.
```
Find expressions for $A$ and $B$, and write the expression for the potential in these terms. 

Applying the boundary conditions $\Phi(r=R_E)=0$ and $\Phi(r=R_I)=V_I$, we get 
```{math}
A = \frac{-B}{R_E}
```
and 
```{math}
\boxed{B = \frac{V_I}{1/R_I - 1/R_E}}
```
This gives us
```{math}
\boxed{A = \frac{V_I}{R_E(1/R_I - 1/R_E)}}
```
and
```{math}
\boxed{\Phi(r) = V_I\frac{1/R_E - 1/r}{1/R_I - 1/R_E}}
```

(c) Find the expression for the electric field, $\vec{E}$, in the region $R_E < r < R_I$. 

```{math}
\begin{aligned}
\vec{E} &= -\vec{\nabla}\Phi \\
        &= -\frac{\partial}{\partial r} \Phi(r)\ \hat{r} \\
        &= -\left(\frac{-B}{r^2}\right)\ \hat{r} \\
        &= \boxed{\frac{B}{r^2}\ \hat{r}}
\end{aligned}
```

(d) Find the numerical values of $A$ and $B$ assuming $R_E=6370\ \text{km}$ and $V_I=100\ \text{kV}$. 

```{math}
\begin{aligned}
B &= \frac{(100\cdot 10^3)}{1/(6470\cdot 10^3) - 1/(6370\cdot 10^3)} \\
  &= \boxed{-4.12 \cdot 10^{13}\ \mathrm{V \cdot m}}
\end{aligned}
```

```{math}
\begin{aligned}
A &= \frac{-(-4.12 \cdot 10^{13})}{(6370\cdot 10^3)} \\ 
  &= \boxed{6.47 \cdot 10^6\ \mathrm{V}}
\end{aligned}
```

(e) What is the strength of the field at 50 km altitude, and in which direction is it pointing?

```{math}
\begin{aligned}
\vec{E} &= \frac{B}{r^2} \hat{r} \\
        &= \frac{(-4.12 \cdot 10^{13})}{(6420\cdot 10^3)^2} \hat{r} \\
        &= \boxed{-1.00\ \mathrm{V/m}\ \hat{r}}
\end{aligned}
```
The field points radially inward (ie. down), from high potential to low.


## 2. The fair-weather field
On a clear day, the air above flat, open ground carries a downward electric field (W4L1, slides 16–17):
```{math}
\vec{E} \approx -E_0\,\hat{z}, \qquad E_0 \approx 100\ \mathrm{V/m}, \qquad V(z) = E_0 z \quad \text{with } V(0) = 0.
```
Cosmic rays continuously ionise the air, producing free electrons and positive ions such as $\mathrm{N_2^+}$. Wind also lifts charged mineral dust from deserts into the atmosphere. Use $e = 1.602\cdot 10^{-19}\ \mathrm{C}$, $g = 9.81\ \mathrm{m/s^2}$ and $1\ \mathrm{eV} = 1.602\cdot 10^{-19}\ \mathrm{J}$ (the energy an elementary charge gains across $1\ \mathrm{V}$).
 
(a) Sketch the equipotentials and field lines for $0 \leq z \leq 10\ \mathrm{m}$. What is the electric potential $V$ at $z = 2\ \mathrm{m}$, given the reference $V(0) = 0$ ?
 
(b) An electron ($q=-e$) and an $\mathrm{N_2^+}$ ion ($q=+e$) are each moved from the ground to $z = 10\ \mathrm{m}$. For each, find $\Delta V$, $\Delta U$ (in J and in eV) and the work done by the field, $W_\mathrm{field}$.
 
(c) Both particles are released from rest. Which one accelerates upward? In which direction does the resulting current flow?
 
(d) A Saharan dust grain (radius $1\ \mu\mathrm{m}$, density $2650\ \mathrm{kg/m^3}$) carries a negative charge. How many excess electrons does it need for the electric force to balance gravity? Does the answer depend on its height in this model?
 
**(a)** The equipotentials are horizontal planes spaced evenly: every metre up adds $100\ \mathrm{V}$. The field lines are vertical, point downward and are equally spaced, so the field is uniform. At head height,
```{math}
V(2\ \mathrm{m}) = E_0 z = (100)(2) = \boxed{200\ \mathrm{V}}.
```
The potential increases upward, while $\vec{E}$ points down, from high to low potential.
 
**(b)** The potential difference does not depend on the test charge:
```{math}
\Delta V = V(10\ \mathrm{m}) - V(0) = \boxed{1000\ \mathrm{V}}.
```
Using $\Delta U = q\Delta V$ and $W_\mathrm{field} = -\Delta U$ (W4L1, slide 13):
 
| | $q$ | $\Delta U$ | $W_\mathrm{field}$ |
|---|---|---|---|
| electron | $-e$ | $-1.60\cdot 10^{-16}\ \mathrm{J} = -1000\ \mathrm{eV}$ | $+1.60\cdot 10^{-16}\ \mathrm{J}$ |
| $\mathrm{N_2^+}$ ion | $+e$ | $+1.60\cdot 10^{-16}\ \mathrm{J} = +1000\ \mathrm{eV}$ | $-1.60\cdot 10^{-16}\ \mathrm{J}$ |
 
Moving up the electron *loses* potential energy, because the field does positive work on it. The ion *gains* potential energy, because the field works against the motion. Same $\Delta V$, opposite energies.
 
**(c)** The force is $\vec{F} = q\vec{E} = q(-E_0\hat{z})$.
- Electron: $\vec{F} = (-e)(-E_0\hat{z}) = +eE_0\hat{z} = +1.6\cdot 10^{-17}\ \mathrm{N}\,\hat{z}$. It **accelerates upward**, toward lower potential energy.
- Ion: $\vec{F} = -eE_0\hat{z}$. It accelerates downward.
Positive charge moving down and negative charge moving up both give a **downward** current. This is the small fair-weather current of the global atmospheric electrical circuit, which flows downward through fair-weather regions because air is a poor, but not perfect, insulator. Thunderstorms help maintain the potential difference between the upper atmosphere and the ground that drives it (W4L1, slide 16).
 
**(d)** The mass of the grain is
```{math}
m = \tfrac{4}{3}\pi a^3 \rho = \tfrac{4}{3}\pi (10^{-6})^3 (2650) = 1.11\cdot 10^{-14}\ \mathrm{kg}.
```
A negative charge feels an upward force (see (c)), so it can balance gravity when $|q|E_0 = mg$:
```{math}
|q| = \frac{mg}{E_0} = \frac{(1.11\cdot 10^{-14})(9.81)}{100} = 1.09\cdot 10^{-15}\ \mathrm{C},
\qquad N = \frac{|q|}{e} \approx \boxed{6.8\cdot 10^{3}\ \text{electrons}}.
```
In this model, $\vec{E}$ is uniform, so the answer **does not depend on height**. The linear potential is only valid near the ground (W4L1, slide 17). In real dust storms, the field near the ground can be much stronger than $E_0$, so far less charge is needed.

## 3. Earth's magnetic field
Far from a compact current system, its magnetic field is that of a dipole (W4L2, slides 14–15). Earth's main field is modelled as a dipole at Earth's centre. As in the lecture, let $\hat m=\hat z$, let $\theta$ be the angle measured from $\hat m$, and work in the $x$–$z$ plane with $\hat r=\sin\theta\,\hat x+\cos\theta\,\hat z$ (slide 22). The field is
```{math}
\vec B = B_*\left(\frac{R}{r}\right)^3\left[3(\hat m\cdot\hat r)\,\hat r-\hat m\right],
\qquad B_*=\frac{\mu_0|\vec m|}{4\pi R^3}.
```
For Earth, take $R=a=6371\ \mathrm{km}$ and $B_*\approx 29.7\ \mu\mathrm{T}$ (called $B_0$ in the teachbook section *Earth as a Magnetic Dipole*). For the present polarity, $\hat m$ points toward the **southern** end of the dipole axis: $\theta=0$ is the southern end, $\theta=\pi$ the northern end, and $\theta=\pi/2$ the dipole equator.
 
```{figure} figures/earth_dipole_setup.png
:width: 45%
 
Geometry of the dipole model, as in W4L2, slides 17 and 22: $\hat m=\hat z$ points up the page, $\theta$ is measured from $\hat m$, and the grey arrows show $\hat r$ at the points used in (a) and (b). The dashed circle is Earth's surface, $r=a$.
```
 
(a) At the surface, $r=a$, find $\vec B/B_*$ at $\theta=0$, $\pi/2$ and $\pi$, and give $|\vec B|$ in $\mu\mathrm{T}$. At each point, does the field point out of the ground, into it, or along it? In which hemisphere does the field enter Earth?
 
(b) At $r=a$ and $\theta=3\pi/4$ (dipole latitude $45^\circ$ N), construct $\vec B/B_*$ head to tail from $3(\hat m\cdot\hat r)\hat r$ and $-\hat m$ (W4L2, slide 16). Find $|\vec B|$ in $\mu\mathrm{T}$ and the angle between $\vec B$ and the local horizontal. *Hint:* use $\vec B\cdot\hat r=|\vec B|\cos\alpha$, where $\alpha$ is the angle between $\vec B$ and $\hat r$.
 
(c) ESA's Swarm satellites measure the field at about $450\ \mathrm{km}$ altitude. What is $|\vec B|$ directly above the point in (b)? Does the direction of $\vec B$ change?
 
(d) At what distance from Earth's centre, above the northern end of the axis, has $|\vec B|$ dropped to $1\%$ of its surface value?
 
**(a)** At $r=a$ the factor $(R/r)^3$ equals 1.
- $\theta=0$: $\hat r=\hat z$, $\hat m\cdot\hat r=1$, so $\vec B/B_*=3\hat z-\hat z=2\hat z=2\hat r$. The field points **out of the ground**, with $|\vec B|=2B_*=\boxed{59.4\ \mu\mathrm{T}}$.
- $\theta=\pi/2$: $\hat r=\hat x$, $\hat m\cdot\hat r=0$, so $\vec B/B_*=-\hat z$. The field is **along the ground** (horizontal), pointing from the southern toward the northern end of the axis, with $|\vec B|=B_*=\boxed{29.7\ \mu\mathrm{T}}$.
- $\theta=\pi$: $\hat r=-\hat z$, $\hat m\cdot\hat r=-1$, so $\vec B/B_*=3(-1)(-\hat z)-\hat z=2\hat z=-2\hat r$. The field points **into the ground**, with $|\vec B|=\boxed{59.4\ \mu\mathrm{T}}$.
The field leaves Earth in the southern hemisphere and **enters Earth in the northern hemisphere**. The field at the poles is twice as strong as at the equator (W4L2, slide 17).
 
**(b)** At $\theta=3\pi/4$: $\hat r=\tfrac{1}{\sqrt2}(\hat x-\hat z)$ and $\hat m\cdot\hat r=\cos\tfrac{3\pi}{4}=-\tfrac{1}{\sqrt2}$. Then
```{math}
3(\hat m\cdot\hat r)\hat r=-\tfrac32(\hat x-\hat z)=-\tfrac32\hat x+\tfrac32\hat z,
\qquad
\frac{\vec B}{B_*}=-\tfrac32\hat x+\tfrac32\hat z-\hat z=\boxed{-\tfrac32\hat x+\tfrac12\hat z}.
```
This is the $\theta=3\pi/4$ arrow of the slide 22 practice. Its magnitude equals that of the slide 16 example:
```{math}
|\vec B|=B_*\sqrt{\tfrac94+\tfrac14}=1.58\,B_*=\boxed{47.0\ \mu\mathrm{T}}.
```
For the direction, $\vec B\cdot\hat r=B_*\tfrac{1}{\sqrt2}\left(-\tfrac32-\tfrac12\right)=-\sqrt2\,B_*$, so
```{math}
\cos\alpha=\frac{-\sqrt2}{1.58}=-0.894,\qquad \alpha=153.4^\circ.
```
$\vec B$ makes $153.4^\circ-90^\circ=\boxed{63.4^\circ}$ with the horizontal and points **into the ground** ($\vec B\cdot\hat r<0$). It is twice as steep as the $45^\circ$ radius.
 
```{figure} figures/earth_dipole_vectors_solution.png
:width: 95%
 
Left: $\vec B/B_*$ at the four points of (a) and (b), drawn with one arrow scale (compare W4L2, slide 17). Right: the head-to-tail construction at $\theta=3\pi/4$ (compare slide 16). The field points into the ground, $63.4^\circ$ below the local horizontal.
```
 
**(c)** The bracket depends only on directions; the distance enters only through $(R/r)^3$ (W4L2, slide 15). With $r=6371+450=6821\ \mathrm{km}$,
```{math}
|\vec B|=47.0\ \mu\mathrm{T}\times\left(\frac{6371}{6821}\right)^3=47.0\times0.815=\boxed{38.3\ \mu\mathrm{T}}.
```
The **direction does not change**: at the same $\theta$, $\hat r$ and the bracket are the same.
 
**(d)** Along the axis, $|\vec B|=2B_*(a/r)^3$, so the ratio to the surface value is $(a/r)^3$:
```{math}
\left(\frac{a}{r}\right)^3=0.01
\quad\Longrightarrow\quad
r=100^{1/3}a=4.64\,a\approx\boxed{2.96\cdot10^{4}\ \mathrm{km}}.
```
Each doubling of the distance reduces the field by a factor of 8 (W4L2, slide 18), and $2^{2.2}\approx4.6$. The same distance holds at every $\theta$, because the ratio depends only on $r$.
 