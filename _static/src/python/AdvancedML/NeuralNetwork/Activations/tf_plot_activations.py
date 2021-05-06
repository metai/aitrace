#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-06 10:28:33
# @Author  : Yan Liu & Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# activations = ['linear', 'sigmoid', 'tanh', 'softplus', 'softsign',
activations = ['tanh', 'sigmoid', 'softplus', 'softsign',
               'elu', 'relu', 'selu', 'swish', 'relu6', 'leaky_relu']

activation = 'swish'

x = np.linspace(-10, 10, 200)

y = np.tanh(x)

sess = tf.Session()
X = tf.placeholder(tf.float32, (None,), name='X')

# Y = tf.nn.sigmoid(X)
# Y = tf.nn.tanh(X)
# Y = tf.nn.softplus(X)
# Y = tf.nn.softsign(X)
# Y = tf.nn.elu(X)
# Y = tf.nn.relu(X)
# Y = tf.nn.selu(X)
# Y = tf.nn.crelu(X)
# Y = tf.nn.relu6(X)
# Y = tf.nn.leaky_relu(X)
Y = tf.nn.swish(X)

y = sess.run(Y, feed_dict={'X:0': x})

plt.figure()
plt.plot(x, y, 'r')
plt.title(activation + ' activation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
