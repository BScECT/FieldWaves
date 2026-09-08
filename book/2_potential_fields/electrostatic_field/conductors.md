# Mobile Charge and Conductors

The source distributions used so far were prescribed: the charges remained where we placed them. In a conductor, some charges are mobile. If an electric field is present, those charges experience a force and move. Their motion changes the charge distribution, which in turn changes the field.

This feedback is the origin of electrostatic conductor boundary conditions.

## Electrostatic equilibrium

Imagine placing a neutral conductor in an external electric field. At first, the field acts on its mobile charges. Charges of opposite sign move in opposite directions and accumulate on different parts of the surface. The separated surface charge creates its own field, which opposes the applied field inside the conductor.

Electrostatic equilibrium is reached when the macroscopic charge distribution no longer changes. In an ordinary conductor allowed to settle, this means that there is no net current. It does not mean that every charge is motionless: microscopic thermal motion continues, but there is no systematic drift. The equilibrium charge distribution produces

$$
\boxed{\vec E_{\mathrm{inside}}=\vec 0.}
$$ (eq:field-inside-electrostatic-conductor)

Because $\vec E=-\vec\nabla V$,

$$
\vec\nabla V=\vec 0,
$$

so the potential is constant throughout each connected conductor. Constant does not mean zero: the value depends on grounding and on the chosen reference.

```{figure} figures/conductor_redistribution.svg
:name: conductor-charge-redistribution
:width: 100%

Mobile charge redistributes in response to an applied field. The induced surface charges create a field that cancels the applied field inside the conductor at electrostatic equilibrium.
```

## The field at the surface

The surface of a conductor in electrostatic equilibrium is an equipotential. Any tangential component of the electric field would exert a force along the surface and cause charge to keep moving. Therefore,

$$
\boxed{\vec E_{\parallel}=\vec 0.}
$$ (eq:conductor-tangential-field)

The external field must meet the surface normally, but its normal component need not vanish. A thin pillbox crossing the surface and Gauss's law give

$$
E_{\perp,\mathrm{outside}}
-E_{\perp,\mathrm{inside}}
=\frac{\sigma_q}{\epsilon_0},
$$ (eq:surface-charge-field-jump)

where $\sigma_q$ is surface charge density. Since the interior field is zero,

$$
\boxed{E_{\perp,\mathrm{outside}}=\frac{\sigma_q}{\epsilon_0}.}
$$ (eq:field-outside-conductor)

The sign of $\sigma_q$ determines whether the external field points away from or toward the surface.

## A conductor carrying steady current

The word **steady** does not imply **electrostatic**. Current describes the transport of charge. If mobile carriers have number density $n$, charge $q$, and average drift velocity $\vec v_{\mathrm d}$, then

$$
\vec J=nq\vec v_{\mathrm d},
$$

where $\vec J$ is the current density. For an ordinary ohmic material with finite conductivity, one writes

$$
\vec J=\sigma_{\mathrm c}\vec E,
$$ (eq:local-ohms-law)

where $\sigma_{\mathrm c}$ denotes conductivity. In such a material, a nonzero steady current requires a nonzero electric field within the material. The conductor is then not in electrostatic equilibrium, even if the current does not change with time.

An ideal **perfect conductor** is a different limiting case. Its resistance is zero, or equivalently its conductivity is taken to be infinite. A current that has already been established can then persist while

$$
\vec E=\vec 0.
$$

Thus, zero electric field does not by itself prove that charges are not moving. It tells us that they are not being driven by a local electric field. For this chapter, electrostatic equilibrium refers specifically to a time-independent charge distribution with no net current; the perfect-conductor case reminds us that $\vec E=0$ is a statement about force, not directly about motion.

```{admonition} Test the boundary conditions
:class: exercise

1. Why would a tangential surface field contradict electrostatic equilibrium?
2. Does $\vec E=0$ inside a conductor imply $V=0$ or only that $V$ is constant?
3. How can the field immediately outside a conductor be nonzero while the field immediately inside is zero?
4. Why does a real wire with finite resistance require an internal field to maintain a steady current?
5. Why can a perfect conductor carry a persistent current even though its internal electric field is zero?
```
