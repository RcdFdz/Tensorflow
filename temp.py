import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def human():
  iq = np.random.normal(100,15)
  return iq

def descendent(parent1, parent2):
  mean_iq = np.mean([parent1,parent2])
  iq = np.random.normal(mean_iq, 15)
  return iq

human_evolution = [descendent(human(),human())]
time = [0]
conjunto_puntos = []

for t in xrange(1,1000):
  human_evolution.append(descendent(human_evolution[-1],human()))
  time.append(t)
  conjunto_puntos.append([time[-1], human_evolution[-1]])

x = [v[0] for v in conjunto_puntos]
y = [v[1] for v in conjunto_puntos]

x = np.array(x)
y = np.array(y)

res = stats.theilslopes(y, x, 0.999)
lsq_res = stats.linregress(x, y)

print res
print lsq_res

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, 'b.')
ax.plot(x, res[1] + res[0] * x, 'r-')
ax.plot(x, res[1] + res[2] * x, 'r--')
ax.plot(x, res[1] + res[3] * x, 'r--')
ax.plot(x, lsq_res[1] + lsq_res[0] * x, 'g-')
plt.show()
