import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.optimize as spopt
import scipy.fftpack as spfft
import scipy.ndimage as spimg
import imageio
import cvxpy as cvx

import torch
from torch.autograd import Variable
import torch.optim as optim
# from torch.nn.functional import normalize
from torchvision.transforms import Normalize,ToTensor

def dct2(x):
    return spfft.dct(spfft.dct(x.T, norm='ortho', axis=0).T, norm='ortho', axis=0)


def idct2(x):
    return spfft.idct(spfft.idct(x.T, norm='ortho', axis=0).T, norm='ortho', axis=0)


# Xorig = imageio.imread('Escher_Waterfall.jpg', as_gray=True, pilmode='L')

# plt.imshow(Xorig)
# plt.imshow(X)
# plt.show()

# print(X.mean(),X.max(),X.min())
# X = X-128
# X = X/128
# print(X.mean(),X.max(),X.min())

def compute(X,sample_rate):
    # extract small sample of signal
    k = round(nx * ny * sample_rate)  # 50% sample
    ri = np.random.choice(nx * ny, k, replace=False)
    # print("ri/n",ri.shape)
    b = X.T.flat[ri]
    # b = np.expand_dims(b, axis=1)
    # print(ri)
    # print(b)

    # create dct matrix operator using kron
    A = np.kron(
        spfft.idct(np.identity(nx), norm='ortho', axis=0),
        spfft.idct(np.identity(ny), norm='ortho', axis=0)
    )
    # print('before',A.shape)
    A = A[ri, :]
    # print('after',A.shape)

    mask = np.zeros(X.shape)
    mask.T.flat[ri] = 255
    Xm = 255 * np.ones(X.shape)
    Xm.T.flat[ri] = X.T.flat[ri]

    # do L1 optimization
    vx = cvx.Variable(nx * ny)
    objective = cvx.Minimize(cvx.norm(vx, 1))
    constraints = [A * vx == b]
    prob = cvx.Problem(objective, constraints)
    result = prob.solve(verbose=True)
    Xat2 = np.array(vx.value).squeeze()

    # reconstruct signal
    Xat = Xat2.reshape(nx, ny)
    Xa = idct2(Xat)

    # confirm solution
    if not np.allclose(X.T.flat[ri], Xa.T.flat[ri]):
        print("Warning values at sample indices dont match original")

    # create images of mask ( for visualization)
    mask = np.zeros(X.shape)
    mask.T.flat[ri] = 255
    Xm = 255 * np.ones(X.shape)
    Xm.T.flat[ri] = X.T.flat[ri]

    savefigs((X,Xm,Xat.T,Xa.T),(2,2),'cvxpy_{}.png'.format(sample_rate))


def savefigs(fig_list,fig_shape,file_name='test.png'):
    num = len(fig_list)
    fig,axes = plt.subplots(2,2)
    for i,a in enumerate(axes.flat):
        a.imshow(fig_list[i],cmap='gray')
    # fig.title(file_name[-7:-4])
    fig.savefig(file_name)


if __name__ == "__main__":
    Xorig = imageio.imread('rome.jpg', as_gray=True, pilmode='L')
    # ny, nx = Xorig.shape
    # print(ny,nx)
    X = spimg.zoom(Xorig, 0.04)
    ny, nx = X.shape 
    # print(X.shape)
    sample_rates = np.arange(0.1,1,0.1)
    sample_rates = sample_rates.tolist()
    # print(sample_rates)
    for s in sample_rates:
        compute(X,s)
        # savefigs([X,X],(2,2),'test.png')