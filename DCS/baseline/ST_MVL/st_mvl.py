
import numpy as np
import pandas as pd

class ST_MVL(object):
    def __init__(self,alpha=1,beta=0.5,window=5,block_window=3):
        super().__init__()
        # self.data_matrix = data_matrix
        self.alpha = alpha
        self.beta = beta
        self.window = window
        self.block_window = block_window
        # self.distance_matrix = distance_matrix
    
    def _idw(self,data_matrix=None):
        if data_matrix is None:
            data_matrix = self.data_matrix
        distance_matrix = self.distance_matrix
        return_matrix = self.data_matrix.copy().astype(float)
        alpha = self.alpha
        if distance_matrix is not None:
            spaital_length,temporal_length = data_matrix.shape

            for i in range(temporal_length):
                tmp = data_matrix.T[i]
                # print(tmp)
                zero_index = np.where(tmp == 0)[0]
                true_index = np.where(tmp != 0)[0]
                res_array = np.zeros_like(zero_index,dtype=float)
                for j,mis in enumerate(zero_index):                
                    dis_array = np.zeros_like(true_index,dtype=np.float)
                    for ii,solid in enumerate(true_index):
                        dis_array[ii] = distance_matrix[mis][solid]
                    dis_array = np.power(dis_array,-alpha)
                    res_array[j] = np.dot(dis_array,tmp[true_index]) / np.sum(dis_array)
                    if np.isinf(res_array[j]) or np.isnan(res_array[j]):
                        res_array[j] = 0

                return_matrix.T[i][zero_index] = res_array
        else:
            pass
        return return_matrix

    def _ses(self,data_matrix=None):
        if data_matrix is None:
            data_matrix = self.data_matrix
            # def ses(data_matrix,beta=0.5,time_interval_array=None):
        beta = self.beta
        return_matrix = self.data_matrix.copy().astype(float)

        spatial_length,temporal_length = data_matrix.shape
        for i in range(spatial_length):
            tmp = data_matrix[i]
            # print(tmp)
            zero_index = np.where(tmp == 0)[0]
            true_index = np.where(tmp != 0)[0]
            res_array = np.zeros_like(zero_index,dtype=float)
            # print('-')
            for j,mis in enumerate(zero_index):
                # print('--')
                time_interval = abs(true_index-mis)
                # print(time_interval)
                # coef_array = time_interval
                coef_array = np.power(1-beta,time_interval-1)*beta
                res_array[j] = np.dot(coef_array,tmp[true_index]) / (np.sum(coef_array))
                if np.isinf(res_array[j]) or np.isnan(res_array[j]):
                    res_array[j] = 0
                # print('res',res_array[j])
            # print(zero_index)
            return_matrix[i][zero_index] = res_array
        return return_matrix
    def _icf(self,data_matrix = None):
        if data_matrix is None:
            data_matrix = self.data_matrix
        window = self.window
        
        return_matrix = data_matrix.copy().astype(float)

        if data_matrix is not None:
            spatial_length, temporal_length = data_matrix.shape
            zero_index = np.where(data_matrix.flatten() == 0)[0]

            res_array = np.zeros_like(zero_index,dtype=float)

            temporal_index = zero_index % temporal_length
            spatial_index = zero_index / temporal_length

            spatial_index = spatial_index.astype(int)
            left_margin = temporal_index - (window-1)/2
            right_margin = temporal_index + (window -1)/2

            left_margin[np.where(left_margin < 0)[0]] = 0
            right_margin[np.where(right_margin >= temporal_length)] = temporal_length-1
            left_margin = left_margin.astype(int)
            right_margin = right_margin.astype(int)

            index = np.arange(temporal_length)
            for i in range(len(zero_index)):
                sim_array = np.zeros(temporal_length)
                sim_array[left_margin[i]:right_margin[i]+1] = 1
                sim_array[temporal_index[i]] = 0

                sim_array_index = np.where(sim_array == 1)[0]

                for ii in sim_array_index :
                    sim_array[ii] = self._sim_temporal(data_matrix,temporal_index[i],ii)

                res_array[i] = np.dot(sim_array,data_matrix[spatial_index[i]]) / np.sum(sim_array)
                if np.isinf(res_array[i]) or np.isnan(res_array[i]):
                    res_array[i] = 0


            return_matrix.flat[zero_index] = res_array

        return return_matrix
        
        pass

    def _sim_temporal(self,sub_data,source_index,target_index):
        source_non_zero_index = np.where(sub_data.T[source_index] != 0)[0]
        target_non_zero_index = np.where(sub_data.T[target_index] != 0)[0]

        intersect = np.intersect1d(source_non_zero_index,target_non_zero_index)

        diff1 = sub_data.T[source_index][intersect]
        diff2 = sub_data.T[target_index][intersect]

        diff_count = np.sqrt(len(diff1-diff2))
        tmp = np.power(diff1-diff2,2)
        tmp = np.sum(tmp)
        if tmp == 0 or tmp == 0.0:
            tmp = 0.0000001
        diff_sum = 1 / np.sqrt(tmp)
        sim = diff_count*diff_sum

        if np.isinf(sim):
            sim = 999
        if np.isnan(sim):
            sim = 0
        return sim

    def _ucf(self,data_matrix=None):
        if data_matrix is None:
            data_matrix = self.data_matrix
        window = self.window
        return_matrix = data_matrix.copy().astype(float) 
        if data_matrix is not None:
            spatial_length, temporal_length = data_matrix.shape
            zero_index = np.where(data_matrix.flatten() == 0)[0]
            
            res_array = np.zeros_like(zero_index,dtype=float)
            temporal_index = zero_index % temporal_length
            spatial_index = zero_index / temporal_length
            spatial_index = spatial_index.astype(int)
       
            left_margin = temporal_index - (window-1)/2
            right_margin = temporal_index + (window -1)/2
       
            left_margin[np.where(left_margin < 0)[0]] = 0
            right_margin[np.where(right_margin >= temporal_length)] = temporal_length-1
            left_margin = left_margin.astype(int)
            right_margin = right_margin.astype(int)
            for i in range(len(zero_index)):
            
                sub = ((data_matrix.T[left_margin[i]:right_margin[i]+1]).T)
                sim_array = np.ones(spatial_length)
                sim_array[spatial_index[i]] = 0
                sim_array_index = np.where(sim_array != 0)[0]
                for ii in sim_array_index:
                    sim_array[ii] = self._sim_local(sub,spatial_index[i],ii)
                
                spatial_data_for_certain_time = data_matrix.T[temporal_index[i]]
                res_array[i] = np.dot(spatial_data_for_certain_time,sim_array) / np.sum(sim_array)
                if np.isinf(res_array[i]) or np.isnan(res_array[i]):
                    res_array[i] = 0
                
            return_matrix.flat[zero_index] = res_array
        return return_matrix


    
    def _sim_local(self,sub_data,spatial_index,current_index):

        sp_non_zero_index = np.where(sub_data[spatial_index] != 0)[0]
        ci_non_zero_index = np.where(sub_data[current_index] != 0)[0]
       
        intersect = np.intersect1d(sp_non_zero_index,ci_non_zero_index)
       
        diff1 = sub_data[spatial_index][intersect]
        diff2 = sub_data[current_index][intersect]
        diff_count = np.sqrt(len(diff1-diff2))

        tmp = np.power(diff1-diff2,2)
        tmp = np.sum(tmp)

        if tmp == 0 or tmp == 0.0:
            tmp = 0.00000001
        diff_sum = 1 / np.sqrt(tmp)
        sim = diff_count*diff_sum
        if np.isinf(sim):
            sim = 999
        if np.isnan(sim):
            sim = 0
        return sim

    def _is_block_missing_1d(self,data_matrix = None,window=None):
        if window is None:
            window = self.block_window
        if data_matrix is None:
            data_matrix = self.data_matrix

        flag = False
        # window = self.block_window
       
        spaital_length, temporal_length = data_matrix.shape

        zero_index = np.where(data_matrix.flatten() == 0)[0]
        spatial_index = zero_index / temporal_length
        spatial_index = spatial_index.astype(int)
        temporal_index = zero_index % temporal_length

        left_margin = temporal_index - (window-1)/2
        right_margin = temporal_index + (window -1)/2
        left_margin[np.where(left_margin < 0)[0]] = 0
        right_margin[np.where(right_margin >= temporal_length)] = temporal_length-1
        left_margin = left_margin.astype(int)
        right_margin = right_margin.astype(int)

        for i in range(len(zero_index)):
            sub_w = data_matrix[spatial_index[i]][left_margin[i]:right_margin[i]+1]
            if not sub_w.any() and len(sub_w) == window:
                flag = True
        return flag

    def is_block_missing(self,window=None):
        if window is None:
            window = self.block_window
        data_matrix = self.data_matrix

        # flag = 3 means both blocks in row and columns are missing
        # flag = 2 means there is a block_missing in column
        # flag = 1 means there is a block_missing in row
        # flag = 0 means there is no block_missing in both row and column

        flag = 0
        if self._is_block_missing_1d(window=window):
            flag = flag +1
        if self._is_block_missing_1d(data_matrix.T,window):
            flag = flag +2
        return flag
    
    def fit(self,data):
        self.data_matrix = data
        print(self.data_matrix)
        pass


    def predict(self,data_matrix,distance_matrix,alpha=None,beta=None,window=None,block_window=None):
        '''the implementation of st_mvl method, consisting of ucf,icf,idw,ses'''

        if alpha is None or beta is None or window is None or block_window is None:
            alpha = self.alpha
            beta = self.beta
            window = self.window
            block_window = self.block_window
        
        self.data_matrix = data_matrix
        self.distance_matrix = distance_matrix

        # data_matirx = self.data_matrix
        # distance_matrix = self.distance_matrix

        return_matrix = data_matrix.copy().astype(float)
        zero_index = np.where(return_matrix.flatten() == 0)[0]

        if self.is_block_missing(3) :
            return_matrix = self._ses()
        dm1 = self._ucf(return_matrix)
        dm2 = self._icf(return_matrix)
        dm3 = self._idw(return_matrix)
        dm4 = self._ses(return_matrix)

        # weight & b should be learing, while remains here as mean value
        weight = np.ones(4)
        b = 0

        for i in zero_index:
            v = (dm1.flat[i],dm2.flat[i],dm3.flat[i],dm4.flat[i])
            return_matrix.flat[i]=(np.dot(v,weight) / np.sum(weight))+b
        return return_matrix
        