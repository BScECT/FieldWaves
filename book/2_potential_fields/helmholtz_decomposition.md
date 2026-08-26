# Non-conservative Fields: Helmholtz Decomposition

In the previous section, we saw that a conservative vector field can be written as the gradient of a scalar field. Equations {eq}`eq:point-mass-gravitational-potential` and {eq}`eq:point-mass-gravity-field`, for example, describe the scalar potential of a point mass and the corresponding gravity vector field. Most of this chapter deals with fields of this type. We may nevertheless wonder whether physical vector fields always have this form. Anticipating that the answer is no, is there still a simple general expression for a vector field?

The answer is given by the **Helmholtz decomposition**. Under suitable smoothness and boundary conditions, a vector field can be written as

$$
  \vec{F} = -\vec{\nabla}\Phi + \vec{\nabla}\times\vec{A}.
$$ (eq:helmholtz-decomposition)

The field is decomposed into two parts:

1. A conservative, or **irrotational**, part given by the gradient of a scalar potential. It is irrotational because

   $$
     \vec{\nabla}\times(-\vec{\nabla}\Phi)=\vec{0}.
   $$

2. A divergence-free, or **solenoidal**, part given by the curl of a **vector potential**. It is solenoidal because

   $$
     \vec{\nabla}\cdot(\vec{\nabla}\times\vec{A})=0.
   $$

The two parts have visibly different characters. Consider a cross-section through a uniform-density sphere and through a long wire carrying a uniform current. Inside the sphere, gravity points toward the centre and the field lines converge, but do not circulate. Inside the wire, the magnetic field circulates around the current, but its field lines neither begin nor end.

```{figure} figures/helmholtz_field_comparison.png
:name: helmholtz-field-comparison
:width: 100%

Two simple physical fields. Left: inside a uniform-density sphere, $\vec{g}=-\kappa(x,y,z)$ is irrotational and has negative divergence. Right: inside a long wire with uniform current in the $z$-direction, $\vec{B}=\beta(-y,x,0)$ is solenoidal and circulates around the current. The arrows show a two-dimensional cross-section; their colour and length indicate field magnitude.
```

Notice that *irrotational* does not mean that the field has no source, and *solenoidal* does not mean that the field cannot curve. The gravity field in the left panel has non-zero divergence within the mass distribution. The magnetic field in the right panel has non-zero curl, but zero divergence.

```{admonition} Exercise: from potentials to physical fields
:class: tip

Work in Cartesian coordinates.

1. Inside a sphere with uniform mass density $\rho$, postulate the gravitational potential per unit mass

   $$
     \Phi_g(x,y,z)=\frac{2\pi G\rho}{3}(x^2+y^2+z^2),
   $$

   where an arbitrary additive constant has been omitted. Calculate $\vec{g}=-\vec{\nabla}\Phi_g$. Then show that $\vec{\nabla}\times\vec{g}=\vec{0}$ and calculate $\vec{\nabla}\cdot\vec{g}$. How does the sign of the divergence relate to the converging arrows in the left panel?

2. Inside a long cylindrical wire carrying a uniform current density $\vec{J}=J\hat{z}$, postulate the vector potential

   $$
     \vec{A}(x,y,z)=-\frac{\mu_0J}{4}(x^2+y^2)\hat{z}.
   $$

   Calculate $\vec{B}=\vec{\nabla}\times\vec{A}$. Then show that $\vec{\nabla}\cdot\vec{B}=0$ and calculate $\vec{\nabla}\times\vec{B}$. How do these results relate to the circulating arrows in the right panel?
```

Later in the course we will use vector potentials to describe magnetic fields in more detail. For now, we will begin with the nicely irrotational gravity field.
