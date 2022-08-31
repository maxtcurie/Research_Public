import os
import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from gacodefuncs import average
from cgyro.data import cgyrodata


# load the cgyro directory
#sim = cgyrodata('reg01/')
sim_dir_list = ['./../reg08/']



n=1
w=1. # time-average over the last w*10%

sim_dic=[]

for sim_dir in sim_dir_list:

	dic={}
	sim=cgyrodata(sim_dir)
	# can read in various input parameters
	alnnt_i = sim.dlntdr[0]   # ion temp gradient scale length
	ky      = sim.ky0         # ky rho_s
	
	# real frequency and linear growth rate
	# compare with >> cgyro_plot -e reg01 -plot freq
	omega    = sim.freq[0,0,-1]
	gamma    = sim.freq[1,0,-1]
	print('omega='+str(omega))
	print('gamma='+str(gamma))

	dic['omega']=omega
	dic['gamma']=gamma

	sim.getflux('auto')
	
	# time-averaged fluxes
	t  = sim.t
	ys = np.sum(sim.ky_flux,axis=(2,3))
	# Now, ys -> {n_species,3,nt}
	
	# particle flux for each species, Gamma/Gamma_GB
	# same result as >> cgyro_plot -e reg01 -plot flux -moment n -w 0.1
	y = ys[:,0,:]
	
	pfluxi = average(y[0,:],t,w,0.)
	pfluxe = average(y[1,:],t,w,0.)
	
	# def average(f,t,wmin,wmax):
	# source code
	# /global/cfs/cdirs/atom/atom-install-cori/gacode-source-mkl/f2py/pygacode/gacodefuncs.py
	# This function average function f over time from (1-wmin)*tmax to (1-wmax)*tmax
	
	# energy flux for each species, Q/Q_GB
	# same result as >> cgyro_plot -e reg01 -plot flux -moment n -w 0.1
	y = ys[:,1,:]
	efluxi = average(y[0,:],t,w,0.0)
	efluxe = average(y[1,:],t,w,0.0)

	


	dic['Q_e']=efluxe
	dic['Q_i']=efluxi
	dic['D_e']=pfluxe
	dic['D_i']=pfluxe

	dic['Q_e_Q_i']=efluxe/efluxi
	dic['D_e_D_i']=pfluxe/pfluxi
	dic['Q_e_D_e']=efluxe/pfluxe
	dic['Q_i_D_i']=efluxi/pfluxi


	sim.getbigfield()

	phi=sim.kxky_phi
	print(np.shape(phi))

	print(dic)
	sim_dic.append(dic)

	