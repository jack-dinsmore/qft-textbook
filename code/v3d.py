import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma, factorial

def integral(s):
    val = 0
    dx = 0.0001
    for x in np.arange(0,1,dx):
        val += 1/np.sqrt(1 - s * x * (1-x) - 0.0001j)
    return val * dx

def v_func(s):
    return np.abs(1/(16 * np.pi) * integral(s))

plt.rcParams["text.usetex"]=True
plt.rcParams["text.usetex"]=True
fig, ax = plt.subplots(figsize=(6.5,4))
xs = np.linspace(0, 4, 500)
ys = v_func(xs)
ax.plot(xs, ys, color='k', linewidth=1)
# xs = np.linspace(4, 8, 100)
# ys = v_func(xs)
# ax.plot(xs, ys, color='k', linewidth=1, linestyle='dashed')
# ax.axvline(4, color='k', linewidth=0.5, linestyle='dotted')

# ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.set_xlim(0, xs[-1])
ax.set_ylim(0, 0.1)
ax.set_ylabel("$mV(s)/i$", size=12)
ax.set_xlabel("$s/m^2$", size=12)
fig.tight_layout()
fig.savefig("../figs/2-2-scalar-v-3d.png")
fig.savefig("../figs/2-2-scalar-v-3d.pdf")