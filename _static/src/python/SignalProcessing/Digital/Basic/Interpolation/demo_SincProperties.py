import numpy as np
import matplotlib.pyplot as plt


# =========================define sinc
# ---------------normalized
def sinc1(x):
    PI = np.pi
    x = np.array(x)
    y = np.where(np.abs(PI * x) < 1e-38, 1.0, np.sin(PI * x) / (PI * x))
    return y


# ---------------denormalized
def sinc2(x):
    y = np.where(np.abs(x) < 1e-38, 1.0, np.sin(x) / x)
    return y


# =========================test sinc definition
a = [1e-15, 1, 1 / 2]
print(a)

print("by numpy: ", np.sinc(a))
print(a)
print("by sinc1: ", sinc1(a))
print(a)
print("by sinc2: ", sinc2(a))
print(a)

# =========================test sinc definition

Ns = 1024
Tp = 4
t = np.linspace(-10, 10, Ns)
y1 = sinc1(t / Tp)
y2 = sinc2(t / Tp)

y1fft = np.fft.fftshift(np.fft.fft(y1))
y2fft = np.fft.fftshift(np.fft.fft(y2))
f = np.fft.fftshift(np.fft.fftfreq(Ns))

# y1fft = np.fft.fft(y1)
# y2fft = np.fft.fft(y2)
# f = np.fft.fftfreq(Ns)

plt.figure()
plt.subplot(131)
plt.plot(t, y1, 'r')
plt.plot(t, y2, '-b')
plt.title('sinc(t/Tp), ' + "Tp=" + str(Tp))
plt.xlabel('Time/s')
plt.ylabel('Amplitude')
plt.legend(['sin(πt/Tp)/(πt/Tp)', 'sin(t/Tp)/(t/Tp)'])
plt.grid()

plt.subplot(132)
plt.plot(f, np.abs(y1fft), '-r')
plt.plot(f, np.abs(y2fft), '-b')
plt.title('FFT of signal')
plt.xlabel('Frequency/Hz')
plt.ylabel('Amplitude')
plt.legend(['sin(πt/Tp)/(πt/Tp)', 'sin(t/Tp)/(t/Tp)'])
plt.grid()

plt.subplot(133)
plt.plot(f, np.abs(y1fft), '-r')
plt.plot(f, np.abs(y2fft), '-b')
plt.title('FFT of signal (zoom out)')
plt.xlabel('Frequency/Hz')
plt.ylabel('Amplitude')
plt.legend(['sin(πt/Tp)/(πt/Tp)', 'sin(t/Tp)/(t/Tp)'])
plt.grid()
plt.show()
