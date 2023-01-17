# %% [markdown]
# # Definicja równania
#
# $\frac{d^2u}{dx^2}=4\pi Gρ(x)$
# $u(0)=-5$
# $u(3)=-4$
# $I=[0,3]$
#
# $ρ(x)=\begin{cases}
# 0 & \text{dla}\ x \in [0, 1] \\
# 10^{11} & \text{dla}\ x \in (1, 2] \\
# 0 & \text{dla}\ x \in (2, 3] \\
# \end{cases}$

# %% [markdown]
# ## Sformułowanie słabe
#
# $\int_0^3u''vdx = \int_0^34\pi Gρ(x)vdx$
# $u'v|_0^3 - \int_0^3u'v'dx = \int_0^34\pi Gρ(x)vdx$
#
# $u'(3)v(3) - u'(0)v(0) - \int_0^3u'v'dx = \int_0^34\pi Gρ(x)vdx$
# $u'(3)v(3) - u'(0)v(0)-\int_0^3u'v'dx = 4\pi G(\int_0^1ρ(x)vdx + \int_1^2ρ(x)vdx + \int_2^3ρ(x)vdx)$
# $u'(3)v(3) - u'(0)v(0)-\int_0^3u'v'dx = 4\pi G(\int_0^10vdx + \int_1^2 10^{11} vdx + \int_2^30vdx)$
# $u'(3)v(3) - u'(0)v(0)-\int_0^3u'v'dx = 4*10^{11}*\pi G \int_1^2 vdx$
# $B(u, v) = L(v)$
#
# $B(u, v) = u'(3)v(3) - u'(0)v(0) - \int_0^3u'v'dx$
# $L(v) = 4*10^{11}*\pi G \int_1^2 vdx = k\int_1^2vdx$
#
# $\stackrel{\sim}{u} = -5e_0 -4e_n $
# ${B}(w, v) = L(v) - B(\frac{x}{3}-5)$
#
# ${B}(w, v) = -\int_0^3u'v'dx$
# $\stackrel{\sim}{L}(v) = k\int_1^2vdx - 5B(e_0, v) - 4(e_n, v)$

# %% [markdown]
# ### Parametry obliczeń

# %%
import matplotlib.pyplot as plt
import numpy as np
N = 100  # liczba elementów
left, right = 0.0, 3.0  # zakres
m = 1000  # liczba punktów użyta podczas wyliczania całek

# %% [markdown]
# ### Kod początkowy

# %%

k = 4 * np.pi * 6.67259
n = N  # liczba elementów podprzestrzeni, po uwzględnieniu warunków brzegowych
w = (right - left) / (n+1)  # szerokość elementu

# %% [markdown]
# ## Elementy skończone
#
# $e_i=\begin{cases}
#     x-(p_i-p_{i-1})*\frac{1}{p_i-p_{i-1}} & \text{dla}\ x < p_i \\
#     x-p_i*\frac{-1}{p_i-p_{i-1}} & \text{dla}\ x >= p_i \\
# \end{cases}$
#

# %%


def e(center, w, first=False, last=False):
    a = 1/w
    def f(x): return (x - (center - w)) * \
        a if x < center else (x - center) * (-a) + 1

    if first:
        return (lambda x: 0.0 if x < center or x > center + w else f(x))
    elif last:
        return (lambda x: 0.0 if x < center - w or x > center else f(x))
    else:
        return (lambda x: 0.0 if x < center - w or x > center + w else f(x))


# %% [markdown]
# ## Pochodne elementów skończonych
#
# $e'_i=\begin{cases}
#     \frac{1}{p_i-p_{i-1}} & \text{dla}\ x < p_i \\
#     \frac{-1}{p_i-p_{i-1}} & \text{dla}\ x >= p_i \\
# \end{cases}$

# %%
def de(center, w, first=False, last=False):
    a = 1/w
    def f(x): return a if x < center else -a

    if first:
        return (lambda x: 0.0 if x < center or x > center+w else f(x))
    elif last:
        return (lambda x: 0.0 if x < center-w or x > center else f(x))
    else:
        return (lambda x: 0.0 if x < center-w or x > center+w else f(x))

# %% [markdown]
# ### B(u, v)

# %%


def b(up, vp, m, left=0, right=3):
    xs = np.linspace(left, right, m)
    ys = np.array([up(x)*vp(x) for x in xs]).reshape(1, -1)[0]

    b = np.trapz(ys, x=xs)
    return -b

# %% [markdown]
# ### g(x)
#
# $\frac{d^2u}{dx^2}=4\pi Gρ(x)$
# $u(0)=-5$
# $u(3)=-4$
# $I=[0,3]$
#
# $ρ(x)=\begin{cases}
# 4\pi Gρ(x)*10^{11} & \text{dla}\ x \in (1, 2] \\
# 0 & \text{dla}\ x \notin  (1, 2] \\
# \end{cases}$

# %%


def g(x):
    if x > 1 and x <= 2:
        return k
    else:
        return 0

# %% [markdown]
# ## Matrix of $b_{i,j} = B(e_i, e_j)$


# %%
xs = np.linspace(0, 3, N + 2)
dV = np.array([de(xs[i], w, i == 0, i == n-1) for i in range(0, N+2)])
V = np.array([e(xs[i], w, i == 0, i == n-1) for i in range(0, N+2)])

for i in range(n+2):
    plt.plot(xs, [V[i](x) for x in xs])
    plt.scatter(xs, [dV[i](x) for x in xs])
plt.show()

B = [[b(dV[i], dV[j], m) for i in range(1, n+1)] for j in range(1, n+1)]

# %% [markdown]
# ## Vector of $l_i = L(e_i) + 5B(e_0, e_i) + 4B(e_n, e_i)$
#
# $\stackrel{\sim}{L}(v) = k\int_1^2vdx +5B(e_0, v) + 4B(e_n, v)$

# %%


def l(v, m):
    xs = np.linspace(1, 2, m)
    ys = np.array([v(x)*k for x in xs]).reshape(1, -1)[0]
    i = np.trapz(ys, x=xs)
    plt.plot(xs, ys)
    return i


# %%
L = np.array([l(V[i], m) + 5*b(dV[0], dV[i], m) + 4 *
             b(dV[n+1], dV[i], m) for i in range(1, n+1)])
plt.show()

# %% [markdown]
# ### Kalkulacja wektora $u_i$

# %%
Bm = np.matrix(B)
Bmi = Bm.getI()
Lm = np.matrix([L]).getT()
U = np.array(Bm * Lm).reshape(1, -1)[0]

print(Bm)
print(Bmi)
print(Lm)
print(U)

# %% [markdown]
# ## Prezentacja funkcji $u(x)$

# %%


def u(x): return sum([U[i] * V[i](x)
                      for i in range(n)]) - 5 * V[0](x) - 4 * V[n+1](x)


xs = np.linspace(0, 3, 100)
ys = np.array([u(x) for x in xs]).reshape(1, -1)[0]

# plt.scatter
plt.plot(xs, ys)
ys = plt.gca()
ys.set_ylim([-100, 100])
plt.savefig('plot_n' + str(N) + '.png')
plt.show()
