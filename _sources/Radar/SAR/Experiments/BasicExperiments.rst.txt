.. _Section-BasicExperimentsExperimentsSARRadar:

基础分析实验
=====================


实验说明
---------

通过点目标仿真, 分析理解调频率, 分辨率等概念.


Python实现代码, 参见文件 `demo_AirboneSAR_Points.py <https://github.com/antsfamily/iprs3.0/tree/master/examples/Air/demo_AirboneSAR_Points.py>`_  .

.. literalinclude:: https://github.com/antsfamily/iprs3.0/tree/master/examples/Air/demo_AirboneSAR_Points.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 43-49
   :linenos:
   :caption: demo_AirboneSAR_Points.py
   :name: bind-id


实验参数
~~~~~~~~~

实验参数如 :table:numref:`table-ParametersSimulatedAirSARPlatform` 所示, 类似文献 :cite:`LanG.CummingFrankH.Wong.2012` 中138页的点目标仿真实验中的参数, 部分参数不一致.


.. table:: 仿真的机载SAR平台参数
   :name: table-ParametersSimulatedAirSARPlatform

   +------------------+--------------------+--------------------+--------------+
   | 参数             | 符号               | 数值               | 单位         |
   +==================+====================+====================+==============+
   | 平台高度         | :math:`H`          | 10                 | :math:`km`   |
   +------------------+--------------------+--------------------+--------------+
   | 雷达有效速度     | :math:`V`          | 150                | :math:`m/s`  |
   +------------------+--------------------+--------------------+--------------+
   | 场景中心斜距     | :math:`R_c`        | 20                 | :math:`km`   |
   +------------------+--------------------+--------------------+--------------+
   | 雷达载频         | :math:`f_0`        | 5.3                | :math:`GHz`  |
   +------------------+--------------------+--------------------+--------------+
   | 发射脉冲时宽     | :math:`T_p`        | 2.5                | :math:`μs`   |
   +------------------+--------------------+--------------------+--------------+
   | 距离向调频率     | :math:`K_r`        | -20.0e12, +20.0e12 | :math:`Hz/s` |
   +------------------+--------------------+--------------------+--------------+
   | 距离向采样率     | :math:`F_{r}`      | 60.0               | :math:`MHz`  |
   +------------------+--------------------+--------------------+--------------+
   | 距离向采样点数   | :math:`N_{r}`      | 320                |              |
   +------------------+--------------------+--------------------+--------------+
   | 方位向采样率     | :math:`F_{a}`      | 100                | :math:`Hz`   |
   +------------------+--------------------+--------------------+--------------+
   | 方位向采样点数   | :math:`N_{a}`      | 256                |              |
   +------------------+--------------------+--------------------+--------------+
   | 距离向天线孔径   | :math:`L_{r}`      | 12.0               | :math:`m`    |
   +------------------+--------------------+--------------------+--------------+
   | 方位向天线孔径   | :math:`L_{a}`      | 3.0                | :math:`m`    |
   +------------------+--------------------+--------------------+--------------+
   | 下视角           | :math:`\theta_{d}` | 30                 | :math:`°`    |
   +------------------+--------------------+--------------------+--------------+
   | 波束距离向宽度   | :math:`\theta_{b}` | 1.32, 1.32, 1.32   | :math:`°`    |
   +------------------+--------------------+--------------------+--------------+
   | 波束斜视角       | :math:`\theta_{s}` | 0.0, 3.5, 21.9     | :math:`°`    |
   +------------------+--------------------+--------------------+--------------+
   | 波束中心偏移时间 | :math:`\eta_{c}`   | 0.0, -8.1, -49.7   | :math:`s`    |
   +------------------+--------------------+--------------------+--------------+
   | 多普勒中心频率   | :math:`f_{\eta_c}` | 0.0, 320, 1975     | :math:`Hz`   |
   +------------------+--------------------+--------------------+--------------+


根据上表参数, 可以计算出如下参数


