import numpy as np
import pandas as pd
import pylab as pl

def data_analysis(path):
    acc_x = []
    acc_y = []
    acc_z = []

    ppg = []
    fpr = open(path, 'r', encoding='utf-8')
    for line in fpr.readlines():
        line_arr = line.split(' ')

        if len(line_arr) != 27:
            continue

        if line_arr[7] == 'bb':
            if line_arr[8] == '12' and line_arr[9] == '01':
                # print('this is data_header')
                continue

            if int(line_arr[8], 16) & 0xf0 == 0x80:
                acc_cnt = int(line_arr[8], 16) & 0x0f
                for i in range(acc_cnt):
                    acc_x.append(int(line_arr[9 + 6 * i], 16) << 8 | int(line_arr[10 + 6 * i], 16) - 128)
                    acc_y.append(int(line_arr[11 + 6 * i], 16) << 8 | int(line_arr[12 + 6 * i], 16) - 128)
                    acc_z.append(int(line_arr[13 + 6 * i], 16) << 8 | int(line_arr[14 + 6 * i], 16) - 128)
                continue

            if int(line_arr[8], 16) & 0xf0 == 0x40:
                ppg_cnt = int(line_arr[8], 16) & 0x0f
                for i in range(ppg_cnt):
                    ppg.append(int(line_arr[9 + 4 * i], 16) << 24 | int(line_arr[10 + 4 * i], 16) << 16 |
                               int(line_arr[11 + 4 * i], 16) << 8 | int(line_arr[12 + 4 * i], 16))
                continue
    sensor_data = {'acc_x': acc_x, 'acc_y': acc_y, 'acc_z': acc_z, 'ppg': ppg}

    return sensor_data


def plot(sensor_data):
    pl.figure('test')
    pl.plot(np.arange(len(sensor_data['acc_x'])), sensor_data['acc_x'], 'or-')
    pl.plot(np.arange(len(sensor_data['acc_y'])), sensor_data['acc_y'], 'og-')
    pl.plot(np.arange(len(sensor_data['acc_y'])), sensor_data['acc_z'], 'ob-')
    pl.show()




# fpr = open(r'C:\Users\99087\Downloads\qinjiaxian_StepCount_Walking_1000steps_20200320_153842_58cc4.txt')
# print(fpr)

if __name__ == '__main__':
    path = r'C:\Users\99087\Documents\WeChat Files\BPW-Rain\FileStorage\File\2020-04\zouwenxun_StepCount_FastWalk_10min_20200428_214545_afe02.txt'
    data = data_analysis(path)
    plot(data)