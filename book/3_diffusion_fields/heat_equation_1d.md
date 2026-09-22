# The heat equation in one dimension

Let us assume the heat can flow only in the $x$-direction, like in a bar. This reduces the heat equation, {eq}`eq:Heat`, to

$$
\partial_t T - \kappa\,\partial_x^2 T = 0,
$$ (eq:Heat1D)

where we assume no source or sink is present, for which reason the right-hand side is zero. If we want to find a solution to this equation, we will need other information. These are initial conditions and boundary conditions. The number of conditions needed is equal to the highest order derivative in a variable. {eq}`eq:Heat1D` has a first-order time derivative, which means we need one initial or boundary condition, and it has a second-order spatial derivative, which means we need two initial or boundary conditions in space. Let us assume the bar has length $L$ and extends from $x=0$ to $x=L$. So-called Dirichlet conditions describe the temperature at the end points, $x=0$ and $x=L$, e.g., $T(0,t)=0$ and $T(L,t)=0$. So-called Neumann conditions prescribe the normal component of the current, or, in this case, the first spatial derivative of temperature. For example, a no-flow end-point condition for an insulated bar, meaning no heat can flow away from the bar, is expressed as

$$
\begin{aligned}
\partial_x T(0,t) &= 0, \\
\partial_x T(L,t) &= 0.
\end{aligned}
$$

For some source-free problems, solutions can be found using the technique of separation of variables. This means that we can write the temperature in the bar as a product of a function that depends only on position and a function that depends only on time. We are going to find a solution for two different cases.

## Example 1: bar with zero temperature at the end points

For such a bar we use the 1D heat equation with conditions on the temperature at the end points,

$$
\begin{aligned}
\partial_t T &= \kappa\,\partial_x^2 T, \\
T(x,0) &= h(x), \\
T(0,t) &= 0, \\
T(L,t) &= 0.
\end{aligned}
$$

Note that the boundary condition at zero time is an arbitrary function $h(x)$ of position. This condition allows for non-trivial solutions and this means that the function $h(x)$ can be seen as the starting point of the diffusive process. We could see it as equivalent to the presence of a source. The boundary conditions do not depend on time and space simultaneously and we can try a solution with separation of variables. We take a solution in the form

$$
T(x,t) = f(x)\,g(t),
$$

and put it in the equation to find

$$
\begin{aligned}
\partial_t\left[f(x)g(t)\right] &= \kappa\,\partial_x^2\left[f(x)g(t)\right], \\
f(x)\,\partial_t g(t) &= \kappa\,g(t)\,\partial_x^2 f(x), \\
\frac{\partial_t g(t)}{g(t)} &= \kappa\frac{\partial_x^2 f(x)}{f(x)} = -\kappa\lambda .
\end{aligned}
$$

The separation constant $\lambda$ is introduced to be able to separate the two equations and solve them independently. Note that attaching $\kappa$ to the separation constant is not required but convenient. If you don't do it, it does not matter. When you discover in a later step that it would be better to do it, you can come back here and do it after all. We can now write the equation as two equations,

$$
\begin{aligned}
\partial_t g(t) &= -\kappa\lambda\,g(t), \\
\partial_x^2 f(x) &= -\lambda\,f(x).
\end{aligned}
$$

Now, we must find out if we can satisfy the boundary conditions for $T(x,t)$ and move them to conditions for $f(x)$ and $g(t)$. We find

$$
T(0,t) = f(0)g(t) = 0 \quad\text{and}\quad T(L,t) = f(L)g(t) = 0 .
$$

If we would choose $g(t)=0$ then we would find the trivial solution that the temperature is zero everywhere and for all times. Hence, we choose $f(0)=f(L)=0$ as boundary conditions for $f(x)$. The separation constant $\lambda$ is known as the eigenvalue of the problem. We are going to find that non-trivial solutions are found only for specific values of $\lambda$. The non-trivial solution for a value of $\lambda$ is then called an eigenfunction. You have encountered or will encounter this in the course ECTB2130, Signals and Time Series. An eigenfunction of a differential equation is a function that, when it is taken as an input signal, gives as output the same function scaled by a factor, which is then the corresponding eigenvalue.

