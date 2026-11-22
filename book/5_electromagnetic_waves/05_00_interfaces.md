# Plane waves at an interface: reflection and transmission

In {doc}`04_00_media_and_losses` we followed a wave **inside** a material. We could calculate its wavelength, phase delay and attenuation, but we took its initial amplitude as given. Now we put two materials next to each other and ask how much of the wave gets in.

This is where radar gets an echo. It is also familiar territory: {doc}`acoustic waves reflect and transmit at material boundaries <../4_mechanical_waves/reflection_transmission>`. We will reuse that calculation where it applies. The new ingredients are the electromagnetic boundary conditions, vector directions and the role of currents.

A useful physical thread is

$$
\boxed{\text{field drives a current}\;\longrightarrow\;
\text{current generates a field}.}
$$

We will work this out for a conducting sheet. Its generated field adds to the incident field, producing reflection and transmission. Then we tilt the incoming wave, recover the familiar Snell's law from phase matching, and see why polarization changes the answer. A short conducting wire will finally carry the idea from a plane reflector to a finite radar target.

Keep our usual harmonic language: the common time factor is $e^{j\omega t}$, forward propagation has $e^{-jkz}$, and the real field is recovered by taking the real part. Unless stated otherwise, the media are linear and isotropic. The first interface calculation uses real, positive $\epsilon$ and $\mu$ and no loss; the conducting-sheet example introduces a current explicitly.

```{tableofcontents}
```
