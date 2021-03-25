import numpy as np
import matplotlib.pyplot as plt

t=np.zeros(200)
x=np.zeros(200)
dt=[-0.1,0.1]

x[0]=0
for j in np.arange(len(dt)):
    for i in np.arange(1, len(t)):
        t[i]=(i-1)*dt[j]
        x[i]=x[i-1]-np.abs(dt[j])      
    plt.plot(t,x,'b')
    plt.plot(t,t,'--r')
plt.plot(0,0,'ko')
plt.savefig('simple.png')
plt.show()
