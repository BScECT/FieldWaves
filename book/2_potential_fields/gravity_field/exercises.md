# Exercises: Sources, Equations and Gravity Observations

Use the same sequence throughout: identify the domain and source, read the mathematics, calculate, and interpret. These are consolidation problems; the full source integrals and general PDE solution methods are not prerequisites.

## 1. Read a source–observer vector

A point mass $M$ is at $(b,0,0)$ and the observation point is the origin, with $b>0$.

1. Write the source position $\vec r\,'$, observation position $\vec r$ and separation $\vec R=\vec r-\vec r\,'$.
2. Predict the field direction before substituting into $\vec g=-GM\vec R/|\vec R|^3$.
3. Move the coordinate origin to the source. Do the physical field and separation change?
4. Explain why the third power in the denominator does not make this an inverse-cube field.

```{admonition} Check
:class: dropdown

Initially $\vec r\,'=b\hat x$, $\vec r=0$, and $\vec R=-b\hat x$. Thus $\vec g=GM\hat x/b^2$, toward the source. After translation the source is at zero and the observer at $-b\hat x$: their difference is unchanged. The numerator has magnitude $b$, leaving an inverse-square field strength.
```

## 2. Read a potential as source information

In a local region, postulate $\Phi=A(x^2+y^2+z^2)$ with $A>0$ in $\mathrm{s^{-2}}$.

1. Sketch the field direction, then compute $\vec g$.
2. Find $\nabla^2\Phi$ and infer the density using Poisson's equation.
3. Compare with $\Phi=A(x^2-z^2)$. Can a varying field exist in a mass-free region?
4. Why does passing the PDE check not establish either expression as a global model of a bounded Earth?

```{admonition} Check
:class: dropdown

The first field is $-2A(x\hat x+y\hat y+z\hat z)$, with $\nabla^2\Phi=6A$ and $\rho=3A/(2\pi G)$. The second has zero Laplacian but a nonzero, spatially varying field. The domain and all boundary data must still be specified and checked; neither quadratic decays at infinity.
```

## 3. Which boundary information selects a solution?

In a horizontally uniform, source-free layer $0<z<H$, consider $\Phi(z)=az+b$.

1. Verify Laplace's equation and recover $\vec g$.
2. Does specifying $\Phi(0)=0$ determine $a$?
3. Add $\Phi(H)=\Phi_H$. Find the unique linear candidate and its field.
4. Instead prescribe only $g_z=-g_0$ throughout this one-dimensional model. Which constant remains undetermined?

```{admonition} Check
:class: dropdown

The second derivative is zero and $\vec g=-a\hat z$. The lower value sets $b=0$, but leaves $a$ free. The upper value fixes $a=\Phi_H/H$. A specified uniform field fixes $a=g_0$ but leaves the potential reference $b$ arbitrary. Horizontal uniformity is an explicit assumption; a bounded three-dimensional region would also require consistent side data.
```

## 4. Two ways to lose information about the sources

**Spatial averaging with height.** Two source-free potential perturbations above a plane have equal boundary amplitudes and wavelengths $\lambda$ and $\lambda/2$. Each decays as $\exp(-2\pi z/\lambda_i)$.

1. At $z=\lambda/(2\pi)$, find the two remaining potential-amplitude fractions.
2. Which spatial structure is harder to recover from observations at height?

**Non-unique sources.** Two uniform spherical density anomalies have the same centre and radii $a$ and $2a$.

3. What relation between their density contrasts makes their fields identical everywhere outside both spheres?
4. Would better measurement precision at those exterior points distinguish them under this model?

```{admonition} Check
:class: dropdown

The amplitude fractions are $e^{-1}$ and $e^{-2}$; finer spatial structure attenuates faster. Equal anomalous mass requires $\Delta\rho_2=\Delta\rho_1/8$. Their exterior fields are then exactly identical in this idealized model. More precision cannot resolve that exact ambiguity without additional information. Attenuation and source non-uniqueness are related practical limitations, but are different mechanisms.
```
