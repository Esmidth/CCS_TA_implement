import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.optimize as spopt
import scipy.fftpack as spfft
import scipy.ndimage as spimg
import cvxpy as cvx

# L1 vs L2 fitting

# x = np.sort(np.random.uniform(0, 10, 15))
# y = 3 + 0.2 * x + 0.1 * np.random.randn(len(x))
#
# l1_fit = lambda x0, x, y: np.sum(np.abs(x0[0] * x + x0[1] - y))
# xopt1 = spopt.fmin(func=l1_fit, x0=[1, 1], args=(x, y))
# y_opt1 = xopt1[0] * x + xopt1[1]
#
# l2_fit = lambda x0, x, y: np.sum(np.power(x0[0] * x + x0[1] - y, 2))
# xopt2 = spopt.fmin(func=l2_fit, x0=[1, 1], args=(x, y))
# y_opt2 = xopt2[0] * x + xopt2[1]

# plt.plot(x,y,x,y_opt1,x,y_opt2)

# plt.scatter(x, y,label='data')
# plt.plot(x, y_opt1, label='l1_fit')
# plt.plot(x, y_opt2, label='l2_fit')
# plt.legend()
# plt.show()
#
# y2 = y.copy()
# y2[3] += 4
# y2[13] -= 3
#
# xopt12 = spopt.fmin(func=l1_fit, x0=[1, 1], args=(x, y2))
# xopt22 = spopt.fmin(func=l2_fit, x0=[1, 1], args=(x, y2))

# y_opt12 = xopt12[0] * x + xopt12[1]
# y_opt22 = xopt22[0] * x + xopt22[1]
# plt.scatter(x, y, label='data')
# plt.plot(x, y_opt12, label='l1_fit')
# plt.plot(x, y_opt22, label='l2_fit')
# plt.legend()
# plt.show()

# Reconstruction of a Simple Signal

# sum of two sinusoids
n = 5000
t = np.linspace(0, 1 / 8, n)
y = np.sin(1394 * np.pi * t) + np.sin(3266 * np.pi * t)
yt = spfft.dct(y, norm="ortho")

sub = 500
m = 50
ri = np.random.choice(sub, m, replace=False)
ri.sort()
t_sub = t[:sub]
y_sub = y[:sub]
# t2 = t_sub[ri]
# y2 = y_sub[ri]
t1 = np.arange(0,500,1)
# print(t1)


t2 = t1[ri]
y2 = y_sub[ri]

# plt.figure()
# plt.plot(t,y)
plt.scatter(t2, y2, label='sample', color='red')

for i in range(m):
    plt.text(t2[i], y2[i], i)

plt.plot(t1, y_sub, label='origin')

ax = plt.gca()
# 去掉上、右边框
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# 移到原点
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.legend()
# plt.show()
A = spfft.idct(np.identity(sub), norm='ortho', axis=0)
A = A[ri]

vx = cvx.Variable(sub)
objective = cvx.Minimize(cvx.norm(vx, 1))
constraints = [A * vx == y2]
prob = cvx.Problem(objective, constraints)
result = prob.solve(verbose=True)

x = np.array(vx.value)
x = np.squeeze(x)
sig = spfft.idct(x, norm='ortho', axis=0)
# plt.figure()
plt.plot(t1,sig,label='reconstruct')
plt.show()
