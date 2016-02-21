import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

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
x = 0

for t in xrange(1,100):
  human_evolution.append(descendent(human_evolution[-1],human()))
  time.append(t)
  conjunto_puntos.append([time[-1], human_evolution[-1]])


x_data = [v[0] for v in conjunto_puntos]
y_data = [v[1] for v in conjunto_puntos]

W = tf.Variable(tf.random_uniform([1], 0, 100))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

loss = tf.reduce_mean(tf.square(y - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for step in range(100):
  sess.run(train)

plt.plot(time,human_evolution, 'ro')
plt.plot(x_data, sess.run(W)*x_data+sess.run(b))
plt.xlabel('t')
plt.ylabel('iq')
plt.legend()
plt.show()
