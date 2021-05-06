import numpy as np
import matplotlib.pyplot as plt

fftaxis = 1

f0 = 10.0

Tss = -1.0
Tse = 1.0
Ts = Tse - Tss

Fs = 100
Ns = Fs * Ts

t = np.linspace(Tss, Tse, Ns)
x = np.sin(2 * np.pi * f0 * t)

X = []
M = 256

for i in range(M):
    X.append(x)

X = np.array(X)

Y = np.fft.fft(X, axis=fftaxis)
Yshift = np.fft.fftshift(np.fft.fft(X, axis=fftaxis))


f = np.linspace(0, Fs, Ns)
fshift = np.linspace(-Fs / 2.0, Fs / 2.0, Ns)


plt.figure()
plt.subplot(131)
plt.imshow(X)
plt.xlabel('Times/s')
plt.ylabel('Amplitude')
plt.title('Original Signal(' + str(f0) + 'Hz)')

plt.subplot(132)
plt.imshow(abs(Y))
plt.xlabel('Frequency/Hz')
plt.ylabel('Amplitude')
plt.title('FFT of Signal')

plt.subplot(133)
plt.imshow(abs(Yshift))
plt.xlabel('Frequency/Hz')
plt.ylabel('Amplitude')
plt.title('FFT of Signal(shifted)')
# plt.subplots_adjust(wspace=0.8)
plt.tight_layout()
plt.show()
