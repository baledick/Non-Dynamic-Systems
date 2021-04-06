import numpy as np
import matplotlib.pyplot as plt

def xdot(x,t):
    return(x*x-1-np.cos(t))
    
Nt=1000
Nb=100
x=np.zeros(Nt)
t=np.linspace(0,2*np.pi,Nt)
dt=(t[1]-t[0])
x0=np.linspace(-1,1.3,Nb)

for j in np.arange(len(x0)):
    x[0]=x0[j]
    for i in np.arange(1, Nt):
        x[i]=x[i-1]+dt*xdot(x[i-1], t[i-1])
    plt.plot(t,x)
plt.ylim(-2,5)

plt.title('Γράφημα της χρονικής εξέλιξης του $x(t)$')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.savefig('Fig/xdot.png')

plt.show()
