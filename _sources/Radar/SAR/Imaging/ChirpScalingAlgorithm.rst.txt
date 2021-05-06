.. _Section-ChirpScalingAlgorithmImagingSARRadar:

调频变标成像
=====================



调频变标原理
--------------------


Chirp Scaling



调频变标成像
---------------------


CSA方法概览
~~~~~~~~~~~~~~~~~~

.. note:: Chirp Scaling 算法

    **输入**: SAR原始回波数据矩阵 :math:`{\bm S}`, SAR平台参数

    **输出**: SAR复数图像

    Step1. 对时域回波数据 :math:`{\bm S}` 作方位FFT, 变换到距离多普勒域 :math:`{\rm FFT}({\bm S})`

    Step2. 通过相位相乘实现调频变标操作, 变标方程为 :eq:`equ-ChirpScaling`

    Step3. 对Step2中结果做FFT变换到二维频域

    Step4. 完成距离压缩, 二次距离压缩和一致RCMC

    Step5. 做距离向 IFFT 将数据变换回距离多普勒域

    Step6. 与随距离变化的匹配滤波器(含相位校正)相乘, 实现方位压缩

    Step7. 通过方位向IFFT将数据变换回二维时域, 即复数SAR图像.



调频变标
~~~~~~~~~~~~~~~~~~

线性调频变标方程为


.. math::
    s_{sc}(\tau^\prime, f_{\eta}) = {\rm exp}\left\{j\pi K_m \left[\frac{D(f_{\eta_{ref}}, V_{{r_{ref}}})}{D(f_{\eta}, V_{{r_{ref}}})} - 1\right](\tau^\prime)^2\right\}
    :label: equ-ChirpScaling

其中, :math:`{\tau^\prime} = \tau- \frac{2R_{ref}}{cD(f_{\eta}, V_{r_{ref}})}`, :math:`K_m = \frac{K_r}{1-K_r\frac{cR_0 f^2_{\eta}}{2V_r^2f_0^3 D^3(f_{\eta, V_r})}}`, :math:`D(f_{\eta}, V_r) = \sqrt{1-\frac{c^2f_{\eta}^2}{4V_r^2f_0^2}}`, 方位频率 :math:`f_{\eta}` 处的时间平移是距离时间的函数

.. math::
    \tau = \frac{2}{c}\left\{\frac{R_0}{D(f_{\eta_{ref}}, V_r)} + \left[ \frac{R_{ref}}{D(f_{\eta}, V_{r_{ref}})} - \frac{R_{ref}}{D(f_{f_{\eta_{ref}}}, V_{r_{ref}})}\right]\right\}




非线性调频变标方程 :cite:`LanG.CummingFrankH.Wong.2012` p209


距离压缩与距离徙动校正
~~~~~~~~~~~~~~~~~~

距离匹配滤波器仍为 :eq:`equ-MatchedFilterRange` 所示的匹配滤波器

.. math::
    H_r(f_\tau) = {\rm rect}\left(\frac{f_\tau}{|K_r|T_p}\right){\rm exp}\left(j\frac{\pi f_\tau^2}{K_r}\right),
    :label: equ-MatchedFilterRange


有关二次距离压缩的内容参见 :ref:`Section-RangeDopplerAlgorithmImagingSARRadar` 中的 :ref:`SubSection-LargeSquintProcessingRangeDopplerAlgorithmImagingSARRadar`.






整体RCM为

.. math::
    {\rm RCM}_{total}(R_0, f_{\eta}) = \frac{R_0}{D(f_{\eta}, V_r)} - \frac{R_0}{D(f_{\eta_{ref}}, V_r)}
    :label: equ-TotalRCM

一致RCM为

.. math::
    {\rm RCM}_{bulk}(f_{\eta}) = \frac{R_{ref}}{D(f_{\eta}, V_{r_{ref}})} - \frac{R_{ref}}{D(f_{\eta_{ref}}, V_{r_{ref}})}
    :label: equ-BulkRCM

补余RCM为 :eq:`equ-TotalRCM` 减去 :eq:`equ-BulkRCM`




方位向处理
~~~~~~~~~~~~~~~~~~~~~


:cite:`LanG.CummingFrankH.Wong.2012` p209



方位向包含三部分处理: 方位向匹配滤波, 附加相位校正, 方位向IFFT.


通过距离向IFFT完成距离向的处理, 得到距离多普勒域信号


.. math::
    S_4(\tau, f_{\eta}) = A_2 p_r\left(\tau-\frac{2R_0}{cD(f_{\eta_{ref}}, V_{r_{ref}})}\right)W_a(f_{\eta}-f_{\eta_c})\\
    × {\rm exp}\left\{-j\frac{4\pi R_0f_0D(f_{\eta}, V_r)}{c}\right\}\\
    × {\rm exp}\left\{j\frac{4\pi K_m}{c^2}\left[1-\frac{D(f_{\eta}, V_{r_{ref}})}{D(f_{\eta_{ref}}, V_{r_{ref}})}\right] \times \left[\frac{R_0}{D(f_{\eta}, V_r)} - \frac{R_{ref}}{D(f_{\eta, V_r})}\right]^2 \right\}
    :label: equ-CSA_AfterIFFT_RD


