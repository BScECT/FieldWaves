# Steady Currents, Charge Conservation and a Bridge to Waves

The current loop and the exterior scalar potential have let us reuse much of the mathematics of gravity. Before leaving this chapter, separate two questions: **what does steady flow require of the currents, and where does that allow a magnetic scalar potential?** Charge conservation answers the first; curl and the observation domain answer the second.

## Current cannot end in permanent accumulation

Take a fixed volume $V$ with outward normal $\hat n$ on its boundary. The current flowing out must equal the rate at which charge inside decreases:

$$
\frac{d}{dt}\int_V\rho_q\,dV
=-\oint_{\partial V}\vec J\cdot\hat n\,dA.
$$ (eq:charge-conservation-integral)

Using the divergence theorem, and requiring this balance for every such volume, gives the local **continuity equation**:

$$
\boxed{\frac{\partial\rho_q}{\partial t}+\vec\nabla\cdot\vec J=0.}
$$ (eq:charge-continuity-magnetic)

This is another physical meaning for divergence: it measures local net outflow. Positive divergence means the local charge density decreases; negative divergence means it increases. No electric charge is created or destroyed {cite}`feynman_magnetostatics`.

In a steady state, $\partial\rho_q/\partial t=0$, hence $\vec\nabla\cdot\vec J=0$. Charge may flow through a region, but its net inflow and outflow balance. A wire carrying current into a dead end would instead accumulate charge and change the electric field; that situation could not remain steady. A complete isolated steady circuit needs a return path, including the path through its power supply.

```{admonition} What does “currents form loops” mean here?
:class: note

It means that a localized steady current system has no endpoints at which charge continually accumulates. It does not mean that every current streamline in a complicated three-dimensional flow must be a simple closed curve. A current can also enter and leave the particular subvolume we choose to study. The precise reusable statement is $\vec\nabla\cdot\vec J=0$ in the steady approximation.
```

## Steady does not mean curl-free everywhere

For steady currents in vacuum,

$$
\vec\nabla\times\vec B=\mu_0\vec J.
$$

Current conservation constrains the **divergence of $\vec J$**. It does not remove $\vec J$ from Ampère's law. A current loop still produces magnetic circulation around paths linking its wire. Thus steady currents alone do not make $\vec B$ the gradient of a globally defined scalar potential.

The exterior construction used in this chapter needs the additional spatial step: enclose the complete source current system in a sphere and work outside it. In that simply connected, current-free exterior, the magnetostatic contribution satisfies

$$
\vec\nabla\times\vec B=0,
\qquad \vec B=-\vec\nabla\Psi_m,
\qquad \nabla^2\Psi_m=0.
$$

This is why a complicated internal current system can be studied through an exterior potential. Actual ionospheric and magnetospheric currents require us to specify which source contribution and which region we are modelling. For a slowly varying field, treating successive snapshots as potential fields is an approximation whose time-dependent terms must be negligible on the scales of interest.

## Temporary accumulation is allowed

A charging capacitor provides a simple example. Current enters one conducting plate and charge accumulates there; opposite charge accumulates on the other plate. The dielectric gap need not carry a conduction current. The continuity equation still holds: local accumulation balances the current arriving at each plate.

We may loosely call a plate a temporary “sink of current”, but **not a sink that destroys charge**. It stores charge. Time dependence changes which terms matter, not the conservation law.

```{admonition} Read a changing charge distribution
:class: exercise

A volume receives $3\,\mathrm{mA}$ of conventional current and releases $1\,\mathrm{mA}$. Find $dQ/dt$ and the charge change after $2\,\mathrm{ms}$. Is this steady? State the sign of the volume integral of $\vec\nabla\cdot\vec J$.
```

```{admonition} Check
:class: dropdown

$dQ/dt=+2\,\mathrm{mC\,s^{-1}}$ and $\Delta Q=+4\,\mu\mathrm C$. The state is not steady. The integrated divergence is the outward current, $-2\,\mathrm{mA}$; its negative sign records net inflow.
```

## What changes on the way to waves?

In time-dependent electromagnetism, Ampère's law in vacuum contains an additional term:

$$
\vec\nabla\times\vec B
=\mu_0\vec J+\mu_0\epsilon_0\frac{\partial\vec E}{\partial t}.
$$ (eq:ampere-maxwell-preview)

The changing-electric-field term, called the **displacement current term**, allows this equation to remain consistent with charge conservation, including during capacitor charging. It does not require charges to cross the vacuum gap {cite}`feynman_maxwell_equations`.

A changing magnetic field also produces electric circulation through Faraday's law:

$$
\vec\nabla\times\vec E=-\frac{\partial\vec B}{\partial t}.
$$

Even in a region with no charges or conduction currents, these time-dependent terms can be nonzero. The fields then need not be curl-free, so a description using only scalar potentials is insufficient. Their coupled evolution permits electromagnetic waves, which we will study later. Temporary charge accumulation helps reveal the limits of the static equations; **a wave does not need local charge accumulation to propagate through vacuum**.

```{admonition} Optional: check the consistency with charge conservation
:class: dropdown

Take the divergence of the Ampère–Maxwell equation. The divergence of a curl is zero, while Gauss's law gives $\vec\nabla\cdot\vec E=\rho_q/\epsilon_0$. Hence

$$
0=\mu_0\vec\nabla\cdot\vec J
+\mu_0\frac{\partial\rho_q}{\partial t}.
$$

We recover the continuity equation. The extra term makes room for changing charge density while preserving local conservation.
```

The connection to the next part of the course is therefore a change in the field equations we must retain. The same divergence, curl and conservation ideas continue to provide the language.
