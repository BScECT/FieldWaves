# Electromagnetic diffusive field equations with a source

Maxwell's equations are given by

$$
-\nabla\times\boldsymbol H + \varepsilon\,\partial_t\boldsymbol E + \sigma\boldsymbol E = -\boldsymbol J^e,
$$ (eq:hrel)

$$
\nabla\times\boldsymbol E + \mu\,\partial_t\boldsymbol H = \boldsymbol 0,
$$ (eq:erel)

where the right-hand sides contain the sources that generate the electromagnetic field. In {eq}`eq:hrel`, the source is the electric current dipole $\boldsymbol J^e$ (A/m$^2$), and in {eq}`eq:erel` the source is zero, because no magnetic monopoles have been found. Some electric sources can be approximated by a magnetic current dipole source. A closed current-carrying loop antenna is such an electric current source that is often described as a magnetic dipole, which can be understood from integrating both sides of {eq}`eq:erel` over the area of the loop, performing a scalar product of each term with the unit normal to the loop, and using Stokes' theorem on the curl of the electric field. In the left-hand sides, $\boldsymbol E$ and $\boldsymbol H$ are the electric and magnetic field strengths in V/m and A/m, respectively, and the medium parameters $\varepsilon,\sigma,\mu$ are the electric permittivity and conductivity, and the magnetic permeability, with units of s/($\Omega$m), 1/($\Omega$m), and s$\Omega$/m, respectively. These equations describe in principle the electric, magnetic and electromagnetic fields for all possible time variations, including the static fields discussed before. Here we are interested in the diffusive field regime.

:::{admonition} A new bridge to wave fields to distinguish them from diffusive fields
:class: important

We see that {eq}`eq:hrel` is Ampère's law modified by Maxwell contains both the electric field and the time derivative of the electric field. We take the divergence of this equation and obtain

$$
(\sigma + \varepsilon\,\partial_t)\,\nabla\cdot\boldsymbol E = -\nabla\cdot\boldsymbol J^e .
$$

If we use the fact the $\boldsymbol D=\varepsilon\boldsymbol E$ and that $\nabla\cdot\boldsymbol D=\rho_f$ with $\rho_f$ being the volume density of free charge (C m$^{-3}$). Substituting this in the equation gives

$$
\partial_t\rho_f = -\nabla\cdot(\sigma\boldsymbol E + \boldsymbol J^e).
$$

You have seen this equation without the external source term in the section on 'Steady Currents, Charge Conservation, and a Bridge to Waves'. This is known as the equation of continuity of electric current, or the charge conservation law. Here we continue the bridge to waves and by assuming there is an accumulation of free charge of $\rho_0$ at $t=0$. We remove the source and replace it with the initial condition that $\rho_f(0)=\rho_0$. We write the electric field as $\boldsymbol E=\boldsymbol D/\varepsilon$, and find

$$
\partial_t\rho_f = -\frac{\sigma}{\varepsilon}\rho_f,
$$

the solution of which is known as

$$
\rho_f = \rho_0\exp\left(-\frac{\sigma}{\varepsilon}t\right) = \rho_0\exp(-t/\tau_r),
$$

with $\tau_r=\varepsilon/\sigma$ is known as the charge relaxation time and it is a measure of the time it takes the medium to return to its equilibrium state after it has been disturbed by an electromagnetic wave. First, we learn from this equation the following theorem:

**_Within a region of non-vanishing conductivity there can be no permanent distribution of free charge_**.

This is the significant equation, because when alternating source currents have oscillation periods much larger than the relaxation time, the effect of $\varepsilon$ can be neglected and we can effectively assume $\varepsilon=0$ in the first Maxwell equation. For all Earth materials, $\varepsilon < 10^{-9}$ F/m and $\sigma\gtrsim 10^{-4}$ S/m for most earth materials under investigation the relaxation time is less than 10 $\mu$s. Hence, for source time function oscillations with periods less than 0.3 $\mu$s, the electromagnetic field will be a wave field, whereas for source time function oscillations with periods longer than 0.3 ms, we can safely take $\varepsilon=0$. Electromagnetic waves are treated later in the course.
:::

We write Maxwell's equations in the diffusive approximation out in components as,

$$
\begin{aligned}
-\partial_y H_z + \partial_z H_y + \sigma E_x &= -J_x^e, \\
-\partial_z H_x + \partial_x H_z + \sigma E_y &= -J_y^e, \\
-\partial_x H_y + \partial_y H_x + \sigma E_z &= -J_z^e,
\end{aligned}
$$

