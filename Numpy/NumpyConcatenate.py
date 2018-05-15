import numpy as np
n,m,p = input().split(' ')
n = int(n)
m = int(m)
p = int(p)

a1,a2 = [],[]
for i in range(0,n):
    a1.append(input().strip().split(' '))

for j in range(0,m):
    a2.append(input().strip().split(' '))

a1 = np.array(a1,int)
a2 = np.array(a2,int)
print(np.concatenate((a1,a2),axis=0))
