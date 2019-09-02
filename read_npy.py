import numpy as np

filename="test.npy"
# filename="test1.npy"
npyDict=np.load(filename,allow_pickle=True).item()
print(type(npyDict))
print(npyDict)
