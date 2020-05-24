import pandas as pd
import numpy as np
from consts import sensor_lat as lat
from consts import sensor_log as log
from consts import valid_sensor_res_10 as valid_sensor_list
from consts import valid_sensor_res_10_old as valid_sensor_list_old
from consts import sensor_day_seconds as day_seconds
from consts import sensor_week_seconds as week_seconds 
from consts import sensor_start_time_unix as start_time
from consts import sensor_end_time_unix as end_time
from consts import sensor_epoch_length as epoch_length
from consts import sensor_optimal_time_interval as optimal_time_interval
from consts import sensor_loc_pic as loc_pic
from consts import sensor_drop_list as drop_list

df_dict = {'rb_optimal':5959,'optimal':5959,'df_list':20160}

def dataset_write(data_list,key,df_dict=df_dict):
    filename = 'ds_'+key+'.h5'
    store = pd.HDFStore(filename)
    for i,item in enumerate(data_list):
        store[key+'_'+str(i)] = item
    store.close()
    return 1

def dataset_read(key,df_dict=df_dict):
    filename = 'ds_'+key+'.h5'
    return_list = []
    store = pd.HDFStore(filename)
    for i in range(df_dict[key]):
        return_list.append(store[key+'_'+str(i)])
    store.close()
    return return_list
