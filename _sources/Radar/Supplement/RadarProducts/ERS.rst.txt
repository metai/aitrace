.. _Section-ERSXRadarProductSupplementRadar:

ERS系列产品介绍
=====================


雷达参数与工作模式
--------------------------

ERS1 与 ERS2 是欧洲航天局 (European Space Agency, ESA) 研发的两颗卫星, 分别于1991年与1995年发射, 两颗卫星搭载的相同参数的雷达. 雷达工作在C波段, 采用HH极化收发方式, 轨道重访周期为35天. 在ERS1与ERS2同时工作的期间, ESA通过进行轨道调整和控制, 使得ERS1与ERS2间满足干涉测量要求, 从而使系统具备干涉测量的能力. 具体雷达参数可以在 `这里 <http://www.esa.int/Applications/Observing_the_Earth/ERS_1_and_2>`_ 与 `这里 <https://crisp.nus.edu.sg/ers/ers.html>`_ 获得. 总结如下:

.. table:: ERS平台参数
   :name: table-ParametersERSPlatform

   +----------------+-----------------------------+---------------------+------------+
   | 参数           | 符号                        | 值                  | 单位       |
   +================+=============================+=====================+============+
   | 平台高度       | :math:`H`                   | 786070              | m          |
   +----------------+-----------------------------+---------------------+------------+
   | 平台速度       | :math:`V`                   | 7098.0194           | m/s        |
   +----------------+-----------------------------+---------------------+------------+
   | 距离向天线长度 | :math:`L_r`                 | 1                   | m          |
   +----------------+-----------------------------+---------------------+------------+
   | 方位向天线长度 | :math:`L_a`                 | 10                  | m          |
   +----------------+-----------------------------+---------------------+------------+
   | 雷达波长       | :math:`\lambda`             | 0.05657             | m          |
   +----------------+-----------------------------+---------------------+------------+
   | 雷达载频       | :math:`f_c`                 | 5.3                 | GHz        |
   +----------------+-----------------------------+---------------------+------------+
   | 脉冲宽度       | :math:`T_p`                 | 37.12               | :math:`μs` |
   +----------------+-----------------------------+---------------------+------------+
   | 距离向调频率   | :math:`K_r`                 | 4.18989015e+11      | Hz/s       |
   +----------------+-----------------------------+---------------------+------------+
   | 距离向带宽     | :math:`B_r`                 | 15.55±0.01          | MHz        |
   +----------------+-----------------------------+---------------------+------------+
   | 距离向采样率   | :math:`F_{rs}`              | 18.962468e+6        | Hz         |
   +----------------+-----------------------------+---------------------+------------+
   | 距离向采样数   | :math:`N_{r}`               | 5616                |            |
   +----------------+-----------------------------+---------------------+------------+
   | 方位向调频率   | :math:`K_a`                 | 2122.96             | Hz/s       |
   +----------------+-----------------------------+---------------------+------------+
   | 方位向采样率   | :math:`F_{as}=PRF`          | 1640-1720, 1679.902 | Hz         |
   +----------------+-----------------------------+---------------------+------------+
   | 方位向采样数   | :math:`N_{a}`               | 不定                |            |
   +----------------+-----------------------------+---------------------+------------+
   | 多普勒中心频率 | :math:`f_{\eta_c}`          | 1257.769            | Hz         |
   +----------------+-----------------------------+---------------------+------------+
   | 成像分辨率     | :math:`\Delta_a × \Delta_r` | :math:`5 × 24.6`    | m          |
   +----------------+-----------------------------+---------------------+------------+
   | 幅宽           |                             | 80400 or 102500     | m          |
   +----------------+-----------------------------+---------------------+------------+
   | 入射角         | :math:`\theta_i`            | 23 (at mid-swath)   | :math:`°`  |
   +----------------+-----------------------------+---------------------+------------+
   | 斜视角         | :math:`\theta_s`            | 0                   | :math:`°`  |
   +----------------+-----------------------------+---------------------+------------+




