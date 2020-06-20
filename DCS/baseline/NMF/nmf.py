import numpy as np


class NMF(object):
    def __init__(self,r=2,k=100,e=1e-5):
        super().__init__()
        # self.V = V
        # self.mask = mask
        self.r = r
        self.k = k
        self.e = e
    


    def predict(self,V,mask):
        m, n = np.shape(V)
        r = self.r
        k = self.k
        e = self.e
        
        W = np.mat(np.random.random((m,r)))
        H = np.mat(np.random.random((r,n)))

        for x in np.arange(k):
            V_pre = W*H
            E = V - np.multiply(V_pre,mask)
            err = np.sum(abs(E))

            if err < e:
                break

            a = W.T * V
            b = W.T * W * H

            for i1 in np.arange(r):
                for j1 in np.arange(n):
                    if b[i1,j1] != 0:
                        H[i1,j1] = H[i1,j1] * a[i1,j1] / b[i1,j1]
            
            c = V*H.T
            d = W*H*H.T

            for i2 in np.arange(m):
                for j2 in np.arange(r):
                    if d[i2,j2] != 0:
                        W[i2,j2] = W[i2,j2] * c[i2,j2] / d[i2,j2]

        self.W = W
        self.H = H
        return W*H
