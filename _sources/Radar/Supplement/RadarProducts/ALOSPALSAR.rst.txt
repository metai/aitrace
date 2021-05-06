.. _Section-ALOSPALSARRadarProductSupplementRadar:

ALOS PALSAR 产品介绍
=====================


ALOS PALSAR 简介
--------------------------


`ALOS PALSAR <https://www.eorc.jaxa.jp/ALOS/en/about/palsar.htm>`_ 是先进陆地观测卫星 (Advanced Land Observing Satellite, ALOS) 上搭载的相控阵型L-波段合成孔径雷达 (Phased Array type L-band Synthetic Aperture Radar, PALSAR), 由日本宇宙航空探索局地球观测研究中心研制, 于2006年开始服役, 2011年结束服役.



ALOS PALSAR 平台参数与工作模式
------------------------------

ALOS PALSAR 具有三种工作模式, 分别为: 精细模式, 扫描模式和极化模式, 其具体参数参见文献 :cite:`Shimada.2019.Imaging` TABLE 2-3, 现总结如下表 :table:numref:`table-ParametersALOSPALSARPlatform` 所示.


.. table:: ALOS PALSAR 精细模式下平台参数
   :name: table-ParametersALOSPALSARPlatform

   +----------------+-----------------------------+----------------+------------+
   | 参数           | 符号                        | 值             | 单位       |
   +================+=============================+================+============+
   | 平台高度       | :math:`H`                   | 691500         | m          |
   +----------------+-----------------------------+----------------+------------+
   | 平台速度       | :math:`V_r`                 | 7172           | m/s        |
   +----------------+-----------------------------+----------------+------------+
   | 距离向天线长度 | :math:`L_r`                 | 2.9            | m          |
   +----------------+-----------------------------+----------------+------------+
   | 方位向天线长度 | :math:`L_a`                 | 8.9            | m          |
   +----------------+-----------------------------+----------------+------------+
   | 雷达波长       | :math:`\lambda`             | 0.236057       | m          |
   +----------------+-----------------------------+----------------+------------+
   | 雷达载频       | :math:`f_c`                 | 1.27           | GHz        |
   +----------------+-----------------------------+----------------+------------+
   | 脉冲宽度       | :math:`T_p`                 | 27.0           | :math:`μs` |
   +----------------+-----------------------------+----------------+------------+
   | 距离向调频率   | :math:`K_r`                 | -1.037e+12     | Hz/s       |
   +----------------+-----------------------------+----------------+------------+
   | 距离向带宽     | :math:`B_r`                 | 28, 14         | MHz        |
   +----------------+-----------------------------+----------------+------------+
   | 距离向采样率   | :math:`F_{rs}`              | 32, 16         | MHz        |
   +----------------+-----------------------------+----------------+------------+
   | 距离向采样数   | :math:`N_{r}`               | 10344, 5616    |            |
   +----------------+-----------------------------+----------------+------------+
   | 方位向调频率   | :math:`K_a`                 | 2122.96        | Hz/s       |
   +----------------+-----------------------------+----------------+------------+
   | 方位向采样率   | :math:`F_{as}=PRF`          | <2700, 2164.50 | Hz         |
   +----------------+-----------------------------+----------------+------------+
   | 方位向采样数   | :math:`N_{a}`               | 不定           |            |
   +----------------+-----------------------------+----------------+------------+
   | 多普勒中心频率 | :math:`f_{\eta_c}`          | 1257.769       | Hz         |
   +----------------+-----------------------------+----------------+------------+
   | 成像分辨率     | :math:`\Delta_a × \Delta_r` | :math:`5 × 5`  | m          |
   +----------------+-----------------------------+----------------+------------+
   | 幅宽           |                             | 70km           | m          |
   +----------------+-----------------------------+----------------+------------+
   | 入射角         | :math:`\theta_i`            | 约 38.7        | :math:`°`  |
   +----------------+-----------------------------+----------------+------------+
   | 斜视角         | :math:`\theta_s`            | 0              | :math:`°`  |
   +----------------+-----------------------------+----------------+------------+


