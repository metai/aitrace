import numpy as np
from utils import *
import matplotlib.pyplot as plt


Re = Rea
Re = Ree
Re = Rep

Fc = 5.3e9  # Hz
H = 807000.0  # height in m
V = 7062.0  # velocity in m/s
Tp = 41.750e-06  # Range pulse length in seconds
Kr = -7.2135e+11  # FM rate of radar pulse (Hz/s)
Lra = 1.5  # antenna length (range) in m
Laa = 15  # antenna length (azimuth) in m
PRF = 1.25698e+03  # Hz
Fs = 32.317e+6

As = -1.58 * PI / 180.0  # squint angle
Ad = 53.0 * PI / 180.0  # depression angle
Ar = 10.6 * PI / 180.0  # beam angle (range) Nsr = 9288
Ar = 3.3420 * PI / 180.0  # beam angle (range) Nsr = 9288
EchoSize = [19438, 9288]


# Fc = 5.3e9  # Hz
# H = 780000  # height in m
# V = 7098.0194  # velocity in m/s
# Tp = 37.12e-06  # Range pulse length in seconds
# Kr = 4.18989015e+11  # FM rate of radar pulse (Hz/s)
# Lra = 1  # antenna length (range) in m
# Laa = 10  # antenna length (azimuth) in m
# PRF = 1.679902e+03  # Hz
# Fs = 18.962468e+6

# As = 0.0  # squint angle
# Ad = 72.6 * PI / 180.0  # depression angle
# Ar = 7.861307 * PI / 180.0  # beam angle (range)
# EchoSize = [28659, 5616]


Rs = Re + H

To = 2 * PI * np.sqrt((Rs)**3 / Ge)  # the orbital period
Ws = 2 * PI / To
Vs = Rs * Ws

Rg = ((Re + H) + np.tan(Ad) * np.sqrt((Re * np.tan(Ad))**2 - 2 * H * Re - H**2)) / (1 + np.tan(Ad)**2)
# Rg = ((Re + H) - np.tan(Ad) * np.sqrt((Re * np.tan(Ad))**2 - 2 * H * Re - H**2)) / (1 + np.tan(Ad)**2)


Vg = Rg * Ws
Vr = np.sqrt(Vg * Vs)
print(To / 60., Vs, Vg, Vr, "To, Vs, vg, Vr")

Vr = V
Vg = Vr**2 / Vs

print(To / 60., Vs, Vg, Vr, "To, Vs, vg, Vr")
print(Re, H, Rs)


Fas = PRF
Frs = Fs

Tas = 1. / Fas
Trs = 1. / Frs


Rnear = H / np.sin(Ad + Ar / 2.0)
Rfar = H / np.sin(Ad - Ar / 2.0)
Srfp = np.sqrt(Rfar**2 + Rnear**2 - 2. * Rnear * Rfar * np.cos(Ar) + EPS)
Sswath = Rfar - Rnear

print(Srfp, Sswath, "Srfp, Sswath")

Rsc = 0.5 * np.sqrt(2. * Rfar**2 + 2. * Rnear**2 - Srfp**2 + EPS)
Rbc = H / np.sin(Ad)

Rs0 = Rsc * np.cos(As)
Rb0 = Rbc * np.cos(As)

Ysc = Rsc * np.sin(As)
Xsc = np.sqrt(np.abs(Rs0**2 - H**2))
SC = [Xsc, Ysc, 0.0]
Ybc = Rbc * np.sin(As)
Xbc = np.sqrt(np.abs(Rb0**2 - H**2))
BC = [Xbc, Ybc, 0.0]

print(Xsc, Xbc, "Xsc, Xbc")
print((Rs - Rg) / np.sin(Ad))

R0 = Rs0
# R0 = Rb0

Wl = C / Fc
Br = np.abs(Kr) * Tp
Lsa = Wl * R0 / Laa
Tsa = Lsa / V

tnear = 2. * Rnear / C
tfar = 2. * Rfar / C

Tr = tfar - tnear
Nr = int(Frs * Tr)
Ta = Tsa * 2
Na = int(Fas * Ta)


print(2 * H / C)

print("Tp, tnear:", Tp, tnear)
print("Tas, tfar, tfar-tnear + Tp: :", Tas, tfar, tfar - tnear + Tp)
print(Tas / tfar)
assert(Tp < tnear)
assert(Tas > (tfar - tnear) + Tp)

print(Na, Nr)

tr = np.linspace(tnear, tfar, Nr)
ta = np.linspace(-Ta / 2., Ta / 2., Na)

fr = np.linspace(-Frs / 2., Frs / 2., Nr)
fa = np.linspace(-Fas / 2., Fas / 2., Na)

