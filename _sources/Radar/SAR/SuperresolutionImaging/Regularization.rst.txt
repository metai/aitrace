.. _Section-RegularizationSuperresolutionImagingSARRadar:

正则化超分辨成像方法
=====================

参见 :ref:`Section-RegularizationImagingSARRadar` 小节


实验与分析
------------------------


实验说明
~~~~~~~~~~~~

- 仿真场景大小: :math:`128\times 128`
- 回波矩阵大小: :math:`32\times 32`
- 稀疏表示字典: 无, ``DCT`` ,  ``DWT``
- 优化方法: ``Lasso`` , ``OMP``


仿真点目标场景图及仿真生成点SAR原始数据幅度与相位图如下:

.. figure:: ../../../_static/figs/Radar/SAR/pub/pointsAmpPhase.png
   :scale: 80 %
   :alt: 仿真点目标场景图, 仿真SAR原始数据幅度相位图
   :align: center

   仿真点目标场景图, 仿真SAR原始数据幅度相位图


仿真船只场景图及仿真生成点SAR原始数据幅度与相位图如下:

.. figure:: ../../../_static/figs/Radar/SAR/pub/shipAmpPhase.png
   :scale: 80 %
   :alt: 仿真船只场景图及仿真生成点SAR原始数据幅度与相位图如下
   :align: center

   仿真船只场景图及仿真生成点SAR原始数据幅度与相位图如下

仿真荷花场景图及仿真生成点SAR原始数据幅度与相位图如下:

.. figure:: ../../../_static/figs/Radar/SAR/pub/lotusAmpPhase.png
   :scale: 80 %
   :alt: 仿真荷花场景图及仿真生成点SAR原始数据幅度与相位图如下
   :align: center

   仿真荷花场景图及仿真生成点SAR原始数据幅度与相位图如下


实验代码
~~~~~~~~~~~~~

`iprs2.0 <https://github.com/antsfamily/iprs2.0>`_  ``demo_regular_sar.py``



实验结果
~~~~~~~~~~~~~


.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/Regularization/RegularizationL1L2_RDA_Points128.png
   :scale: 100 %
   :alt: Imaging result of :math:`\ell_1, \ell_2` regularization and RDA.
   :align: center

   Imaging result of :math:`\ell_1, \ell_2` regularization and RDA. :math:`\lambda=0.001` , max iter 1000


.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/Regularization/RegularizationL1L2_RDA_Lotus128.png
   :scale: 100 %
   :alt: Imaging result of :math:`\ell_1, \ell_2` regularization and RDA.
   :align: center

   Imaging result of :math:`\ell_1, \ell_2` regularization and RDA. :math:`\lambda=0.001` , max iter 1000


.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/Regularization/RegularizationL1L2_RDA_Ship128.png
   :scale: 100 %
   :alt: Imaging result of :math:`\ell_1, \ell_2` regularization and RDA.
   :align: center

   Imaging result of :math:`\ell_1, \ell_2` regularization and RDA. :math:`\lambda=0.001` , max iter 1000


- 运行时间: 平均约100s
- 重构误差: