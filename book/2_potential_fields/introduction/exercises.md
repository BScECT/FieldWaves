# Exercises: Work, Fields and Potential

These problems consolidate the section. For each one, sketch or predict first, calculate second, and finish with a sentence interpreting the result. Hints and checks are folded away so they can be used after an individual or paired attempt.

## 1. Work along an unfamiliar route

In a uniform gravitational field $\vec g=-g_0\hat z$, a mass $m$ travels from $A=(0,0,0)$ to $B=(L,0,h)$ by first rising to height $2h$, moving horizontally to $x=L$, and descending to $B$. Here $L,h,g_0>0$.

1. Predict the sign of the total work by gravity.
2. Calculate the work on each segment and add it.
3. Compare with a straight path from $A$ to $B$ using $\vec g\cdot d\vec s=-g_0\,dz$.
4. Find $\Delta U$ and $\Delta\Phi$. Which quantities depend on the test mass?

```{admonition} Check your reasoning
:class: dropdown

The three work contributions are $-2mg_0h$, zero, and $+mg_0h$. Their sum is $-mg_0h$. Integrating along any path gives the same result because only the net change in $z$ remains. Thus $\Delta U=mg_0h$ and $\Delta\Phi=g_0h$. Work and energy depend on $m$; the field and potential difference do not.
```

## 2. Potential value, gradient and reference

Consider $\Phi(x,y,z)=g_0z+C$.

1. Give two different choices of $C$ that describe the same field.
2. Where is $\Phi=0$ for each choice? Does the field vanish there?
3. Sketch two equipotential surfaces and the field direction.
4. A particle is displaced within one equipotential. Does zero gravitational work imply that no other force can do work?

```{admonition} Check your reasoning
:class: dropdown

For example, $C=0$ and $C=-g_0h$ put the zero-potential plane at $z=0$ and $z=h$. Both give $\vec g=-g_0\hat z$. The equipotentials are horizontal planes; the field points toward decreasing potential. The gravitational work within a plane is zero. This says nothing about the work done by other forces or about the effort needed to prescribe a path.
```

## 3. One field, two different integrals

A uniform field $\vec g=-g_0\hat z$ passes through a rectangular box. Let $C$ be a closed rectangular path on one vertical face and $S$ the entire closed surface of the box.

1. Explain geometrically why $\oint_C\vec g\cdot d\vec s=0$.
2. Explain separately why $\oint_S\vec g\cdot\hat n\,dA=0$.
3. State the units of each integral. Which becomes work when multiplied by $m$?
4. Does either zero imply that the field is zero?

```{admonition} Check your reasoning
:class: dropdown

Upward and downward path contributions cancel; horizontal ones vanish. For flux, the top and bottom faces contribute opposite amounts and the side faces contribute zero. The circulation has units $\mathrm{m^2/s^2}=\mathrm{J/kg}$; the flux has units $\mathrm{m^3/s^2}$. Only the first becomes work after multiplication by mass. Neither zero requires zero field.
```

## 4. Can this force have a position potential energy?

Let $\vec F=k(-y\hat x+x\hat y)$, where $k>0$ has units $\mathrm{N/m}$. Traverse the circle $x=R\cos t$, $y=R\sin t$, $0\leq t\leq2\pi$, counterclockwise.

1. Sketch the force at the four axis intersections before integrating.
2. Write the displacement vector $d\vec s$ and find $\oint\vec F\cdot d\vec s$.
3. Can a single-valued function $U(x,y)$ satisfy $\vec F=-\vec\nabla U$ throughout the plane?
4. Explain why a source must supply energy if this force is maintained while a particle repeatedly follows the circle.

```{admonition} Hint and check
:class: dropdown

Use $d\vec s=R(-\sin t\hat x+\cos t\hat y)dt$. The dot product is $kR^2dt$, so the work is $2\pi kR^2>0$. A position potential would return to its initial value after a loop and cannot account for this nonzero work. Maintaining repeated positive work requires an energy supply; nonconservative forces do not invalidate conservation of energy.
```
