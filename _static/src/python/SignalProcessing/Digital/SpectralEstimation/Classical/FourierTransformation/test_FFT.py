import numpy as np
import matplotlib.pyplot as plt


f0 = 10.0

Tss = -1.0
Tse = 1.0
Ts = Tse - Tss

Fs = 100
Ns = Fs * Ts

t = np.linspace(Tss, Tse, Ns)
x = np.sin(2 * np.pi * f0 * t)

y = np.fft.fft(x)
yshift = np.fft.fftshift(np.fft.fft(x))


f = np.linspace(0, Fs, Ns)
fshift = np.linspace(-Fs / 2.0, Fs / 2.0, Ns)


plt.figure()
plt.subplot(311)
plt.plot(t, x, '-r')
plt.grid()
plt.xlabel('Times/s')
plt.ylabel('Amplitude')
plt.title('Original Signal(' + str(f0) + 'Hz)')

plt.subplot(312)
plt.plot(f, np.abs(y), '-r')
plt.grid()
plt.xlabel('Frequency/Hz')
plt.ylabel('Amplitude')
plt.title('FFT of Signal')

plt.subplot(313)
plt.plot(fshift, np.abs(yshift), '-r')
plt.grid()
plt.xlabel('Frequency/Hz')
plt.ylabel('Amplitude')
plt.title('FFT of Signal(shifted)')
# plt.subplots_adjust(wspace=0.8)
plt.tight_layout()
plt.show()
