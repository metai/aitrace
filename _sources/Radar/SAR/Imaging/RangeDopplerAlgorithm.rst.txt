.. _Section-RangeDopplerAlgorithmImagingSARRadar:

距离多普勒成像
=====================

距离多普勒方法
---------------


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA.png
   :scale: 80 %
   :alt: Range Doppler Algorithm
   :align: center

   Framework of Range Doppler Algorithm



.. hint::
    对于大斜视SAR, 距离压缩中包含二次距离压缩 (Second Rage Compression, SRC), 距离徙动校正也不一样.


小斜视下的RDA
~~~~~~~~~~~~~~


SAR原始数据
^^^^^^^^^^^^^^^^^

SAR 原始数据是指SAR系统接收到的数据, 数据先被解调至基带, 距离频率中心被置零, 解调后的基带信号为 (参见: :ref:`Section-SARSignalSystemOverviewSARRadar` 小结, :eq:`equ-SARPhaseHistory` )

.. math::
   \begin{aligned}
   s_i(\eta, \tau) &= G_i h(\tau, \eta)\\ &= G_i w_r\left(\tau-2R(\eta)/c\right) w_a(\eta-\eta_c)\\
   &   {\rm exp}\left\{ -j4\pi f_0 R(\eta)/c  +  j\pi K_r\left(\tau-2R(\eta)/c\right)^2 \right\}.
   \end{aligned}


距离压缩
^^^^^^^^^^^^^^^^^

- 将SAR基带信号的距离维FFT变换 :math:`S_r(\eta, f_\tau)` 与距离向匹配滤波器 :math:`H_r(f_{\tau})` 相乘;
- 进行距离维逆FFT完成距离维压缩.

匹配滤波器的生成与实现方式不同, 距离压缩的方式也不同. 如采用复制脉冲尾部补零经FFT后的复共轭作为滤波器.

SAR回波信号 :math:`s(\eta, \tau)` 的距离维傅里叶变换为

.. math::
   \begin{aligned}
   S_r(\eta, f_{\tau}) &={\rm FFT}_{\tau}\left\{s(\eta, \tau)\right\}\\ &= G W_r(f_\tau)w_a(\eta-\eta_c) \\
   &
   {\rm exp}\left\{-j\frac{4\pi(f_0+f_\tau)R(\eta)}{c}\right\}{\rm exp}\left\{-j\frac{\pi f_\tau^2}{K_r}\right\},
   \end{aligned}

其中, :math:`G` 为常数, :math:`W_r(f_\tau)=w_r(f_\tau/K_r)` 是距离频谱的包络.

匹配滤波的目的在于消除上式中的第二个指数项, 故取距离向匹配滤波器为

.. math::
    H_r(f_\tau) = {\rm exp}\left\{j\frac{\pi f_\tau^2}{K_r}\right\},
    :label: equ-MatchedFilterRange


对滤波器输出进行距离向IFFT, 得到距离向压缩输出为


.. math::
   \begin{aligned}
   s_{rc}(\eta, \tau) &= {\rm IFFT}_{\tau}\left\{S_r(\eta, f_{\tau})H_r(f_{\tau})\right\} \\
   &= G p_r\left(\tau-\frac{2R(\eta)}{c}\right)w_a(\eta-\eta_c) \\
   &  {\rm exp}\left(-j\frac{4\pi f_0 R(\eta)}{c}\right),
   \end{aligned}
   :label: equ-SARSignalRangeCompressionOut

其中, 压缩脉冲包络 :math:`p_r(\tau)` 为窗函数 :math:`W_r(f_{\tau})` 的傅里叶逆变换: 对于矩形窗, :math:`p_r(\tau)` 为 :math:`\rm sinc` 函数, 对于锐化窗(kasier), :math:`p_r(\tau)` 为旁瓣较低的 :math:`\rm sinc` 函数. :math:`G` 为包括散射系数在内的总增益, 常假定为1.



方位向傅里叶变换
^^^^^^^^^^^^^^^^^

小斜视下, 波束指向接近零多普勒方向, 且 :math:`R_0 \gg V_r\eta` , 可将距离近似为抛物线

.. math::
    R(\eta) = \sqrt{R_0^2 +V_r^2\eta^2} \thickapprox R_0 + \frac{V_r^2\eta^2}{2R_0},

代入距离向压缩输出表达 :eq:`equ-SARSignalRangeCompressionOut` 得

.. math::
    s_{rc}(\eta,\tau) \thickapprox G p_r(\tau-\frac{2R(\eta)}{c})w_a(\eta-\eta_c) \\
    \qquad {\rm exp}\left(-j\frac{4\pi f_0 R_0}{c}\right) {\rm exp}\left(-j \frac{\pi 2V_r^2 \eta^2}{\lambda R_0}\right).

