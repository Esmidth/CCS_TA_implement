import numpy as np


class NMF(object):
    def __init__(self,V,mask,r,k,e):
        super().__init__()
        self.V = V
        self.mask = mask
        self.r = r
        self.k = k
        self.e = e
    


    def predict(self):
        pass
