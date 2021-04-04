import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import array as arr

#https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html

name_list=['kx000','kx020','kx040','kx060','kx080']
title_list=['kx=0.00','kx=0.20','kx=0.40','kx=0.60','kx=0.80']

#all the ky, so that plot can show the stable ky
ky0=[0.05,0.06,0.07,0.08,0.11,0.13,0.14,0.16,0.18,0.1, 0.12, 0.15, 0.17, 0.18, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1]
#i_list: 
i_list=[2,3,4] 	#The kx folder has unstable ITG 
				#where 0 is kx000, 1 is kx020 and so on. 

#plt.clf()

fig, axs = plt.subplots(len(name_list), sharex=True, sharey=True, )
fig.suptitle('Local linear k dependence')


for i in range(len(name_list)):
	name=name_list[i]
	path='./EV_scan/'+name+'/'

	MTM=pd.read_csv(path+'MTM.csv')  
	ETG=pd.read_csv(path+'ETG.csv') 
	
	ky_min_list0=np.append(ETG['kymin'],MTM['kymin'])
	ky_min_list0=list(set(ky_min_list0))
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
	

	axs[i].scatter(ETG['kymin'],ETG['gamma(cs/a)'],marker='o',label='ETG',color='blue')
	
	axs[i].scatter(MTM['kymin'],MTM['gamma(cs/a)'],marker='o',color='red',label='MTM')

	axs[i].scatter(ky,[0]*len(ky),marker='o',color='grey',label='Stable')
	if i in i_list:
		ITG=pd.read_csv(path+'ITG.csv') 
		axs[i].scatter(ITG['kymin'],ITG['gamma(cs/a)'],marker='o',color='green',label='ITG')
	
	plt.xlim(0.08,1)
	plt.ylim(0,10)
	axs[i].legend()

	axs[i].set_title(title_list[i])
#
'''
	if i==0:
		plt.ylabel(r'$\gamma(cs/a)$',fontsize=10)
	elif i==len(name_list)-1:
		plt.xlabel(r'$k_y\rho_i$',fontsize=10)
'''

plt.xlabel(r'$k_y\rho_s$',fontsize=10)
plt.ylabel(r'$\gamma(cs/a)$',fontsize=10)

plt.show()


fig, axs = plt.subplots(len(name_list), sharex=True, sharey=True, )
fig.suptitle('Local linear k dependence')


for i in range(len(name_list)):
	name=name_list[i]
	path='./EV_scan/'+name+'/'

	MTM=pd.read_csv(path+'MTM.csv')  
	ETG=pd.read_csv(path+'ETG.csv') 
	
	ky_min_list0=np.append(ETG['kymin'],MTM['kymin'])
	ky_min_list0=list(set(ky_min_list0))
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
	

	axs[i].scatter(ETG['kymin'],abs(ETG['omega(kHz)']),marker='o',label='ETG',color='blue')
	
	axs[i].scatter(MTM['kymin'],abs(MTM['omega(kHz)']),marker='o',color='red',label='MTM')

	axs[i].scatter(ky,[0]*len(ky),marker='o',color='grey',label='Stable')
	if i in i_list:
		ITG=pd.read_csv(path+'ITG.csv') 
		axs[i].scatter(ITG['kymin'],abs(ITG['omega(kHz)']),marker='o',color='green',label='ITG')
	
	plt.xlim(0.08,1)
	plt.ylim(0,1000)
	axs[i].legend()

	axs[i].set_title(title_list[i])
#
'''
	if i==0:
		plt.ylabel(r'$\gamma(cs/a)$',fontsize=10)
	elif i==len(name_list)-1:
		plt.xlabel(r'$k_y\rho_i$',fontsize=10)
'''

plt.xlabel(r'$k_y\rho_s$',fontsize=10)
plt.ylabel('Frequency(kHz)',fontsize=10)

plt.show()
