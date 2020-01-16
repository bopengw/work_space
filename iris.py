# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:44:07 2019

@author: wbp
"""
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
iris_feature = iris.data
iris_target = iris.target

train_set = np.vstack((iris_feature[:45], iris_feature[51:96], iris_feature[101:146]))
train_setosa_label = np.zeros((45,1))
train_versicolor_label = np.zeros((45, 1))
train_virginica_label = np.ones((45, 1))
train_label = np.vstack((train_setosa_label, train_versicolor_label, train_virginica_label)).flatten()
#train_label = np.vstack((iris_target[:45], iris_target[51:96], iris_target[101:146])).flatten()

test_set = np.vstack((iris_feature[45:51], iris_feature[96:101], iris_feature[146:]))

log_model = LogisticRegression(solver='lbfgs', max_iter=500, multi_class='ovr')
# 训练逻辑回归模型
log_model.fit(train_set, train_label)

y_pred = log_model.predict(test_set)
print(log_model.coef_)
print(y_pred)