数据获取
--------------------


从 `ASF <https://www.asf.alaska.edu/>`_ 上可以下载到ERS卫星SAR数据, 解压下载的 ``zip`` 数据文件, 可以得到 ``.raw  .vol .ldr`` 等文件, 此种格式使用 **SNAP, NEST** 这些软件都无法打开, 可以使用 `GMTSAR <https://topex.ucsd.edu/gmtsar/>`_ 来读取数据或者本书作者开发的 `iprs <http://iridescent.ink/iprs3.0/>`_ 工具读取.


.. hint::
   从ASF上下载数据很慢, 而且经常动不动中断, 后来找了个多线程下载工具, 写了个脚本终于顺利下载, 参见 :ref:`SubSubSection-MultiThreadDownload` 小节. 此外, GMTSAR依赖于通用映射依赖(Generic Mapping Tools, GMT)软件, 需要先安装GMT依赖, 然而其下载速度相当慢, 可以从 `国内镜像下载 <http://mirrors.ustc.edu.cn/gmt/>`_. GMT 与 GMTSAR 的安装采用源码安装即可, 具体可参见源码目录中的自述文件, 安装过程比较简单, 不再赘述.



原始回波数据读取
--------------------

ERS原始SAR回波数据及单视复数产品文件结构描述均可以在 `这里 <https://crisp.nus.edu.sg/ers/ers.html>`_ 看到, 下面简要介绍原始数据的文件结构及数据提取. 本节以从ASF上下载的 `E2_84690_STD_L0_F137.zip` 原始回波数据文件和 `E2_84690_STD_F137.zip` 单视复数数据文件为例进行讲解.

目录及文件格式
~~~~~~~~~~~~~~

ERS产品采用CEOS(参见 :ref:`SubSection-CEOSProductDataFormationRadarProductSupplementRadar` 小节)格式存储数据,


在本书作者开发的 :guilabel:`iprs` 工具包中, 定义的SAR信号数据映射字典如 :code-block:numref:`code-iprsSarDataFileSignalDataRecordERS`, 如记录长度(``'Length of this record'``)字段的起止地址为 ``(9,12)``, 占4个字节, 类型为 ``1B4``, 即一个四字节的数. 又如字段 ``'Raw Data'``, 表示采样数据, 第一个样本的起止地址为 ``(413,414)``, 占2个字节, 类型为 ``2B4``, 即包含两个单字节整数.

.. code-block:: python
   :lineno-start: 1
   :emphasize-lines: 6,33
   :linenos:
   :caption: ERS Sar Data File Signal Data Record Descriptor Dictionary defined in :guilabel:`iprs`
   :name: code-iprsSarDataFileSignalDataRecordERS

    SarDataFileSignalDataRecordERS = {
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
        'Actual count of data pixels (samples)': [(25, 28), '1B4', 0],
        'Actual count of right-fill pixels': [(29, 32), '1B4', 0],
        'Reserved1': [(33, 84), '1I52', 0],
        'Spare1': [(85, 88), '1I4', 0],
        'Spare2': [(89, 92), '1I4', 0],
        'Reserved2': [(93, 124), '1I32', 0],
        'Spare3': [(125, 128), '1I4', 0],
        # PREFIX DATA PLATFORM REFERENCE INFORMATION
        'Platform information': [(129, 192), '1B64', 0],
        # PREFIX DATA - SENSOR/FACILITY SPECIFIC, AUXILIARY DATA
        'Fixed code = AA in Hexadecimal notation': [(193, 193), '1B1', 0],
        'OGRC/OBRC flag (1 or 0)': [(194, 194), '1B1', 0],
        'ICU on board time': [(195, 198), '1B4', 0],
        'Activity task': [(199, 200), '1B2', 0],
        'Image format counter': [(201, 204), '1B4', 0],
        'Sampling window start time': [(205, 206), '1B2', 0],
        'Pulse repetition interval': [(207, 208), '1B2', 0],
        'Calibration attenuation setting': [(209, 209), '1B1', 0],
        'Receiver gain attenuation setting': [(210, 210), '1B1', 0],
        'Spare4': [(211, 340), '130B1', 0],
        '36 calibration pulses as (4bit spare 6bit Q 6bit I from MSB down to LSB)': [(341, 412), '36B2', 0],
        # SAR RAW SIGNAL DATA
        'Raw Data': [(-1, -1), '2B1', 0]  # auto infer, (413, )
    }


