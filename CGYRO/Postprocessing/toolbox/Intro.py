import os
import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from gacodefuncs import average
from cgyro.data import cgyrodata

#libaray gacodefuncs is from: 
# /global/cfs/cdirs/atom/atom-install-cori/gacode-source-mkl/f2py/pygacode/gacodefuncs.py

#libaray cgyro.data are from: 
# /global/cfs/cdirs/atom/atom-install-cori/gacode-source-mkl/f2py/pygacode/cgyro/data.py


#from mc_average import average

# load the cgyro directory
#sim = cgyrodata('reg01/')
sim = cgyrodata('./../reg08/')

# can read in various input parameters
alnnt_i = sim.dlntdr[0]   # ion temp gradient scale length
ky      = sim.ky0         # ky rho_s

# real frequency and linear growth rate
# compare with >> cgyro_plot -e reg01 -plot freq
omega    = sim.freq[0,0,-1]
gamma    = sim.freq[1,0,-1]
print('omega='+str(omega))
print('omega='+str(gamma))


sim.getflux('auto')

t  = sim.t
ys = np.sum(sim.ky_flux,axis=(2,3))
# Now, ys -> {n_species,3,nt}
w=1. # time-average over the last w*10%


# particle flux for each species, Gamma/Gamma_GB
# same result as >> cgyro_plot -e reg01 -plot flux -moment n -w 0.1
y = ys[:,0,:]

print(y[0,:])
print(t)
print(w)
pfluxi = average(y[0,:],t,w,0.)
pfluxe = average(y[1,:],t,w,0.)

# energy flux for each species, Q/Q_GB
# same result as >> cgyro_plot -e reg01 -plot flux -moment n -w 0.1
y = ys[:,1,:]
efluxi = average(y[0,:],t,w,0.0)
efluxe = average(y[1,:],t,w,0.0)

print(efluxi,efluxe)

sim.getbigfield()

phi=sim.kxky_phi
print(np.shape(phi))
