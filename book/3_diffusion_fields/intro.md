# Diffusive fields

In the previous chapter, you have learned about potential fields. Those are fields that mathematically satisfy a Laplace equation when we investigate potential fields without a forcing function or source, or a Poisson equation when the driving force or source is included. These functions are assumed to not vary as a function of time. Those are useful approximations for the class of fields known as potential fields. You can imagine that when we put an electric current in the ground between two electrodes connected to the earth at different locations, initially the current distribution in the earth is not yet established and will vary as a function of time. If the current that we inject is constant after initially switching it on, the current in the earth will become a constant as well under the conditions that no chemical reactions, heating up, and so on will occur. This is of course an approximation in itself, but we can manage to make those influences small enough to neglect them. Then after some initiation time, the fields become constant in time and satisfy a Laplace or Poisson equation.

Another class of fields is called diffusive fields. These are fields that slowly change over time. Examples are the electromagnetic field after a constant current is switched on or off in a conductive loop in air, which creates a time-varying electric and magnetic field. If we keep the current running in the loop, the fields will become constants again or die out when time progresses in the limit to infinity. Another example is a hot wire that is left to cool off. The heat equation is the first we are going to investigate. We are going to do that by assuming it occurs through diffusion. A human body, e.g., is described to lose heat during activity by four mechanisms: conduction, advection, evaporation, and radiation. In atmospheric physics, energy transport by radiation and evaporation play crucial roles. Here we concentrate on the conduction part and must look at the heat content inside a volume. We do that under the assumption that the specific heat is constant, which simplifies heat content to temperature, $T$, multiplied with a constant, and we leave the constant out for simplicity. Hence, we are going to find an equation for the temperature. We can understand that heat flows from warm to cool regions. From the property of the gradient we know that $\nabla T$ points from cold to warm regions, hence the conduction of heat should be proportional to minus the gradient of temperature. This gives

$$
\boldsymbol J_c = -\kappa\nabla T,
$$ (eq:fourier-law)

where the factor $\kappa$ is the heat conductivity. This is Fourier's law for a medium with constant heat capacity. We can observe from this equation that the magnitude of the heat current increases for a fixed gradient with increasing values of $\kappa$, which means that $\kappa$ is indeed a measure for conductivity. When large temperature differences occur in a medium and a good heat conductor is close to a poor heat conductor, this equation is too simple, but we will restrict ourselves to this expression. When there is advection, there is flow to carry the heat and we have

$$
\boldsymbol J_a = \boldsymbol v\,T,
$$

with $\boldsymbol J_a$ the advection current density and $\boldsymbol v$ the flow velocity. The total current is the sum of these two. Using both terms will bring this course in overlap with ECTB2150, Fluid Dynamics, for which reason we restrict ourselves here to the no-flow situation. The heat equation is then given by

$$
\partial_t T + \nabla\cdot\boldsymbol J_c = S,
$$

where $S$ is a heat source $(S>0)$ or sink $(S<0)$, and substitution of Fourier's law in this equation gives

$$
\partial_t T - \kappa\nabla^2 T = S,
$$ (eq:Heat)

where we have assumed constant heat conductivity. This is called a scalar diffusive field, or parabolic, equation, because in all source- and sink-free regions, a first-order time derivative of temperature is equal to a second-order spatial derivative of temperature. This is a general expression for a diffusion equation in three-dimensional space and time. A similar equation exists for other fields, for non-scalar fields as well, and we look at the electromagnetic field diffusion later. We first look at the heat equation in one and three dimensions.