方位向的时频关系为 :math:`f_{\eta} = -K_a\eta` , 其中记方位向调频率 :math:`K_a \thickapprox \frac{2V_r^2}{\lambda R_0}` , 代入上式, 方位向FFT后的信号变为

.. math::
   \begin{aligned}
   S_a(f_{\eta}, \tau) &= {\rm FFT}_{\eta}\left\{s_{rc}(\eta, \tau)\right\} \\
   &= G p_r(\tau-\frac{2R_{rd}(f_\eta)}{c})W_a(f_\eta-f_{\eta_c}) \\
   & {\rm exp}\left(-j \frac{4\pi f_0 R_0}{c}\right) {\rm exp}\left(j \frac{\pi {f_\eta}^2}{K_a}\right),
   \end{aligned}

其中, :math:`W_a(f_{\eta} - f_{\eta_c})` 为方位向天线方向图 :math:`w_a(\eta-\eta_c)` 的频域形式. 第一个指数项含有目标固有的相位信息(干涉极化)与图像强度无关. 第二项指数项为具有线性调频特性的频域方位调制. 距离徙动补偿项为

.. math::
   R_{rd}(f_\eta) \thickapprox R_0 + \frac{V_r^2}{2R_0}\left(\frac{f_\eta}{K_a}\right)^2 = R_0 + \frac{\lambda^2R_0 f_{\eta}^2}{8V_r^2}.

距离徙动校正
^^^^^^^^^^^^^^^^^

距离徙动校正 (RCMC) 有两种实现方式.

一种是在距离多普勒域进行距离插值, 可以基于 :math:`\rm sinc` 函数进行插值处理. 需要校正的 RCM 为方位频率 :math:`f_\eta` 的函数, 也是 :math:`R_0` 的函数:

.. math::
    \Delta R(f_\eta) = \frac{\lambda^2R_0f_\eta^2}{8V_r^2}.

距离徙动校正因子：

.. math::
    D(f_{\eta}, V_r) = \sqrt{1-\frac{c^2f_{\eta}^2}{4V_r^2f_0^2}} = \sqrt{1- \frac{\lambda^2f_{\eta}^2 }{4V_r^2}}
    :label: equ-RCMC_factor_RD



另一种是基于RCM在有限区域内不随距离改变, 从而可以通过 ``FFT --> 线性相位相乘 --> IFFT`` 实现, 相位乘法器为

.. math::
    Q_{rcmc}(f_\tau) = {\rm exp}\left(j\frac{4\pi f_\tau \Delta R(f_\eta)}{c}\right),

但这种需要对数据进行分块, 复杂度高, 一般不采用.


基于 :math:`\rm sinc` 插值进行RCMC后的信号变为

.. math::
   \begin{aligned}
   S_{rcmc}(f_{\eta}, \tau) &= {\rm FFT}_{\eta}\left\{s_{rc}(\eta, \tau)\right\} \\
   &= G p_r \left(\tau-\frac{2R_0}{c}\right)W_a(f_\eta-f_{\eta_c}) \\
   & {\rm exp}\left(-j\frac{4\pi f_0 R_0}{c}\right) {\rm exp}\left(j\frac{\pi {f_\eta}^2}{K_a}\right).
   \end{aligned}


有关实验请参考 :ref:`SubSection-RCMCBasicExperimentsExperimentsSARRadar` 小节.


方位压缩
^^^^^^^^^^^^^^^^^

- 将方位向FFT后的 :math:`S_a(f_{\eta}, \tau)` (或RCMC后的 :math:`S_{rcmc}(f_{\eta}, \tau)` ) 与方位向匹配滤波器 :math:`H_a(f_{\eta})` 相乘;
- 进行方位维逆FFT完成方位维压缩.

方位向压缩在于消除方位向FFT(或RCMC)后的信号的第二个指数项成分, 因而匹配滤波器为其复共轭:

.. math::
    H_{a}(f_\eta) = {\rm exp}\left\{-j\frac{\pi f_\eta^2}{K_a}\right\}.

实现方式如下


匹配滤波后的输出变为


.. math::
   \begin{aligned}
   {S_{af}}({f_\eta },\tau ) &= {S_{rcmc}}({f_\eta },\tau ){H_a}({f_\eta })\\ &= G{p_r}\left( {\tau  - \frac{{2{R_0}}}{c}} \right){W_a}({f_\eta } - {f_\eta }_c)\\
   &{\rm{exp}}\left( { - j\frac{{4\pi {f_0}{R_0}}}{c}} \right)
   \end{aligned}
   :label: equ-MatchedFilterAzimuth

