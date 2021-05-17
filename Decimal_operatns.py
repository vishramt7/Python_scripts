import numpy as np
import math
from decimal import *
a = [1.2]
b = [1.0]
x = np.array (a)
y = np.array (b)
#print (format (math.pi,'0.12f'))
#print ("I like", np.pi)
#print (type(a))

x = 2.675
y = 3.12
#print (round(x, 2))
# Convert the operation to string and use it with Decimal
print( Decimal (str ( x * y)) )