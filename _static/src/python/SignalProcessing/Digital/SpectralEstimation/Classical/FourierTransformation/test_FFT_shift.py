import numpy as np
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = np.fft.fft(x)
yshift1 = np.fft.fftshift(np.fft.fft(x))
yshift2 = np.fft.fftshift(np.fft.fft(np.fft.fftshift(x)))

yabs = np.abs(y)
yshift1abs = np.abs(yshift1)
yshift2abs = np.abs(yshift2)


print(y)
print(yshift1)
print(yshift2)

print(yabs)
print(yshift1abs)
print(yshift2abs)

plt.figure()

plt.plot(np.abs(y), 'r')
plt.plot(np.abs(yshift1), '-og')
plt.plot(np.abs(yshift2), '-+b')
plt.show()
