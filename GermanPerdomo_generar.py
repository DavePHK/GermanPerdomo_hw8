import numpy as np

#Se definen dos funciones que generan muestras de numeros aleatorios
#Sample_1 genera numeros aleatorios que siguen una probabilidad especifica
#Sample_2 los genera a partir de una distribucion exponencial con beta = 0.5

def sample_1(N):	
	sample = np.random.choice(np.array([-10.0,-5.0,3.0,9.0]),size=N,p=[0.1,0.4,0.2,0.3])
	return sample 

def sample_2(N):
	sample = np.random.exponential(0.5,N)
	return sample

#Esta funcion crea un array de M promedios dada una funcion de sample
def get_mean(sampling_fun,N,M):
	promedios = []
	for i in range(0,M):
		mean = np.mean(sampling_fun(N))
		promedios.append(mean)
	
	return np.array(promedios)


samplings = ['sample_1','sample_2']
N=[10,100,1000]
M=10000

for sample in samplings:
	if sample == 'sample_1':
		for j in range(0,len(N)):
			
			np.savetxt('sample_1_'+str(N[j])+'.txt',get_mean(sample_1,N[j],M).T)
			
					
	else:
		for k in range(0,len(N)):
			
			np.savetxt('sample_2_'+str(N[k])+'.txt',get_mean(sample_2,N[k],M).T)


			




				
	
