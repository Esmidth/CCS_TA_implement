import numpy as np
import torch.optim as optim
import pandas as pd
import matplotlib.pyplot as plt
from consts import res,lat,log
# Latitude 维度
# Longitude 经度

def get_data(dataset):
    """return pandas.Dataframe"""
    prefix = 'Dataset/'
    if dataset == 'rat':
        filename = 'Rat_Sightings.csv'
    if dataset == 'noise':
        filename = 'Noise_Complaints_Heatmap.csv'
    return pd.read_csv(prefix+filename)

def data_structure_conversion(dataset,df):
    if dataset == 'rat':
        pass

def generate_date_dataframe(date_range,df):
    """date_range: (from,to)"""
    return df[(df['New_Date'] > str(date_range[0])) & (df['New_Date'] < str(date_range[1]))]


def draw_rat_heatmap(df,res,lat=lat,log=log):
    lat_range = np.linspace(lat[0],lat[1],res+1)
    log_range = np.linspace(log[0],log[1],res+1)
    pic = np.zeros((res,res))
    for i in range(res):
        # print(i,lat_range[i],lat_range[i+1])
        for j in range(res):
            sub_df = df[(df['Latitude'] > lat_range[i]) & (df['Latitude'] < lat_range[i+1]) & (df['Longitude'] > log_range[j]) & (df['Longitude'] < log_range[j+1])]
            pic[i][j] = len(sub_df)
    return pic

def draw_pics(pic_list,arrange=(1,8),init_name=2010,figsize=(8,8),filename=None):
    plt.figure(figsize=figsize)
    x = arrange[0]
    y = arrange[1]
    if x * y < len(pic_list):
        x = 1
        y = len(pic_list)
    for i,pic in enumerate(pic_list):
        plt.subplot(x,y,i+1)
        plt.imshow(pic)
        if type(init_name) == int:
            plt.title(str(init_name+i))
        else:
            plt.title(init_name)
    plt.tight_layout()
    
    if(filename == None):
        plt.show()
    else:
        plt.savefig(filename,dpi=300)

def get_year_heatmap(date_range,df,res=res):
    """date_range: (start_year,end_year)"""
    date_df_list = []
    date_range_verbose = np.linspace(date_range[0],date_range[1],date_range[1]-date_range[0]+1,dtype=int)
    # print(date_range_verbose)
    for i in range(date_range[1]-date_range[0]):
        # print(date_range_verbose[i],date_range_verbose[i+1])
        sub_df = generate_date_dataframe((date_range_verbose[i],date_range_verbose[i+1]),df)
        date_df_list.append(sub_df)
    pic_list = []
    for date_df in date_df_list:
        pic = draw_rat_heatmap(date_df,res,lat,log)
        pic_list.append(pic)
    return pic_list

def draw_rat_heatmaps(df_list,res=res,lat=lat,log=log):
    """df_list : dataframe_list"""
    pic_list = []
    for df in df_list:
        pic = draw_rat_heatmap(df,res,lat,log)
        pic_list.append(pic)
    return pic_list

def get_year_dataframes(df,year:int):
    """返回的列表中含有一年中以月为单位的dataframe"""
    month_list = np.linspace(1,12,12,dtype=int)
    month_list = np.array(month_list,dtype=str)
    str_list = []
    for i in month_list:
        str_list.append(str(year)+'-'+i)
    str_list.append(str(year+1)+'-1')
    df_list = []
    for i in range(12):
        tmp = generate_date_dataframe((str_list[i],str_list[i+1]),df)
        df_list.append(tmp)
    return df_list