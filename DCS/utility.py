import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import consts
import h5py
import pandas as pd
import numpy as np
from consts import sensor_data_index as data_index
from consts import sensor_df_dict as df_dict
from consts import sensor_idd as idd
from consts import sensor_unix_column as unix_column
from consts import sensor_a_temperature as a_temperature
from consts import sensor_s_temperature as s_temperature



def dataset_read(key,df_dict=df_dict):
    filename = 'ds_'+key+'.h5'
    return_list = []
    store = pd.HDFStore(filename)
    for i in range(df_dict[key]):
        return_list.append(store[key+'_'+str(i)])
    store.close()
    return return_list


def dataset_write(data_list,key,df_dict=df_dict):
    filename = 'ds_'+key+'.h5'
    store = pd.HDFStore(filename)
    for i,item in enumerate(data_list):
        store[key+'_'+str(i)] = item
    store.close()
    return 1


def get_h5_data():
    with h5py.File('dataset.h5','r') as f:
        a_temperature_mean = f[data_index[0]][:]
        a_temperature_std = f[data_index[1]][:]
        a_temperature_array = f[data_index[2]][:]
        sub_df_list_optimal_index = f[data_index[3]][:]
        time_stamp = f[data_index[4]][:]
    return a_temperature_array,a_temperature_mean,a_temperature_std,sub_df_list_optimal_index,time_stamp

def remove_duplicated(df):
    '''剔除dataframe中的重复项，以Station ID为基准'''
    sub_df = df[-df[idd].duplicated()]
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