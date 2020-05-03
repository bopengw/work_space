#SVM多分类
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets(r'C:\work\work_space\MNIST_data', one_hot=True)
train_data = mnist.train.images   #所有训练数据
val_data = mnist.validation.images  #(5000,784)
test_data = mnist.test.images

# Third-party libraries

from sklearn import svm

def svm_baseline():
    mnist = input_data.read_data_sets(r'C:\work\work_space\MNIST_data', one_hot=False)
    training_data = mnist.train.images  # 所有训练数据
    val_data = mnist.validation.images  # (5000,784)
    test_data = mnist.test.images

    # train

    clf = svm.SVC()

    clf.fit(training_data, mnist.train.labels)

    # test

    predictions = [int(a) for a in clf.predict(test_data)]

    num_correct = sum(int(a == y) for a, y in zip(predictions, mnist.test.labels))

    print("Baseline classifier using an SVM.")

    print("%s of %s values correct." % (num_correct, len(test_data)))



if __name__ == "__main__":

    svm_baseline()