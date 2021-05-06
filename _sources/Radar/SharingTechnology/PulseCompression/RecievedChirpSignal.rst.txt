.. _Section-RecievedChirpSignalPulseCompressionSharingTechnologyRadar:

接收信号
=====================


接收信号
-----------------

假设发射的调频信号为

.. math::
   s_t(t)={\rm rect}\left(\frac{t}{T}\right){\rm exp}\{j\phi(t)\},
   :label: equ-TransmittedSignal

该信号经 :math:`t_0` 时间到达距离它 :math:`R_0` 处的目标并返回, 则接收信号为

.. math::
   s_r(t) = {\rm rect}\left(\frac{t-t_0}{T}\right){\rm exp}\{j\phi(t-t_0)\},
   :label: equ-RecievedSignal

其中, :math:`t_0=2R_0/C`, :math:`C` 为光速.



接收线性调频信号的频谱
----------------------

本部分考虑线性调频的情况, 即发射信号 :math:`s_t(t)` 的调制频率线性变化, 记调频率为 :math:`K`, 载频为 :math:`F_c`, 则接收到的信号为

.. math::
   s_r(t) = {\rm rect}\left(\frac{t-t_0}{T}\right){\rm exp}\left\{j\left[\phi_0 + 2\pi F_c (t-t_0) + \pi K(t-t_0)^2\right]\right\},
   :label: equ-RecievedChirpSignalWithCarrierFrequency

被积相位 :math:`\phi(t-t_0)-2\pi ft=\phi_0 + 2\pi F_c (t-t_0) + \pi K(t-t_0)^2 -2\pi ft` 对于时间的一阶导数为 :math:`\phi'(t-t_0)=2\pi F_c + 2\pi K(t-t_0) -2\pi f`, 二阶导数为 :math:`\phi''(t-t_0)=2\pi K`, 利用PoSP原理, 可以求得接收信号的频谱为

.. math::
   {\mathcal S}_r(t) = \sqrt{\frac{1}{|K|}}{\rm rect}\left(\frac{f-F_c}{KT}\right){\rm exp}\left\{-j\pi \frac{(f-F_c)^2}{K}\right\}{\rm exp}\left\{-j2\pi ft_0\right\},
   :label: equ-SpectrumOfRecievedChirpSignalWithCarrierFrequency

:eq:`equ-SpectrumOfRecievedChirpSignalWithCarrierFrequency` 中忽略了 :math:`\pi/4` 项.

