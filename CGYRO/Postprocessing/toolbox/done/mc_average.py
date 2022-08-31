import numpy as np 

def average(f,t,wmin,wmax):

    n_time = len(t)

    tmin = (1.0-wmin)*t[-1]
    tmax = (1.0-wmax)*t[-1]

    tmin_index=np.argmin(abs(t-tmin))
    tmax_index=np.argmin(abs(t-tmin))

    # Manage case with 2 time points or less (eigenvalue)
    if tmax_index-tmin_index<=1:
        ave  = f[-1]
        
    else:
        t_window = 0.0
        ave      = 0.0
        for i in range(tmin_index,tmax_index+1):
            if t[i] >= tmin and t[i] <= tmax:
                ave = ave+0.5*(f[i]+f[i+1])*(t[i+1]-t[i])
                t_window = t_window+t[i+1]-t[i]
        ave = ave/t_window

    return ave