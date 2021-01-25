import numpy as np
import matplotlib.pyplot as plt

#Un-uniform FFT: https://scicomp.stackexchange.com/questions/593/how-do-i-take-the-fft-of-unevenly-spaced-data

def sort_x_f(x_unsort,f_unsort): 
   
    arr_unsort=[x_unsort,f_unsort]
    f_x_unsort=tuple(map(tuple, np.transpose(arr_unsort)))
      
    f_x_sort=sorted(f_x_unsort, key=lambda f_x_unsort: f_x_unsort[0])
    f_x_sort=np.array(f_x_sort)
    f_x_sort=np.transpose(f_x_sort)
    x_sort=f_x_sort[0,:]
    f_sort=f_x_sort[1,:]

    return x_sort,f_sort

def FFT_function_time_uniform(function,time,timestep,plot):
    
    norm=1./float(len(time))  #normalizing factor
    
    amplitude_complex = np.fft.fft(function)
    #print(str(time.shape[-1]))
    #output_x = np.fft.fftfreq(t.shape[-1])
    frequency = np.fft.fftfreq(time.shape[-1], d=timestep)
    amplitude_frequency=abs(norm*amplitude_complex)
    #amplitude_frequency=norm*amplitude_complex.real
    phase_frequency=np.angle(amplitude_complex)

    #https://stackoverflow.com/questions/43019136/how-to-get-phase-fft-of-a-signal-can-i-get-phase-in-time-domain

    if plot==True: 
        plt.clf()
        plt.ylabel(r'$function$',fontsize=10)
        plt.xlabel(r'$time$',fontsize=10)
        plt.plot(time,function)
        plt.title('Function of time',fontsize=20)
        plt.show()

        plt.clf()
        plt.ylabel(r'$amplitude$',fontsize=10)
        plt.xlabel(r'$frequency$',fontsize=10)
        #plt.axvline(frequency,color='red', label="correct frequency")
        #plt.axvline(2.*frequency,color='red', label="correct frequency")
        plt.plot(frequency,amplitude_frequency,label="frequency")
        plt.legend()
        plt.title('Function of frequency',fontsize=20)
        plt.show()

    return frequency,amplitude_frequency,phase_frequency


def FFT_function_time_not_uniform(function,time,plot):
    dt=time[:-1]-time[1:]

    dt_min=np.min(abs(dt))

    print('length of the time: '+str(float(int(abs((max(time)-min(time))/dt_min)*1.5))))
    uni_time = np.linspace(min(time),max(time),int(abs((max(time)-min(time))/dt_min)*1.5)) #uniform time
    uni_function = np.interp(uni_time,time,function)

    dt=uni_time[:-1]-uni_time[1:]
    timestep=dt[0]
    
    frequency,amplitude_frequency,phase_frequency=FFT_function_time_uniform(uni_function,uni_time,timestep,plot)
    return frequency,amplitude_frequency,phase_frequency


def FFT_function_time(function,time,plot=False): 
    time=np.array(time)
    print(time)
    dt=time[1:]-time[:-1]
    print(dt)
    #plt.clf()
    #plt.ylabel(r'$n$',fontsize=10)
    #plt.xlabel(r'$dt$',fontsize=10)
    #plt.plot(time[1:])
    #plt.plot(time[:-1])
    #plt.plot(dt)
    #plt.title('dt',fontsize=20)
    #plt.show()
    print(np.min(dt))
    if abs(np.std(dt))<np.min(dt)*0.01:
        timestep=dt[0]
        print('time step is uniform, dt=: '+str(timestep))
        print('Runing uniform FFT')
        frequency,amplitude_frequency,phase_frequency=FFT_function_time_uniform(function,time,timestep,plot)
    else:
        print('time step is NOT uniform. Runing non-uniform FFT')
        frequency,amplitude_frequency,phase_frequency=FFT_function_time_not_uniform(function,time,plot)

    frequency_sort,amplitude_frequency_sort=sort_x_f(frequency,amplitude_frequency)
    frequency_sort,phase_frequency_sort=sort_x_f(frequency,phase_frequency)

    return frequency_sort,amplitude_frequency_sort,phase_frequency_sort


'''
#*********Demo function****************
timestep0=0.002
time1 = np.arange(0.,2.,timestep0)
time2 = np.arange(2.00001,3.,timestep0*0.1)

#time = time1
time = np.append(time1, time2)
print(str(time))
#time.append(2.001)
#time.extend(time)


frequency=20.
omega = 2.*np.pi*frequency
function=1+np.exp(-1.j * omega * time -3.j)+0.5*np.exp(+1.j * 2*omega * time-1.j)
#*********Demo function****************

#frequency,amplitude_frequency,amplitude_growth = FFT_function_time(abs(function)**2.,time,plot=True)
frequency,amplitude_frequency,amplitude_growth = FFT_function_time(function,time,plot=True)
#frequency,amplitude_frequency,amplitude_growth = window_FFT_function_time(function,time,plot=True)




'''