import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


f = 100
Fs = 1000
T = 0.5
Tw = 0.5

Ns = int(T * Fs)

Nw = int(Tw * Fs)

t = np.linspace(0, T, Ns)
tw = np.linspace(0, Tw, Nw)

x = np.cos(2 * np.pi * f * t)


# windn = ('tukey', 10)
# windn = ('kaiser', 10)
# windn = ('gaussian', 100)
# windn = ('hamming')
# windn = ('cosine')
windn = ('blackman')


window = signal.get_window(windn, Nw)


print(Nw, len(window))

xfft = np.fft.fft(x)
ffft = np.fft.fftfreq(x.shape[-1])

idx = 0
y = x.copy()
y[idx:idx + Nw] = x[idx:idx + Nw] * window

print(y.shape, t.shape)

plt.figure(figsize=(10, 10))
plt.subplot(221)
plt.grid()
plt.plot(t, x)
plt.title('signal')
plt.xlabel('Time/s')
plt.ylabel('Amplitude')

plt.subplot(222)
plt.grid()
plt.plot(tw, window)
plt.title('window: ' + str(windn))
plt.xlabel('Time/s')
plt.ylabel('Amplitude')

plt.subplot(223)
plt.grid()
plt.plot(t, y)
plt.title('applied window on signal')
plt.xlabel('Time/s')
plt.ylabel('Amplitude')

yfft = np.fft.fft(y)

plt.subplot(224)
plt.grid()
plt.plot(ffft * Fs, np.abs(xfft), '-b')
plt.plot(ffft * Fs, np.abs(yfft), '-r')
plt.title('FFT of signal')
plt.legend(['orignal', 'windowed'])
plt.xlabel('Frequency/Hz')
plt.ylabel('Amplitude')
plt.show()
