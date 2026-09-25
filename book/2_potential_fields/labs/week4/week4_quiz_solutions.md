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
 
**(a)** The equipotentials are horizontal planes spaced evenly: every metre up adds $100\ \mathrm{V}$. The field lines are vertical, point downward and are equally spaced, so the field is uniform. At head height,
```{math}
V(2\ \mathrm{m}) = E_0 z = (100)(2) = \boxed{200\ \mathrm{V}}.
```
The potential increases upward, while $\vec{E}$ points down, from high to low potential.
 
(b) An electron ($q=-e$) and an $\mathrm{N_2^+}$ ion ($q=+e$) are each moved from the ground to $z = 10\ \mathrm{m}$. For each, find $\Delta V$, $\Delta U$ (in J and in eV) and the work done by the field, $W_\mathrm{field}$.
 
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
 
(c) Both particles are released from rest. Which one accelerates upward? In which direction does the resulting current flow?
 
**(c)** The force is $\vec{F} = q\vec{E} = q(-E_0\hat{z})$.
- Electron: $\vec{F} = (-e)(-E_0\hat{z}) = +eE_0\hat{z} = +1.6\cdot 10^{-17}\ \mathrm{N}\,\hat{z}$. It **accelerates upward**, toward lower potential energy.
- Ion: $\vec{F} = -eE_0\hat{z}$. It accelerates downward.
Positive charge moving down and negative charge moving up both give a **downward** current. This is the small fair-weather current of the global atmospheric electrical circuit, which flows downward through fair-weather regions because air is a poor, but not perfect, insulator. Thunderstorms help maintain the potential difference between the upper atmosphere and the ground that drives it (W4L1, slide 16).
 
(d) A Saharan dust grain (radius $1\ \mu\mathrm{m}$, density $2650\ \mathrm{kg/m^3}$) carries a negative charge. How many excess electrons does it need for the electric force to balance gravity? Does the answer depend on its height in this model?
 
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
 
Written in the local directions $\hat r$ (outward) and $\hat\theta$ (tangent to the surface, in the direction of increasing $\theta$), the same field is
```{math}
\frac{\vec B}{B_*} = \left(\frac{R}{r}\right)^3\left(2\cos\theta\,\hat r + \sin\theta\,\hat\theta\right),
\qquad\text{that is}\qquad
B_r = 2B_*\left(\frac{R}{r}\right)^3\cos\theta,
\quad
B_\theta = B_*\left(\frac{R}{r}\right)^3\sin\theta .
```
You may use either form.
 
```{figure} figures/earth_dipole_setup.png
:width: 45%
 
Geometry of the dipole model, as in W4L2, slides 17 and 22: $\hat m=\hat z$ points up the page, $\theta$ is measured from $\hat m$, and the grey arrows show $\hat r$ at the points used in (a) and (b). The dashed circle is Earth's surface, $r=a$.
```
 
(a) At the surface, $r=a$, find $\vec B/B_*$ at $\theta=0$ and $\pi/2$, and give $|\vec B|$ in $\mu\mathrm{T}$. At each point, determine whether $\vec B$ points into the Earth, out of the Earth or is tangent to the Earth's surface. Using $B_r\propto\cos\theta$, in which hemisphere does the field enter Earth?
 
**(a)** At $r=a$ the factor $(R/r)^3$ equals 1.
- $\theta=0$: $\hat r=\hat z$, $\hat m\cdot\hat r=1$, so $\vec B/B_*=3\hat z-\hat z=2\hat z=2\hat r$. The field points **out of the ground**, with $|\vec B|=2B_*=\boxed{59.4\ \mu\mathrm{T}}$.
- $\theta=\pi/2$: $\hat r=\hat x$, $\hat m\cdot\hat r=0$, so $\vec B/B_*=-\hat z$. The field is **along the ground** (horizontal), pointing from the southern toward the northern end of the axis, with $|\vec B|=B_*=\boxed{29.7\ \mu\mathrm{T}}$.
Since $B_r=2B_*\cos\theta$, the radial component is positive (outward) for $\theta<\pi/2$ and negative (inward) for $\theta>\pi/2$. The field therefore leaves Earth in the southern hemisphere and **enters Earth in the northern hemisphere**; at $\theta=\pi$ it is $2\hat z=-2\hat r$, the mirror image of $\theta=0$. The field at the poles is twice as strong as at the equator (W4L2, slide 17).
 
