#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-15 16:03:02
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import os
import pytool
import numpy as np
import tensorflow as tf


# phase = 'train'
# phase = 'test'
phase = 'demo'
batch_size = 100
training_epochs = 100000
display_step = 1000
snapshot_step = 10000
learning_rate = 0.001

test_step = 90000
demo_step = 90000

snapshot_dir = './snapshot/mlp/ckpt/'
eventout_dir = './snapshot/mlp/graphs/'


# =======================prepare data=========================

rootdir = '../../data/mnist/'
# rootdir = '/home/liu/ws/tf/study/tfstudy/data/mnist/'

# read images(folder names are groundtruth labels) and scale from [0 ,255] --
if phase is 'train':
    X_train, Y_train = pytool.read_mnist(
        rootdir=rootdir, dataset='train',
        scale=True, isonehot=True, verbose=False)
    print("original shape ", X_train.shape)
    [nTrain, H, W] = X_train.shape
    X_train = np.reshape(X_train, (nTrain, H * W))
    print("reshape to ", X_train.shape)

    X_test, Y_test = pytool.read_mnist(
        rootdir=rootdir, dataset='test',
        scale=True, isonehot=True, verbose=False)
    print("original shape ", X_test.shape)
    [nTest, H, W] = X_test.shape
    X_test = np.reshape(X_test, (nTest, H * W))
    print("reshape to ", X_test.shape)

    X_val = X_test
    Y_val = Y_test

if phase is 'test':
    X_test, Y_test = pytool.read_mnist(
        rootdir=rootdir, dataset='test',
        scale=True, isonehot=True, verbose=False)
    print("original shape ", X_test.shape)
    [nTest, H, W] = X_test.shape
    X_test = np.reshape(X_test, (nTest, H * W))
    print("reshape to ", X_test.shape)

if phase is 'demo':
    X_demo, Y_demo = pytool.read_mnist(
        rootdir=rootdir, dataset='demo',
        scale=True, isonehot=True, verbose=True)
    print("original shape ", X_demo.shape)
    [nDemo, H, W] = X_demo.shape
    X_demo = np.reshape(X_demo, (nDemo, H * W))
    print("reshape to ", X_demo.shape)


C = 1
nClass = 10

# =======================build net=========================

dtype = tf.float32
# N-H-W-C
inlsize = H * W * C  # input layer size
hlssize = [256, 256, 32]  # hidden layers size
outlsize = nClass


X = tf.placeholder(dtype, [None, inlsize], name='X')
Y = tf.placeholder(dtype, [None, nClass], name='Y')

# init weights
W0 = tf.get_variable('W0', [inlsize, hlssize[0]], dtype=dtype,  # (nIL, nHL1)
                     initializer=tf.random_normal_initializer())
W1 = tf.get_variable('W1', [hlssize[0], hlssize[1]], dtype=dtype,  # (nHL1, nHL2)
                     initializer=tf.random_normal_initializer())
W2 = tf.get_variable('W2', [hlssize[1], hlssize[2]], dtype=dtype,  # (nHL2, nHL3)
                     initializer=tf.random_normal_initializer())
W3 = tf.get_variable('W3', [hlssize[2], outlsize], dtype=dtype,  # (nHL3, nOL)
                     initializer=tf.random_normal_initializer())
# init bias
b0 = tf.get_variable('b0', [hlssize[0]], dtype=dtype,  # (nHL1, )
                     initializer=tf.random_normal_initializer())
b1 = tf.get_variable('b1', [hlssize[1]], dtype=dtype,  # (nHL2, )
                     initializer=tf.random_normal_initializer())
b2 = tf.get_variable('b2', [hlssize[2]], dtype=dtype,  # (nHL3, )
                     initializer=tf.random_normal_initializer())
b3 = tf.get_variable('b3', [outlsize], dtype=dtype,  # (nHL4, )
                     initializer=tf.random_normal_initializer())

# input --> hidden layer1

F0 = tf.matmul(X, W0)  # (N, nIL) x (nIL, nHL1) --> (N, nHL1)
F0 = tf.add(F0, b0)
F0 = tf.nn.sigmoid(F0)
# hidden layer1 --> hidden layer2

F1 = tf.matmul(F0, W1)  # (N, nHL1) x (nHL1, nHL2) -->( N, nHL2)
F1 = tf.add(F1, b1)
F1 = tf.nn.sigmoid(F1)

# hidden layer2 --> hidden layer3

F2 = tf.matmul(F1, W2)  # (N, nHL2) x (nHL2, nHL3) -->( N, nHL3)
F2 = tf.add(F2, b2)
F2 = tf.nn.sigmoid(F2)

