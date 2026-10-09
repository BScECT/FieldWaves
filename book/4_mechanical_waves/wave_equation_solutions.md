# Solution(s) to the wave equation

The solution to the wave equation for the pressure is:

$$
p(x,t) = s(t \pm x/c)
$$ (eq:pxt)

where $s(t)$ is some function. Note the dependency on space and time via $(t \pm x/c)$, which denotes that it is a travelling wave, and behaves as a direct wave as discussed in [](./snells_law.md). The sign in the argument depends on the direction the wave is travelling.

Often, seismic responses are analyzed in terms of frequencies, i.e., Fourier spectra. The definition used here is:

$$
G(\omega) = \int_{-\infty}^{+\infty} g(t) \exp(- i \omega t) \, dt
$$ (eq:fourier1)

where the radial frequency $\omega$ is used, so $\omega = 2 \pi f$ where $f$ is the (ordinary) frequency. Using this convention, it is easy to show that differentiation with respect to time is equivalent to multiplication with $i\omega$ in the Fourier domain. When we transform the solution of the wave equation ({eq}`eq:pxt`) to the Fourier domain, we obtain:

$$
P(x,\omega) = S(\omega) \exp (\pm i\omega x/c).
$$ (eq:Pxw)

Note here that the time delay $x/c$ (in the time domain) becomes a *linear* phase in the Fourier domain, so the phase $\pm \omega x/c$ is linear as a function of $\omega$.

In the above, we gave an expression for the pressure, but one can also derive an equivalent expression for the particle velocity $v_x$. For that purpose, we can use the equation of motion as expressed in {eq}`eq:eqmotion`, but then in its Fourier-transformed version, which is:

$$
V_x(x,\omega) = -\frac{1}{i\omega \rho} \frac{\partial P(x,\omega)}{\partial x}.
$$

When we substitute the solution for the pressure from above ({eq}`eq:Pxw`), we get for the negative sign:

$$
\begin{aligned}
V_x(x,\omega) & = -\frac{1}{i \omega \rho}
                    S(\omega) \frac{- i \omega}{c} \exp(-i\omega x/c)
\\
              & = S(\omega) \frac{1}{\rho c} \exp(-i\omega x/c).
\end{aligned}
$$

Notice that the particle velocity is a scaled version of the pressure:

$$
V_x(x,\omega) = \frac{P(x,\omega)}{\rho c}.
$$

The scaling factor is ($\rho c$), being called the *seismic impedance*.
