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
h=np.linspace(0, 1/4, 1000)

x0=np.linspace(0.01,1.2,len(h))
x1=[]
x2=[]
fm=[]
fp=[]
for i in np.arange(len(x0)):
    if x0[i] < 0.5:
        x1 = np.append(x1, x0[i])
    else:
        x2 = np.append(x2, x0[i])

P=np.zeros(len(h))

for k in np.arange(len(h)):
    for j in np.arange(len(x0)):
        x[0]=x0[j]
        for i in np.arange(1, system.stepsnumber):
            system.htgompertz(x[i-1], h[k], t[i])
            x[i]=x[i-1]+system.hgompt
            
            if x[i]<=0:
                x[i]=0.000000000000001
                
        P[k]=x[i]


    idx1 = (np.abs(P[0:len(x1)] - x1)).argmin()
    fm=np.append(fm, x1[idx1])
    idx2 = (np.abs(P[len(x1):] - x2)).argmin()
    fp=np.append(fp, x2[idx2])
    
hp=(1+np.sqrt(1-(4*h)))/2
hm=(1-np.sqrt(1-(4*h)))/2



plt.plot(h, fm, '--r')
plt.plot(h, fp, 'b')
#plt.plot(h, hp, '--k')
#plt.plot(h, hm, '--k')
plt.title('Διάγραμα Διακλάδωσης για τη χρονοεξαρτώμενη μορφή.')
plt.xlabel('$h$')
plt.ylabel('$X_e(h)$')
plt.savefig('Fig/hgompt.png')

plt.show()
