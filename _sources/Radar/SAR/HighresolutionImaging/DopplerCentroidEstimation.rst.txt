.. _Section-DopplerCentroidEstimationHighresolutionImagingSARRadar:

多普勒中心估计
=====================


引言
---------------

多普勒中心频率简称多普勒中心, 用于估计多普勒中心频率的算法通常称为多普勒中心估计器(Doppler Centroid Estimator, DCE).

- 是什么
- 为什么
- 怎么做


多普勒中心频率组成
~~~~~~~~~~~~~~~~


.. math::
   f_{\eta_c} = f_{\eta_c}^{\prime} + M_a F_{sa}
   :label: equ-DopplerCentroidFrequencyAzimuth


其中, :math:`f_{\eta_c}` 为方位向绝对多普勒中心频率, :math:`f_{\eta_c}^{\prime}\in {-F_{sa}/2, F_{sa}/2}` 为方位向基带多普勒中心频率, 也称为 :math:`f_{\eta_c}` 的小数部分, :math:`M_a\in {\mathbb Z}^+` 为多普勒模糊数, :math:`F_{sa}` 为方位向采样率, :math:`M_aF_{sa}` 称为 :math:`f_{\eta_c}` 的整数部分. 多普勒中心频率估计通常是估计小数部分频率, 多普勒中心频率估计算法通常称为多普勒中心估计器(Doppler Centroid Estimator, DCE), 估计后的频率通常称为精细(fine)多普勒中心频率; 多普勒模糊数估计算法通常称为多普勒模糊求解器(Doppler Ambiguity Resolver, DAR), 多普勒中心与多普勒模糊数的估计通常是不独立的.

多普勒中心不仅受方位向的运动影响, 也会随着距离向距离的改变而改变, 所以同时需要估计不同距离单元的多普勒中心, 并用多项式函数拟合的方法来得到准确的估计 :cite:`ASARHandbook2007`.



传统估计方法
----------------


怎么做
---------------

`````````````





