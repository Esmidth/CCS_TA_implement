from ake import AKE
import numpy as np

def generate_data_matrix(spatial_size, temporal_size, miss_ratio=0):
    data_matrix = np.random.randint(1,5,size=(spatial_size,temporal_size))
    origin = data_matrix.copy()
    k = round(spatial_size*temporal_size*miss_ratio)
    ri = np.random.choice(spatial_size*temporal_size,k,replace=False)
    data_matrix.flat[ri] = 0
    return origin,data_matrix

def main():

    origin,dm = generate_data_matrix(5,6,0.1)
    ake = AKE()
    rec = ake.predict(dm)
    print(rec-dm)


if __name__ == "__main__":
    main()