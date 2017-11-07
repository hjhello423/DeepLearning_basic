import numpy as np
import matplotlib.pylab as plt

def softmax(x):
    z = np.max(x)
    expX = np.exp(x - z)
    sumExpX = np.sum(expX)
    y = expX / sumExpX
    return y

if __name__ == '__main__':
    x = np.array([0.3, 2.9, 4.0])
    print(x)
    
    expA = np.exp(x)#지수함수
    print('expA : ' + str(expA))

    sumExpA = np.sum(expA)#배열의 합
    print('sumExpA : ' + str(sumExpA))

    y = expA / sumExpA
    print('y : ' + str(y))

    z = softmax(x)
    print('z : ' + str(z))