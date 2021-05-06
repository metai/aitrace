.. _Section-SentinelRadarProductSupplementRadar:

Sentinel系列产品介绍
=====================


Sentinel-1 产品
--------------------------


从 `SCIHUB <https://scihub.copernicus.eu/>`_ 和 `ASF <https://www.asf.alaska.edu/>`_ 均可以下载 Sentinel 系列卫星产品数据, 有关 Sentinel-1 SAR 的信息可在 `这里 <https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar>`_ 查看.


Sentinel-1 雷达参数与工作模式
~~~~~~~~~~~~~~~~~~~~~~~~~~~


Sentinel-1 合成孔径雷达参数如 :table:numref:`table-ParametersSentinel1Platform`


.. table:: Sentinel-1平台参数
   :name: table-ParametersSentinel1Platform

   +-------------------------------------------+--------------------------------------------------------------+
   | Centre frequency                          | 5.405 GHz (corresponding to a wavelength of ~5.5465763cm cm) |
   +===========================================+==============================================================+
   | Bandwidth                                 | 0-100 MHz (programmable)                                     |
   +-------------------------------------------+--------------------------------------------------------------+
   | Polarisation                              | HH+HV, VV+VH, VV, HH                                         |
   +-------------------------------------------+--------------------------------------------------------------+
   | Incidence angle range                     | 20°- 46°                                                     |
   +-------------------------------------------+--------------------------------------------------------------+
   | Look direction                            | right                                                        |
   +-------------------------------------------+--------------------------------------------------------------+
   | Antenna type                              | Slotted waveguide radiators                                  |
   +-------------------------------------------+--------------------------------------------------------------+
   | Antenna size                              | 12.3 m x 0.821 m                                             |
   +-------------------------------------------+--------------------------------------------------------------+
   | Antenna mass                              | 880 kg (representing 40% of the total launch mass)           |
   +-------------------------------------------+--------------------------------------------------------------+
   | Azimuth beam width                        | 0.23°                                                        |
   +-------------------------------------------+--------------------------------------------------------------+
   | Azimuth beam steering range               | -0.9° to +0.9°                                               |
   +-------------------------------------------+--------------------------------------------------------------+
   | Elevation beam width                      | 3.43°                                                        |
   +-------------------------------------------+--------------------------------------------------------------+
   | Elevation beam steering range             | -13.0° to +12.3°                                             |
   +-------------------------------------------+--------------------------------------------------------------+
   | RF Peak power                             | - 4.368 kW, - 4.075 kW (IW, dual polarisations)              |
   +-------------------------------------------+--------------------------------------------------------------+
   | Pulse width                               | 5-100 µs (programmable)                                      |
   +-------------------------------------------+--------------------------------------------------------------+
   | Transmit duty cycle                       | Max 12%, SM 8.5%, IW 9%, EW 5%, WV 0.8%                      |
   +-------------------------------------------+--------------------------------------------------------------+
   | Receiver noise figure at module input     | 3 dB                                                         |
   +-------------------------------------------+--------------------------------------------------------------+
   | Maximum range bandwidth                   | 100 MHz                                                      |
   +-------------------------------------------+--------------------------------------------------------------+
   | PRF (Pulse Repetition Frequency)          | 1 000 - 3 000 Hz (programmable)                              |
   +-------------------------------------------+--------------------------------------------------------------+
   | Data compression                          | FDBAQ (Flexible Dynamic Block Adaptive Quantization)         |
   +-------------------------------------------+--------------------------------------------------------------+
   | ADC sampling frequency                    | 300 MHz (real sampling)                                      |
   +-------------------------------------------+--------------------------------------------------------------+
   | Data quantisation                         | 10 bit                                                       |
   +-------------------------------------------+--------------------------------------------------------------+
   | Total instrument mass (including antenna) | 945 kg                                                       |
   +-------------------------------------------+--------------------------------------------------------------+
   | Attitude steering                         | Zero-Doppler steering and roll steering                      |
   +-------------------------------------------+--------------------------------------------------------------+



Sentinel-1产品格式
~~~~~~~~~~~~~~~~~

传感器类型与产品类型
^^^^^^^^^^^^^^^^^

Sentinel-1 SAR 具有多种传感器模式和数据产品, 列举如下:

* 传感器模式 (Sensor Mode)
    - Level-0 and Level-1
        + 条带式 (Strip Map, SM): 80 km swath, 5 x 5 m spatial resolution
        + 干涉宽幅式 (Interferometric Wide Swath, IW): 250 km swath, 5 x 20 m spatial resolution
        + 超宽幅式 (Extra Wide Swath, EW): 400 km swath, 20 x 40 m spatial resolution
    - Level-2
        + Wave (WV)
        + 干涉宽幅宽式 (Interferometric Wide Swath, IW)
        + 超宽幅宽式 (Extra Wide Swath, EW)
* 产品类型 (Product Type)
    - Level-0
        + 原始回波数据格式 RAW
    - Level-1
        + 单视复数格式 (Single Look Complex, SLC)
        + 地距探测格式 Ground Range Detected (GRD)
    - Level-2
        + (Ocean, OCN) 包含3种成份: Ocean Swell spectra (OSW), Ocean Wind Fields (OWI), Surface Radial Velocities (RVL).


.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/SentinelX/Sentinel1_L1_products.png
   :alt: Sentinel1 SAR Level 1 级别产品
   :align: center

   Sentinel1 SAR Level 1 级别产品