.. danger:: 文献 :cite:`Shimada.2019.Imaging` 中表 2-3 中所给速度为波束掠过地面的速度 :math:`V_g = 6700`,  根据平台高度等参数可以计算出卫星速度 :math:`V_s=7514`, 从而计算出实际有效速度为 :math:`V_r=7100`. 在距离徙动校正时用的是 :math:`V_r`, 若使用 :math:`V_g`, 则校正失效, 成像模糊. 另外, 该等效速度仅为近似速度, 如对于 **IMG-HH-ALPSRP050500980-H1(sl=1el=35345)** 数据, 实际取 :math:`V_r=7172` 时, 成像效果最好(几乎无需自聚焦); 当有效速度计算不准确时, 可通过自聚焦改善成像效果.





ALOS PALSAR 产品
---------------------


有关 ALOS PALSAR 的信息可在 `这里 <https://asf.alaska.edu/data-sets/sar-data-sets/alos-palsar/>`_ 和 `这里 <https://www.eorc.jaxa.jp/ALOS/en/about/palsar.htm>`_  查看. ALOS PALSAR 有


产品格式说明
~~~~~~~~~~~~~~~








数据下载
~~~~~~~~~~~~~~~~

从 `ASF <https://www.asf.alaska.edu/>`_ 上可以下载 ALOS PALSAR 系列卫星产品数据,




ALOS PALSAR 数据读取
---------------------

原始数据读取
~~~~~~~~~~~~~~~~~~~~

与RADARSAT和ERS产品类似, ALOS PALSAR产品数据采用CEOS(参见 :ref:`SubSection-CEOSProductDataFormationRadarProductSupplementRadar` 小节)格式存储数据, ALOS PALSAR产品文件结构描述参考文件 :cite:`EarthObservationResearchCenter.2006` (可以从 `这里 <https://asf.alaska.edu/data-sets/sar-data-sets/alos-palsar/alos-palsar-documents-tools/>`_ ), 下面简要介绍原始数据的文件结构及数据提取. 本节以从ASF上下载温哥华地区精细模式下的数据 `ALPSRP050500980-L1.0.zip` 原始回波数据文件为例进行讲解. 数据的读取可以采用本书开发的Python工具包 :guilabel:`iprs`, 其中在本书作者开发的 :guilabel:`iprs` 工具包中, 定义的SAR信号数据映射字典如 :code-block:numref:`code-iprsSarDataFileSignalDataRecordALOSPALSAR` 所示.


