.. _Section-UAVSARRadarProductSupplementRadar:

UAVSAR 产品介绍
=====================


UAVSAR 简介
--------------------------

UAVSAR (Uninhabited/Unmanned Aerial Vehicle Synthetic Aperture Radar) 是由美国国家航空和航天局 (National Aeronautics and Space Administration, NASA) 的喷气推进实验室（Jet Propulsion Laboratory, JPL）设计和建造的一种无人驾驶飞行器合成孔径雷达, 属于机载合成孔径雷达的一种, 专门被设计用于获取机载重复轨道SAR数据, 从而用于差分干涉测量. UAVSAR 于2007年8月发射, 服役至今(2020年). 有关 UAVSAR 的信息可在 `这里 <https://uavsar.jpl.nasa.gov/>`_ 和 `这里 <https://asf.alaska.edu/data-sets/sar-data-sets/uavsar/>`_   查看, 从 `ASF <https://www.asf.alaska.edu/>`_ 和 `JPL <https://uavsar.jpl.nasa.gov/cgi-bin/data.pl>`_  上均可以下载 UAVSAR 产品数据.

- PolSAR: MLC, Compressed Stokes Matrix, Ground Projected Complex, Pauli Decomposition
- RPI: Interferogram, Ground Projected Interferogram, Amplitude, Ground Projected Amplitude


UAVSAR 平台参数与工作模式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:table:numref:`table-ParametersUAVSARPlatform`

详细的参数参见 `这里 <https://earth.esa.int/web/eoportal/airborne-sensors/uavsar>`_



.. table:: UAVSAR平台参数
   :name: table-ParametersUAVSARPlatform

   +-------------------------------+-------------------+
   | Frequency                     | L-band            |
   +===============================+===================+
   | Flight altitude               | 13.8km            |
   +-------------------------------+-------------------+
   | Flight velocity               | Full              |
   +-------------------------------+-------------------+
   | Frequency                     | 1.26GHz          |
   +-------------------------------+-------------------+
   | Bandwidth                     | 80MHz             |
   +-------------------------------+-------------------+
   | Pulse width                   | 30ms              |
   +-------------------------------+-------------------+
   | Antenna size (azimuth, range) | 1.6m × 0.5m       |
   +-------------------------------+-------------------+
   | Polarization                  | Quad Polarization |
   +-------------------------------+-------------------+
   | Transmit power                | 2.0kW             |
   +-------------------------------+-------------------+
   | Resolution (azimuth, range)   | 0.8m × 1.8m      |
   +-------------------------------+-------------------+
   | Swath Width                   | 16km             |
   +-------------------------------+-------------------+
   | Pulse repetition frequency    | 387.60Hz          |
   +-------------------------------+-------------------+
   | Ground speed range            | 100 - 250m/s     |
   +-------------------------------+-------------------+
   | Look angle range              | 25º - 65º         |
   +-------------------------------+-------------------+



AIRSAR有两种工作模式, 分别为: 极化合成孔径雷达 (POLarimetric Synthetic Aperture Radar, POLSAR) 模式, 重复轨道干涉合成孔径雷达 (Repeat Pass Interferometry, RPI) 模式


数据读取
----------------------




多视数据
~~~~~~~~~~~~~~~~~~~~~~~~

多视数据文件后缀名为 ``.mlc``, 其中为数据的二进制值, 每个浮点数占4字节, 按行顺序存储, 若为复数数据, 则按实部虚部的顺序存储, 在MATLAB中可以使用如下代码读取::


   im_size = [3185, 5843];
   im_size_c = im_size.*[2,1];

   % for real floating-point data
   fid = fopen(filename, 'rb');
   X = fread(fid,im_size,'real*4=>single');
   fclose(fid);


   % for complex floating-point data
   fid = fopen(filename, 'rb');
   X = fread(fid,im_size_c,'real*4=>single');
   X = X(1:2:end, :) + 1j*X(2:2:end, :);
   fclose(fid);


以 **Salt Lake City** 的区域为例, 如 :figure:numref:`fig-ASF_SearchUAVSARData` 所示, 从ASF上可查询到 Salt Lake City 区域的两景数据, 选择数据 ``stlake_27129_20002_008_200131_L090_CX_01_mlc.zip`` 下载, 对应  :figure:numref:`fig-ASF_SearchUAVSARData` 中的红色框, 读取后显示得到 :figure:numref:`fig-UAVSAR_stlake_27129_20002_008_200131_L090HHHV_CX_01` 所示结果, 对比 :figure:numref:`fig-ASF_SearchUAVSARData` 和 :figure:numref:`fig-UAVSAR_stlake_27129_20002_008_200131_L090HHHV_CX_01`, 可知数据读取正确.



.. _fig-ASF_SearchUAVSARData:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/UAVSAR/ASF_UAVSAR_MLC_SaltLakeCity.*
   :alt: Search UAVSAR data
   :align: center

   Search UAVSAR data


需要注意的是, 原始数据大小为 :math:`3185×5843`,  :figure:numref:`fig-UAVSAR_stlake_27129_20002_008_200131_L090HHHV_CX_01` 所示结果被降采样至 :math:`1366×744`. 此外, 由于飞机自西向东飞行, 成像后的数据进行水平翻转后才能与实际区域相吻合.


.. _fig-UAVSAR_stlake_27129_20002_008_200131_L090HHHV_CX_01:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/UAVSAR/UAVSAR_stlake_27129_20002_008_200131_L090HHHV_CX_01.*
   :alt: Visualization of stlake_27129_20002_008_200131_L090HHHV_CX_01
   :align: center

   Visualization of data stlake_27129_20002_008_200131_L090HHHV_CX_01




数据成像
----------------------
