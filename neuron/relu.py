import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)#두 입력 중 큰값 반환

if __name__ == '__main__':
    x = np.arange(-1.0, 1.0, 0.1)
    y = relu(x)
    plt.plot(x, y)
    plt.ylim(-1.0, 1.0)#y축 범위 지정
    plt.show()