.. _Section-RADARSATRadarProductSupplementRadar:

RADARSAT 产品介绍
=====================

RADARSAT 产品包含 RADARSAT1 和 RADASAT2 两中产品


RADARSAT1 产品
--------------------------


RADARSAT1 雷达参数与工作模式
~~~~~~~~~~~~~~~~~~~~~~~~~~

**RADARSAT SAR 平台工作参数信息** 可以从 `这里 <http://www.asc-csa.gc.ca/eng/satellites/radarsat/radarsat-tableau.asp>`_ 查到.

RADARSAT1的详细参数在 `这里 <http://www.asc-csa.gc.ca/eng/satellites/radarsat1/components.asp>`_ . 可知 RADARSAT1 成像模式为右视 (right looking) 条带式(stripmap mode) 成像, 属于 :math:`C` 波段雷达, 极化方式为 ``HH`` 极化. 轨道倾角 ( :term:`Orbital Inclination` ) 为 :math:`98.6^°` 与雷达的斜视角 ( :term:`Squint Angle` ) 不同, 由于轨道倾角 (相对于地球赤道的倾角) 为 :math:`98.6^°`, 所以卫星处于太阳同步轨道 (参见 :ref:`SubSubSection-SunSynchronousOrbit` 小节), 经过南北两极. 成像时用到的RADARSAT雷达参数如 :table:numref:`table-ParametersRadarsat1Platform` 所示.



.. table:: RADARSAT1平台参数
   :name: table-ParametersRadarsat1Platform

   +--------------------+-----------------------------+---------------+------------+
   | 参数               | 符号                        | 值            | 单位       |
   +====================+=============================+===============+============+
   | 航天器航向         |                             | 344.49        | :math:`°`  |
   +--------------------+-----------------------------+---------------+------------+
   | 平台纬度           |                             | 48.36         | :math:`°`  |
   +--------------------+-----------------------------+---------------+------------+
   | 平台经度           |                             | 229.29        | :math:`°`  |
   +--------------------+-----------------------------+---------------+------------+
   | 平台高度           | :math:`H`                   | 793-821       | km         |
   +--------------------+-----------------------------+---------------+------------+
   | 平台速度(等效速度) | :math:`V_r`                 | 7062          | m/s        |
   +--------------------+-----------------------------+---------------+------------+
   | 距离向天线长度     | :math:`L_r`                 | 1.5           | m          |
   +--------------------+-----------------------------+---------------+------------+
   | 方位向天线长度     | :math:`L_a`                 | 15            | m          |
   +--------------------+-----------------------------+---------------+------------+
   | 雷达波长           | :math:`\lambda`             | 0.05657       | m          |
   +--------------------+-----------------------------+---------------+------------+
   | 雷达载频           | :math:`f_c`                 | 5.3           | GHz        |
   +--------------------+-----------------------------+---------------+------------+
   | 脉冲宽度           | :math:`T_p`                 | 41.75         | :math:`μs` |
   +--------------------+-----------------------------+---------------+------------+
   | 距离向调频率       | :math:`K_r`                 | -7.2135e+11   | Hz/s       |
   +--------------------+-----------------------------+---------------+------------+
   | 距离向带宽         | :math:`B_r`                 | 30.12         | MHz        |
   +--------------------+-----------------------------+---------------+------------+
   | 距离向采样率       | :math:`F_{rs}`              | 32.317e+6     | Hz         |
   +--------------------+-----------------------------+---------------+------------+
   | 距离向采样数       | :math:`N_{r}`               | 9288          |            |
   +--------------------+-----------------------------+---------------+------------+
   | 方位向调频率       | :math:`K_a`                 | 1733          | Hz/s       |
   +--------------------+-----------------------------+---------------+------------+
   | 方位向采样率       | :math:`F_{as}=PRF`          | 1256.98       | Hz         |
   +--------------------+-----------------------------+---------------+------------+
   | 方位向采样数       | :math:`N_{a}`               | 不定, 19438   |            |
   +--------------------+-----------------------------+---------------+------------+
   | 多普勒中心频率     | :math:`f_{\eta_c}`          | -6900         | Hz         |
   +--------------------+-----------------------------+---------------+------------+
   | 成像分辨率         | :math:`\Delta_a × \Delta_r` | :math:`8 × 8` | m          |
   +--------------------+-----------------------------+---------------+------------+
   | 轨道运行周期       | :math:`T_o`                 | 100.7         | min        |
   +--------------------+-----------------------------+---------------+------------+
   | 卫星轨道半径       | :math:`r`                   | 7149752       | m          |
   +--------------------+-----------------------------+---------------+------------+
   | 地球极地半径       | :math:`R_e`                 | 6356752       | m          |
   +--------------------+-----------------------------+---------------+------------+
   | 地球平均半径       | :math:`R_e`                 | 6367856       | m          |
   +--------------------+-----------------------------+---------------+------------+
   | 轨道倾角           |                             | 98.6          | :math:`°`  |
   +--------------------+-----------------------------+---------------+------------+
   | 近距入射角         |                             | 38.64         | :math:`°`  |
   +--------------------+-----------------------------+---------------+------------+
   | 中距入射角         |                             | 40.15         | :math:`°`  |
   +--------------------+-----------------------------+---------------+------------+
   | 远距入射角         |                             | 41.61         | :math:`°`  |
   +--------------------+-----------------------------+---------------+------------+


