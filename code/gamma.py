import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma, factorial
from mpl_toolkits.axisartist.axislines import AxesZero

plt.rcParams["text.usetex"]=True
plt.rcParams["text.usetex"]=True
fig, ax = plt.subplots(figsize=(6,4))
xs = np.linspace(-3.5, 4.5, 1000)
ys = gamma(xs)
for integer in range(int(np.floor(xs[0])), 0):
    mask = (integer < xs) & (xs < integer + 1)
    ax.plot(xs[mask], gamma(xs[mask]), color='k', linewidth=1)
    ax.axvline(integer+1, ymin=0.5, linestyle='dashed', linewidth=0.5, color='grey')
    ax.axvline(integer+1, ymax=0.43, linestyle='dashed', linewidth=0.5, color='grey')
mask = (xs > 0)
ax.plot(xs[mask], gamma(xs[mask]), color='k', linewidth=1)

fact_xs = []
fact_ys = []
for n in range(int(xs[-1])):
    fact_xs.append(n+1)
    fact_ys.append(factorial(n))
ax.scatter(fact_xs, fact_ys, facecolor="none", edgecolor="k", marker="o")

ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.set_ylim(-10,10)
ax.set_xlim(xs[0], xs[-1])
ax.set_ylabel("$\Gamma(x)$", size=12)
ax.set_xlabel("$x$", loc="right", size=12)
fig.tight_layout()
fig.savefig("../figs/gamma.png")
fig.savefig("../figs/gamma.pdf")