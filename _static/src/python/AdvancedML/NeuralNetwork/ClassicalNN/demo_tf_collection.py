import tensorflow as tf
import util

variables = tf.global_variables()

print(variables)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # 返回当前计算图中手动添加的张量集合
    v = tf.get_collection(tf.global_variables('v'))
    print(v)
    print(v[0].eval())
    print(v[1].eval())
