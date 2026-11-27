# Lab 3: Attenuation and reflection of electromagnetic waves

:::{admonition} Pen-and-paper exercises
:class: note

These exercises accompany {doc}`../04_02_lossy_dielectrics` to {doc}`../04_04_radar_penetration`, and {doc}`../05_01_normal_incidence` to {doc}`../05_04_polarization_at_interface`.
Use $c=3.00\times10^8\ \mathrm{m/s}$, $\eta_0=\sqrt{\mu_0/\epsilon_0}\simeq377\ \Omega$, $\mu_0=4\pi\times10^{-7}\ \mathrm{H/m}$ and $\epsilon_0=8.854\times10^{-12}\ \mathrm{F/m}$ throughout. Fields are phasors with peak amplitudes and the time factor $e^{j\omega t}$. All materials are non-magnetic, $\mu=\mu_0$.
:::

### 1. Ground-penetrating radar in moist soil and seawater

A ground-penetrating radar (GPR) sends a $100\ \mathrm{MHz}$ wave straight down, along $+z$, into moist soil with effective complex permittivity $\epsilon_{\mathrm{eff}}=\epsilon_0\,(8.96-1.20j)$. Just below the surface, $\vec E(z)=\hat x\,E_0e^{-jkz}$ with $E_0=10\ \mathrm{V/m}$.

(a) Check that $k=k_0(3-0.2j)$, with $k_0=\omega/c$, satisfies $k^2=\omega^2\mu_0\epsilon_{\mathrm{eff}}$. Writing $k=\beta-j\alpha$, find $\beta$, $\alpha$, the wavelength $\lambda$ and the field attenuation depth $\delta_E$.

(b) Use Faraday's law to find $\vec H(z)$ and the impedance $\eta=E_x/H_y$. By how many degrees does $H_y$ lag $E_x$?

(c) Find $\langle\vec S\rangle$ just below the surface. A pipe is buried at $d=1.5\ \mathrm{m}$. Compared with a lossless soil, by what factor does absorption reduce the power of its echo?

(d) Over a saline estuary, the same radar meets seawater with $\epsilon'\simeq80\,\epsilon_0$ and $\sigma=4\ \mathrm{S/m}$; neglect its dielectric loss. Compare $\sigma$ with $\omega\epsilon'$: is seawater a good conductor at $100\ \mathrm{MHz}$? Find its skin depth and compare it with $\delta_E$ in the soil.

:::{admonition} Solution
:class: dropdown

(a) Since $\omega^2\mu_0\epsilon_0=\omega^2/c^2=k_0^2$, the equation to check is $(k/k_0)^2=\epsilon_{\mathrm{eff}}/\epsilon_0$:

$$
\begin{aligned}
k_0&=\frac{\omega}{c}=\frac{2\pi(100\times10^6)}{3.00\times10^8}\simeq2.09\ \mathrm{rad/m},\\
\left(\frac{k}{k_0}\right)^2&=(3-0.2j)^2=9-1.2j+(0.2j)^2=8.96-1.20j=\frac{\epsilon_{\mathrm{eff}}}{\epsilon_0}.
\end{aligned}
$$

The proposed $k$ works. Reading off its real and imaginary parts,

$$
\begin{aligned}
\beta&=3k_0\simeq6.28\ \mathrm{rad/m},\qquad&\lambda&=\frac{2\pi}{\beta}=1.00\ \mathrm{m},\\
\alpha&=0.2k_0\simeq0.419\ \mathrm{Np/m},\qquad&\delta_E&=\frac{1}{\alpha}\simeq2.39\ \mathrm{m}.
\end{aligned}
$$

The field is $E_x=E_0e^{-\alpha z}e^{-j\beta z}$. With $\beta>0$ the wave travels down, and $\alpha>0$ makes it decay as it goes: the passive soil takes energy from the wave. The small imaginary part of $\epsilon_{\mathrm{eff}}$ hardly changes the wavelength, but it makes the field fade.

(b) Only $\partial E_x/\partial z$ survives in the curl:

$$
\begin{aligned}
\nabla\times\vec E&=\hat y\,\frac{\partial E_x}{\partial z}=-jk\,E_x\,\hat y=-j\omega\mu_0\vec H,\\
\vec H&=\hat y\,\frac{k}{\omega\mu_0}E_x.
\end{aligned}
$$

