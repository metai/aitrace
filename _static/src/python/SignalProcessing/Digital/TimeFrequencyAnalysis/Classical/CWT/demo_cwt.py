import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

Ts = 5
Fs = 400.0
n = Ts * Fs

f1 = 10
f2 = 25
f3 = 50
f4 = 100

t1 = np.linspace(0, Ts, n)
x1 = np.cos(2 * np.pi * f1 * t1)
t2 = np.linspace(Ts, 2 * Ts, n)
x2 = np.cos(2 * np.pi * f2 * t2)
t3 = np.linspace(2 * Ts, 3 * Ts, n)
x3 = np.cos(2 * np.pi * f3 * t3)
t4 = np.linspace(3 * Ts, 4 * Ts, n)
x4 = np.cos(2 * np.pi * f4 * t4)

x = np.hstack((x1, x2, x3, x4))
t = np.hstack((t1, t2, t3, t4))

TW = 400e-3
NW = int(TW * Fs)
print(NW)


# wavelet = signal.morlet
wavelet = signal.ricker
widths = np.arange(1, NW + 1)
S = signal.cwt(x, wavelet, widths)

T = np.linspace(0, 4 * Ts, len(x))
F = np.linspace(0, Fs, NW)
print(S.shape, np.min(S[:]), np.max(S[:]))

# S = (S - np.min(S[:])) / (np.max(S[:]) - np.min(S[:]))

# plt.figure(figsize=(10, 10))
plt.figure()
plt.subplot(211)
plt.plot(t, x, '-r')
plt.ylabel('Amplitude')
plt.xlabel('Time/s')
plt.axis('tight')
plt.title('orignal signal')

plt.subplot(212)

map = plt.pcolormesh(T, F, S, cmap='jet')

plt.ylabel('Scales')
plt.xlabel('Time/s')
plt.axis('tight')
plt.title('CWT->' + str('ricker'))
cb = plt.colorbar(cax=None, ax=None, shrink=1)
plt.show()
