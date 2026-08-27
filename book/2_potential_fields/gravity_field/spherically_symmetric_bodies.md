# Spherically Symmetric Bodies

We now return to the spherical mass distributions encountered in the discussion of Newton's *Principia*. Let a body of radius $R$ have a density

$$
\rho=\rho(r'),
$$

which may vary with distance $r'$ from the centre but not with direction. Such a body can be regarded as a collection of concentric thin spherical shells. Newton's shell theorem tells us that a shell produces no field at points inside it, while at exterior points it acts as if all its mass were concentrated at the centre.

At a distance $r$ from the centre, only the mass at radii $r'<r$ contributes to the gravity field. The enclosed mass is

$$
M_{\mathrm{enc}}(r)
=4\pi\int_0^r \rho(r')\,r'^2\,\mathrm{d}r',
\qquad 0\leq r\leq R.
$$ (eq:spherical-enclosed-mass)

Spherical symmetry requires the field to be radial, so

$$
\vec{g}(\vec{r})
=-G\frac{M_{\mathrm{enc}}(r)}{r^2}\hat{r},
\qquad 0<r\leq R.
$$ (eq:spherical-interior-gravity-general)

The minus sign indicates that the field points towards the centre.

## The exterior field

Outside the body, every shell lies inside the observation radius. Equation {eq}`eq:spherical-enclosed-mass` then contains the total mass

$$
M=4\pi\int_0^R \rho(r')\,r'^2\,\mathrm{d}r',
$$ (eq:spherical-total-mass)

and the field becomes

$$
\vec{g}(\vec{r})
=-\frac{GM}{r^2}\hat{r},
\qquad r\geq R.
$$ (eq:spherical-exterior-gravity)

Thus, the exterior field depends on the radial density distribution only through its total mass. It is exactly the field of a point mass $M$ at the centre, even close to the surface. This statement is exact for a spherically symmetric body, not an approximation based on being far away. If the spherical symmetry is broken, as in the disturbed-shell example in {doc}`../introduction/newtons_principia`, the exterior field generally contains additional information about the mass distribution.

## A sphere of uniform density

Consider a solid sphere with constant density $\rho_0$. Its total mass is

$$
M=\frac{4\pi}{3}\rho_0R^3,
$$ (eq:uniform-sphere-total-mass)

while the mass enclosed by a sphere of radius $r\leq R$ is

$$
M_{\mathrm{enc}}(r)
=\frac{4\pi}{3}\rho_0r^3
=M\frac{r^3}{R^3}.
$$ (eq:uniform-sphere-enclosed-mass)

Substituting this result into Equation {eq}`eq:spherical-interior-gravity-general` gives the field inside the sphere:

$$
\vec{g}(\vec{r})
=-\frac{GM}{R^3}r\hat{r}
=-\frac{GM}{R^3}\vec{r},
\qquad 0\leq r\leq R.
$$ (eq:uniform-sphere-interior-gravity)

The field vanishes at the centre and increases linearly in magnitude as we move outwards. At the surface its magnitude is $GM/R^2$, which agrees continuously with the exterior field. Combining the two regions,

$$
\vec{g}(\vec{r})=
\begin{cases}
-\dfrac{GM}{R^3}r\hat{r}, & 0\leq r\leq R,\\[6pt]
-\dfrac{GM}{r^2}\hat{r}, & r\geq R.
\end{cases}
$$ (eq:uniform-sphere-gravity)

We can also obtain the gravitational potential, choosing $\Phi\rightarrow0$ at infinity. Outside the sphere, the point-mass result gives

$$
\Phi(r)=-\frac{GM}{r},
\qquad r\geq R.
$$

Inside, we start from the known surface value $\Phi(R)=-GM/R$ and integrate the field radially:

$$
\begin{aligned}
\Phi(r)-\Phi(R)
&=-\int_R^r \vec{g}\cdot\mathrm{d}\vec{s}\\
&=-\int_R^r\left(-\frac{GM}{R^3}s\right)\mathrm{d}s
=\frac{GM}{2R^3}\left(r^2-R^2\right).
\end{aligned}
$$

The potential of the uniform sphere is therefore

$$
\Phi(r)=
\begin{cases}
-\dfrac{GM}{2R}\left(3-\dfrac{r^2}{R^2}\right), & 0\leq r\leq R,\\[8pt]
-\dfrac{GM}{r}, & r\geq R.
\end{cases}
$$ (eq:uniform-sphere-potential)

Both $\Phi$ and $\vec{g}=-\vec{\nabla}\Phi$ are continuous at the surface. Notice that the potential does not vanish at the centre, even though the field does: the field measures the spatial change of the potential, not its value.

## Exercise: a uniform thick shell

```{admonition} From a shell to a layered Earth
:class: exercise

Consider a uniform thick spherical shell with inner radius $R_i$, outer radius $R_o$, and density $\rho_0$. There is no mass in the cavity $0\leq r<R_i$.

1. Calculate the total mass $M$ of the shell.
2. Find $M_{\mathrm{enc}}(r)$ separately in the regions $0\leq r<R_i$, $R_i\leq r\leq R_o$, and $r>R_o$.
3. Use Equation {eq}`eq:spherical-interior-gravity-general` to find $\vec{g}(\vec{r})$ in all three regions.
4. Verify that the field is continuous at $R_i$ and $R_o$. Where does its magnitude reach a maximum?
5. Taking $\Phi\rightarrow0$ at infinity, derive the potential in all three regions. Require $\Phi$ to be continuous at both boundaries.
6. Show that the limit $R_i\rightarrow0$ recovers the uniform solid sphere.
```

```{dropdown} Hints and physical checks
The enclosed mass within the material is the volume between $R_i$ and the observation radius $r$, multiplied by $\rho_0$. Matter at radii greater than $r$ contributes no field there, but it does contribute a constant to the potential.

Your field should vanish everywhere in the cavity, vary within the material, and reduce to $-GM\hat{r}/r^2$ outside. The potential should be constant, but generally not zero, throughout the cavity.
```

The field and its radial profile can be explored in the existing {doc}`../introduction/spherical_shell_gravity` notebook. Try predicting each region before comparing your result with the figure.

## From shells to a simple Earth model

A spherically layered Earth can be constructed from a central sphere and a sequence of concentric thick shells. Let the boundaries be

$$
0=R_0<R_1<\cdots<R_N=R,
$$

with constant density $\rho_i$ in the layer $R_{i-1}<r<R_i$. The mass of a complete layer is

$$
M_i=\frac{4\pi}{3}\rho_i\left(R_i^3-R_{i-1}^3\right).
$$ (eq:spherical-layer-mass)

Within any layer, the enclosed mass consists of all the complete inner layers plus the part of the current layer lying below the observation point. If $R_{k-1}\leq r\leq R_k$, then

$$
M_{\mathrm{enc}}(r)
=\sum_{i=1}^{k-1}M_i
+\frac{4\pi}{3}\rho_k\left(r^3-R_{k-1}^3\right).
$$ (eq:layered-sphere-enclosed-mass)

Substitution into Equation {eq}`eq:spherical-interior-gravity-general` gives the field in that layer. Repeating this procedure gives a simple multi-layer Earth model. Its interior field reflects the chosen layer densities, but its exterior field still depends only on the sum $M=\sum_i M_i$. Consequently, perfectly spherical external gravity measurements can determine the total mass, but cannot distinguish one radial density profile from another.
