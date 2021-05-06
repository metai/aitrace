.. _SectionSubRegionImagingExperimentsSARRadar:

子区域成像实验
=====================


实验说明
---------

从原始较大场景数据中, 选择不同大小的场景区域数据进行成像, 成像方法为调频变标算法(CSA). 一种方法是将选取子区域外的数据置零后成像, 另一种是仅用选取的子区域大小数据成像.


仿真数据实验
------------------------

点目标数据实验
~~~~~~~~~~~~~~~~~~~

实验代码
^^^^^^^^^^^^^^^



实验结果
^^^^^^^^^^^^^^^


真实数据实验
------------------------

RADARSAT1数据实验
~~~~~~~~~~~~~~~~~~~


实验中所用数据为 RADARSAT1 卫星获得的数据, 成像区域为史丹利公园 (Stanley Park), 有关RADARSAT1的参数信息, 可参考 :ref:`Section-RADARSATRadarProductSupplementRadar` 小节.



.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_StanleyPark.*
   :scale: 80 %
   :align: center

   Stanley Park 区域原始数据幅度与成像结果


.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_StanleyPark_SubRegion.*
   :scale: 80 %
   :align: center

   对成像后的Stanley Park地区影像, 选取场景中心附近不同大小的区域可视化结果.


实验代码
^^^^^^^^^^^^^^^

.. code-block:: python
    :lineno-start: 0
    :emphasize-lines: 9
    :linenos:
    :caption: demo_RADARSAT1_SubRegion.py
    :name: bind-id

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # @Date    : 2019-02-18 10:14:12
    # @Author  : Yan Liu & Zhi Liu (zhiliu.mind@gmail.com)
    # @Link    : http://iridescent.ink
    # @Version : $1.0$

    import iprs
    import numpy as np
    import scipy.io as scio
    import matplotlib.pyplot as plt

    imagingMethod = 'RDA'
    # imagingMethod = 'OmegaK'
    imagingMethod = 'CSA'

    zpadar = (512, 512)
    # zpadar = False
    # zpadar = None
    usesrc = True
    # usesrc = False
    usedpc = True
    # usedpc = False
    rcmc = False
    rcmc = 32

    fulltime = False
    # fulltime = True

    usemask = False
    # usemask = True

    sensor_name = 'RADARSAT1'
    acquis_name = 'RADARSAT1'

    sarplat = iprs.SarPlat()
    sarplat.name = "sensor=" + sensor_name + "_acquisition=" + acquis_name
    sarplat.sensor = iprs.SENSORS[sensor_name]
    sarplat.acquisition = iprs.ACQUISITION[acquis_name]
    sarplat.params = None


    ROI = {
        'SubSceneArea': None,  # SceneArea
        # 'SubSceneArea': [0.5, 0.5, 0.5, 0.5],  # SceneArea/2.0
        # 'SubEchoSize': None,  # EchoSize
        'SubEchoSize': [1., 1.],
        # 'SubEchoSize': [1. / 3, 1. / 4],
        # 'SubEchoSize': [1. / 6, 1. / 8],
        'SubEchoSize': [1. / 12, 1. / 16],
    }

    sarplat.selection = ROI
    ROIY = sarplat.selection['SubEchoSize'][0]
    ROIX = sarplat.selection['SubEchoSize'][1]

    # sarplat.selection = None
    NstartX = int(sarplat.acquisition['EchoSize'][1] / 2. - ROIX / 2.)
    NstartY = int(sarplat.acquisition['EchoSize'][0] / 2. - ROIY / 2.)


    if fulltime:
        mask = np.zeros(sarplat.acquisition['EchoSize'])
        sarplat.selection = None

    sarplat.select()
    sarplat.printsp()

    SA = sarplat.selection['SubSceneArea']

    disk = '/mnt/d/'
    # disk = 'D:/'
    # datafile = disk + 'DataSets/sar/RADARSAT/frombooks/mat/sardataRADARSAT1scene01AzimuthBlock1.mat'
    # datafile = disk + 'DataSets/sar/RADARSAT/frombooks/mat/sardataRADARSAT1scene01AzimuthBlock1_Squamish.mat'
    # datafile = disk + 'DataSets/sar/RADARSAT/frombooks/mat/sardataRADARSAT1scene01AzimuthBlock1_VancouverAirport.mat'
    # datafile = disk + 'DataSets/sar/RADARSAT/frombooks/mat/sardataRADARSAT1scene01AzimuthBlock1_Brackendale.mat'
    datafile = disk + 'DataSets/sar/RADARSAT/frombooks/mat/sardataRADARSAT1scene01AzimuthBlock1_EnglishBayShips.mat'
    datafile = disk + 'DataSets/sar/RADARSAT/frombooks/mat/sardataRADARSAT1scene01AzimuthBlock1_StanleyPark.mat'
    # datafile = disk + 'DataSets/sar/RADARSAT/frombooks/mat/sardataRADARSAT1scene01AzimuthBlock1_UBC.mat'
    # datafile = disk + 'DataSets/sar/RADARSAT/frombooks/mat/sardataRADARSAT1scene01AzimuthBlock2_River.mat'


    data = scio.loadmat(datafile, struct_as_record=True)

    temp = data['sardata']
    temp = temp['rawdata'][0][0]

    NendY = NstartY + ROIY
    NendX = NstartX + ROIX

    if fulltime:
        Sr = np.zeros_like(temp)
        Sr[NstartY:NendY, NstartX:NendX] = temp[NstartY:NendY, NstartX:NendX]
        mask[NstartY:NendY, NstartX:NendX] = 1
    else:
        Sr = temp[NstartY:NendY, NstartX:NendX]

    print(NstartY, NstartX, NendY, NendX)

    Na, Nr = Sr.shape
    print("SAR raw data: ", Sr.shape, Sr.dtype)


    if imagingMethod is 'RDA':
        # SI, _, _ = iprs.rda(Sr, sarplat, verbose=True)
        SI = iprs.rda_adv(Sr, sarplat, zpadar=zpadar,
                          usesrc=usesrc, usedpc=usedpc, rcmc=rcmc, verbose=False)
    if imagingMethod is 'CSA':
        # SI = iprs.csa(Sr, sarplat, verbose=True)
        SI = iprs.csa_adv(Sr, sarplat, zpadar=zpadar,
                          usesrc=usesrc, rcmc=rcmc, usedpc=usedpc, verbose=False)

    SI = np.abs(SI)

    data = {'SI': SI}
    scio.savemat('./SI.mat', data)

    print(SI.max(), SI.min())

    SI = SI / SI.max()
    print(SI.max(), SI.min())
    SI = 20 * np.log10(SI + iprs.EPS)
    print(SI.max(), SI.min())
    # a = np.abs(SI.mean())
    a = 50

    SI = (SI + a) / a * 255
    print(SI.max(), SI.min())
    # SI = exposure.adjust_log(SI + iprs.EPS)
    # SI = SI * 255
    # SI = exposure.adjust_log(SI)
    SI[SI < 0] = 0
    SI = SI.astype('uint8')
    SI = np.flipud(SI)

    if fulltime and usemask:
        SI = SI * mask

    print("SI.shape: ", SI.shape)

    Title = 'Imaging result of RDA('

    Title = 'Imaging Result of ' + imagingMethod


    if usesrc or rcmc:
        Title = Title + '\n ('
        if usesrc:
            Title = Title + 'SRC+'
        if rcmc:
            Title = Title + 'RCMC+'
    if usedpc:
        Title = Title + 'DPC'

    Title = Title + ")"


    cmap = 'gray'
    # cmap = 'hot'
    # cmap = None

    extent = SA
    extent = None

    plt.figure()
    plt.subplot(211)
    plt.imshow(np.abs(Sr), cmap=cmap)
    plt.title("SAR raw data(Amplitude)")
    plt.xlabel("Range")
    plt.ylabel("Azimuth")
    plt.subplot(212)
    plt.imshow(SI, extent=extent, cmap=cmap)
    plt.title(Title)
    plt.xlabel("Range")
    plt.ylabel("Azimuth")
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.imshow(SI, extent=extent, cmap='gray')
    plt.xlabel("Range/m")
    plt.ylabel("Azimuth/m")
    plt.title(Title)
    plt.show()


