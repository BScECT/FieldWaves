# Sums, series, approximations

In all classical physics domains, it is useful to write a quantity as a sum of a large number of terms. In many cases, each such term has a physical interpretation. Often, the large sum of terms can be approximated by neglecting most terms based on physical arguments, and keeping only a few terms as the approximate solution for the quantity we investigate.

A simple example is position as a function of time. A particle that is not moving has a fixed position and we can denote it as

$$
x(t) = x_0 .
$$

This expression states that for any time value the particle is located at position $x_0$. If at $t=0$ the particle starts to move with a constant velocity $v_0$, the position becomes a linear function of time. We can express it as

$$
x(t) = x_0 + v_0 t .
$$

If we take $t=0$ in this expression, we find the starting position $x(t=0) = x_0$. To find the velocity, we must differentiate the position with respect to time and find

$$
v_0 = \frac{\mathrm{d}x(t)}{\mathrm{d}t} .
$$

As long as the velocity is constant, we can evaluate this expression at any time instant, but if the velocity is variable we must evaluate the expression at $t=0$. Hence, we express velocity as

$$
v_0 = \lim_{t\downarrow 0}\frac{\mathrm{d}x(t)}{\mathrm{d}t}
    = \left.\frac{\mathrm{d}x(t)}{\mathrm{d}t}\right|_{t\downarrow 0} .
$$

:::{admonition} The unit-step function
:class: note
Note that in this expression we take the limit from positive values of $t$ to zero, because the derivative of the position of the particle is not continuous at $t=0$. This can be seen because $x(t) = x_0$ for $t<0$, and the velocity of the particle is $v=0$ for $t<0$ and $v=v_0$ for $t>0$. We express this as

$$
v(t) = v_0\, u(t) ,
$$

where $u(t)$ is known as the unit-step function, given by