经过方位向IFFT后的压缩信号为

.. math::
   \begin{aligned}{s_{ac}}(\eta ,\tau ) &= {\rm{IFFT}}_\eta\left\{ {{S_{af}}({f_\eta },\tau )} \right\}\\ &= G{p_r}\left(\tau  - \frac{{2{R_0}}}{c}\right){p_a}(\eta )\\
   & {\rm{exp}}\left( { - j\frac{{4\pi {f_0}{R_0}}}{c}} \right){\rm{exp}}\left( {j2\pi {f_\eta }_c\eta } \right),
   \end{aligned}

其中, :math:`p_a` 为方位向冲击响应的幅度, 与 :math:`p_r` 一样为 :math:`{\rm sinc}` 函数. 至此, 目标已经被校正到 :math:`\eta = 0, \tau=2R_0/c` 处.


.. hint::
    在非零斜视角下, 使用抛物线近似距离使得相位精度不能被保证, 可以使用双曲相位形式的匹配滤波器, 即不进行近似.

多视处理
^^^^^^^^^^^^^^^^^

多视处理可以减少相干斑点噪声, 其主要思路是在方位向做平均滤波, 当然也可以在距离向上做滤波.


.. _SubSection-LargeSquintProcessingRangeDopplerAlgorithmImagingSARRadar:

大斜视下的RDA
~~~~~~~~~~~~~~

在低斜视时, 距离等式近似为时间的抛物线方程式, 抛物线模型相当于时域中的线性调频信号, 变换到频域后的信号也具有线性调频形式 :cite:`LanG.CummingFrankH.Wong.2012`. 在大斜视角时, 距离等式应该采用更为精确的双曲线模型, 此时时频间呈非线性关系, 用于距离徙动补偿和方位匹配滤波器的距离应采用新的距离方程, 大斜视引入较强的距离和方位耦合(散焦),  :cite:`LanG.CummingFrankH.Wong.2012` 可以通过二次距离压缩来校正.


.. hint::
   下述中, 将徙动因子 :math:`D(f_\eta, V_r)` 展开并忽略 :math:`f_\eta` 二阶及以上项, 则退化为低斜视角下的表达式.


二次距离压缩
^^^^^^^^^^^^^^^^^^


在含有交叉耦合的信号的距离多普勒域信号中的调频率由 :math:`K_r` 变为了 :math:`K_m` :cite:`LanG.CummingFrankH.Wong.2012` p170. 其中,

.. math::
   K_m = \frac{K_r}{1-K_r/K_{src}}

二次压缩滤波器中的调频率为

.. math::
   K_{src}(R_0, f_{\eta}) = \frac{2V_r^2f_0^3D^3(f_\eta, V_r)}{cR_0f_\eta^2}.
   :label: equ-Ksrc


首先使用调频率为 :math:`K_r` 的滤波器进行匹配滤波实现初级压缩, 再使用调频率为 :math:`K_{src}` 的滤波器进行次级的匹配滤波实现二次压缩, 因而叫二次距离压缩. 二次距离压缩的滤波器为

.. math::
    H_{src}(f_{\tau}) = {\rm exp}\left\{-j\pi\frac{f_{\tau}^2}{K_{src}(R_0, f_{\eta})} \right\}
    :label: equ-SecondMatchedFilterRange

该滤波器与距离 :math:`R_0` 和方位向频率 :math:`f_\eta` 有关. 在距离频域中, SRC滤波器可以并入距离压缩滤波器中, 合并的滤波器为

.. math::
   \begin{aligned}
   H_{m}\left(f_{\tau}\right) &=\exp \left\{j \pi \frac{f_{\tau}^{2}}{K_{r}}\right\} \exp \left\{-j \pi \frac{f_{\tau}^{2}}{K_{src}\left(R_{0}, f_{\eta}\right)}\right\} \\ &=\exp \left\{j \pi f_{\tau}^{2}\left(\frac{1}{K_{r}}-\frac{1}{K_{src}\left(R_{0}, f_{\eta}\right)}\right)\right\} \\ &=\exp \left\{j \pi \frac{f_{\tau}^{2}}{K_{m}\left(R_{0}, f_{\eta}\right)}\right\}
   \end{aligned}


.. hint:: 二次距离压缩的实现方式

   二次距离压缩的实现方式有三种:

   1. 方式一: 在距离多普勒域中, 随RCMC插值一同进行
   2. 方式二: 通过二维频域中的相位相乘实现
   3. 方式三: 在距离频率 - 方位时域中进行



多普勒相位补偿
^^^^^^^^^^^^^^^^^

