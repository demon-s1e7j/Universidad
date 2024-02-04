# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:35:28 2023

@author: Juan
"""

import numpy as np
#import sympy as sym
import matplotlib.pyplot as plt

def E(i,k,r,w,t,theta,E0=1,N=5):
    return E0*np.cos(k*np.sin((i-1)*(theta/(N-1)))*r-w*t)
lmbd=400
f=3*10**17/lmbd
k=2*np.pi/lmbd
w=2*np.pi*f
theta=30*np.pi/180
y=np.linspace(-5e3,5e3,500)
t=np.linspace(0,1/f,500)

Et=np.zeros(len(y))

indx= np.linspace(1,5,5)
#print(indx)
#"""
for i in range(len(y)):
    for j in range(len(t)):
        for o in range(len(indx)):
            Et[i] += E(indx[o],k,y[i],w,t[j],theta)
    Et[i] *= 1/len(t)
plt.figure(1)
plt.plot(y,Et)
plt.grid()
plt.figure(2)
plt.plot(y,Et**2)   
plt.grid()     
#"""
