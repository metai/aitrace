.. _Section-SAREmittedSignalSystemOverviewSARRadar:

SAR发射信号及其性质
=====================


SAR发射信号
-----------------


如文献 :cite:`Cumming2005Digital` 中所述, 在距离向, 雷达发射的调频脉冲通常为:

.. math::
   s_t(\tau) = w_r(\tau){\rm cos}\left(2\pi \sum_{n=0}^{N}P_n{\tau^n}\right)
   :label: equ-RadarEmittedSignalRange

其中, :math:`\tau` 距离向脉冲时间, :math:`P_n` 为幂级数形式下的相位的系数, :math:`w_r(\tau)` 为脉冲包络, 通常为矩形脉冲包络 :math:`w_r(\tau)={\rm rect}(\tau/T_p)`, :math:`T_p` 为脉冲宽度. 在雷达中, 最长用的脉冲为线性调频脉冲

.. math::
   \begin{aligned}
   s_t(\tau) &= w_r(\tau){\rm cos}\left(2\pi F_c \tau + \pi K_r \tau^2 \right) \\
             &= w_r(\tau){\rm cos}\left[2\pi \left(F_c \tau + \frac{K_r}{2} \tau^2 \right)\right]
   \end{aligned}
   :label: equ-RadarEmittedSignalRangeRealLFM

其中, :math:`f_c` 为载频, :math:`K_r` 为距离向调频率, :math:`\tau` 为距离向脉冲时间, 通常取脉冲中心为参考原点. 对比 :eq:`equ-RadarEmittedSignalRange` 可知, 此种形式下的系数 :math:`P_0=0`, :math:`P_1=F_c`, :math:`P_2=K_r/2`, :math:`P_n=0, n>2`.

通常雷达系统发射两路信号, 一路是与 :eq:`equ-RadarEmittedSignalRange` 所表示信号相位同相的 I (in-phase) 路信号, 另一路是与 :eq:`equ-RadarEmittedSignalRange` 所表示信号相位正交的 Q (quadrature) 路信号, 这两路信号构成一个复指数信号, 通常取 I为实部, Q为虚部．因而,　实际雷达系统发射的具有 :eq:`equ-RadarEmittedSignalRangeRealLFM` 所示线性调频特性的复指数信号可以表示为

.. math::
   \begin{aligned}
   s_t(\tau) &= w_r(\tau){\rm exp}\left(j2\pi F_c \tau + j\pi K_r \tau^2 \right) \\
             &= w_r(\tau){\rm exp}\left[j2\pi \left(F_c \tau + \frac{K_r}{2} \tau^2 \right)\right]
   \end{aligned}
   :label: equ-RadarEmittedSignalRangeＣomplexＥxponentialLFM


为什么采用复指数信号
-----------------

