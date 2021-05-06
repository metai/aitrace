import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import *

C = 3e8
PI = np.pi
H = 10e3
V = 150
Fc = 5.3e9
Tp = 25e-6
Kr = 0.25e12
Fsr = 7.5e6
Nr = 256
Fsa = 104
Na = 256
Lr = 12.0
La = 3.0

As = 0 * PI / 180.0
# As = 1.5 * PI / 180.0
# As = 21.9 * PI / 180.0
Ad = 30.0 * PI / 180.0
Ab = 8.4 * PI / 180.0

Rc = 20e3


# Earth Bending Geometry (Vg < Vr < Vs)
Vs = V  # platform
Vg = 1.0 * V  # ground
# Linear geometry
Vr = np.sqrt(Vs * Vg)  # Equivalent velocity


targets = [
    # [-100, 60, 0, 1],
    # [-100, 0, 0, 1],
    # [100, -60, 0, 1],
    [0, 0, 0, 1],
    [180, 50, 0, 1],
    # [100, 100, 0, 1],
    # [150, 100, 0, 1],
]


# -------------------------------------------

Wl = C / Fc
Br = abs(Kr) * Tp
R0 = Rc * np.cos(As)
Xc = np.sqrt(R0**2 - H**2)
Yc = Rc * np.sin(As)
Zc = 0

SC = [Xc, Yc, Zc]
SA = [-200, 200, -200, 200]
ES = [0, Na, 0, Nr]
print("SC: ", SC)
print("SA: ", SA)

print(C / (2 * Br))

Xmin = SA[0] + Xc
Xmax = SA[1] + Xc
Ymin = SA[2] + Yc
Ymax = SA[3] + Yc


SS = [Xmin, Xmax, Ymin, Ymax]
print("[Xmin, Xmax, Ymin, Ymax]", [Xmin, Xmax, Ymin, Ymax])
Rnear = np.sqrt(Xmin**2 + Ymin**2 + H**2)
Rfar = np.sqrt(Xmax**2 + Ymax**2 + H**2)
print("Rnear, Rfar: ", Rnear, Rfar)


# Rnear = H / np.sin(Ad + Ab / 2.0)
# Rfar = H / np.sin(Ad - Ab / 2.0)
# print("Rnear, Rfar: ", Rnear, Rfar)

Ynear = Rnear * np.sin(As)
Yfar = Rfar * np.sin(As)
Xnear = np.sqrt((Rnear * np.cos(As))**2 - H**2)
Xfar = np.sqrt((Rfar * np.cos(As))**2 - H**2)

# Xnear = (H / np.tan(Ad + Ab / 2.0))
# Xfar = (H / np.tan(Ad - Ab / 2.0))

print("Xnear, Xfar, Ynear, Yfar: ", Xnear, Xfar, Ynear, Yfar)
SA[0] = Xnear - Xc
SA[1] = Xfar - Xc

print("SC: ", SC)
print("SA: ", SA)

# -------------------------------------------

etac = -R0 * np.tan(As) / Vg
fetac = 2.0 * Vg * np.sin(As) / Wl

print(etac, fetac)

Tsa = Na / Fsa

ta = np.linspace(-Tsa / 2.0, Tsa / 2.0, Na)
fa = np.linspace(-Fsa / 2.0, Fsa / 2.0, Na) + fetac
# fa = np.linspace(-Fsa / 2.0, Fsa / 2.0, Na)
ta = np.reshape(ta, (Na, 1))
fa = np.reshape(fa, (Na, 1))


Tsr = 2 * (Rfar - Rnear) / C
tnear = 2 * Rnear / C
tfar = 2 * Rfar / C

# tr = np.linspace(tnear, tfar, Nr)
# tr = np.linspace(-Tsr / 2.0, Tsr / 2.0, Nr) + tnear
tr = np.linspace(-Nr / 2.0, Nr / 2.0, Nr) / Fsr + (tnear + tfar) / 2.0
fr = np.linspace(-Fsr / 2.0, Fsr / 2.0, Nr)
tr = np.reshape(tr, (Nr, 1))
fr = np.reshape(fr, (Nr, 1))


# ------------------------------------------------

nTGs = len(targets)

tas = np.matmul(ta, np.ones((1, Nr)))
trs = np.matmul(np.ones((Na, 1)), tr.transpose())
print(tas.shape, trs.shape)
targets = np.array(targets) + np.array(SC + [0])