.. code-block:: python
   :lineno-start: 1
   :emphasize-lines: 6,33
   :linenos:
   :caption: ALOS PALSAR Data File Signal Data Record Descriptor Dictionary defined in :guilabel:`iprs`
   :name: code-iprsSarDataFileSignalDataRecordALOSPALSAR

   SarDataFileSignalDataRecordALOSPALSAR = {
       'Record sequence number': [(1, 4), '1B4', 0],
       'l-st record sub-type code': [(5, 5), '1B1', 0],
       'Record type code': [(6, 6), '1B1', 0],
       '2-nd record sub-type code': [(7, 7), '1B1', 0],
       '3-rd record sub-type code': [(8, 8), '1B1', 0],
       'Length of this record': [(9, 12), '1B4', 0],
       # PREFIX DATA - GENERAL INFORMATION
       'SAR image data line number': [(13, 16), '1B4', 0],
       'SAR image data record index (indicates the record sequence number of the image line)': [(17, 20), '1B4', 0],
       'Actual count of left-fill pixels': [(21, 24), '1B4', 0],
       'Actual count of data pixels': [(25, 28), '1B4', 0],
       'Actual count of right-fill pixels': [(29, 32), '1B4', 0],
       # PREFIX DATA-SENSOR PARAMETERS
       'Sensor parameters update flag (1=data in this section is an update 0=data is a repeat)': [(33, 36), '1B4', 0],
       'Sensor acquisition year (UT)': [(37, 40), '1B4', 0],
       'Sensor acquisition day of year (UT) ': [(41, 44), '1B4', 0],
       'Sensor acquisition msecs of day (UT)': [(45, 48), '1B4', 0],
       'SAR channel indicator (sequence number in multi-channel SAR data, polarization)': [(49, 50), '1B2', 0],
       'SAR channel code (0 = L, 1 = 5, 2 = C, 3 = X, 4 = KU and 5 = KA channel)': [(51, 52), '1B2', 0],
       'Transmitted polarization': [(53, 54), '1B2', 0],
       'Received polarization': [(55, 56), '1B2', 0],
       'PRF [mHz]': [(57, 60), '1B4', 0],
       'Scan ID for SCAN SAR mode ( 1 - 5 ) except Wide Observation mode = always 0': [(61, 64), '1B4', 0],
       'Onboard Range compressed flag (0 = no/1 = yes) = always 0': [(65, 66), '1B2', 0],
       'Pulse (chirp) type designator (0 = "LINEARbFMbCHIRPb",1 = "PHASEbMODULATORS") = always 0': [(67, 68), '1B2', 0],
       'Chirp length (nano-secs)': [(69, 72), '1B4', 0],
       'Chirp constant coefficient (Hz) (nominal value)': [(73, 76), '1B4', 0],
       'Chirp linear coefficient (Hz/usec) (nominal value)': [(77, 80), '1B4', 0],
       'Chirp quadratic coefficient (Hz/Wsec,)': [(81, 84), '1B4', 0],
       'spare Always blank(0) filled1': [(85, 88), '1B4', 0],
       'spare Always blank(0) filled2': [(89, 92), '1B4', 0],
       'Receiver gain (dB) nominal value': [(93, 96), '1B4', 0],
       'Nought line flag (0 = no(Right Line)/1 = yes(Loss Line))': [(97, 100), '1B4', 0],
       'Electronic antenna squint angle (millionths of degrees)= always blank (0) filled': [(101, 104), '1B4', 0],
       'Antenna mechanical elevation angle from nadir (millionths of degrees)= always blank (0) filled': [(105, 108), '1B4', 0],
       'Electronic antenna squint angle (millionths of degrees)': [(109, 112), '1B4', 0],
       'Mechanical antenna squint angle (millionths of degrees)= always blank (0) filled': [(113, 116), '1B4', 0],
       'Slant range to 1st data sample (m)': [(117, 120), '1B4', 0],
       'Data record window position (i.e.. sample delay) (nano-secs)': [(121, 124), '1B4', 0],
       'spare Always blank(0) filled3': [(125, 128), '1B4', 0],
       # PREFIX DATA-PLATFORM REFERENCE INFORMATION
       'Platform information': [(129, 192), '1B64', 0],
       # PREFIX DATA - SENSOR/FACILITY SPECIFIC, AUXILIARY DATA
       'Always blank (0) filled1': [(193, 284), '1B92', 0],
       'Counter of PALSAR frame': [(285, 288), '1B4', 0],
       'PALSAR auxiliary data': [(289, 388), '1B100', 0],
       'Always blank (0) filled2': [(389, 412), '1B24', 0],
       # SAR RAW SIGNAL DATA
       'Raw Data': [(413, 414), '2B1', 0]  # [I, Q]
   }


使用 :guilabel:`iprs` 读取的文件 :file:`ALPSRP050500980-L1.0/IMG-HH-ALPSRP050500980-H1.0__A` 的记录信息见 :code-block:numref:`code-SarDataFileSignalDataRecordALOSPALSAR` 所示.

