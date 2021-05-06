import tensorflow as tf


H, W, C = (256, 256, 3)

nClasses = 10

X = tf.placeholder("float", [None, H, W, C], 'inputs')
Y = tf.placeholder("float", [None, nClasses], 'labels')


tf.nn.conv2d()

weights = tf.get_variable('weights', shape = [kernel_height, kernel_height, input_channels/groups, num_kernels])
biases = tf.get_variable('biases', shape = [num_kernels])

conv1 = self.conv(self.input_x, 11, 96, 4, name='conv1', padding='VALID')
pool1 = self.maxPooling(
    conv1, filter_size=3, stride=2, name='pool1', padding='VALID')
norm1 = self.lrn(pool1, 2, 2e-05, 0.75, name='norm1')
# layer 2
conv2 = self.conv(norm1, 5, 256, 1, name='conv2', padding_num=0, groups=2)
pool2 = self.maxPooling(
    conv2, filter_size=3, stride=2, name='pool2', padding='VALID')
norm2 = self.lrn(pool2, 2, 2e-05, 0.75, name='norm2')
# layer 3
conv3 = self.conv(norm2, 3, 384, 1, name='conv3')
# layer 4
conv4 = self.conv(conv3, 3, 384, 1, name='conv4', groups=2)
# layer 5
conv5 = self.conv(conv4, 3, 256, 1, name='conv5', groups=2)
pool5 = self.maxPooling(
    conv5, filter_size=3, stride=2, name='pool5', padding='VALID')
# layer 6
flattened = tf.reshape(pool5, [-1, 6 * 6 * 256])
fc6 = self.fc(input=flattened, num_in=6 * 6 * 256, num_out=4096,
              name='fc6', drop_ratio=1.0 - self.keep_prob, relu=True)
# layer 7
fc7 = self.fc(input=fc6, num_in=4096, num_out=4096, name='fc7',
              drop_ratio=1.0 - self.keep_prob, relu=True)
# layer 8
self.fc8 = self.fc(input=fc7, num_in=4096,
                   num_out=self.num_classes, name='fc8', drop_ratio=0, relu=False)
