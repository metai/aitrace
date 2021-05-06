import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio
from skimage import exposure
import iprs
import utils
EPS = 2.2e-16

datafile = '/mnt/d/DataSets/sar/RADARSAT/frombooks/mat/sardataRADARSAT1scene01.mat'
# datafile = '/mnt/d/DataSets/sar/RADARSAT/frombooks/mat/sardataRADARSAT1scene02.mat'


data = scio.loadmat(datafile, struct_as_record=True)

temp = data['sardata']
s = temp['rawdata'][0][0]
Na, Nr = s.shape
print("SAR raw data: ", s.shape, s.dtype)

C = 299792458.0
PI = 3.1415926535898

As = 1.58 * PI / 180.0
Ad = (90 - 58.2) * PI / 180.0

F0 = 5.3e9
B = 30e6
Kr = -0.72135e+12
Ka = 1733
Tp = 41.75e-6
Lr = 15.0
La = 1.5

fc = -6900

PRF = 1.25698e+03
Fsa = PRF
Fsr = 32.317e+6

H = 793000.0
Vs = 7062
Vg = 7050
Vr = np.sqrt(Vs * Vg)

R0 = 0.0100386 * C / 2.0
# R0 = 6.5956e-3 * C / 2.0

R0 = R0 * np.cos(As)

Wl = C / F0
Ka = (2 * Vr**2) / (Wl * R0)
print(Ka, "ka")
print(R0, "R0")
R0 = H / np.cos(PI / 2 - Ad)
print(R0, "R0")


fetac = 2 * Vs * np.sin(As) / Wl


# SI = utils.range_dopp1(s=s, Fsr=Fsr, Fsa=Fsa, Kr=Kr, Tp=Tp, Ka=Ka)

SI = utils.range_dopp(s=s, Fsr=Fsr, Fsa=Fsa, Kr=Kr,
                      Tp=Tp, V=Vs, F0=F0, R0=R0, fetac=fetac)

SI = np.abs(SI)

SI = SI / SI.max()
# SI = 20 * np.log10(SI + EPS)
# SI = exposure.adjust_log(SI + EPS)
SI = SI * 255
SI = exposure.adjust_log(SI + EPS)
# SI.astype('uint8')

print("SI.shape: ", SI.shape)

Title = 'Imaging result of RDA('


if usesrc:
    Title = Title + 'SRC'
if usermc:
    Title = Title + '+RCM'

Title = Title + ")"

cmap = 'gray'
cmap = None


plt.figure()
plt.subplot(211)
plt.imshow(np.abs(s), cmap=cmap)
plt.title("SAR raw data(Amplitude)")
plt.xlabel("Range")
plt.ylabel("Azimuth")
plt.subplot(212)
# plt.imshow(SI, extent=extent, cmap=cmap)
plt.imshow(SI, cmap=cmap)
plt.xlabel("Range/m")
plt.ylabel("Azimuth/m")
plt.title(Title)
plt.show()
