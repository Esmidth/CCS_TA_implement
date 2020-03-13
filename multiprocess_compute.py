# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%

# %%
import pickle
import numpy as np
import pandas as pd
import os,sys
import utils
import matplotlib.pyplot as plt
from consts import sensor_lat as lat
from consts import sensor_log as log
from consts import valid_sensor_res_10 as valid_sensor_list
from numpy import array
import time
from multiprocessing import Pool
import multiprocessing as mp

# %%
# df = pd.read_hdf('data.h5','df_sub')


# %%
unix_column = 'Time since the epoch [s]'
idd = 'Station ID'


# %%
def coverage_test(df,time_stamps,valid_sensor_list):
    error = 0
    # all_np_list = []
    for i in range(len(time_stamps)-1):
        # print(i)
        # print(time_stamps[i],time_stamps[i+1])
        sub_df = df[(df[unix_column] > time_stamps[i]) & (df[unix_column] < time_stamps[i+1])]
        sensor_list = sub_df[idd].values
        uniq = np.unique(sensor_list)
        diff = np.setdiff1d(valid_sensor_list,uniq)    
        # np_court = all_np(sensor_list)
        # all_np_list.append(np_court)
        error += len(diff)
    return error


# %%
def compute(start_point,valid_sensor_list):
    df = pd.read_hdf('day.h5',str(start_point))
    epoch_length = 1800
    day_second = 86400
    week_second = 7*day_second
    start_time = time.time()
    time_stamps = np.arange(start_point,start_point+week_second+epoch_length,epoch_length)
    error_num = 0
    # all_np_list = []
    for i in range(len(time_stamps)-1):
        # print(i)
        # print(time_stamps[i],time_stamps[i+1])
        sub_df = df[(df[unix_column] > time_stamps[i]) & (df[unix_column] < time_stamps[i+1])]
        sensor_list = sub_df[idd].values
        uniq = np.unique(sensor_list)
        diff = np.setdiff1d(valid_sensor_list,uniq)    
        # np_court = all_np(sensor_list)
        # all_np_list.append(np_court)
        error_num += len(diff)
    now = time.gmtime(start_point)
    ratio = len(df) / error_num
    print("{0} \t {1}-{2}-{3}:\t {4}\t/{6} {7} \t {5}".format(start_point,now.tm_year,now.tm_mon,now.tm_mday,error_num,time.time()-start_time,len(df),ratio))
    return (start_point, now, error_num, len(df), ratio, time.time()-start_time)


if __name__ == "__main__":

# %%
    manager = mp.Manager()
    aggreateData = manager.dict()
    start = time.time()
    day_second = 86400
    week_second = 7*day_second
    start_list = np.arange(1162393768,1178747998+day_second,day_second)
    epoch_length = 1800
    # start_list = start_list[:3]
    output = open('data.pkl','wb')




    # %%
    results = []
    p = Pool(8)
    for start_point in start_list:
        # print('assign\t',str(start_point))
        result = p.apply_async(func=compute,args=(start_point,valid_sensor_list,))
        results.append(result)
    p.close()
    p.join()
    output_list = []
    for result in results:
        output_list.append(result.get())
    print('compute_time:',time.time()-start)
    pickle.dump(output_list,output)
    output.close()

