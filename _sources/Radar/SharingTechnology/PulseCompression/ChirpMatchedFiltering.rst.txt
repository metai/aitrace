.. _Section-ChirpMatchedFilteringPulseCompressionSharingTechnologyRadar:

匹配滤波与脉冲压缩
=====================

匹配滤波概念回顾
---------------

有关匹配滤波的概念参见 :ref:`Section-MatchedFilterFilterStatisticalSignalProcessing` 小节.



时域匹配滤波
-----------------------

记 :math:`s_t(t), s_r(t)` 分别为雷达发射和接收的信号, :math:`g(t)` 为发射信号的复制信号, :math:`h(t)` 为匹配滤波器, 则匹配滤波的过程可以表示为

.. math::
   s_{pc}(t) = \int_{-\infty}^{+\infty} s_r(\tau)h(t) {\rm d}\tau
   :label: equ-MatchedFilteringInTimeDomain



若采用相关实现匹配滤波, 则时域相关匹配滤波器为复制信号 :math:`g(t)`, 即 :math:`h(t)=g(t)`, 从而有

.. math::
   \begin{aligned}
   s_{pc}(t) &= \int_{-\infty}^{+\infty} s_r(\tau)\overline{h(\tau-t)} {\rm d}\tau \\
             &= \int_{-\infty}^{+\infty} s_r(\tau)\overline{g(\tau-t)} {\rm d}\tau \\
   \end{aligned}
   :label: equ-MatchedFilteringInTimeDomainCorr



若采用卷积实现匹配滤波, 则时域卷积匹配滤波器为复制信号 :math:`g(t)` 时间反褶后的复共轭, 即 :math:`h(t)=\overline{g(-t)}`, 从而有

.. math::
   \begin{aligned}
   s_{pc}(t) &= \int_{-\infty}^{+\infty} s_r(\tau)h(t-\tau) {\rm d}\tau \\
             &= \int_{-\infty}^{+\infty} s_r(\tau)\overline{g(\tau-t)} {\rm d}\tau \\
   \end{aligned}
   :label: equ-MatchedFilteringInTimeDomainConv


由 :eq:`equ-MatchedFilteringInTimeDomainCorr` 和 :eq:`equ-MatchedFilteringInTimeDomainConv` 知无论采用相关还是卷积滤波器, 滤波结果是一样的.

对于 :eq:`equ-RecievedSignal` 所示的接收信号, 其发射信号如 :eq:`equ-TransmittedSignal` 所示, 则匹配滤波的输出为

.. math::
   \begin{aligned}
   s_{pc}(t) &= \int_{-\infty}^{+\infty} s_r(\tau)\overline{g(\tau-t)} {\rm d}\tau \\
             &= \int_{-\infty}^{+\infty} {\rm rect}\left(\frac{\tau-t_0}{T}\right){\rm exp}\{j\phi(\tau-t_0)\}\overline{{\rm rect}\left(\frac{\tau-t}{T}\right){\rm exp}\{j\phi(\tau-t)\}} {\rm d}\tau \\
   \end{aligned}
   :label: equ-MatchedFilteringInTimeDomainConv



基带信号
~~~~~~~~~~~~~~~~~~


非基带信号
~~~~~~~~~~~~~~~~~~



频域匹配滤波
-----------------------




基带信号
~~~~~~~~~~~~~~~~~~


非基带信号
~~~~~~~~~~~~~~~~~~



实验与分析
-----------------




