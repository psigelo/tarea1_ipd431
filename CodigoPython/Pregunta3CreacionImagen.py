import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

u = 1.5
x = np.linspace(0, 2 * np.pi, 100)
z = x + 100

plt.ylim([0,1])
plt.xlim([0,1])
plt.fill_between(x, z, x/(u-1), color='black', facecolor='green', interpolate=True, alpha=0.3)
plt.fill_between(x, x, x, color='black', facecolor='green', interpolate=True, alpha=0.3)
plt.fill_between(x, x*(u-1), x-x , color='black', facecolor='red', interpolate=True, alpha=0.3)
plt.text( 0.6, 0.1, "Region A1", ha="center", family='sans-serif', size=11)
plt.text( 0.14, 0.65, "Region A2", ha="center", family='sans-serif', size=11)
plt.text( 0.6, 0.5, "y=x", ha="center", family='sans-serif', size=11)
plt.text( 0.55, 0.3, "y=x(u-1)", ha="center", family='sans-serif', size=11)
plt.text( 0.37, 0.6 , "y=x/(u-1)", ha="center", family='sans-serif', size=11)
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('../latex/img/pregunta3.pdf',  bbox_inches=0)
