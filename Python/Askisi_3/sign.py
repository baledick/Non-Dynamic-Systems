import numpy as np
import matplotlib.pyplot as plt
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from funcs import NonLinear

system = NonLinear(0.5,0.1)

x=np.zeros(system.stepsnumber)
t=np.linspace(0,0,system.stepsnumber)

x[0]=0

for i in np.arange(system.stepsnumber):
    t[i]=(i-1)*system.dt
    system.sign(x[i-1])
    x[i]=x[i-1]+system.signdt
    
print(t[0:3])
plt.plot(t, x, 'b')
plt.plot(t, t, 'r')
plt.title('$\dot{x}=\pm 1$')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.savefig('sign.png')
plt.show()
