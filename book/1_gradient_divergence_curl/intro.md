# Introduction

Mathematics is the language to describe physics, and physics gives the empirical content consisting of experiments. Mathematics is grammar, the model is a simplification that is meant to understand a measurement. The model states *if $a$ then $b$*, while the experiment states *if $A$ then $B$*. If $b$ matches $B$ to our satisfaction, we adopt the model; if not, we reject it. But even when adopted, we must continue to scrutinise the model, and later an experiment will come that makes us understand that the model was adopted earlier but needs revision.

Scientific progress is made through doubt.

AI changes the direction of knowledge: not any more from rule to reality, but from reality to rule. The data are used to understand and to generate a model.

Physical objects can be described in a quantitative way only with the aid of mathematics. In classical physics, all physical objects are geometric objects. The course *Fields and Waves* combines the physics of fields and waves with the mathematical tools required to describe these phenomena. The course enables students to develop essential understanding of the physical interpretation of mathematical formulations. Examples are radar waves that are used for earth surface and subsurface observations from antennas placed on satellites, airplanes, and close to or on the ground surface; sound waves, electromagnetic diffusion fields, electric and magnetic potential fields, and the gravity field to probe the earth's interior, the surface and the atmosphere. They are used to characterise layers and objects in terms of physical and geological parameters, and to monitor dynamic processes as well. The sources for these fields can be natural or anthropic.

## Dimensions and units

Seven fundamental quantities, or dimensions, have been defined. They are *length* ($L$), *time* ($T$), *temperature* ($\mathcal{T}$), *mass* ($M$), *electric current* ($I$), *amount of substance* ($n$) and *luminous intensity* ($\mathcal{L}$). Other dimensions are then secondary and can be written in terms of several or all of these seven. Electric charge has fundamental dimensions $IT$ and the fundamental dimensions of electric field are given by $ML/(IT^3)$.

Dimensions must be given a value to work with them numerically. For this the international agreement is to use the so-called metric system, and the present-day variant has the seven fundamental units that correspond to the fundamental dimensions. This system is known as the SI system, from the French *Système Internationale d'Unités*, known as the International System of Units. In this system, the dimension length has unit *meter* (m), the dimension time has unit *second* (s), the dimension temperature has unit *kelvin* (K), the dimension mass has unit *kilogram* (kg), the dimension electric current has unit *ampere* (A), the dimension amount of substance has unit *mole* (mol), and the dimension luminous intensity has unit *candela* (cd). These units are defined as follows:

- **Meter** (m). One meter is equal to the path length travelled by light in vacuum in a time of $t = 1/299\,792\,458$ second. This defines the electromagnetic wave propagation velocity in vacuum as $c_0 = 299\,792\,458$ m/s.
- **Second** (s). One second is equal to the duration of $9\,192\,631\,770$ periods of radiation corresponding to the transition between two hyperfine levels of the ground state of cesium 133. This is now known as the atomic clock. Atomic clocks are accurate to approximately 1 microsecond per year. Before the atomic clock the second was defined as the mean solar day divided by 86400, but because the earth's rotation around the sun is slowing down it was regarded inaccurate as a standard. The two standards differ in the order of 1 second per year. Distant fast rotating pulsars are, with their 1000 revolutions per second, a possible new replacement for the atomic clocks and will then yield a standard with an accuracy in the order of nanoseconds per year.
- **Kelvin** (K). One kelvin is the temperature equal to $1/273.16$ of the triple point of water, defining the triple point of water as $273.16$ kelvin. Water boils at a temperature of $T = 100\,^{\circ}\mathrm{C} = 373.15$ K.
- **Kilogram** (kg). For a long time this was the only unit still defined by a physical prototype: a cylinder of platinum and iridium alloy stored in Sèvres, France. In this sense the kilogram was an anomaly among the unit definitions.
- **Ampere** (A). One ampere is equal to the electric current flowing in each of two infinitely long parallel wires in vacuum separated by one meter, which produces a force of 200 nanonewton per meter of length.
- **Mole** (mol). The mole is defined as the amount of substance of a system which contains as many "elemental entities" (e.g., atoms, molecules, ions, electrons) as there are atoms in $0.012$ kg of carbon-12. It is related to the number of particles, which is the Avogadro constant $N_A = 6.022\,141\,79\times 10^{23}$ mol$^{-1}$.
- **Candela** (cd). One candela is the luminous intensity equal to that of $1/600\,000$ square meter of a perfect radiator at the temperature of freezing platinum at a pressure of one standard atmosphere.

:::{note}
The definitions above are the ones you will meet in most textbooks, and they are the ones used throughout these notes. Since the SI revision of 2019, the base units are instead fixed by assigning exact values to seven defining constants: $\Delta\nu_{\mathrm{Cs}}$, $c_0$, $h$, $e$, $k_{\mathrm{B}}$, $N_A$ and $K_{\mathrm{cd}}$. The kilogram is now realised from the Planck constant $h$ rather than from the prototype cylinder, and the ampere from the elementary charge $e$ rather than from the force between two wires. The numerical values change by far less than any measurement we make in this course, so nothing in what follows depends on which convention you have in mind.
:::

The other units are called secondary, or derived, units and can all be expressed as combinations of these seven. The International System of Units also recommends the use of abbreviations of units in steps of three orders of magnitude. To take length as an example, it is recommended to use 10 mm over 1 cm. In these notes the SI system is used and the abbreviation recommendation is adhered to. The metric system and its scientific prefixes are given in {numref}`tab-si-prefixes`.

```{list-table} Numbers in the metric system and their prefixes.
:header-rows: 1
:name: tab-si-prefixes

* - Numerical value
  -
  - Prefix
  - Symbol
* - 1 000 000 000 000 000 000
  - $10^{18}$
  - exa
  - E
* - 1 000 000 000 000 000
  - $10^{15}$
  - peta
  - P
* - 1 000 000 000 000
  - $10^{12}$
  - tera
  - T
* - 1 000 000 000
  - $10^{9}$
  - giga
  - G
* - 1 000 000
  - $10^{6}$
  - mega
  - M
* - 1 000
  - $10^{3}$
  - kilo
  - k
* - 1
  - $1$
  - one
  - –
* - 0.001
  - $10^{-3}$
  - milli
  - m
* - 0.000 001
  - $10^{-6}$
  - micro
  - $\mu$
* - 0.000 000 001
  - $10^{-9}$
  - nano
  - n
* - 0.000 000 000 001
  - $10^{-12}$
  - pico
  - p
* - 0.000 000 000 000 001
  - $10^{-15}$
  - femto
  - f
* - 0.000 000 000 000 000 001
  - $10^{-18}$
  - atto
  - a
```

## What follows

The remaining pages of this introduction deal with sums, series and approximations, and with reference frames, symbols and notations for scalar, vector, and matrix quantities, together with the notion of time and temporal variations of a function. The pages after those describe the three main spatial derivative operators — gradient, divergence, and curl — and discuss their physical meaning. Later chapters describe potential, diffusive, and wave fields, respectively.
