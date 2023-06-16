import torch
from torch import nn # nn contains all the building blocks to build a neural network'
import matplotlib.pyplot

#create parameters

weight = 0.7
bias = 0.3

#we know these numbers, but the network doesn't. We have to build a model that can estimate these numbers by looking at different examples

#create data
start = 0
end = 1
step = 0.02

X = torch.arange(start, end, step).unsqueeze(dim=1)
y = weight * X + bias

print(X[:10], y[:10])
