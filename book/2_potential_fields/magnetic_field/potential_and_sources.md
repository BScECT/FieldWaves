# From Dipoles to Magnetization

The dipole model captures much of Earth's main field, but magnetized rocks also contribute to what we measure. How can we describe a body containing many magnetic moments, with different strengths and directions? We can reuse the step from point masses to a density distribution: **add elementary contributions, then pass from a sum to an integral**.

## A density of magnetic moments

Magnetic minerals contain microscopic magnetic moments. These have quantum origins, including electron spin; the small current loop provides a useful dipole model without requiring us to imagine literal classical loops inside every atom. If the moments largely oppose one another, their vector sum can be small even when the individual moments are substantial.

Define the **magnetization** $\vec M$ as magnetic dipole moment per unit volume. A small volume element at source position $\vec r\,'$ contributes

$$
d\vec m=\vec M(\vec r\,')\,dV',
\qquad
[\vec M]=\frac{\mathrm{A\,m^2}}{\mathrm{m^3}}=\mathrm{A\,m^{-1}}.
$$ (eq:magnetization-density)

This is a macroscopic description: a volume element is small compared with the scale of the body but contains many microscopic moments. Unlike mass density, magnetization is a **vector density**. It records the direction as well as the amount of net moment. This connection between microscopic dipoles and magnetization is also developed in the MIT notes {cite}`mit_essentials_geophysics_ch3`.

| Building the source description | Gravity | Magnetization |
|---|---|---|
| Elementary source | Mass $dm$ | Dipole moment $d\vec m$ |
| Density | Scalar $\rho$ | Vector $\vec M$ |
| Volume contribution | $dm=\rho\,dV'$ | $d\vec m=\vec M\,dV'$ |
| Total source quantity | $\int\rho\,dV'$ | $\int\vec M\,dV'$ |

For magnetization, changing the orientation of some contributions can change the total without changing their individual magnitudes.

## Superpose dipole potentials

Let $\vec r$ be an observation point outside a magnetized body occupying volume $\mathcal V$. A dipole $\vec m_i$ at $\vec r_i$ has separation vector

$$
\vec R_i=\vec r-\vec r_i,
\qquad R_i=|\vec R_i|,
$$

and contributes the potential already introduced for a dipole, now translated to its source position:

$$
\Psi_i(\vec r)=\frac{\mu_0}{4\pi}
\frac{\vec m_i\cdot\vec R_i}{R_i^3}.
$$

Remember the units: one power of distance is in the numerator, so this is an inverse-square dipole potential. The dot product selects the component of the moment along the source-to-observer direction.

Divide the body into small cells. Approximate each cell by its net dipole moment $\vec M_i\Delta V_i$. Adding their **scalar potentials** gives

$$
\Psi_m(\vec r)\approx\frac{\mu_0}{4\pi}
\sum_i\frac{\vec M_i\cdot(\vec r-\vec r_i)}{|\vec r-\vec r_i|^3}\,\Delta V_i.
$$

Passing to the continuum description gives

$$
\boxed{
\Psi_m(\vec r)=\frac{\mu_0}{4\pi}
\int_{\mathcal V}
\frac{\vec M(\vec r\,')\cdot(\vec r-\vec r\,')}{|\vec r-\vec r\,'|^3}\,dV',
\qquad \vec r\notin\overline{\mathcal V}.
}
$$ (eq:magnetization-exterior-potential)

Read the integral as an instruction: at each source element, form its separation from the observer, project its moment along that separation, weight by distance, and add the scalar contribution. This is a complete forward description of the **external field produced by the prescribed magnetization distribution**, not an assumption that the whole body behaves as one point dipole.

Recover the field using $\vec B_{\mathrm M}=-\vec\nabla_{\vec r}\Psi_m$. The gradient acts on the observation coordinates; the source coordinates are the integration variables. Differentiation and superposition commute here, so summing the elementary vector fields gives the same result as differentiating the summed potential.

```{admonition} The domain still matters
:class: note

The formula above describes observations outside the magnetized material, in the magnetostatic vacuum approximation. There it gives a harmonic scalar potential and its magnetic field. Inside a magnetized body, $\vec B$ need not be curl-free; we cannot simply extend $\vec B=-\vec\nabla\Psi_m$ into the material. A fuller material description distinguishes $\vec B$ from $\vec H$ and includes the magnetization contribution explicitly.
```

## What survives far from the body?

If the observation distance is much greater than the size of the source region, all source-to-observer directions and distances are nearly the same. The leading term therefore contains only

$$
\vec m_{\mathrm{total}}=\int_{\mathcal V}\vec M(\vec r\,')\,dV',
\qquad
\Psi_m(\vec r)\approx\frac{\mu_0}{4\pi}
\frac{\vec m_{\mathrm{total}}\cdot\hat r}{r^2}.
$$

A distributed body thus approaches a single dipole when its net moment is nonzero. If that vector integral vanishes, the dipole term cancels and higher spatial terms become important. This is the same cancellation explored with {ref}`two opposing dipoles <sec:opposing-dipoles>`.

```{admonition} Predict before integrating
:class: exercise

Two separated blocks each have volume $V_b$. Their uniform magnetizations are initially both $M_0\hat z$. Find the total moment and describe the distant field. Now reverse the magnetization of one block. Does the field vanish everywhere, or only its leading dipole contribution? Why can observations nearby distinguish configurations with the same total moment?
```

```{admonition} Check
:class: dropdown

The aligned blocks have total moment $2M_0V_b\hat z$. Opposing blocks have zero total moment, but their source elements have different distances and directions relative to a nearby observer. Their fields do not generally cancel point by point. The full integral retains that source geometry; replacing it by the total moment discards it.
```

## Why this matters for rocks

A rock's magnetization can contain an **induced** part, responding to the present field, and a **remanent** part retained from its history. Some minerals acquire remanence as they cool, making rocks useful records of past field directions. The details depend on mineralogy and magnetic history {cite}`mit_essentials_geophysics_ch3`.

For this section, take $\vec M$ as given. Predicting how it responds to an applied field is a separate material problem. Superposition is linear in the prescribed moments, even when the material's response is more complicated.

This model is particularly useful for crustal magnetic anomalies. The dominant core field comes from the geodynamo; writing a magnetization integral for rocks does not replace that current system by a permanently magnetized core. A field model can add core, crustal and external contributions, while retaining the appropriate physical description of each source. Conversely, recovering a unique magnetization distribution from an observed external field is generally impossible without additional information, just as gravity observations do not uniquely determine density.
