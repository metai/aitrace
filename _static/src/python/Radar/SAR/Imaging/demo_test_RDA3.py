import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure
import utils
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-18 10:14:12
# @Author  : Yan Liu & Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import iprs

sensor_name = 'DIY4'
acquis_name = 'DIY4'

# sensor_name = 'DIY3'
# acquis_name = 'DIY3'

sarplat = iprs.SarPlat()
sarplat.name = "sensor=" + sensor_name + "_acquisition=" + acquis_name
sarplat.sensor = iprs.SENSORS[sensor_name]
sarplat.acquisition = iprs.ACQUISITION[acquis_name]
sarplat.params = None
sarplat.printsp()

SC = sarplat.acquisition['SceneCenter']
Xc = SC[0]
Yc = SC[1]
SA = sarplat.acquisition['SceneArea']

datasetname = 'point'
outfolder = '../data/sar/point/'

imagingMethod = 'RangeDoppler'
# imagingMethod = 'OmegaK'
# imagingMethod = 'ChirpScaling'

# targets = [
#     [100, 100, 0, 0, 0, 0, 1],
#     [-150, -50, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 1],
#     [200, 0, 0, 0, 0, 0, 1],
#     [200, 0, 0, 0, 0, 0, 1],
#     [500, -500, 0, 0, 0, 0, 1],
# ]

targets = [
    [-300, 300, 0, 0, 0, 0, 1],
    [20, 200, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [-50, -200, 0, 0, 0, 0, 1],
    [30, -200, 0, 0, 0, 0, 1],
]

print(targets)

Sr, ta, tr = iprs.tgs2rawdata(sarplat, targets, verbose=False)

print(Sr.shape)
# visualize
iprs.show_amplitude_phase(Sr)

imgshape = (SA[1] - SA[0], SA[3] - SA[2])

SrI = iprs.show_targets(targets, imgshape)


R0 = sarplat.params['R0']
Rc = sarplat.params['Rc']
Fsr = sarplat.params['Fs']
Fsa = sarplat.params['Fa']
Nr = sarplat.params['Nr']
Na = sarplat.params['Na']
Tp = sarplat.sensor['Tp']
Kr = sarplat.sensor['Kr']
V = sarplat.sensor['V']
F0 = sarplat.sensor['Fc']
Wl = sarplat.sensor['Wl']
As = sarplat.acquisition['As']

Ka = (2 * V**2) / (Wl * R0)

Vs = V

fetac = 2 * Vs * np.sin(As) / Wl


# SI = utils.range_dopp1(Sr, Fsr=Fsr, Fsa=Fsa, Kr=Kr, Tp=Tp, Ka=Ka)
SI = utils.range_dopp(s=Sr, Fsr=Fsr, Fsa=Fsa, Kr=Kr,
                      Tp=Tp, V=V, F0=F0, R0=R0, fetac=fetac)

SI = np.abs(SI)
# SI = exposure.adjust_log(SI)
print("SI.shape: ", SI.shape, SI.min(), SI.max())

Title = 'Imaging result of RDA('


if usesrc:
    Title = Title + 'SRC'
if usermc:
    Title = Title + '+RCM'

Title = Title + ")"

cmap = 'gray'
cmap = None

extent = SA

plt.figure()
plt.subplot(211)
plt.imshow(np.abs(Sr), cmap=cmap)
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