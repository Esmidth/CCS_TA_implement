import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.optimize as spopt
import scipy.fftpack as spfft
import scipy.ndimage as spimg
import imageio
import cvxpy as cvx


def dct2(x):
    return spfft.dct(spfft.dct(x.T, norm='ortho', axis=0).T, norm='ortho', axis=0)


def idct2(x):
    return spfft.idct(spfft.idct(x.T, norm='ortho', axis=0).T, norm='ortho', axis=0)


# Xorig = imageio.imread('Escher_Waterfall.jpg', as_gray=True, pilmode='L')
Xorig = imageio.imread('rome.jpg', as_gray=True, pilmode='L')
# ny, nx = Xorig.shape
# print(ny,nx)
X = spimg.zoom(Xorig, 0.04)
ny, nx = X.shape
print(X.shape)
# plt.imshow(Xorig)
# plt.imshow(X)
# plt.show()

# extract small sample of signal
k = round(nx * ny * 0.5)  # 50% sample
ri = np.random.choice(nx * ny, k, replace=False)
print("ri/n",ri.shape)
b = X.T.flat[ri]
# b = np.expand_dims(b, axis=1)
print(b.shape)

# create dct matrix operator using kron
A = np.kron(
    spfft.idct(np.identity(nx), norm='ortho', axis=0),
    spfft.idct(np.identity(ny), norm='ortho', axis=0)
)
print('before',A.shape)
A = A[ri, :]
print('after',A.shape)

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

plt.figure()
plt.imshow(X, cmap='gray')
plt.title('X')
plt.figure()
plt.imshow(A, cmap='gray')
plt.figure()
plt.imshow(Xm, cmap='gray')
plt.figure()
plt.imshow(Xa.T, cmap='gray')
plt.title('xa')
plt.show()
# plt.savefig('2d.png',dpi=300)
