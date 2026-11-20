# Relation between pressure and particle velocity: impedance

Let us take the solution to the wave equation for the pressure as:

$$
p(x,t) = s(t - x/c)
$$ (eq:pxt)

where $s(t)$ is the function imposed at $x=0$. Often, seismic responses are analyzed in terms of frequencies, i.e., Fourier spectra. The definition used here is:

$$
S(\omega) = \int_{-\infty}^{+\infty} s(t) \exp(- i \omega t) \, dt
$$ (eq:fourier1)

where the radial frequency $\omega$ is used, so $\omega = 2 \pi f$ where $f$ is the (ordinary) frequency. Using this convention, it is easy to show that differentiation with respect to time is equivalent to multiplication with $i\omega$ in the Fourier domain. When we transform the pressure as in {eq}`eq:pxt` to the Fourier domain, we obtain:

$$
P(x,\omega) = S(\omega) \exp (- i\omega x/c).
$$ (eq:Pxw)

Note here that the time delay $x/c$ (in the time domain) becomes a *linear* phase in the Fourier domain, so the phase $(- \omega x/c)$ is linear as a function of $\omega$.

In the above, we gave an expression for the pressure, but one can also derive an equivalent expression for the particle velocity $v_x$. For that purpose, we can use the equation of motion as expressed in {eq}`eq:eqmotion`, but then in its Fourier-transformed version, which is:

$$
V_x(x,\omega) = -\frac{1}{i\omega \rho} \frac{\partial P(x,\omega)}{\partial x}.
$$

When we substitute the solution for the pressure from above ({eq}`eq:Pxw`), we get:

$$
\begin{aligned}
V_x(x,\omega) & = -\frac{1}{i \omega \rho}
                    S(\omega) \frac{- i \omega}{c} \exp(-i\omega x/c)
\\
              & = S(\omega) \frac{1}{\rho c} \exp(-i\omega x/c).
\end{aligned}
$$

Now, it can be observed that the particle velocity is a scaled version of the pressure:

$$
V_x(x,\omega) = \frac{P(x,\omega)}{\rho c}.
$$ (eq:vxp_imp)

The scaling factor ($\rho c$) is called the *seismic impedance*.

(subsec-exerc-imp)=
## Exercise on seismic impedance

In the above, we assumed that the wave was travelling in the positive $x-$direction, i.e., $s(t-x/c)$. Now assume it is travelling in the negative direction, i.e., $s(t+x/c)$:

- Derive the relation between pressure and particle velocity again;
- What is different from the solution above (in {eq}`eq:vxp_imp`)?
