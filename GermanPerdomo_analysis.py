import numpy as np
import matplotlib.pyplot as plt
import os
pi=np.pi
def normal_dist(x,mean,sigma):
	funcion = np.sqrt(1.0/(2.0*pi*(sigma**2))) / np.exp(((mean - x)**2)/(sigma**2))
	return funcion

def get_fit(filename):
	datos=np.loadtxt(filename)
	plt.figure()
	plt.hist(datos)
	plt.savefig(filename+'.png')
	print np.mean(datos), np.std(datos)
	


archivos = os.listdir('./*txt')

for i in archivos:
	get_fit(i)
	