不同成像模式下分辨率, 幅宽, 入射角不一致. 如入射角 (Incidence Angles) 在精细 (Fine) 成像模式下为 :math:`34-47^°`, 在标准 (Standard) 成像模式下为 :math:`20-49^°`, 扩展先进模式下为 :math:`52-58^°`. RADARSAT支持的波束模式以及不同模式下的幅宽与分辨率如 :table:numref:`table-BeamModeSwathResolutionRadarsat1Platform1`, :table:numref:`table-BeamModeSwathResolutionRadarsat1Platform2` 所示.



.. table:: RADARSAT1的波束模式及对应幅宽分辨率1
   :name: table-BeamModeSwathResolutionRadarsat1Platform1

   +------------+----------+---------------+
   | 波束模式   | 幅宽(km) | 近似分辨率(m) |
   +============+==========+===============+
   | 低分辨100m | 500      | 100           |
   +------------+----------+---------------+
   | 中分辨50m  | 350      | 50            |
   +------------+----------+---------------+
   | 中分辨30m  | 125      | 30            |
   +------------+----------+---------------+
   | 中分辨16m  | 30       | 16            |
   +------------+----------+---------------+
   | 高分辨5m   | 30       | 5             |
   +------------+----------+---------------+


.. table:: RADARSAT1的波束模式及对应幅宽分辨率2
   :name: table-BeamModeSwathResolutionRadarsat1Platform2

   +----------------+----------+---------------+
   | 波束模式       | 幅宽(km) | 近似分辨率(m) |
   +================+==========+===============+
   | Fine           | 45       | 8             |
   +----------------+----------+---------------+
   | Standard       | 100      | 30            |
   +----------------+----------+---------------+
   | Wide           | 125      | 30            |
   +----------------+----------+---------------+
   | ScanSAR Narrow | 300      | 50            |
   +----------------+----------+---------------+
   | ScanSAR Wide   | 500      | 100           |
   +----------------+----------+---------------+
   | Extended High  | 75       | 18-27         |
   +----------------+----------+---------------+
   | Extended Low   | 170      | 30            |
   +----------------+----------+---------------+


.. hint::
    幅宽是波束一次扫描照射的宽度, 即波束距离向上在地面的投影宽度.



RADARSAT1 参数分析
~~~~~~~~~~~~~~~~~~~~~~~~

该小节通过查询的RADARSAT1工作参数, 计算部分成像需要的参数.

下面进行一些参数的计算, 其中地球半径取极地半径 :math:`R_e=6356752` m, 引力常量 :math:`G_e=3.98603e14 {\rm m^3/s^2}`.

