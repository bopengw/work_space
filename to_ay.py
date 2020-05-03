


import pickle
import gzip
import numpy as np

def load_data():
    f = gzip.open(r'C:\work\work_space\MNIST_data\train-images-idx3-ubyte.gz', 'rb')
    # pickle .load(f)
    training_data = f.read()
    f.close()
    return training_data

# res = load_data()
# print(res)

with gzip.open(r'C:\work\work_space\MNIST_data\train-labels-idx1-ubyte.gz', 'rb') as f:
    training_data = f.read()
    st = int.from_bytes(training_data, byteorder='big', signed=False)