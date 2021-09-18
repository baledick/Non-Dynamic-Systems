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

x0=np.array([0,0.1,1,1.9,2])


for i in x0:
    x[0]=i
    for j in np.arange(1,system.stepsnumber):
        t[j]=(j-1)*system.dt
        system.symlogistic(x[j-1])
        x[j]=x[j-1]+system.symlogdt
    plt.plot(system.steps, x, '-' )
plt.legend(x0)
plt.title('Μια συμμετρική μορφή της λογιστικής καμπήλης')
plt.savefig('symm.png')
plt.show()