.. code-block:: python
   :lineno-start: 1
   :emphasize-lines: 6,33
   :linenos:
   :caption: Signal data record of file IMG-HH-ALPSRP050500980-H1.0__A
   :name: code-SarDataFileSignalDataRecordALOSPALSAR

   Record sequence number [(1, 4), '1B4', [2]]
   l-st record sub-type code [(5, 5), '1B1', [50]]
   Record type code [(6, 6), '1B1', [10]]
   2-nd record sub-type code [(7, 7), '1B1', [18]]
   3-rd record sub-type code [(8, 8), '1B1', [20]]
   Length of this record [(9, 12), '1B4', [21100]]
   SAR image data line number [(13, 16), '1B4', [1]]
   SAR image data record index (indicates the record sequence number of the image line) [(17, 20), '1B4', [1]]
   Actual count of left-fill pixels [(21, 24), '1B4', [0]]
   Actual count of data pixels [(25, 28), '1B4', [10304]]
   Actual count of right-fill pixels [(29, 32), '1B4', [40]]
   Sensor parameters update flag (1=data in this section is an update 0=data is a repeat) [(33, 36), '1B4', [1]]
   Sensor acquisition year (UT) [(37, 40), '1B4', [2007]]
   Sensor acquisition day of year (UT)  [(41, 44), '1B4', [5]]
   Sensor acquisition msecs of day (UT) [(45, 48), '1B4', [23518945]]
   SAR channel indicator (sequence number in multi-channel SAR data, polarization) [(49, 50), '1B2', [1]]
   SAR channel code (0 = L, 1 = 5, 2 = C, 3 = X, 4 = KU and 5 = KA channel) [(51, 52), '1B2', [0]]
   Transmitted polarization [(53, 54), '1B2', [0]]
   Received polarization [(55, 56), '1B2', [0]]
   PRF [mHz] [(57, 60), '1B4', [2155172]]
   Scan ID for SCAN SAR mode ( 1 - 5 ) except Wide Observation mode = always 0 [(61, 64), '1B4', [0]]
   Onboard Range compressed flag (0 = no/1 = yes) = always 0 [(65, 66), '1B2', [0]]
   Pulse (chirp) type designator (0 = "LINEARbFMbCHIRPb",1 = "PHASEbMODULATORS") = always 0 [(67, 68), '1B2', [0]]
   Chirp length (nano-secs) [(69, 72), '1B4', [27000]]
   Chirp constant coefficient (Hz) (nominal value) [(73, 76), '1B4', [0]]
   Chirp linear coefficient (Hz/usec) (nominal value) [(77, 80), '1B4', [1232940752]]
   Chirp quadratic coefficient (Hz/Wsec,) [(81, 84), '1B4', [0]]
   spare Always blank(0) filled1 [(85, 88), '1B4', [0]]
   spare Always blank(0) filled2 [(89, 92), '1B4', [0]]
   Receiver gain (dB) nominal value [(93, 96), '1B4', [24]]
   Nought line flag (0 = no(Right Line)/1 = yes(Loss Line)) [(97, 100), '1B4', [0]]
   Electronic antenna squint angle (millionths of degrees)= always blank (0) filled [(101, 104), '1B4', [0]]
   Antenna mechanical elevation angle from nadir (millionths of degrees)= always blank (0) filled [(105, 108), '1B4', [0]]
   Electronic antenna squint angle (millionths of degrees) [(109, 112), '1B4', [0]]
   Mechanical antenna squint angle (millionths of degrees)= always blank (0) filled [(113, 116), '1B4', [0]]
   Slant range to 1st data sample (m) [(117, 120), '1B4', [850614]]
   Data record window position (i.e.. sample delay) (nano-secs) [(121, 124), '1B4', [106684]]
   spare Always blank(0) filled3 [(125, 128), '1B4', [0]]
   Platform information [(129, 192), '1B64', [0]]
   Always blank (0) filled1 [(193, 284), '1B92', [0]]
   Counter of PALSAR frame [(285, 288), '1B4', [752607]]
   PALSAR auxiliary data [(289, 388), '1B100', [263129968205480992023280643085359307138574792461797720331625355555552187227123992216825909049138802819234429379486614773355864556286127397455858336090606728798761926618935967276621537709384105360275969343101570371356070712498890271222661120]]
   Always blank (0) filled2 [(389, 412), '1B24', [0]]
   Raw Data [(413, 414), '2B1', [29, 20]]


可见该文件中共包含, 脉冲重复频率为 :math:`2155.172Hz`, 脉冲宽度为 :math:`27μs`, 第一个样本斜距为 :math:`850614m`.


.. warning:: 需要注意的是, IQ通道数据在写入前被施加了直流偏置, 它们的值可以从 ``SAR Leader File Descriptor Record`` 记录中读取, 映射格式如下, 即为16位浮点数, 读取的本小节数据中的直流偏置的值均为15.5:

   +--------+------------+--------+-------------------------+
   | Number | Bytes      | Format | Description             |
   +========+============+========+=========================+
   | 66     | 819 － 834 | F16.7  | DC Bias for I-component |
   +--------+------------+--------+-------------------------+
   | 67     | 835 － 850 | F16.7  | DC Bias for Q-componen  |
   +--------+------------+--------+-------------------------+





ALOS PALSAR 数据成像
---------------------

对上一小节中读取的温哥华地区的数据, 采用调频变标方法成像 (:ref:`Section-ChirpScalingAlgorithmImagingSARRadar`) 小节. 由于原始数据较大, 且方位向采样点数一般远大于距离向采样点数, 故这里仅给出降采样的成像结果图以及多视处理后的结果图.


