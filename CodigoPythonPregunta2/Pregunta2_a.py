import random
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


	# """
	# Demo of the histogram (hist) function with a few features.

	# In addition to the basic histogram, this demo shows a few optional features:

	#     * Setting the number of data bins
	#     * The ``normed`` flag, which normalizes bin heights so that the integral of
	#       the histogram is 1. The resulting histogram is a probability density.
	#     * Setting the face color of the bars
	#     * Setting the opacity (alpha value).

	# """
	


	# # example data
	# mu = 100 # mean of distribution
	# sigma = 15 # standard deviation of distribution
	# x = mu + sigma * np.random.randn(10000)

	# num_bins = 50
	# # the histogram of the data
	# n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
	# # add a 'best fit' line
	# y = mlab.normpdf(bins, mu, sigma)
	# plt.plot(bins, y, 'r--')
	# plt.xlabel('Smarts')
	# plt.ylabel('Probability')
	# plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

	# # Tweak spacing to prevent clipping of ylabel
	# plt.subplots_adjust(left=0.15)
	# plt.show()