- 卫星轨道半径 :math:`R_s = R_e+H ∈ [6356752+793000, 6356752+821000]=[7149752{\rm m}, 7177752{\rm m}]`
- 轨道运行周期 :math:`T_o = 2π \sqrt{\frac{R_s^3}{Ge}} ∈ [100.3{\rm min}, 100.9{\rm min}]`
- 卫星运行角速度 :math:`\omega_s = 2\pi/T_o \in [0.00103785{\rm rad/s}, 0.00104406{\rm rad/s}]`
- 卫星飞行速度 :math:`V_s = R_s \omega_s \in [7420.419{\rm m/s}, 7494.042{\rm m/s}]`

距离向调频带宽 :math:`B_r = |K_r|T_p = 30.12e6 Hz`, 距离向分辨率 :math:`\Delta_r = c/2B_r = 4.98m` 但是查到的是 :math:`8m`, 这是怎么回事呢, 这是因为上述计算的是斜距分辨率, 其地距分辨率为 :math:`\Delta_x = \Delta_r/{\rm sin}\theta_i ≈ \Delta_r/{\rm sin}38.64^° ≈ 8.08m`. 其中, :math:`\theta_i` 表示入射角.


由多普勒中心频率 :math:`f_{\eta_c} = 2V{\rm sin}\theta_s/ \lambda` 可以计算出斜视角约为 :math:`\theta_s ≈ -1.58^°`, 即后侧视.


由方位向采样率及方位向采样点数可知方位向采样时间 :math:`T_{a} = N_{a}/F_{as} = 15.464s`, 这些时间内, 雷达方位向飞行的距离为 :math:`VT_{a} = 108987.85m`.

由距离向采样率及距离向采样点数知距离向采样时间为 :math:`T_{r} = N_r/F_{rs} = 28.74e-3s`




RADARSAT1 数据读取
~~~~~~~~~~~~~~~~~~~~~~~

数据简介
^^^^^^^^^^^^^^^^^^^^

数据源于书籍 :cite:`Cumming.2005,LanG.CummingFrankH.Wong.2012` 中提供的温哥华(Vancouver)地区的RADARSAT1数据, 其场景图如 :figure:numref:`fig-VancouverScence` 所示. 部分典型的地标已经在图上标出, 含史丹利公园(Stanley Park), 哥伦比亚大学(University of British Columbia), 温哥华机场 (Vancouver Airport)等等.


.. _fig-VancouverScence:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/VancouverImage.*
   :alt: Image of Vancouver scence
   :align: center

   Image of Vancouver scence


数据格式与读取
^^^^^^^^^^^^^^^^^^^^

RADARSAT1 数据采用CEOS(参见 :ref:`SubSection-CEOSProductDataFormationRadarProductSupplementRadar` 小节)格式记录存储数据, 文件后缀是 ``.001``, 数据及读取源码可在作者 `主页 <http://sar.ece.ubc.ca/SAR_Book/>`_ 下载, 也可以使用本书作者开发的雷达处理库 :guilabel:`iprs` 读取. :code-block:numref:`code-FileHeaderInfoInRadarsat1RawDataFile` 给出了读取到的书籍 :cite:`Cumming.2005` 中提供的RADARSAT1数据中的文件头记录信息:


