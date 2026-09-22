# Electromagnetic diffusive field equations with a source

Maxwell's equations are given by

$$
-\nabla\times\boldsymbol H + \varepsilon\,\partial_t\boldsymbol E + \sigma\boldsymbol E = -\boldsymbol J^e,
$$ (eq:hrel)

$$
\nabla\times\boldsymbol E + \mu\,\partial_t\boldsymbol H = \boldsymbol 0,
$$ (eq:erel)

where the right-hand sides contain the sources that generate the electromagnetic field. In {eq}`eq:hrel`, the source is the electric current dipole $\boldsymbol J^e$ (A/m$^2$), and in {eq}`eq:erel` the source is zero, because no magnetic monopoles have been found. Some electric sources can be approximated by a magnetic current dipole source. A closed current-carrying loop antenna is such an electric current source that is often described as a magnetic dipole, which can be understood from integrating both sides of {eq}`eq:erel` over the area of the loop, performing a scalar product of each term with the unit normal to the loop, and using Stokes' theorem on the curl of the electric field. In the left-hand sides, $\boldsymbol E$ and $\boldsymbol H$ are the electric and magnetic field strengths in V/m and A/m, respectively, and the medium parameters $\varepsilon,\sigma,\mu$ are the electric permittivity and conductivity, and the magnetic permeability, with units of s/($\Omega$m), 1/($\Omega$m), and s$\Omega$/m, respectively. These equations describe in principle the electric, magnetic and electromagnetic fields for all possible time variations, including the static fields discussed before. Here we are interested in the diffusive field regime. We see that {eq}`eq:hrel`, Ampère's law modified by Maxwell, contains both the electric field and the time derivative of the electric field. If we take the divergence of this equation, we obtain

$$
(\sigma + \varepsilon\,\partial_t)\,\nabla\cdot\boldsymbol E = -\nabla\cdot\boldsymbol J^e .
$$

We use the fact that $\boldsymbol D=\varepsilon\boldsymbol E$ and that $\nabla\cdot\boldsymbol D=\rho_f$, with $\rho_f$ being the volume density of free charge (C m$^{-3}$). Substituting this in the equation gives

$$
\partial_t\rho_f = -\nabla\cdot(\sigma\boldsymbol E + \boldsymbol J^e),
$$

which is known as the equation of continuity of electric current, or the charge conservation law. We replace the source by assuming there is an accumulation of free charge $\rho_0$ at $t=0$, which removes the source and replaces it with the initial condition $\rho_f(0)=\rho_0$. If we write the electric field as $\boldsymbol E=\boldsymbol D/\varepsilon$, the equation becomes

$$
\partial_t\rho_f = -\frac{\sigma}{\varepsilon}\rho_f,
$$

the solution of which is known as

$$
\rho_f = \rho_0\exp\left(-\frac{\sigma}{\varepsilon}t\right) = \rho_0\exp(-t/\tau_r),
$$

where $\tau_r=\varepsilon/\sigma$ is known as the charge relaxation time. It is a measure of the time it takes the medium to return to its equilibrium state after it has been disturbed by an electromagnetic wave. First, we learn from this equation the following theorem: *within a region of non-vanishing conductivity there can be no permanent distribution of free charge*. This is the significant equation, because when alternating source currents have oscillation periods much larger than the relaxation time, the effect of $\varepsilon$ can be neglected and we can effectively assume $\varepsilon=0$ in the first Maxwell equation. For most Earth materials, $\varepsilon\lesssim 10^{-9}$ F/m and $\sigma\gtrsim 10^{-4}$ S/m, so for most earth materials under investigation the relaxation time is less than 10 $\mu$s. Hence, for source time function oscillations with periods longer than 0.3 ms, we can safely take $\varepsilon=0$. For now, we assume this is the case. Electromagnetic waves are treated later in the course. We write Maxwell's equations in the diffusive approximation out in components as

$$
\begin{aligned}
-\partial_y H_z + \partial_z H_y + \sigma E_x &= -J_x^e, \\
-\partial_z H_x + \partial_x H_z + \sigma E_y &= -J_y^e, \\
-\partial_x H_y + \partial_y H_x + \sigma E_z &= -J_z^e, \\
\partial_y E_z - \partial_z E_y + \mu\,\partial_t H_x &= 0, \\
\partial_z E_x - \partial_x E_z + \mu\,\partial_t H_y &= 0, \\
\partial_x E_y - \partial_y E_x + \mu\,\partial_t H_z &= 0 .
\end{aligned}
$$

