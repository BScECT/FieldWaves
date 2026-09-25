# Quiz Week 4 (Solutions)


## 1. 
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


## 2. 
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
