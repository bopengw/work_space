import numpy as np
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
a = tf.constant(2)
sess = tf.Session()
print(sess.run(a))