First we link these equations to the 1D heat equation by assuming a one-dimensional problem here as well. If the source is an infinite current sheet with a constant current in the $(x,y)$-plane, it means that all fields are independent of the $x$- and $y$-coordinates and all derivatives $\partial_x$ and $\partial_y$ become zero. Then, when the current has an $x$-component only, we have $J_y^e=J_z^e=0$. We substitute these findings in the equations and find

$$
\begin{aligned}
\partial_z H_y + \sigma E_x &= -J_x^e, \\
-\partial_z H_x + \sigma E_y &= 0, \\
\sigma E_z &= 0, \\
-\partial_z E_y + \mu\,\partial_t H_x &= 0, \\
\partial_z E_x + \mu\,\partial_t H_y &= 0, \\
\mu\,\partial_t H_z &= 0,
\end{aligned}
$$ (eq:plzHy)

which eliminates the vertical electric and magnetic field components and results in two equal but independent sets of two coupled differential equations, one for $E_x,H_y$ and one for $E_y,H_x$, but the latter has no source to generate the fields. The source is taken as $J_x^e(z,t)=\delta(z)W(t)$, which represents the plane electric current sheet in the $(x,y)$-plane at $z=0$ with a current directed along the $x$-axis and with a time function $W(t)$. This means it is a point source in the $z$-direction and of infinite extent in the $x$- and $y$-directions. In the course Signals and Time Series, the delta-function was introduced in time, but we can use it in all coordinates. Here, this leads to equations for $E_x$ and $H_y$, as

$$
\begin{aligned}
\partial_z H_y(z,t) + \sigma E_x(z,t) &= -J_x^e(z,t), \\
\partial_z E_x(z,t) + \mu\,\partial_t H_y(z,t) &= 0 .
\end{aligned}
$$

The diffusive field that satisfies these equations is called the Transverse ElectroMagnetic (TEM) diffusive field. The diffusion equation for the electric field is obtained by eliminating the magnetic field from the two equations above. We do that as follows,

$$
\begin{aligned}
\partial_z\left(\mu\,\partial_t H_y(z,t)\right) + \sigma\mu\,\partial_t E_x(z,t) &= -\mu\,\partial_t J_x^e(z,t), \\
\mu\,\partial_t H_y(z,t) &= -\partial_z E_x(z,t),
\end{aligned}
$$

and substituting the right-hand side of the second equation to replace the term with the magnetic field in the first equation. The electric field is found to satisfy the following diffusion equation:

$$
\partial_z\partial_z E_x - \mu\sigma\,\partial_t E_x = \mu\,\partial_t J_x^e(z,t).
$$ (eq:dee)

For $J_x^e(z,t)=\delta(z)W(t)$, the solution is known and given by

