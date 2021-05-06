import numpy as np
import matplotlib.pyplot as plt
PI = np.pi

# =========================define sinc
# ---------------normalized


def sinc1(x):
    PI = np.pi
    x = np.array(x)
    y = np.where(np.abs(PI * x) < 1e-38, 1.0, np.sin(PI * x) / (PI * x))
    return y


def sinc_interpolation(x, t, T):
    ns = np.arange(x.size)
    print(ns, "============")

    y = []
    for tt in t:
        y.append(np.sum(x * sinc1((tt - ns * T) / T)))

    return np.array(y)


# =========================test sinc definition
f0 = 100

Ns = 2000
Tp = 20.0 / Ns
t = np.linspace(-10, 10, Ns)
t2 = np.linspace(-10, 10, Ns * 2)
y1 = sinc1(t / Tp)


x = np.sin(2 * PI * f0 * t)
print(x.shape)

y = sinc_interpolation(x, t2, Tp)

print(y.shape, "===")

yfft = np.fft.fftshift(np.fft.fft(y))

plt.figure()
plt.subplot(131)
plt.plot(t, x, '^b')
plt.plot(t2, y, '+r')
plt.legend(['original', 'sinc interpolated'])
plt.title('sinc(t/Tp), ' + "Tp=" + str(Tp))
plt.xlabel('Time/s')
plt.ylabel('Amplitude')
plt.grid()


plt.show()