.. code-block:: python
   :lineno-start: 1
   :emphasize-lines: 6,14,9,27,28,45,50
   :linenos:
   :caption: File header information in Radarsat1 raw data file
   :name: code-FileHeaderInfoInRadarsat1RawDataFile


   Record sequence number [(1, 4), '1B4', [1]]
   l-st record sub-type code [(5, 5), '1B1', [63]]
   Record type code [(6, 6), '1B1', [192]]
   2-nd record sub-type code [(7, 7), '1B1', [18]]
   3-rd record sub-type code [(8, 8), '1B1', [18]]
   Length of this record [(9, 12), '1B4', [16252]]
   ASCII/EBCDIC flag [(13, 14), '1A2', ['A ']]
   1Blanks [(15, 16), '1A2', ['  ']]
   Format control document ID [(17, 28), '1A12', ['CEOS-SAR-CCT']]
   Format control document revision level [(29, 30), '1A2', [' B']]
   File design descriptor revision letter [(31, 32), '1A2', [' B']]
   Generating software release and revision level [(33, 44), '1A12', ['MSSAR 7.7.1 ']]
   File number [(45, 48), '1I4', [2]]
   File name [(49, 64), '1A16', ['RSAT-1-SAR-RAW  ']]
   Record sequence and location type flag [(65, 68), '1A4', ['FSEQ']]
   Sequence number location [(69, 76), '1I8', [1]]
   Sequence number field length [(77, 80), '1I4', [4]]
   Record code and location type flag [(81, 84), '1A4', ['FTYP']]
   Record code location [(85, 92), '1I8', [5]]
   Record code field length [(93, 96), '1I4', [4]]
   Record length and location type flag [(97, 100), '1A4', ['FLGT']]
   Record length location [(101, 108), '1I8', [9]]
   Record length field length [(109, 112), '1I4', [4]]
   Reserved1 [(113, 113), '1I1', [[]]]
   Reserved4 [(116, 116), '1I1', [[]]]
   Reserved segment [(117, 180), '1A64', ['                                                                ']]
   Number of SAR DATA records (nominal) [(181, 186), '1I6', [19438]]
   SAR DATA record length (bytes) [(187, 192), '1I6', [18768]]
   Reserved1 (blanks) [(193, 216), '1A4', ['    ']]
   Number of bits per sample [(217, 220), '1I4', [8]]
   Number of samples per data group (or pixels) [(221, 224), '1I4', [2]]
   Number of bytes per data group (or pixel) [(225, 228), '1I4', [2]]
   Justification and order of samples within data group [(229, 232), '1A4', ['    ']]
   Number of SAR channels in this file [(233, 236), '1I4', [1]]
   Number of lines per data set (nominal) [(237, 244), '1I8', [19438]]
   Number of left border pixels per line [(245, 248), '1I4', [0]]
   Total number of data groups per line per SAR channel [(249, 256), '1I8', [[]]]
   Number of right border pixels per line [(257, 260), '1I4', [0]]
   Number of top border lines [(261, 264), '1I4', [0]]
   Number of bottom border lines [(265, 268), '1I4', [0]]
   Interleaving indicator [(269, 272), '1A4', ['BSQ ']]
   Number of physical records per line [(273, 274), '1I2', [1]]
   Number of physical records per multi-channel line [(275, 276), '1I2', [1]]
   Number of bytes of prefix data per record [(277, 280), '1I4', [180]]
   Number of bytes of SAR data (or pixel data) per record (nominal) [(281, 288), '1I8', [18576]]
   Number of bytes of suffix data per record [(289, 292), '1I4', [0]]
   Reserved2 [(293, 340), '1A48', ['      13 4PB  49 2PB  45 4PB  21 4PB  29 4PB    ']]
   Blanks [(341, 368), '1A28', ['                            ']]
   Reserved3 [(369, 400), '1A32', ['                                ']]
   SAR Data format type identifier [(401, 428), '1A28', ['COMPLEX INTEGER*2           ']]
   SAR Data format type code [(429, 432), '1A4', ['CI*2']]
   Number of left fill bits within pixel [(433, 436), '1I4', [4]]
   Number of right fill bits within pixel [(437, 440), '1I4', [0]]
   Maximum data range of pixel (max-min value for I and Q) [(441, 448), '1I8', [15]]

可见, 数据格式为 ``CEOS-SAR-CCT``, 该数据共 :math:`19384` 行脉冲数据, 每行为一次脉冲回波, 一个脉冲含 :math:`9288` 个距离单元, 每个像素含实部(I)虚部(Q)共2个字节, 故每行脉冲含18576个字节, 文件头记录长度为16252字节.

.. danger::
   RADARSAT1 原始信号数据记录不是固定长度, 每8帧会多出一段长度为2880字节(1440个复数)的数据, 这些数据是发射脉冲复制品 (transmitted replica), 其中心频率是 :math:`0Hz`, 线性调频率为 :math:`0.72135e+12 Hz/s`, 该信号为数字生成信号, 且4-bit量化存储, 不够精确, 因而本书中不使用.



