import numpy as np
n = input().strip().split(' ')
n = np.array(n,int)
print(np.reshape(n,(3,3)))