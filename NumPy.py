import numpy as np

__author__ = 'Administrator'

print("一个NumPy数组是一些类型相同的元素组成的类矩阵数据。用list或者层叠的list可以初始化:")
a = np.array([1,2,3])
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[0] = 5
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0,0],b[0,1],b[1,0])
a = np.zeros((2,2))
print(a)

b = np.ones((1,2))
print(b)

d = np.eye(2)
print(d)

print()

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print(x + y)
print(np.add(x, y))

print(x - y)
print(np.subtract(x, y))

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))