数据读取与解析
~~~~~~~~~~~~~~

采用本书作者开发的 :guilabel:`iprs` 工具包可以读取ERS原始SAR回波数据, 使用 :guilabel:`iprs` 读取 `E2_84690_STD_L0_F137.zip` 中的 `E2_84690_STD_L0_F137.000.raw` 文件, 这里给出读取的SAR数据文件文件描述记录, 参见 :code-block:numref:`code-ERSSarDataFileFileDescriptorRecordE2_84690_STD_L0_F137`.


.. code-block:: python
   :lineno-start: 1
   :emphasize-lines: 6,14,9,27,28,45,50
   :linenos:
   :caption: Sar Data File File Descriptor Record in sar raw data file of product E2_84690_STD_L0_F137.
   :name: code-ERSSarDataFileFileDescriptorRecordE2_84690_STD_L0_F137

    Record sequence number [(1, 4), '1B4', [1]]
    l-st record sub-type code [(5, 5), '1B1', [63]]
    Record type code [(6, 6), '1B1', [192]]
    2-nd record sub-type code [(7, 7), '1B1', [18]]
    3-rd record sub-type code [(8, 8), '1B1', [18]]
    Length of this record [(9, 12), '1B4', [11644]]
    ASCII/EBCDIC flag [(13, 14), '1A2', ['A ']]
    1Blanks [(15, 16), '1A2', ['  ']]
    Format control document ID [(17, 28), '1A12', ['CEOS-SAR-CCT']]
    Format control document revision level [(29, 30), '1A2', ['B ']]
    File design descriptor revision letter [(31, 32), '1A2', ['B ']]
    Generating software release and revision level [(33, 44), '1A12', ['SKY 5.4.8   ']]
    File number [(45, 48), '1I4', [2]]
    File name [(49, 64), '1A16', ['ERS2.SAR.RAWIMGY']]
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
    Number of SAR DATA records (nominal) [(181, 186), '1I6', [28603]]
    SAR DATA record length (bytes) [(187, 192), '1I6', [11644]]
    Reserved1 (blanks) [(193, 216), '1A4', ['    ']]
    Number of bits per sample [(217, 220), '1I4', [16]]
    Number of samples per data group (or pixels) [(221, 224), '1I4', [1]]
    Number of bytes per data group (or pixel) [(225, 228), '1I4', [2]]
    Justification and order of samples within data group [(229, 232), '1A4', ['    ']]
    Number of SAR channels in this file [(233, 236), '1I4', [1]]
    Number of lines per data set (nominal) [(237, 244), '1I8', [28603]]
    Number of left border pixels per line [(245, 248), '1I4', [0]]
    Total number of data groups per line per SAR channel [(249, 256), '1I8', [5616]]
    Number of right border pixels per line [(257, 260), '1I4', [0]]
    Number of top border lines [(261, 264), '1I4', [0]]
    Number of bottom border lines [(265, 268), '1I4', [0]]
    Interleaving indicator [(269, 272), '1A4', ['BSQ ']]
    Number of physical records per line [(273, 274), '1I2', [1]]
    Number of physical records per multi-channel line [(275, 276), '1I2', [[]]]
    Number of bytes of prefix data per record [(277, 280), '1I4', [412]]
    Number of bytes of SAR data (or pixel data) per record (nominal) [(281, 288), '1I8', [11232]]
    Number of bytes of suffix data per record [(289, 292), '1I4', [0]]
    Reserved2 [(293, 340), '1A48', ['       1 4PB  37 2PB  33 4PB   9 4PB  17 4PB    ']]
    Blanks [(341, 368), '1A28', ['                            ']]
    Reserved3 [(369, 400), '1A32', ['                                ']]
    SAR Data format type identifier [(401, 428), '1A28', ['COMPLEX SIGNED INTEGER*2    ']]
    SAR Data format type code [(429, 432), '1A4', ['CIS2']]
    Number of left fill bits within pixel [(433, 436), '1I4', [0]]
    Number of right fill bits within pixel [(437, 440), '1I4', [0]]
    Maximum data range of pixel (max-min value for I and Q) [(441, 448), '1I8', [65535]]


