#!/usr/bin/env python

import numpy as np
import random
import matplotlib.pyplot as plt
import math
from scipy import polyfit
import matplotlib

# Abelian sandpile model


# Parameters
N = 31 # size of the system
zc = 3 # slope threshold that starts the avalanche
T = 100000 # number of steps
tstacj = 2500 # time to stationary state
nanim = 500 # steps to create plot


siec = np.zeros((N+2,N+2)) # +2 for boundary condition
brzeg = (np.arange((N+2)*(N+2)).reshape(N+2,N+2))
brzeg = np.choose( ( (brzeg<N+2) | (brzeg>(N+2)*(N+2-1)) | (brzeg%(N+2)==0) | (brzeg%(N+2)==N+2-1) ) , (0,1) ) # boundary

# Algorithm:
ziarenka = [] # number of grains of sand
lawiny = np.zeros(0.1*N*N) # number of avalanches
for t in xrange(T):
 # Add grain
 random.seed()
 x = N/2
 y = x
 siec[x+1][y+1] += 1
 # critical value -> avalanche
 crit = (siec > zc)
 S = 0 # size of the avalanche
 while (np.sum(crit) > 0):
  S += np.sum(crit)
  helper = np.choose(crit,(0,1))
  helper = np.roll(helper,-1,axis=0) + np.roll(helper,1,axis=0) + np.roll(helper,-1,axis=1) + np.roll(helper,1,axis=1)
  siec = np.choose(crit,(siec,0))
  siec += helper*(zc+1)/4
  # boundaries
  siec = np.choose(brzeg,(siec,0))
  crit = (siec > zc)
 # save size of the avalanche
 if t>tstacj and S>0 and S < np.size(lawiny):
  lawiny[S] += 1
 # Count grains
 ziarenka.append(np.sum(siec))
 # Plots:
 if not t%nanim:
  fig=plt.figure()
  ax=fig.add_subplot(111)
  ax.set_title('Height of the Sandpile')
  cax = ax.imshow(siec, interpolation='nearest')
  cax.set_clim(vmin=0, vmax=4)
  cbar = fig.colorbar(cax, ticks=[0,3, 5, 8], orientation='vertical')
  filename = str('%03d' % (t/nanim)) + '.png'
  plt.savefig(filename, dpi=100)
  plt.clf()


# Plot number of grains as a function of time
plt.plot(ziarenka[0:40000],'m-',label="number of grains")
plt.grid()
plt.title("Number of grains as a function of time for "+str(N)+'x'+str(N))
plt.savefig("Stationary_N"+str(N))
