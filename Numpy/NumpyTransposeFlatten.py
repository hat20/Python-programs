import numpy as np
n,m = input().split(' ')
n = int(n)
m = int(m)
a = []
for i in range(0,n):
    a.append(input().split(' '))

a =  np.array(a,int)
print(np.transpose(a))
print(a.flatten())
