import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# create tensor (on cpu by default)
tensor = torch.tensor([1, 2, 3])

#move tensor to gpu
tensor_on_gpu = tensor.to(device)
tensor_on_gpu

# move back to cpu
# if tensor is on GPU, can't use numpy() directly
tensor_back_on_cpu = tensor_on_gpu.cpu()
tensor_back_on_cpu
