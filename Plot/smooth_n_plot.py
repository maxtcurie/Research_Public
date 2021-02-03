import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def smooth(avg_list,bin_size):
    l_list=len(avg_list)
    list_avg=np.zeros(l_list-bin_size+1)
    list_dev=np.zeros(l_list-bin_size+1)
    avg=0
    for i in range(0,len(list_avg)):
      list_avg[i]=np.mean(avg_list[i:i+bin_size]) 
      list_dev[i]=np.std(avg_list[i:i+bin_size]) 

    return list_avg, list_dev



data=pd.read_csv('0B_r_f_from_0.035_to_-0.035_smooth.csv')  

f_avg, f_dev=smooth(data['f(kHz)'],20)
B1_avg, B1_dev=smooth(data['B_R(Gauss)'],20)

if csv_output==True:
    d = {'f(kHz)':f_avg,'f_err(kHz)':f_dev,'B_R(Gauss)':B1_avg,'B_R_err(Gauss)':B1_dev}
    df=pd.DataFrame(d, columns=['f(kHz)','f_err(kHz)','B_R(Gauss)','B_R_err(Gauss)'])
    df.to_csv('0B_r_f_from_'+str(max_Z0)+'_to_'+str(min_Z0)+'_smooth.csv',index=False)


plt.clf()
ax2=df.plot(kind='scatter',x='f(kHz)',xerr='f_err(kHz)',y='B_R(Gauss)',y_err='B_R_err(Gauss)',color='blue',grid=True)
ax2.set_xlabel('frequency (kHz)',fontsize=15)
ax2.set_ylabel(r'$B_r(Gauss)$',fontsize=15)
plt.title(r'$\bar{B}_r$ spectrogram',fontsize=20)
plt.savefig('0B1_f_smooth.png')
plt.show()