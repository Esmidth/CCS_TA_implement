import numpy as np
import torch.optim as optim
import pandas as pd

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