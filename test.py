# import tensorflow as tf
# import numpy as np
# #只用cpu
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"
# a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
# b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
# c = tf.matmul(a, b)
# # with device('\gpu1'):
# sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# print(sess.run(c))

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())