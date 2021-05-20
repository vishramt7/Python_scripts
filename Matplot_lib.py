import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# This changes the size of the plot
#plt.figure(figsize=(2,2), dpi=300)
xvalues = np.linspace(-np.pi, np.pi, 20)
yvalues1 = np.sin(xvalues)
yvalues2 = np.cos(xvalues)
#plt.plot(xvalues, yvalues1, lw=2, color='red', label='sin(x)')
#plt.axhline(0, lw=0.5, color='black')
# plt.axvline(0, lw=0.5, color='black')
#plt.plot (xvalues,yvalues1, 'r.--', label='sinx')
#plt.plot (xvalues,yvalues2, 'b.--', label='cosx')

#plt.show()
#plt.savefig('temp.png', dpi = 300)
#plt.savefig('output.png')

# bar plot
#labels = ['A', 'B', 'C']
#values = [ 1, 4, 2]
#bar = plt.bar(labels, values)
#bar[0].set_hatch('/')
#plt.show()

#line graph
#gas = pd.read_csv('gas_prices.csv')
#for country in gas:
#    if country != 'Year':
#        print(country)
#        plt.plot(gas.Year, gas[country], marker='.', label=country)

#plt.plot(gas.Year, gas.USA, 'b.-',label='Unites States')
#plt.plot(gas.Year, gas.Canada, 'r.--', label='Canada')
#plt.legend()
#plt.xticks(gas.Year[::3])

#Histogram
fifa = pd.read_csv('../matplotlib_tut/matplotlib_tutorial/fifa_data.csv')
#print (fifa.head(5))
histo_bins = list(range(0,110,10))
print(histo_bins)
plt.hist(fifa.Overall, bins=histo_bins )
plt.xticks(histo_bins)
plt.show()
#print(gas)