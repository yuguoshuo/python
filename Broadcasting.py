import numpy as np

__author__ = 'Administrator'

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
y = np.empty_like(x)

for i in range(4):
    y[i, :] = x[i, :] + v

print(y)
print()

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
vv = np.tile(v,(4,1))
print(vv)
print()
y = x ++ vv
print(y)

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
print(y)
print()

v = np.array([1,2,3])
w = np.array([4,5])
print(np.reshape(v,(3,1))*w)



