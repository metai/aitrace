.. _Section-ConceptSystemOverviewSARRadar:

相关概念汇总
=====================

SAR分类
-----------------


.. fancybox:: ../../../_static/figs/Radar/SAR/SystemOverview/KindsOfSAR.*


.. figure:: ../../../_static/figs/Radar/SAR/SystemOverview/KindsOfSAR.*
   :scale: 50 %
   :alt: SAR 分类
   :align: center

    SAR 分类

    SAR 分类


`Synthetic-aperture radar <http://en.volupedia.org/wiki/Synthetic-aperture_radar>`_


SAR成像几何关系
---------------------

.. figure:: ../../../_static/figs/Radar/SAR/SystemOverview/SAR_geometry.*
   :scale: 50 %
   :alt: SAR成像几何关系
   :align: center

    SAR 成像几何关系

    SAR 成像几何关系


.. warning::
   注意上图中的斜视角定义为波束中心线方向与 :math:`x-O-z` 平面间的夹角. 如下图所示几何关系知 :math:`\theta_h` 与 :math:`\theta_0` 满足如下关系

   .. math::
      {\rm tan}{\theta_h} = \frac{1}{\sqrt{\left(\frac{OP}{AB}\right)^2 + \frac{1}{{\rm tan}^2{\theta_0}}}}.

   .. image:: ../../../_static/figs/Radar/SAR/SystemOverview/SquintAngle.*


**如果雷达在距离向上不作扫描, 那么雷达成像区域范围与波束宽度有关, 所以超出波束覆盖范围的地方是没法成像的？**


.. hint::
    - 俯角 ( :term:`Depression Angle` ) : 如图中 :math:`\theta_d` ;
    - 斜视角 ( :term:`Squint Angle` ) : 如图中 :math:`\theta_s`, 即波束中心线与零多普勒线之间的夹角
    - 入射角 ( :term:`Incidence Angle` ) : 也叫视角 (look angle), 即波束照射方向与地平面的法线间的夹角, 如图中 :math:`\theta_i` ;
    - 掠地角 ( :term:`Grazing Angle` ) : 即波束照射方向与地平面间的夹角, 如图中 :math:`\theta_g` .
    - 轨道倾角 ( :term:`Orbital Inclination` ) : 某一轨道相对于另一参考平面的倾斜角度, 图中未标出.
    - 目标被波束中心照射一般是指波束中心线经过目标的时刻.


符号列表
------------------

- :math:`C` : 光速 ( `Light speed <http://en.volupedia.org/wiki/Speed_of_light>`_ );
- :math:`f_0` : 中心频率 ( `Center frequency <http://en.volupedia.org/wiki/Center_frequency>`_ );
- :math:`f_c` : 载波频率 ( `Carrier frequency <http://en.volupedia.org/wiki/Carrier_frequency>`_ ), 指载波的中心频率/频率;
- :math:`\lambda = \frac{C}{f_c}` : 波长 ( `Wavelength <http://en.volupedia.org/wiki/Wavelength>`_ );
- :math:`D` 或者 :math:`La` : 天线真实孔径长度;
- :math:`L_s` : 合成孔径长度 (Synthetic aperture length);
- :math:`T_s` : 合成孔径时间 (Synthetic aperture time);
- :math:`R` : 雷达与目标间的垂直距离/瞬时斜距;
- :math:`\alpha = \lambda / D` : 天线波束宽度(Antenna beam width);
- :math:`H` : 平台高度;
- :math:`V` : 平台运动速度;
- :math:`T_p` : 脉冲宽度 (pulse width);
- :math:`B` : 带宽 (band width);
- :math:`K_r` : 线性调频率 (`Linear chirp rate <http://en.volupedia.org/wiki/Chirp#Rate>`_) , :math:`K_r = B/T_p` ;


合成孔径与真实孔径: :math:`L_s = {\lambda \over D} \cdot R`

合成孔径时间与合成孔径长度: :math:`L_s = V T_s`


实孔径距离向分辨率: :math:`{\rho}_r = \frac{C}{2K_rT_p} = \frac{C}{2B}`

实孔径方位向分辨率: :math:`{\rho}_a = {\alpha} \cdot R = \frac{\lambda \cdot R }{D}`

合成孔径方位向分辨率: :math:`{\rho}_a = {\alpha_h} \cdot R= {\frac{\lambda}{2L_s}} \cdot R = \frac{D}{2}`

因为合成孔径雷达发射和接收共用一副天线且信号的距离差是双程差, 进一步锐化了波束, 所以合成孔径雷达的有效半功率波束宽度近似为相同长度实孔径的一半, 它的半功率波束宽度为: :math:`\alpha_h = \frac{\lambda}{2L_s}`



SAR利用脉冲压缩技术获得高的距离向分辨率, 利用合成孔径原理获得高的方位向分辨率, 从而获得高分辨率雷达图像.

SAR回波信号经距离向脉冲压缩后, 雷达的距离分辨率由雷达发射信号带宽决定: :math:`\rho_{r}=\frac{C}{2B_{r}}` , 式中 :math:`\rho_{r}` 表示雷达的距离分辨率, :math:`B_{r}` 表示雷达发射信号带宽, :math:`C` 表示光速.

