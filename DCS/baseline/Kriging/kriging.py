import numpy as np
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging


class OrdryKriging(object):
    def __init__(self):
        super().__init__()
    
    def train(self,data_matrix):
        self.data_matrix = data_matrix
        zero_index = np.where(data_matrix.flatten() == 0)[0]
        non_zero_index = np.where(data_matrix.flatten() != 0)[0]

        spatial_length = data_matrix.shape[0]
        temporal_length = data_matrix.shape[1]

        temporal_index = non_zero_index % temporal_length
        spatial_index = non_zero_index / temporal_length
        spatial_index = spatial_index.astype(int)


        non_zero_values = data_matrix.flatten()[non_zero_index]

        OK = OrdinaryKriging(spatial_index,temporal_index,non_zero_values,variogram_model='linear'
        ,verbose=False,enable_plotting=False,coordinates_type='geographic')
        self.model = OK


        # self.t_index = t_index
        self.t_temporal_index = np.arange(0,temporal_length,1)
        self.t_spatial_index = np.arange(0,spatial_length,1)
        # print(self.t_temporal_index)
        # print(self.t_spatial_index)
        
        # print(self.t_temporal_index.shape)
        # print(self.t_spatial_index.shape)

        # print(len(non_zero_index))
        # print(len(zero_index))
        # print(data_matrix.shape[0] * data_matrix.shape[1] == len(non_zero_index)+len(zero_index))

        # print(zero_index)

    def predict(self):
        z,ss = self.model.execute("grid",self.t_spatial_index,self.t_temporal_index)
        return z.T