由 :code-block:numref:`code-ERSSarDataFileFileDescriptorRecordE2_84690_STD_L0_F137` 知, 数据存储格式为 ``CEOS-SAR-CCT``, 该数据共 :math:`28603` 行脉冲数据, 每行为一次脉冲回波, 一个脉冲含 :math:`5616` 个距离单元, 每个像素含实部(I)虚部(Q)共2个字节, 故每行脉冲含11232个字节. 该记录长度为11644字节, 后面的SAR数据记录长度亦为11644字节.



单视复数数据读取
--------------------

:code-block:numref:`code-ERSSingleLookComplexDataRecordFormation` 给出了ERS合成孔径雷达单视复数数据文件的记录格式, 按照该格式读取数据即可, 本书作者开发的 :guilabel:`iprs` 工具包可以读取ERS单视复数数据, 读取函数为 :func:`read_ers_sar_slc`, :guilabel:`iprs` 中定义的用于读取处理后的SAR数据映射字典如下::

    SarDataFileProcessedDataRecordERS = {
        'Record sequence number': [(1, 4), '1B4', 0],
        'l-st record sub-type code': [(5, 5), '1B1', 0],
        'Record type code': [(6, 6), '1B1', 0],
        '2-nd record sub-type code': [(7, 7), '1B1', 0],
        '3-rd record sub-type code': [(8, 8), '1B1', 0],
        'Length of this record': [(9, 12), '1B4', 0],
        # SAR PROCESSED DATA
        'Processed Data': [(13, 16), '1C4', 0]  # '2F2' for [real, imag], or '1C4' for real + 1j*imag
    }


.. caution:: 需要注意的是, 下载到的单视复数数据可能仅仅是幅度图, 这种情况下, 读取到的 ``SAR Data format type code`` 值可能为 ``IU1`` 即一字节无符号整数, 而不是 :code-block:numref:`code-ERSSingleLookComplexDataRecordFormation` 中所列的 ``CI*4``. 此时将映射表中的 ``'Processed Data'`` 段的类型改为 ``'1B'`` 即可.


