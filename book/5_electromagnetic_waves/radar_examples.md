# Radar examples

An Earth Observation radar sends out a pulse and listens for an echo. With the travelling waves of {doc}`plane_waves_1d` and the complex notation of {doc}`harmonic_waves`, we can already say something useful about that echo, before asking what creates it.

## A delay becomes a distance

For a radar receiving an echo from a stationary target, the pulse travels out and back. Approximating the path by vacuum,

$$
\Delta t=\frac{2R}{c},\qquad
\boxed{R=\frac{c\Delta t}{2}.}
$$

Here $R$ is the distance along the line of sight, or **slant range**. At $R=600\ \mathrm{km}$, the round-trip time is about $4\ \mathrm{ms}$. We will deal with what creates an echo later; for now, its travel time already tells us something useful.

Ground-penetrating radar uses the same basic idea below the surface. There, turning a delay into a depth also requires knowing the propagation speed in the ground. That is one reason to study materials later.

## A round trip becomes a phase

Delaying a harmonic signal by $\Delta t$ multiplies it by $e^{-j\omega\Delta t}$. For a harmonic signal, a one-way propagation distance $R$ contributes the factor $e^{-jkR}$. For a radar echo, the round-trip propagation therefore contributes

$$
e^{-j2kR},
$$

in addition to the target's own scattering response. Where the pulse picture turned a journey into a delay, the harmonic picture turns it into a phase.
