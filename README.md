# Approximate Methods-Practical
>Python scripts to demonstrate some basic ways of solving differential equations on a computer.


## Environment to run on:
The code will run on a Linux system. It is possible to run on other systems, but you will need to change the location of where the plots are saved as they save to a temporary location that is specific to Linux filesystems. 

Several python libraries are required. See python scripts for details.

## Running code:
e.g. type:

	python3 approximate_methods01.py
or
	
	python3 approximate_methods02.py
or

	python3 approximate_methods03.py
	
## How the methods work:
These python scripts were set-up to demonstrate how differential equations can be solved by approximate methods on a computer. One method we will talk about is the simple <i>forward Euler</i> method. The <i>forward Euler</i> method solves a differential equation approximating the gradient by a forward difference to find a <i>finite difference equation</i>. We then rearrange to find the solution in steps. For example, consider the differential equation describing radioactive decay:

\begin{equation}
\frac{dN}{dt}=-\lambda N
\end{equation}
where $\lambda$ is a constant.

We can approximate the derivative with a forward difference over a finite time-step, $\Delta t$:

\begin{equation}
\frac{N_{n+1}-N_{n}}{\Delta t}=-\lambda N_{n}
\end{equation}
where subscript $n$ means at the current time-level and $n+1$ is at the <i>next</i> time level.

If we know the value of $N$ at time level $n$, we can then rearrange to find the value of $N$ at time level $n+1$:

\begin{equation}
N_{n+1}=N_n - \Delta t \times \lambda N_n
\end{equation}
then you can find the next level again by calling $n+1$, $n$ and repeating as many times as necessary. This is the basis of how approximate methods work. 

