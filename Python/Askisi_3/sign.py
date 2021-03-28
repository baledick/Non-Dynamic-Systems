import numpy as np
import matplotlib.pyplot as plt
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from funcs import NonLinear

system = NonLinear(50,0.1)

x=np.zeros(system.stepsnumber)
t=np.zeros(system.stepsnumber)

x[0]=0

for i in np.arange(system.stepsnumber):
    t[i]=(i-1)*system.dt
    system.sign(x[i-1])
    x[i]=x[i-1]+system.signdt
    
plt.plot(t, x, 'b')
plt.plot(t, t, 'r')
plt.plot(t, np.zeros(system.stepsnumber), 'k')
plt.title('Άσκηση 8')
plt.xlabel('$t$')
plt.xlim(0,0.5)
plt.ylim(0,1)
plt.ylabel('$x(t)$')
plt.savefig('Fig/sign.png')
plt.show()
