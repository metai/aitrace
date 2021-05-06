import tensorflow as tf
import numpy as np


a = np.arange(12)
print(a)
b = np.random.shuffle(a)
print(a)
print(b)
a = np.arange(12)
print(a)
b = np.random.permutation(a)
print(b)
print(a)

def llll():

    with tf.variable_scope('name') as scope:
        v1 = tf.get_variable(
            'v1', shape=[3], initializer=tf.ones_initializer())
        v2 = tf.get_variable('v2', shape=[5], initializer=tf.random_uniform_initializer(
            maxval=-1., minval=1., seed=0))
        # 向当前计算图中添加张量集合
        tf.add_to_collection('v', v1)
        tf.add_to_collection('v', v2)