.. hint::
   - `Sentinel PDF Documentation <https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/document-library>`_
   - 用户手册参见 `User Guides <https://earth.esa.int/web/sentinel/user-guides>`_
   - 技术手册参见 `Sentinel Technical Guides <https://earth.esa.int/web/sentinel/sentinel-technical-guides>`_
   - 传感器类型, 各级产品所采用的算法, 以及各级产品数据格式参见 `这里 <https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-1-sar/products-algorithms>`_.
   - 能量分布参见 `Willkommen bei den Energy Charts <https://www.energy-charts.de/>`_


Sentinel 产品数据命名格式
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/SentinelX/SentinelXProductNamingConvention.*
   :alt: Sentinel Product Naming Convention
   :align: center

   Sentinel 产品命名格式


举例如下

- ``S1A_S3_SLC__1SDV_20191202T094416_20191202T094445_030167_037285_9342`` : Sentinel1A_S3_单视复数_L1SAR双V极化(VV/VH)_起始时间_结束时间_绝对轨道号_任务数据获取ID_产品特有ID
- ``S1A_S3_RAW__0SDV_20191202T094415_20191202T094446_030167_037285_0156`` : Sentinel1A_S3_原始数据_L0SAR双V极化(VV/VH)_起始时间_结束时间_绝对轨道号_任务数据获取ID_产品特有ID





数据下载与处理
~~~~~~~~~~~~~~~~~


下载数据需要注册账号. 从scihub上下载数据可根据 `Self Registration <https://scihub.copernicus.eu/userguide/SelfRegistration>`_ 页面说明注册账号, 具体使用方法参见 `Overview <https://scihub.copernicus.eu/userguide/>`_; 从 asf 下载数据需要注册 `EARTHDATA <https://earthdata.nasa.gov/>`_ 账号. 若下载过慢, 可以使用多线程工具 (如 ``aria2c``).


.. hint:: 从scihub上下载数据时, 可通过右击设置多边形搜索区域.



SNAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- `SNAP Wiki <https://senbox.atlassian.net/wiki/spaces/SNAP/overview>`_
  + `Using SNAP in your Python programs <https://senbox.atlassian.net/wiki/spaces/SNAP/pages/24051781/Using+SNAP+in+your+Python+programs>`_
- `SANP docs <http://step.esa.int/main/doc/>`_
  + `SNAP Engine 2.0 API docs <http://step.esa.int/docs/v2.0/apidoc/engine/overview-summary.html>`_



Sentinel1 Level0级数据解析
~~~~~~~~~~~~~~~~~~~~~~~~~

Sentinel1 Level0 有四种数据产品: 标准产品、校正产品、噪声产品、标记产品; 波束模式可以为 SM, IW, EW, WV; 极化模式可以为单极化和双极化. 由于块自适应量化型 (Block Adaptive Quantisation-like, BAQ) 原始数据压缩器会引入量化噪声, 造成信噪比下降, 因而 Sentinel1 数据采用弹性动态块自适应量化 (Flexible Dynamic Block Adaptive Quantisation, FDBAQ) 技术, FDBAQ是基于熵约束块自适应量化(Entropy Constrained Block Adaptive Quantisation, ECBAQ)算法做出的改进.

Sentinel产品数据格式基于欧洲标准文件格式(Standard Archive Format for Europe, SAFE)定制. SENTINEL-SAFE 格式包裹了一个包含二进制格式的图像数据和XML格式的产品元数据(metadata), 用法相当灵活, 足以表达各级别的Sentinel数据产品. 通常 Sentinel Level0 级 ``SAFE`` 格式产品包含以下文件:

- :attr:`manifest.safe` : 以XML格式保存一般的产品信息(平台, 任务, 仪器, 产品历史, 时序, 轨道等等)
- :attr:`xxxxx.dat` : 观测数据组件(若为单极化则含有一个二进制数据文件, 若为双极化则含有两个二进制数据文件), 数据以大端(big-endian)格式存储
- :attr:`xxxx_index.dat` : 索引数据组件(若为单极化则含有一个二进制索引文件, 若为双极化则含有两个二进制索引文件), 索引数据包含了数据逻辑块描述(字节位置, 时间, 大小等等), 它指向了观测数据中的子块, 使得可以快速获取子块数据.
- :attr:`xxxx_annot.dat` : 注释数据组件是二进制文件, 索引数据文件(若为单极化则含有一个二进制索引文件, 若为双极化则含有两个二进制索引文件), 索引数据包含了数据逻辑块描述(字节位置, 时间, 大小等等), 它指向了观测数据中的子块, 使得可以快速获取子块数据.
- :attr:`support` : 表示数据文件的支持文件夹, 以XML格式提供观测数据和注释数据的格式或语法信息.

如 :figure:numref:`fig-StructureOfSentinel1SARLevel0Safe` 所示, 为双极化RAW格式数据, 可以看到上述文件组件, 详细的Level0级文件格式可参考文档 `Sentinel1 Level0 Product Format Specifications <https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/document-library/>`_


.. _fig-StructureOfSentinel1SARLevel0Safe:

.. figure:: ../../../_static/figs/Radar/Supplement/RadarProducts/SentinelX/Sentinel_RAW_L0_SAFE_demo.*
   :alt: Sentinel1 SAR Level 0 级别产品SAFE文件结构示例
   :align: center

   Sentinel1 SAR Level 0 级别产品SAFE文件结构示例



Sentinel-2 雷达
--------------------------

