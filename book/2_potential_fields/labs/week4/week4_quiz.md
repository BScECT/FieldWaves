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
 
(b) At $r=a$ and $\theta=3\pi/4$ (dipole latitude $45^\circ$ N), construct $\vec B/B_*$ head to tail from $3(\hat m\cdot\hat r)\hat r$ and $-\hat m$ (W4L2, slide 16). Find $|\vec B|$ in $\mu\mathrm{T}$ and the angle between $\vec B$ and the local horizontal. *Hint:* use $\vec B\cdot\hat r=|\vec B|\cos\alpha$, where $\alpha$ is the angle between $\vec B$ and $\hat r$. The local horizontal is perpendicular to $\hat r$, so the angle between $\vec B$ and the horizontal is $|90^\circ-\alpha|$.
 
(c) ESA's Swarm satellites measure the Earth's magnetic field at about $450\ \mathrm{km}$ altitude. Consider a point directly above the location in (b), i.e. at the same dipole latitude. What happens to the magnitude $|\vec B|$ and direction of $\vec B$?
 
(d) Above the northern end of the dipole axis, at what distance from Earth's centre has the magnetic field magnitude $|\vec B|$ decreased to $1\%$ of its value at Earth's surface ?

## 4. A current loop as a magnetic dipole
Far from a compact current loop, its magnetic field is that of a dipole (W4L2, slide 14). A circular loop carrying current $I$ around an area $A$ has the magnetic moment
```{math}
\vec m = IA\,\hat n,
```
where $\hat n$ is the normal to the loop given by the right-hand rule: curl the fingers along the current, and the thumb gives $\hat n$. Use $\mu_0 = 4\pi\cdot10^{-7}\ \mathrm{T\,m/A}$.
 
(a) In question 3, the magnetic field at Earth's dipole equator and surface was described by $B_*=\mu_0|\vec m|/(4\pi a^3)\approx 29.7\ \mu\mathrm{T}$, with $a=6371\ \mathrm{km}$. Find Earth's dipole moment $|\vec m|$.
 
(b) Earth's field is generated by electric currents in the liquid outer core (the geodynamo). As a size estimate, replace these currents by a single circular loop in the dipole's equatorial plane, with the radius of the outer core, $R_c = 3480\ \mathrm{km}$. What current $I$ is needed? Seen from above the northern end of the dipole axis, does the current circulate clockwise or counterclockwise? *Hint:* Use the right-hand rule: point your right thumb in the direction of $\hat m$, toward the southern end of Earth's dipole axis. Your curled fingers show the direction of the current.
 
(c) A geophysicist lays out a circular wire loop of radius $R_L = 50\ \mathrm{m}$ on flat ground and drives a current $I = 10\ \mathrm{A}$ through it. Find its magnetic moment. On the axis of the loop, at height $z$ above its centre, the exact field is (you do not need to derive it)
```{math}
B_\mathrm{loop}(z) = \frac{\mu_0 I R_L^2}{2\left(R_L^2+z^2\right)^{3/2}}.
```
Starting from the exact loop field, show that when $z \gg R_L$, the field reduces to the dipole field on the axis $B_\mathrm{dip}(z)=\dfrac{\mu_0|\vec m|}{2\pi z^3}$ (corresponding to $\theta=0$ case of question 3).
 
(d) Find $B_\mathrm{loop}$ and $B_\mathrm{dip}$ in nT at $z = 100\ \mathrm{m}$ $(=2R_L)$ and at $z = 250\ \mathrm{m}$ $(=5R_L)$. By how many percent does the dipole formula overestimate the field at each height? Based on these results, for what approximate values of $ z/R_L $ does the dipole approximation become reasonably accurate? *Hint:* $B_\mathrm{dip}/B_\mathrm{loop} = \left(1+R_L^2/z^2\right)^{3/2}$.
 