AGC补偿
^^^^^^^^^^^^^^^^



RADARSAT1 数据成像
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

全部区域成像
^^^^^^^^^^^^^^^^^^


:figure:numref:`fig-VancouverCSAImagingSLC_a20b50` 和 :figure:numref:`fig-VancouverCSAImagingSLC_a30b50` 给出了温哥华地区的单视成像结果(进行了降采样, 距离向与方位向尺度均缩小为原来的四分之一, 插值采用cubic插值), :figure:numref:`fig-VancouverCSAImagingMLC4_a10b50` 和 :figure:numref:`fig-VancouverCSAImagingMLC4_a20b50` 给出了温哥华地区的多视成像结果(视数为4, 多视处理后未进行降采样). 在CSA成像处理完成后, 还需要进行一些增强后处理操作(本节结果未进行RCS换算, 仅进行对数增强, 数值截断图像增强操作, 参见 :ref:`SubSection-LogContrastEnhancementDigitalImageSignalProcessing` 小节), 才能得到图示结果, 若不进行, 图像会比较暗, 对比度低. 可见与书籍 :cite:`Cumming.2005,LanG.CummingFrankH.Wong.2012` 中图3.6的结果基本一致.

:figure:numref:`fig-VancouverCSAImagingSLC_a20b50` 所示为对数增强后, 对区间 :math:`[20, 50]` 之外的数据进行截断处理的结果, :figure:numref:`fig-VancouverCSAImagingSLC_a30b50` 所示为对数增强后, 对区间 :math:`[30, 50]` 之外的数据进行截断处理的结果, :figure:numref:`fig-VancouverCSAImagingMLC4_a10b50` 所示为对数增强后, 对区间 :math:`[10, 50]` 之外的数据进行截断处理的结果, :figure:numref:`fig-VancouverCSAImagingMLC4_a20b50` 所示为对数增强后, 对区间 :math:`[20, 50]` 之外的数据进行截断处理的结果.

.. _fig-VancouverCSAImagingSLC_a20b50:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/RADARSAT1_Vancouver_CSA(SRC+RCMC+DPC)_SLC_a20b50.*
   :alt: Single look imaging result (with truncation parameters :math:`a=20, b=50`) of Chirp Scaling Algorithm.
   :align: center

   Single look imaging result (with truncation parameters :math:`a=20, b=50`) of Chirp Scaling Algorithm.

.. _fig-VancouverCSAImagingSLC_a30b50:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/RADARSAT1_Vancouver_CSA(SRC+RCMC+DPC)_SLC_a30b50.*
   :alt: Single look imaging result (with truncation parameters :math:`a=30, b=50`) of Chirp Scaling Algorithm.
   :align: center

   Single look imaging result (with truncation parameters :math:`a=30, b=50`) of Chirp Scaling Algorithm.


.. _fig-VancouverCSAImagingMLC4_a20b50:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/RADARSAT1_Vancouver_CSA(SRC+RCMC+DPC)_MLC4_a10b50.*
   :alt: Multiple looks (4, 4) imaging result (with truncation parameters :math:`a=10, b=50`) of Chirp Scaling Algorithm.
   :align: center

   Multiple looks (4, 4) imaging result (with truncation parameters :math:`a=10, b=50`) of Chirp Scaling Algorithm.

.. _fig-VancouverCSAImagingMLC4_a10b50:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/RADARSAT1_Vancouver_CSA(SRC+RCMC+DPC)_MLC4_a20b50.*
   :alt: Multiple looks (4, 4) imaging result (with truncation parameters :math:`a=20, b=50`) of Chirp Scaling Algorithm.
   :align: center

   Multiple looks (4, 4) imaging result (with truncation parameters :math:`a=20, b=50`) of Chirp Scaling Algorithm.


.. warning::
   首先, 本节结果未进行RCS转换, 其次, 使用Python中的Matplotlib, PIL, Opencv或MATLAB显示出来的图看起来像是有很多噪声点, 将矩阵保存成 ``.tiff`` 图像后, 用其它显示软件打开则相对平滑, 如 :figure:numref:`fig-RADARSAT1_ViewByDiffSoftwares` 所示.


