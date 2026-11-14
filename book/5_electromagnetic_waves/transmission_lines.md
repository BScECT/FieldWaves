# Transmission lines: the same mathematics

A radar pulse also needs time to travel through the cable feeding the antenna. We can understand this using the same field equations as in {doc}`plane_waves_1d`, with **voltage and current** taking the roles of our two coupled quantities.

Consider two ideal conducting plates, separated by a distance $d$ along $x$, wide along $y$, and extending along $z$. Let their width be $w\gg d$, so we can neglect fields near the side edges. Between them we use the same transverse fields $E_x(z,t)$ and $H_y(z,t)$.

```{figure} figures/plane_wave_parallel_plates.png
:name: fig:em-plane-line
:width: 85%

Cross-section of an ideal parallel-plate line, looking along $+z$. The electric field points across the gap. The magnetic field runs across the width. The conductor current $I$ is positive along $+z$ on the lower plate; the upper plate carries the return current. The geometry is schematic.
```

The voltage across the gap at a given $z$ comes from integrating $E_x$ across the separation. To obtain the current, we need the magnetic boundary condition at a conductor surface.

A **surface current density** $\vec K_s$ has units of A/m: current per unit width of the surface. For the wave field inside an ideal conductor, $\vec H=0$. Applying Ampère's law to a small loop across the surface gives

$$
\boxed{\vec K_s=\hat n\times\vec H_{\mathrm{gap}},}
$$

where $\hat n$ points **from the conductor into the gap**. Only the tangential magnetic field contributes. At the lower plate, $\hat n=\hat x$ and $\vec H=H_y\hat y$, so $\vec K_s=H_y\hat z$. Integrating across the width of the plate gives the total current:

$$
I(z,t)=\int_0^w K_{s,z}(z,t)\,dy=wH_y(z,t).
$$

On the upper plate the normal reverses, giving the return current. We therefore have

$$
V(z,t)=\int_0^d E_x(z,t)\,dx=dE_x(z,t),\qquad
I(z,t)=wH_y(z,t).
$$

The last equalities use the approximately uniform fields between the wide plates. We now multiply the coupled field equations for $E_x$ and $H_y$ from {doc}`plane_waves_1d` by $d$ and $w$:

$$
\frac{\partial V}{\partial z}
=-\frac{\mu_0d}{w}\frac{\partial I}{\partial t},
\qquad
\frac{\partial I}{\partial z}
=-\frac{\epsilon_0w}{d}\frac{\partial V}{\partial t}.
$$

The geometry gives two parameters,

$$
L'=\frac{\mu_0d}{w}\quad[\mathrm{H/m}],\qquad
C'=\frac{\epsilon_0w}{d}\quad[\mathrm{F/m}],
$$

the **inductance per unit length** and **capacitance per unit length**. Here the prime means “per unit length”, not a derivative. Our equations become the **lossless telegrapher's equations**:

$$
\boxed{
\frac{\partial V}{\partial z}=-L'\frac{\partial I}{\partial t},
\qquad
\frac{\partial I}{\partial z}=-C'\frac{\partial V}{\partial t}.
}
$$ (eq:em-plane-telegrapher)

Differentiate the first equation with respect to $z$ and substitute the second. For constant line parameters,

$$
\frac{\partial^2 V}{\partial z^2}=L'C'\frac{\partial^2 V}{\partial t^2}.
$$

Another wave equation! Its speed and forward-wave voltage–current ratio are

$$
v_{\mathrm{line}}=\frac{1}{\sqrt{L'C'}},\qquad
Z_0=\sqrt{\frac{L'}{C'}}.
$$

For these vacuum-filled plates, $v_{\mathrm{line}}=c$ and $Z_0=\eta_0d/w$. Both $Z_0$ and $\eta_0$ have units of ohms, but the line impedance also depends on geometry. Real cables contain other materials and have losses; we will return to those effects later.

```{admonition} Recognize the structure
:class: question

Compare the telegrapher's equations with the coupled equations for $E_x,H_y$, and with the earlier equations for acoustic pressure and particle velocity. Which quantities play corresponding mathematical roles? Which physical directions are different?
```

We now have three settings—acoustics, unguided electromagnetic waves and transmission lines—with a common mathematical structure. Two coupled first-order equations give a wave equation; a waveform travels with a definite speed; and an impedance relates its two quantities. Recognizing that structure lets us reuse what we already know.

## Reading and sources

Staelin's open [*Electromagnetics and Applications*](https://www.ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/mit6_013_s09_coursetextbook.pdf), §7.1, develops the transmission-line connection. A complementary treatment of one-dimensional waves and lines is Haus and Melcher's [*Electromagnetic Fields and Energy*, Chapter 14](https://ocw.mit.edu/courses/res-6-001-electromagnetic-fields-and-energy-spring-2008/pages/chapter-14/).
