.. _Section-SiameseSRDeepLerningImagingSARRadar:

学习式压缩感知成像
=======================

动机与贡献
--------------------------



SAR数据特性
~~~~~~~~~~~~~~~


由 :ref:`Section-SARSignalSystemOverviewSARRadar` 小节可知, 雷达接收采样后的IQ双通道原始信号可以表示为

.. math::
   \begin{aligned}
   s_{I}(\eta, \tau) &= r(\eta, \tau) {\rm cos}[ \phi(\eta, \tau)]\\
   s_{Q}(\eta, \tau) &= r(\eta, \tau) {\rm sin}[ \phi(\eta, \tau)]\\
   s(\eta, \tau) &= r(\eta, \tau) {\rm exp}{[j \phi(\eta, \tau)]} \\
   &= s_{I}(\eta, \tau) + s_{Q}(\eta, \tau)\\
   \end{aligned},
   :label: equ-SAR_Receive_Signal_IQ


其中, 相位 :math:`\phi(\eta, \tau)` 为

.. math::
   \phi(\eta, \tau) = - \frac{4\pi f_c R(\eta)}{c} + \pi K_r \left(\tau-\frac{2R(\eta)}{c}\right)^2,

地面反射率与天线增益合成项 :math:`r(\eta, \tau)` 为

.. math::
   r(\eta, \tau) = g(\eta, \tau) w_a(\eta-\eta_c) w_r\left(\tau-2R(\eta)/c\right).

由 :eq:`equ-SAR_Receive_Signal_IQ` 知



