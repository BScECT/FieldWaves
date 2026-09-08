# From Gravitational to Electric Potential

For gravity we found

$$
\vec g=-\vec\nabla\Phi,
\qquad
\vec\nabla\cdot\vec g=-4\pi G\rho,
\qquad
\nabla^2\Phi=4\pi G\rho.
$$

The same three ideas appear in electrostatics. Electric potential $V$ is defined so that

$$
\boxed{\vec E=-\vec\nabla V.}
$$ (eq:electric-field-from-potential)

Gauss's law relates the outward electric flux to the enclosed charge,

$$
\boxed{
\oint_{\partial \mathcal V}\vec E\cdot\mathrm d\vec A
=\frac{Q_{\mathrm{enc}}}{\epsilon_0}.
}
$$ (eq:gauss-law-electric-integral)

Here $\epsilon_0$ is the **vacuum permittivity**. It sets the strength of the electrical interaction in vacuum. The more familiar Coulomb constant is

$$
k_{\mathrm e}=\frac{1}{4\pi\epsilon_0}.
$$ (eq:coulomb-constant)

The factor $4\pi$ has therefore not disappeared; it is included in the relation between $k_{\mathrm e}$ and $\epsilon_0$.

## Sources, sinks, and signs

The area vector $\mathrm d\vec A$ points out of a closed surface. A positive charge produces an outward field and positive flux. A negative charge produces an inward field and negative flux. This contrasts with gravity, where positive mass produces inward flux.

```{figure} figures/gravity_electric_flux_comparison.svg
:name: gravity-electric-flux-comparison
:width: 100%

The same outward-oriented surface surrounds a positive mass and a positive charge. Gravity points inward, giving negative flux, while the electric field of positive charge points outward, giving positive flux.
```

Using the divergence theorem already developed in {doc}`../gravity_field/poisson_laplace_equations`, Gauss's law becomes

$$
\boxed{\vec\nabla\cdot\vec E=\frac{\rho_q}{\epsilon_0},}
$$ (eq:gauss-law-electric-differential)

where $\rho_q$ is charge per unit volume. Substitution of $\vec E=-\vec\nabla V$ gives

$$
-\vec\nabla\cdot(\vec\nabla V)=\frac{\rho_q}{\epsilon_0},
$$

and hence

$$
\boxed{\nabla^2V=-\frac{\rho_q}{\epsilon_0}.}
$$ (eq:electrostatic-poisson-equation)

This minus sign is not an arbitrary electrical convention. It follows from two facts: positive charge creates positive divergence, and the field points toward decreasing potential.

## Charge-free regions

Where $\rho_q=0$, Poisson's equation reduces to Laplace's equation

$$
\boxed{\nabla^2V=0.}
$$ (eq:electrostatic-laplace-equation)

This does not require $V$ to be constant or $\vec E$ to vanish, the same way that the gravitational potential field and $\vec g$ are not constant in mass-free regions. It says only that there is no charge **in the region under consideration**. Charges outside that region may still produce a spatially varying potential within it.

```{admonition} Read before calculating
:class: exercise

1. Can $V$ vary in a region where $\rho_q=0$?
2. What is the sign of $\nabla^2V$ in a region of positive charge density?
3. Compare this with the sign of $\nabla^2\Phi$ in matter. Explain the difference using field-line directions.
```