Since $\omega\mu_0=k_0\eta_0$,

$$
\begin{aligned}
\eta&=\frac{E_x}{H_y}=\frac{\omega\mu_0}{k}=\frac{\eta_0}{3-0.2j}=\frac{377\,(3+0.2j)}{9.04}
\simeq(125.1+8.3j)\ \Omega\simeq125.4\,e^{j3.8^\circ}\ \Omega,\\
\vec H(z)&=\hat y\,\frac{E_0}{\eta}\,e^{-jkz}\simeq\hat y\,0.080\,e^{-j3.8^\circ}\,e^{-\alpha z}e^{-j\beta z}\ \mathrm{A/m}.
\end{aligned}
$$

$H_y$ lags $E_x$ by $3.8^\circ$. In a lossless medium $\eta$ is real and the two fields are in phase; the loss makes $\eta$ complex.

(c) Keep the conjugate in the Poynting vector. With $1/\eta^*=(3+0.2j)/\eta_0$,

$$
\begin{aligned}
\langle\vec S\rangle&=\frac12\operatorname{Re}\{\vec E\times\vec H^*\}
=\hat z\,\frac{|E_0|^2}{2}\operatorname{Re}\left\{\frac{1}{\eta^*}\right\}e^{-2\alpha z}
=\hat z\,\frac{|E_0|^2}{2}\,\frac{3}{\eta_0}\,e^{-2\alpha z},\\
\langle\vec S\rangle(0)&=\hat z\,\frac{(10)^2}{2}\,\frac{3}{377}\simeq0.40\ \mathrm{W/m^2}\,\hat z.
\end{aligned}
$$

The echo travels $d$ down and $d$ back up, and the power flux decays as $e^{-2\alpha z}$ along each leg:

$$
e^{-4\alpha d}=e^{-4(0.419)(1.5)}=e^{-2.51}\simeq0.081\qquad(\simeq-11\ \mathrm{dB}).
$$

The pipe lies above $\delta_E$, yet absorption alone removes more than 90% of the echo power. The echo field is reduced by $e^{-2\alpha d}\simeq0.28$.

(d)

