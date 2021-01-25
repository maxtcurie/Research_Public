import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.periodogram.html
def spectral_density(function,time,plot=False):
	time=np.array(time)
	dt=time[1:]-time[:-1]
	dt_min=np.min(dt)

	if abs(np.std(dt))>=np.min(dt)*0.01:
		print('time step is NOT uniform. interperlating')
		uni_time = np.linspace(min(time),max(time),int(abs((max(time)-min(time))/dt_min)*1.5)) #uniform time
		uni_function = np.interp(uni_time,time,function)
	else:
		uni_time=time
		uni_function=function


	fs=1./np.mean(abs(uni_time[1:]-uni_time[:-1]))
	print('avg_dt='+str(np.mean(abs(uni_time[1:]-uni_time[:-1]))))
	print('std_dt='+str(np.std(abs(uni_time[1:]-uni_time[:-1]))))
	f, Pxx_den = signal.periodogram(uni_function, fs) #, scaling='spectrum')
	if plot==True:
		plt.plot(f, Pxx_den)
		plt.plot(f, np.sqrt(Pxx_den))
		#plt.semilogy(f, Pxx_den)
		#plt.ylim([1e-7, 1e2])
		plt.xlabel('frequency [Hz]')
		plt.ylabel('PSD [V**2/Hz]')
		plt.show()
	return f, Pxx_den


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
#function=1+np.exp(-1.j * omega * time -3.j)+0.5*np.exp(+1.j * 2*omega * time-1.j)+0.5*np.exp(+1.j * 3.*omega * time-1.j)

function=np.exp(-1.j * omega * time )+0.5*np.exp(+1.j * 2*omega * time)+2.*np.exp(+1.j * 3.*omega * time)

#*********Demo function****************


f, Pxx_den=spectral_density(function,time,plot=True)


