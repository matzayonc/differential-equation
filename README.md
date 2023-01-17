# Definicja równania

$\frac{d^2u}{dx^2}=4\pi Gρ(x)$  
$u(0)=-5$  
$u(3)=-4$  
$I=[0,3]$

$ρ(x)=\begin{cases}
0 & \text{dla}\ x \in [0, 1] \\
10^{11} & \text{dla}\ x \in (1, 2] \\
0 & \text{dla}\ x \in (2, 3] \\
\end{cases}$

## Sformułowanie słabe

$\int_0^3u''vdx = \int_0^34\pi Gρ(x)vdx$  
$u'v|_0^3 - \int_0^3u'v'dx = \int_0^34\pi Gρ(x)vdx$  

$u'(3)v(3) - u'(0)v(0) - \int_0^3u'v'dx = \int_0^34\pi Gρ(x)vdx$  
$-\int_0^3u'v'dx = \int_0^34\pi Gρ(x)vdx$  
$-\int_0^3u'v'dx = 4\pi G(\int_0^1ρ(x)vdx + \int_1^2ρ(x)vdx + \int_2^3ρ(x)vdx)$
$-\int_0^3u'v'dx = 4\pi G(\int_0^10vdx + \int_1^2 10^{11} vdx + \int_2^30vdx)$
$-\int_0^3u'v'dx = 4*10^{11}*\pi G \int_1^2 vdx$

$B(u, v) = -\int_0^3u'v'dx$  
$L(v) = 4*10^{11}*\pi G \int_1^2 vdx$

## Definicja przestrzeni

$u=w +\stackrel{\sim}{u}$

$V_h =〈e_1, e_2, ..., e_{n-1}〉$  
$e_n = \stackrel{\sim}{u}$

$B(w,v)=L(v)-B(\stackrel{\sim}{u},v)$  
$B(w,v)=\stackrel{\sim}{L}(v)$

## Forma dla $N=3$

$\begin{bmatrix}
B(e_1, e_1) & B(e_2, e_1)\\
B(e_1, e_2) & B(e_2, e_2)
\end{bmatrix}
\begin{bmatrix}
u_1 \\
u_2
\end{bmatrix} =
\begin{bmatrix}
L(e_1) - B(e_3,e_1) \\
L(e_2)  - B(e_3, e_2)
\end{bmatrix}
$