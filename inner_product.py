import numpy as np

a = np.array([1,2,3,4])#1차원배열
print(a)
print(np.ndim(a))#배열의 차원 수
print(a.shape)#배열의 형상

b = np.array([[1,2], [3,4], [5,6]])
print(b)
print(np.ndim(b))
print(b.shape)

x = np.array([[1,2], [3,4]])
print(x.shape)
y = np.array([[5,6], [7,8]])
print(y.shape)
print(np.dot(x, y))#내적