$$
E_x(z,t) = -\int_{t'=0}^{t}\left(\frac{\sigma\mu z^2}{4(t-t')} - \frac{1}{2}\right)\sqrt{\frac{\mu}{4\pi\sigma(t-t')^3}}\exp\left(-\frac{\sigma\mu z^2}{4(t-t')}\right)W(t')\,\mathrm{d}t',
$$ (eq:extW)

where the convolutional integral is present because the function $W(t)$ has not been defined yet. If the current is switched on and kept at a constant value $I$ for all times after $t=0$, $W(t)=0$ for $t<0$ and $W(t)=I$ for $t>0$, the integral can be evaluated explicitly and the solution is

$$
E_x(z,t) = -I\sqrt{\frac{\mu}{4\pi\sigma t}}\exp\left(-\frac{\sigma\mu z^2}{4t}\right), \quad\text{for } t>0 .
$$ (eq:ExtH)

You recognise the similarity with the solution to the heat equation with a Gaussian distribution for the initial temperature on an infinitely long wire. Note that here we make explicit that the expression for the electric field exists only for positive times. This is because $t=0$ is the moment the source is switched on, and physics tells us that the Earth will respond to a source action only at or after the moment the source becomes active, and not before. This is the notion of causality.

## Solution using Fourier transformation

In the course on Signals and Time Series, you have learned Fourier series and the Fourier transformation. In the heat equation for a finite-length wire, we use Fourier series to find solutions, but we can solve partial differential equations with a non-zero source term more formally with the aid of Fourier transformations. We do this by transforming {eq}`eq:dee` to the frequency domain using

$$
\hat{\boldsymbol E}(z,\omega) = \int_{t=0}^{\infty}\exp(-\mathrm{i}\omega t)\,\boldsymbol E(z,t)\,\mathrm{d}t,
$$

to obtain

$$
\partial_z\partial_z\hat E_x - \mathrm{i}\omega\sigma\mu\,\hat E_x = \mathrm{i}\omega\mu\,\hat W(\omega)\,\delta(z).
$$ (eq:dees)

The diacritical hat on the quantities denotes the Fourier transform of the quantity. The time derivative is gone and replaced by an algebraic multiplication with $\mathrm{i}\omega$, and the equation has been reduced to an ordinary second-order differential equation. As you have learned in the course Signals and Time Series, the exponential function is an eigenfunction, so we can propose a solution in the form

$$
\hat E_x = \hat A\exp\left(-\sqrt{\mathrm{i}\omega\mu\sigma}\,|z|\right),
$$

where $\hat A$ is the constant that needs to be determined. The reason why $|z|$ is in the argument of the exponential function is that the field must diffuse away from the source and decrease in amplitude with increasing distance in both the positive and negative $z$-directions. Evaluating the first and second derivatives with respect to $z$ gives

$$
\begin{aligned}
\partial_z\hat E_x &= -\sqrt{\mathrm{i}\omega\sigma\mu}\,\hat A\exp\left(-\sqrt{\mathrm{i}\omega\sigma\mu}\,|z|\right)\frac{z}{|z|}, \\
\partial_z\partial_z\hat E_x &= \mathrm{i}\omega\mu\sigma\,\hat A\exp\left(-\sqrt{\mathrm{i}\omega\sigma\mu}\,|z|\right) - 2\sqrt{\mathrm{i}\omega\sigma\mu}\,\hat A\,\delta(z)\exp\left(-\sqrt{\mathrm{i}\omega\sigma\mu}\,|z|\right), \\
&= \mathrm{i}\omega\sigma\mu\,\hat E_x - 2\sqrt{\mathrm{i}\omega\sigma\mu}\,\hat A\,\delta(z),
\end{aligned}
$$

where we have used the fact that

$$
\mathrm{sign}(z) = \frac{z}{|z|} = \left\{\begin{array}{rl} -1, & z<0, \\ 1, & z>0, \end{array}\right.
$$

is known as the sign-function. It has a sudden step of size 2 at $z=0$, for which reason its derivative is equal to $\partial_z\,\mathrm{sign}(z)=2\delta(z)$. Because the impulse function acts only at $z=0$, we can substitute that already in the exponential function that multiplies the delta-function. If we substitute these results in {eq}`eq:dees` we find that

$$
\hat A = -\frac{\sqrt{\mathrm{i}\omega\mu}}{2\sqrt{\sigma}}\hat W .
$$

The solution for the electric field is then found as

$$
\hat E_x(z,\omega) = -\frac{\sqrt{\mu}}{2\sqrt{\sigma}}\hat W\sqrt{\mathrm{i}\omega}\exp\left(-\sqrt{\mathrm{i}\omega\sigma\mu}\,|z|\right).
$$ (eq:eesd)

This is the space-frequency domain solution for the one-dimensional electric field in the Earth in response to an electric current sheet that is an impulse at $z=0$ but exists for all $x$- and $y$-values, and has a time function $W(t)$. The transformation back to time results in the expression given in {eq}`eq:extW`, and in {eq}`eq:ExtH` in case the source is a step-function switch-on, in which case its frequency transform is given by $\hat W=I/(\mathrm{i}\omega)$. Now we can explain the convolution in time, because you know from the course Signals and Time Series that a product in the frequency domain leads to a convolution in the time domain.

## The concept of the principle of superposition

Before we go to the three-dimensional problem, we take a look at the right-hand side of {eq}`eq:dee` for the given source time function that is switched on at $t=0$ and kept constant after that, and note that $\partial_t u(t)=\delta(t)$, where $u(t)$ is the unit-step function and $\delta(t)$ is the delta-function. In that case the equation for the electric field becomes

$$
\partial_z\partial_z E_x - \mu\sigma\,\partial_t E_x = \mu I\,\delta(t)\,\delta(z).
$$ (eq:deeg)

The function that collapses a differential equation to an impulse in space and time is called the Green's function. Physically, the Green's function describes the (scalar) response to an impulse in space and time. This is a general principle for linear partial differential equations and you have discussed this in the course Signals and Time Series. The equation for the space-time impulse response is then

$$
(\partial_z\partial_z - \mu\sigma\,\partial_t)\,G(z-z',t-t') = -\delta(t-t')\,\delta(z-z'),
$$ (eq:deg)

where the minus sign in the right-hand side is a historic choice. The constant displacements $t'$ and $z'$ are chosen because the real source may have a finite length in the $z$-direction and have a certain time duration. If we now multiply both sides of this equation with a function $-\mu\,\partial_{t'}J_x^e(z',t')$, assume that $J_x^e(z',t')\ne 0$ only for $z_b<z'<z_e$ and $t_b<t'<t_e$, and integrate the resulting equation over all time and space, we find

$$
(\partial_z\partial_z - \mu\sigma\,\partial_t)\int_{z'=z_b}^{z_e}\int_{t'=t_b}^{t_e} -\mu\,G(z-z',t-t')\,\partial_{t'}J_x^e(z',t')\,\mathrm{d}z'\,\mathrm{d}t'
= \mu\int_{z'=z_b}^{z_e}\int_{t'=t_b}^{t_e}\delta(t-t')\,\delta(z-z')\,\partial_{t'}J_x^e(z',t')\,\mathrm{d}z'\,\mathrm{d}t',
$$

and using the sifting property of the delta-function we find

$$
(\partial_z\partial_z - \mu\sigma\,\partial_t)\int_{z'=z_b}^{z_e}\int_{t'=t_b}^{t_e} -\mu\,G(z-z',t-t')\,\partial_{t'}J_x^e(z',t')\,\mathrm{d}z'\,\mathrm{d}t' = \mu\,\partial_t J_x^e(z,t).
$$ (eq:dege)

We recognise the right-hand side of {eq}`eq:dege` as the right-hand side of {eq}`eq:dee`! This means that the integral in the left-hand side of {eq}`eq:dege` is equal to the electric field:

$$
E_x(z,t) = -\mu\int_{z'=z_b}^{z_e}\int_{t'=t_b}^{t_e} G(z-z',t-t')\,\partial_{t'}J_x^e(z',t')\,\mathrm{d}z'\,\mathrm{d}t' .
$$

We conclude that once we have solved for the Earth impulse response, we can make the Earth response to any space-time source function by convolutional integrals. This is why Green's functions are important functions to find. Now we find the three-dimensional diffusive field impulse response.

## The three-dimensional diffusive field impulse response

If we return to the Maxwell equations and find the scalar three-dimensional second-order differential equation, we end up with

$$
(\nabla^2 - \mathrm{i}\omega\sigma\mu)\,\hat G = -\delta(\boldsymbol r-\boldsymbol r'),
$$

and the frequency-domain Green's function is given by

$$
\hat G(\boldsymbol r-\boldsymbol r',\omega) = \frac{\exp\left(-\sqrt{\mathrm{i}\omega\sigma\mu}\,|\boldsymbol r-\boldsymbol r'|\right)}{4\pi|\boldsymbol r-\boldsymbol r'|} .
$$

The space-time domain Green's function is

$$
G(\boldsymbol r-\boldsymbol r',t-t') = \frac{(\sigma\mu)^{1/2}}{(4\pi)^{3/2}(t-t')^{3/2}}\exp\left(-\frac{\sigma\mu|\boldsymbol r-\boldsymbol r'|^2}{4(t-t')}\right), \quad\text{for } t>t',
$$ (eq:G3D)

and it satisfies

$$
(\nabla^2 - \sigma\mu\,\partial_t)\,G = -\delta(\boldsymbol r-\boldsymbol r')\,\delta(t-t') .
$$

Again we recognise the similarity with the solution for the heat equation for an infinitely long wire with an initial temperature that was a Gaussian distribution. It also resembles the 1D diffusive field solution to Maxwell's equations. The major difference is that here the late-time behaviour is proportional to $t^{-3/2}$. The electric and magnetic fields have much more complicated behaviour, but that is far beyond the scope of the present course.

### Brief analysis of the outcome

For a source in the location $\boldsymbol r'$, the field diffuses away in spherical direction and the amplitude only depends on radial distance. The product $\sigma\mu$ is the diffusion constant and has the unit of s/m$^2$. It is a measure of how fast the width of the Gaussian spreads in space for a given time instant.

**Early time behaviour.** The early-time behaviour is similar to what we saw in the 1D heat equation.

**Late time behaviour.** The late-time behaviour is inversely proportional to $t^{3/2}$, which is faster than what we saw in the solutions to the 1D heat and Maxwell diffusion equations.

**Time to the peak.** If we differentiate the Green's function to $t$ and equate the result to zero, we find the time to the peak to be $t-t'=t_p$, at $t_p=\sigma\mu|\boldsymbol r-\boldsymbol r'|^2/6$. The amplitude of the Green's function at the peak time is given by

$$
G(\boldsymbol r-\boldsymbol r',t-t'=t_p) = \frac{3\sqrt{6}\exp(-3/2)}{4\pi^{3/2}\sigma\mu|\boldsymbol r-\boldsymbol r'|^3},
$$

which shows that if you double the distance to the source, the peak amplitude is 8 times smaller.