$$
\begin{aligned}
\partial_y E_z - \partial_z E_y + \mu\,\partial_t H_x &= 0, \\
\partial_z E_x - \partial_x E_z + \mu\,\partial_t H_y &= 0, \\
\partial_x E_y - \partial_y E_x + \mu\,\partial_t H_z &= 0 .
\end{aligned}
$$

First we link these equations to the 1D heat equation by assuming a one-dimensional problem here as well.

## Maxwell's equations in one dimension with a source

If the source is an infinite current sheet with a constant current in the $(x,y)$-plane and the medium parameters $\sigma$ and $\mu$ are constant, it means that all fields are independent of the $x$- and $y$-coordinates and the derivatives $\partial_x$ and $\partial_y$ become zero. Then, when the current has an $x$-component only, we have $J_y^e=J_z^e=0$. We substitute these findings in the equations and find

$$
\begin{aligned}
\partial_z H_y + \sigma E_x &= -J_x^e, \\
-\partial_z H_x + \sigma E_y &= 0, \\
\sigma E_z &= 0, \\
-\partial_z E_y + \mu\,\partial_t H_x &= 0, \\
\partial_z E_x + \mu\,\partial_t H_y &= 0, \\
\mu\,\partial_t H_z &= 0,
\end{aligned}
$$

which eliminates the vertical electric and magnetic field components and results in two equal but independent sets of two coupled differential equations, one for $E_x,H_y$ and one for $E_y,H_x$, but the latter has no source to generate the fields and without a generating source, they will be zero. This leads to equations for $E_x$ and $H_y$, as

$$
\partial_z H_y(z,t) + \sigma E_x(z,t) = -J_x^e(z,t),
$$ (eq:plzHy)

$$
\partial_z E_x(z,t) + \mu\,\partial_t H_y(z,t) = 0 .
$$

The diffusive field that satisfies this equation is called the Transverse ElectroMagnetic (TEM) diffusive field, because both the electric and magnetic fields are transverse (perpendicular) to the propagation direction. The diffusion equation for the electric field is obtained by eliminating the magnetic field from the two equations above. We do that as follows, we multiply both sides of {eq}`eq:plzHy` with $\mu$ and apply a time derivative, which leads to,

$$
\partial_z\left(\mu\,\partial_t H_y(z,t)\right) + \sigma\mu\,\partial_t E_x(z,t) = -\mu\,\partial_t J_x^e(z,t),
$$ (eq:plzpltHy)

$$
\mu\,\partial_t H_y(z,t) = -\partial_z E_x(z,t).
$$ (eq:pltHy)

We then substitute the right-hand side of the {eq}`eq:pltHy` to replace the term with the magnetic field in {eq}`eq:plzpltHy`, we find that the electric field satisfies the following diffusion equation:

$$
\partial_z\partial_z E_x - \mu\sigma\,\partial_t E_x = \mu\,\partial_t J_x^e(z,t).
$$ (eq:dee)

{eq}`eq:dee` has the same structure as the heat equation. We now have the electric field instead of temperature and the heat conductivity $\kappa$ has been replaced by $\sigma\mu$, which is the electromagnetic diffusion coefficient and it has units of s/m$^2$, and there is a source term in the right-hand side.

To construct the solution for this equation, we assume the source is active in an arbitrary space-time interval, given by $J_x^e(z,t)\ne0$ for $z_b<z<z_e$ and $t_b<t<t_e$, and use the sifting property of the delta function to express the right-hand side of {eq}`eq:dee` as