- 方位向匹配滤波器为 :eq:`equ-CSA_AfterIFFT_RD` 中的 **第一个指数项的复共轭**
- 对于线性调频变标, 附加相位校正乘法器为 :eq:`equ-CSA_AfterIFFT_RD` 中的 **第二个指数项的复共轭**





实验与分析
--------------------------


仿真数据实验
~~~~~~~~~~~~~~~

实验说明
^^^^^^^^^^^

实验参数及代码参见 :ref:`Section-BasicExperimentsExperimentsSARRadar` 小节, 设置斜视角 :math:`\theta_s = 8.5^°`.



实验结果
^^^^^^^^^^^

.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_4POINTS_RDSRCF2D.*
   :scale: 90 %
   :alt: 时域, 距离多普勒域及二维频域幅度相位谱
   :align: center

   时域, 距离多普勒域及二维频域幅度相位谱

   时域, 距离多普勒域及二维频域幅度相位谱.



.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CSA/CSA_4POINTS_RC_SRC_RCMC.*
   :scale: 90 %
   :alt: 距离压缩, 二次距离压缩及距离徙动校正结果
   :align: center

   距离压缩, 二次距离压缩及距离徙动校正结果

   距离压缩, 二次距离压缩及距离徙动校正结果


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CSA/CSA_4POINTS_RC_SRC_RCMC_DPC.*
   :scale: 80 %
   :alt: 多普勒相位补偿结果
   :align: center

   多普勒相位补偿结果

   多普勒相位补偿结果


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CSA/CSA_4POINTS_RC_SRC_RCMC_DPC_AC.*
   :scale: 100 %
   :alt: 方位向压缩结果 (含距离徙动校正)
   :align: center

   方位向压缩结果 (含距离徙动校正)

   方位向压缩结果 (含距离徙动校正)


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CSA/CSA_4POINTS_RC_SRC_DPC_AC.*
   :scale: 90 %
   :alt: CSA算法最终成像结果 (不含距离徙动校正, 含多普勒相位补偿)
   :align: center

   CSA算法最终成像结果 (不含距离徙动校正, 含多普勒相位补偿)

   CSA算法最终成像结果 (不含距离徙动校正, 含多普勒相位补偿)


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CSA/CSA_4POINTS_CSA_SRC_RCMC_ACo.*
   :scale: 90 %
   :alt: CSA算法最终成像结果 (含距离徙动校正, 不含多普勒相位补偿)
   :align: center

   CSA算法最终成像结果 (含距离徙动校正, 不含多普勒相位补偿)

   CSA算法最终成像结果 (含距离徙动校正, 不含多普勒相位补偿)


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CSA/CSA_4POINTS_CSA_SRC_RCMC_DPC_ACo.*
   :scale: 90 %
   :alt: CSA算法最终成像结果 (含距离徙动校正, 含多普勒相位补偿)
   :align: center

   CSA算法最终成像结果 (含距离徙动校正, 含多普勒相位补偿)

   CSA算法最终成像结果 (含距离徙动校正, 含多普勒相位补偿)



真实数据实验
~~~~~~~~~~~~~~~

实验数据
^^^^^^^^^^^

实验所采用数据为 RADARSAT1 卫星上的合成孔径雷达获取的温哥华地区的图像. 具体介绍参见 :ref:`Section-RADARSATRadarProductSupplementRadar` 小节.

实验说明
^^^^^^^^^^^


分析RDA算法中二次距离压缩与距离徙动补偿的影响.



实验代码
^^^^^^^^^^^

Python实现代码, 参见文件 `demo_RADARSAT1.py <https://github.com/antsfamily/iprs3.0/tree/master/examples/Products/demo_RADARSAT1.py>`_  .

.. literalinclude:: https://github.com/antsfamily/iprs3.0/tree/master/examples/Products/demo_RADARSAT1.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 43-49
   :linenos:
   :caption: demo_RADARSAT1.py
   :name: bind-id


实验结果
^^^^^^^^^^^


RADARSAT1 获取的史丹利公园的SAR数据幅度与相位

.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/SAR_StanleyPark_AmplitudePhase.*
   :scale: 90 %
   :alt: SAR raw data amplitude and phase of Stanley Park
   :align: center

   SAR raw data amplitude and phase of Stanley Park.

   SAR raw data amplitude and phase of Stanley Park.


CSA 成像结果


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CSA/CSA_StanleyPark_noSRC_noRCMC.*
    :scale: 90 %
    :alt: Imaging result of CSA (without SRC, without RCMC)
    :align: center

    Imaging result of CSA (without SRC, without RCMC)

    Imaging result of CSA (without SRC, without RCMC)


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CSA/CSA_StanleyPark_SRC_noRCMC.*
    :scale: 90 %
    :alt: Imaging result of CSA (with SRC, without RCMC)
    :align: center

    Imaging result of CSA (with SRC, without RCMC)

    Imaging result of CSA (with SRC, without RCMC)


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CSA/CSA_StanleyPark_noSRC_RCMC.*
    :scale: 90 %
    :alt: Imaging result of CSA (without SRC, with RCMC)
    :align: center

    Imaging result of CSA (without SRC, with RCMC)

    Imaging result of CSA (without SRC, with RCMC)


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CSA/CSA_StanleyPark_SRC_RCMC.*
    :scale: 90 %
    :alt: Imaging result of CSA (with SRC, with RCMC)
    :align: center

    Imaging result of CSA (with SRC, with RCMC)

    Imaging result of CSA (with SRC, with RCMC)

