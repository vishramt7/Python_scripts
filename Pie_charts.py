import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#fifa = pd.read_csv('../matplotlib_tut/matplotlib_tutorial/fifa_data.csv')
#left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
#right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
#labels = ['Left','Right']
#plt.pie([left, right], autopct='%.2f', labels=labels)

def func(pct, allvals):
        abs_val = int(round(pct/100*sum(allvals)))
#        return "{:.1f} ({:d})".format(pct,abs_val)
        return "{:d}".format(abs_val)

y = np.array([35, 25, 25, 15])
labels = ["Apples " + str(y[0]), "Bananas " + str(y[1]), "Cherries " + str(y[2]), "Peaches " + str(y[3])]
new_explode = [0.2, 0, 0, 0]
color_code = ["#F67280", "#C06C84", "#6C5B7B", "#355C7D"]
#003f5c
#58508d
#bc5090
#ff6361
#ffa600
plt.pie(y, 
        labels=labels, 
        startangle=90, 
        explode= new_explode, 
        colors=color_code,
#        autopct= '%.2f')
        autopct = lambda pct : func(pct, y),
        wedgeprops={'edgecolor' : 'white'},
        textprops=dict(color="k"))

#plt.legend(title="Fruits", bbox_to_anchor= (0.1,0.15,0,0.1))
#plt.annotate("New Apples"
#                xy = (0,0),
#                xytext = (0.1,0.1),
#                arrowprops=dict (arrowstyle="-", facecolor='black'))
#)


plt.style.use("fivethirtyeight")
plt.title("Fruits")
plt.tight_layout()
plt.show()
#plt.savefig('New_Piechart.png', dpi = 300)
#plt.legend()