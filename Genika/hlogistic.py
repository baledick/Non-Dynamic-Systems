import numpy as np
import matplotlib.pyplot as plt
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from funcs import NonLinear

system = NonLinear(6,0.1)

h=np.append(np.linspace(0,1/4,int(system.stepsnumber/2)),np.linspace(1/4+1.e-05,1/3,int(system.stepsnumber/2)))

x=np.zeros(system.stepsnumber)
t=np.zeros(system.stepsnumber)

x[0]=0.3

for k in np.arange(len(h)):
    for j in np.arange(system.stepsnumber):
        t[j]=(j-1)*system.dt
        system.hlogistic(x[j-1],h[k])
        x[j]=x[j-1]+system.hlogdt
        if x[j]<0:
            x[j]=0
    
    xt = x[system.stepsnumber-1]
    
    if h[k]>1/4:
        #plt.plot(h[1:k],xt[1:k],'r')
        plt.plot(h[1:31],(1+np.sqrt(1-4*h[1:31]))/2,'--b','Linewidth',2)
        #plt.plot(h[31:k],0*h[31:k],'--b','Linewidth',2)
        plt.xlabel('t','Fontsize',24)
        plt.ylabel('x(t)','Fontsize',24)
    
    #plt.plot(h, x, '-' )
    
#plt.title('Η λογιστική καμπήλη με μεταβολή του $h$')
#plt.savefig('hlogistic.png')
plt.show()
