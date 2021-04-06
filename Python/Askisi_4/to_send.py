import numpy as np
import matplotlib.pyplot as plt

def gompertz_t(x, h, t):
    return (-(x*np.log(x))-h*(1+np.sin(t)))

Nt=10 #to exw mikro gia na to kanei pio grigora to laptop
Nb=1000
x=np.zeros(Nt)
t=np.linspace(0,2*np.pi,Nt)
dt=(t[1]-t[0])

h=np.linspace(0, 1/4, Nb)
x0=np.linspace(0.01,1.2,Nb)
P=np.zeros(Nb)

x1=[]
x2=[]
fm=[]
fp=[]

for i in np.arange(len(x0)):
    if x0[i] < 0.5:
        x1 = np.append(x1, x0[i])
    else:
        x2 = np.append(x2, x0[i])

for k in np.arange(Nb):
    for j in np.arange(Nb):
        x[0]=x0[j]
        for i in np.arange(1, Nt):
            x[i]=x[i-1]+dt*gompertz_t(x[i-1], h[k], t[i])

            if x[i]<=0:
                x[i]=0.000000000000001

        P[k]=x[i]


    idx1 = (np.abs(P[0:len(x1)] - x1)).argmin()
    fm=np.append(fm, x1[idx1])
    idx2 = (np.abs(P[len(x1):] - x2)).argmin()
    fp=np.append(fp, x2[idx2])

#hp=(1+np.sqrt(1-(4*h)))/2  #to thewritiko (lathos)
#hm=(1-np.sqrt(1-4*h))/2    #to idio lathos


plt.plot(h, fm, '--r')
plt.plot(h, fp, 'b')
#plt.plot(h, hp, '--k') #plotarei to lαthos
#plt.plot(h, hm, '--k') #same
plt.title('Διάγραμα Διακλάδωσης για τη χρονοεξαρτώμενη μορφή.')
plt.xlabel('$h$')
plt.ylabel('$X_e(h)$')

plt.show()
