# Quiz Week 4


## 1. Earth-ionosphere system
The Earth-ionosphere system can be modeled in a simple way by assuming the Earth to be a perfectly conducting sphere of radius $R_E$, surrounded by a thin, perfectly conducting spherical shell with radius $R_I = R_E + 100\ \text{km}$, with free space between them. The surface of the Earth has a potential $\Phi(r=R_E)=0\ \text{V}$, and the ionosphere has potential $\Phi(r=R_I)=V_I$.

```{figure} figures/simple_ionosphere.png
:width: 35%
```

(a) Write the equation you would use to determine the potential in the region $R_E < r < R_I$ in the simplest form possible given the information provided. 

(b) Assume the solution for the potential has the form
```{math}
\Phi(r) = A + \frac{B}{r}.
```
Find expressions for $A$ and $B$, and write the expression for the potential in these terms. 

(c) Find the expression for the electric field, $\vec{E}$, in the region $R_E < r < R_I$. 


(d) Find the numerical values of $A$ and $B$ assuming $R_E=6370\ \text{km}$ and $V_I=100\ \text{kV}$. 


(e) What is the strength of the field at 50 km altitude, and in which direction is it pointing?


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
 
(a) At the surface, $r=a$, find $\vec B/B_*$ at $\theta=0$, $\pi/2$ and $\pi$, and give $|\vec B|$ in $\mu\mathrm{T}$. At each point, determine whether $\vec B$ points into the Earth, out of the Earth or is tangent to the Earth's surface. In which hemisphere does the field enter Earth?
 
(b) At $r=a$ and $\theta=3\pi/4$ (dipole latitude $45^\circ$ N), construct $\vec B/B_*$ head to tail from $3(\hat m\cdot\hat r)\hat r$ and $-\hat m$ (W4L2, slide 16). Find $|\vec B|$ in $\mu\mathrm{T}$ and the angle between $\vec B$ and the local horizontal. *Hint:* use $\vec B\cdot\hat r=|\vec B|\cos\alpha$, where $\alpha$ is the angle between $\vec B$ and $\hat r$.
 
(c) ESA's Swarm satellites measure the Earth's magnetic field at about $450\ \mathrm{km}$ altitude. Consider a point directly above the locaion in (b), i.e. at the same dipole latitude. What happens to the magnitude $|\vec B|$ and direction of $\vec B$?
 
(d) Above the northern end of the dipole axis, at what distance from Earth's centre has the magnetic field magnitude $|\vec B|$ decreased to $1\%$ of its value at Earth's surface ?