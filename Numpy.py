import numpy as np
a = np.full((2,2), 99)
a[0] = 1
print(a)
b = np.genfromtxt('data_frame.csv', delimiter =',')
print(b[b>1])