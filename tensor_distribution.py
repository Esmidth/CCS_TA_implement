import numpy as np
import pandas as pd
import os,sys
import utilities
import matplotlib.pyplot as plt
from numpy import array
from multiprocessing import Pool
import multiprocessing as mp
from consts import sensor_lat as lat
from consts import sensor_log as log
from consts import valid_sensor_res_10 as valid_sensor_list
from consts import valid_sensor_res_10_old as valid_sensor_list_old
from consts import sensor_day_seconds as day_seconds
from consts import sensor_week_seconds as week_seconds 
from consts import sensor_start_time_unix as start_time
from consts import sensor_end_time_unix as end_time
from consts import sensor_epoch_length as epoch_length
from consts import sensor_loc_pic as loc_pic
from consts import sensor_drop_list as drop_list
import consts
import time
import pickle
import copy

unix_column = 'Time since the epoch [s]'
idd = 'Station ID'
a_temperature = 'Ambient Temperature'
s_temperature = 'Surface Temperature'

def remove_duplicated(df,drop_list=drop_list):
    '''剔除dataframe中的重复项，以Station ID为基准'''

    sub_df = df[-df[idd].duplicated()]
    for i in drop_list:
        sub_df = sub_df[-(sub_df[idd] == i)]
    return sub_df

def dataframe_to_matrix(df,loc,drop_list):
    temper = np.copy(loc)
    # print(temper)
    temper = temper.reshape(100)
    for i in range(len(temper)):
        if int(temper[i]) != 0 and int(temper[i]) not in drop_list:
            v = df[df[idd] == temper[i]][a_temperature].values
            index = df[df[idd] == temper[i]].index.tolist()
            # print(temper[i],v)
            if len(v) == 1 and np.isnan(v[0]) == False:
                # print(v[0])
                temper[i] = v[0]
            else:
                temper[i] = 0
            # print(index)
            # print(df.loc(index,a_temperature))
        else:
            temper[i] = 0
    temper = temper.reshape(10,10)
    # print(temper)
    return temper

if __name__ == '__main__':
    df = pd.read_hdf('optimal.h5','optimal_df')

    uniq_list = []
    time_gaps = [30]
    # time_gaps = np.arange(50,3600,50)
    sum_list = np.zeros_like(time_gaps)
    for j,time_gap in enumerate(time_gaps):
        time_stamp = np.arange(start_time,end_time+time_gap,time_gap)
        uniq_sub_df_list = []
        for i in range(len(time_stamp)-1):
            # print(time_stamp[i],time_stamp[i+1])
            sub_df = df[(df[unix_column] >= time_stamp[i]) & (df[unix_column] < time_stamp[i+1])]
            uniq_sub_df = remove_duplicated(sub_df)
            if len(uniq_sub_df) == 45:
                sum_list[j] += 1
            else:
                # print(i)
                pass
            uniq_sub_df_list.append(len(uniq_sub_df))
        uniq_sub_df_list = np.array(uniq_sub_df_list)
        uniq_list.append(uniq_sub_df_list)
        print(j,sum_list[j],time_gap,len(time_stamp))
        # print(len(time_stamp))
    uniq_list = np.array(uniq_list)
    for i,time in enumerate(uniq_list):
        print('-------------------')
        print(time_gaps[i])
        print(time.mean(axis=0))
        print(time.std(axis=0))
        print(sum_list[i])
