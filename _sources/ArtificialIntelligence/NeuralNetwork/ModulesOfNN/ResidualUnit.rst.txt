.. _Section-ResidualUnit:

残差单元
=====================




经典残差块分析
------------------

残差块结构
~~~~~~~~~~~~






梯度传播分析
~~~~~~~~~~~~~~


利用链式求导法则, :figure:numref:`fig-ClassicalNetClassicalResidualNetDemo` (a) 所示传统神经网络的梯度传播过程可以表示为 :eq:`equ-ClassicalNetGradientPropagation_3HiddenLayers`


.. math::
   \begin{aligned}
   \frac{\partial L}{\partial {\bm w}_3} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm w}_3}\\
   \frac{\partial L}{\partial {\bm w}_2} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_3}\times \frac{\partial {\bm h}_3}{\partial {\bm w}_2}\\
   \frac{\partial L}{\partial {\bm w}_1} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_3}\times \frac{\partial {\bm h}_3}{\partial {\bm h}_2}\times \frac{\partial {\bm h}_2}{\partial {\bm w}_1}\\
   \frac{\partial L}{\partial {\bm w}_0} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_3}\times \frac{\partial {\bm h}_3}{\partial {\bm h}_2}\times \frac{\partial {\bm h}_2}{\partial {\bm h}_1}\times \frac{\partial {\bm h}_1}{\partial {\bm w}_0}\\
   \end{aligned}
   :label: equ-ClassicalNetGradientPropagation_3HiddenLayers



.. _fig-ClassicalNetClassicalResidualNetDemo:

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/ResidualUnit/ClassicalNetClassicalResidualNetDemo.*
   :alt: 经典神经网络与残差网络结构对比
   :align: center

   经典神经网络与残差网络结构对比. (a) 含三个隐藏层的神经网络结构示意图; (b) 含三个残差块的神经网络示意图.



同样地, 根据链式求导法则, :figure:numref:`fig-ClassicalNetClassicalResidualNetDemo` (b) 所示残差神经网络的梯度传播过程可以表示为 :eq:`equ-ClassicalNetGradientPropagation_3ResidualBlocks`


.. math::
   \begin{aligned}
   \frac{\partial L}{\partial {\bm w}_3} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm w}_3}\\
   \frac{\partial L}{\partial {\bm w}_2} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm s}_3}\times \frac{\partial {\bm s}_3}{\partial {\bm w}_2}\\
   \frac{\partial L}{\partial {\bm w}_1} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm s}_3}\times \frac{\partial {\bm s}_3}{\partial {\bm s}_2}\times \frac{\partial {\bm s}_2}{\partial {\bm w}_1}\\
   \frac{\partial L}{\partial {\bm w}_0} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm s}_3}\times \frac{\partial {\bm s}_3}{\partial {\bm s}_2}\times \frac{\partial {\bm s}_2}{\partial {\bm s}_1}\times \frac{\partial {\bm s}_1}{\partial {\bm w}_0}\\
   \end{aligned}
   :label: equ-ClassicalNetGradientPropagation_3ResidualBlocks

又 :math:`\frac{\partial {\bm s}_n}{\partial {\bm w}_{n-1}} = \frac{\partial {\bm h}_n}{\partial {\bm w}_{n-1}}`, :math:`\frac{\partial {\bm s}_n}{\partial {\bm s}_{n-1}} = \frac{\partial {\bm h}_n}{\partial {\bm s}_{n-1}} + 1`, 代入 :eq:`equ-ClassicalNetGradientPropagation_3ResidualBlocks` 中得

.. math::
   \begin{aligned}
   \frac{\partial L}{\partial {\bm w}_3} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm w}_3}\\
   \frac{\partial L}{\partial {\bm w}_2} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm s}_3}\times \frac{\partial {\bm h}_3}{\partial {\bm w}_2}\\
   \frac{\partial L}{\partial {\bm w}_1} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm s}_3}\times \left(\frac{\partial {\bm h}_3}{\partial {\bm s}_2} + 1 \right)\times \frac{\partial {\bm h}_2}{\partial {\bm w}_1}\\
   \frac{\partial L}{\partial {\bm w}_0} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm s}_3}\times \left(\frac{\partial {\bm h}_3}{\partial {\bm s}_2} + 1 \right)\times \left(\frac{\partial {\bm h}_2}{\partial {\bm s}_1} + 1 \right)\times \frac{\partial {\bm h}_1}{\partial {\bm w}_0}\\
   \end{aligned}
   :label: equ-ClassicalNetGradientPropagation_3ResidualBlocks_Final

