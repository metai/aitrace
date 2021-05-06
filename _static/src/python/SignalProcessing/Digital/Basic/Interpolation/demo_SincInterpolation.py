import numpy as np
import matplotlib.pyplot as plt
PI = np.pi


def sinc_interp(xin, r=1.0):
    xin = np.array(xin)
    N = xin.size
    M = int(N * r)

    u = np.linspace(0, N, M)
    v = np.linspace(0, N, N)
    xout = []
    for i in u:
        xout.append(np.sum(xin * sinc(v - i)))
    return np.array(xout), np.array(u)


def sinc(x):
    x = np.array(x)
    eps = 1.0e-8
    y = np.where(np.abs(PI * x) < eps, 1.0,
                 np.sin(PI * x + eps) / (PI * x + eps))
    return y


Ns = 100.0
T = 64.0
Fs = Ns / T
Ts = 1.0 / Fs

t0 = np.linspace(0, T, Ns)

a = 0.9
x0 = t0 * a**t0


r = 8.0
t1 = np.linspace(0, T, Ns * r)

x1 = np.interp(t1, t0, x0)

x2, n2 = sinc_interp(x0, r=r)

t2 = n2 * Ts

plt.figure()
plt.plot(t0, x0, '-ob')
plt.plot(t1, x1, '-g')
plt.plot(t2, x2, '-r')
plt.grid()
plt.xlabel('Time/s')
plt.ylabel('Amplitude')
plt.title('interpolation')
plt.legend(['original', 'np.interp', 'sinc_interp'])

plt.show()