$$
\mu\,\partial_t J_x^e(z,t) = \mu\int_{z'=z_b}^{z_e}\delta(z-z')\int_{t'=0}^{t}\delta(t-t')\,\partial_{t'}J_x^e(z',t')\,\mathrm{d}t'\,\mathrm{d}z' .
$$

In the course Signals and Time Series, the delta-function was introduced in time, but we can use it in all coordinates. Because {eq}`eq:dee` relates the electric field linearly to the source, we use the principle of superposition to express the electric field as

$$
E_x(z,t) = -\mu\int_{z'=z_b}^{z_e}\int_{t'=t_b}^{t_e} G(z-z',t-t')\,\partial_{t'}J_x^e(z',t')\,\mathrm{d}z'\,\mathrm{d}t',
$$ (eq:EGJ)

where $G$ is known as the Green's function and the minus-sign was chosen for convenience. Substituting these two expressions in {eq}`eq:dee`, removing the integrals over $z'$ and $t'$ and removing the same terms in the left-hand and right-hand sides, results in

$$
(\partial_z\partial_z - \mu\sigma\,\partial_t)\,G = -\delta(z-z')\,\delta(t-t').
$$ (eq:deeg)

We now recognise $G$ as the impulse response. Hence, the Green's function is the impulse response of the Earth if we would generate signals with an impulse in space and time. Once $G$ has been found, the electric field can be obtained from the space-time convolution of the Green's function and the time derivative of the source as expressed in {eq}`eq:EGJ`. We find the solution for the Green's function by transforming {eq}`eq:deeg` to the frequency domain using

$$
\hat G(z-z',\omega) = \int_{t=0}^{\infty}\exp(-\mathrm{i}\omega t)\,G(z-z',t)\,\mathrm{d}t,
$$

The diacritical hat on the quantities denote the Fourier transform of the quantity. We find,

$$
(\partial_z\partial_z - \mathrm{i}\omega\sigma\mu)\,\hat G = -\delta(z-z')\exp(-\mathrm{i}\omega t').
$$ (eq:deegs)

The time-derivative transforms to an algebraic multiplication with $\mathrm{i}\omega$ and the delta-function in time transforms to a multiplication with $\exp(-\mathrm{i}\omega t')$ that keeps the information on the time-shift $t'$. {eq}`eq:deegs` is an ordinary second order differential equation. You have learned in the course Signals and Time Series, and seen in the part on potential fields, that the exponential function is an eigenfunction. If there is a source at $z=z'$ and the medium parameters are constants, the field will propagate in the direction where it started from the source. This means that the field propagates in the negative $z$-direction when $z-z'<0$ and propagates in the positive $z$-direction when $z>z'$. We can assume the strength of these two fields are equal and we can propose a solution of the form,

$$
\hat G = \hat A\left\{\exp\left[-\sqrt{\mathrm{i}\omega\mu\sigma}\,(z-z')\right]u(z-z') + \exp\left[\sqrt{\mathrm{i}\omega\mu\sigma}\,(z-z')\right]u(z'-z)\right\}.
$$

where $\hat A$ is the constant that needs to be determined. The field must diffuse away from the source and decrease in amplitude with increasing distances in both the positive and negative $z$-directions, as depicted in {numref}`fig-greens1d`. This is in contrast with finite domains where we have to impose end point conditions and signals travelling in both directions can occur everywhere on the line segment. Here the fields travel only in one direction and we use physics to tell us that the field should go to zero when we move infinitely far away from the source. Evaluating the first and second derivatives with respect to $z$ gives

```{figure} figures/Greens1D.png
:name: fig-greens1d
:width: 70%

The generated of signals by a point source on the line at $z=z'$ with a signal that propagates in the positive and in the negative $z$-directions away from the location $z=z'$.
```

$$
\begin{aligned}
\partial_z\hat G &= -\sqrt{\mathrm{i}\omega\sigma\mu}\,\hat A\left\{\exp\left[-\sqrt{\mathrm{i}\omega\mu\sigma}\,(z-z')\right]u(z-z') - \exp\left[\sqrt{\mathrm{i}\omega\mu\sigma}\,(z-z')\right]u(z'-z)\right\}, \\
\partial_z\partial_z\hat G &= \mathrm{i}\omega\mu\sigma\hat A\exp\left(-\sqrt{\mathrm{i}\omega\sigma\mu}\,|z-z'|\right) - 2\sqrt{\mathrm{i}\omega\sigma\mu}\,\hat A\,\delta(z-z')\exp\left(-\sqrt{\mathrm{i}\omega\sigma\mu}\,|z-z'|\right) \\
&= \mathrm{i}\omega\sigma\mu\hat G - 2\sqrt{\mathrm{i}\omega\sigma\mu}\,\hat A\,\delta(z-z'),
\end{aligned}
$$

where we used the fact that

$$
\partial_z u[\pm(z-z')] = \pm\delta(z-z')
$$

and the terms with those derivatives cancel in the expression of the first derivative, whereas in the second derivative they add up. We have used the fact that we can combine the two solutions as

$$
\exp\left(-\sqrt{\mathrm{i}\omega\sigma\mu}\,|z-z'|\right) = \exp\left[-\sqrt{\mathrm{i}\omega\mu\sigma}\,(z-z')\right]u(z-z') + \exp\left[\sqrt{\mathrm{i}\omega\mu\sigma}\,(z-z')\right]u(z'-z).
$$

If we substitute these results in {eq}`eq:deegs` we find that

$$
\hat A = \frac{\exp(-\mathrm{i}\omega t')}{2\sqrt{\mathrm{i}\omega\sigma\mu}},
$$

and the Green's function is then

$$
\hat G = \frac{\exp\left(-\sqrt{\mathrm{i}\omega\sigma\mu}\,|z-z'|\right)}{2\sqrt{\mathrm{i}\omega\sigma\mu}}\exp(-\mathrm{i}\omega t').
$$

The space-time Green's function is obtained by the inverse Fourier transformation, which is known but beyond the scope of the course. It is given by

$$
G(z-z',t-t') = \sqrt{\frac{1}{4\pi\sigma\mu(t-t')}}\exp\left(-\frac{\sigma\mu(z-z')^2}{4(t-t')}\right), \quad\text{for } t>t'.
$$

The source is taken as $J_x^e(z,t)=I\delta(z)u(t)$, which represents the plane electric current sheet in the $(x,y)$-plane at $z=0$ with a current $I$ directed along the $x$-axis and with a step switch-on time function $u(t)$. This means it is an impulse in the $z$-direction and of infinite extent in the $x$- and $y$-directions. The switch-on current source means $I$ is a constant for all times after $t=0$, $u(t)=0$ for $t<0$ and $u(t)=1$ for $t>0$. For this source, the integrals in {eq}`eq:EGJ` can be evaluated explicitly and the electric field is given by

$$
E_x(z,t) = -I\sqrt{\frac{\mu}{4\pi\sigma t}}\exp\left(-\frac{\sigma\mu z^2}{4t}\right), \quad\text{for } t>0 .
$$ (eq:ExtH)

You recognise the similarity with the solution to the heat equation with a Gaussian distribution for the initial temperature on an infinitely long wire. Note that here we make explicit that the expression for the electric field exists only for positive times. This is because $t=0$ is the moment the source is switched on and physics tells us that the Earth will respond to a source action only at or after the moment the source becomes active and not before. This is the notion of causality.

## Maxwell's equations in two dimensions with a source

If the source is an infinitely long wire and with a constant current in the $z$-direction, and the medium parameters are constants, all fields are independent of the $z$-coordinate and the derivative $\partial_z$ becomes zero, and $J_x^e=J_y^e=0$. With these choices, Maxwell's equations become

$$
\begin{aligned}
-\partial_y H_z + \sigma E_x &= 0, \\
\partial_x H_z + \sigma E_y &= 0, \\
-\partial_x H_y + \partial_y H_x + \sigma E_z &= -J_z^e, \\
\partial_y E_z + \mu\,\partial_t H_x &= 0, \\
-\partial_x E_z + \mu\,\partial_t H_y &= 0, \\
\partial_x E_y - \partial_y E_x + \mu\,\partial_t H_z &= 0 .
\end{aligned}
$$

The fields that connect to the source are grouped as

$$
-\partial_x H_y + \partial_y H_x + \sigma E_z = -J_z^e,
$$ (eq:TEEy)

$$
\mu\,\partial_t H_x = -\partial_y E_z,
$$ (eq:TEHx)

$$
\mu\,\partial_t H_y = \partial_x E_z.
$$ (eq:TEHz)

Because the fields do not depend on the $z$-direction, the plane of interest is the $(x,y)$-plane. We see that the electric field is perpendicular to the plane where the fields will change while the magnetic field has a direction in that plane. For this reason this is called the Transverse Electric or TE mode. We use {eq}`eq:TEHx` and {eq}`eq:TEHz` to substitute the magnetic fields in {eq}`eq:TEEy` to find the differential equation that $E_z$ satisfies,

$$
(\partial_x^2 + \partial_y^2 - \sigma\mu\,\partial_t)E_z = \mu\,\partial_t J_z^e.
$$

We recognise that the equation is very similar to the equation in one dimension. We can also see that the two magnetic field components satisfy

$$
\begin{aligned}
(\partial_x^2 + \partial_y^2 - \sigma\mu\,\partial_t)H_x &= -\partial_y J_z^e, \\
(\partial_x^2 + \partial_y^2 - \sigma\mu\,\partial_t)H_y &= \partial_x J_z^e.
\end{aligned}
$$

We are not going to derive solutions but give the electric and magnetic fields for a current $I$ that is switched on at $t=0$ and remains constant after that,

$$
\begin{aligned}
E_z(x,y,t) &= -\frac{\mu I}{4\pi t}\exp\left(-\frac{\sigma\mu\varrho^2}{4t}\right), \\
H_x(x,y,t) &= -\frac{\mu y I}{2\pi\varrho^2}\exp\left(-\frac{\sigma\mu\varrho^2}{4t}\right), \\
H_y(x,y,t) &= \frac{\mu x I}{2\pi\varrho^2}\exp\left(-\frac{\sigma\mu\varrho^2}{4t}\right).
\end{aligned}
$$

The expressions are in Cartesian coordinates, but we use $\varrho=\sqrt{x^2+y^2}$ for horizontal distance. First, we observe that the electric field will go to zero inversely proportional to time, while the magnetic field components will increase to its static value. In the section about the curl-operator, an expression was given for the static magnetic field of an infinitely long vertical electric wire in Cartesian coordinates in {eq}`eq:HJcyl`. There, we assumed the current was switched on infinitely long ago. We could then show that the static magnetic field is curl-free at any point outside the wire, while {eq}`eq:TEEy` shows that as long as the magnetic field is diffusive, its curl is not zero. In the Introduction to Potential Fields, it was given in cylindrical coordinates. Here we see that the electric and magnetic field have transient behaviour that is the result of switching the current on in the wire. The electric field vanishes while the magnetic field becomes a constant at infinite time. This means that towards infinite time, the magnetic field becomes a potential field. A final note is that the conductivity of the medium determines how fast the electric field vanishes and the magnetic field attains its final value but that the final magnetic field strength does not depend on the conductivity of the medium. The behaviour of the electric field as a function of time is shown in {numref}`fig-ezt` for three different distances to the wire. The conductivity of the medium is $\sigma=3$ S/m, which is a good value to mimic the value in seawater.

```{figure} figures/Ezt.png
:name: fig-ezt
:width: 70%

The vertical electric field strength as a function of time for three distances to the infinitely long wire.
```

The figure shows the curves at 0.36 m (black line), 15 m (red line) and 30 m (dashed blue line) distances to the wire. Very close to the wire the electric field is already fully established at 0.1 ms and only shows it is inversely proportional to time, which is shown by the black line. For increasing distances to the wire, the field is initially small, then rises exponentially and at some time after its peak value it will show behaviour that inversely proportional to time. The time to the maximum value is obtained as $t_p=\sigma\mu\varrho^2/4$. This means the electric field reaches its maximum value at $t_p=0.21$ ms at 15 m distance and at $t_p=0.84$ ms at 30 m distance. Once the field becomes inversely proportional to time, all values are the same and the field goes uniformly to zero. The magnetic field can be analysed as well. The equations show that they both have the exponential function that governs the time behaviour. We take the zeroth- and first-order terms of the Taylor series expansion of the exponential function in the expression of the magnetic field for large time and find

$$
\exp\left(-\frac{\sigma\mu\varrho^2}{4t}\right) = 1 - \frac{\sigma\mu\varrho^2}{4t} + \mathcal{O}(t^{-2}).
$$

When it would be 1, the magnetic field would have its static value. The second term shows how far away from the static value the magnetic field is. That is the behaviour to analyse. We plot these functions for two different distances. We can see that their difference from the static value will have asymptotic behaviour inversely proportional to time for large values of time, $t\gg\sigma\mu\varrho^2/4$. {numref}`fig-hxt` shows

$$
H_x(x,y,t) - H_x(x,y,t\rightarrow\infty) = \frac{\mu y I}{2\pi\varrho^2}\left[1 - \exp\left(-\frac{\sigma\mu\varrho^2}{4t}\right)\right],
$$

for a constant $y$-value of $y=0.25$ m and two radial distances of 15 m (red line) and 30 m (dashed blue line) to the wire together with its asymptotic value proportional to inverse time (black line). Hence, for constant $y$, $H_x$ depends only on $t$ for $t\gg\sigma\mu\varrho^2/4$. We conclude that the magnetic field approaches its static value in exactly the same way the electric field vanishes! This is true for the $y$-component of the magnetic field as well and hence for the total magnetic field magnitude.

```{figure} figures/Hxt.png
:name: fig-hxt
:width: 70%

The $x$-component of the magnetic field strength minus its static value as a function of time for a fixed $y$-value of $y=0.25$ m and two distances to the infinitely long wire.
```

## Maxwell's equations in three dimensions with a source

If we return to the Maxwell equations and find the scalar three-dimensional second order differential equation and replace the right-hand side with a three-dimensional delta-function, we end up with the diffusion equation for the Green's function in three dimensions. The derivation is beyond the scope of this course, but we will work with the Green's function. The Green's function satisfies,

$$
(\nabla^2 - \mathrm{i}\omega\sigma\mu)\,\hat G = -\delta(\boldsymbol r-\boldsymbol r'),
$$

and the frequency domain Green's function is given by

$$
\hat G(\boldsymbol r-\boldsymbol r',\omega) = \frac{\exp\left(-\sqrt{\mathrm{i}\omega\sigma\mu}\,|\boldsymbol r-\boldsymbol r'|\right)}{4\pi|\boldsymbol r-\boldsymbol r'|} .
$$

The space-time domain Green's function is

$$
G(\boldsymbol r-\boldsymbol r',t-t') = \frac{(\sigma\mu)^{1/2}}{[4\pi(t-t')]^{3/2}}\exp\left(-\frac{\sigma\mu|\boldsymbol r-\boldsymbol r'|^2}{4(t-t')}\right), \quad\text{for } t>t',
$$ (eq:G3D)

and it satisfies

$$
(\nabla^2 - \sigma\mu\,\partial_t)\,G = -\delta(\boldsymbol r-\boldsymbol r')\,\delta(t-t') .
$$

Again we recognise the similarity with solution for the heat equation for an infinitely long wire with an initial temperature that was a Gaussian distribution. It also resembles the 1D and 2D diffusive field solution to Maxwell's equations. The major difference is that here the late-time behaviour is proportional to $t^{-3/2}$. The electric and magnetic field have much more complicated behaviour but that is beyond the scope of the present course. In case of an electric current loop source the electric field can be written in the same way as for the infinitely long wire, but now we must integrate along the wire segments of the loop. The reason is that the electric field generated by a loop source is divergence-free.

### Brief analysis of the outcome

For a source in the location $\boldsymbol r'$, the field diffuses away in spherical direction and the amplitude only depends on radial distance. The product $\sigma\mu$ is the diffusion constant and has the unit of s/m$^2$. It is a measure of how fast the width of the Gaussian spreads in space for a given time instant.

**Early time behaviour.** The early-time behaviour is similar to what we saw in the 1D heat equation.

**Late time behaviour.** The late-time behaviour is inversely proportional to $t^{3/2}$, which is faster than what we saw in the solutions to the 1D heat and Maxwell diffusion equations.

**Time to the peak.** If we differentiate the Green's function to $t$ and equate the result to zero, we find the time to the peak to be $t-t'=t_p$, at $t_p=\sigma\mu|\boldsymbol r-\boldsymbol r'|^2/6$. The amplitude of the Green's function at the peak time is given by

$$
G(\boldsymbol r-\boldsymbol r',t-t'=t_p) = \frac{3\sqrt{6}\exp(-3/2)}{4\pi^{3/2}\sigma\mu|\boldsymbol r-\boldsymbol r'|^3},
$$

which shows that if you double the distance to the source, the peak amplitude is 8 times smaller.

## The diffusive electric field generated by an electric loop source

In the field, a loop is often used to generate a transient electromagnetic field and the Earth response is recorded at the ground surface with an electric field antenna or with a loop receiver. Loops are also carried in the air by a helicopter or a drone, in which case either the same loop, or another smaller loop is used to measure the time derivative of the magnetic induction in the Earth response. Here we look at the electric field that is generated in a conductive medium by a rectangular loop as indicated in {numref}`fig-loop`, with sides $L_x$ and $L_y$ and a unit amplitude step switch-on source time function. The current runs clockwise from the vertices labeled 1 to 4. The coordinates of these vertices are given by

$$
\begin{aligned}
\boldsymbol r_1 &= (-L_x/2,-L_y/2,0), & \boldsymbol r_2 &= (L_x/2,-L_y/2,0),\\
\boldsymbol r_3 &= (L_x/2,L_y/2,0), & \boldsymbol r_4 &= (-L_x/2,L_y/2,0).
\end{aligned}
$$

The point of observation is $\boldsymbol r$. For a loop source, the electric field is divergence-free and we can write the electric field as a convolution of the Green's function and the source vector, given by

$$
\boldsymbol E(\boldsymbol r,t) = -\mu\oint_{\boldsymbol r'\in L} G(\boldsymbol r-\boldsymbol r',t)\,\boldsymbol\tau(\boldsymbol r')\,\mathrm{d}l,
$$

which is a line integral along the four line segments of the loop. The unit vector $\boldsymbol\tau$ is equal to $\hat{\boldsymbol x}$ when we integrate from $\boldsymbol r_1$ to $\boldsymbol r_2$ and it is $-\hat{\boldsymbol x}$ when we integrate from $\boldsymbol r_3$ to $\boldsymbol r_4$. Similarly, the unit vector $\boldsymbol\tau$ is equal to $\hat{\boldsymbol y}$ when we integrate from $\boldsymbol r_2$ to $\boldsymbol r_3$ and it is $-\hat{\boldsymbol y}$ when we integrate from $\boldsymbol r_4$ to $\boldsymbol r_1$. We can therefore write the two horizontal components of the electric field as

$$
\begin{aligned}
E_x(\boldsymbol r,t) &= -\frac{\mu}{4\pi}\sqrt{\frac{\sigma\mu}{4\pi t^3}}\left\{\exp\left(-\frac{\sigma\mu[(y+L_y/2)^2+z^2]}{4t}\right) - \exp\left(-\frac{\sigma\mu[(y-L_y/2)^2+z^2]}{4t}\right)\right\} \\
&\quad\times\int_{-L_x/2}^{L_x/2}\exp\left(-\frac{\sigma\mu(x-x')^2}{4t}\right)\mathrm{d}x',
\end{aligned}
$$

$$
\begin{aligned}
E_y(\boldsymbol r,t) &= -\frac{\mu}{4\pi}\sqrt{\frac{\sigma\mu}{4\pi t^3}}\left\{\exp\left(-\frac{\sigma\mu[(x-L_x/2)^2+z^2]}{4t}\right) - \exp\left(-\frac{\sigma\mu[(x+L_x/2)^2+z^2]}{4t}\right)\right\} \\
&\quad\times\int_{-L_y/2}^{L_y/2}\exp\left(-\frac{\sigma\mu(y-y')^2}{4t}\right)\mathrm{d}y',
\end{aligned}
$$

```{figure} figures/Loopsrc.png
:name: fig-loop
:width: 80%

An electric current square loop source with a unit step switch-on current and its vertices 1, 2, 3, and 4.
```

where the exponentials with argument $y\pm L_y/2$ represent the integrals from point $\boldsymbol r_2$ to $\boldsymbol r_3$ and from $\boldsymbol r_4$ to $\boldsymbol r_1$, respectively. Because the integrals are similar but just run over a different coordinate axis, we will carry out the integral in the $x$-direction and then we write down the solution for the integral in $y$-direction by substitution. In the integral, we substitute $p=\sqrt{\sigma\mu(x-x')^2/(4t)}$ and integrate over the new variable $p$. The Jacobian of the parameter transformation is $\mathrm{d}p=\sqrt{\sigma\mu/(4t)}\,\mathrm{d}x'$.

$$
\int_{-L_x/2}^{L_x/2}\exp\left(-\frac{\sigma\mu(x-x')^2}{4t}\right)\mathrm{d}x' = \sqrt{\frac{4t}{\sigma\mu}}\int_{\sqrt{\frac{\sigma\mu}{4t}}x_m}^{\sqrt{\frac{\sigma\mu}{4t}}x_p}\exp(-p^2)\,\mathrm{d}p,
$$

where the new coordinates are introduced as $x_m=x-L_x/2$ and $x_p=x+L_x/2$. This is also a good moment to introduce the diffusion distance as

$$
D = \sqrt{\frac{4t}{\sigma\mu}}.
$$

Independent from whether $x\pm L_x/2>0$ or $x\pm L_x/2<0$, we can always write the integral as a difference of two integrals that both start at $p=0$,

$$
\int_{Dx_m}^{Dx_p}\exp(-p^2)\,\mathrm{d}p = \int_{0}^{Dx_p}\exp(-p^2)\,\mathrm{d}p - \int_{0}^{Dx_m}\exp(-p^2)\,\mathrm{d}p = \frac{\sqrt{\pi}}{2}\left[\mathrm{erf}(Dx_p) - \mathrm{erf}(Dx_m)\right],
$$

where $\mathrm{erf}$ denotes the error function and the scale factor is chosen such that $\mathrm{erf}(\infty)=1$. Substituting these results in the expressions for the electric field, we finally obtain

$$
E_x(\boldsymbol r,t) = -\frac{\mu}{8\pi t}\left\{\exp\left(-\frac{y_p^2+z^2}{D^2}\right) - \exp\left(-\frac{y_m^2+z^2}{D^2}\right)\right\}\left[\mathrm{erf}\left(\frac{x_p}{D}\right) - \mathrm{erf}\left(\frac{x_m}{D}\right)\right],
$$ (eq:Exloop)

$$
E_y(\boldsymbol r,t) = -\frac{\mu}{8\pi t}\left\{\exp\left(-\frac{x_m^2+z^2}{D^2}\right) - \exp\left(-\frac{x_p^2+z^2}{D^2}\right)\right\}\left[\mathrm{erf}\left(\frac{y_p}{D}\right) - \mathrm{erf}\left(\frac{y_m}{D}\right)\right].
$$ (eq:Eyloop)

{eq}`eq:Exloop` and {eq}`eq:Eyloop` are the expressions for the electric field anywhere in space and for all times after the source has been switched on. They show that $E_x=0$ in the $(x,z)$-plane at $y=0$ because then $y_p^2=y_m^2$ and $E_y=0$ in the $(y,z)$-plane at $x=0$ because then $x_p^2=x_m^2$. That makes sense because the contributions from the two line-segments in the $x$-direction have equal distance to all the points in the $(x,z)$ plane but have opposite currents. The equations also show that $E_y$ is the strongest in the $(x,z)$-plane at $y=0$ because then $y_p=-y_m$ and the error functions add up, and similarly $E_x$ is strongest in the $(y,z)$-plane at $x=0$ because then $x_p=-x_m$. The electric field is computed for a square loop with 100 m long segments placed in a conductive medium with $\sigma=0.3$ S/m. The result can be seen in {numref}`fig-et12xz` where $E_y$ is shown for two time instances in the $(x,z)$-plane at $y=0$, which is the cross-section right through the middle of the loop, such that the wire segments between points 4 and 1 and points 2 and 3 are perpendicular to the plane of the graph. The figure shows $E_y$ as a function of $x$ and $z$ at $t=0.03$ ms (left plot) and $t=5$ ms (right plot). It is shown only for positive depth values, but the field is symmetric in $z$ and the plot can be mirrored to add the picture of negative $z$. It can be seen that at 0.03 ms, the field is very strong and concentrated around the wires of the loop, whereas at 5 ms, the field is three orders of magnitude weaker and it almost occupies all the plane where the plot is made. Hence, we see that the maximum value of the electric field moves away from the loop wire segments and the width of the Gaussian in space widens with increasing time.

```{figure} figures/Eyt_xz.png
:name: fig-et12xz
:width: 100%

The electric field $E_y$ generated by a unit step switch-on current in the $(x,z)$-plane at $y=0$ m, for times $0.03$ ms (left plot) and $5$ ms (right plot).
```

At very early times and not too far away from the loop in the $z$-direction, the electric field shows the shape of the loop but the vector points in the opposite direction of the current vector in the loop. This can be seen in {numref}`fig-et12xy` where the magnitude of the electric field vector is shown in colour in the $(x,y)$-plane at $z=10$ m, at $t=0.03$ ms (left plot) and $t=5$ ms (right plot) and the white arrows show the direction of the electric field. At $t=0.03$ ms, the left plot shows that far away from the line segments, the electric field is fully aligned with but points in opposite direction as the current direction in the line segments, but the amplitude is very small. Curvature of the field lines going around the loop can be seen closer to the loop and is again almost fully aligned with the line segments just above them, but also here the field points in the opposite direction as the source current. At the later time of 5 ms, the right plot shows that the shape of the source loop is lost and the electric field is almost circular inside and around the loop. Notice also that the field strength has decreased by three orders of magnitude, the same factor as in the $(x,z)$-plane. Once the diffusion distance $D$ exceeds the size of the loop, the error function bracket goes as $L_y/D$ and the difference of exponentials as $2xL_x/D^2$, so away from the symmetry axes the field falls off as $t^{-5/2}$ at every position. The rate is a property of the diffusion, not of the direction we look in.

```{figure} figures/Eyt_xy.png
:name: fig-et12xy
:width: 100%

The magnitude $|\boldsymbol E|$ of the electric field generated by a unit step switch-on current in the $(x,y)$-plane at $z=10$ m, for times $0.03$ ms (left plot) and $5$ ms (right plot). The white arrows give the direction of the field.
```