(b) At $r=a$ and $\theta=3\pi/4$ (dipole latitude $45^\circ$ N), construct $\vec B/B_*$ head to tail from $3(\hat m\cdot\hat r)\hat r$ and $-\hat m$ (W4L2, slide 16). Find $|\vec B|$ in $\mu\mathrm{T}$ and the angle between $\vec B$ and the local horizontal. *Hint:* use $\vec B\cdot\hat r=|\vec B|\cos\alpha$, where $\alpha$ is the angle between $\vec B$ and $\hat r$. The local horizontal is perpendicular to $\hat r$, so the angle between $\vec B$ and the horizontal is $|90^\circ-\alpha|$.
 
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
Because $\hat r$ points outward, $\alpha>90^\circ$ already tells us that the radial component is inward: the field points **into the ground**, as it must in the northern hemisphere by part (a).

$\hat r$ is the local vertical, so an angle measured from $\hat r$ and an angle measured from the local horizontal are complements. The field therefore lies
```{math}
|90^\circ-153.4^\circ|=\boxed{63.4^\circ}
```
below the horizontal. Note that $\tan I=|B_r|/B_\theta=2\tan\lambda_m$: at dipole latitude $45^\circ$ it is the *tangent* of the inclination that is doubled, not the angle. That relation is derived in lab exercise 3(e).
 
The component form gives the same result in one step: $B_r/B_*=2\cos\tfrac{3\pi}{4}=-\sqrt2$ and $B_\theta/B_*=\sin\tfrac{3\pi}{4}=\tfrac{1}{\sqrt2}$, so $|\vec B|=B_*\sqrt{2+\tfrac12}=1.58\,B_*$ and $\tan I=|B_r|/B_\theta=2$, i.e. $I=63.4^\circ$ below the horizontal.
 
```{figure} figures/earth_dipole_vectors_solution.png
:width: 95%
 
Left: $\vec B/B_*$ at the points of (a) and (b), together with the northern end, drawn with one arrow scale (compare W4L2, slide 17). Right: the head-to-tail construction at $\theta=3\pi/4$ (compare slide 16). The field points into the ground, $63.4^\circ$ below the local horizontal.
```
 
(c) ESA's Swarm satellites measure the Earth's magnetic field at about $450\ \mathrm{km}$ altitude. Consider a point directly above the location in (b), i.e. at the same dipole latitude. What happens to the magnitude $|\vec B|$ and direction of $\vec B$?
 
**(c)** The bracket depends only on directions; the distance enters only through $(R/r)^3$ (W4L2, slide 15). With $r=6371+450=6821\ \mathrm{km}$,
```{math}
|\vec B|=47.0\ \mu\mathrm{T}\times\left(\frac{6371}{6821}\right)^3=47.0\times0.815=\boxed{38.3\ \mu\mathrm{T}}.
```
The **direction does not change**: at the same $\theta$, $\hat r$ and the bracket are the same.
 
(d) Above the northern end of the dipole axis, at what distance from Earth's centre has the magnetic field magnitude $|\vec B|$ decreased to $1\%$ of its value at Earth's surface ?
 
**(d)** Along the axis, $|\vec B|=2B_*(a/r)^3$, so the ratio to the surface value is $(a/r)^3$:
```{math}
\left(\frac{a}{r}\right)^3=0.01
\quad\Longrightarrow\quad
r=100^{1/3}a=4.64\,a\approx\boxed{2.96\cdot10^{4}\ \mathrm{km}}.
```
Each doubling of the distance reduces the field by a factor of 8 (W4L2, slide 18), and $2^{2.2}\approx4.6$. The same distance holds at every $\theta$, because the ratio depends only on $r$.


## 4. A current loop as a magnetic dipole
 
Far from a compact current loop, its magnetic field is that of a dipole (W4L2, slide 14). A circular loop carrying current $I$ around an area $A$ has the magnetic moment
```{math}
\vec m = IA\,\hat n,
```
where $\hat n$ is the normal to the loop given by the right-hand rule: curl the fingers along the current, and the thumb gives $\hat n$. Use $\mu_0 = 4\pi\cdot10^{-7}\ \mathrm{T\,m/A}$.
 
(a) In question 3, the magnetic field at Earth's dipole equator and surface was described by $B_*=\mu_0|\vec m|/(4\pi a^3)\approx 29.7\ \mu\mathrm{T}$, with $a=6371\ \mathrm{km}$. Find Earth's dipole moment $|\vec m|$.
 
**(a)** Rearranging $B_*=\mu_0|\vec m|/(4\pi a^3)$,
```{math}
|\vec m| = \frac{4\pi a^3 B_*}{\mu_0}
= \frac{4\pi (6.371\cdot 10^{6})^3 (29.7\cdot 10^{-6})}{4\pi\cdot 10^{-7}}
= \boxed{7.7\cdot 10^{22}\ \mathrm{A\,m^2}},
```
which is the accepted value for Earth's dipole moment.
 
