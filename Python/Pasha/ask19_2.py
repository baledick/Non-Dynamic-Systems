import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
#%%
steps=500
t_val=np.array([0,1/2,1,2,3])
x_range = np.linspace(-5, 5, steps)
psi_range = np.zeros(steps)
tb=1

for i in np.arange(len(t_val)):
    t_val[i]=t_val[i]*tb
    for j in np.arange(steps):
        x=x_range[j]
        f = lambda psi : psi + psi*(x-psi*t_val[i])**2 - 1
        psi_range[j] = fsolve(f, 0)
    plt.plot(x_range, psi_range+0.3*i, 'k')
plt.savefig('ask2_2.png')
plt.show()
# %%