$$
u(t) = \left\{
\begin{array}{ll}
0    & t < 0 \\
1/2  & t = 0 \\
1    & t > 0
\end{array}\right. .
$$

This function is also known as the Heaviside function, after Oliver Heaviside. The value at $t=0$ for $u(t)$ is obtained by taking the limit on both sides to $t=0$ and keeping the average. This is called the principal value. To avoid differentiating a function with a step discontinuity at this moment, we have used the differentiation in the time window where the position of the particle is continuous and continuously differentiable. We deal with differentiating across discontinuities later.
:::

Suppose the particle also has a constant acceleration $a_0$. From classical mechanics we know that the position of the particle as a function of time can then be expressed as

$$
x(t) = x_0 + v_0 t + \tfrac{1}{2}a_0 t^2 .
$$

To find $x_0$ and $v_0$ we can use the recipes above, while to obtain $a_0$ we must differentiate $x(t)$ twice with respect to $t$. Now we assume the position of the particle is twice continuously differentiable with respect to time, and this is true for both negative and positive times but not for $t=0$. Hence, to find the acceleration, we should evaluate

$$
a_0 = \lim_{t\downarrow 0}\frac{\mathrm{d}^2 x(t)}{\mathrm{d}t^2}
    = \left.\frac{\mathrm{d}^2 x(t)}{\mathrm{d}t^2}\right|_{t\downarrow 0} .
$$

It shows the intuitive knowledge that acceleration is in the second derivative of position with respect to time.

Now, if we generalise this notion, we can think of a position that changes location in an arbitrary way and has many more non-zero derivatives that are all smooth functions of time except across the start of the motion. This is one of the aspects of the principle of causality: a response cannot be present before an action happens. In classical mechanics it means the position cannot change unless the particle is already in motion or a force acts on it, in which case it has a non-zero acceleration. This notion belongs to the concept of the generation of fields and waves and we discuss it in more detail later. Here we state that the position of the particle can be generally expressed as

$$
x(t) = c_0 + c_1 t + c_2 t^2 + \cdots = \sum_{m=0}^{\infty} c_m t^m ,
$$ (eq:pm)

and

$$
c_m = \left.\frac{1}{m!}\frac{\mathrm{d}^m x(t)}{\mathrm{d}t^m}\right|_{t\downarrow 0} .
$$

## The Taylor series

This series, where a function is expressed as a sum of terms with increasing powers of the independent variable, is called a Taylor series. It demonstrates that we can know a function if we know its value at every point in time, $x(t)$, **or** when we know all of its derivatives at one single time instant. This is under the assumptions that

1. the function is continuously differentiable infinitely many times, and
2. the series sums up to a finite result that represents the function.

The Taylor series can of course be used for any function, for any variable, and in more than one dimension. We can therefore write an arbitrary function of position $x$ as $f(x)$ and express it as

$$
f(x) = \sum_{m=0}^{\infty}\left.\frac{1}{m!}\frac{\mathrm{d}^m f(x)}{\mathrm{d}x^m}\right|_{x=0} x^m
     = f(0) + x f^{(1)}(0) + \frac{f^{(2)}(0)}{2}x^2 + \cdots ,
$$

where $f^{(m)}(0)$ is short-hand notation for $\left.\dfrac{\mathrm{d}^m f(x)}{\mathrm{d}x^m}\right|_{x=0}$.

It is not necessary to expand a function around zero, and we can expand it around any point $x=a$. It is given by

$$
f(x) = \sum_{m=0}^{\infty}\frac{f^{(m)}(x=a)}{m!}(x-a)^m
     = f(a) + f^{(1)}(a)(x-a) + \frac{f^{(2)}(a)}{2}(x-a)^2 + \cdots .
$$ (eq:Taylor)

We saw for the particle motion that for negative $t$ the particle is at rest and has position $x_0$. The reason is that at $t=0$ something happens and the information is not present in $x(t)$ for negative times. We saw that $x(t)$ changes continuously, but the slope does not change continuously. Functions that have a discontinuity in one or more derivatives are called non-analytic. Taylor series cannot be used for such functions. Until you reach a derivative that is not continuous, a truncated Taylor series expansion can still be useful.

## Exercises

1. Expand the particle motion of {eq}`eq:pm` around $t=-1$, using $f(x) = x(t)$ in {eq}`eq:Taylor` with $a=-1$, and explain why it is not giving you more than $x(t) = x_0$.
2. Find the expansions for $\sin(x)$, $\cos(x)$, $\exp(-x)$, $(1+x)^{-1}$ around $x=0$ and determine whether the Taylor series converges.
3. What happens if you try a Taylor series expansion for $\sqrt{t}$ and $1/t$?
4. Consider the simple model of the bouncing ball problem. The ball leaves the surface at $z=0$ with upward velocity $v_0$.

    (a) Give the expression for the height of the ball for $t>0$ that is valid until the ball hits the ground again for the first time.

    (b) Determine the time $T_0$ at which the ball hits the ground and the maximum height $H$ the ball reaches the first time.

    Assume that every time the ball hits the ground there is some plastic deformation of the ball and the ball loses a fraction $\gamma$ of its energy at every bounce, such that at the $n^{\text{th}}$ bounce the velocity can be expressed as $v_n = \sqrt{1-\gamma}\,v_{n-1}$ for $n>0$.

    (c) The time it takes to complete the $n^{\text{th}}$ bounce, $T_n$, can be written in terms of $T_{n-1}$ as $T_n = \alpha T_{n-1}$, and in terms of $T_0$ as $T_n = \beta T_0$. Determine $\alpha$ and $\beta$.

    (d) Show that $T_n = (1-\gamma)^{n/2}\sqrt{\dfrac{8H}{g}}$.

    (e) Give an expression for $T_\infty$ by evaluating the series $T_\infty = \sum_{m=0}^{\infty}T_m$. Since $\gamma$ is a fraction, it has a positive non-zero value smaller than 1, so that the series can be summed to an explicit expression. Why does it take only a finite time for the ball to make infinitely many bounces?

    (f) If the energy loss per bounce is extremely small, $\gamma\ll 1$, use a Taylor series expansion around $\gamma=0$ for $T_\infty$ and keep only the leading term as a first-order approximation to the time required to make an infinite number of bounces.

    (g) Plot the height as a function of time and try different values for $\gamma$, to understand truncation of a series as an approximation of a function. How many terms do you need in the sum to arrive at the same time as the approximate expression?

    :::{admonition} Answers to (a)–(f)
    :class: tip dropdown
    (a) $z = v_0 t - \tfrac{1}{2}gt^2$.

    (b) $H = \dfrac{v_0^2}{2g}$ and $T_0 = \dfrac{2v_0}{g}$.

    (c) $T_n$ is proportional to $v_n$, hence $T_n = \sqrt{1-\gamma}\,T_{n-1} = (1-\gamma)^{n/2}T_0$, so $\alpha=\sqrt{1-\gamma}$ and $\beta=(1-\gamma)^{n/2}$.

    (d) In the expression for $T_n$ in (c), express $T_0$ in terms of $H$ instead of in terms of $v_0$.

    (e) $T_\infty = T_0\sum_{m=0}^{\infty}(1-\gamma)^{m/2} = \sqrt{\dfrac{8H}{g}}\dfrac{1}{1-\sqrt{1-\gamma}}$.

    (f) In that case $\sqrt{1-\gamma}\approx 1-\tfrac{\gamma}{2}$ and $T_\infty \approx \sqrt{\dfrac{8H}{g}}\dfrac{2}{\gamma}$.
    :::
