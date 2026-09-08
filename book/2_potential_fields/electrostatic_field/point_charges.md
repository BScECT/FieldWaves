# Point Charges and Superposition

Place a source charge $Q$ at $\vec r'$ and consider the field at the observation position $\vec r$. As in the gravity chapter, define

$$
\vec R=\vec r-\vec r',
\qquad
\hat R=\frac{\vec R}{|\vec R|}.
$$ (eq:electric-separation-vector)

The electric potential of the source charge, choosing $V\rightarrow0$ infinitely far away, is

$$
V(\vec r)
=\frac{1}{4\pi\epsilon_0}
\frac{Q}{|\vec r-\vec r'|}.
$$ (eq:point-charge-potential)

Taking the negative gradient gives

$$
\boxed{
\vec E(\vec r)
=\frac{1}{4\pi\epsilon_0}Q
\frac{\vec r-\vec r'}{|\vec r-\vec r'|^3}.
}
$$ (eq:point-charge-field)

```{admonition} Reminder: vector form versus unit-vector form
:class: note

The third power in the denominator does **not** make this an inverse-cube field. The numerator $\vec r-\vec r'$ is a vector whose magnitude is $|\vec r-\vec r'|$. One power in the denominator compensates for that magnitude and leaves the inverse-square dependence of the field strength. Using the unit vector from Equation {eq}`eq:electric-separation-vector`, we can write

$$
\frac{\vec r-\vec r'}{|\vec r-\vec r'|^3}
=
\frac{1}{|\vec r-\vec r'|^2}
\frac{\vec r-\vec r'}{|\vec r-\vec r'|}
=
\frac{\hat R}{|\vec r-\vec r'|^2}.
$$

The factor $1/|\vec r-\vec r'|^2$ sets the magnitude, while $\hat R$ supplies the direction.
```

For $Q>0$, the field points in the direction of $\vec R$, away from the source. For $Q<0$, multiplication by a negative number reverses the direction and the field points toward the source.

```{figure} figures/source_and_test_charge.svg
:name: source-and-test-charge
:width: 94%

A source charge $Q$ at $\vec r'$ creates the electric field at $\vec r$. A test charge $q$ placed there experiences a force. The separation vector is defined independently of the signs of either charge.
```

## Source charge and test charge

The electric field describes the influence of the **source charge** $Q$ before we choose what object to place in it. A sufficiently small **test charge** $q$ samples that field without appreciably rearranging the sources. The force on it is

$$
\boxed{\vec F=q\vec E.}
$$ (eq:electric-force-field)

Changing the sign of $Q$ reverses the field itself. Changing only the sign of $q$ leaves the field unchanged but reverses the force on the test charge. A positive test charge accelerates along $\vec E$; a negative test charge accelerates opposite to $\vec E$.

## Superposition

Electric potential and electric field obey the same linear superposition principle as their gravitational counterparts. For point charges $Q_i$ at positions $\vec r'_i$,

$$
V(\vec r)
=\frac{1}{4\pi\epsilon_0}
\sum_i\frac{Q_i}{|\vec r-\vec r'_i|},
$$ (eq:point-charge-superposition-potential)

and

$$
\vec E(\vec r)
=\frac{1}{4\pi\epsilon_0}
\sum_i Q_i
\frac{\vec r-\vec r'_i}{|\vec r-\vec r'_i|^3}.
$$ (eq:point-charge-superposition-field)

Positive and negative contributions can reinforce or cancel. The resulting field and potential should not be confused: their zeros need not occur at the same positions.

```{figure} figures/electric_dipole_field.png
:name: electric-dipole-field
:width: 100%

Electric field lines and equipotential contours for equal positive and negative point charges. Field lines follow $\vec E=-\vec\nabla V$ and therefore cross equipotentials at right angles. The plotting code is included in {doc}`making_of`.
```

```{admonition} Separate the roles of $Q$, $q$, $V$, and $\vec E$
:class: exercise

1. Which quantities change sign if the source charge $Q$ is reversed?
2. Which quantities change sign if only the test charge $q$ is reversed?
3. At a point where $V=0$, must $\vec E=0$?
4. At a point where $\vec E=0$, must $V=0$?
5. Use the dipole figure to find evidence for your answers.
```
