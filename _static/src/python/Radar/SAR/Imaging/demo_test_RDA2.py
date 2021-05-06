import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure
import utils
import iprs


C = 299792458.0
PI = 3.1415926535898

As = (90 - 98.6) * PI / 180.0
As = (90 - 90) * PI / 180.0
# As = (90 - 80) * PI / 180.0
Ai = 58.2 * PI / 180.0
Ad = (90 - 58.2) * PI / 180.0
# Ad = (90 - 10.2) * PI / 180.0

F0 = 5.3e9
B = 30e6
Tp = 41.75e-4
Lr = 15.0
La = 1.5

PRF = 1.25698e+03
Fsa = PRF
Fsr = 32.317e+6

H = 793000.0
Vs = 7062
Vg = 7050
Vr = np.sqrt(Vs * Vg)

dt = 1 / (2 * B)


Rc = H / np.cos(PI / 2 - Ad)
Yc = Rc * np.sin(As)
Xc = np.sqrt(Rc**2 - H**2 - Yc**2)

print("Xc, Yc, Rc: ", Xc, Yc, Rc)
XX = 5590

Wl = C / F0
Kr = B / Tp
Ka = 1733
# Ka = (2 * Vr**2) / (Wl * R0)
print("ka: ", Ka, "Wl: ", Wl)

Tsas = 0
Tsae = 1.2219765
Tsa = Tsae - Tsas

Rmin = np.sqrt((Xc - XX)**2 + H**2)
Rmax = np.sqrt((Xc + XX)**2 + H**2)

Tsrs = 2 * Rmin / C
Tsre = 2 * Rmax / C
Tsr = Tsre - Tsrs

print("Tsrs, Tsre, Tsas, Tsae: ", Tsrs, Tsre, Tsas, Tsae)

etas = np.linspace(Tsas, Tsae, Fsa * Tsa)
print(etas.shape)
Na = etas.shape[0]

taus = np.linspace(Tsrs, Tsre, Fsr * Tsr)
print(taus.shape)
Nr = taus.shape[0]

print(Na, Nr)

targets = [[-512, -512, 3.0], [0, 0, 1.0], [512, 512, 1.0]]
targets = [[0, 0, 1.0]]
for tg in targets:
    tg[0] = tg[0] + Xc
    tg[1] = tg[1] + Yc


# s = np.zeros(Na, Nr)
s = []
for eta in etas:
    s_eta = 0.0
    for tg in targets:
        R0 = np.sqrt(H**2 + tg[0]**2)
        eta_c = tg[1] / Vg
        R_eta = np.sqrt(tg[0]**2 + H**2 + (tg[1] - Vr * eta)**2)
        # print("R_eta, eta, eta_c: ", R_eta, eta, eta_c)

        wrs = utils.rect((taus - 2 * R_eta / C) / Tp) * \
            np.exp(1j * PI * Kr * (taus - 2 * R_eta / C)**2)
        wa = utils.sinc(Lr * np.arctan(Vg * (eta - eta_c) / R0) / Wl)**2
        # footprinty = 2 * np.tan(0.886 * Wl / (2 * Lr)) * R0
        # wa = np.sinc((Vg * eta - tg[1]) / footprinty)**2
        tt = utils.rect((taus - 2 * R_eta / C) / Tp)
        # print(taus.min(), taus.max())
        # print("tt ----> min, max", tt.min(), tt.max())
        # print(wrs.max())
        # print("wa: ", wa)
        phase_eta = -1j * 4 * PI * F0 * R_eta / C + \
            1j * PI * Kr * (taus - 2 * R_eta / C)**2
        # print(phase_eta.min(), phase_eta.max())
        s_eta = s_eta + tg[2] * wrs * wa * np.exp(phase_eta)
        # print(np.sum(s_eta), tg[2])
    s.append(s_eta)

s = np.array(s)

print("s.shape", s.shape)
print("s.min, s.max", s.min(), s.max())

extent = [-1024, 1024, -1024, 1024]

# plt.figure()
# plt.imshow(np.abs(s), extent=extent)
# plt.show()


SI = utils.range_dopp1(s=s, Fsr=Fsr, Fsa=Fsa, Kr=Kr, Tp=Tp, Ka=Ka)

SI = np.abs(SI)
SI = exposure.adjust_log(SI)
print("SI.shape: ", SI.shape)

cmap = 'gray'
cmap = None
plt.figure()
plt.subplot(121)
plt.imshow(np.abs(s), cmap=cmap)
plt.title("SAR raw data(Amplitude)")
plt.subplot(122)
plt.imshow(SI, cmap=cmap)
plt.xlabel("Range/m")
plt.xlabel("Azimuth/m")
plt.title("Imaging with RDA")
plt.show()
