# Lab 2: Electromagnetic waves

:::{admonition} Pen-and-paper exercises
:class: note

Use $c=3.00\times10^8\ \mathrm{m/s}$ and $\eta_0=\sqrt{\mu_0/\epsilon_0}\simeq377\ \Omega$ throughout.
:::

### 1. Ground-penetrating radar in dry sand

A ground-penetrating radar (GPR) antenna sends a 500 MHz wave straight down, along $+z$, into dry sand. The sand is lossless and non-magnetic, with $\epsilon_r=4$. Just below the surface, the electric field phasor is

$$
\mathbf{E}(z)=60\,\hat{x}\,e^{-ikz}\ \mathrm{V/m}.
$$

(a) Find the phase velocity $c_p$, the wavelength $\lambda$, the wavenumber $k$ and the impedance $\eta$ in the sand.

(b) Find the phasor $\mathbf{H}(z)$, and write the physical field $\mathbf{H}(z,t)$.

(c) An echo from a buried pipe arrives 20 ns after the pulse is transmitted. How deep is the pipe?

(d) What round-trip phase $\Delta \phi$ does the echo pick up? How does the phase of the echo change if the pipe is 7.5 cm deeper?

(e) Find $\langle\mathbf{S}\rangle$ just below the surface.

:::{admonition} Solution
:class: dropdown

(a)

$$
\begin{aligned}
c_p&=\frac{c}{\sqrt{\epsilon_r}}=\frac{3\cdot 10^8}{2}=1.5\cdot 10^8\ \mathrm{m/s},\\
\lambda&=\frac{c_p}{f}=\frac{1.5\cdot 10^8}{500\cdot 10^6}=0.30\ \mathrm{m},\\
k&=\frac{2\pi}{\lambda}\simeq20.9\ \mathrm{rad/m},\\
\eta&=\frac{\eta_0}{\sqrt{\epsilon_r}}=\frac{377}{2}\simeq188.5\ \Omega.
\end{aligned}
$$

(b) The wave travels along $\hat{n}=\hat{z}$:

$$
\begin{aligned}
\mathbf{H}(z)&=\frac{1}{\eta}\,\hat{z}\times\mathbf{E}(z)\\
&=\frac{60}{188.5}\,e^{-ikz}\,\hat{z}\times\hat{x}\\
&\simeq0.318\,e^{-ikz}\,\hat{y}\ \mathrm{A/m}.
\end{aligned}
$$

Multiplying by $e^{i\omega t}$ and taking the real part,

$$
\mathbf{H}(z,t)\simeq0.318\cos(\omega t-kz)\,\hat{y}\ \mathrm{A/m},
$$

with $\omega=2\pi(500\cdot 10^6)\simeq3.14\cdot 10^9\ \mathrm{rad/s}$.

(c) The pulse travels down and back at $c_p$, not $c$:

$$
\begin{aligned}
R&=\frac{c_p\,\Delta t}{2}\\
&=\frac{(1.5\cdot 10^8)(20\cdot 10^{-9})}{2}\\
&=1.5\ \mathrm{m}.
\end{aligned}
$$

Using $c$ instead would give 3 m, twice the true depth.

(d)

$$
\begin{aligned}
2kR&=2\,(20.9)(1.5)\\
&\simeq62.8\ \mathrm{rad}=20\pi,
\end{aligned}
$$

which is exactly 10 cycles, because the round trip $2R=3\ \mathrm{m}$ is 10 wavelengths. If the pipe is 7.5 cm deeper, the round trip is $15\ \mathrm{cm}=\lambda/2$ longer, so the phase increases by $\pi$: the echo flips sign.

(e)

$$
\begin{aligned}
\langle\mathbf{S}\rangle&=\frac{|\mathbf{E}|^2}{2\eta}\,\hat{z}\\
&=\frac{60^2}{2\,(188.5)}\,\hat{z}\\
&\simeq9.55\ \mathrm{W/m^2}\,\hat{z}.
\end{aligned}
$$
:::

