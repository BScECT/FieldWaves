# Wave fields in a fluid: acoustic (P) waves

With acoustic waves, we assume a fluid in which no shear forces exist, and therefore only P-waves exist. Since waves are physical phenomena, they should have a relation to basic physical laws. The two laws applicable are the conservation of mass and Newton's second law. These two have been used in [the appendix on 1-D acoustic wave motion](./appendix_acoustic_1d.md) to derive the two equations governing the wave motion due to a P-wave. There are some simplifying assumptions in the derivation, one of them being that we consider a 1-dimensional wave. When we denote $p$ as the pressure and $v_x$ as the particle velocity, the conservation of mass leads to:

$$
- \frac{1}{K} \frac{\partial p}{\partial t} = \frac{\partial v_x}{\partial x}
$$ (eq:eqdeform)

in which $K$ is called the bulk modulus. The other relation follows from an application of Newton's law:

$$
-\frac{\partial p}{\partial x} = \rho \frac{\partial v_x}{\partial t}
$$ (eq:eqmotion)

where $\rho$ denotes the mass density. This equation is called the equation of motion.

We are now going to combine these two equations. Therefore, we let the operator $\partial / \partial x$ work on the equation of motion:

$$
- \frac{\partial}{\partial x} \left( \frac{\partial p}{\partial x} \right)
 =
 \frac{\partial}{\partial x}
    \left( \rho \frac{\partial v_x}{\partial t} \right).
$$ (eq:diffeqmotion)

Now, assuming $\rho$ is constant, it can be taken in front of the $\partial / \partial x$ operator. And differentiations with respect to space $x$ and time $t$ are commutative, so:

$$
  \frac{\partial}{\partial x} \left( \frac{\partial v_x}{\partial t} \right)
  =
  \frac{\partial}{\partial t} \left( \frac{\partial v_x}{\partial x} \right).
$$ (eq:commut)

Now for $\partial v_x / \partial x$, the conservation of mass can be substituted in {eq}`eq:diffeqmotion` to give:

$$
   -\frac{\partial^2 p}{\partial x^2} = \rho
  \frac{\partial}{\partial t}
        \left( - \frac{1}{K} \frac{\partial p}{\partial t} \right).
$$

Rewriting gives us the 1-Dimensional wave equation:

$$
\frac{\partial^2 p}{\partial x^2}
	- \frac{1}{c^2} \frac{\partial^2p}{\partial t^2} = 0
$$

in which $c$ can be seen as the velocity of the wave, for which we have: $c = \sqrt{K/ \rho}$.

This is the basic wave equation for one-dimensional acoustic waves. Equally well, we can derive from the same two equations {eq}`eq:eqdeform` and {eq}`eq:eqmotion` (see also *EXERCISES*) that the particle velocity also satisfies the wave equation:

$$
\frac{\partial^2 v_x}{\partial x^2}
	- \frac{1}{c^2} \frac{\partial^2 v_x}{\partial t^2} = 0
$$ (eq:waveqacv)

where $c$ is the same as in the wave equation of the pressure.

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
