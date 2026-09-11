# From gravitational force to electric force: Coulomb's Law

Recall that Newton's Law of gravity states

$$
\vec F=\frac{-GMm}{|\vec R|^2} \hat R.
$$

The same symmetry appears in electrostatics. The force between two charges, $Q_1$ and $Q_2$, is given by **Coulomb's Law**

$$
\vec F=\frac{kQ_1 Q_2}{|\vec R|^2} \hat R.
$$

Note the sign change. Positive charges produce an outwardly oriented field. Negative charges produce an inwardly oriented field, similar to gravity. Unlike gravity, both positive and negative charges are found in nature.

The constant $k$ is called the Coulomb constant, and is equal to

$$
k_{\mathrm e}=\frac{1}{4\pi\epsilon_0}.
$$ (eq:coulomb-constant)

Here $\epsilon_0$ is the **vacuum permittivity**. It tells us the strength of electrical interaction in vacuum. Coulomb's Law is more commonly expressed in terms of this quantity:

$$
\boxed{
\vec F=\frac{Q_1 Q_2}{4\pi\epsilon_0|\vec R|^2} \hat R.
}
$$ (eq:coulombs-law)

## The electric field
The electric field is denoted by the symbol $\vec E$. Analogous to $\vec g$, the electric field produced by a charge $Q$ is

$$
\boxed{
\vec E=\frac{Q}{4\pi\epsilon_0|\vec R|^2} \hat R.
}
$$ (eq:electric-field)

Dimensional analysis tells us that $\vec E$ is measured in units of N/C; however, we generally use the more practical units of **V/m**.

::::{grid} 2
:gutter: 2
:margin: 0
:padding: 0

:::{figure} figures/e_field_positive_q.png
:width: 100%
:name: e-field-positive-q

Electric field of a positive point charge.
:::

:::{figure} figures/e_field_negative_q.png
:width: 100%
:name: e-field-negative-q

Electric field of a negative point charge.
:::
::::

The electric field of a positive point charge (left) and a negative point charge (right). Field lines radiate outward from a positive charge and inward toward a negative charge.

## Flux and Gauss's Law

The area vector $\mathrm d\vec A$ points out of a closed surface. A positive charge produces an outward field and positive flux. A negative charge produces an inward field and negative flux. This contrasts with gravity, where positive mass produces inward flux.

```{figure} figures/gravity_electric_flux_comparison.svg
:name: gravity-electric-flux-comparison
:width: 100%

The same outward-oriented surface surrounds a positive mass and a positive charge. Gravity points inward, giving negative flux, while the electric field of positive charge points outward, giving positive flux.
```

For comparison, consider a closed surface next to the charge that does not surround it. The number of field lines entering the circle is the same as the number leaving it. This means the net flux is zero.

```{figure} figures/net_zero_flux.png
:name: fig:net-zero-flux
:width: 45%

A closed surface containing no charge has zero net flux.
```
The total flux entering or leaving the closed surface is equal to the charge enclosed by that surface. This is Gauss's Law, which we have already seen for gravity. We can express this in integral form as

$$
\boxed{
\oint_{\partial \mathcal V}\vec E\cdot\mathrm d\vec A
=\frac{Q_{\mathrm{enc}}}{\epsilon_0} = \frac{1}{\epsilon_0}\int_{dV} \rho_q d\mathcal V.
}
$$ (eq:gauss-law-electric-integral)

where $\rho_q$ is a charge density (C/m$^3$). 