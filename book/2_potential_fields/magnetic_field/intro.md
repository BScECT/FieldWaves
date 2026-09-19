# Earth's Magnetic Field


The study of Earth's magnetic field has a remarkably long history, largely because of its value for navigation. Magnetic compasses were being used in China by at least the twelfth century. A compass made the field useful long before its origin was understood: it gave a reproducible direction, but not yet an explanation of why that direction existed or why it changed from place to place.

In 1600, William Gilbert published *De Magnete* and argued that Earth itself behaves like a great magnet. In the language we will develop in this chapter, the largest part of the field observed at Earth's surface resembles the field of a magnetic dipole. The resemblance is not exact, and the dipole axis is not aligned with Earth's rotation axis.

It had also become clear that the field changes both across Earth's surface and over time. In 1701, Edmond Halley published a chart of magnetic **declination**: the angle between the direction indicated by a compass and geographic north. Such charts turned scattered compass observations into a picture of a field distributed over the globe. In 1838, Carl Friedrich Gauss took the decisive mathematical step. Using a spherical-harmonic description of surface measurements, he showed that almost all of the main field originates inside Earth and described its dominant, approximately dipolar structure. The dipole axis differs from the rotation axis; its present orientation will be quantified below using a dated reference model.

This result located the dominant source but did not explain how it was sustained. A permanent magnet cannot survive the high temperatures of Earth's deep interior. During the first half of the twentieth century, evidence for a liquid, electrically conducting outer core and the development of dynamo theory led to the modern picture: motion of conducting iron in the outer core continually generates and reorganizes the geomagnetic field. Numerical simulations now allow geophysicists to explore this **geodynamo**, although its detailed behaviour and temporal variations remain active research topics.

The historical path—from compass directions, to global maps, to a mathematical model, and finally to a physical source—is also the path we will follow conceptually. We will ask what a dipole model explains, what it misses, and how observations made outside Earth contain information about sources hidden within it. This account and the structure of the chapter are inspired in part by the MIT OpenCourseWare notes *Essentials of Geophysics*, Chapter 3, “The Magnetic Field of the Earth” {cite}`mit_essentials_geophysics_ch3`.

```{admonition} The route through this section
:class: important

The central question is: **how can we reuse potential-field mathematics when a magnetic field is not generally irrotational?**

1. **Start with currents.** A current-carrying wire gives magnetic circulation; Ampère's law and Stokes' theorem connect current density to curl. This is why we cannot assume a magnetic scalar potential everywhere.
2. **Find where a potential is useful.** A compact current loop leads to a dipole. Outside a sphere enclosing the currents, the magnetostatic field is curl-free and can be described by a scalar potential. Read its vector pattern and understand its decay.
3. **Test the Earth model.** Check Laplace's equation, recover the field and compare it with boundary observations. A dipole explains much, but leaves a structured residual.
4. **Reuse the ideas.** Add simple spatial patterns, use the Lorentz force to explain particle deflection, and build the potential of magnetized rock by superposition. Finish by connecting steady currents to charge conservation and previewing waves.

The worked examples and exercises develop these ideas. Folded material marked **Optional** gives further detail. In particular, **spherical-harmonic formulas and calculations are not learning requirements here**: the relevant idea is the familiar one of representing a complicated pattern as a sum of simpler ones.
```

Begin with {doc}`from_currents_to_dipoles` and use {doc}`dipole_explorer` to visualize superposition and cancellation. Then follow the same dipole potential into {doc}`dipole_model`. The residual motivates the short conceptual discussion in {doc}`beyond_the_dipole`.

The applications follow in {doc}`forces_and_protection` and {doc}`potential_and_sources`. The closing {doc}`currents_and_waves` explains what the steady approximation assumes and what will change later in the course. The {doc}`exercises` page consolidates the section; {doc}`making_of` records how the figures were produced.