### 2. An elliptically polarized wave

The magnetic field of a 400 MHz plane wave in a lossless, non-magnetic material is given in phasor form as

$$
\mathbf{H}(x)=(2\,\hat{y}-5i\,\hat{z})\,e^{-i25x}\ \mathrm{A/m},
$$

and the accompanying electric field has a maximum amplitude of $E_0=630\ \mathrm{V/m}$.

(a) Find the phase constant $\beta$.

(b) Find the impedance $\eta$.

(c) Find the wavelength $\lambda$.

(d) Find the phase velocity $c_p$.

(e) Find the relative permittivity $\epsilon_r$.

(f) Write the full expression for $\mathbf{H}(x,t)$.

:::{admonition} Solution
:class: dropdown

(a)

$$
\begin{aligned}
\beta&=\mathrm{Im}\{ik\}\\
&=25\ \mathrm{rad/m}.
\end{aligned}
$$

(b)
The $\hat{z}$ part of the field is 90 degrees out of phase with the $\hat{y}$ part. That means the maximum amplitude that $H_0$ reaches is 5 A/m.

$$
\begin{aligned}
\eta&=\frac{E_0}{H_0}\\
&=\frac{630}{5}\\
&=126\ \Omega.
\end{aligned}
$$


(c)

$$
\begin{aligned}
\lambda &=\frac{2\pi}{\beta} \\
&=\frac{2\pi}{25} \\
&=0.251\ \mathrm{m}.
\end{aligned}
$$

(d)

$$
\begin{aligned}
c_p &=\frac{\omega}{\beta} \\
&=\frac{2\pi (400\cdot 10^6)}{25} \\
&=1.00 \cdot 10^8\ \mathrm{m/s}.
\end{aligned}
$$

(e)

$$
\begin{aligned}
c_p &=\frac{1}{\sqrt{\mu\epsilon}} \\
&=\frac{1}{\sqrt{\mu_0\epsilon_0}}\frac{1}{\sqrt{\mu_r\epsilon_r}} \\
&=c\cdot \frac{1}{\sqrt{(1)\epsilon_r}} \\
\epsilon_r &= \frac{c^2}{c_p^2} \\
&= \frac{(3\cdot 10^8)^2}{(1\cdot 10^8)^2} \\
&= 9.
\end{aligned}
$$

(f) Multiply the phasor by $e^{i\omega t}$ and take the real part, using $-i=e^{-i\pi/2}$:

$$
\begin{aligned}
\mathbf{H}(x,t)&=\mathrm{Re}\left\{(2\,\hat{y}-5i\,\hat{z})\,e^{i(\omega t-25x)}\right\}\\
&=2\cos(\omega t-25x)\,\hat{y}+5\sin(\omega t-25x)\,\hat{z}\ \mathrm{A/m},
\end{aligned}
$$

with $\omega=2\pi(400\cdot 10^6)\simeq2.51\cdot 10^9\ \mathrm{rad/s}$. The field does not depend on $y$ or $z$.

:::

### 3. A spherical wave

The electric field of a spherical wave in free space is given in spherical coordinates as

$$
\mathbf{E}(r)=E(r)\,e^{-ikr}\,\hat{\theta}\ \mathrm{V/m}.
$$

(a) Find $\mathbf{H}(r)$.

(b) Find $\langle\mathbf{S}\rangle$.

(c) What is the average outward power through a closed spherical shell of radius $r$ (centered at the origin)?

(d) What form should $E(r)$ take to make this a physically realistic field? (Hint: look at the expression you got for $P$.)

:::{admonition} Solution
:class: dropdown

(a)

$$
\begin{aligned}
\mathbf{H}(r)&=\frac{1}{\eta}\,\hat{n}\times\mathbf{E}(r)\\
&=\frac{E(r)}{\eta_0}\,e^{-ikr}\,\hat{r}\times\hat{\theta}\\
&=\frac{E(r)}{\eta_0}\,e^{-ikr}\,\hat{\phi}.
\end{aligned}
$$

