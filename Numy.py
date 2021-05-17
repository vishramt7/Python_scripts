import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

b = [5, 6, 7]
a = np.array([2, 3, 4])
c = np.ones((2,4), dtype=np.int64)
#print (a[0], b[0], c[0][1])
#print (np.sort(c))

rng = np.random.default_rng(0)
Z = rng.integers(5, size=(2, 4))
print (Z)

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
uniq_a = np.unique(a)
for j in uniq_a:
    print (j)

np.savetxt ('array_save.csv', uniq_a)
print (np.loadtxt ('array_save.csv'))

panda_check = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
                [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
                [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
                [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])

#dataframe = pd.DataFrame(panda_check)
#print(dataframe)
#dataframe.to_csv('data_frame.csv')
#plt.plot(a)
#plt.show()
#x = np.linspace(0, 5, 20)
#y = np.linspace(0, 10, 20)
#plt.plot(x, y, 'purple') # line
#plt.plot(x, y, 'o')
#plt.show()

list = [2, 3, 4, 5]
#print (list.dtype)

numpy_list = np.array(list)
#print (numpy_list.dtype)

a = np.array( [20,30,40,50] )
#print (10*np.sin(a))
print (a[1:3])

z = np.arange(2, 7, 1)**2
index_z = np.arange(2)
#print (z[index_z])
print(type(z))