- 场景中心斜距: :math:`R_c = H / {\rm sin}\theta_d ≈ 20000.0m`
- 最短斜距: :math:`R_0 = R_c {\rm cos} \theta_s ≈ 18556.7m`
- 斜距分辨率: :math:`\Delta_r = \frac{c}{2B_r} = \frac{c}{2|K_r|T_p} ≈ 2.99m`
- 地距分辨率: :math:`\Delta_x = \Delta_r /{\rm cos}\theta_i ≈ 3.46m`
- 方位向距离分辨率: :math:`\Delta_a=\Delta_y = L_a/2 = 1.5m`
- 场景中心坐标: :math:`(x_c, y_c)`, :math:`x_c = {\sqrt{R_0^2 - H^2}}`, :math:`y_c = R_c{\rm sin}\theta_s`
    + :math:`\theta_s = 0, x_c=17320.50m, y_c=0m`
    + :math:`\theta_s = 3.5, x_c=17286.62m, y_c=1221.45m`
    + :math:`\theta_s = 21.9, x_c=15640.55m, y_c=7462.73m`
- 近地点斜距: :math:`R_{near} = H/{\rm sin}(\theta_d+\theta_b/2)`
    + :math:`\theta_s = 0, R_{near}=19609.59m`
    + :math:`\theta_s = 3.5, R_{near}=19610.05m`
    + :math:`\theta_s=21.9, R_{near}=19609.59m`
- 远地点斜距: :math:`R_{far} = H/{\rm sin}(\theta_d-\theta_b/2)`
    + :math:`\theta_s = 0, R_{far}=20409.03m`
    + :math:`\theta_s = 3.5, R_{far}=20409.03m`
    + :math:`\theta_s=21.9, R_{far}=20409.03m`
- 刈幅宽度 (swath size): :math:`S_x = (H/{\rm tan}(\theta_d-\theta_b/2) - H/{\rm tan}(\theta_d+\theta_b/2)){\rm cos}\theta_s = 921.9{\rm cos}\theta_s`
    + :math:`\theta_s = 0, S_x=923.05m`
    + :math:`\theta_s = 3.5, S_x=921.91m`
    + :math:`\theta_s = 21.9, S_x=880.48m`
- 方位向成像宽度: :math:`S_y = VT_{sa} = 384.0m`
- 成像区域: :math:`(x_{min}, x_{max}, y_{min}, y_{max})`
    + :math:`\theta_s = 0, SA=(-461.53, 461.53, -192.0, 192.0)`
    + :math:`\theta_s = 3.5, SA=(-460.96, 460.95, -192.0, 192.0)`
    + :math:`\theta_s = 21.9, SA=(-440.58, 439.91, -192.0, 192.0)`

调频方向分析
-------------

设置目标位于场景中心处, 即相对坐标 :math:`(0, 0)`, 目标强度为 1, 观察不同调频方向, 不同斜视角下的时域(原始信号), 距离多普勒域(原始信号在方位维做FFT), 频域(原始信号在距离和方位上均做FFT)的幅度相位.


零斜视角, :math:`\theta_s=0.0^°`, 正调频

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/OnePointKr20e12As0Ad30.*
    :scale: 90 %
    :alt: The property of point target in Range Doppler domain (positive frequency modulation).
    :align: center

    The property of point target in different domain (positive frequency modulation).


零斜视角, :math:`\theta_s=0.0^°`, 负调频

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/OnePointKr-20e12As0Ad30.*
    :scale: 90 %
    :alt: The property of point target in Range Doppler domain (negative frequency modulation).
    :align: center

    The property of point target in different domain (negative frequency modulation).



斜视角 :math:`\theta_s=3.5^°` , 正调频

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/OnePointKr20e12As3d5Ad30.*
    :scale: 90 %
    :alt: The property of point target in Range Doppler domain (positive frequency modulation).
    :align: center

    The property of point target in different domain (positive frequency modulation).


斜视角 :math:`\theta_s=3.5^°` , 负调频

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/OnePointKr-20e12As3d5Ad30.*
    :scale: 90 %
    :alt: The property of point target in Range Doppler domain (negative frequency modulation).
    :align: center

    The property of point target in different domain (negative frequency modulation).

斜视角 :math:`\theta_s=21.9^°` , 正调频

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/OnePointKr20e12As21d9Ad30.*
    :scale: 90 %
    :alt: The property of point target in Range Doppler domain (positive frequency modulation).
    :align: center

    The property of point target in different domain (positive frequency modulation).


斜视角 :math:`\theta_s=21.9^°` , 负调频

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/OnePointKr-20e12As21d9Ad30.*
    :scale: 90 %
    :alt: The property of point target in Range Doppler domain (negative frequency modulation).
    :align: center

    The property of point target in different domain (negative frequency modulation).




