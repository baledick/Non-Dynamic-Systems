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
h=np.linspace(0, 1/2, 10)

x0=np.linspace(0,2,1000)
P=np.zeros(1000)

ex=[]
ep=[]
for k in np.arange(len(h)):

    for j in np.arange(len(x0)):
        x[0]=x0[j]

        for i in np.arange(1, system.stepsnumber):
            system.helogistic(x[i-1], h[k], 1, t[i])
            x[i]=x[i-1]+system.helogdt
            if x[i] <=0:
                x[i]=0
            
        P[j]=x[i]

    idx = np.argwhere(np.diff(np.sign(P - x0))).flatten()
    plt.plot(x0[idx], P[idx], 'ro')
    np.append(x0[idx], ex)
    #plt.plot(x0, P, 'b')
print(ex)
#plt.plot(x0, x0, '--r')
#plt.title('Απεικόνιση Poincare για μεταβλητό $h$')
#plt.xlabel('$x$')
#plt.ylabel('$P(x)$')
plt.savefig('Fig/poinc_pp.png')
plt.show()
