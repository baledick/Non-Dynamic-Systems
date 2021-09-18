#%%
import numpy as np
import matplotlib.pyplot as plt

def xdot(x,y):
    return (x-y)/2

def rk4(x0,xn,n):

    h = (xn-x0)/n
    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2)))
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        x0 += h

leg=[]
po2=np.zeros(6)

for i in range(2,8):
    po2[i-2] = 2**(i-1)

for i in po2:
    leg = np.append(leg, 'RK4 using '+(str(int(i)))+' steps')

print(leg)
# %%
