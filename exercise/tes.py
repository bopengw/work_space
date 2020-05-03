import exercise.network as network
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
from sklearn import datasets
import tensorflow as tf
# mnist = tf.keras.datasets.mnist # 包含了很多数据集，第一次使用需要下载
# (X_train, y_train), (X_test, y_test) = mnist.load_data()
# print(X_train.shape) # out: (60000, 28, 28)
# print(y_train.shape) # out: (60000,)


mnist = input_data.read_data_sets(r'C:\work\work_space\MNIST_data', one_hot=False)
# train_data = mnist.train.images   #所有训练数据
# val_data = mnist.validation.images  #(5000,784)
# test_data = mnist.test.images
#
# train_data = np.c_[train_data, mnist.train.labels]
# test_data = np.c_[test_data, mnist.test.labels]

iris = datasets.load_iris()
iris_feature = iris.data
iris_target = iris.target
iris_data = np.c_[iris_feature, iris_target]
print(iris_data.shape, iris_data[:5,:])
net = network.net([4, 1])
net.SGD(iris_data, 10, 10, 1.5, test_data=iris_data)