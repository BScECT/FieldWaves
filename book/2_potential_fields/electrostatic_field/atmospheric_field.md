# The Electric Field Above the Ground

The atmosphere and ground provide a useful setting in which sources, fields, potentials, and boundary conditions appear together. We first consider the field present in fair weather, then examine how a nearby charged cloud changes it.

## An electric field on a clear day

Even on a clear day, away from thunderstorms, there is an electric field above the ground. A representative near-surface value over flat, open ground is about $100\ \mathrm{V/m}$, directed **downward**. Electric potential therefore increases with height: a positive test charge experiences a downward electric force, while a negative test charge experiences an upward force.

This fair-weather field is part of the **global atmospheric electrical circuit**. The conducting upper atmosphere, or ionosphere, is at a positive potential of a few hundred kilovolts relative to the ground. Thunderstorms help maintain this potential difference by separating and transporting charge. Air is a poor conductor, but its conductivity is not zero, so a small conventional current flows downward through fair-weather regions. Measurements above thunderstorms provide evidence for their contribution to this circuit {cite}`thomas2009global_circuit`.

A clear sky overhead therefore does not mean that the electrical influence of the rest of the atmosphere disappears. The local field belongs to a much larger physical system. We will describe it using a slowly varying, approximately electrostatic field; the real atmosphere is not in strict electrostatic equilibrium.

## From the observed field to potential

Take the ground to be locally flat at $z=0$, with $z$ increasing upward. Because the ground conducts much better than air, we approximate its surface as an equipotential and choose this as our reference:

$$
V(x,y,0)=0.
$$ (eq:ground-potential-boundary)

Treating the ground as an equipotential is a physical approximation. Assigning that potential the value zero is a choice of reference. In this approximation, the field immediately above the surface is normal to it.

Over a small region near the surface, write the downward field as

$$
\vec E\approx-E_0\hat z,
\qquad E_0\approx100\ \mathrm{V/m},
$$

where $E_0$ is a positive magnitude. Since $\vec E=-\vec\nabla V$, a corresponding potential is

$$
V(z)\approx E_0z.
$$ (eq:uniform-atmospheric-potential)

The equipotential surfaces are horizontal planes, crossed at right angles by the downward field. In this idealized, undisturbed field, two points separated vertically by $1\ \mathrm m$ differ in potential by about $100\ \mathrm V$. Moving a positive test charge $q$ upward through $\Delta z$ increases its potential energy by $qE_0\Delta z$; the field does work $-qE_0\Delta z$.

This is a **local approximation**. Atmospheric conductivity and charge density vary with height, so we cannot extrapolate this linear potential all the way to the ionosphere. An object placed in the field can also redistribute charge and disturb it; the potential difference between two points in undisturbed air is not automatically the voltage across an object spanning those heights.

## What does Laplace's equation tell us here?

The linear potential satisfies

$$
\nabla^2V=0.
$$

As in the uniform-gravity example, a nonzero field is entirely consistent with Laplace's equation. Our local uniform-field model neglects volume charge in the small region being described. It does not assert that the whole atmosphere is charge-free.

There is another useful lesson: the ground boundary condition does not determine $E_0$. Every potential of the form $V=az$, for any constant $a$ with units of $\mathrm{V/m}$, satisfies both Laplace's equation and $V=0$ at the ground. To select the physical field, we need further information from the surrounding atmosphere, such as a potential specified at an upper boundary. The differential equation and one boundary alone do not supply that information.

## What does the field tell us about the ground?

We can now read the conductor boundary condition in geophysical terms. The outward normal from the ground into the air points upward, while the fair-weather field points downward. Using Equation {eq}`eq:field-outside-conductor`,

$$
\sigma_q=\epsilon_0 E_{\perp,\mathrm{outside}}
\approx-\epsilon_0E_0
\approx-8.9\times10^{-10}\ \mathrm{C/m^2}.
$$ (eq:fair-weather-ground-charge)

Thus, the downward field corresponds to a small **negative surface charge density** in our locally flat conducting-ground model. A nonzero field outside and an approximately zero field inside are compatible because the surface charge accounts for the jump in normal field.

```{admonition} Read the fair-weather field
:class: exercise

1. Why does a downward electric field imply that potential increases with height?
2. What is the change in potential energy when a negative test charge is moved upward in this field?
3. Why does $V=0$ at the ground not imply that the field above it is zero?
4. Can the ground boundary condition alone distinguish between downward fields of $100\ \mathrm{V/m}$ and $200\ \mathrm{V/m}$?
5. What sign of surface charge would correspond to an upward field just above the ground?
```

