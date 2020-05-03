import numpy as np
import pandas as pd
import json
from sklearn import datasets
import pylab as pl
import random
import math

class LR():
    def __init__(self, size):
        self.weight = np.random.random([size + 1, 1])
        self.biases = np.random.random(1)
        print(self.weight.shape)

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def diff(self, f):
        return (1 - f) * f

    def train(self, feature, label, max_cycle, ratio):
        for i in range(max_cycle):
            f = self.sigmoid(feature.dot(self.weight))
            error = label.reshape(-1, 1) - f
            self.weight = self.weight + ratio * feature.T.dot(error)
            if i % 30 == 0:
                print(self.error_rate(f, label.reshape(-1,1)))
        print(self.accuracy(feature, label.reshape(-1,1)))
        return self.weight

    def save(self, filename):
        data = {"weight": [w.tolist() for w in self.weight]}
        f = open(filename, "w")
        json.dump(data, f)
        f.close()
    def accuracy(self, x, y):
        predict = self.sigmoid(x.dot(self.weight))
        print(predict)
        predict = predict > 0.5
        return sum(y == predict)/len(y)
    def error_rate(self, h, label):
        m = np.shape(h)[0]
        sum_err = 0

        for i in range(m):
            if h[i, 0] > 0 and 1-h[i, 0] > 0:
                sum_err -=(label[i, 0]*np.log(h[i, 0]) + (1 - label[i, 0]) * np.log(1 - h[i, 0]))
            else:
                sum_err -= 0
        return sum_err/m


class kmeans():

    def distance(self, arr1, arr2):
        if len(arr1) != len(arr2):
            print('input must equal')
            return
        return np.sqrt(sum((arr1 - arr2) ** 2))
    def center(self, arr, k):
        rows, columns = arr.shape
        center = np.zeros((k,columns))
        rand = random.sample(range(0, rows), k)
        for i in range(k):
            center[i, :] = arr[rand[i], :]
        return center
    def train(self, arr, k):
        rows = arr.shape[0]
        cluster_assment = np.zeros([rows, 2])
        center = self.center(arr, k)
        for i in range(rows):
            min_dist = 1000000
            min_index = -1
            dist = 0
            for j in range(k):
                dist = self.distance(arr[i, :], center[j, :])
                if dist < min_dist:
                    min_dist = dist
                    min_index = j
            center[min_index, :] = (center[min_index, :] + arr[i, :]) / 2
            cluster_assment[i, :] = min_index, dist
        return center, cluster_assment

    def show_cluster(self, arr, k, center, cluster_assment):
        mark = ['or', 'oc', 'ob']
        for i in range(arr.shape[0]):
            pl.plot(arr[i, 0], arr[i, 1], mark[int(cluster_assment[i, 0])])
        pl.show()


import numpy as np
import pandas as pd
import random
import sys
import time


class KMeansClusterer:
    def __init__(self, ndarray, cluster_num):
        self.ndarray = ndarray
        self.cluster_num = cluster_num
        self.points = self.__pick_start_point(ndarray, cluster_num)

    def cluster(self):
        result = []
        for i in range(self.cluster_num):
            result.append([])
        for item in self.ndarray:
            distance_min = sys.maxsize
            index = -1
            for i in range(len(self.points)):
                distance = self.__distance(item, self.points[i])
                if distance < distance_min:
                    distance_min = distance
                    index = i
            result[index] = result[index] + [item.tolist()]
        new_center = []
        for item in result:
            new_center.append(self.__center(item).tolist())
        # 中心点未改变，说明达到稳态，结束递归
        if (self.points == new_center).all():
            return result

        self.points = np.array(new_center)
        return self.cluster()

    def __center(self, list):
        '''计算一组坐标的中心点
        '''
        # 计算每一列的平均值
        return np.array(list).mean(axis=0)

    def __distance(self, p1, p2):
        '''计算两点间距
        '''
        tmp = 0
        for i in range(len(p1)):
            tmp += pow(p1[i] - p2[i], 2)
        return pow(tmp, 0.5)

    def __pick_start_point(self, ndarray, cluster_num):

        if cluster_num < 0 or cluster_num > ndarray.shape[0]:
            raise Exception("簇数设置有误")

        # 随机点的下标
        indexes = random.sample(np.arange(0, ndarray.shape[0], step=1).tolist(), cluster_num)
        points = []
        for index in indexes:
            points.append(ndarray[index].tolist())
        return np.array(points)

class node():
    def __init__(self, fea=-1, value=None, results=None, right=None, left=None):
        self.fea = fea
        self.value = value
        self.results = results
        self.right = right
        self.left = left

    def build_tree(self, data):
        if len(data) == 0:
            return node()

        current_gini = ()

        best_gini = 0.0
        best_criteria = None
        best_sets = None
        feature_num = len(data[0]) - 1
        for fea in range(feature_num):
            feature_values = {}
            for sample in data:
                feature_values[sample[fea]] = 1

            for value in feature_values.keys():
                (set1, set2) = split_tree(data, fea, value)
                now_gini = float(len(set1)*cal_gini_index(set1) + len(set2)*cal_gini_index(set2))/len(data)
                gain = current_gini - now_gini

                if gain > best_gini and len(set1) > 0 and len(set2) > 0:
                    best_gini = gain
                    best_criteria = (fea, value)
                    best_sets = (set1, set2)
        if best_gini > 0:
            right = self.build_tree(best_sets[0])
            left = self.build_tree(best_sets[1])
            return node(fea=best_criteria[0], value=best_criteria[1], right=right, left=left)
        else:
            return node(results=label_uniq_cnt(data))

def calc_entropy(data):
    num_entries = len(data)
    label_cnt = {}
    for feature in data:
        current_label = feature[-1]
        if current_label not in label_cnt.keys():
            label_cnt[current_label] = 0
        label_cnt[current_label] += 1
    entropy = 0.0
    for key in label_cnt:
        prob = float(label_cnt[key]) / num_entries
        entropy -= prob * math.log(prob, 2)
    return entropy
if __name__ == '__main__':
    iris = datasets.load_iris()
    #lr
    # iris_feature = iris.data[:100, :2]
    # iris_target = iris.target[:100]
    # lg = LR(2)
    # bias = np.ones([100, 1])
    # iris_feature = np.c_[iris_feature, bias]
    # weight = lg.train(iris_feature, iris_target, 300, 0.3)
    # pl.plot(iris_feature[:, 0], iris_feature[:, 1], 'oc')
    # pl.plot(np.arange(10), [(186.2868641 * i -48.67551809) / 314.55294802 for i in range(10)], 'om-')
    # pl.show()

    #kmeans
    iris_feature = iris.data[:, 1:3]
    kmeans = kmeans()
    # center, cluster_assment = kmeans.train(iris_feature, 3)
    # kmeans.show_cluster(iris_feature, 3, center, cluster_assment)
    kmean_alg = KMeansClusterer(iris_feature, 3)
    kmean_alg.cluster()
