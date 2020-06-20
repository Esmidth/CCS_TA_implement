import numpy as np
from sklearn.linear_model import LinearRegression

class AKE(object):
    def __init__(self):
        super().__init__()

    
    def sim_temporal(self,sub_data,source_index,target_index):
        # source_index，指数据较多项
        # target_index，指数据缺失项
        source_non_zero_index = np.where(sub_data[source_index] != 0)[0]
        target_non_zero_index = np.where(sub_data[target_index] != 0)[0]

        intersect = np.intersect1d(source_non_zero_index,target_non_zero_index)
        # 取消过短的序列
        if len(intersect) < 3:        
            return 0,None

        diff1 = sub_data[source_index][intersect]
        diff2 = sub_data[target_index][intersect]
        # print(diff1)
        # print(diff2)
        reg = LinearRegression().fit(diff1.reshape(-1,1),diff2.reshape(-1,1))

        # print(reg.predict(np.array([3]).reshape(-1,1)))
        # print('cof',reg.coef_)
        # print('inter',reg.intercept_)

        target_mean = np.mean(diff2)
        # print('tm',target_mean)
        target_square = np.square(diff2 - target_mean)
        # print('sq',target_square)
        # print(target_mean)

        rec = reg.predict(diff1.reshape(-1,1))
        rec = rec.reshape(1,-1)[0]
        # print('rec',rec)
        rec_square = np.square(rec-target_mean)

        tmp = np.sum(target_square)
        if tmp == 0.0 or tmp == 0:
            tmp = 0.0000001
        Rj = np.sum(rec_square) / tmp
        if np.isnan(Rj):
            Rj = 0
        elif np.isinf(Rj):
            Rj = 999

        # print('Rj',Rj)

        # print('rec_square',rec_square)
        # print('ts',target_square)

        full = sub_data[source_index]
        # print(tmp)
        # print('coef',reg.coef_)
        # print('inter',reg.intercept_)
        # print(full)
        rec_full = reg.predict(full.reshape(-1,1)).reshape(1,-1)[0]
        # print('rec_full',rec_full)
        # # print(diff1.reshape(-1,1))
        # # print(np.array([diff1]))
        # print(diff1.reshape(1,-1))
        # print(diff2)
        return Rj,rec_full



    def predict(self,data_matrix = None):
        if data_matrix is not None:
            return_matrix = data_matrix.copy().astype(float)
        
            spatial_length, temporal_length = data_matrix.shape
            zero_index = np.where(data_matrix.flatten() == 0)[0]
            rec_array_global = np.zeros_like(zero_index,dtype=float)

            temporal_index = zero_index % temporal_length
            spatial_index = zero_index / temporal_length
            spatial_index = spatial_index.astype(int)

            # print(zero_index)
            # print('ti',temporal_index)
            # print('si',spatial_index)
            index = np.arange(temporal_length)
            for i in range(len(zero_index)):
                # print(zero_index[i])
                sim_array = np.ones(spatial_length)
                # sim_array[spatial_index[i]] = 0
                tmp = data_matrix.T[temporal_index[i]]
                tmp_zero_index = np.where(tmp == 0)[0]
                sim_array[tmp_zero_index] = 0
                sim_array_index = np.where(sim_array==1)[0]
                rec_array = np.zeros_like(sim_array)
                # print(rec_array.shape)
                # tmp_one_index = np.where(tmp != 0)[0]
                for ii in sim_array_index:
                    sim_array[ii],tmp_rec_array = self.sim_temporal(data_matrix,spatial_index[i],ii)
                    if tmp_rec_array is not None:
                        rec_array[ii] = tmp_rec_array[temporal_index[i]]
                        # print(tmp_rec_array.shape)
                # print(sim_array)
                sim_array = sim_array / np.sum(sim_array)
                # print(sim_array)
                # print(rec_array)
                # print('---')
                rec_array_global[i] = np.dot(sim_array,rec_array)
                if np.isnan(rec_array_global[i]) or np.isinf(rec_array_global[i]):
                    rec_array_global[i] = 0


            # print('rec',rec_array_global)
            return_matrix.flat[zero_index] = rec_array_global
        

            return return_matrix
        else:
            return None