实验结果
^^^^^^^^^^^^^^^

观察实验结果可以发现, 场景中某一目标信息会分布在回波数据的不同位置, 如果仅选取目标附近子区域成像, 会使得信息丢失, 成像模糊.

.. _fig-RADARSAT1_SubRegion512_FullTime_UseMaskFalse:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_SubRegion512_FullTime_UseMaskFalse.*
   :scale: 80 %
   :align: center

   选取子区域大小 :math:`512\times 512`, 子区域外的数据做补零处理后进行成像.


.. _fig-RADARSAT1_SubRegion512_FullTime_UseMaskTrue:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_SubRegion512_FullTime_UseMaskTrue.*
   :scale: 80 %
   :align: center

   选取子区域大小 :math:`512\times 512`, 子区域外的数据做补零处理后进行成像, 成像后子区域外成像数据被置零且进行局部放大后显示.


.. _fig-RADARSAT1_SubRegion512_PartlTime:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_SubRegion512_PartlTime.*
   :scale: 80 %
   :align: center

   选取子区域大小 :math:`512\times 512`, 仅选取的数据被用来成像.




.. _fig-RADARSAT1_SubRegion256_FullTime_UseMaskFalse:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_SubRegion256_FullTime_UseMaskFalse.*
   :scale: 80 %
   :align: center

   选取子区域大小 :math:`256\times 256`, 子区域外的数据做补零处理后进行成像.


.. _fig-RADARSAT1_SubRegion256_FullTime_UseMaskTrue:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_SubRegion256_FullTime_UseMaskTrue.*
   :scale: 80 %
   :align: center

   选取子区域大小 :math:`256\times 256`, 子区域外的数据做补零处理后进行成像, 成像后子区域外成像数据被置零且进行局部放大后显示.


.. _fig-RADARSAT1_SubRegion256_PartlTime:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_SubRegion256_PartlTime.*
   :scale: 80 %
   :align: center

   选取子区域大小 :math:`256\times 256`, 仅选取的数据被用来成像.




.. _fig-RADARSAT1_SubRegion128_FullTime_UseMaskFalse:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_SubRegion128_FullTime_UseMaskFalse.*
   :scale: 80 %
   :align: center

   选取子区域大小 :math:`128\times 128`, 子区域外的数据做补零处理后进行成像.


.. _fig-RADARSAT1_SubRegion128_FullTime_UseMaskTrue:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_SubRegion128_FullTime_UseMaskTrue.*
   :scale: 80 %
   :align: center

   选取子区域大小 :math:`128\times 128`, 子区域外的数据做补零处理后进行成像, 成像后子区域外成像数据被置零且进行局部放大后显示.


.. _fig-RADARSAT1_SubRegion128_PartlTime:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/SubRegionImaging/RADARSAT1_SubRegion128_PartlTime.*
   :scale: 80 %
   :align: center

   选取子区域大小 :math:`128\times 128`, 仅选取的数据被用来成像.
