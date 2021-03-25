import numpy as np
import matplotlib.pyplot as plt
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from funcs import NonLinear

system = NonLinear(6,0.1)

x=np.zeros(system.stepsnumber)
t=np.zeros(system.stepsnumber)

x0=np.array([0,0.1,1,1.9])


for i in x0:
    x[0]=i
    for j in np.arange(1,system.stepsnumber):
        t[j]=(j-1)*system.dt
        system.logistic(x[j-1])
        x[j]=x[j-1]+system.logdt
        plt.plot(t[0:j], x[0:j])
plt.legend(x0)
plt.title('Η λογιστική καμπήλη')
plt.savefig('logistic.png')
plt.show()