(b)

$$
\begin{aligned}
\langle\mathbf{S}\rangle&=\frac{|\mathbf{E}(r)|^2}{2\eta}\,\hat{n}\\
&=\frac{|E(r)|^2}{2\eta_0}\,\hat{r}.
\end{aligned}
$$

(c)

$$
\begin{aligned}
P&=\iint_A\langle\mathbf{S}\rangle\cdot d\mathbf{A}\\
&=\int_0^{2\pi}\!\!\int_0^{\pi}\frac{|E(r)|^2}{2\eta_0}\,\hat{r}\cdot\hat{r}\,r^2\sin\theta\,d\theta\,d\phi\\
&=\frac{|E(r)|^2}{2\eta_0}\,r^2\int_0^{2\pi}\!\!\int_0^{\pi}\sin\theta\,d\theta\,d\phi\\
&=4\pi r^2\,|\langle\mathbf{S}\rangle|\\
&=\frac{2\pi r^2|E(r)|^2}{\eta_0}.
\end{aligned}
$$

(d) A realistic field has $E(r)=E_0/r$, with $E_0$ a constant. Then $P=2\pi E_0^2/\eta_0$, so the same power passes through the shell for any $r$.
:::


### 4. Radar sounding of an ice sheet

Airborne radars measure the thickness of ice sheets by sending 60 MHz waves down through the ice and timing the echo from the bedrock. Glacier ice is (approximately) lossless and non-magnetic. It responds to an electric field with a polarization density $\mathbf{P}=\epsilon_0\chi_e\mathbf{E}$, where $\chi_e=2.15$ is its electric susceptibility.

Inside the ice, the radar wave travels down, along $+z$, with magnetic field phasor

$$
\mathbf{H}(z)=H_0\,(\hat{x}-i\,\hat{y})\,e^{-ikz}\ \mathrm{A/m}.
$$

(a) Write the physical field $\mathbf{H}(z,t)$. How does the tip of $\mathbf{H}$ move in time at a fixed $z$? What is the polarization of this wave?

(b) In the ice, the Ampère–Maxwell law becomes $\nabla\times\mathbf{H}=\frac{\partial\mathbf{D}}{\partial t}$, with $\mathbf{D}=\epsilon_0\mathbf{E}+\mathbf{P}$. Find $\mathbf{E}$ in phasor form, in terms of $H_0$, $\eta_0$ and $\chi_e$, where $\epsilon_r=1+\chi_e$.

(c) What are $c_p$ and $\eta$ in terms of $c$, $\eta_0$ and $\chi_e$? What is the amplitude of $\mathbf{E}$ if $H_0=0.1$ A/m?

(d) Find the phasor $\mathbf{P}(z)$. What fraction of $\mathbf{D}$ comes from the polarization density of the ice?

(e) The bedrock echo arrives $20\ \mu\mathrm{s}$ after the echo from the ice surface. How thick is the ice? What thickness would you get if you ignored $\chi_e$?

:::{admonition} Solution
:class: dropdown

(a) Multiply by $e^{i\omega t}$ and take the real part, using $-i=e^{-i\pi/2}$:

$$
\begin{aligned}
\mathbf{H}(z,t)&=\mathrm{Re}\left\{H_0\,(\hat{x}-i\,\hat{y})\,e^{i(\omega t-kz)}\right\}\\
&=H_0\cos(\omega t-kz)\,\hat{x}+H_0\sin(\omega t-kz)\,\hat{y}\ \mathrm{A/m},
\end{aligned}
$$

with $\omega=2\pi(60\cdot 10^6)\simeq3.77\cdot 10^8\ \mathrm{rad/s}$. The two components have equal amplitudes and are $90^\circ$ out of phase. At a fixed $z$, the tip of $\mathbf{H}$ goes around in a circle of radius $H_0$, from $\hat{x}$ towards $\hat{y}$: the wave is circularly polarized.

(b) In phasor form, the Ampère–Maxwell law is $\nabla\times\mathbf{H}=i\omega\mathbf{D}$. Use it to find $\mathbf{D}$. The fields depend only on $z$, so