对于斜视SAR, 还需要做多普勒相位补偿 (Doppler Phase Compensation, DPC), 补偿滤波器为

.. math::
   H(f_{\eta}) = {\rm exp}\left\{1j 2 π f_{\eta} Y_c / V_s\right\}

其中, :math:`f_{\eta}` 为方位向频率, :math:`Y_c` 为场景中心在方位向坐标轴上的投影, :math:`V_s` 为SAR平台速度.



距离徙动的改进
^^^^^^^^^^^^^^^^^^


RDA算法的距离徙动补偿在距离多普勒域执行, 徙动因子如式 : :eq:`equ-RCMC_factor_RD` 所示. 在大斜视时, 在距离多普勒域的距离徙动量调整为

.. math::
   \Delta R(f_\eta) = R_{rd}(f_\eta) -R_0 = R_0\left[\frac{1-D(f_\eta, V_r)}{D(f_\eta, V_r)}\right].


方位匹配滤波器的改进
^^^^^^^^^^^^^^^^^^


对 :eq:`equ-MatchedFilterAzimuth` 所示方位匹配滤波器调整为

.. math::
   H_a(f_\eta) = {\rm exp}\left\{j\frac{4\pi R_0 D(f_\eta, V_r)f_0}{c}\right\}
   :label: equ-MatchedFilterAzimuthAdv



实验与分析
--------------

仿真数据实验
~~~~~~~~~~~~~~~

实验说明
^^^^^^^^^^^

实验参数及代码参见 :ref:`SectionBasicExperimentsExperimentsSARRadar` 小节, 设置斜视角 :math:`\theta_s = 8.5^°`.



实验结果
^^^^^^^^^^^

.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_4POINTS_RDSRCF2D.*
   :scale: 90 %
   :alt: 时域, 距离多普勒域及二维频域幅度相位谱
   :align: center

   时域, 距离多普勒域及二维频域幅度相位谱

   时域, 距离多普勒域及二维频域幅度相位谱.


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_4POINTS_RC.*
   :scale: 90 %
   :alt: 距离压缩后结果
   :align: center

   距离压缩后结果

   距离压缩后结果



.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_4POINTS_SRC.*
   :scale: 90 %
   :alt: 二次距离压缩后结果
   :align: center

   二次距离压缩后结果

   二次距离压缩后结果


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_4POINTS_DPC.*
   :scale: 90 %
   :alt: 多普勒相位补偿结果
   :align: center

   多普勒相位补偿结果

   多普勒相位补偿结果



.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_4POINTS_RCMC32.*
   :scale: 90 %
   :alt: 距离徙动校正结果
   :align: center

   距离徙动校正结果

   距离徙动校正结果



.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_4POINTS_AC.*
   :scale: 90 %
   :alt: 方位向压缩结果
   :align: center

   方位向压缩结果

   方位向压缩结果



.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_4POINTS_noRCMC_RDAo.*
   :scale: 90 %
   :alt: RDA算法最终成像结果
   :align: center

   RDA算法最终成像结果 (不含距离徙动校正)

   RDA算法最终成像结果 (不含距离徙动校正)


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_4POINTS_RCMC_RDAo.*
   :scale: 90 %
   :alt: RDA算法最终成像结果
   :align: center

   RDA算法最终成像结果 (含距离徙动校正)

   RDA算法最终成像结果 (含距离徙动校正)


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


RDA 成像结果 (以下结果均含多普勒相位补偿操作)


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_StanleyPark_noSRC_noRCMC.*
    :scale: 90 %
    :alt: Imaging result of RDA (without SRC, without RCMC)
    :align: center

    Imaging result of RDA (without SRC, without RCMC)

    Imaging result of RDA (without SRC, without RCMC)


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_StanleyPark_SRC_noRCMC.*
    :scale: 90 %
    :alt: Imaging result of RDA (with SRC, without RCMC)
    :align: center

    Imaging result of RDA (with SRC, without RCMC)

    Imaging result of RDA (with SRC, without RCMC)


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_StanleyPark_noSRC_RCMC32.*
    :scale: 90 %
    :alt: Imaging result of RDA (without SRC, with RCMC(sinc 32))
    :align: center

    Imaging result of RDA (without SRC, with RCMC(sinc 32))

    Imaging result of RDA (without SRC, with RCMC(sinc 32))


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/RDA/RDA_StanleyPark_SRC_RCMC32.*
    :scale: 90 %
    :alt: Imaging result of RDA (with SRC, with RCMC(sinc 32))
    :align: center

    Imaging result of RDA (with SRC, with RCMC(sinc 32))

    Imaging result of RDA (with SRC, with RCMC(sinc 32))

