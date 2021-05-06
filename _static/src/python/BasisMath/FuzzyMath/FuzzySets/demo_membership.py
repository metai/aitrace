import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def bellshape(x, a, b, c):
    y = 1.0 + np.abs((x - c) / (a + EPS)) ** (2 * b)
    return 1.0 / y


def gauss(x, a, c):
    y = - np.square(x - c) / ((a + EPS) ** 2)
    y = np.exp(y)
    return y


if __name__ == '__main__':
    EPS = 1.0e-16
    N = 1
    Ns = 100

    x = np.linspace(0, N, Ns)

    a1 = 0.3
    b1 = 1.5
    c1 = 0.4
    y1 = bellshape(x, a=a1, b=b1, c=c1)

    a2 = 0.3
    b2 = 2
    c2 = 0.6
    y2 = bellshape(x, a=a2, b=b2, c=c2)

    plt.figure()
    plt.plot(x, y1, '-r')
    plt.plot(x, y2, '-b')
    plt.legend(['a=' + str(a1) + ', b=' + str(b1) + ', c=' + str(c1),
                'a=' + str(a2) + ', b=' + str(b2) + ', c=' + str(c2)])
    plt.hold()
    plt.grid()
    plt.title('bell shape membership function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

    a1 = 0.2
    c1 = 0.4
    y1 = gauss(x, a=a1, c=c1)

    a2 = 0.1
    c2 = 0.6
    y2 = gauss(x, a=a2, c=c2)

    plt.figure()
    plt.plot(x, y1, '-r')
    plt.plot(x, y2, '-b')
    plt.legend(['a=' + str(a1) + ', c=' + str(c1),
                'a=' + str(a2) + ', c=' + str(c2)])
    plt.hold()
    plt.grid()
    plt.title('gauss membership function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