.. code-block:: text
   :lineno-start: 1
   :emphasize-lines: 6,14,9,27,28,45,50
   :linenos:
   :caption: Sar Data File File Descriptor Record in sar raw data file of product E2_84690_STD_L0_F137.
   :name: code-ERSSingleLookComplexDataRecordFormation

    ===DATA SET FILE FORMAT DEFINITION

    ---1 SAR DATA FILE - FILE DESCRIPTOR RECORD (FIXED SEGMENT)

    FIELD  BYTES    FORMAT  DESCRIPTION                                             CONTENT
     1     1-4      B4      Record sequence number                                      (1)
     2     5        Bl      1-st record sub-type code                                  (63)
     3     6        Bl      Record type code                                          (192)
     4     7        Bl      2-nd record sub-type code                                  (18)
     5     8        Bl      3-rd record sub-type code                                  (18)
     6     9-12     B4      Length of this record                                   (10012)
     7     13-14    A2      ASCII/EBCDIC flag                                            A$
     8     15-16    A2      blanks                                                       $$
     9     17-28    A12     Format control document ID for this data file
                            format CEOS-SAR-CCT
    10     29-30    A2      Format control document revision level                       $B
    11     31-32    A2      File design descriptor revision letter                       $B
    12     33-44    A12     Generating software release and revision level         <......>
    13     45-48    I4      File number                                                $$$2
    14     49-64    A16     File name                                      ERS1.SAR.SLCIMGY
    15     65-68    A4      Record sequence and location type flag                     FSEQ
    16     69-76    I8      Sequence number location                               $$$$$$$1
    17     77-80    I4      Sequence number field length                               $$$4
    18     81-84    A4      Record code and location type flag                         FTYP
    19     85-92    I8      Record code location                                   $$$$$$$5
    20     93-96    I4      Record code field length                                   $$$4
    21     97-100   A4      Record length and location type flag                       FLGT
    22     101-108  I8      Record length location                                 $$$$$$$9
    23     109-112  I4      Record length field length                                 $$$4
    24     113      A1      Reserved                                               <$....$>
    25     114      Al      Reserved                                               <$....$>
    26     115      Al      Reserved                                               <$....$>
    27     116      Al      Reserved                                               <$....$>
    28     117-180  A64     Reserved segment                                       <$....$>


    ---2 SAR DATA IMAGERY OPTIONS FILE FILE DESCRIPTOR RECORD VARIABLE SEGMENT

    FIELD  BYTES    FORMAT  DESCRIPTION                                             CONTENT

    29     181-186  I6      Number of SAR DATA records  (nominal)                   $15000
    30     187-192  I6      SAR DATA record length (bytes)                          $10012
    31     193-216  A24     Reserved (blanks)                                      <$....$>

                            SAMPLE GROUP DATA

    32     217-220  I4      Number of bits per sample                                 $$32
    33     221-224  I4      Number of samples per data group  (or pixels)             $$$1
    34     225-228  I4      Number of bytes per data group (or pixel)                 $$$4
    35     229-232  A4      Justification and order of samples within data group    <$....$>

                            SAR RELATED DATA IN THE RECORD

    36     233-236  I4      Number of SAR channels in this file                       $$$1
    37     237-244  I8      Number of lines per data set   (minimum)              $$$15000
    38     245-248  I4      Number of left border pixels per line                     $$$0
    39     249-256  I8      Total number of data groups per line per SAR channel  $$$$2500
    40     257-260  I4      Number of right border pixels per line                    $$$0
    41     261-264  I4      Number of top border lines                                $$$0
    42     265-268  I4      Number of bottom border lines                             $$$0
    43     269-272  A4      Interleaving indicator                                    BSQ$

                            RECORD DATA IN THE FILE

    44     273-274  I2      Number of physical records per line                         $1
    45     275-276  I2      Number of physical records per multi-channel line           $$
    46     277-280  I4      Number of bytes of prefix data per record                 $$$0
    47     281-288  I8      Number of bytes of SAR data (or pixel data)           $$$10000
                            per record (nominal)
    48     289-292  I4      Number of bytes of suffix data per record                 $$$0
    49-55  293-340  A48     reserved                                               <$....$>
    56     341-368  A28     blanks                                                 <$....$>
    57-60  369-400  A32     reserved                                               <$....$>
    61     401-428  A28     SAR Data format type identifier             COMPLEX$INTEGER$..$
    62     429-432  A4      SAR Data format type code                                  CI*4
    63     433-436  I4      Number of left fill bits within pixel                      $$$0
    64     437-440  I4      Number of right fill bits within pixel                     $$$0
    65     441-448  I8      Maximum data range of pixel                            $$$65535
    66     449-EOR  A15564  spare                                                  <$....$>

    ===DATA RECORD

    ---1 IMAGERY OPTIONS FILE - PROCESSED DATA RECORD

    FIELD  BYTES       FORMAT  DESCRIPTION                                            CONTENT

    1     1-4         B4      Record sequence number                                (n)
    2     5           Bl      1-st record sub-type code                             (50)
    3     6           Bl      Record type code                                      (11)
    4     7           Bl      2-nd record sub-type code                             (31)
    5     8           Bl      3-rd record sub-type code                             (20)
    6     9-12        B4      Length of this record     (nominal)                   (10012)
    7     13-16       C4      first sample of image line                            (n)
    8     17-20       C4      second sample of image line                           (n)

    .      .....    ..      ............................                            ..........

    5006   10009-10012 C4      last sample of image line                            (n)


