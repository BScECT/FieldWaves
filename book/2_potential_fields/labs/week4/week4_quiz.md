# Quiz Week 4 (Solutions)


## 1. 
The Earth-ionosphere system can be modeled in a simple way by assuming the Earth to be a perfectly conducting sphere of radius $R_E$, surrounded by a thin, perfectly conducting spherical shell with radius $R_I = R_E + 100\ \text{km}$, with free space between them. The surface of the Earth has a potential $\Phi(r=R_E)=0\ \text{V}$, and the ionosphere has potential $\Phi(r=R_I)=V_I$.

(a) Write the equation you would use to determine the potential in the region $R_E < r < R_I$ in the simplest form possible given the information provided. 

Since the region between the Earth and ionosphere is modeled as free space, we use Laplace's equation:
```{math}
\nabla^2\Phi = 0.
```
The problem has spherical symmetry (there is no dependance on $\phi$ or $\theta$). Thus the equation reduces to
```{math}
\boxed{\frac{1}{r^2}\frac{\partial}{\partial r} \left( r^2 \frac{\partial \Phi}{\partial r} \right)=0}
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