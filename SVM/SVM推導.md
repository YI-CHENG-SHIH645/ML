### Lagrange Multiplier

$$
\text{critical points of } \\ f(x,y) \\
\text{under constraint } \\ g(x,y)=b \\
$$

$$
\nabla f = -\lambda\nabla g\\
$$

## Lagrange Function

$$
L(x,y,\lambda) = f(x,y) + \lambda(g(x,y)-b) \\
\nabla L = \begin{bmatrix}
              \frac{\partial L}{\partial x} \\
              \frac{\partial L}{\partial y} \\
              \frac{\partial L}{\partial \lambda}
            \end{bmatrix}
         = \begin{bmatrix}
              \frac{\partial f}{\partial x} + \lambda\frac{\partial g}{\partial x} \\
              \frac{\partial f}{\partial y} + \lambda\frac{\partial g}{\partial y} \\
              g(x,y) - b
            \end{bmatrix}
         = 0
$$

## The problem we wanna solve :

$$
z = \phi(x), x \in R^m, z \in R^k \\
min(\frac{1}{2}w^Tw + C\sum_{i=1}^n s_i)\\
\text{subject to} \\
y_i(w^Tz_i - b) \geq 1 - s_i,  \forall i \\
\text{ where $s_i$ is a slack variable}, s_i \geq 0
$$



## The constraint is inequation ?

$$
\text{critical points of } \\ f(x,y) \\
\text{under constraint } \\ g(x,y) \leq k \\ h(x,y) = b
$$

## KKT Theorem tells us that ......

$$
L(x,y,\lambda,\mu) = f(x,y) + \lambda(h(x,y)-b) + \mu(g(x,y)-k) \\
\text{where $\lambda$ is lagrange multiplier} \\
\text{$\mu$ is KKT multiplier} \\
$$

$$
\text{to minimize f} \\
\text{solve } \nabla L = 0 \text{ (except KKT multipliers)} \\
\text{then maximize over KKT multipliers}  \\
\text{under constraints} \\
------------------------\\
g(x,y) \leq k \\
------------------------\\
\mu \geq 0 \\
------------------------\\
\mu(g(x,y) - k) = 0 \\
------------------------\\
$$



## Apply to our problem

$$
max_{\mu}(min_{w,b,s_i}(L)) \\
\text{under constraints} \\
------------------------\\
-(y_i(w^Tz_i - b) - 1 + s_i) \leq 0, \forall i \\
-s_i \leq 0, \forall i \\
------------------------\\
\mu \geq 0 \\
------------------------\\
\mu (y_i(w^Tz_i - b) - 1 + s_i) = 0, \forall i \\
\mu s_i = 0, \forall i \\
------------------------\\
$$


$$
f = \frac{1}{2}w^Tw + C\sum_{i=1}^n s_i \\
\text{to min $f$} \\
L(w,b,s_i,\mu^1,\mu^2) = \frac{1}{2}w^Tw + C\sum_{i=1}^n s_i - \sum_{i=1}^n\mu_i^1(y_i(w^Tz_i - b) - 1 + s_i) - \sum_{i=1}^n\mu_i^2 s_i
$$

$$
\nabla L_{w,b,s_i} = \begin{bmatrix}
                        \frac{\partial L}{\partial w} \\
                        \frac{\partial L}{\partial b} \\
                        \frac{\partial L}{\partial s_i}
                      \end{bmatrix}
                   = \begin{bmatrix}
                        w - \sum_{i=1}^n \mu^1_i y_i z_i \\
                        \sum_{i=1}^n \mu^1_i y_i \\
                        C - \mu^1_i - \mu^2_i
                      \end{bmatrix}
                   = 0
$$

$$
w = \sum_{i=1}^n \mu^1_i y_i z_i \\
C = \mu^1_i + \mu^2_i \\
\text{plug ($w$, $C$) into L}
$$

$$
L = \frac{1}{2}\sum_{i=1}^n \mu^1_i y_i z_i^T \sum_{i=1}^n \mu^1_i y_i z_i \\
	 	+ \sum_{i=1}^n(\mu^1_i + \mu^2_i)s_i + \sum_{i=1}^n(- \mu^1_i - \mu^2_i)s_i \\
	 	- \sum_{i=1}^n \mu^1_i y_i z_i^T \sum_{i=1}^n \mu^1_i y_i z_i \\
    + b\sum_{i=1}^n \mu_i^1 y_i + \sum_{i=1}^n \mu_i^1 \\
\Rightarrow
L = -\frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \mu^1_i \mu^1_j y_i y_j z_i^T z_j + \sum_{i=1}^n \mu_i^1 \\
$$

$$
max_{\mu_i^1} L = max_{\mu_i^1} (-\frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \mu^1_i \mu^1_j y_i y_j z_i^T z_j + \sum_{i=1}^n \mu_i^1) \\
\text{subject to } \sum_{i=1}^n \mu_i^1 y_i = 0, \mu_i^1 \geq 0
$$

## Quadratic Programming

$$
------------------------\\
min_{\mu} (\frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \mu^1_i \mu^1_j y_i y_j z_i^T z_j - \sum_{i=1}^n \mu_i^1) \\
\Rightarrow min_{\mu} (\frac{1}{2} \mu^TP\mu + q^T\mu) \\
\text{where } P = \begin{bmatrix}
                    y_1 y_1 ... y_1y_n \\.\\.\\ y_n y_1 ... y_n y_n
                  \end{bmatrix}_{n*n} * 
                  \begin{bmatrix}
                    z_1 z_1 ... z_1 z_n \\.\\.\\ z_n z_1 ... z_n z_n
                  \end{bmatrix}_{n*n} \\ 
              q = \begin{bmatrix}
                    -1 \\.\\.\\ -1
                  \end{bmatrix}_{n*1}
$$

$$
------------------------\\
\text{subject to} \\
A^T\mu = b \\
\text{where } A = \begin{bmatrix}
                    y_1 \\.\\.\\ y_n
                  \end{bmatrix}
              b = \begin{bmatrix}
                    0 \\.\\.\\ 0
                  \end{bmatrix}_{n*1}
$$

$$
------------------------\\
\mu \geq 0 \\
G\mu \leq h \\
\text{where } G = diag_{n}(-1), h = b \\
------------------------\\
$$

$$
\text{so we get the $\hat \mu$} \\
\hat w = \sum_{i \in sv} \hat {\mu_i} y_i z_i \\
\hat b = y_j - \hat w^Tz_j, {j \in sv}
$$

## But wait, where is our $z$ ? Or more specifically... $\phi$ ?

### Mercer's Theorem

$$
K(x_i, x_j) = \phi(x_i)^T\phi(x_i) \\
\text{where K is a Kernel funciton(similarity function)} \\
\text{s.t. $K(x_i, x_j)$ is symmetric & P.S.D.}
$$

$$
min_{\mu} (\frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \mu^1_i \mu^1_j y_i y_j K(x_i,x_j) - \sum_{i=1}^n \mu_i^1) \\
\Rightarrow min_{\mu} (\frac{1}{2} \mu^TP\mu + q^T\mu) \\
\text{where } P = \begin{bmatrix}
                    y_1 y_1 ... y_1y_n \\.\\.\\ y_n y_1 ... y_n y_n
                  \end{bmatrix}_{n*n} * K_{n*n}
$$

