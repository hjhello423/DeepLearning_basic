import numpy as np
import matplotlib.pylab as plt

def step_function(x): #계단함수
    y = x > 0
    return y.astype(np.int)

def step_function_plot(x):
    return np.array(x > 0, dtype=np.int)

if __name__ == '__main__':
    x = np.array([-1.0, 1.0, 2.0])
    print(x)
    y = x > 0
    print(y)
    print(type(y))
    y = y.astype(np.int) #넘파이 배열의 자료형을 bool에서 int로 변환
    print(y)

    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function_plot(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)#y축 범위 지정
    plt.show()#계단함수 그리기