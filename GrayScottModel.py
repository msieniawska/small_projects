#!/usr/bin/env python

import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib

# Gray-Scott Model of a Reaction-Diffusion System
dt = 1.
T = 20000.
anim = 100 
L = 2.
N = 100
dx = dy = 0.02
Du = 2.e-5
Dv = 1.e-5
F = 0.037
k = 0.06


u = np.ones((N,N))
v = np.zeros((N,N))
for i in xrange(N/4,3*N/4):
 for j in xrange(N/4,3*N/4):
  random.seed()
  u[i][j] = random.random()*0.2+0.4
  v[i][j] = random.random()*0.2+0.2

t = 0.
nanim = 0
while (t < T):
 
 du_dt = (np.roll(u,1,axis=0) - 2.*u + np.roll(u,-1,axis=0)) * Du/dx**2
 du_dt += (np.roll(u,1,axis=1) - 2.*u + np.roll(u,-1,axis=1)) * Du/dx**2
 du_dt += -u*v*v + F*(1.-u)
 
 dv_dt = (np.roll(v,1,axis=0) - 2.*v + np.roll(v,-1,axis=0)) * Dv/dx**2
 dv_dt += (np.roll(v,1,axis=1) - 2.*v + np.roll(v,-1,axis=1)) * Dv/dx**2
 dv_dt += u*v*v - (F+k)*v

 u += du_dt*dt
 v += dv_dt*dt

 if not t % anim:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  cax = ax.imshow(u, interpolation='nearest')
  cax.set_clim(vmin=0, vmax=1)
  cbar = fig.colorbar(cax, ticks=[0.,0.3,0.5,1.],orientation='vertical')
  fig.savefig(str(nanim) + '.png')
  nanim += 1
  plt.clf()
 
 t += dt
