# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:50:35 2018

@author: hean
"""
import pandas as pd
import math
import pylab as pl
from zigzag import *

x1 = []
x1_offset = 0

x2 = []
x2_offset = 0
gm_raws = []
gx_xraws = []
gx_raws = []
gy_raws = []
gz_raws = []
ppg_raws = []
line_nums = 0
gz_v_raws = []

last_header_serial = 0
first_header_flag = 1
header_serial = 0
header_acc_missed_cnt = 0
header_ppg_missed_cnt = 0
sensor_lost_cnt = 0
last_sensor_lost_cnt = 0
header_sensor_cnt     = 0
data_sensor_cnt       = 0

fpr = open(r'C:\Users\wbp\Downloads\liudonghong_HeartRate_static_5min_20191108_175958_0dbb2.txt','r', encoding="utf-8")
for line in fpr.readlines():
    line_array = line.split(' ')
    line_nums += 1

    array_cnt = len(line_array)
    # print(array_cnt)
    if(array_cnt != 27):
        continue
    #协议命令字
    if (int(line_array[7], 16) != 0xBB):
        continue
    # print(array_cnt)
    #可以控制数据开始和结束行
    if (line_nums < 100 ):
        continue

    # print(line_array[8], line_array[9], line_array[10], (int(line_array[8], 16) & 0xF0 ))
    # print(line_array)
    #get ppg data
    if (int(line_array[8], 16) & 0xF0 == 0x40):
        print(line_array[8], line_array[9], line_array[10])
        count = int(line_array[8], 16) & 0x3F
        # print(count)
        if count > 4:
            continue
        data_sensor_cnt += count
        for i in range(0, count):
            #print(line_array)
            ppg_value = (int(line_array[9 + i*4], 16) << 24 | int(line_array[10 + i*4], 16) << 16 |
                         int(line_array[11 + i * 4], 16) << 8 | int(line_array[12 + i * 4], 16))
            ppg_raws.append(ppg_value/1000)
            # fpw.write(str(ppg_value) + '\n')
            x1_offset += 1
            x1.append(x1_offset)
    
fpr.close()
# print(ppg_raws)
# print(peak_valley_pivots(ppg_raws, 0.03, -0.03))
arr = peak_valley_pivots(np.array(ppg_raws), 0.03, -0.03)

print(arr)
for i in range(x1_offset):
    arr[i] = abs(arr[i] * ppg_raws[i])
# fpw.close()
# plot_x_dot = pl.plot(x2, gx_raws, 'or', label="gx_raws")# use pylab to plot x and y
# plot_x_spline = pl.plot(x2, gx_raws, 'r')# use pylab to plot x and y
# plot_y_dot = pl.plot(x2, gy_raws, 'og', label="gy_raws")# use pylab to plot x and y
# plot_y_spline = pl.plot(x2, gy_raws, 'g')# use pylab to plot x and y
plot_z_dot = pl.plot(x1, ppg_raws, '.y-', label="gz_raws")# use pylab to plot x and y
plot_z_spline = pl.plot(x1, arr, 'ob')# use pylab to plot x and y



#plot_ppg_dot = pl.plot(x2, gx_xraws, 'oc', label="ppg_raws")# use pylab to plot x and y
#plot_ppg_spline = pl.plot(x2, gx_xraws, 'c')# use pylab to plot x and y

pl.legend(loc='upper left', numpoints=1)
pl.show()