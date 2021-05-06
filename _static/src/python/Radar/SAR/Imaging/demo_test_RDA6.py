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

sarfile = '/mnt/d/DataSets/zhi/SAR/MiniSAR/sensor=DIY4_acquisition=DIY4_gaoxiong001.pkl'

sardata, sarplat = iprs.sarread(sarfile)
s = sardata.rawdata
print(sardata.name)

sarplat.printsp()

imagingMethod = 'RangeDoppler'
# imagingMethod = 'OmegaK'
# imagingMethod = 'ChirpScaling'


R0 = sarplat.params['R0']
Rc = sarplat.params['Rc']
Fsr = sarplat.params['Fs']
Fsa = sarplat.params['PRF']
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
SI = utils.range_dopp(s=s, Fsr=Fsr, Fsa=Fsa, Kr=Kr,
                      Tp=Tp, V=V, F0=F0, R0=R0, fetac=fetac)

SI = np.abs(SI)
# SI = exposure.adjust_log(SI)
print("SI.shape: ", SI.shape, SI.min(), SI.max())

cmap = 'gray'
# cmap = None
plt.figure()
plt.subplot(211)
plt.imshow(np.abs(s), cmap=cmap)
plt.title("SAR raw data(Amplitude)")
plt.subplot(212)
plt.imshow(SI, cmap=cmap)
plt.xlabel("Range/m")
plt.xlabel("Azimuth/m")
plt.title("Imaging with RDA")
plt.show()
