# Practice: build and check an interface solution

Use the material from {doc}`05_01_normal_incidence` to {doc}`05_05_finite_object_scattering`. Keep the equations nearby: the aim is to construct and check a solution, with a physical interpretation of every sign and factor.

## One wave too few

Two lossless, nonmagnetic media meet at $z=0$. Their permittivities are $\epsilon_1=\epsilon_0$ and $\epsilon_2=9\epsilon_0$. Someone proposes

$$
\vec E_1=\hat x E_0e^{-jk_1z},\qquad
\vec E_2=\hat x E_0e^{-jk_2z},\qquad k_2=3k_1.
$$

1. Check that each field satisfies the wave equation in its own medium.
2. Obtain the magnetic fields from Faraday's law.
3. Check the tangential boundary conditions, assuming no current sheet. Which one fails?
4. Add a reflected wave, find its amplitude and correct the transmitted amplitude.
5. Calculate reflected and transmitted power fractions. Check conservation and describe the reflected electric phase.

```{admonition} Check your result
:class: dropdown

Both electric fields solve their bulk equations, and their boundary values match. Their magnetic fields do not: $\eta_2=\eta_1/3$, so the proposed transmitted $H$ is three times the incident $H$ at $z=0$. The corrected amplitudes are $r=-1/2$ and $t=1/2$. The power fractions are $\mathcal R=1/4$ and $\mathcal T=3/4$; the reflected electric field has a $\pi$ phase shift at the interface.
```

## Optional extension: a driven current sheet repairs the magnetic jump

Keep the *original proposed fields* above, but now permit an externally driven current sheet at $z=0$.

1. Find $\vec K$ from $\hat z\times(\vec H_2-\vec H_1)$.
2. Compare incident and outgoing power. Is this sheet absorbing energy or supplying it?
3. Could a passive sheet with real $G_s\geq0$ and $K_x=G_sE_x(0)$ support these fields?

```{admonition} Check the direction and the energy
:class: dropdown

$\vec K=-\hat x\,2E_0/\eta_1$. The proposed transmitted power is three times the incident power, so the external source supplies the difference. Indeed, $\tfrac12\operatorname{Re}\{E_xK_x^*\}=-|E_0|^2/\eta_1$: the electromagnetic field does negative work on the driven sheet. This is incompatible with passive positive conductance. The source condition and the material law are additional information; matching a magnetic jump alone does not establish a passive physical solution.
```

## Tilt and check

Return to the passive, no-sheet-current interface, with $\epsilon_2=4\epsilon_0$ and incident angle $30^\circ$.

1. Find the transmitted vector wavenumber in terms of $k_1$, using phase matching and the bulk equation.
2. For horizontal polarization, derive the transmitted magnetic field by taking a Cartesian curl.
3. Calculate $r_H$ and check both tangential matching conditions.
4. Use the supplied V-polarization coefficients to compare reflected power for the two polarizations. Check the normal-incidence limit separately.

```{admonition} Intermediate checks
:class: dropdown

$\sin\theta_t=1/4$ and $\vec k_t=(k_1/2)\hat x+(\sqrt{15}k_1/2)\hat z$. For transmitted amplitude $C$ along $y$,

$$
\vec H_t=\frac{C}{\omega\mu_0}
\left(-\frac{\sqrt{15}k_1}{2}\hat x+\frac{k_1}{2}\hat z\right)e^{-j\vec k_t\cdot\vec r}.
$$

The H-polarized amplitude is $r_H\approx-0.382$, so $\mathcal R_H\approx0.146$. V polarization gives $r_V\approx-0.283$ and $\mathcal R_V\approx0.080$. At normal incidence both become $r=-1/3$ for this material pair.
```
