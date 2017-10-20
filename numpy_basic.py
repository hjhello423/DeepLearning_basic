import numpy as np

#numpy.array() : list를 인수로 받아 mumpy.ndarray로 반환
a = np.array([1.0, 2.0, 3.0])
print(a)#[ 1.  2.  3.]
print(type(a))#<class 'numpy.ndarray'>

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
#numpy.ndarray는 원소수가 같을때 각 원소에 대해 산술연산을 실행
print(x+y)#[ 3.  6.  9.]
print(x-y)
print(x/y)
print(x/2)#[ 0.5  1.   1.5]

A = np.array([[1,2], [3,4]])
print(A)
"""
[[1 2]
 [3 4]]
"""
print(A.shape)#행렬 형상 출력  => (2, 2)

B = np.array([[3,0], [0,6]])
print(A + B)
"""
[[ 4  2]
 [ 3 10]]
"""

print(A * 10)
"""
[[10 20]
 [30 40]]
"""

A = np.array([[1,2], [3,4]])
print(A.dtype)#행렬에 담긴 원소의 자료형

A = np.array([[1,2], [3,4]])
B = np.array([10, 20])
print(A * B)#브로드캐스트 -> B행렬이 2*2로 확대후 연산
"""
[[10 40]
 [30 80]]
"""

X = np.array([[10,20], [30,40], [50,60]])
X = X.flatten()#1차원 배열로 평탄화
print(X)#[10 20 30 40 50 60]
print(X[np.array([1, 3, 5])])#1,3,5번 index 원소 반환 => [20 40 60]
print(X > 40)#[False False False False  True  True]
print(X < 30)#[ True  True False False False False]