import os
import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import gacodefuncs
from cgyro.data import cgyrodata

import tool

class sim_info:
    def __init__(self,sim_dir,w=0.1):
        # w=time-average over the last w*10%
        sim=cgyrodata(sim_dir)
        # can read in various input parameters
        alnnt_i = sim.dlntdr[0]   # ion temp gradient scale length
        ky      = sim.ky0         # ky rho_s
        sim.getflux('auto')
        sim.getbigfield()
        t  = sim.t
        ys = np.sum(sim.ky_flux,axis=(2,3))

        # real frequency and linear growth rate
        # compare with >> cgyro_plot -e reg01 -plot freq
        omega_avg, omega_dev = tool.avg_dev(sim.freq[0,0,:],t,w,0.)
        gamma_avg, gamma_dev = tool.avg_dev(sim.freq[1,0,:],t,w,0.)

        print('omega='+str(omega_avg)+'+-'+str(omega_dev))
        print('gamma='+str(gamma_avg)+'+-'+str(gamma_dev))
        # case for not converging
        if max(abs(omega_dev/omega_avg),abs(gamma_dev/gamma_avg)) >0.02:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('run is not converging')
            run_or_not=input('countiune running: 1. yes, 0. no\n')
            if int(run_or_not)==1:
                pass
            else:
                raise sys.exit("Run not converging, please run for longer time")

        dic={}
        dic['omega']=omega_avg
        dic['gamma']=gamma_avg
        dic['omega_dev']=omega_dev
        dic['gamma_dev']=gamma_dev

        # time-averaged fluxes
        # Now, ys -> {n_species,3,nt}
        # particle flux for each species, Gamma/Gamma_GB
        # same result as >> cgyro_plot -e reg01 -plot flux -moment n -w 0.1
        y = ys[:,0,:]
        
        pfluxi = tool.average(y[0,:],t,w,0.)
        pfluxe = tool.average(y[1,:],t,w,0.)
        
        # def average(f,t,wmin,wmax):
        # source code
        # /global/cfs/cdirs/atom/atom-install-cori/gacode-source-mkl/f2py/pygacode/gacodefuncs.py
        # This function average function f over time from (1-wmin)*tmax to (1-wmax)*tmax
        
        # energy flux for each species, Q/Q_GB
        # same result as >> cgyro_plot -e reg01 -plot flux -moment n -w 0.1
        y = ys[:,1,:]
        efluxi = tool.average(y[0,:],t,w,0.0)
        efluxe = tool.average(y[1,:],t,w,0.0)

    
        dic['Q_e']=efluxe
        dic['Q_i']=efluxi
        dic['D_e']=pfluxe
        dic['D_i']=pfluxe
    
        dic['Q_e_Q_i']=efluxe/efluxi
        dic['D_e_D_i']=pfluxe/pfluxi
        dic['Q_e_D_e']=efluxe/pfluxe
        dic['Q_i_D_i']=efluxi/pfluxi
        
        #phi=(kx,ky,t)
        phi=sim.kxky_phi
        try:
            apar=sim.kxky_apar
        except:
            print('apar is not avaiable')

        try:
            bpar=sim.kxky_bpar
        except:
            print('bpar is not avaiable')

        print(np.shape(phi))
        
        print(dic)


        self.t       =sim.t
        self.omega_t =sim.freq[0,0,:]
        self.gamma_t =sim.freq[1,0,:]
        self.phi_kx_ky_t=sim.kxky_phi

        self.dic=dic
        
    