BWa = 0.886 * Wl / Laa

a = 600
targets = [
    # [-700, -400, 0, 0, 0, 0, 1],
    [a, a, 0, 0, 0, 0, 1],
    # [a, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1],
    # [0, a, 0, 0, 0, 0, 1],
    # [-a, -a, 0, 0, 0, 0, 1],

    # [-100, -50, 0, 0, 0, 0, 1],
    # [-100, -51, 0, 0, 0, 0, 1],
    # [-100, -52, 0, 0, 0, 0, 1],
    # [-100, 50, 0, 0, 0, 0, 1],
    # [-100, 51, 0, 0, 0, 0, 1],
    # [-100, 52, 0, 0, 0, 0, 1],
    # [0, 0, 0, 0, 0, 0, 1],
    # [0, 1, 0, 0, 0, 0, 1],
    # [0, 2, 0, 0, 0, 0, 1],
    # [100, -50, 0, 0, 0, 0, 3],
    # # [100, -51, 0, 0, 0, 0, 1],
    # # [100, -52, 0, 0, 0, 0, 1],
    # [100, 50, 0, 0, 0, 0, 3],
    # # [100, 51, 0, 0, 0, 0, 1],
    # # [100, 52, 0, 0, 0, 0, 1],
]

# waf = lambda t: antenna_pattern_azimuth(Wl, Laa, Ata(t))
waf = lambda t, R0: antenna_pattern_azimuth(Wl, Laa, np.arctan(Vg * t) / R0)**2
wrf = lambda t: rect(t / Tp)  # wr function


nTGs = len(targets)

targets = np.array(targets)
targets = targets.astype('float')
targets[:, 0] = targets[:, 0] + SC[0]
targets[:, 1] = targets[:, 1] + SC[1]

# targets[:, 0] = targets[:, 0] + BC[0]
# targets[:, 1] = targets[:, 1] + BC[1]

t2 = 0.5 * (ta ** 2)

trs = np.repeat(tr, Na).reshape(Nr, Na).transpose()  # [Na, Nr]
tas = np.repeat(ta, Nr).reshape(Na, Nr)  # [Na, Nr]
tac = Ysc / Vg
Sr = 0.
for n in range(nTGs):
    target = targets[n]
    x0, y0, vx, vy, ax, ay, G0 = target

    R0R0 = x0**2 + H**2
    R0 = np.sqrt(R0R0)
    print(R0)
    # R0 = Rs0
    R0 = R0 * np.ones((Na, Nr))  # [Na, Nr]
    Rta = np.sqrt(R0R0 + (Vg * ta)**2)  # [Na, 1]

    x = x0 + vx * ta + ax * t2  # [Na, 1]
    y = y0 + vy * ta + ay * t2 - Vg * ta  # [Na, 1]

    R = np.sqrt(x ** 2 + y ** 2 + H ** 2)  # [Na, 1]
    # Rta = R

    # print(Rta)
    # print(R)
    # print(np.sum(np.abs(R-Rta)) / Na)

    tac = y0 / Vg

    Rta = np.repeat(Rta, Nr).reshape(Na, Nr)  # [Na, Nr]
    phase1 = -1j * (4 * PI * Fc * Rta / C)
    phase2 = 1j * PI * Kr * (trs - 2 * Rta / C)**2

    # Wa = waf(tas - tac, R0)
    Wa = np.sinc(0.886 * np.arctan((tas * V - y0) / R0) / BWa)**2
    Wr = wrf((trs - 2 * Rta / C))

    print(Wa.shape, Wr.shape)

    Sr += G0 * Wa * Wr * np.exp(phase1 + phase2)

print(Sr.shape)
print(Sr.min(), Sr.max())


plt.figure()
plt.subplot(121)
plt.imshow(np.abs(Sr))
plt.subplot(122)
plt.imshow(np.angle(Sr))
plt.show()


R0 = Rs0
Yc = Ysc
rcmc = 32
tac = Ysc / Vg
fadc = 2 * (Vr**2) * tac / (Wl * Rsc)
print(Yc, R0, tac, fadc)
SI = chirp_scaling(Sr, ta, tr, fa, fr, tnear, tfar, Tp, Fc, Kr, V, Vr, fadc, R0,
                   Yc, zpadar=False, usesrc=True, rcmc=None, usedpc=True, verbose=True)

print(SI.min(), SI.max())

SIlog = 20 * np.log10(np.abs(SI) + EPS)

plt.figure()
plt.subplot(221)
plt.imshow(np.abs(SI))
plt.subplot(222)
plt.imshow(np.angle(SI))
plt.subplot(223)
plt.imshow(SIlog)
plt.subplot(224)
plt.imshow(np.abs(SI))
plt.show()
