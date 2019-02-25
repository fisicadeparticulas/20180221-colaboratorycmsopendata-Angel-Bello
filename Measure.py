import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

X = pd.read_csv('Sample5.csv')
X.head()

len (X)
plt.figure(1)
plt.title('Masa Invariante Sample 5')

plt.hist(X.MT, 50,range = (0,150), color = "red")
plt.xlabel('Masa Transversa $m^2=(E)^2-(p)^2$')
plt.ylabel('Numero de eventos')
plt.savefig('GraficaMT.jpg')
plt.figure(2)
plt.hist(X.TMI, 300, range = (0,100))
plt.xlabel('Masa Transversa Invariante $m=sqrt((E)^2-(ip)^2)$')
plt.ylabel('Numero de eventos')
plt.savefig('GraficaMTI.jpg')
plt.show()
