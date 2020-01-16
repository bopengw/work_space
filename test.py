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

# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())

# import cv2
#
# img = cv2.imread(r'C:\Users\wbp\Desktop\59.png')
# [h, w, c] = img.shape
# print(h, w, c)
import pandas as pd
import numpy as np
# import subprocess
#
# EXE = r'C:\work\work_for_C\cmake-build-debug\work_for_C.exe'
# subprocess.call([EXE, '1', '2'])
import hashlib, json

block_genesis = {
    'prev_hash': None,
    'transactions': [1, 3, 4, 2]
}

block_genesiss = json.dumps(block_genesis, sort_keys=True).encode('utf-8')
block_genesis_hash = hashlib.sha256(block_genesiss).hexdigest()
print(block_genesis_hash)