.. _fig-RADARSAT1_ViewByDiffSoftwares:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/RADARSAT1_ViewByDiffSoftwares.*
   :alt: View by ASFVIEW, Document Viewer, Matlab, Python
   :align: center

   View imaging image with different programs. (a) Ubuntu Document Viewer, (b) ASF view program, (c) Matlab's :func:`imshow`, (d) Python's :func:`plt.imshow`.




部分区域成像
^^^^^^^^^^^^^^^^^


如前所述, RADARSAT1 幅宽为 :math:`45km`, 距离向采样点数为 :math:`Nr = 9280`, 每个像素点的距离分辨率为 :math:`\delta_x=45000/9280 = 4.85` (注意这只说明距离向过采样, 距离向的地距分辨率仍然为先前计算的 :math:`8m` ). 取数据中的 :math:`1536\times 2048` 个像素作为待成像区域, 则地理区域为 :math:`(1536\times \delta_y) \times (2048\times \delta_x) = 8896m\times 15886m)`.

以史丹利公园区域数据为例, 如 :figure:numref:`fig-StanleyParkEathMap` 所示为该区域的地图, 其地理区域区域范围测量结果已经在图中标出, 与上面计算的区域基本一致. :figure:numref:`fig-StanleyPark_CSA_Matplot` 为matplotlib工具显示的该区域数据CSA成像结果, 其中, 坐标轴已经对应到实际距离, 可见与计算和地图测量结果基本一致. :figure:numref:`fig-StanleyPark_CSA_Matplot` 显示的结果已经进行了下采样, :figure:numref:`fig-StanleyParkEathMap` 给出了该区域未进行下采样的成像结果.


.. _fig-StanleyParkEathMap:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/StanleyParkEathMap.*
   :alt: Eath Map of Stanley Park
   :align: center

   Eath Map of Stanley Park


.. _fig-StanleyPark_CSA_Matplot:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/StanleyPark_CSA_Matplot.*
   :alt: Imaging result of Chirp Scaling Algorithm (Stanley Park).
   :align: center

   Imaging result of Chirp Scaling Algorithm (Stanley Park) shown by matplotlib.


.. _fig-StanleyPark_CSA:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/StanleyPark_CSA.*
   :alt: Imaging result image of Chirp Scaling Algorithm (Stanley Park).
   :align: center

   Imaging result image of Chirp Scaling Algorithm (Stanley Park).



:figure:numref:`fig-UBC_CSA`, :figure:numref:`fig-VancouverAirport_CSA`, :figure:numref:`fig-SquamishGaribaldi` 分别给出了哥伦比亚大学(UBC), 温哥华机场(Vancouver Airport), 斯阔米什(Squamish Garibaldi) 地区数据的CSA算法成像结果.

.. _fig-UBC_CSA:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/UBC_CSA.*
   :alt: Imaging result of Chirp Scaling Algorithm (UBC).
   :align: center

   Imaging result of Chirp Scaling Algorithm (UBC).


.. _fig-VancouverAirport_CSA:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/VancouverAirport_CSA.*
   :alt: Imaging result of Chirp Scaling Algorithm (Vancouver Airport).
   :align: center

   Imaging result of Chirp Scaling Algorithm (Vancouver Airport).


.. _fig-SquamishGaribaldi:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/RADARSAT/SquamishGaribaldi_CSA.*
   :alt: Imaging result of Chirp Scaling Algorithm (Squamish and Garibaldi).
   :align: center

   Imaging result of Chirp Scaling Algorithm (Squamish Garibaldi).




RADARSAT2 产品介绍
---------------------------

RADARSAT2 雷达参数
~~~~~~~~~~~~~~~~~~~



.. rubric:: Footnotes
.. [#RDA_Inclination] 这里是指轨道倾角 ( :term:`Orbital Inclination` ), 与雷达的斜视角( :term:`Squint Angle` ) 不同.
