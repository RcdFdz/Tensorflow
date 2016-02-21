import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import seaborn as sns

num_puntos = 2000
conjunto_puntos = []
for I in xrange(num_puntos):
  if np.random.random() > 0.5:
    conjunto_puntos.append([np.random.normal(0.0,0.9), np.random.normal(0.0,0.9)])
  else:
    conjunto_puntos.append([np.random.normal(3.0,0.5), np.random.normal(1.0,0.5)])

df = pd.DataFrame({"x": [v[0] for v in conjunto_puntos], "y": [v[1] for v in conjunto_puntos]})
sns.lmplot("x", "y", data=df, fit_reg=False,size=6)
plt.show()


'''
plt.plot(conjunto_puntos,'ro', label = 'Odata')
plt.legend()
plt.show()
'''
