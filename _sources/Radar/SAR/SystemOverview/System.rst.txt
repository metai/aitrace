.. _Section-SystemSystemOverviewSARRadar:

SAR系统组成
=====================


硬件系统
-----------------



脉冲时序与采样
------------------

如 :figure:numref:`fig-BeamAngleRangeGeometry` 与 :figure:numref:`fig-TimeSequenceOfRadarTransmittingAndReceivingPulse` 所示, 设雷达于 :math:`t_k` 时刻发射第 :math:`k` 个脉冲波束, 脉冲宽度为 :math:`T_p`. 设经过 :math:`t_{near}` 时间, 发射脉冲前边缘于 :math:`t_{A_k}=t_k+t_{near}` 时刻到达近地点 :math:`A`; 经过 :math:`t_{far}` 时间, 发射脉冲前边缘于 :math:`t_{B_k}=t_k+t_{far}` 时刻到达远地点 :math:`B`, 前边缘到达远地点的脉冲又经过 :math:`t_{far}+T_p` 时间, 其后边缘到达雷达. 雷达接收机在稍早于 :math:`2t_{A_k}` 的时刻 :math:`2t_{A_k} - \delta_{A_k}` 开始采样, 并于稍晚于 :math:`2t_{B_k}+T_p` 的时刻 :math:`2t_{B_k} + T_p + \delta_{B_k}` 结束采样, 则采样时间为 :math:`T_{r} = (2t_{B_k} + T_p + \delta_{B_k}) - (2t_{A_k} - \delta_{A_k})`. 其中, :math:`\delta_{A_k} > 0, \delta_{B_k} > 0`, :math:`(k=0, 1, \cdots, N_a)` 为很小的正数, 故采样时间

.. math::
   T_{r} \approx 2t_{far} + T_p - 2t_{near}.
   :label: equ-RangeSamplingTime

.. _fig-TimeSequenceOfRadarTransmittingAndReceivingPulse:

.. figure:: ../../../_static/figs/Radar/SAR/SystemOverview/TimeSequenceOfRadarTransmittingAndReceivingPulse.*
   :alt: Time sequence of SAR transmitting and receiving pulse.
   :align: center

   Time sequence of SAR transmitting and receiving pulse.

如 :figure:numref:`fig-TimeSequenceOfRadarTransmittingAndReceivingPulse` 所示, 第 :math:`k+1` 个脉冲必须在第 :math:`k` 个脉冲到达雷达后才可以发射, 因而有

.. math::
   t_{k+1}+2 t_{n e a r}>t_{k}+2 t_{f a r}+T_{p},


从而有

.. math::
   T_{a s}=\frac{1}{F_{a s}}>2 t_{f a r}-2 t_{n e a r}+T_{p}=T_{r},
   :label: equ-AzimuthSamplingPeriodAndDistanceSamplingTime

其中, :math:`F_{as}` 为方位向采样频率, :math:`T_{as}` 为方位向采样周期, :math:`T_{r}` 为距离向采样时间.


几何建模
-----------------

关键参数计算
~~~~~~~~~~~~~~~~~~


卫星速度与波束掠过地面的速度
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如 :figure:numref:`fig-SatelliteVelocityAndBeamVelocityOnTheground` 所示, 地球半径为 :math:`R_e`, 卫星在距离地面高度为 :math:`H` 的高空以速度 :math:`V_s` 围绕地球运动, 下视角为 :math:`\theta_d`, 波束掠过地面的速度为 :math:`V_g`. 由 :figure:numref:`fig-SatelliteVelocityAndBeamVelocityOnTheground` 中几何关系知 :math:`x + AB{\tan}\theta_d = R_e + H`, 即

.. math::
   x + {\sqrt{R_e^2-x^2}\ {\tan}\theta_d} = R_e + H

化简后得

.. math::
   (1+{\tan}^2\theta_d)x^2 - 2(R_e+H)x + (R_e+H)^2 - R_e^2{\tan}^2\theta_d = 0
   :label: equ-DistanceSatelliteVelocityAndBeamVelocityOnTheground