读取的 `E2_84690_STD_F137` 文件中的数据大小为 :math:`9182×9182`, 实际有效数据大小为 :math:`9182×7833`, 从7834到9182列为填补的无效数据. 该数据实际上为幅度图像数据, 而不是复数数据, 由于数据较大, 故进行8倍降采样显示, 显示结果如 :figure:numref:`_fig-E2_84690_STD_F137` 所示, 其中左图未去除无效右边界像素, 右图去除了无效右边界的像素. 此外, 可以看到成像算法处理完后的数据对比度较低, 可以通过增强算法进行调整.

.. _fig-E2_84690_STD_F137:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/ERS/E2_84690_STD_F137.*
   :alt: Imaging result of Chirp Scaling Algorithm
   :align: center

   数据 E2_84690_STD_F137 中的图像数据. (左) 未去除无效右边界像素, (右) 去除无效右边界的像素.



原始数据成像
---------------------

本节给出Chirp Scaling Algorithm(CSA)在以上两景ERS数据上的成像结果, 有关CSA算法, 参见 :ref:`Section-ChirpScalingAlgorithmImagingSARRadar` 小节. 由于原始数据较大, 且方位向采样点数一般远大于距离向采样点数, 故这里仅给出降采样的成像结果图以及多视处理后的结果图. 对于数据 `E2_84690_STD_L0_F137`, 其方位向采样点数为 :math:`N_a=28603`, 距离向采样点数为 :math:`N_r=5616`, 成像后的单视复数图像矩阵大小为 :math:`28603 × 5616`, 将其降采样至 :math:`1024 × 1000`, 得到 :figure:numref:`fig-E2_84690_STD_L0_F137_CSA_Imaging_SLC` 所示结果. :figure:numref:`fig-E2_84690_STD_L0_F137_CSA_Imaging_MLC4` 显示的是方位向多视处理结果, 其中视数为4, 处理得到 :math:`7150 × 5616` 的数据, 将其降采样至 :math:`1024 × 1000` 显示. :figure:numref:`fig-E2_84690_STD_SLC_F137` 显示的是下载的数据 `E2_84690_STD_L0_F137` 的单视复数图像, 对比可以发现, CSA成像结果正确.


.. _fig-E2_84690_STD_SLC_F137:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/ERS/E2_84690_STD_SLC_F137.*
   :alt: Single Look Complex image of ERS SAR product (E2_84690_STD_SLC_F137)
   :align: center

   Single Look Complex image of ERS SAR product (E2_84690_STD_SLC_F137)


.. _fig-E2_84690_STD_L0_F137_CSA_Imaging_SLC:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/ERS/imageERSERS2_SAR_RAW=E2_84690_STD_L0_F137(sl=1el=28603)(sa0ea28603sr0er5616)_CSA_Imaging_SLC.*
   :alt: Single look imaging result of ERS SAR product (E2_84690_STD_L0_F137) using ChirpScaling Algorithm
   :align: center

   Single look imaging result of ERS SAR product (E2_84690_STD_L0_F137) using ChirpScaling Algorithm


