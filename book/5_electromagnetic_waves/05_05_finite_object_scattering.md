# From a reflecting plane to a finite radar target

In {doc}`05_02_conducting_reflection`, the incident field drove a current sheet and the sheet emitted waves. We could solve the problem because the sheet was infinite and uniform: there was only one direction of spatial variation.

The same physical thread helps us understand a finite object. The current distribution becomes more complicated, but we can still ask what drives the current, what field it generates and which part reaches our receiver.

## A short wire gives the field somewhere to drive charge

Imagine a slender conducting wire, short compared with the wavelength. An electric field along the wire moves charge along it. The current oscillates, and charge accumulates at the ends. Charge conservation still applies:

$$
\nabla\cdot\vec J=-j\omega\rho.
$$

This is the harmonic form of the continuity equation that mattered in {doc}`01_history_maxwell`. Where current converges, charge changes. The wire acts as a small oscillating electric dipole, which emits an electromagnetic field.

We will use a simple dipole illustration here, without deriving its radiation solution or calculating the detailed current in a real wire. Its excitation depends on the electric field along the wire axis $\hat a$:

$$
I_0\propto\vec E_i\cdot\hat a.
$$

This projection should look familiar from the receiving-antenna calculation in {doc}`03_03_polarization`. Rotating a slender wire changes the current that the incident wave can drive. Our ideal model retains its response along the wire; a real finite-width object can also have a weaker transverse response.

## Show the field emitted by the object

A finite target emits a **scattered field**. The part travelling towards the radar is **backscatter**. This vocabulary is useful: a finite target can send a field into many directions, rather than behaving like a small piece of an infinite mirror.

Far enough from a small wire, the emitted wavefronts are curved, with field amplitude decreasing as $1/R$. The strength also depends on observation direction: dipole radiation is strongest perpendicular to the wire and vanishes along its axis. The radiated electric field is perpendicular to the local propagation direction. This connects the {doc}`spreading-wave picture <03_01_waves_3d>` to an actual current source, with direction-dependent amplitude.

```{admonition} Figure and interactive activity to develop — field, current, scattered field
:class: note

Use a short wire illuminated by a linearly polarized plane wave. Show the incident electric field, oscillating wire current and end charges, and the emitted field. Mark a radar observation direction and allow the wire to rotate.

Provide views of the scattered field alone and incident-plus-scattered field. Label the plotted electric component or intensity explicitly. Use a normalized dipole model in its radiation region, with directional amplitude rather than equally bright spherical rings. Exclude the immediate neighborhood of the wire from that far-field approximation. Hold incident illumination fixed when comparing observation distances.

Ask for predictions before rotating the wire or moving the observation point. The radiation model will be provided; deriving it is not required.
```

```{admonition} Optional — read a supplied field model
:class: dropdown

A compact radiation-region model is

$$
\vec E_s(R,\hat n)=C(\omega)
\left[\hat a-(\hat a\cdot\hat n)\hat n\right]\frac{e^{-jkR}}{R},
$$

where $\hat n$ points from the wire to the observation point and $C(\omega)$ is a complex coefficient containing the induced response and its strength. We supply this expression rather than derive it.

Take its dot product with $\hat n$: the field is transverse. Set $\hat n=\hat a$: the field vanishes. Set $\hat n\cdot\hat a=0$: the angular factor has its maximum magnitude. The factor $e^{-jkR}/R$ supplies propagation phase and spreading. Each part of the expression has a job we can interpret.
```

## Add the fields and predict the receiver signal

Linear superposition gives

$$
\boxed{\vec E_{\mathrm{total}}=\vec E_i+\vec E_s.}
$$

In the current-sheet problem the sum produced cancellation on one side in the perfect-conductor limit. For a finite object the interference depends on position. The incident and scattered fields have different wavefront geometries.

A receiving antenna responds to the scattered field projected onto its axis. The full chain is therefore: incident polarization affects the target current; that current produces a directional scattered field; the receiving antenna selects a component of that field.

```{admonition} Predict the echo
:class: question

1. A wave propagates along $+z$ with electric field along $x$. Compare our wire model oriented along $x$, $y$ and $z$. Which orientations give strong or weak excitation, and why?
2. For an excited $x$-directed wire, compare observations along $z$ and along $x$. Does strong excitation imply strong radiation in every direction?
3. Hold the illumination at the wire fixed and double the distance to an observer in a fixed radiation direction. What happens to scattered field amplitude and average intensity? Link your answer to {doc}`03_02_energy_flow`.
4. Could rotating the receiving antenna change its signal while leaving the target current unchanged?
```

## Reading and sources

For background on dipole radiation and its directional field, see [Feynman, Volume II, §21–4](https://www.feynmanlectures.caltech.edu/II_21.html#Ch21-S4) and the [MIT electromagnetism notes, §13.8](https://web.mit.edu/viz/EM/visualizations/notes/modules/emwaves.pdf). The simple wire illustration is an application of that model, rather than a full finite-conductor scattering calculation.
