import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.bar.html
width=0.5
labels = ['MTM', 'ETG', 'Neoclassical']#, 'Other'
#colors=['orange','blue']
sizes = [2.7, 0.17, 1.54]
error = [0.5,0.01,0]
total_trans=4.2
trans_error=1.5

locations=np.arange(0.5*width,0.5*width+float(len(labels))*width+0.00001,width)

total=np.sum(sizes)
total_error=0
for i in error:
	total_error=total_error+i**2.

total_error=np.sqrt(total_error)

print("Total transport: "+str(total))
print("Total transport error: "+str(total_error))

plt.clf()
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
for i in range(len(sizes)):
	plt.bar(locations[i], sizes[i], width, yerr=error[i],label=labels[i])

plt.bar(locations[-1], total, width, yerr=total_error,label='total')

'''
x_max=np.max(locations+0.5*width)
x=[0,0,x_max,x_max]
y=[total_trans-trans_error,total_trans+trans_error,total_trans+trans_error,total_trans-trans_error]
matplotlib.patches.Rectangle((0,total_trans-trans_error),10,2.*trans_error,alpha=0.4)
plt.fill(x,y,alpha=0.6,label='total transport')
'''

plt.axhline(total_trans,color='red',alpha=0.5,label='total heating')

plt.legend()

plt.show()

