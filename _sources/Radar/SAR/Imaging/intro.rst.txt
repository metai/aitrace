.. _Section-IntroductionImagingSARRadar:

SAR成像简介
=====================


.. note::
   目前压缩感知重构算法分为两大类:


   1. 贪婪算法: 通过迭代选择合适的原子使得重构误差最小， 包括匹配追踪, 正交匹配追踪, 补空间匹配追踪等

   2. 凸优化: 通过放宽正则约束 (如 :math:`\ell_0` --> :math:`\ell_1, \ell_2` ) 转化为凸优化问题, 包括梯度投影法, 基追踪, 最小角回归

   凸优化方法比贪婪算法所求解更为精确, 但计算复杂度高.


.. hint::

   压缩感知与正则化成像:

   1. 压缩感知强调压缩观测, 在信号不稀疏时先进行稀疏表示, 再求解
   2. 正则化方法强调通过加入先验, 使得问题有极小范数解
   3. 优化方法可以一致

不同成像方法结果对比
--------------------

- 仿真场景大小: :math:`32\times 32`
-
- 回波矩阵大小: :math:`32\times 32`

- 数据生成

   + 通过模拟SAR成像过程生成SAR原始数据 :math:`\bf s`
   + 通过 :math:`{\bf s} = {\bf A}{\bf g}` 生成SAR原始数据 :math:`\bf s`

- 成像方法

   + 广义逆: :math:`\hat{\bf g} = {\bf A}^{+}{\bf s}`
   + 共轭转置: :math:`\hat{\bf g} = {\bf A}^H{\bf s}`
   + 距离多普勒方法: 匹配滤波, 距离徙动校正等.


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/Introduction/LotusOrignalAmplitudePhase.png
   :scale: 100 %
   :alt: Lotus
   :align: center

   原始彩色荷花图(左)与仿真得到的SAR原始数据幅度(中)与相位(右).


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/Introduction/lotusImaging.png
   :scale: 100 %
   :alt: Lotus Imaging
   :align: center

   不同方法成像结果