同样, SAR回波信号经方位向合成孔径后, 雷达的方位分辨率由雷达方位向的多谱勒带宽决定: :math:`\rho_{a}=\frac{v_{a}}{B_{a}}` , 式中 :math:`\rho_{a}` 表示雷达的方位分辨率, :math:`B_{a}` 表示雷达方位向多谱勒带宽, :math:`v_{a}` 表示方位向SAR平台速度. 在小斜视角的情况下, 方位分辨率近似表示为 :math:`\rho_{a}=\frac{D}{2}` , 其中 :math:`D` 是方位向合成孔径的长度.




SAR数据获取
------------------------

设 :math:`t=0` 时刻, 天线发射一脉宽为 :math:`T_p` 的脉冲, 于 :math:`t_1` 时刻脉冲起始边缘最先到达近距地面点, 于 :math:`t_2` 时间脉冲结束边缘到达远距地面点, :math:`t_1` 时刻到达地面的波束, 于 :math:`2t_1` 时刻返回到天线, :math:`t_2` 到达地面的波束于 :math:`2t_2` 时刻返回到天线. 接收机在稍早于 :math:`2t_1` 的时刻开始采样, 于稍晚于 :math:`2t_2` 时刻的时候停止采样. 由此, 雷达距离向的采样时间为 :math:`T_{sr} = 2t_2 - 2t_1`



.. figure:: ../../../_static/figs/Radar/SAR/SystemOverview/imaging.*
   :scale: 80 %
   :alt: 成像与原始数据存储
   :align: center

   成像与原始数据存储

   成像与原始数据存储


采样参数的选取
~~~~~~~~~~~~

记方位向采样频率即脉冲重复频率(PRF)为 :math:`F_{sa}`, 方位向采样时间为 :math:`T_{sa}`, 距离向采样频率为 :math:`F_{sr}`, 距离向采样时间为 :math:`T_{sr}`, 近地点脉冲起始到达时刻为 :math:`t_1`, 远地点脉冲起始远离时刻为 :math:`t_2`, 则需要满足以下准则 (参见文献 :cite:`LanG.CummingFrankH.Wong.2012` pp.90):


1. 奈奎斯特采样率: 即 :math:`F_{sa} > α_a B_a`, 过采样率因子一般需满足 :math:`\alpha_a \in [1.1, 1.4]`, 太低会引起方位模糊, 且 :math:`\alpha_a > \alpha_r`.
2. 距离测绘带宽度: 即 :math:`1/F_{sa} - T_p > T_{sr} = 2t_2-2t_1`, PRF需足够低, 以使得测绘带内的脉冲回波都可以被采集到, 若过大, 不同脉冲回波出现在同一接收窗内, 会产生距离模糊, 若距离模糊过大且PRF不能降低, 需要减小俯仰方向的波束宽度(减小了测绘带宽).
3. 接收窗起始时间: 在星载情况下, 某时刻发射的脉冲需要经过好几个脉冲间隔才能被接收, 这一被接收的时刻受PRF的影响.
4. 星下点回波: 来自星下点处的地面反射能量往往会比较大, 导致图像上出现亮条纹(镜像反射且每个距离单元覆盖较大的面积)距离模糊, 通过选择合适的PRF可以使得星下点回波不在接收窗内.

.. hint::
   在星载情况下需要考虑这些准则, 机载情况下一般可以忽略.

SAR成像模式
-------------------


.. figure:: ../../../_static/figs/Radar/SAR/SystemOverview/SAR_mode.png
   :scale: 80 %
   :alt: SAR成像模式
   :align: center

   SAR成像模式

   SAR成像模式


斑点噪声(Speckle)
---------------------

诸如SAR、声纳这样的相干成像系统经常遭受一种称为散斑的乘性噪声。当相干辐射照射的物体具有与成像波长相比粗糙的表面时，会出现散斑。它是由在每个分辨单元内的小反射器散射的相干回波的建设性和破坏性干涉引起的。斑点噪声严重影响后续目标辨识等性能, 通过在成像模型中引入正则可以减轻斑点噪声, 即对恢复图像施加正则, 常用的正则有, :math:`\ell_1`, :math:`\ell_{1/2}`, TV正则等等 :cite:`Patel2010Compressed` .

有关正则化技术参见 :ref:``


公式总结
--------------------

.. figure:: ../../../_static/figs/Radar/SAR/SystemOverview/equationSAR.png
   :scale: 80 %
   :alt: 合成孔径相关公式
   :align: center

   合成孔径相关公式

.. figure:: ../../../_static/figs/Radar/SAR/SystemOverview/equationSAR1.png
   :scale: 80 %
   :alt: 相关参数说明
   :align: center

   相关参数说明


术语解释
-------------------

Foot Print
~~~~~~~~~~~~~~~

雷达波束在地面上的脚印(footprint), 即指真实孔径照射的区域. 分距离向与方位向的两种脚印.

距离向的脚印(Along range footprint size)大小可由下式近似计算

.. math::
   R_{AR} \approx \frac{\lambda}{L_r}\frac{H}{{\rm cos}^2\theta_d}

方位向的脚印(Cross range footprint size)大小可由下式近似计算

.. math::
   R_{CR} \approx \frac{\lambda}{L_a}\frac{H}{{\rm cos}\theta_d}

其中, :math:`\lambda` 为雷达发射波长, :math:`L_r, L_a` 分别为天线距离向与方位向的天线孔径, :math:`H` 为平台高度, :math:`\theta_d` 为雷达下视角.



