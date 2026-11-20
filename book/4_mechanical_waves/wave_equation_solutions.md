# Solution(s) to the wave equation

Let us focus on the wave equation for the pressure as given in {eq}`eq:waveqacp`. As you can see, it is a (scaled) difference of squares of the operators $\partial/\partial x$ and $\partial /\partial t$, and therefore it can be written as:

$$
\left\{ \frac{\partial}{\partial x}
	- \frac{1}{c} \frac{\partial}{\partial t} \right\}
\left\{ \frac{\partial}{\partial x}
	+ \frac{1}{c} \frac{\partial}{\partial t} \right\} p
    = 0.
$$

Each of the two terms on the left-hand side can be equal to zero, i.e.:

$$
\begin{aligned}
\frac{\partial p}{\partial x}
	& = \frac{1}{c} \frac{\partial p}{\partial t},
\\
  \frac{\partial p}{\partial x}
	& = - \frac{1}{c} \frac{\partial p}{\partial t}.
\end{aligned}
$$ (eq:waveqaconeway)

Each of these equations can be solved when considered as a boundary-value problem. Taking the first one: when at the boundary $x=0$, the pressure field is equal to some function $f(t)$, then we have the boundary-value problem:

$$
\begin{aligned}
   \frac{\partial p}{\partial x}
	    & = \frac{1}{c} \frac{\partial p}{\partial t},
\\
  p(x\!=\!0,t) & = f(t).
\end{aligned}
$$ (eq:bvproblem)

From this set, the solution is quite easy to find: the partial derivative in one direction is a $c$-scaled version of the partial derivative in the other direction. The solution is then found to be:

$$
p(x,t) = f(t+x/c).
$$ (eq:solutionbvproblem)

So, the pressure at a location $x$ gives a time-shifted version (by $x/c$) of the function $f(t)$ at the boundary $x=0$, which can physically be interpreted as a travelling wave. It behaves as a direct wave as discussed in [](./snells_law.md). It is a wave travelling in the *negative* $x-$direction: for a wave to maintain its shape as it moves (so time $t$ *increases*), the value $t+x/c$ must remain constant, and the distance $x$ must therefore *decrease*.

Here, we used a boundary value at $x=0$ to get to the travelling-wave solution. However, an initial value at $t=0$ can also be used to get a similar solution: see the [*EXERCISE* on solutions of the wave equation](#subsec-exerc-sol-waveq).

In the same way, for the second of equations {eq}`eq:waveqaconeway`, when at the boundary $x=0$ the pressure field is equal to some function $g(t)$, we have the boundary-value problem:

$$
\begin{aligned}
   \frac{\partial p}{\partial x}
	    & = - \frac{1}{c} \frac{\partial p}{\partial t},
\\
  p(x\!=\!0,t) & = g(t).
\end{aligned}
$$

This then has the following solution:

$$
p(x,t) = g(t-x/c),
$$

where it can be noticed that we have a negative shift in time, compared to the solution given earlier. As above, this solution behaves as a direct wave but now travelling in the *positive* $x-$direction.

(subsec-exerc-sol-waveq)=
## Exercise on solutions of the wave equation

In the above, a travelling-wave solution was obtained when the problem was formulated as a boundary-value problem (at $x=0$), see {eq}`eq:bvproblem` and {eq}`eq:solutionbvproblem`. However, such a solution can also be obtained when the problem is formulated as an initial-value problem (at $t=0$):

$$
\begin{aligned}
   \frac{\partial p}{\partial x}
	    &= \frac{1}{c} \frac{\partial p}{\partial t},
\\
  p(x,t\!=\!0) &= h(x).
\end{aligned}
$$

- What is the travelling-wave solution in this case?
- Show that this solution satisfies the initial-value problem.
