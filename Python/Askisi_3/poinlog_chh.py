import numpy as np
import matplotlib.pyplot as plt
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from funcs import NonLinear

system = NonLinear(2,0.1)

x=np.zeros(system.stepsnumber)
t=np.linspace(0,2*np.pi,system.stepsnumber)
h=np.linspace(1/16, 1/4, 5)

x0=np.linspace(0,2,50)
P=np.zeros(50)
PP=np.zeros(50)

for k in np.arange(len(h)):
    
    for l in np.arange(len(x0)):
        for j in np.arange(len(x0)):
            x[0]=x0[j]
    
            for i in np.arange(1, system.stepsnumber):
                system.helogistic(x[i-1], h[k], 1, t[i])
                x[i]=x[i-1]+system.helogdt
                if x[i] <=0:
                    x[i]=0
                
            P[j]=x[i]
        plt.plot(x0, P, 'b')
        PP[l]=P[j]
    idx = np.argwhere(np.diff(np.sign(PP - x0))).flatten()
    print(P[idx], P[idx])
    plt.plot(P[idx], PP[idx], 'ro')
    plt.plot(x0, PP, 'g')

plt.plot(x0, x0, '--r')
#plt.title('Απεικόνιση Poincare της Απεικόνισης Poincare')
plt.xlabel('$x$')
plt.ylabel('$P(P(x))$')
plt.savefig('Fig/ppoinch.png')
plt.show()
