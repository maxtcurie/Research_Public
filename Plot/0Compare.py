import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


path1='2d_list/36th_V3'
path2='2d_list/36th_V3_z0_zpi'
marker_size=5
bin_size=10

mid_Height=pd.read_csv(path1+'/Plot_data/0B_r_f_smooth.csv')
mid_z=pd.read_csv(path2+'/Plot_data/0B_r_f_smooth.csv')


f=mid_Height['f(kHz)']
f=f[::-1]

uni_freq     =np.linspace(np.min(f), np.max(f),num=len(f)*10)
Br_10        =np.interp(uni_freq,mid_Height['f(kHz)'][::-1],mid_Height['B_R(Gauss)'][::-1])
Br_1_error0  =np.interp(uni_freq,mid_Height['f(kHz)'][::-1],mid_Height['B_R_err(Gauss)'][::-1])
Br_20        =np.interp(uni_freq,mid_z['f(kHz)'][::-1],mid_z['B_R(Gauss)'][::-1])
Br_2_error0  =np.interp(uni_freq,mid_z['f(kHz)'][::-1],mid_z['B_R_err(Gauss)'][::-1])

#difference between 1 can 2
Br_30        =abs(Br_10-Br_20)
Br_3_error0  =(Br_1_error0**2.+Br_2_error0**2.)**0.5

f           =[]
f_error     =[]
Br_1        =[]
Br_1_error  =[]
Br_2        =[]
Br_2_error  =[]
Br_3        =[]
Br_3_error  =[]


for i in range(len(uni_freq)):
    if i%bin_size==0:
        Br_1.append(np.mean(Br_10[i:i+bin_size]))
        Br_2.append(np.mean(Br_20[i:i+bin_size]))
        Br_3.append(np.mean(Br_30[i:i+bin_size]))
        f.append(np.mean(uni_freq[i:i+bin_size]))
        Br_1_error.append((np.mean((Br_1_error0[i:i+bin_size])**2.))**0.5)
        Br_2_error.append((np.mean((Br_2_error0[i:i+bin_size])**2.))**0.5)
        Br_3_error.append((np.mean((Br_3_error0[i:i+bin_size])**2.))**0.5)

f=np.array(f)

f_error=[np.mean(abs(f[1:]-f[:-1]))]*len(f)


print(len(f))
print(len(Br_2))
print(len(Br_2_error))

plt.clf()
plt.errorbar(f,Br_1,xerr=f_error,yerr=Br_1_error,marker='s',ms=marker_size,linestyle='none',alpha=1,label=r'$Z=0\pm 3.5cm$')   
plt.errorbar(f,Br_2,xerr=f_error,yerr=Br_2_error,marker='s',ms=marker_size,linestyle='none',alpha=1,label=r'$z=0,\pi$')
plt.errorbar(f,Br_3,xerr=f_error,yerr=Br_3_error,marker='o',ms=marker_size,linestyle='none',alpha=1,label='diff')
plt.xlabel(r'$frequency(kHz)$',fontsize=15)
plt.ylabel(r'$\bar{B}_r(Gauss/\sqrt{Hz})$',fontsize=15)
plt.title(r'$\bar{B}_r$ spectrogram',fontsize=20)
plt.legend()
plt.savefig('B1_compare.png')
plt.show()



#********RIP***********

