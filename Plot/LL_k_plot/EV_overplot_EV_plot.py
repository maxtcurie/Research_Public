import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import array as arr

#https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html

name_list=['kx000','kx020','kx040','kx060','kx080']
title_list=['kx=0.00','kx=0.20','kx=0.40','kx=0.60','kx=0.80']
Dir_name='./1966ms/'
#all the ky, so that plot can show the stable ky
ky0=[0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
Dopppler_kHz=245.6 #Doppler shift in kHz for ky=1.0

#Plot growth rate 

fig, axs = plt.subplots(len(name_list), sharex=True, sharey=True, )
fig.suptitle('Local linear k dependence')


for i in range(len(name_list)):
	name=name_list[i]
	path=Dir_name+name+'/'

	MTM=pd.read_csv(path+'MTM.csv')  
	ETG=pd.read_csv(path+'ETG.csv') 
	ITG=pd.read_csv(path+'ITG.csv') 
	KBM=pd.read_csv(path+'KBM.csv') 


	ky_min_list0=np.append(ETG['kymin'],MTM['kymin'])
	ky_min_list0=np.append(ky_min_list0,ITG['kymin'])
	ky_min_list0=np.append(ky_min_list0,KBM['kymin'])

	print(str(ky_min_list0))
	#clear the nan in the list
	ky_min_list0 = [x for x in ky_min_list0 if str(x) != 'nan']
	ky_min_list0=list(set(ky_min_list0))
	print(str(ky_min_list0))
	ky_min_list=[]
	for ky_temp in ky_min_list0:
		ky_min_list.append(round(ky_temp,2))

	ky=list(set(ky0))
	print('*******'+str(ky)) 
	#ky = arr.array('f', ky)
	#print(ky)
	for k_temp in ky_min_list:
		print(k_temp)
		ky.remove(k_temp)
	print('*******'+str(ky))

	axs[i].scatter(ky,[0]*len(ky),marker='o',color='grey',label='Stable')

	ITG_list0 = [x for x in ITG['kymin'] if str(x) != 'nan']
	if len(ITG_list0)!=0:
		axs[i].scatter(ITG['kymin'],ITG['gamma(cs/a)'],marker='o',color='green',label='ITG')
	ETG_list0 = [x for x in ETG['kymin'] if str(x) != 'nan']
	if len(ETG_list0)!=0:
		axs[i].scatter(ETG['kymin'],ETG['gamma(cs/a)'],marker='o',color='blue',label='ETG')
	MTM_list0 = [x for x in MTM['kymin'] if str(x) != 'nan']
	if len(MTM_list0)!=0:
		axs[i].scatter(MTM['kymin'],MTM['gamma(cs/a)'],marker='o',color='red',label='MTM')
	KBM_list0 = [x for x in KBM['kymin'] if str(x) != 'nan']
	if len(KBM_list0)!=0:
		axs[i].scatter(KBM['kymin'],KBM['gamma(cs/a)'],marker='o',color='purple',label='KBM')
	
	plt.xlim(0.08,1)
	plt.ylim(0,10)
	axs[i].legend()

	axs[i].set_title(title_list[i])



#Plot frequency in plasma frame

plt.xlabel(r'$k_y\rho_s$',fontsize=10)
plt.ylabel(r'$\gamma(cs/a)$',fontsize=10)

plt.show()


fig, axs = plt.subplots(len(name_list), sharex=True, sharey=True, )
fig.suptitle('Local linear k dependence(Plasma frame)')

for i in range(len(name_list)):
	name=name_list[i]
	path=Dir_name+name+'/'

	MTM=pd.read_csv(path+'MTM.csv')  
	ETG=pd.read_csv(path+'ETG.csv') 
	ITG=pd.read_csv(path+'ITG.csv') 
	KBM=pd.read_csv(path+'KBM.csv') 

	ky_min_list0=np.append(ETG['kymin'],MTM['kymin'])
	ky_min_list0=np.append(ky_min_list0,ITG['kymin'])
	ky_min_list0=np.append(ky_min_list0,KBM['kymin'])

	print(str(ky_min_list0))
	#clear the nan in the list
	ky_min_list0 = [x for x in ky_min_list0 if str(x) != 'nan']
	ky_min_list0=list(set(ky_min_list0))
	print(str(ky_min_list0))
	ky_min_list=[]
	for ky_temp in ky_min_list0:
		ky_min_list.append(round(ky_temp,2))

	axs[i].scatter(ky,[0]*len(ky),marker='o',color='grey',label='Stable')

	ITG_list0 = [x for x in ITG['kymin'] if str(x) != 'nan']
	if len(ITG_list0)!=0:
		axs[i].scatter(ITG['kymin'],ITG['gamma(cs/a)'],marker='o',color='green',label='ITG')
	ETG_list0 = [x for x in ETG['kymin'] if str(x) != 'nan']
	if len(ETG_list0)!=0:
		axs[i].scatter(ETG['kymin'],ETG['gamma(cs/a)'],marker='o',color='blue',label='ETG')
	MTM_list0 = [x for x in MTM['kymin'] if str(x) != 'nan']
	if len(MTM_list0)!=0:
		axs[i].scatter(MTM['kymin'],MTM['gamma(cs/a)'],marker='o',color='red',label='MTM')
	KBM_list0 = [x for x in KBM['kymin'] if str(x) != 'nan']
	if len(KBM_list0)!=0:
		axs[i].scatter(KBM['kymin'],KBM['gamma(cs/a)'],marker='o',color='purple',label='KBM')
	
	plt.xlim(0.08,1)
	plt.ylim(0,1000)
	axs[i].legend()
	axs[i].set_title(title_list[i])
plt.xlabel(r'$k_y\rho_s$',fontsize=10)
plt.ylabel('Frequency(kHz)',fontsize=10)
plt.show()

#Plot frequency in lab frame

fig, axs = plt.subplots(len(name_list), sharex=True, sharey=True, )
fig.suptitle('Local linear k dependence(Lab frame)')
for i in range(len(name_list)):
	name=name_list[i]
	path=Dir_name+name+'/'

	ky_min_list0=np.append(ETG['kymin'],MTM['kymin'])
	ky_min_list0=np.append(ky_min_list0,ITG['kymin'])
	ky_min_list0=np.append(ky_min_list0,KBM['kymin'])

	print(str(ky_min_list0))
	#clear the nan in the list
	ky_min_list0 = [x for x in ky_min_list0 if str(x) != 'nan']
	ky_min_list0=list(set(ky_min_list0))
	print(str(ky_min_list0))
	ky_min_list=[]
	for ky_temp in ky_min_list0:
		ky_min_list.append(round(ky_temp,2))
	ky=list(set(ky0))
	print('*******'+str(ky)) 
	#ky = arr.array('f', ky)
	#print(ky)
	for k_temp in ky_min_list:
		print(k_temp)
		ky.remove(k_temp)
	print('*******'+str(ky))
	axs[i].scatter(ky,[0]*len(ky),marker='o',color='grey',label='Stable')

	ITG_list0 = [x for x in ITG['kymin'] if str(x) != 'nan']
	if len(ITG_list0)!=0:
		axs[i].scatter(ITG['kymin'],ITG['gamma(cs/a)'],marker='o',color='green',label='ITG')
	ETG_list0 = [x for x in ETG['kymin'] if str(x) != 'nan']
	if len(ETG_list0)!=0:
		axs[i].scatter(ETG['kymin'],ETG['gamma(cs/a)'],marker='o',color='blue',label='ETG')
	MTM_list0 = [x for x in MTM['kymin'] if str(x) != 'nan']
	if len(MTM_list0)!=0:
		axs[i].scatter(MTM['kymin'],MTM['gamma(cs/a)'],marker='o',color='red',label='MTM')
	KBM_list0 = [x for x in KBM['kymin'] if str(x) != 'nan']
	if len(KBM_list0)!=0:
		axs[i].scatter(KBM['kymin'],KBM['gamma(cs/a)'],marker='o',color='purple',label='KBM')
	
	
	plt.xlim(0.08,1)
	plt.ylim(0,1000)
	axs[i].legend()
	axs[i].set_title(title_list[i])
plt.xlabel(r'$k_y\rho_s$',fontsize=10)
plt.ylabel('Frequency(kHz)',fontsize=10)
plt.show()