分辨率分析
-------------


设置目标为 :math:`(0.0, 0.0), (-6, -6), (-6, 6), (6, -6), (6, 6), (9, 9)`, 目标强度均为1, 进行如下设置.

- 方位向设置
    + 采样率: :math:`F_{sa} = 100Hz` 和 :math:`F_{sa} = 200Hz`
    + 采样点: :math:`N_{sa} = 256` 和 :math:`N_{sa} = 1024`
    + 天线孔径: :math:`L_{a} = 6.0m`, :math:`L_{a} = 3.0m` 和 :math:`L_{a} = 1.5m`
- 距离向设置
    + 采样率: :math:`F_{sr} = 60.0e6Hz`
    + 采样点: :math:`N_{sr} = 320` 和 :math:`N_{sr} = 1280`
    + 调频率: :math:`K_{r} = -20.0e12Hz/s`和 :math:`K_{r} = -40.0e12Hz/s`
    + 脉宽: :math:`Tp = 2.5e-6s` 和 :math:`Tp = 5.0e-6s`


方位向的分辨率由方位向天线孔径长度与方位向采样率决定, 其中, :math:`L_a` 直接决定方位向分辨率上限 :math:`ΔR_a`, :math:`F_{sa}` 决定了能多大程度地恢复方位向分辨率为 :math:`ΔR_a` 场景数据. 即使是过采样, 恢复后的最大分辨率仍然为 :math:`ΔR_a`, 但若是欠采样, 恢复后的分辨率将小于 :math:`ΔR_a`.

距离向的分辨率由距离向带宽和采样率决定, 其中, :math:`Br = |K_r|T_P` 决定了距离向分辨率上限 :math:`ΔR_r`, :math:`F_{sr}` 决定了能多大程度地恢复方位向分辨率为 :math:`ΔR_a` 场景数据. 即使是过采样, 恢复后的最大分辨率仍然为 :math:`ΔR_r`, 但若是欠采样, 恢复后的分辨率将小于 :math:`ΔR_r`.


.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/Fsr60e6Nsr320Kr10e12Tp25e-7Fsa100Nsa256La6.*
    :scale: 90 %
    :alt: Imaging result of RDA.
    :align: center

    Imaging result of RDA.

    Imaging result of RDA. :math:`F_{sa}=100Hz`, :math:`N_{sa}=256`, :math:`L_a=6m`, :math:`F_{sr}=60e6Hz`, :math:`N_{sr}=320`, :math:`K_r=10e12Hz/s`, :math:`T_p=2.5e-6s`

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/Fsr60e6Nsr320Kr20e12Tp25e-7Fsa100Nsa256La3.*
    :scale: 90 %
    :alt: Imaging result of RDA.
    :align: center

    Imaging result of RDA.

    Imaging result of RDA. :math:`F_{sa}=100Hz`, :math:`N_{sa}=256`, :math:`L_a=3m`, :math:`F_{sr}=60e6Hz`, :math:`N_{sr}=320`, :math:`K_r=20e12Hz/s`, :math:`T_p=2.5e-6s`

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/Fsr240e6Nsr1280Kr40e12Tp25e-6Fsa200Nsa1024La1p5.*
    :scale: 90 %
    :alt: Imaging result of RDA.
    :align: center

    Imaging result of RDA.

    Imaging result of RDA. :math:`F_{sa}=200Hz`, :math:`N_{sa}=1024`, :math:`L_a=1.5m`, :math:`F_{sr}=240e6Hz`, :math:`N_{sr}=1280`, :math:`K_r=40e12Hz/s`, :math:`T_p=25e-6s`



.. _SubSection-RCMCBasicExperimentsExperimentsSARRadar:

距离徙动校正
----------------


设置斜视角 :math:`\theta_s = 8.5^°`, 调频率 :math:`K_r=20e12, L_a=3.0, L_r=12`, 方位向采样率 :math:`F_{sa}=100Hz`, 距离向采样率 :math:`F_{sr}=60MHz`,  目标位置 :math:`(0, 0)`, 目标强度均为1. 分析距离徙动校正的效果, 分析不同大小的 :math:`\rm{sinc}` 插值核 :math:`r=4, 8, 32` 的影响.