(b) Earth's field is generated by electric currents in the liquid outer core (the geodynamo). As a size estimate, replace these currents by a single circular loop in the dipole's equatorial plane, with the radius of the outer core, $R_c = 3480\ \mathrm{km}$. What current $I$ is needed? Seen from above the northern end of the dipole axis, does the current circulate clockwise or counterclockwise? *Hint:* Use the right-hand rule: point your right thumb in the direction of $\hat m$, toward the southern end of Earth's dipole axis. Your curled fingers show the direction of the current.
 
**(b)** The loop area is $A=\pi R_c^2=\pi(3.48\cdot 10^{6})^2=3.81\cdot 10^{13}\ \mathrm{m^2}$, so
```{math}
I = \frac{|\vec m|}{A} = \frac{7.68\cdot 10^{22}}{3.81\cdot 10^{13}}
= \boxed{2.0\cdot 10^{9}\ \mathrm{A}} \approx 2\ \mathrm{GA}.
```
$\hat m$ points toward the **southern** end of the dipole axis (question 3). Pointing the right thumb that way, the fingers curl so that the current runs **clockwise seen from above the northern end** of the axis.

Two billion amperes is enormous for a single wire, but the geodynamo is a broad, distributed flow of conducting liquid iron, not one loop. The estimate gives the right order of magnitude for the total circulating current.
 
(c) A geophysicist lays out a circular wire loop of radius $R_L = 50\ \mathrm{m}$ on flat ground and drives a current $I = 10\ \mathrm{A}$ through it. Find its magnetic moment. On the axis of the loop, at height $z$ above its centre, the exact field is (you do not need to derive it)
```{math}
B_\mathrm{loop}(z) = \frac{\mu_0 I R_L^2}{2\left(R_L^2+z^2\right)^{3/2}}.
```
Starting from the exact loop field, show that when $z \gg R_L$, the field reduces to the dipole field on the axis $B_\mathrm{dip}(z)=\dfrac{\mu_0|\vec m|}{2\pi z^3}$ (corresponding to $\theta=0$ case of question 3).
 
**(c)** The moment of the field loop is
```{math}
|\vec m| = IA = I\pi R_L^2 = (10)\pi(50)^2 = \boxed{7.9\cdot 10^{4}\ \mathrm{A\,m^2}}.
```
Factor $z^3$ out of the exact expression:
```{math}
B_\mathrm{loop}(z) = \frac{\mu_0 I R_L^2}{2\left(R_L^2+z^2\right)^{3/2}}
= \frac{\mu_0 I R_L^2}{2z^3\left(1+R_L^2/z^2\right)^{3/2}}.
```
For $z \gg R_L$ the bracket tends to 1, and writing $I R_L^2 = |\vec m|/\pi$,
```{math}
B_\mathrm{loop} \to \frac{\mu_0 I R_L^2}{2z^3} = \boxed{\frac{\mu_0|\vec m|}{2\pi z^3} = B_\mathrm{dip}(z)},
```
the on-axis dipole field, which is the $\theta=0$ case of question 3. The loop only looks like a dipole from far enough away that its size no longer matters.
 
(d) Find $B_\mathrm{loop}$ and $B_\mathrm{dip}$ in nT at $z = 100\ \mathrm{m}$ $(=2R_L)$ and at $z = 250\ \mathrm{m}$ $(=5R_L)$. By how many percent does the dipole formula overestimate the field at each height? Based on these results, for what approximate values of $ z/R_L $ does the dipole approximation become reasonably accurate? *Hint:* $B_\mathrm{dip}/B_\mathrm{loop} = \left(1+R_L^2/z^2\right)^{3/2}$.
 
**(d)** Using the two expressions directly:

| $z$ | $z/R_L$ | $B_\mathrm{loop}$ | $B_\mathrm{dip}$ | overestimate |
|---|---|---|---|---|
| $100\ \mathrm{m}$ | 2 | $11.2\ \mathrm{nT}$ | $15.7\ \mathrm{nT}$ | $40\%$ |
| $250\ \mathrm{m}$ | 5 | $0.95\ \mathrm{nT}$ | $1.01\ \mathrm{nT}$ | $6\%$ |

The hint gives the error directly, since
```{math}
\frac{B_\mathrm{dip}}{B_\mathrm{loop}} = \left(1+\frac{R_L^2}{z^2}\right)^{3/2}
\approx 1 + \frac{3}{2}\frac{R_L^2}{z^2} \quad (z \gg R_L),
```
so the overestimate falls off as $(R_L/z)^2$: $40\%$ at $z/R_L=2$, $6\%$ at $5$, $1.5\%$ at $10$ and $0.4\%$ at $20$. The dipole formula is therefore **reasonably accurate for $z/R_L \gtrsim 5$**, and good to about a percent for $z/R_L \gtrsim 10$. The same rule of thumb is why Earth's field is well described by a dipole at satellite altitude, but not close to the core.
