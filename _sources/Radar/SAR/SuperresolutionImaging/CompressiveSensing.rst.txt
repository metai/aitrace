.. _Section-CompressiveSensingSuperresolutionImagingSARRadar:

压缩感知超分辨SAR成像
=====================

压缩感知超分辨SAR成像
-------------------------

在 :ref:`Section-CompressiveSensingImagingSARRadar` 小节已经介绍了压缩感知SAR成像原理.

压缩成像 :cite:`Patel2010Compressed` ,

:cite:`Baraniuk2007Compressive`







实验与分析
-------------------------



实验与分析
----------------------


仿真数据
~~~~~~~~~~~~~~

实验说明
^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^



实验结果
^^^^^^^^^^^^^^

**1. OMP优化, 不采用字典进行稀疏表示, 和采用DCT字典进行稀疏表示的结果如下:**

点目标结果


.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/CS/CSOMP_CSDCT_points128.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of points.
   :align: center

   Compressive Sensing based and RDA Imaging Results of points (OMP).


船只结果:

.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/CS/CSOMP_CSDCT_ship128.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of ship.
   :align: center

   Compressive Sensing based and RDA Imaging Results of ship (OMP).

荷花结果:

.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/CS/CSOMP_CSDCT_lotus128.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of lotus (OMP).
   :align: center

   Compressive Sensing based and RDA Imaging Results of lotus.


**2. Lasso优化, 不采用字典进行稀疏表示, 和采用DCT字典进行稀疏表示的结果如下:**

点目标结果

.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/CS/CSLASSO_CSDCT_points128.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of points.
   :align: center

   Compressive Sensing based and RDA Imaging Results of points (Lasso).


船只结果:

.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/CS/CSLASSO_CSDCT_ship128.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of ship.
   :align: center

   Compressive Sensing based and RDA Imaging Results of ship (Lasso).

荷花结果:

.. figure:: ../../../_static/figs/Radar/SAR/SRImaging/CS/CSLASSO_CSDCT_lotus128.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of lotus.
   :align: center

   Compressive Sensing based and RDA Imaging Results of lotus (Lasso).


真实数据
~~~~~~~~~~~~~~~


实验说明
^^^^^^^^^^^^^^

实验代码
^^^^^^^^^^^^^^



实验结果
^^^^^^^^^^^^^^

