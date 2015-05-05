import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

if __name__ == "__main__":
	x = []
	shape = 5.0
	cantidad_bins = 100
	alpha = 5.0
	beta = 1.0
	cantidad_datos = 100000
	scale = 1
	datos_gamma_teorema_lim_central=[]
	datos_betta_teorema_lim_central=[]
	esperanza_teorica_gamma=[]
	esperanza_teorica_beta=[]
	datos_gamma = np.random.gamma(shape, scale, cantidad_datos)
	datos_betta = np.random.beta(alpha, beta, cantidad_datos)
	
	suma_parcial = 0
	for iterator in range(cantidad_datos):
		suma_parcial += datos_gamma[iterator]
		datos_gamma_teorema_lim_central.append( suma_parcial/( iterator + 1 ) )
		esperanza_teorica_gamma.append( scale * shape )
		x.append(iterator)

	suma_parcial = 0
	for iterator in range(cantidad_datos):
		suma_parcial += datos_betta[iterator]
		datos_betta_teorema_lim_central.append( suma_parcial/( iterator + 1 ) )
		esperanza_teorica_beta.append( alpha/(alpha + beta) )

	plt.figure(1)
	plt.subplot(211)
	n, bins, patches = plt.hist(datos_gamma, cantidad_bins, normed=1, facecolor='green', alpha=0.5)
	plt.subplot(211).set_title('Histograma densidad gamma')
	plt.subplot(212)
	plt.ylim([4.8,5.2])
	plt.fill_between(x, datos_gamma_teorema_lim_central, esperanza_teorica_gamma, color='green', facecolor='green', interpolate=True, alpha=0.3)
	plt.xlabel('Cantidad de realizaciones de la variable aleatoria')
	plt.subplot(212).set_title('Promedio de los datos')

	plt.savefig('../latex/img/pregunta2_a_gamma.pdf',  bbox_inches=0)

	plt.figure(2)
	plt.subplot(211)
	n, bins, patches = plt.hist(datos_betta, cantidad_bins, normed=1, facecolor='red', alpha=0.5)
	plt.subplot(211).set_title('Histograma densidad beta')
	plt.subplot(212)
	plt.ylim([0.8,0.86])
	plt.fill_between(x, datos_betta_teorema_lim_central, esperanza_teorica_beta, color='red', facecolor='red', interpolate=True, alpha=0.3)
	plt.xlabel('Cantidad de realizaciones de la variable aleatoria')
	plt.subplot(212).set_title('Promedio de los datos')
	plt.savefig('../latex/img/pregunta2_a_beta.pdf',  bbox_inches=0)
	
	
	print '\nTodo Ok!\nLas imagenes generadas fueron guardadas en el directrio ../latex/img para ser usadas directamente en la confeccion del informe.'