:eq:`equ-DistanceSatelliteVelocityAndBeamVelocityOnTheground` 的解为

.. math::
   x = \frac{(R_e+H) \pm {\tan \theta_d}\sqrt{R_e^2{\tan}^2\theta_d - 2HR_e-H^2}}{1+{\tan}^2\theta_d},
   :label: equ-DistanceSatelliteVelocityAndBeamVelocityOnThegroundSolution

:eq:`equ-DistanceSatelliteVelocityAndBeamVelocityOnThegroundSolution` 中, 当 :math:`0 < \theta_d < \pi/2` 时, 分子取加号; 当 :math:`π/2 < \theta_d < \pi` 时, 分子取减号.

.. _fig-SatelliteVelocityAndBeamVelocityOnTheground:

.. figure:: ../../../_static/figs/Radar/SAR/SystemOverview/SatelliteVelocityAndBeamVelocityOnTheground.*
   :alt: Satellite velocity and beam skimming velocity
   :align: center

   Satellite velocity and beam skimming velocity



距离向波束宽度计算
^^^^^^^^^^^^^^^^^^

根据采样点数 :math:`N_r`, 采样率 :math:`F_{rs}`, 平台高度 :math:`H` 以及下视角 :math:`\theta_d`, 可以计算距离向波束宽度 (antenna elevation beamwidth) :math:`\beta_e`. 如 :figure:numref:`fig-BeamAngleRangeGeometry` 所示, 由 :figure:numref:`fig-BeamAngleRangeGeometry` 中几何关系及 :eq:`equ-RangeSamplingTime` 得


.. math::
   \begin{aligned}
   T_{r}-T_p &= \frac{N_{r} - N_p}{F_{rs}} \\
          &\approx 2t_{far} - 2t_{near} \\
          &=\frac{2PB}{c} - \frac{2PA}{c} \\
          &= \frac{2H}{c\cdot{\rm sin}(\theta_d-\beta_e/2)} - \frac{2H}{c\cdot{\rm sin}(\theta_d+\beta_e/2)}
   \end{aligned}
   :label: equ-SamplingTimeBeamAngleRange

其中, :math:`c` 为光速, :math:`N_r` 为距离向采样点数, :math:`N_p` 为 :math:`T_p` 时间内的距离向采样点数. :eq:`equ-SamplingTimeBeamAngleRange` 代入积化和差 :math:`\sin \alpha \sin \beta=\frac{1}{2}[\cos (\alpha-\beta) - \cos (\alpha+\beta)]` 与和差化积公式 :math:`\sin \alpha-\sin \beta=2 \cos \frac{\alpha+\beta}{2} \sin \frac{\alpha-\beta}{2}`, :eq:`equ-SamplingTimeBeamAngleRange` 化简后得到

.. math::
   a\cdot{\sin}^2{\frac{\beta_e}{2}} + 4H{\cos}\theta_d {\sin}{\frac{\beta_e}{2}} + \frac{a}{2}({\cos}2\theta_d - 1) = 0

即

.. math::
   \left({\sin}{\frac{\beta_e}{2}} + \frac{2H{\cos}\theta_d}{a}\right)^2 = a\cdot{\sin}^2{\theta_d} + \frac{4H^2{\cos}^2{\theta_d}}{a}

从而解得

.. math::
   {\sin}{\frac{\beta_e}{2}} = -\frac{2H{\cos}\theta_d}{a} ±\sqrt{{\sin}^2\theta_d + \frac{4H^2{\cos}^2\theta_d}{a^2}},

其中, :math:`a = \frac{c(N_{r}-N_p)}{F_{rs}}`, :math:`c` 为光速. 由于 :math:`{\sin}\frac{\beta_e}{2}\in[-1, 1]`, 可以排除一个解.


.. _fig-BeamAngleRangeGeometry:

.. figure:: ../../../_static/figs/Radar/SAR/SystemOverview/BeamAngleRangeGeometry.*
   :alt: Beam width and footprint in range direction
   :align: center

   Beam width and footprint geometry in range direction






