import numpy as np
import matplotlib.pyplot as plt

class NonLinear:

    def __init__(self, numbersteps, stepsize):
        self.dt=stepsize
        self.steps=np.arange(0,numbersteps,self.dt)
        self.stepsnumber=int(len(self.steps))
        
    def logistic(self, c):
        val = c*(1-c)
        self.logdt = val*self.dt
        return self
     
    def symlogistic(self,c):
        val = c*(1-c)*(2-c)
        self.symlogdt = val*self.dt
        return self
        
    def hlogistic(self, c, h):
        val = c*(1-c)-h
        self.hlogdt = val*self.dt
        return self
    
    def helogistic(self, c, h, e, t):
        val = c*(1-c)-h*(1+e*np.sin(t))
        self.helogdt = val*self.dt
        return self
        
    def sign(self, c):
        if c>0:
            val=-1
        elif c<=0:
            val=1
        self.signdt = val*self.dt
        return self
        
    def hgompertz(self, c, h):
        val = -(c*np.log(c))-h
        self.hgomp=val*self.dt
        return self
        
    def htgompertz(self, c, h, t):
        val = -(c*np.log(c))-h*(1+np.sin(t))
        self.hgompt=val*self.dt
        return self
        
    def xsq(self, c, t):
        val = x*2-1-np.cos(t)
        self.xqrd = val*self.dt
        return self
            
        