# hidden layer3 --> classify layer

F3 = tf.matmul(F2, W3)  # (N, nHL3) x (nHL3, nOL) -->( N, nOL)
F3 = tf.add(F3, b3)
F3 = tf.nn.sigmoid(F3)

Fo = F3

# =======================Loss Function=====================
entropy = tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=Fo)
loss_op = tf.reduce_mean(entropy, name='loss_op')

# =======================Optimizer=========================
optimizer = tf.train.AdamOptimizer(learning_rate)
train_op = optimizer.minimize(loss_op)

# =======================Evaluate==========================
labels = tf.argmax(Y, axis=1)
pred_labels = tf.argmax(Fo, axis=1)
print("==========")

correct_prediction = tf.equal(labels, pred_labels)
acc_op = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(labels.shape, pred_labels.shape)

# =======================Summaries=========================
# Create summaries to write on TensorBoard
with tf.name_scope('summaries'):
    tf.summary.scalar('loss_op', loss_op)
    tf.summary.scalar('accuracy', acc_op)
    tf.summary.histogram('histogram loss_op', loss_op)
    summary_op = tf.summary.merge_all()


def train():
    print("---------------Start Training------------------")

    writer = tf.summary.FileWriter(
        eventout_dir, tf.get_default_graph())

    # -------------Training cycle
    for epoch in range(training_epochs):
        avg_loss = 0.
        avg_acc = 0.
        total_batch = int(nTrain / batch_size)
        for batch in pytool.get_batches(X_train, Y_train, batch_size, shuffle=True):
            batch_xs, batch_ys = batch

            # Fit training using batch data
            _, lossv, accv, summaries = sess.run([train_op, loss_op,
                                                  acc_op, summary_op],
                                                 feed_dict={X: batch_xs, Y: batch_ys})
            avg_loss += lossv / total_batch
            avg_acc += accv / total_batch

            # xx = sess.run(X, feed_dict={X: batch_xs})
            # print(len(xx[0]), xx[0])

        # -------------display logs per display_step
        if epoch % display_step == 0:
            print("---------------Epoch:", '%04d' % (epoch + 1), " TRAIN: "
                  "avg loss=", "{:.3f}".format(avg_loss),
                  "avg acc=", "{:.3f}".format(avg_acc))

            lossv, accv = sess.run([loss_op, acc_op],
                                   feed_dict={X: X_val, Y: Y_val})
            print("---------------Epoch:", '%04d' % (epoch + 1), " VAL: "
                  "loss=", "{:.3f}".format(lossv),
                  "acc=", "{:.3f}".format(accv))

        # -------------snapshot
        if epoch % snapshot_step == 0:
            # Generate new checkpoint
            snapshot_file = snapshot_dir + "epoch"
            saver = tf.train.Saver(sharded=True)
            saver.save(sess, snapshot_file, global_step=epoch)

            # summaries
            writer.add_summary(summaries, global_step=epoch)

            print("Checkpoint of step " + str(epoch) + " saved!")
    writer.close()


def test():

    # Restore variables from checkpoint
    saver = tf.train.Saver()
    filename = "epoch-" + str(test_step)
    filepath = os.path.join(snapshot_dir, filename)
    saver.restore(sess, filepath)

    print("Checkpoint of step " + str(test_step) + " restored!")

    print("---------------Start Testing------------------")
    lossv, accv = sess.run([loss_op, acc_op],
                           feed_dict={X: X_test, Y: Y_test})
    print("---------------Testing loss=", "{:.3f}".format(lossv),
          "Testing acc=", "{:.3f}".format(accv))


def demo():

    # Restore variables from checkpoint
    saver = tf.train.Saver()
    filename = "epoch-" + str(demo_step)
    filepath = os.path.join(snapshot_dir, filename)
    saver.restore(sess, filepath)

    print("Checkpoint of step " + str(demo_step) + " restored!")

    print("---------------Start Demo------------------")
    lossv, accv, labelsv, pred_labelsv = sess.run([loss_op, acc_op, labels, pred_labels],
                                                  feed_dict={X: X_demo, Y: Y_demo})
    print("---------------Demo loss=", "{:.3f}".format(lossv),
          "Demo acc=", "{:.3f}".format(accv))
    print("groundtruth labels: ", labelsv)
    print("prediction labels: ", pred_labelsv)


if __name__ == '__main__':

    init = tf.initialize_all_variables()
    saver = tf.train.Saver(tf.global_variables())
    # with tf.Session() as sess:
    sess = tf.Session()
    sess.run(init)  # init graph

    if phase is 'train':
        train()
    if phase is 'test':
        test()
    if phase is 'demo':
        demo()