Sr = 0
for target in targets:
    print(target)

    x, y, z, G = target

    R = np.sqrt(H**2 + x**2 + (y - V * ta)**2)

    # P = np.hstack((np.zeros((Na, 1)), V * ta, np.ones((Na, 1)) * H))
    # T = np.matmul(np.ones((Na, 1)), np.reshape(target[0:3], (1, 3)))
    # R = np.sqrt(np.sum(np.square(P - T), 1))

    Wr = np.abs(trs - 2 * R / C) < (Tp / 2.0)

    Aeta = np.arctan((tas - etac) * Vg / R0)
    BWa = 0.886 * Wl / La
    Wa = np.sinc(0.886 * Aeta / BWa)
    Wa = Wa**2

    # Wr = 1
    # Wa = 1

    Sr += G * Wr * Wa * np.exp(-1j * 4 * PI * Fc * R / C +
                               1j * PI * Kr * (trs - 2 * R / C)**2)
print("Simulation is done!")


RD = fftshift(fft(
    fftshift(Sr, axes=(0,)), axis=0), axes=0)

# F2D = fft2(Sr)
F2D = fft(RD, axis=1)

cmap = 'jet'
# cmap = 'gray'

extent = ES
extent = SA

plt.figure()
plt.subplot(321)
plt.imshow(np.absolute(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('Time domain (amplitude)')
plt.subplot(322)
plt.imshow(np.angle(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('Time domain (phase)')

plt.subplot(323)
plt.imshow(np.absolute(RD), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('RD domain (amplitude)')
plt.subplot(324)
plt.imshow(np.angle(RD), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('RD domain (phase)')


plt.subplot(325)
plt.imshow(np.absolute(F2D), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('2D frequency domain (amplitude)')
plt.subplot(326)
plt.imshow(np.angle(F2D), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('2D frequency domain (phase)')
plt.tight_layout()
plt.show()


# ------------------------------------------------------


hh = np.exp(1j * 2.0 * np.pi * fetac * fa)
Has = np.reshape(np.repeat(hh, Nr), (Na, Nr))
Sr = Sr * Has

# ---range compression

frs = np.matmul(np.ones((Na, 1)), fr.transpose())
Hrs = np.exp(1j * PI * frs**2 / Kr)

Sr = fftshift(fft(fftshift(Sr, axes=1), axis=1), axes=1)
Sr = Sr * Hrs
Sr = ifftshift(ifft(ifftshift(Sr, axes=1), axis=1), axes=1)

plt.figure()
plt.subplot(321)
plt.imshow(np.absolute(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('After range compression (amplitude)')
plt.subplot(322)
plt.imshow(np.angle(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('After range compression (phase)')


# ---azimuth FFT
Sr = fftshift(fft(fftshift(Sr, axes=0), axis=0), axes=0)
fas = np.matmul(fa, np.ones((1, Nr)))


# ---way2 SRC

D = np.sqrt(1 - (Wl**2) * fas**2 / (4 * Vr**2))
Ksrc = 2 * Vr**2 * Fc**3 * D**3 / (C * R0 * fas**2)
Km = Kr / (1 - Kr / Ksrc)

Hsrc = np.exp(-1j * PI * fas**2 / Ksrc)
Sr = fftshift(fft(fftshift(Sr, axes=1), axis=1), axes=1)  # 2D frequency domain
Sr = Sr * Hsrc
Sr = ifftshift(ifft(ifftshift(Sr, axes=1), axis=1), axes=1)

plt.subplot(323)
plt.imshow(np.absolute(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('After second RC (amplitude)')
plt.subplot(324)
plt.imshow(np.angle(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('After second RC (phase)')


# ---RCMC


plt.subplot(323)
plt.imshow(np.absolute(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('After second RC (amplitude)')
plt.subplot(324)
plt.imshow(np.angle(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('After second RC (phase)')
plt.tight_layout()
plt.show()


# ---Azimuth compression

Has = np.exp(1j * 4 * PI * R0 * D * Fc / C)

Sr = Sr * Has

Sr = ifftshift(ifft(ifftshift(Sr, axes=0), axis=0), axes=0)

plt.figure()

plt.subplot(221)
plt.imshow(np.absolute(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('After azimuth compression (amplitude)')
plt.subplot(222)
plt.imshow(np.angle(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('After azimuth compression (phase)')

Sr = np.flipud(Sr)

plt.subplot(223)
plt.imshow(np.absolute(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('Reconstructed (amplitude)')
plt.subplot(224)
plt.imshow(np.angle(Sr), extent=extent, cmap=cmap)
plt.xlabel('Range')
plt.ylabel('Azimuth')
plt.title('Reconstructed (phase)')

plt.tight_layout()


plt.show()
