(subsec-wavetheory)=
# Reflection and transmission at boundaries

In this section, we will consider what happens at a boundary between two layers with different mechanical properties. Then we can show which characteristics are responsible for, e.g., a reflection. To that end, we will focus on the basic physical and theoretical principles of reflection and transmission in this section. The basic equations describing wave motion in one direction will be used to derive an expression for the reflection and transmission coefficient at a boundary between two layers with different wave speeds and densities. In the previous section, the solution for the wave equation in the frequency domain was given, i.e.:

$$
P(x,\omega) = S(\omega) \exp (\pm i\omega x/c).
$$

```{figure} figures/refltrans.png
:name: fig-refltrans
:width: 60%

Reflection and transmission at boundary between two media with different wave velocities $(c)$ and densities $(\rho)$.
```

Let us consider {numref}`fig-refltrans`. We defined a plane boundary between two regions with different wave speeds and mass densities. The boundary will reflect some of the energy back, and some will be transmitted. Above the boundary ($x<0$), we will have a so-called incident wave with some amplitude $S(\omega)$. In addition, we have a reflected wave above the boundary, which is travelling in the opposite direction as the incident field. This reflected field has a scaled version of the amplitude of the incident field. This scaling factor is called $R$, which is called the reflection coefficient. Below the boundary ($x>0$), we have a wave travelling in the same direction as the incident field, but has a scaled amplitude due to the transmission through the boundary. We call this amplitude $T$, which is the transmission coefficient. So, above the boundary ($x<0$), we have:

$$
P(x,\omega) = S(\omega) \exp(-i\omega x/c_1) + R S(\omega) \exp(i\omega x/c_1)
$$

Below the boundary ($x>0$), we have:

$$
P(x,\omega) = T S(\omega) \exp(-i\omega x/c_2)
$$

We have defined the reflection and transmission coefficient, but we still need to quantify them. This is achieved by posing the boundary conditions, which are that both the pressure and the particle velocity must be continuous, i.e.:

$$
\lim_{x \uparrow 0} P(x,\omega) = \lim_{x \downarrow 0} P(x,\omega)
$$ (eq:limitp)

$$
\lim_{x \uparrow 0} V_x(x,\omega) = \lim_{x \downarrow 0} V_x(x,\omega)
$$ (eq:limitv)

The first boundary condition can be retrieved directly from the solutions for the pressure. However, for the second boundary condition, we need to use the equation of motion in its Fourier-transformed version, which is:

$$
V_x(x,\omega) = - \frac{1}{i\omega \rho} \frac{\partial P(x,\omega)}{\partial x}
$$

Working these out for the regions above and below the boundary, we obtain, respectively:

$$
\begin{aligned}
V_x(x,\omega) & = S(\omega) \frac{1}{\rho_1 c_1} \exp(-i\omega x/c_1)
		- R S(\omega) \frac{1}{\rho_1 c_1} \exp(i\omega x/c_1)
		& & \text{for } x < 0 \\
V_x(x,\omega) & = T S(\omega) \frac{1}{\rho_2 c_2} \exp(-i\omega x/c_2)
		& & \text{for } x > 0
\end{aligned}
$$

Now we simply substitute the equations in the boundary conditions {eq}`eq:limitp` and {eq}`eq:limitv`, which give:

$$
\begin{aligned}
1 + R & = T
\\
\frac{1}{\rho_1 c_1} - \frac{1}{\rho_1 c_1} R & =
\frac{1}{\rho_2 c_2} T.
\end{aligned}
$$

Working this out, we obtain for the reflection and transmission coefficients $R$ and $T$:

$$
\begin{aligned}
R & = \frac{\rho_2 c_2 - \rho_1 c_1}{\rho_2 c_2 + \rho_1 c_1} \\
T & = \frac{2\rho_2 c_2}{\rho_2 c_2 + \rho_1 c_1}
\end{aligned}
$$

These are the desired expressions. First, notice that we have expressions in terms of seismic impedances, which are the product of the wave speed with the mass density, i.e., $\rho c$. Second, note that the reflection coefficient is determined by the *contrast in the seismic impedances of the different regions*.