## Adding a charged cloud

A charged cloud changes the potential above the ground. Its field acts on mobile charges in the conducting Earth, causing them to redistribute. The induced surface charge then contributes its own potential and field. At equilibrium the combined solution must satisfy both the field equation in the air and the boundary condition at the ground.

In any region of air containing negligible charge,

$$
\nabla^2V=0.
$$

Within a charged part of the cloud,

$$
\nabla^2V=-\frac{\rho_q}{\epsilon_0}.
$$

At the ground, $V$ is constant and $\vec E_{\parallel}=0$. Field lines therefore meet the surface at right angles. The normal external field is supported by the induced surface charge.

## A standard trick: the method of images

To isolate the cloud contribution, first leave out the fair-weather background field. As a deliberately simple model, replace a compact charged region by a point charge $Q$ at height $h$ above a grounded conducting plane. The physical domain is the air, $z>0$. We seek a potential that

- has the point charge $Q$ as its source;
- satisfies Laplace's equation everywhere in the air away from $Q$;
- satisfies the conductor boundary condition $V=0$ at $z=0$;
- approaches zero far from the charge.

Instead of solving the differential equation directly, we will use a standard electrostatic trick called the **method of images**. The idea is to place one or more fictitious charges outside the physical domain so that a superposition of familiar point-charge potentials satisfies the required boundary condition. This method works especially well for simple conductor geometries such as planes and spheres.

Place the real charge and a proposed image charge at

$$
\vec r_Q=(0,0,h),
\qquad
\vec r_{\mathrm{image}}=(0,0,-h).
$$

Give the image the opposite charge, $-Q$, and postulate the potential

$$
V(\vec r)
=\frac{1}{4\pi\epsilon_0}
\left(
\frac{Q}{|\vec r-\vec r_Q|}
-\frac{Q}{|\vec r-\vec r_{\mathrm{image}}|}
\right),
\qquad z>0.
$$ (eq:charge-above-ground-potential)

At this stage, Equation {eq}`eq:charge-above-ground-potential` is only a proposed solution. As with the postulated gravitational potentials in {doc}`../gravity_field/postulating_laplace_solutions`, we must check both the governing equation and the boundary conditions.

```{admonition} Guided verification of the image solution
:class: exercise

Work only in the physical domain $z>0$.

1. Recall that $1/|\vec r-\vec r_0|$ satisfies Laplace's equation everywhere except at $\vec r=\vec r_0$. Show that the proposed $V$ therefore satisfies

   $$
   \nabla^2V=0
   $$

   at every point in the air away from the real charge.

2. The point charge itself is represented by

   $$
   \nabla^2V
   =-\frac{Q}{\epsilon_0}
   \delta(\vec r-\vec r_Q).
   $$

   Why does the image charge introduce no additional source into the physical domain?

3. For an arbitrary point $(x,y,0)$ on the ground, compare its distance to $\vec r_Q$ with its distance to $\vec r_{\mathrm{image}}$. Use Equation {eq}`eq:charge-above-ground-potential` to verify that

   $$
   V(x,y,0)=0.
   $$

4. Explain why a constant value of $V$ along the plane implies that the tangential electric field vanishes there.

5. Check that $V\rightarrow0$ as $|\vec r|\rightarrow\infty$.

The proposed potential has now passed all the tests that define the physical boundary-value problem. By the {ref}`uniqueness principle <sec:uniqueness-potential-problems>`, another, different potential cannot satisfy the same source distribution and boundary conditions. We are done: the image construction is not merely plausible but is the solution within $z>0$. How we guessed it no longer matters.
```

```{dropdown} Check the image construction

Each point-charge term is harmonic away from its own position. The image lies at $z=-h$, outside the physical domain, so the only singular source in $z>0$ is the real charge $Q$ at $z=h$.

At a point $(x,y,0)$ on the plane,

$$
|\vec r-\vec r_Q|
=\sqrt{x^2+y^2+h^2}
=|\vec r-\vec r_{\mathrm{image}}|.
$$

The contributions from $Q$ and $-Q$ consequently cancel, giving $V=0$ everywhere on the ground. Since $V$ is constant along the surface, its tangential derivatives vanish and hence $\vec E_{\parallel}=\vec 0$. Both terms also decrease far from the charges, so $V\rightarrow0$ at infinity.
```