:figure:numref:`fig-RCMC_before_rcmcsinc` 显示的是二次距离压缩及多普勒相位补偿后的结果, 即为进行距离徙动校正, :figure:numref:`fig-RCMC_after_rcmcsinc4`, :figure:numref:`fig-RCMC_after_rcmcsinc8`, :figure:numref:`fig-RCMC_after_rcmcsinc32` 为 :math:`\rm{sinc}` 插值核大小分别为 :math:`r=4, 8, 32` 的时的距离徙动校正后的结果. 可见, 经过插值核越大, 距离徙动校正越精确.

.. _fig-RCMC_before_rcmcsinc:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/RCMC_before_rcmcsinc.*
   :scale: 90%
   :alt: After RC SRC, DPC
   :align: center

   After RC SRC, DPC

   After RC SRC, DPC

.. _fig-RCMC_after_rcmcsinc4:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/RCMC_after_rcmcsinc4.*
   :scale: 90%
   :alt: After RC SRC, DPC, RCMC
   :align: center

   After RC SRC, DPC, RCMC. :math:`\rm sinc` interpolation, :math:`r=4`.

   After RC SRC, DPC, RCMC. :math:`\rm sinc` interpolation, :math:`r=4`.


.. _fig-RCMC_after_rcmcsinc8:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/RCMC_after_rcmcsinc8.*
   :scale: 90%
   :alt: After RC SRC, DPC, RCMC.
   :align: center

   After RC SRC, DPC, RCMC. :math:`\rm sinc` interpolation, :math:`r=8`.

   After RC SRC, DPC, RCMC. :math:`\rm sinc` interpolation, :math:`r=8`.

.. _fig-RCMC_after_rcmcsinc32:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/RCMC_after_rcmcsinc32.*
   :scale: 90%
   :alt: After RC SRC, DPC, RCMC.
   :align: center

   After RC SRC, DPC, RCMC. :math:`\rm sinc` interpolation, :math:`r=32`.

   After RC SRC, DPC, RCMC. :math:`\rm sinc` interpolation, :math:`r=32`.


:figure:numref:`fig-RCMC_RDA_noRCMC` 给出了无距离徙动校正条件下, 距离多普勒成像算法的成像结果, 由图可见, 距离徙动现象很明显, 同一目标分布在不同距离与方位单元. :figure:numref:`fig-RCMC_RDA_rcmcsinc4`, :figure:numref:`fig-RCMC_RDA_rcmcsinc8`, :figure:numref:`fig-RCMC_RDA_rcmcsinc32` 为 :math:`{\rm sinc}` 插值核分别为 :math:`4,8,32` 的条件下, 距离多普勒算法的成像结果, 对比 :figure:numref:`fig-RCMC_RDA_noRCMC` - :figure:numref:`fig-RCMC_RDA_rcmcsinc32`, 可以发现, 基于 :math:`\rm sinc` 插值的距离徙动算法校正效果明显, 且插值核越大, 距离徙动校正越精确.



.. _fig-RCMC_RDA_noRCMC:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/RCMC_RDA_noRCMC.*
   :scale: 90%
   :alt: Imaging results of RDA (Without RCMC)
   :align: center

   Imaging result of RDA.

   Imaging result of RDA. Without RCMC.


.. _fig-RCMC_RDA_rcmcsinc4:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/RCMC_RDA_rcmcsinc4.*
   :scale: 90%
   :alt: Imaging results of RDA
   :align: center

   Imaging result of RDA. :math:`\rm sinc` interpolation (:math:`r=4`).

   Imaging result of RDA. :math:`\rm sinc` interpolation (:math:`r=4`).

.. _fig-RCMC_RDA_rcmcsinc8:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/RCMC_RDA_rcmcsinc8.*
   :scale: 90%
   :alt: Imaging results of RDA
   :align: center

   Imaging result of RDA. :math:`\rm sinc` interpolation (:math:`r=8`).

   Imaging result of RDA. :math:`\rm sinc` interpolation (:math:`r=8`).

.. _fig-RCMC_RDA_rcmcsinc32:

.. figure:: ../../../_static/figs/Radar/SAR/Experiments/BasicExperiments/RCMC_RDA_rcmcsinc32.*
   :scale: 90%
   :alt: Imaging results of RDA
   :align: center

   Imaging result of RDA. :math:`\rm sinc` interpolation (:math:`r=32`).

   Imaging result of RDA. :math:`\rm sinc` interpolation (:math:`r=32`).







