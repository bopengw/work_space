import pylab as pl
import numpy as np
import pandas as pd
import data_analysis as data_analysis


if __name__ == '__main__':
    path = r'C:\Users\99087\Downloads\qinjiaxian_StepCount_Walking_1000steps_20200320_153842_58cc4.txt'
    sensor_data = data_analysis.data_analysis(path)
    fig = pl.figure('acc')
    pl.plot(np.arange(len(sensor_data['acc_x'])), sensor_data['acc_x'], 'or-')
    pl.plot(np.arange(len(sensor_data['acc_x'])), sensor_data['acc_y'], 'og-')
    pl.plot(np.arange(len(sensor_data['acc_x'])), sensor_data['acc_z'], 'ob-')
    fig = pl.figure('ppg')
    pl.plot(np.arange(len(sensor_data['ppg'])), sensor_data['ppg'], 'ob-')
    pl.show()