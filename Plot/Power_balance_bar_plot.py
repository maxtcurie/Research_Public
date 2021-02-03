import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.bar.html
width=0.5
labels = ['MTM', 'ETG']#, 'Neoclassical']#, 'Other'
#colors=['orange','blue']
sizes = [2.7, 0.17]#, 0]
error = [0.5,0.01]#,0]
total_heating=4.2
neo=total_heating-np.sum(sizes)

locations=np.arange(0.5*width,0.5*width+float(len(labels))*width+0.00001,width)

total=np.sum(sizes)
total_error=0
for i in error:
	total_error=total_error+i**2.

total_error=np.sqrt(total_error)

plt.clf()
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
for i in range(len(sizes)):
	plt.bar(locations[i], sizes[i], width, yerr=error[i],label=labels[i])

plt.bar(locations[-1], total, width, yerr=total_error,label='total')

plt.axhline(total_heating,color='red',alpha=0.5,label='total heating')

plt.legend()

plt.show()

