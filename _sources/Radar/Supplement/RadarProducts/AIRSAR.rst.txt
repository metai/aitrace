.. _Section-AIRSARRadarProductSupplementRadar:

AIRSAR 产品介绍
=====================


AIRSAR 简介
--------------------------

AIRSAR (AIRborne Synthetic Aperture Radar) 是由美国国家航空和航天局 (National Aeronautics and Space Administration, NASA) 的喷气推进实验室（Jet Propulsion Laboratory, JPL）设计和建造的一种机载合成孔径雷达. 机载合成孔径雷达是一种能够穿透云层并在夜间收集数据的全天候成像工具, 更长的波长也可以穿透森林冠层和和薄的沙层与积雪, 被广泛用于地形观测. AIRSAR于1988年首次飞行, 并于2004年完成了最后一次飞行任务, 飞机以每秒215米的速度在平均地形上空8公里的高度飞行.

有关 AIRSAR 的信息可在 `这里 <https://airsar.jpl.nasa.gov/index.html>`_ 和 `这里 <https://asf.alaska.edu/data-sets/sar-data-sets/airsar/>`_  查看. 从 `ASF <https://www.asf.alaska.edu/>`_ 上可以下载 AIRSAR 产品数据, 可获得的数据格式如下:

- PolSAR: 3-frequency polarimetry
- TOPSAR: C-, L-, and P-band Compressed Stokes Matrix, C-band TIFF, DEM
- ATI: Interferograms



AIRSAR 雷达参数与工作模式
~~~~~~~~~~~~~~~~~~~~~~~

.. table:: AIRSAR平台参数
   :name: table-ParametersAIRSARPlatform

   +--------------------------+----------------+----------------+-----------------+
   |                          | P-band         | L-band         | C-band          |
   +==========================+================+================+=================+
   | Flight altitude          | 8km            | 8km            | 8km             |
   +--------------------------+----------------+----------------+-----------------+
   | Flight velocity          | 215m/s         | 215m/s         | 215m/s          |
   +--------------------------+----------------+----------------+-----------------+
   | Frequency/wavelength     | 0.45 GHz/67 cm | 1.26 GHz/23 cm | 5.31 GHz/5.7 cm |
   +--------------------------+----------------+----------------+-----------------+
   | Polarization             | Full           | Full           | Full            |
   +--------------------------+----------------+----------------+-----------------+
   | Range Resolution         | 7.5 m          | 3.75 m         | 1.875 m         |
   +--------------------------+----------------+----------------+-----------------+
   | Swath Width (nominal)    | 10 km          | 10 km          | 10 km           |
   +--------------------------+----------------+----------------+-----------------+
   | Off-Nadir Angle (normal) | 20-60°         | 20-60°         | 20-60°          |
   +--------------------------+----------------+----------------+-----------------+



AIRSAR有三种工作模式, 分别为: 极化合成孔径雷达 (POLarimetric Synthetic Aperture Radar, POLSAR) 模式, 渐进扫描地形观测合成孔径雷达 (Terrain Observation by Progressive scans Synthetic Aperture Radar, TOPSAR) 模式, 以及沿轨干涉 (Along Track Interferometry, ATI) 模式.



POLSAR Data Operation Mode
In POLSAR mode, fully polarimetric data are acquired at all three frequencies in P-, L-, C-band for 40 Mhz or 20 Mhz.  The L-band also provides 80 MHz bandwidth data.   Fully polarimetric means that radar waves are transmitted and received in both horizontal (H) and vertical (V) polarizations.  POLSAR data are sensitive to the geometry (including vegetation) and dielectrical properties (water content) of the terrain.



TOPSAR Data Operation Mode

In TOPSAR mode, AIRSAR collects interferometric data using C- and L-band vertically-displaced antenna pairs to produce digital elevation models (DEM's). The radars which are not being used for interferometry (P-band for XTI2 or P-band and L-band for XTI1) collect quad-pol data co-registered with the C-band DEM.  Interferometric data can be collected in "ping-pong" mode, where each antenna is used alternately for transmit and the effective baseline is doubled, and in "common-transmitter" mode where only one antenna is used for transmit.



ATI Data Operation Mode (Experimental)

Data collected in the along-track interferometry (ATI) mode can be used to measure ocean current velocities.  Two pairs of antennas, one C-band and one L-band, separated along the body of the plane, are used to collect ATI data.



数据读取
----------------------






数据成像
----------------------