Now we are ready to solve the corresponding two equations,

$$
\begin{aligned}
(\partial_t + \kappa\lambda)\,g &= 0, \\
(\partial_x^2 + \lambda)\,f &= 0, \\
f(0) = f(L) &= 0 .
\end{aligned}
$$

In fact, we solve first the spatial equation. We must consider three ranges for $\lambda$ to find solutions for the second-order differential equation.

**Case $\lambda>0$.** For positive eigenvalues, the solution consists of oscillating functions,

$$
f(x) = c_1\sin(x\sqrt{\lambda}) + c_2\cos(x\sqrt{\lambda}).
$$

Because $f(0)=0$, we find $c_2=0$. Because $f(L)=0$, we find that $\sin(L\sqrt{\lambda})=0$, which leads to

$$
\lambda = \left(\frac{n\pi}{L}\right)^2, \quad\text{for } n=1,2,3,\cdots,
$$

hence the solution is given by

$$
f(x) = c_1\sin\left(\frac{n\pi x}{L}\right), \quad\text{for } n=1,2,3,\cdots .
$$

There is an infinite number of eigenvalues, each of which has its own eigenfunction as solution to the problem. Note that $c_1$ is not determined by this condition and we could remove it, because later we will need to make sure to satisfy the last condition of $T(x,0)=h(x)$. For simplicity we keep it here as an undetermined constant.

**Case $\lambda=0$.** For a zero eigenvalue, the solution is given by $f(x)=c_0+c_1x$. Because both $f(0)$ and $f(L)$ must be zero, we find that both coefficients are zero and only the trivial solution exists. Hence $f(x)=0$. This also means that $\lambda=0$ is not an eigenvalue for this problem!

**Case $\lambda<0$.** For negative eigenvalues, the solution consists of exponential functions given by

$$
f(x) = c_1\exp(x\sqrt{-\lambda}) + c_2\exp(-x\sqrt{-\lambda}).
$$

Setting $f(0)=0$ and $f(L)=0$ leads again to $c_1=0$ and $c_2=0$. We see that for negative values of $\lambda$ only the trivial solution is found. Hence, also no negative eigenvalues exist for this problem.

Now it is time to solve the time equation. We must consider only positive values of $\lambda$ and substitute $\lambda_n$ that we can later specify as found above. For each value of $\lambda_n$, we should find a solution $g_n(t)$. The corresponding equation is written as

$$
(\partial_t + \kappa\lambda_n)\,g_n = 0 .
$$

This is a simple first-order equation and we know that exponential functions are repeated when differentiated. Hence, we find the solution to be of the form

$$
g_n(t) = c_n\exp(-\kappa\lambda_n t) = c_n\exp\left[-\kappa\left(\frac{n\pi}{L}\right)^2 t\right].
$$

The temperature is given by the product of the two solutions. We can write for every $n$,

$$
T_n(x,t) = C_n\sin\left(\frac{n\pi x}{L}\right)\exp\left[-\kappa\left(\frac{n\pi}{L}\right)^2 t\right].
$$ (eq:T1Dn)

The coefficient $C_n$ combines the coefficients we found in the solution in space and in time. Note that this is a solution, but that does not mean that this function alone can satisfy all boundary conditions we can think of. The function $h(x)$ of the boundary condition at zero time is an arbitrary function of position. This means that the solution is quite restrictive and can be used only for functions $h(x)$ that match $T_n(x,0)$. We are of course allowed to combine solutions for different values of $n$, because the problem is linear and the principle of superposition applies. This means we can write the temperature as a solution to the heat equation as

$$
T(x,t) = \sum_{n=1}^{\infty} C_n\sin\left(\frac{n\pi x}{L}\right)\exp\left[-\kappa\left(\frac{n\pi}{L}\right)^2 t\right],
$$

with initial condition

$$
T(x,0) = h(x) = \sum_{n=1}^{\infty} C_n\sin\left(\frac{n\pi x}{L}\right).
$$ (eq:BCheat1D)

