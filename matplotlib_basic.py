import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)#0~6까지 0.1 간격으로 생성
print(x)
"""
[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.   1.1  1.2  1.3  1.4
  1.5  1.6  1.7  1.8  1.9  2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8  2.9
  3.   3.1  3.2  3.3  3.4  3.5  3.6  3.7  3.8  3.9  4.   4.1  4.2  4.3  4.4
  4.5  4.6  4.7  4.8  4.9  5.   5.1  5.2  5.3  5.4  5.5  5.6  5.7  5.8  5.9]
"""
y1 = np.sin(x)

plt.plot(x, y1)#그래프 생성
plt.show()#그래프 출력

y2 = np.cos(x)
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")#점선으로 그리기
plt.xlabel("X")
plt.ylabel("y")
plt.title('sin & cos')#제목 표시
plt.legend()#legend 표시
plt.show()