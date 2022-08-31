import numpy as np
import matplotlib.pyplot as plt


def uniform(function,time):
    function = np.array(function)
    time=np.array(time)

    dt=time[1:]-time[:-1]
    dt_min=np.mean(dt)
    
    if abs(np.std(dt))>=np.min(dt)*0.01:
        print('time step is NOT uniform. interperlating')
        uni_time = np.linspace(min(time),max(time),int(abs((max(time)-min(time))/dt_min)*1.5)) #uniform time
        uni_function = np.interp(uni_time,time,function)
    else:
        uni_time=time
        uni_function=function
    return uni_function,uni_time    


def avg_dev(f,t,wmin,wmax):
    n_time = len(t)

    tmin = (1.0-wmin)*t[-1]
    tmax = (1.0-wmax)*t[-1]
    print(f)
    print(t)
    tmin_index=np.argmin(abs(t-tmin))
    tmax_index=np.argmin(abs(t-tmax))

    # Manage case with 2 time points or less (eigenvalue)
    if tmax_index-tmin_index==0:
        avg  = f[-1]
        dev = 0
    elif tmax_index-tmin_index==1:
        avg  = f[-1]
        dev  = f[-1]
    else:
        if tmax_index==len(f)-1:
            f,t=uniform(f[tmin_index:],t[tmin_index:])
        else:
            f,t=uniform(f[tmin_index:tmax_index],t[tmin_index:tmax_index])
        avg=np.mean(f)
        dev=np.std(f)
    return avg,dev


def average(f,t,wmin,wmax):
    n_time = len(t)

    tmin = (1.0-wmin)*t[-1]
    tmax = (1.0-wmax)*t[-1]

    tmin_index=np.argmin(abs(t-tmin))
    tmax_index=np.argmin(abs(t-tmax))

    # Manage case with 2 time points or less (eigenvalue)
    if tmax_index-tmin_index<=1:
        ave  = f[-1]
        
    else:
        t_window = 0.0
        ave      = 0.0
        for i in range(max(0,tmin_index-1),min(tmax_index+1,len(t)-1)):
            if t[i] >= tmin and t[i] <= tmax:
                ave = ave+0.5*(f[i]+f[i+1])*(t[i+1]-t[i])
                t_window = t_window+t[i+1]-t[i]
        ave = ave/t_window

    return ave


