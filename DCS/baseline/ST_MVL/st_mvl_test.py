# from DCS.baseline.ST_MVL.st_mvl import ST_MVL
from st_mvl import ST_MVL
import numpy as np

def generate_data_matrix(spatial_size, temporal_size, miss_ratio=0):
    data_matrix = np.random.randint(1,5,size=(spatial_size,temporal_size))
    origin = data_matrix.copy()
    k = round(spatial_size*temporal_size*miss_ratio)
    ri = np.random.choice(spatial_size*temporal_size,k,replace=False)
    data_matrix.flat[ri] = 0
    return origin,data_matrix

def get_distance_matrix(data_matrix,linear=False):
    if not linear:
        spatial_length = data_matrix.shape[0]
        # print(spatial_length)
        dis_matrix = np.random.rand(spatial_length,spatial_length)
        dis_matrix += dis_matrix.T
        np.fill_diagonal(dis_matrix,0)
        return dis_matrix
    else:
        spatial_length = data_matrix.shape[0]
        dis_matrix = np.zeros((spatial_length,spatial_length))
        for i in range(spatial_length):
            dis_matrix[i][i:] = np.arange(0,spatial_length-i)
        dis_matrix = dis_matrix + dis_matrix.T
        return dis_matrix


def main():
    origin,dm = generate_data_matrix(5,4,0.2)
    ds=get_distance_matrix(origin,True)
    # dm = np.array([[1,2,3],[4,5,6],[0,0,0]])
    stmvl = ST_MVL()

    # idw,ses = stmvl.predict()
    icf = stmvl.predict(dm,ds)
    # flag  = stmvl.is_block_missing()

    # print(type(stmvl))
    # print(idw-dm)
    # print(ses-dm)
    print(icf-dm)
    # print(flag)


if __name__ == '__main__':
    main()