$$
\begin{aligned}
\nabla\times\mathbf{H} &= i\omega\mathbf{D}(z) \\
-\frac{\partial H_y}{\partial z}\,\hat{x}+\frac{\partial H_x}{\partial z}\,\hat{y} &= i\omega\mathbf{D}(z) \\
-(-ik)(-H_0i)\,e^{-ikz}\,\hat{x}+(-ik)(H_0)\,e^{-ikz}\,\hat{y} &= i\omega\mathbf{D}(z) \\
H_0k\,(\hat{x}-i\,\hat{y})\,e^{-ikz} &= i\omega\mathbf{D}(z) \\
\mathbf{D}(z) &= \frac{k}{\omega}\,H_0(-i\,\hat{x}-\hat{y})\,e^{-ikz}.
\end{aligned}
$$

Now substitute $\mathbf{D} = \epsilon_r\epsilon_0 \mathbf{E}\,$ and $c_p=\frac{\omega}{k}$:

$$
\begin{aligned}
\mathbf{E} &= \frac{k}{\omega\epsilon_r\epsilon_0}\,H_0(-i\,\hat{x}-\hat{y})\,e^{-ikz}\\
\mathbf{E} &= \frac{1}{\epsilon_r\epsilon_0 c_p}\,H_0(-i\,\hat{x}-\hat{y})\,e^{-ikz}\\
&= \frac{\sqrt{\epsilon_r\epsilon_0\mu_0}}{\epsilon_r\epsilon_0}\,H_0(-i\,\hat{x}-\hat{y})\,e^{-ikz}\\
&= \frac{\eta_0}{\sqrt{\epsilon_r}}\,H_0(-i\,\hat{x}-\hat{y})\,e^{-ikz}\\
&= \frac{\eta_0}{\sqrt{1+\chi_e}}\,H_0(-i\,\hat{x}-\hat{y})\,e^{-ikz}
\end{aligned}
$$


(c)

$$
\begin{aligned}
c_p&=\frac{\omega}{k}=\frac{1}{\sqrt{\mu_0\epsilon_0\epsilon_r}}=\frac{c}{\sqrt{1+\chi_e}}\simeq\frac{3\cdot 10^8}{\sqrt{3.15}}\simeq1.69\cdot 10^8\ \mathrm{m/s},\\
\eta&=\frac{\omega\mu_0}{k}=\sqrt{\frac{\mu_0}{\epsilon_0\epsilon_r}}=\frac{\eta_0}{\sqrt{1+\chi_e}}\simeq\frac{377}{\sqrt{3.15}}\simeq212\ \Omega.
\end{aligned}
$$

The amplitude of $\mathbf{E}$ is therefore $0.1\,\eta\simeq21.2\ \mathrm{V/m}$.

(d)

$$
\begin{aligned}
\mathbf{P}(z)&=\epsilon_0\chi_e\mathbf{E}(z)\\
&\simeq(8.854\cdot 10^{-12})(2.15)(21.2)\,(-i\,\hat{x}-\hat{y})\,e^{-ikz}\\
&\simeq4.04\cdot 10^{-10}\,(-i\,\hat{x}-\hat{y})\,e^{-ikz}\ \mathrm{C/m^2}.
\end{aligned}
$$

The polarization density supplies a fraction $\chi_e/(1+\chi_e)=2.15/3.15\simeq68\%$ of $\mathbf{D}$.

(e) The pulse travels down and back through the ice at $c_p$:

$$
\begin{aligned}
d&=\frac{c_p\,\Delta t}{2}\\
&=\frac{(1.69\cdot 10^8)(20\cdot 10^{-6})}{2}\\
&\simeq1690\ \mathrm{m}.
\end{aligned}
$$

Ignoring $\chi_e$ means using $c$, which gives $3000\ \mathrm{m}$: an overestimate by a factor $\sqrt{1+\chi_e}\simeq1.77$.
:::
