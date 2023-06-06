import torch
x = torch.arange(1, 10).reshape(1, 3, 3)
x, x.shape

print(f"1st square bracket:\n{x[0]}") 
#indexing on middle bracket
print(f"2nd square bracket: {x[0, 0]}") 
#indexing on most inner dimension
print(f"3rd square bracket: {x[0, 2, 2]}")

#selecting all of a target dimension
x[:, 0]

#get all values of 0th and 1st dimensions but only index 1 of 2nd dimension
x[:, :, 1]

#get all values of the 0 dimension but only 1 index value of the 1st and 2nd dimensions
x[:, 1, 1]

#get index 0 of 0th and 1st dimension and all values of 2nd dimension
x[0, 0, :]

#index on x to return 3,6,9
print (x[0, :, 2])
