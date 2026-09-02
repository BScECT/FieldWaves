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
