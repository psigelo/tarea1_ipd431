import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

if __name__ == "__main__":
	shape = 5.0
	cantidad_bins = 100
	alpha = 5.0
	beta = 1.0
	cantidad_datos = 100000
	cantVariablesAleatoriasImpresion=[2,10,50,100]
	scale = 1
	esperanza_gamma = scale * shape
	esperanza_beta = alpha/(alpha + beta)
	varianza_gamma = shape*scale*scale
	varianza_beta = alpha*beta/((alpha+beta+1)*(alpha+beta)**2)

	plt.figure(1)
	plt.subplot(411)


	datos_gamma = np.random.gamma(shape, scale, cantVariablesAleatoriasImpresion[ 3 ] * cantidad_datos)
	datos_betta = np.random.beta(alpha, beta, cantVariablesAleatoriasImpresion[ 3 ] * cantidad_datos)


	for iterador_1 in xrange(0,4):
		Z=[]		
		for iterator in range(cantidad_datos):
			sn=np.sum(datos_gamma[iterator:iterator+cantVariablesAleatoriasImpresion[ iterador_1] :1])
			Z.append( (sn-cantVariablesAleatoriasImpresion[ iterador_1 ]*esperanza_gamma)/(np.sqrt(cantVariablesAleatoriasImpresion[ iterador_1 ]*varianza_gamma)) )
		
		
		plt.subplot(4,1,iterador_1+1)
		plt.xlim([-4,4])
		plt.subplot(4,1,iterador_1+1).set_title('Cantidad de v.a, n='+str(cantVariablesAleatoriasImpresion[ iterador_1]))
		n, bins, patches = plt.hist(Z, cantidad_bins, normed=1, facecolor='green', alpha=0.5)
		y = mlab.normpdf(bins, 0, 1)
		plt.plot(bins, y, 'r--')

	plt.subplots_adjust(left=0.15)
	plt.tight_layout()
	plt.savefig('../latex/img/pregunta2_b_gamma.pdf',  bbox_inches=0)

	plt.figure(2)
	plt.subplot(411)

	for iterador_1 in xrange(0,4):
		Z=[]
		for iterator in range(cantidad_datos):
			sn=np.sum(datos_betta[iterator:iterator+cantVariablesAleatoriasImpresion[ iterador_1] :1])
			Z.append( (sn-cantVariablesAleatoriasImpresion[ iterador_1 ]*esperanza_beta)/(np.sqrt(cantVariablesAleatoriasImpresion[ iterador_1 ]*varianza_beta)) )
		
		
		plt.subplot(4,1,iterador_1+1)
		plt.xlim([-4,4])
		plt.subplot(4,1,iterador_1+1).set_title('Cantidad de v.a, n='+str(cantVariablesAleatoriasImpresion[ iterador_1]))
		n, bins, patches = plt.hist(Z, cantidad_bins, normed=1, facecolor='red', alpha=0.5)
		y = mlab.normpdf(bins, 0, 1)
		plt.plot(bins, y, 'r--')

	plt.subplots_adjust(left=0.15)
	plt.tight_layout()
	plt.savefig('../latex/img/pregunta2_b_beta.pdf',  bbox_inches=0)
	
	
	print '\nTodo Ok!\nLas imagenes generadas fueron guardadas en el directrio ../latex/img para ser usadas directamente en la confeccion del informe.'