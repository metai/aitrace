.. _Section-CorrelationLinearOperatorFunctionalAnalysisBasicMath:

相关算子
=====================

互相关
-----------------


**互相关** ( :term:`Cross Correlation` ) 在不同领域有稍微不同的定义.

在数字信号处理中, 互相关两个序列相似性的度量, 是一个序列相对于另一序列的位移函数. 通常被称为滑动点积或滑动内积, 且用于搜索较长信号的较短的已知特征, 在模式识别, 单粒子分析, 电子断层扫描, 密码分析和神经生理学中有广泛应用. 互相关与卷积本质上相似, 自相关是信号自己的互相关.




确定信号的互相关
~~~~~~~~~~~~~~~~~

对于连续函数 :math:`f, g` , 互相关定义为

.. math::
    (f\star g)(\tau) = \int_{-\infty}^{+\infty}\overline{f(t)}g(t+\tau){\rm d}t = \int_{-\infty}^{+\infty}\overline{f(t-\tau)}g(t){\rm d}t
    :label: equ-CrossCorrelationContinues


其中, :math:`\overline{f}` 表示 :math:`f` 的共轭转置, :math:`\tau` 表示移位.


类似的, 对于离散函数 :math:`f, g` , 互相关定义为


.. math::
    (f\star g)[n] = \sum_{m=-\infty}^{+\infty}{\overline{f[m]}g[m+n]} = \sum_{m=-\infty}^{+\infty}\overline{f[m-n]}g[m]
    :label: equ-1DCrossCorrelationDiscrete



不确定信号的互相关
~~~~~~~~~~~~~~~~~

参见章节 :ref:`Chapter-CorrelationAnalysis` 的 :ref:`Section-CorrelationCorrelationAnalysisProbabilityStatistics` 小节.


周期信号的互相关
~~~~~~~~~~~~~~~~~



自相关
-------------------
