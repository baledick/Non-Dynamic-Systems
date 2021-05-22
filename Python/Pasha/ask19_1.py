import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
#%%
steps = 100
x_range = np.linspace(-2, 4, steps)
t_range = np.linspace(0,3,steps)
psi_range = 1/(1+x_range**2)

for i in range(steps):
    f=psi_range[i]
    x=f*t_range+x_range[i]
    plt.plot(x,t_range,'b')


plt.savefig('ask1.png')
plt.show()
# %%