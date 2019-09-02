import numpy as np

filename="test.npy"
npyDict=np.load(filename,allow_pickle=True).item()
print(npyDict)

modifyKey="lan"
val='js'
npyDict[modifyKey]=val
print(npyDict)

np.save('test1.npy',npyDict)


