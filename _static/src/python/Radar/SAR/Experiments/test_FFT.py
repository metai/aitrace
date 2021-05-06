
import numpy as np
from numpy.fft import *


x = [1, 2, 3, 4]
x = np.array(x)

print("\n---x")
print(x)
print("\n---fft([1, 2, 3, 4])")
print(fft([1, 2, 3, 4]))
print("\n---fft([4, 3, 2, 1])")
print(fft([4, 3, 2, 1]))


x = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]

x = np.array(x)

print("\n---x")
print(x)
print("\n---fftshift(x, axes=0)")
print(fftshift(x, axes=0))
print("\n---fftshift(x, axes=1)")
print(fftshift(x, axes=1))

print("\n---x")
print(x)
print("\n---ifftshift(x, axes=0)")
print(ifftshift(x, axes=0))
print("\n---ifftshift(x, axes=1)")
print(ifftshift(x, axes=1))

y0 = fft(x, axis=0)
y1 = fft(x, axis=1)

print("\n---fft(x, axis=0)")
print(y0)
print("\n---fft(x, axis=1)")
print(y1)


ys00 = fft(fftshift(x, axes=0), axis=0)
ys11 = fft(fftshift(x, axes=1), axis=1)

print("\n---fft(fftshift(x, axes=0), axis=0)")
print(ys00)
print("\n---fft(fftshift(x, axes=1), axis=1)")
print(ys11)

ys000 = fftshift(fft(fftshift(x, axes=0), axis=0), axes=0)
ys111 = fftshift(fft(fftshift(x, axes=1), axis=1), axes=1)


print("\n---fftshift(fft(fftshift(x, axes=0), axis=0), axes=0)")
print(ys000)
print("\n---fftshift(fft(fftshift(x, axes=1), axis=1), axes=1)")
print(ys111)


print("-------------------------------------")

x = [1, 2, 3, 4]
x = np.array(x)

y = fft(x)

print("---x")
print(x)

print("---fft(x)")
print(y)

yy = fftshift(fft(fftshift(x)))

print("---x")
print(x)

print("---fftshift(fft(fftshift(x)))")
print(yy)


x = ifft(y)
print("---ifft(fft(x))")
print(x)


x = ifft(yy)
print("---ifft(yy)")
print(x)


x = ifft(fftshift(yy))
print("---ifft(fftshift(yy))")
print(x)

x = fftshift(ifft(yy))
print("---fftshift(ifft(yy))")
print(x)


x = ifftshift(ifft(ifftshift(yy)))
print("---ifftshift(ifft(ifftshift(yy)))")
print(x)

x = fftshift(ifft(fftshift(yy)))
print("---fftshift(ifft(fftshift(yy)))")
print(x)

x = ifftshift(ifft(fftshift(yy)))
print("---ifftshift(ifft(fftshift(yy)))")
print(x)

x = fftshift(ifft(ifftshift(yy)))
print("---fftshift(ifft(ifftshift(yy)))")
print(x)
