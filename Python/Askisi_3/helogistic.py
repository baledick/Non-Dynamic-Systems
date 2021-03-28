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

x0=np.linspace(0,2,50)
P=np.zeros(50)

plt.figure(1)
plt.title('Λογιστική Καμπύλη')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.ylim(0, 2)
for j in np.arange(len(x0)):
    x[0]=x0[j]

    for i in np.arange(1, system.stepsnumber):
        system.helogistic(x[i-1], 1/8, 1, t[i])
        x[i]=x[i-1]+system.helogdt
        if x[i] <=0:
            x[i]=0
    plt.plot(t, x, 'b')
        
    P[j]=x[i]
plt.savefig('Fig/helog.png')
plt.figure(2)
idx = np.argwhere(np.diff(np.sign(P - x0))).flatten()
plt.plot(x0[idx], P[idx], 'ro')
plt.plot(x0, P, 'b')
plt.plot(x0, x0, '--r')
plt.title('Απεικόνιση Poincare')
plt.xlabel('$x$')
plt.ylabel('$P(x)$')
plt.savefig('Fig/poinc.png')
plt.show()
