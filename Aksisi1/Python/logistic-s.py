import numpy as np
import matplotlib.pyplot as plt

def xdot(c):
    val = c*(1-c)*(2-c)
    return val

dt=0.01
step=np.arange(0,6,dt)
stepnum=len(step)

x=np.zeros(stepnum)
t=np.zeros(stepnum)

x0=np.array([0,0.1,1,1.9,2])
for i in np.arange(len(x0)):
    x[0]=x0[i]
    for j in np.arange(1,stepnum):
        t[j]=(j-1)*dt
        x[j]=x[j-1]+dt*xdot(x[j-1])
    plt.plot(step, x, '-' )
plt.legend(x0)
plt.title('Η συμμετρική μορφή της λογιστικής καμπήλης')
plt.savefig('symm.png')
plt.show()

