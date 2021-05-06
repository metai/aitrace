.. _Section-IntroductionSuperresolutionImagingSARRadar:

SAR超分辨成像简介
=====================



不同成像方法结果对比
--------------------

- 仿真场景大小: :math:`128\times 128`

- 回波矩阵大小: :math:`32\times 32`

- 数据生成

   + 通过模拟SAR成像过程生成SAR原始数据 :math:`\bm s`
   + 通过 :math:`{\bm s} = {\bm A}{\bm g}` 生成SAR原始数据 :math:`\bm s`

- 成像方法

   + 广义逆: :math:`\hat{\bm g} = {\bm A}^{+}{\bm s}`
   + 共轭转置: :math:`\hat{\bm g} = {\bm A}^H{\bm s}`
   + 距离多普勒方法: 匹配滤波, 距离徙动校正等.


.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/Introduction/Lotus.png
   :scale: 80 %
   :alt: Lotus
   :align: center

   原始彩色荷花图(左)与仿真得到的SAR原始数据幅度(中)与相位(右).


.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/Introduction/INVA_AH_RDA_Lotus128.png
   :scale: 120 %
   :alt: Lotus Imaging
   :align: center

   不同方法成像结果



.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/Introduction/ship.png
   :scale: 80 %
   :alt: ship
   :align: center

   原始船只图(左)与仿真得到的SAR原始数据幅度(中)与相位(右).


.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/Introduction/INVA_AH_RDA_ship128.png
   :scale: 120 %
   :alt: ship Imaging
   :align: center

   不同方法成像结果




