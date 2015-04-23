import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

if __name__ == "__main__":

	tetha = 5.0
	cantidad_bins = 100
	alpha = 5.0
	beta = 1.0
	cantidad_datos = 10000
	factor_escala_gamma = 1
	datos_gamma_teorema_lim_central=[]
	datos_betta_teorema_lim_central=[]
	esperanza_teorica_gamma=[]
	esperanza_teorica_beta=[]
	datos_gamma = np.random.gamma(tetha, factor_escala_gamma, cantidad_datos)
	datos_betta = np.random.beta(alpha, beta, cantidad_datos)
	
	suma_parcial = 0
	for iterator in range(cantidad_datos):
		suma_parcial += datos_gamma[iterator]
		datos_gamma_teorema_lim_central.append( suma_parcial/( iterator + 1 ) )
		esperanza_teorica_gamma.append( factor_escala_gamma * tetha )

	suma_parcial = 0
	for iterator in range(cantidad_datos):
		suma_parcial += datos_betta[iterator]
		datos_betta_teorema_lim_central.append( suma_parcial/( iterator + 1 ) )
		esperanza_teorica_beta.append( alpha/(alpha + beta) )

	plt.figure(1)
	plt.subplot(221)
	n, bins, patches = plt.hist(datos_gamma, cantidad_bins, normed=1, facecolor='green', alpha=0.5)
	plt.subplot(222)
	n, bins, patches = plt.hist(datos_betta, cantidad_bins, normed=1, facecolor='red', alpha=0.5)
	plt.subplot(223)
	plt.plot(datos_gamma_teorema_lim_central, color='red')
	plt.plot(esperanza_teorica_gamma, color='blue')
	plt.subplot(224)
	plt.plot(datos_betta_teorema_lim_central, color='red')
	plt.plot(esperanza_teorica_beta, color='blue')
	plt.show()
