import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

if __name__ == '__main__':
    x = np.array([-1.0, 1.0, 2.0])
    print(sigmoid(x))

    a = np.arange(-5.0, 5.0, 0.1)
    b = sigmoid(a)
    plt.plot(a, b)
    plt.ylim(-0.1, 1.1)#y축 범위 지정
    plt.show()
