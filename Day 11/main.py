import torch
from torch import nn # nn contains all the building blocks to build a neural network'
import matplotlib.pyplot

#create parameters

weight = 0.7
bias = 0.3

#create data
start = 0
end = 1
step = 0.02

X = torch.arange(start, end, step).unsqueeze(dim=1)
y = weight * X + bias


#create a train/test set
train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]
len(X_train), len(y_train), len(X_test), len(y_test)
