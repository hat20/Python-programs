import numpy as np
m,n = input().strip().split(' ')
m = int(m)
n = int(n)
np.set_printoptions(sign=' ')
print(np.eye(m, n, k=0))



