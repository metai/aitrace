.. _Section-PoolingUnit:

池化单元
=====================



经典二维池化运算
------------------------


与经典二维卷积一样, 池化后的特征图大小为

.. math::
   \begin{array}{ll}
   H_{o} &= \left\lfloor\frac{H_{i}  + 2 \times P_h - K_h}{S_h} + 1\right\rfloor \\
   W_{o} &= \left\lfloor\frac{W_{i}  + 2 \times P_w - K_w}{S_w} + 1\right\rfloor
   \end{array}
   :label: equ-ClassicalPooling2dSize



膨胀二维池化运算
------------------------

.. math::
   \begin{array}{ll}
   H_{o} &= \left\lfloor\frac{H_{i}  + 2 \times P_h - D_h \times (K_h - 1) - 1}{S_h} + 1\right\rfloor \\
   W_{o} &= \left\lfloor\frac{W_{i}  + 2 \times P_w - D_w \times (K_w - 1) - 1}{S_w} + 1\right\rfloor
   \end{array}
   :label: equ-DilationPooling2dSize



金字塔池化
--------------------------




空间金字塔池化
~~~~~~~~~~~~~~~~~~~~~~

空间金字塔池化(Spatial Pyramid Pooling, SPP)由何凯明等人于2015年提出 :cite:`Spatial.K.He.2015`, 如 :figure:numref:`fig-SPP` 所示, 对于任意大小的特征图输出, 通过使用不同池化窗口和步长, 对特征图进行池化, 将特征图划分成具有不同尺度的固定大小特征图, 特征图拉成列向量并连接, 得到固定的输出维度, 实现了多尺度网络的训练以及识别，进而提升了图像分类和目标检测的精度.

.. _fig-SPP:

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Pooling/SPP.*
   :scale: 80 %
   :alt: 空间金字塔池化
   :align: center

   空间金字塔池化

   空间金字塔池化



金字塔场景池化
~~~~~~~~~~~~~~~~~~~~~~

赵等人 :cite:`Pyramid.Zhao.2016` 于2016年提出一种用于语义分割的金字塔场景分析网络(Pyramid Scene Parsing Network, PSP-Net), 其中采用 :figure:numref:`fig-PSPNetSPP` 所示池化结构, 与SPP类似, 通过使用不同池化窗口和步长, 对特征图进行池化, 可以得到不同等级池化特征(图中对应全局池化, :math:`2×2`, :math:`3×3`, :math:`6×6`), 与SPP不同的是, 空间金字塔池化后, 采用 :math:`1×1×N` 的卷积核来调整通道数, 并使用上采样操作将不同等级的特征图上采样到与原始卷积输出特征图一致大小.


.. _fig-PSPNetSPP:

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Pooling/PSP.*
   :scale: 80 %
   :alt: 金字塔池化
   :align: center

   金字塔池化

   金字塔池化




扩张空间金字塔池化
~~~~~~~~~~~~~~~~~~~~~~

扩张空间金字塔池化(Atrous Spatial Pyramid Pooling, ASPP)由陈等人 :cite:`Rethinking.Chen.2017,Encoder.Chen.2018,DeepLab.L.Chen.2018` 提出, 如 :figure:numref:`fig-PSPNetASPP` 所示, 通过不同大小的卷积核, 膨胀因子和填补大小, 输出相同大小的卷积特征图, 将这些不同尺度的特征拼接再经过 :math:`1×1` 卷积等到 ASPP 池化输出.


.. _fig-PSPNetASPP:

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Pooling/ASPP.*
   :scale: 80 %
   :alt: 扩张空间金字塔池化
   :align: center

   扩张空间金字塔池化

   扩张空间金字塔池化
