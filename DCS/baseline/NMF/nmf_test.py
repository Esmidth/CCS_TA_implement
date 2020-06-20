from nmf import NMF
import numpy as np

def load_data(spatial_size, temporal_size, miss_ratio=0):
    origin = np.random.randint(1,5,size=(spatial_size,temporal_size))
    mask = np.ones_like(origin)
    k = round(spatial_size*temporal_size*miss_ratio)
    ri = np.random.choice(spatial_size*temporal_size,k,replace=False)
    mask.flat[ri] = 0
    return origin,mask


def main():
    origin,mask = load_data(4,5,0.2)
    dm = origin*mask
    mask1 = dm / origin
    print(mask1)
    print(mask)
    nmf = NMF()
    rec = nmf.predict(dm,mask)
    print(rec-dm)


if __name__ == "__main__":
    main()