.. _fig-E2_84690_STD_L0_F137_CSA_Imaging_MLC4:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/ERS/imageERSERS2_SAR_RAW=E2_84690_STD_L0_F137(sl=1el=28603)(sa0ea28603sr0er5616)_CSA_Imaging_MLC4.*
   :alt: Multiple look (4) imaging result of ERS SAR product (E2_84690_STD_L0_F137) using ChirpScaling Algorithm
   :align: center

   Multiple look (4) imaging result of ERS SAR product (E2_84690_STD_L0_F137) using ChirpScaling Algorithm


同样地, :figure:numref:`fig-E2_84686_STD_SLC_F203` 显示的是下载的数据 `E2_84686_STD_L0_F203` 的单视复数图像, `E2_84686_STD_L0_F203` 数据的方位向采样点数为 :math:`N_a=28659`, 距离向采样点数为 :math:`N_r=5616`, 成像后的单视复数图像矩阵大小为 :math:`28659 × 5616`, 将其降采样至 :math:`1024 × 1000`, 得到 :figure:numref:`fig-E2_84686_STD_L0_F203_CSA_Imaging_SLC` 所示结果. :figure:numref:`fig-E2_84686_STD_L0_F203_CSA_Imaging_MLC4` 显示的是方位向多视处理结果, 其中视数为4, 处理得到 :math:`7150 × 5616` 的数据, 将其降采样至 :math:`1024 × 1000` 显示


.. _fig-E2_84686_STD_SLC_F203:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/ERS/E2_84686_STD_SLC_F203.*
   :alt: Single Look Complex image of ERS SAR product (E2_84686_STD_SLC_F203)
   :align: center

   Single Look Complex image of ERS SAR product (E2_84686_STD_SLC_F203)


.. _fig-E2_84686_STD_L0_F203_CSA_Imaging_SLC:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/ERS/imageERSERS2_SAR_RAW=E2_84686_STD_L0_F203(sl=1el=28659)(sa0ea28659sr0er5616)_CSA_Imaging_SLC.*
   :alt: Single look imaging result of ERS SAR product (E2_84686_STD_L0_F203) using ChirpScaling Algorithm
   :align: center

   Single look imaging result of ERS SAR product (E2_84686_STD_L0_F203) using ChirpScaling Algorithm

.. _fig-E2_84686_STD_L0_F203_CSA_Imaging_MLC4:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/ERS/imageERSERS2_SAR_RAW=E2_84686_STD_L0_F203(sl=1el=28659)(sa0ea28659sr0er5616)_CSA_Imaging_MLC4.*
   :alt: Multiple look (4) imaging result of ERS SAR product (E2_84686_STD_L0_F203) using ChirpScaling Algorithm
   :align: center

   Multiple look (4) imaging result of ERS SAR product (E2_84686_STD_L0_F203) using ChirpScaling Algorithm


.. attention::
   需要注意的是, 使用CSA成像后得到的是单视复数图像数据 :math:`\bm I`, 经过多视处理后得到降噪后的多视数据, :figure:numref:`fig-E2_84690_STD_L0_F137_CSA_Imaging_SLC`, :figure:numref:`fig-E2_84690_STD_L0_F137_CSA_Imaging_MLC4`, :figure:numref:`fig-E2_84686_STD_L0_F203_CSA_Imaging_SLC`, :figure:numref:`fig-E2_84686_STD_L0_F203_CSA_Imaging_MLC4` 中显示的结果, 为成像复数结果的幅度图, 未进行RCS换算, 由此得到的图像往往对比度较低, 不能准确还原目标的RCS, 这里采用对数增强与截断操作增强图像 (参见 :ref:`SubSection-LogContrastEnhancementDigitalImageSignalProcessing` 小节). 此外, 仔细观察可以发现, 下载的单视复数结果图像与本节CSA算法成像结果略有不同, 后者场景区域稍大一些, 这是由于在进行CSA成像时, 未丢弃非完全成像边界区域.