The image charge is not a real charge hidden underground. It is a mathematical construction whose field in the upper half-space reproduces the effect of the actual surface-charge distribution induced on the conductor.

```{figure} figures/cloud_ground_field.png
:name: cloud-ground-field
:width: 100%

Equipotential contours and electric field lines for a positive point-cloud model above grounded conducting Earth, with the fair-weather background omitted. The image charge below the surface is shown only to explain the construction. In the physical region $z>0$, field lines meet the equipotential ground normally. The plotting code is included in {doc}`making_of`.
```

### Finding the induced surface charge

The potential gives us the field everywhere in the air, so it also tells us how charge has redistributed on the conducting ground. Let

$$
s=\sqrt{x^2+y^2}
$$

be the horizontal distance from the point directly below the model cloud charge. Just above the ground, the field has no tangential component. Its normal component follows from the vertical derivative of the potential:

$$
E_z(s,0^+)
=-\left.\frac{\partial V}{\partial z}\right|_{z=0^+}
=-\frac{Qh}{2\pi\epsilon_0(s^2+h^2)^{3/2}}.
$$ (eq:cloud-ground-normal-field)

The outward normal from the conductor into the air is $\hat z$. Because the field inside the conductor is zero, the surface boundary condition gives

$$
\boxed{
\sigma_q(s)
=\epsilon_0 E_z(s,0^+)
=-\frac{Qh}{2\pi(s^2+h^2)^{3/2}}
}.
$$ (eq:cloud-induced-surface-charge)

For a positive cloud charge, $\sigma_q$ is negative everywhere. Its magnitude is largest directly below the charge,

$$
\sigma_q(0)=-\frac{Q}{2\pi h^2},
$$

and decreases with horizontal distance. This is the mathematical description of the physical redistribution: the positive cloud charge attracts mobile negative charge toward the nearby ground surface. If $Q$ is negative, all signs reverse.

There is also a useful global check. Integrating the surface density over the infinite plane gives

$$
Q_{\mathrm{induced}}
=\int_0^\infty \sigma_q(s)\,2\pi s\,\mathrm ds
=-Q.
$$

Thus the fictitious image charge has the same value as the **total real charge induced on the grounded plane**, even though the real charge is spread continuously over its surface. The result $Q_{\mathrm{induced}}=-Q$ relies on the plane being infinite and grounded; grounding allows charge to flow to or from the Earth.

We can restore the locally uniform fair-weather background by superposition. Calling the cloud-and-image potential above $V_{\mathrm c}$,

$$
V_{\mathrm{total}}=E_0z+V_{\mathrm c},
\qquad
\vec E_{\mathrm{total}}=-E_0\hat z-\vec\nabla V_{\mathrm c}.
$$ (eq:cloud-with-fair-weather-background)

Both potential contributions vanish at $z=0$, so their sum preserves the ground boundary condition. Depending on the cloud charge, its field can reinforce or oppose the fair-weather field. Reversing only the cloud charge no longer simply reverses the total field, because the background remains unchanged. This superposition is a local model, not a description of the whole global circuit.

The fair-weather background also contributes to the surface charge. In this local model the total surface density is

$$
\sigma_{q,\mathrm{total}}(s)
=-\epsilon_0E_0
-\frac{Qh}{2\pi(s^2+h^2)^{3/2}}.
$$

The first term is the approximately uniform fair-weather contribution; the second is the localized redistribution caused by the cloud.

```{admonition} Read the cloud--ground model
:class: exercise

1. Where does Poisson's equation apply, and where does Laplace's equation apply?
2. Why can the field just above the ground be nonzero when the field inside it is zero?
3. Why must the field lines meet the ground normally?
4. Which charge shown in the figure is a mathematical construction rather than a physical source?
5. Where is the magnitude of the cloud-induced surface charge largest, and why?
6. Predict the induced surface-charge distribution beneath a negatively charged cloud.
7. Which assumptions in this model fail during a lightning discharge?
```

## What this example teaches

We did not solve Laplace's equation by a general procedure. Instead, we combined a familiar point-source potential with superposition and selected a construction that obeys the physical boundary condition. This is the same strategy used for gravity anomalies: mathematical building blocks acquire physical meaning only after the domain and its boundaries have been specified.
