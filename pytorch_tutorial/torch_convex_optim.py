import torch
import torch.optim as optim
from torch.autograd import Variable

w = Variable(torch.randn(3,5),requires_grad=True)
b = Variable(torch.randn(3),requires_grad=True)
x = Variable(torch.randn(5))
print("x: \t",x)
print("w: \t",w)
print("b: \t",b)
y = Variable(torch.randn(3))
print("y: \t",y)

optimzer = optim.SGD([w,b],lr=0.01)

num_epochs = 1000
for epoch in range(num_epochs):
    optimzer.zero_grad()
    y_pred = torch.mv(w,x)+b
    loss = ((y-y_pred)**2).sum()
    loss.backward()
    optimzer.step()
    if epoch % 5 == 0:
        print(loss)
y_pred = torch.mv(w,x)+b
print("y_pred:\t",y_pred)
print("w: \t",w)
print("b: \t",b)