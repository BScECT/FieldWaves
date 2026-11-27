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


### 2. Soil moisture from a radar echo

A radar on a drone looks straight down at a flat field. Air fills $z<0$ (medium 1) and soil fills $z>0$ (medium 2); positive $z$ points down. Treat both media as lossless. The soil has $\epsilon_r=2.25$ before rain and $\epsilon_r=16$ after rain. The incident wave is $\vec E_i=\hat x\,Ae^{-jk_1z}$.

(a) Write $\vec E$ and $\vec H$ in each medium, with a reflected wave of amplitude $B$ and a transmitted wave of amplitude $C$. Use Faraday's law to find $\vec H$.

(b) Use continuity of the tangential electric and magnetic fields at $z=0$ to find $r=B/A$ and $t=C/A$ in terms of $\eta_1$ and $\eta_2$. Evaluate them before and after rain.

(c) After rain, find $\mathcal R=|r|^2$ and $\mathcal T=(\eta_1/\eta_2)|t|^2$, and check that $\mathcal R+\mathcal T=1$. By how many decibels does the surface echo increase after rain?


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


### 5. A metal plate: the current makes the echo

Metal plates and corner reflectors are used to calibrate radar satellites. A plane wave $\vec E_i=\hat x\,E_0e^{-jkz}$ in air ($\eta=\eta_0$) hits a flat metal plate at $z=0$, modelled as a perfect conductor. The incident field drives a surface current $\hat x\,K_0$ (A/m) in the plate. That current emits plane waves to both sides:

$$
\vec E_{\mathrm{emitted}}(z)=-\hat x\,\frac{\eta K_0}{2}\,e^{-jk|z|}.
$$

(a) At the surface of a perfect conductor, the total tangential electric field is zero. Use this to find $K_0$. The reflected wave is the emitted wave in $z<0$: find $r$. What is the total field behind the plate, in $z>0$?

(b) Find the total magnetic field just in front of the plate. Which fields cancel at the surface, and which add? Check the jump condition $\hat z\times(\vec H_2-\vec H_1)=\vec K$, where medium 1 is $z<0$ and medium 2 is $z>0$.

(c) For $E_0=1\ \mathrm{V/m}$, find $K_0$. What fraction of the incident power is reflected? The tangential electric field at the plate is zero, yet a current flows: why does the plate absorb no power?
