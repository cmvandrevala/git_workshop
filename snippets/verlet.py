# -*- coding: utf-8 -*-
"""
Use Verlet integration for solving
    F = m*a

Created on Fri Oct 24 18:26:57 2014

@author: nicoguaro
"""

#!/usr/bin/python
## Verlet Integration Algorithm
from numpy import *
from scipy import linalg as LA
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def LJ_force(e,r_min,r):
    """
        Force for a particle in a Lennard-Jones potential.

        The potential is given by
        V = e*(r_min**12/r**12-2.*(r_min**6)/r**6)  ,

        so, the experimented force is
        F =  -12.*e*( r_min**6/r**7-r_min**12/r**13)   .

        e is the deep length of the potential (double float)
        r_min is the equilibrium position (double float)
        r is the position (double float)
    """
    F =  -12.*e*( r_min**6/r**7-r_min**12/r**13)
    return F

def spring_force(k,x):
    """
        For for a particle attached to a string of constant k.

        The potential is given by
        V = 1./2.k*x**2   ,

        so, the experimented force is
        F =  -k*x   .

        k is the elastic constant (double float)
        x is the elongation of the spring (double float)
    """
    F =  -k*x
    return F

def cuartic_sp_force(k,x):
    """
        For for a particle attached to a string of constant k.

        The potential is given by
        V = 1./4.k*x**4   ,

        so, the experimented force is
        F =  -k*x**3   .

        k is the elastic constant (double float)
        x is the elongation of the spring (double float)
    """
    F =  -k*x**3
    return F

def simple_pendulum(g,theta):
    """
        For a particle attached to a massless bar with in a constant
        gravity field g.

        The potential is given by
        V = g*cos(theta)   ,

        so, the experimented force is
        F = -g*sin(theta)   .

        g is the gravity constant divided by the particle mass (double float)
        theta is the angle respect the vertical line (double float)
    """
    F =  -g*sin(theta)
    return F


r_min = 1.
epsilon = 0.1
k = 1.
v0 = 0.0
x0 = 1.58
Dt = 0.001
m = 1.
L = 1000.
g = 9.78
time = 1000.
nsteps = int(time/Dt)

print "Time step: ", Dt
print "Number of time steps: ", nsteps
print "Initial position: ", x0
print "Initial speed: ", v0

time = zeros( (nsteps+1) )
x = zeros( (nsteps+1) )
v = zeros( (nsteps+1) )
time[0] = 0.
x[0] = x0
v[0] = v0
time[1] = Dt
x[1] = x[0] + v0*Dt +1./2.*Dt**2*simple_pendulum(g,x0)/L
for i in range(1,nsteps):
    a = simple_pendulum(g,x[i])/L
    time[i+1] = time[i] + Dt
    x[i+1] = 2*x[i]-x[i-1]+a*Dt**2
    v[i] = (x[i+1] - x[i-1])/2./Dt
v[nsteps] = (x[nsteps] - x[nsteps-1])/Dt

plt.plot(time,x)
plt.xlabel("Time")
plt.ylabel("Position")
plt.show()
    
