import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio
from skimage import exposure
import iprs
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

As = (90 - 98.6) * PI / 180.0
Ad = (90 - 58.2) * PI / 180.0

F0 = 5.3e9
B = 30e6
Kr = 0.72135e+12
Ka = 1733
Tp = 41.75e-6
Lr = 15.0
La = 1.5

PRF = 1.25698e+03
Fsa = PRF
Fsr = 32.317e+6

H = 793000.0
Vs = 7062
Vg = 7050
Vr = np.sqrt(Vs * Vg)

R0 = 0.0100386 * C / 2.0
R0 = 6.5956e-3 * C / 2.0

Wl = C / F0
Ka = (2 * Vr**2) / (Wl * R0)
print(Ka, "ka")
print(R0, "R0")
R0 = H / np.cos(PI / 2 - Ad)
print(R0, "R0")

# =================range compression
# -----------------Step1: FFT in range

Sr = np.fft.fft(s, axis=1)
# ftaus = np.fft.fftshift(np.fft.fftfreq(Nr, 1.0 / Fsr))
ftaus = np.linspace(-Fsr / 2.0, Fsr / 2.0, Nr)
print(ftaus)
print("ftaus.shape: ", ftaus.shape, np.min(ftaus), np.max(ftaus))
print("after FFT in range: ", Sr.shape, Sr.dtype)

# -----------------Step2: Filter in range
# Hr = iprs.rect(ftaus / (np.abs(Kr) * Tp)) * np.exp(1j * PI * ftaus**2 / Kr - PI/4)
Hr = iprs.rect(ftaus / (np.abs(Kr) * Tp)) * \
    np.exp(1j * PI * ftaus**2 / Kr)

print("Hr.shape: ", Hr.shape)


Hrs = np.reshape(np.repeat(Hr, Na), (Nr, Na)).transpose()

print(Hrs.shape, Hrs[0, 10], Hrs[1, 10], Hrs[3, 10])
print(Hrs.shape, Hrs[10, 0], Hrs[10, 1], Hrs[10, 3])

Srf = Sr * Hrs

print("Srf.shape; ", Srf.shape)

# -----------------Step3: IFFT in range
Src = np.fft.ifft(Srf, axis=1)


# =================azimuth FFT
# -----------------Step4: FFT in azimuth
Sa = np.fft.fft(Src, axis=0)

# =================RCMC
# -----------------Step5: RCMC
Srcmc = Sa


# =================azimuth compression
# -----------------Step6: Filter in azimuth
fetas = np.linspace(-Fsa / 2.0, Fsa / 2.0, Na)
Ha = np.exp(-1j * (PI * fetas**2) / Ka)
print("Ha.shape: ", Ha.shape)
Has = np.reshape(np.repeat(Ha, Nr), (Na, Nr))
print("Has.shape: ", Has.shape)
print(Has.shape, Has[0, 10], Has[1, 10], Has[3, 10])
print(Has.shape, Has[10, 0], Has[10, 1], Has[10, 3])

Saf = Srcmc * Has
print("Saf.shape: ", Saf.shape)
# -----------------Step7: IFFT in azimuth
SI = np.fft.ifft(Saf, axis=0)


SI = np.abs(SI)
SI = exposure.adjust_log(SI)
print("SI.shape: ", SI.shape)

cmap = 'gray'
plt.figure()
plt.subplot(121)
plt.imshow(np.abs(s), cmap=cmap)
plt.subplot(122)
plt.imshow(SI, cmap=cmap)
plt.xlabel("Range/m")
plt.xlabel("Azimuth/m")
plt.title("Imaging with RDA")
plt.show()
