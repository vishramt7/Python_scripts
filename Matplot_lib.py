import numpy as np
import matplotlib.pyplot as plt

xvalues = np.linspace(-np.pi, np.pi, 300)
yvalues1 = np.sin(xvalues)
yvalues2 = np.cos(xvalues)
plt.plot(xvalues, yvalues1, lw=2, color='red', label='sin(x)')
plt.axhline(0, lw=0.5, color='black')
plt.axvline(0, lw=0.5, color='black')
#plt.show()
plt.savefig('temp.pdf')