$$
\begin{aligned}
\omega\epsilon'&=2\pi(100\times10^6)(80)(8.854\times10^{-12})\simeq0.445\ \mathrm{S/m},\\
\frac{\sigma}{\omega\epsilon'}&=\frac{4}{0.445}\simeq9.0.
\end{aligned}
$$

The conduction current is about nine times the displacement current, so seawater is conduction-dominated at $100\ \mathrm{MHz}$ and the good-conductor approximation is reasonable:

$$
\delta_E\simeq\sqrt{\frac{2}{\omega\mu_0\sigma}}
=\sqrt{\frac{2}{(6.28\times10^8)(4\pi\times10^{-7})(4)}}
\simeq2.5\times10^{-2}\ \mathrm{m}=2.5\ \mathrm{cm}.
$$

(The full complex $k$ gives $2.7\ \mathrm{cm}$.) The skin depth in seawater is about 100 times smaller than $\delta_E$ in the soil. The mobile ions, not the large $\epsilon'$, stop the radar wave. Since $\delta_E\propto1/\sqrt f$, a much lower frequency is needed to reach into seawater: at $1\ \mathrm{MHz}$, $\delta_E\simeq25\ \mathrm{cm}$. This is the diffusion regime of {doc}`../../3_diffusion_fields/em_diffusion`.
:::

### 2. Soil moisture from a radar echo

A radar on a drone looks straight down at a flat field. Air fills $z<0$ (medium 1) and soil fills $z>0$ (medium 2); positive $z$ points down. Treat both media as lossless. The soil has $\epsilon_r=2.25$ before rain and $\epsilon_r=16$ after rain. The incident wave is $\vec E_i=\hat x\,Ae^{-jk_1z}$.

(a) Write $\vec E$ and $\vec H$ in each medium, with a reflected wave of amplitude $B$ and a transmitted wave of amplitude $C$. Use Faraday's law to find $\vec H$.

(b) Use continuity of the tangential electric and magnetic fields at $z=0$ to find $r=B/A$ and $t=C/A$ in terms of $\eta_1$ and $\eta_2$. Evaluate them before and after rain.

(c) After rain, find $\mathcal R=|r|^2$ and $\mathcal T=(\eta_1/\eta_2)|t|^2$, and check that $\mathcal R+\mathcal T=1$. By how many decibels does the surface echo increase after rain?

:::{admonition} Solution
:class: dropdown

(a) The incident and reflected waves share the air; only a downward wave exists in the soil:

$$
E_{1x}=Ae^{-jk_1z}+Be^{+jk_1z},\qquad
E_{2x}=Ce^{-jk_2z}.
$$

For $\vec E=\hat x\,E_x(z)$, Faraday's law gives $\nabla\times\vec E=\hat y\,dE_x/dz=-j\omega\mu_0\vec H$, so $H_y=\dfrac{j}{\omega\mu_0}\dfrac{dE_x}{dz}$. Using $k_m/(\omega\mu_0)=1/\eta_m$ for each term,

$$
H_{1y}=\frac{Ae^{-jk_1z}-Be^{+jk_1z}}{\eta_1},\qquad
H_{2y}=\frac{Ce^{-jk_2z}}{\eta_2}.
$$

The reflected term changes sign because its spatial derivative brings $+jk_1$ instead of $-jk_1$. Physically, the reflected wave travels along $-z$, so $\vec E_r\times\vec H_r$ must point along $-z$: $\hat x\times(-\hat y)=-\hat z$.

(b) At $z=0$, with no surface current,

$$
\begin{aligned}
A+B&=C,\\
\frac{A-B}{\eta_1}&=\frac{C}{\eta_2}.
\end{aligned}
$$

Divide by $A$: $1+r=t$ and $(1-r)/\eta_1=t/\eta_2$. Substituting $t$ gives $(1-r)\eta_2=(1+r)\eta_1$, so

$$
r=\frac{\eta_2-\eta_1}{\eta_2+\eta_1},\qquad
t=1+r=\frac{2\eta_2}{\eta_2+\eta_1}.
$$

This is the acoustic result, with $\eta$ in place of $\rho c$. For non-magnetic media, $\eta_1=\eta_0$ and $\eta_2=\eta_0/\sqrt{\epsilon_r}$, so $r=(1-\sqrt{\epsilon_r})/(1+\sqrt{\epsilon_r})$ and $t=2/(1+\sqrt{\epsilon_r})$:

| | $\sqrt{\epsilon_r}$ | $r$ | $t$ |
|---|---|---|---|
| before rain, $\epsilon_r=2.25$ | $1.5$ | $-0.20$ | $0.80$ |
| after rain, $\epsilon_r=16$ | $4$ | $-0.60$ | $0.40$ |

The negative $r$ means that at $z=0$ the reflected electric field points opposite to the incident one: a phase shift of $\pi$.

(c) After rain, $\eta_1/\eta_2=\sqrt{\epsilon_r}=4$:

$$
\mathcal R=(0.60)^2=0.36,\qquad
\mathcal T=4\,(0.40)^2=0.64,\qquad
\mathcal R+\mathcal T=1.
$$

The impedance factor in $\mathcal T$ is essential: $|t|^2$ alone does not compare powers in two different media. Before rain, $\mathcal R=(0.20)^2=0.04$, so

$$
10\log_{10}\frac{0.36}{0.04}=10\log_{10}9\simeq9.5\ \mathrm{dB}.
$$

The interface has not moved; only the soil permittivity, and with it $\eta_2$, has changed. This is why the strength of the surface echo carries information about soil moisture.
:::

### 3. Radar polarization channels

Radar satellites label each image channel with two letters. The first gives the polarization of the transmitted electric field, and the second the polarization that the antenna receives. In both cases the electric field is perpendicular to the direction of propagation, as for any plane wave; the letters say which of the two transverse directions it takes. H (horizontal): the electric field is horizontal, perpendicular to the vertical plane that contains the line of sight. Over flat ground it is parallel to the ground. V (vertical): the electric field lies in that vertical plane. The letters describe the electric field: the H of a radar channel is not the magnetic field $\vec H$.

| Mission (agency, launch) | Band, centre frequency | Channels |
|---|---|---|
| Sentinel-1C/1D (ESA–EU Copernicus, 2024/2025) | C, $5.405\ \mathrm{GHz}$ | VV+VH over land; HH+HV over sea ice |
| ALOS-4 (JAXA, 2024) | L, $1.26\ \mathrm{GHz}$ | HH, or HH+HV |
| NISAR (NASA–ISRO, 2025) | L, $1.26\ \mathrm{GHz}$ | HH+HV or VV+VH globally; HH, HV, VH and VV over selected areas |
| Biomass (ESA, 2025) | P, $435\ \mathrm{MHz}$ | HH, HV, VH and VV |

(a) Find the wavelength of each radar. Which mission has a wavelength comparable to the trunks and large branches of trees?

(b) For HH, HV, VH and VV, give the transmitted and received polarizations, and say whether each channel is co-polarized (same letters) or cross-polarized. Which channels does Sentinel-1 record over land? Which does Biomass record?

(c) A smooth, flat interface reflects an H-polarized wave as an H-polarized wave, and a V-polarized wave as a V-polarized wave. What does the HV channel record from a perfectly flat, bare field? NISAR and Biomass use cross-polarized channels to estimate forest biomass. What must the leaves and branches do to the transmitted wave to produce an HV signal?

:::{admonition} Solution
:class: dropdown

(a) $\lambda=c/f$:

| Mission | Band | $\lambda=c/f$ |
|---|---|---|
| Sentinel-1 | C | $\dfrac{3.00\times10^8}{5.405\times10^9}\simeq5.55\ \mathrm{cm}$ |
| ALOS-4 and NISAR | L | $\dfrac{3.00\times10^8}{1.26\times10^9}\simeq24\ \mathrm{cm}$ |
| Biomass | P | $\dfrac{3.00\times10^8}{435\times10^6}\simeq69\ \mathrm{cm}$ |

Biomass, with a wavelength of about $70\ \mathrm{cm}$, is comparable to trunks and large branches, while leaves and twigs are much smaller than its wavelength. Its radar is designed to sense the woody parts of the forest, where trees store most of their carbon.

(b)

| Channel | Transmitted | Received | Type |
|---|---|---|---|
| HH | H | H | co-polarized |
| HV | H | V | cross-polarized |
| VH | V | H | cross-polarized |
| VV | V | V | co-polarized |

Over land, Sentinel-1 records VV and VH: one co-polarized and one cross-polarized channel, both with V transmitted. Biomass records all four channels; it is fully polarimetric.

(c) Nothing. A flat interface reflects an H wave as a pure H wave. The returned field has no V component, so an antenna oriented along V picks up no signal ({doc}`../03_03_polarization`). The leaves and branches must **depolarize** the wave: turn part of the transmitted H field into V. They do this because they point in many directions. Like the short wire in {doc}`../05_05_finite_object_scattering`, a branch along $\hat a$ carries a current proportional to $\vec E_i\cdot\hat a$ and re-radiates a field along its own axis. A branch tilted between H and V, lit by an H wave, therefore sends back a field with a V component. The more woody material there is, the stronger the cross-polarized signal; bare surfaces depolarize only weakly.
:::

### 4. A tilted wave on dry sand

A radar wave in air hits a smooth surface of dry sand (lossless, $\epsilon_r=3$) at $\theta_i=60^\circ$ from the normal. The plane of incidence is the $xz$ plane, the interface is $z=0$, and positive $z$ points down into the sand. In air, $k_1=\omega/c$.

(a) Find the transmitted angle $\theta_t$. Write the incident, reflected and transmitted vector wavenumbers $\vec k_i$, $\vec k_r$ and $\vec k_t$ in terms of $k_1$.

(b) The Fresnel reflection coefficients for H and V polarization are

$$
r_H=\frac{\eta_2\cos\theta_i-\eta_1\cos\theta_t}{\eta_2\cos\theta_i+\eta_1\cos\theta_t},\qquad
r_V=\frac{\eta_2\cos\theta_t-\eta_1\cos\theta_i}{\eta_2\cos\theta_t+\eta_1\cos\theta_i}.
$$

Evaluate $r_H$ and $r_V$ at $60^\circ$. What is special about this angle for the sand?

(c) The incident wave is linearly polarized, with equal H and V components. What is the polarization of the reflected wave? What does an ideal linear antenna aligned with the reflected V direction receive?

:::{admonition} Solution
:class: dropdown

(a) The phase must match along the whole interface, so all three waves share the tangential wavenumber of the incident wave. The sand fixes $k_2=\sqrt{\epsilon_r}\,k_1=\sqrt3\,k_1$:

$$
\begin{aligned}
k_\parallel&=k_1\sin\theta_i=\frac{\sqrt3}{2}k_1,\\
\sin\theta_t&=\frac{k_\parallel}{k_2}=\frac{\sqrt3/2}{\sqrt3}=\frac12,\qquad\theta_t=30^\circ.
\end{aligned}
$$

The normal component in the sand is $k_{z2}=k_2\cos\theta_t=\tfrac32k_1$. Hence

$$
\begin{aligned}
\vec k_i&=k_1\left(\frac{\sqrt3}{2}\hat x+\frac12\hat z\right),\\
\vec k_r&=k_1\left(\frac{\sqrt3}{2}\hat x-\frac12\hat z\right),\\
\vec k_t&=k_1\left(\frac{\sqrt3}{2}\hat x+\frac32\hat z\right).
\end{aligned}
$$

Check: $|\vec k_i|^2=|\vec k_r|^2=k_1^2\left(\tfrac34+\tfrac14\right)=k_1^2$ and $|\vec k_t|^2=k_1^2\left(\tfrac34+\tfrac94\right)=3k_1^2=k_2^2$. The transmitted wave bends towards the normal: its wavenumber is larger, but its tangential component must stay the same.

(b) With $\eta_1=\eta_0$, $\eta_2=\eta_0/\sqrt3$, $\cos\theta_i=\tfrac12$ and $\cos\theta_t=\tfrac{\sqrt3}{2}$:

$$
\begin{aligned}
\eta_2\cos\theta_i&=\frac{\eta_0}{2\sqrt3},&\eta_1\cos\theta_t&=\frac{\sqrt3}{2}\eta_0,\\
\eta_2\cos\theta_t&=\frac{\eta_0}{2},&\eta_1\cos\theta_i&=\frac{\eta_0}{2}.
\end{aligned}
$$

Multiplying the numerator and denominator of $r_H$ by $2\sqrt3/\eta_0$,

$$
r_H=\frac{1-3}{1+3}=-\frac12,\qquad
r_V=\frac{\tfrac12-\tfrac12}{\tfrac12+\tfrac12}=0.
$$

For this sand, $60^\circ$ is the **Brewster angle**: V-polarized waves are not reflected at all, while H-polarized waves reflect $\mathcal R_H=0.25$ of their power. Check: $\tan\theta_B=\sqrt{\epsilon_r}=\sqrt3$ gives $\theta_B=60^\circ$, and $\theta_i+\theta_t=90^\circ$, so the reflected and transmitted rays are perpendicular. At normal incidence both coefficients would be $(1-\sqrt3)/(1+\sqrt3)\simeq-0.27$.

(c) Write the incident field as $\vec E_i=\frac{A}{\sqrt2}\left(\hat y+\hat e_i\right)e^{-j\vec k_i\cdot\vec r}$, with the V direction $\hat e_i=\hat x\cos\theta_i-\hat z\sin\theta_i$. The reflected V direction is $\hat e_r=\hat x\cos\theta_i+\hat z\sin\theta_i$. Each component reflects with its own coefficient:

$$
\vec E_r=\frac{A}{\sqrt2}\left(r_H\,\hat y+r_V\,\hat e_r\right)e^{-j\vec k_r\cdot\vec r}
=-\frac{A}{2\sqrt2}\,\hat y\,e^{-j\vec k_r\cdot\vec r}.
$$

The reflected wave is linearly polarized along $\hat y$: purely H. Reflection at the Brewster angle acts as a polarizer. An antenna aligned with $\hat e_r$ receives nothing, since $\vec E_r\cdot\hat e_r=0$. An antenna aligned with $\hat y$ receives the whole reflected wave, which carries $|\vec E_r|^2/|A|^2=1/8$ of the incident power density. This is why polarizing sunglasses, which pass only the V component, remove most of the glare from a wet road or a lake.
:::

### 5. A metal plate: the current makes the echo

Metal plates and corner reflectors are used to calibrate radar satellites. A plane wave $\vec E_i=\hat x\,E_0e^{-jkz}$ in air ($\eta=\eta_0$) hits a flat metal plate at $z=0$, modelled as a perfect conductor. The incident field drives a surface current $\hat x\,K_0$ (A/m) in the plate. That current emits plane waves to both sides:

$$
\vec E_{\mathrm{emitted}}(z)=-\hat x\,\frac{\eta K_0}{2}\,e^{-jk|z|}.
$$

(a) At the surface of a perfect conductor, the total tangential electric field is zero. Use this to find $K_0$. The reflected wave is the emitted wave in $z<0$: find $r$. What is the total field behind the plate, in $z>0$?

(b) Find the total magnetic field just in front of the plate. Which fields cancel at the surface, and which add? Check the jump condition $\hat z\times(\vec H_2-\vec H_1)=\vec K$, where medium 1 is $z<0$ and medium 2 is $z>0$.

(c) For $E_0=1\ \mathrm{V/m}$, find $K_0$. What fraction of the incident power is reflected? The tangential electric field at the plate is zero, yet a current flows: why does the plate absorb no power?

:::{admonition} Solution
:class: dropdown

(a) The total tangential field at the plate is the incident field plus the field emitted by the current. At $z=0$ the emitted field is $-\eta K_0/2$, so

$$
\begin{aligned}
E_0-\frac{\eta K_0}{2}&=0,\\
K_0&=\frac{2E_0}{\eta}.
\end{aligned}
$$

In $z<0$ the emitted wave travels along $-z$:

$$
\vec E_r(z)=-\hat x\,\frac{\eta K_0}{2}\,e^{+jkz}=-\hat x\,E_0\,e^{+jkz},\qquad r=-1.
$$

In $z>0$ the incident and emitted waves travel together along $+z$:

$$
\vec E_{\mathrm{total}}(z)=\hat x\left(E_0-\frac{\eta K_0}{2}\right)e^{-jkz}=0.
$$

The forward wave emitted by the current cancels the incident wave exactly: there is no field behind the plate, $t=0$. The metal shields the region behind it.

(b) Use $H_y=\dfrac{j}{\omega\mu_0}\dfrac{dE_x}{dz}$, as in Exercise 2. The incident wave gives $H_y=(E_0/\eta)e^{-jkz}$. The reflected wave, $-E_0e^{+jkz}$, travels along $-z$, so its magnetic field has the opposite sign to its electric field: $H_y=+(E_0/\eta)e^{+jkz}$. At $z=0$:

$$
\begin{aligned}
E_x(0)&=E_0-E_0=0,\\
H_y(0)&=\frac{E_0}{\eta}+\frac{E_0}{\eta}=\frac{2E_0}{\eta}.
\end{aligned}
$$

The electric fields cancel and the magnetic fields add. Behind the plate $\vec H_2=0$. With $\hat z\times\hat y=-\hat x$,

$$
\hat z\times(\vec H_2-\vec H_1)=\hat z\times\left(-\hat y\,\frac{2E_0}{\eta}\right)=\hat x\,\frac{2E_0}{\eta}=\vec K.
$$

The jump in the magnetic field gives back the same current as (a).

(c)

$$
K_0=\frac{2(1\ \mathrm{V/m})}{377\ \Omega}\simeq5.3\times10^{-3}\ \mathrm{A/m}=5.3\ \mathrm{mA/m}.
$$

$\mathcal R=|r|^2=1$: all the incident power is reflected. The power per unit area that the field delivers to the current is

$$
\tfrac12\operatorname{Re}\{E_x(0)\,K_0^*\}=0,
$$

because the tangential electric field at the plate is zero. A field does work on a current only through the electric field along it. The current is not heating the metal; it re-emits the energy as the reflected wave. A real metal has finite conductivity: a weak field enters a thin skin layer, and a small fraction of the power is absorbed there ({doc}`../04_03_conductors_and_skin_depth`).
:::

### Formative assessment

A ground-penetrating radar is towed on a small boat across a freshwater lake to map the depth of the lake bed. Its antenna, just above the water, sends a $100\ \mathrm{MHz}$ wave straight down, along $+z$. The lake water is non-magnetic, with $\epsilon'=81\,\epsilon_0$ and conductivity $\sigma=0.01\ \mathrm{S/m}$. Its dielectric loss is negligible.

(a) Compare $\sigma$ with $\omega\epsilon'$. Is the lake water a good conductor or a low-loss dielectric at this frequency?

(b) For the reflection at the water surface, treat the water as lossless, with $\eta_w=\eta_0/\sqrt{\epsilon_r}$. Find the reflection coefficient $r$ and the reflected and transmitted power fractions $\mathcal R$ and $\mathcal T$ at normal incidence.

(c) In a low-loss dielectric, $\alpha\simeq\dfrac{\sigma}{2}\sqrt{\dfrac{\mu_0}{\epsilon'}}$. Find the phase velocity $v_p$, the wavelength $\lambda$, the attenuation constant $\alpha$ and the field attenuation depth $\delta_E$ in the water.

(d) The echo from the lake bed arrives $300\ \mathrm{ns}$ after the echo from the water surface. How deep is the lake? By what factor does absorption in the water reduce the power of the lake-bed echo?

(e) Suppose the lake bed reflected all the power reaching it. Ignoring spreading, what fraction of the incident power density returns to the antenna? Use $\mathcal T$ from (b) for both crossings of the water surface. Would the survey work on a saline lake with $\sigma=4\ \mathrm{S/m}$, where the skin depth is about $2.5\ \mathrm{cm}$?

:::{admonition} Solution
:class: dropdown

(a)

$$
\begin{aligned}
\omega\epsilon'&=2\pi(100\times10^6)(81)(8.854\times10^{-12})\simeq0.45\ \mathrm{S/m},\\
\frac{\sigma}{\omega\epsilon'}&=\frac{0.01}{0.45}\simeq0.022\ll1.
\end{aligned}
$$

The displacement current is about 45 times the conduction current: at $100\ \mathrm{MHz}$ fresh lake water is a low-loss dielectric, not a good conductor.

(b)

$$
\begin{aligned}
\eta_w&=\frac{\eta_0}{\sqrt{\epsilon_r}}=\frac{377}{\sqrt{81}}\simeq41.9\ \Omega,\\
r&=\frac{\eta_w-\eta_0}{\eta_w+\eta_0}=\frac{1/9-1}{1/9+1}=-0.8,\\
\mathcal R&=|r|^2=0.64,\qquad\mathcal T=1-\mathcal R=0.36.
\end{aligned}
$$

Equivalently, $t=1+r=0.2$ and $\mathcal T=(\eta_0/\eta_w)|t|^2=9\,(0.2)^2=0.36$. Most of the power is reflected at the water surface.

(c) With $\sqrt{\mu_0/\epsilon'}=\eta_0/9$:

$$
\begin{aligned}
v_p&=\frac{c}{9}\simeq3.33\times10^7\ \mathrm{m/s},\qquad
\lambda=\frac{v_p}{f}\simeq0.333\ \mathrm{m},\\
\alpha&\simeq\frac{0.01}{2}\cdot\frac{377}{9}\simeq0.209\ \mathrm{Np/m},\qquad
\delta_E=\frac1\alpha\simeq4.8\ \mathrm{m}.
\end{aligned}
$$

(d) The $300\ \mathrm{ns}$ is the down-and-back travel time in the water:

$$
\begin{aligned}
d&=\frac{v_p\,\Delta t}{2}=\frac{(3.33\times10^7)(300\times10^{-9})}{2}=5.0\ \mathrm{m},\\
e^{-4\alpha d}&=e^{-4(0.209)(5.0)}=e^{-4.19}\simeq0.015\quad(\simeq-18\ \mathrm{dB}).
\end{aligned}
$$

Using $c$ instead of $v_p$ would give a lake $45\ \mathrm{m}$ deep.

(e) The wave crosses the surface down and back up, and is absorbed over $2d$:

$$
\mathcal T^2e^{-4\alpha d}=(0.36)^2(0.015)\simeq2.0\times10^{-3}\quad(\simeq-27\ \mathrm{dB}).
$$

A small but measurable fraction returns. In a saline lake, $\delta_E\simeq2.5\ \mathrm{cm}\ll d$: the absorption factor would be $e^{-4d/\delta_E}=e^{-800}$, and no echo would come back from the lake bed. The survey would fail because of conduction in the water, not because of the reflection at its surface.
:::
