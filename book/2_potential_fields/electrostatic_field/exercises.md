# Exercises: Charge, Potential and Conducting Boundaries

Start with a diagram or a sign prediction. Keep source charge, test charge, potential, field, energy and work distinct. The electric-dipole explorer in the magnetic section also revisits superposition using actual electric charges: {doc}`../magnetic_field/dipole_explorer`.

## 1. One potential difference, two test charges

In a static field, $V(A)=150\,\mathrm V$ and $V(B)=50\,\mathrm V$.

1. Find $\Delta U$ and the work done by the field when $q=+2\,\mu\mathrm C$ is moved from $A$ to $B$.
2. Repeat for $q=-2\,\mu\mathrm C$.
3. Which results depend on the path? Which depend on the sign of the test charge?
4. Does changing the test charge change $V(A)$ or $V(B)$ under the test-charge approximation?

```{admonition} Check
:class: dropdown

The common potential difference is $-100\,\mathrm V$. For the positive charge, $\Delta U=-200\,\mu\mathrm J$ and $W=+200\,\mu\mathrm J$; for the negative charge the signs reverse. None of these changes depends on the path. The prescribed source potential does not change with the test charge.
```

## 2. What cancels at a midpoint, and what survives far away?

Put equal charges $+Q$ and $-Q$ at $z=d/2$ and $z=-d/2$, with $Q,d>0$ and the potential zero at infinity.

1. Find the potential at the midpoint. Sketch both field contributions there and add them.
2. Replace $-Q$ by $+Q$. Which quantity now cancels at the midpoint?
3. Return to opposite signs, but use $+2Q$ and $-Q$. What is the total charge? Predict whether the leading distant field is inverse-square or inverse-cube.
4. Explain why charge cancellation and vector cancellation are different questions.

```{admonition} Check
:class: dropdown

For opposite equal charges, $V=0$ but $\vec E=-8k_eQ\hat z/d^2$. For equal positive charges the midpoint field is zero but $V=4k_eQ/d$. The unequal opposite pair has net charge $Q$, so a leading monopole contribution survives: its far field decays as $r^{-2}$. The field is the vector sum of influences at an observation point; net charge is a property of the source distribution.
```

## 3. Ground potential does not determine the atmospheric field

In a local charge-free layer above flat conducting ground, take $V=az$ with upward $z$ and $V(0)=0$.

1. Find $\vec E$ and verify Laplace's equation.
2. Can both $a=100\,\mathrm{V/m}$ and $a=200\,\mathrm{V/m}$ satisfy the stated ground condition?
3. If a downward field of $100\,\mathrm{V/m}$ is measured, what sign of ground surface charge is required by $\sigma_q=\epsilon_0E_z(0^+)$?
4. Why does a nonzero external field not contradict zero field inside an equilibrium conductor?

```{admonition} Check
:class: dropdown

The field is $-a\hat z$ and the Laplacian is zero. Both slopes satisfy the lower boundary; further data are needed to select one. A downward field requires negative surface charge, approximately $-8.9\times10^{-10}\,\mathrm{C/m^2}$. Surface charge permits the jump in normal field. The local approximation is not a global charge-free-atmosphere model.
```

## 4. Verify a construction rather than solve a PDE

A point charge $Q$ is at $(0,0,h)$ above a grounded plane. Propose the potential of $Q$ plus an image $-Q$ at $(0,0,-h)$, working only in $z>0$ and omitting the fair-weather background.

1. Check the potential on the entire ground plane, not just the point directly below $Q$.
2. Identify the sources within the physical domain and check the far-field condition.
3. Which uniqueness statement makes these checks decisive?
4. Explain why continuing the formula into $z<0$ would not describe the field inside the conductor.
5. If a background potential $E_0z$ is added, which boundary condition remains unchanged and which far-field condition changes?

```{admonition} Check
:class: dropdown

Equal distances give cancellation everywhere on $z=0$. Only $Q$ lies in the air; the image introduces no extra physical-domain source. Both terms decay at infinity. With the specified source singularity and complete Dirichlet boundary conditions, uniqueness selects the solution. The lower-half-space formula is a mathematical continuation with a fictitious source, whereas the equilibrium conductor has zero field. Adding $E_0z$ preserves the grounded boundary but no longer gives a potential tending to zero at infinity.
```
