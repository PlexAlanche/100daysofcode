#PyTorch tensors and numpy 
import torch
import numpy as np

array = np.arange(1.0, 8.0)
tensor = torch.from_numpy(array)
array, tensor

#default dtype of tensor is float32
#default dtype of numpy array is float64

# change value of array and what it does to tensor
array = array + 1
array, tensor

# tensor to numpy array
tensor = torch.ones(7)
numpy_tensor = tensor.numpy()
tensor, numpy_tensor

print("array: ", array)
print("tensor: ", tensor)
print("numpy_tensor: ", numpy_tensor)

