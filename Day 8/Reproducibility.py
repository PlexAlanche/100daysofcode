#Reproducibility (taking out random out of random)

import torch

# set random seed
random_seed = 42
torch.manual_seed(random_seed)
random_tensor_c = torch.rand(3, 4)
torch.manual_seed(random_seed)
random_tensor_d = torch. rand(3, 4)

print(random_tensor_c)
print(random_tensor_d)
print(random_tensor_c == random_tensor_d)