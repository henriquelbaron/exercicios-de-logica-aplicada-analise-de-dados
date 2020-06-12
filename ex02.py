import numpy as np
import math
import matplotlib.pyplot as plt


def freq(x):
    return math.sqrt((math.pi * 2)) * math.e ** (-(x ** 2) / 2)


x = []
y = np.linspace(10, -10, num=2001)
for i in y:
    x.append(freq(i))

plt.title('Grafico')
plt.plot(y, x)
plt.show()
