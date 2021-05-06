from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from Spectral_density import spectral_density
from FFT_general import FFT_function_time

np.random.seed(1234)

fs = 10e3
N = 1e5
amp = 2*np.sqrt(2)
freq = 1234.0
noise_power = 0.001 * fs / 2
time = np.arange(N) / fs
function = amp*np.sin(2*np.pi*freq*time)
function += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)


f, Pxx_den=spectral_density(function,time,window_for_FFT='boxcar',plot=False)
frequency_sort,amplitude_frequency_sort,phase_frequency_sort=FFT_function_time(function,time,plot=False)

plt.clf()
plt.plot(time,function)
plt.show()

#f, Pxx_den = signal.periodogram(function, fs)

#plt.semilogy(f, Pxx_den)
plt.plot(f, np.sqrt(Pxx_den),label='Welch')
plt.plot(frequency_sort,amplitude_frequency_sort,label='FFT')
plt.ylim([1e-7, 1e2])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.legend()
plt.show()