With an infinite sum of functions, we can imagine we can satisfy almost all functions $h(x)$. Now the question is: How can we find the coefficients $C_n$ such that {eq}`eq:BCheat1D` is satisfied? That is not very difficult. We see that the argument of the sine-function is at least spanning half a period for $0<x<L$. If we multiply the sine-function with a sine-function that has the same argument but a different counter $m$, and integrate over the length $L$, we obtain

$$
\int_{x=0}^{L} h(x)\sin\left(\frac{m\pi x}{L}\right)\mathrm{d}x
= \sum_{n=1}^{\infty} C_n\int_{x=0}^{L}\sin\left(\frac{n\pi x}{L}\right)\sin\left(\frac{m\pi x}{L}\right)\mathrm{d}x .
$$ (eq:F-orth)

When $m\ne n$, we integrate the right-hand side of {eq}`eq:F-orth` over a product of two different sine-functions, one of which spans at least a whole period, and the integral is equal to zero. When $m=n$ we integrate a squared sine-function and the result is $L/2$, as we have seen in the example of the theorem of Gauss in cylindrical and spherical coordinates in the chapter on [divergence](../1_gradient_divergence_curl/divergence.md). Hence, we find

$$
\int_{x=0}^{L}\sin\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x
= \left\{\begin{array}{ll}
0, & m\ne n, \\[1mm]
\displaystyle\int_{x=0}^{L}\sin^2\left(\frac{n\pi x}{L}\right)\mathrm{d}x = \frac{L}{2}, & m=n .
\end{array}\right.
$$

This result is known as Fourier orthogonality of sine-functions. It is part of Fourier theory and you have seen this already in the course ECTB2130, Signals and Time Series. Substituting this result in our solution gives

$$
C_n = \frac{2}{L}\int_{x=0}^{L} h(x)\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x .
$$

Notice that we didn't have to specify $h(x)$ and we conclude we can now use this solution for any boundary condition $h(x)$. This is not entirely true and the conditions on $h(x)$ under which it is true are discussed in ECTB2130. The final solution is then given by

$$
\begin{aligned}
T(x,t) &= \sum_{n=1}^{\infty} C_n\sin\left(\frac{n\pi x}{L}\right)\exp\left[-\kappa\left(\frac{n\pi}{L}\right)^2 t\right], \\
C_n &= \frac{2}{L}\int_{x=0}^{L} h(x)\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x .
\end{aligned}
$$

With these two expressions, we have finally fully solved a partial differential equation with Dirichlet boundary conditions. Now we solve one with Neumann boundary conditions.

## Example 2: bar with insulated end points

For such a bar we use the 1D heat equation with conditions on the derivative of the temperature at the end points. Because only the boundary conditions are different from the previous example, we take big steps here. The equations to solve are

$$
\begin{aligned}
\partial_t T &= \kappa\,\partial_x^2 T, \\
T(x,0) &= h(x), \\
\lim_{x\downarrow 0}\partial_x T(x,t) &= T'(0,t) = 0, \\
\lim_{x\uparrow L}\partial_x T(x,t) &= T'(L,t) = 0 .
\end{aligned}
$$

We choose again a solution with separation of variables and take a solution in the same form as before,

$$
T(x,t) = f(x)\,g(t),
$$

and put it in the equation to find the following ordinary differential equations,

$$
\begin{aligned}
\partial_t g(t) &= -\kappa\lambda\,g(t), \\
\partial_x^2 f(x) &= -\lambda\,f(x).
\end{aligned}
$$

Now, we must find out if we can satisfy the boundary conditions for $T(x,t)$ and move them to conditions for $f(x)$ and $g(t)$. We find

$$
T'(0,t) = f'(0)g(t) = 0 \quad\text{and}\quad T'(L,t) = f'(L)g(t) = 0 .
$$

We can choose only $f'(0)=f'(L)=0$ to avoid finding the trivial solution only. We again investigate the three regimes for values of $\lambda$.

**Case $\lambda>0$.** For positive eigenvalues, the solution consists of oscillating functions,

$$
f(x) = c_1\sin(x\sqrt{\lambda}) + c_2\cos(x\sqrt{\lambda}).
$$

Because $f'(0)=0$, we find $\left.\partial_x f(x)\right|_{x=0} = c_1\sqrt{\lambda} = 0$, hence $c_1=0$. Because $f'(L)=0$, we find that $c_2\sin(L\sqrt{\lambda})=0$, which leads to

$$
\lambda = \left(\frac{n\pi}{L}\right)^2, \quad\text{for } n=1,2,3,\cdots,
$$

hence the solution is given by

$$
f_n(x) = c_2\cos\left(\frac{n\pi x}{L}\right), \quad\text{for } n=1,2,\cdots .
$$

There is an infinite number of eigenvalues, each of which has its own eigenfunction as solution to the problem.

**Case $\lambda=0$.** For a zero eigenvalue, the solution is given by $f(x)=c_0+c_1x$. Because both $f'(0)$ and $f'(L)$ must be zero, we find that the coefficient $c_1=0$ and only the solution $f(x)=c_0$ exists for $\lambda=0$. This means that $\lambda=0$ is an eigenvalue for this problem!

**Case $\lambda<0$.** For negative eigenvalues, the solution consists of exponential functions given by

$$
f(x) = c_1\exp(x\sqrt{-\lambda}) + c_2\exp(-x\sqrt{-\lambda}).
$$

To impose $f'(0)=0$ and $f'(L)=0$ we need

$$
f'(x) = \sqrt{-\lambda}\left[c_1\exp(x\sqrt{-\lambda}) - c_2\exp(-x\sqrt{-\lambda})\right].
$$

This leads from $f'(0)=0$ to $c_1=c_2$, and from $f'(L)=0$ we find $c_1=c_2=0$. Hence, there are no negative eigenvalues for this problem.

The total solution so far is

$$
f_n(x) = c_2\cos\left(\frac{n\pi x}{L}\right), \quad\text{for } n=0,1,2,\cdots .
$$

Now it is time to solve the time equation. We recognise that this part of the problem is the same as before and we find the solution to be of the form

$$
g_n(t) = c_n\exp\left[-\kappa\left(\frac{n\pi}{L}\right)^2 t\right].
$$

The temperature is given by the product of the two solutions. We can write for every $n$

$$
T_n(x,t) = C_n\cos\left(\frac{n\pi x}{L}\right)\exp\left[-\kappa\left(\frac{n\pi}{L}\right)^2 t\right], \quad n=0,1,2,\cdots .
$$ (eq:T1Dnc)

Note that $n=0$ is now part of the solution. The temperature as a solution to the heat equation is the sum of all solutions $T_n$ and given by

$$
T(x,t) = \sum_{n=0}^{\infty} C_n\cos\left(\frac{n\pi x}{L}\right)\exp\left[-\kappa\left(\frac{n\pi}{L}\right)^2 t\right],
$$

with initial condition

$$
T(x,0) = h(x) = \sum_{n=0}^{\infty} C_n\cos\left(\frac{n\pi x}{L}\right).
$$

What we found for Fourier sine-series in the previous example applies to the Fourier cosine-series as well. Applying Fourier orthogonality of cosine-functions results in the final solution

$$
\begin{aligned}
T(x,t) &= \sum_{n=0}^{\infty} C_n\cos\left(\frac{n\pi x}{L}\right)\exp\left[-\kappa\left(\frac{n\pi}{L}\right)^2 t\right], \\
C_n &= \left\{\begin{array}{ll}
\dfrac{1}{L}\displaystyle\int_{x=0}^{L} h(x)\,\mathrm{d}x, & n=0, \\[3mm]
\dfrac{2}{L}\displaystyle\int_{x=0}^{L} h(x)\cos\left(\frac{n\pi x}{L}\right)\mathrm{d}x, & n=1,2,3,\cdots .
\end{array}\right.
\end{aligned}
$$

With these two expressions, we have fully solved a partial differential equation with Neumann boundary conditions. Note that now the temperature does not necessarily go to zero when time goes to infinity.

## A completely different solution procedure

### An infinitely long wire with an initial Gaussian temperature distribution

Solving problems with separation of variables is not always the best solution, e.g., when the temperature distribution at $t=0$ is a Gaussian function. For this example, we assume an infinitely long wire. Hence, we are solving

$$
\begin{aligned}
\partial_t T &= \kappa\,\partial_x^2 T, \\
T(x,0) &= T_0\exp\left(-\frac{x^2}{L^2}\right).
\end{aligned}
$$ (eq:c0time)

Note that we do not use explicit boundary conditions at the end points, but are satisfied with zero conditions, which seems to make sense from a physical point of view. We can see from the initial condition of {eq}`eq:c0time` that

$$
\lim_{x\rightarrow\pm\infty} T(x,t) = 0 .
$$ (eq:endcond)

The boundary condition at zero time shows that at $x=0$ and $t=0$ the temperature is $T_0$, which is the peak value of the temperature. The constant $L$ in the Gaussian is a measure of the width of the Gaussian function. The actual peak value may change and the width of the Gaussian may change, but we assume that the solution will have a Gaussian structure in space, and we are going to find what its time behaviour then is. Let us propose a solution of the form

$$
T(x,t) = f(t)\exp\left(-h(t)x^2\right).
$$

The two functions $f(t)$ and $h(t)$ allow for time variations in peak temperature and the time at which the peak occurs. Note that this solution cannot be easily written as a product of a time-dependent function and a space-dependent function as we did in the method of separation of variables. For $h(t)\ge 0$, the temperature will exponentially decrease with increasing $x$. Because we introduce two new time functions that we want to find, we need boundary conditions for them. We can find them from the boundary condition on $T(x,0)$ as

$$
f(0) = T_0, \qquad h(0) = \frac{1}{L^2} .
$$ (eq:initchf)

We substitute the proposed solution in {eq}`eq:Heat1D` and find

$$
\begin{aligned}
\exp\left(-h(t)x^2\right)\left[\partial_t f(t) - x^2 f(t)\,\partial_t h(t)\right] &= \kappa\left[4f(t)h^2(t)x^2 - 2f(t)h(t)\right]\exp\left(-h(t)x^2\right), \\
\partial_t f(t) + 2\kappa f(t)h(t) &= x^2\left[f(t)\,\partial_t h(t) + 4\kappa f(t)h^2(t)\right].
\end{aligned}
$$

Similar to the solution with separation of variables, here we see that the left-hand side of the equation constitutes an equation that can be solved independent from $x$, and the right-hand side does depend on the location. Hence the whole equation can be satisfied for all values of $x$ only when the left-hand side is satisfied independently from the right-hand side and vice versa. We find the following two differential equations,

$$
\partial_t f(t) = -2\kappa f(t)h(t),
$$ (eq:eqhf)

$$
\partial_t h(t) = -4\kappa h^2(t).
$$ (eq:eqhh)

The first equation depends on both $f(t)$ and $h(t)$ and must be solved after we solve the equation for $h(t)$. It is not hard to show that

$$
h(t) = \frac{1}{4\kappa t + L^2}
$$

is a solution to {eq}`eq:eqhh` that satisfies the initial condition of {eq}`eq:initchf` as well. Similarly, it is then not hard to show that

$$
f(t) = T_0\frac{L}{\sqrt{4\kappa t + L^2}}
$$

satisfies {eq}`eq:eqhf` and satisfies the initial condition of {eq}`eq:initchf`. This solves the problem and we find the temperature along the bar as a function of time as

$$
T(x,t) = \frac{T_0 L}{\sqrt{4\kappa t + L^2}}\exp\left(-\frac{x^2}{4\kappa t + L^2}\right).
$$ (eq:TGauss)

Notice that we have solved the heat equation using the initial condition for $T(x,0)$ at zero time expressed in {eq}`eq:c0time` and end-point conditions at infinity for all times expressed in {eq}`eq:endcond`. We found a solution in terms of a single expression using ordinary functions. It is clear that this problem cannot be easily solved with the method of separation of variables. In the exercises, we find a solution in terms of the Fourier cosine series. The explicit exact solution that we found here gives a better insight in the space-time behaviour of diffusive fields than the solution with separation of variables, and can be analysed.

### Analysis of the outcome

**Early time behaviour.** We can see that for zero time, the solution is well behaved, because the square root in time in the denominator goes to $L$ when time goes to zero and the temperature goes to $T_0$ as given as the initial value. If we think about the origin of this heat, it must have come from some negative time, and we can imagine it must have come from time equal to $t=-L^2/(4\kappa)$. In that case the denominator goes to zero and the polynomial term will blow up to infinity. But we can see that for $x\ne 0$, the exponential function has the time in the denominator of its argument and that will bring the temperature to zero at $t=-L^2/(4\kappa)$. The only problematic point is then $x=0$, which must be the location of the origin of the heat. This is characteristic for solutions to the diffusive field equation with a source that is approximated to be localised in a single point. Note that all finite order derivatives to time of this function go to zero at zero time. Another way of saying this is: an exponential function with a negative argument that is inversely proportional to time goes to zero faster than a polynomial of any finite inverse power of time goes to infinity for zero time. Notice that for times $t<-L^2/(4\kappa)$ the solution is no longer physical. The reason is that the square root in the polynomial term will have a negative argument and the outcome of such a square root will be complex, which we regard as non-physical in space-time. You can see that

$$
\begin{aligned}
\lim_{t\uparrow -\frac{L^2}{4\kappa}}\exp\left(-\frac{x^2}{4\kappa t + L^2}\right) &= \infty, \\
\lim_{t\rightarrow -\infty}\exp\left(-\frac{x^2}{4\kappa t + L^2}\right) &= 1,
\end{aligned}
$$

from which we conclude that negative infinite time is not a problem for the exponential term, but the negative side of the zero denominator in the exponential function is the problem. In addition, we can see that for any fixed time $t<-L^2/(4\kappa)$ the exponential function is no longer well-behaved as a function of $x$ and grows exponentially for increasing distance. That is a second reason to regard solutions for $t<-L^2/(4\kappa)$ as non-physical.

**Late time behaviour.** The late-time behaviour is entirely determined by the polynomial function, and hence we conclude that the temperature drops proportional to the inverse square root of time and does not depend on location anymore! The reason is that when $t\rightarrow\infty$, $\exp\left[-x^2/(4\kappa t + L^2)\right]\rightarrow 1$ for any fixed position. Hence, the exponential function is a Gaussian in space, but as a function of time it is zero at zero time and it smoothly goes to 1 at infinite time. Hence, for late times, the exponential function has no more influence on the value of the temperature in the bar.

**Time to the peak temperature.** We can compute how much time it takes for the temperature to reach its peak value at any point on the bar. To determine the time to the peak value, we take the derivative to time and equate the result to zero. The derivative to time of {eq}`eq:TGauss` is given by

$$
\begin{aligned}
\partial_t T(x,t) &= \exp\left(-\frac{x^2}{4\kappa t + L^2}\right)\partial_t\frac{T_0 L}{\sqrt{4\kappa t + L^2}}
+ \frac{T_0 L}{\sqrt{4\kappa t + L^2}}\,\partial_t\exp\left(-\frac{x^2}{4\kappa t + L^2}\right), \\
&= -\frac{2\kappa T_0 L}{(4\kappa t + L^2)^{3/2}}\exp\left(-\frac{x^2}{4\kappa t + L^2}\right)
+ \frac{4\kappa T_0 L x^2}{(4\kappa t + L^2)^{5/2}}\exp\left(-\frac{x^2}{4\kappa t + L^2}\right).
\end{aligned}
$$

This derivative is zero when time is equal to the time to the peak, $t_p$, and this is given by

$$
t_p = \frac{2x^2 - L^2}{4\kappa},
$$

from which it is clear that only for $|x|>L/\sqrt{2}$ this happens at positive times. That means that for points on the bar where $|x|<L/\sqrt{2}$ the temperature will only decrease for positive times, while for points $|x|>L/\sqrt{2}$ the temperature will first rise for $0<t<t_p$, after which the temperature will drop. Notice that the exponential function has a value of $1/\sqrt{e}$ independent of where on the bar the peak time will occur, and the value of the maximum temperature is entirely determined by the inverse square root term. We can write the temperature at the time it attains its peak value as

$$
T(x,t_p) = \frac{T_0 L}{\sqrt{2e}\,|x|}, \qquad\text{for } |x|>L/\sqrt{2} .
$$

We conclude that the temperature has a maximum value that is inversely proportional to distance $|x|$, and it occurs on the bar for positions $|x|>L/\sqrt{2}$.

### An infinitely long wire with an initial double Gaussian temperature distribution

If the initial condition specifies two shifted Gaussians, the solution can be written immediately by understanding that the superposition principle holds. This means that two separate initial conditions each lead to a solution that can be summed and that is equal to the solution we would obtain by specifying the two initial conditions as a single starting point and then solving the equation. Hence, if we have

$$
\begin{aligned}
\partial_t T &= \kappa\,\partial_x^2 T, \\
T(x,0) &= T_0\left[\exp\left(-\frac{(x+2L)^2}{L^2}\right) + \exp\left(-\frac{(x-2L)^2}{L^2}\right)\right],
\end{aligned}
$$ (eq:2c0time)

the solution can be readily given by

$$
T(x,t) = \frac{T_0 L}{\sqrt{4\kappa t + L^2}}\left[\exp\left(-\frac{(x+2L)^2}{4\kappa t + L^2}\right) + \exp\left(-\frac{(x-2L)^2}{4\kappa t + L^2}\right)\right].
$$ (eq:T2Gauss)

From this solution, and the fact that the exponential functions are quite distinct for early times but become equal for late times, we can understand that after some time we cannot distinguish between a field that consisted initially of two Gaussians and one that consisted of a single Gaussian temperature distribution. The closer the initial peak values are together, the earlier the blurring is such that the distinction cannot be made anymore. In a nutshell, that is the difficulty with analysing diffusive field signals when we record them to obtain information about the Earth.

As a last topic, we discuss the inhomogeneous electromagnetic diffusive field equations. This means we are going to put a source somewhere in space and solve Maxwell's diffusive field equations in one and three dimensions.

## Exercises

1. Solve {eq}`eq:Heat1D` with boundary conditions $T(x,0)=\tfrac{1}{2}$, $T(0,t)=T(L,t)=0$.
2. Solve {eq}`eq:Heat1D` with boundary conditions $T(x,0)=\tfrac{1}{2}$, $T'(0,t)=T'(L,t)=0$.
3. Solve {eq}`eq:Heat1D` with boundary conditions $T(x,0)=h(x)$, $T(0,t)=T'(L,t)=0$.
4. Python exercise: use the solution structure for {eq}`eq:Heat1D` as found in the first example of a bar of length $L$, hence with $T(0,t)=T(L,t)=0$, but now for $T(x,0)=h(x)=(0,-1,1,0)$ for $(0<x<L/4,\ L/4<x<L/2,\ L/2<x<3L/4,\ 3L/4<x<L)$, as shown in {numref}`fig-heat-ic-quarters`.

    ```{figure} figures/heat_ic_quarters.svg
    :name: fig-heat-ic-quarters
    :width: 55%

    Initial temperature $h(x)$ for exercise 4.
    ```

5. Python exercise: use the solution structure for {eq}`eq:Heat1D` as found in the second example of a bar of length $L$, hence with $T'(0,t)=T'(L,t)=0$, but now for $T(x,0)=h(x)=(1,-1,1)$ for $(0<x<L/3,\ L/3<x<2L/3,\ 2L/3<x<L)$, as shown in {numref}`fig-heat-ic-thirds`.

    ```{figure} figures/heat_ic_thirds.svg
    :name: fig-heat-ic-thirds
    :width: 55%

    Initial temperature $h(x)$ for exercise 5.
    ```

6. Python exercise: write a code for the solution expressed in {eq}`eq:TGauss`. Take the product $\kappa t$ on a logarithmic scale such that $-1<\log_{10}(\kappa t)<3$, $L=3$, and use a linear scale for position $-10<x<10$. Show a colour 2D plot as a function of all points in space and time where the colour shows the temperature, and make a line-plot movie of the temperature in space where time evolves.
7. Python exercise: repeat the previous exercise, but now with the double Gaussian as initial temperature distribution as given in {eq}`eq:2c0time`, which has the solution given in {eq}`eq:T2Gauss`. You can make the separation between the two Gaussians, which is now $4L$, a variable that you can change to see the effect on the shape of the time evolution of temperature along the bar.
