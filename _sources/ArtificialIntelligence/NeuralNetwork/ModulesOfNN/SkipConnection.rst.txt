.. _Section-SkipConnectionModulesNeuralNetworkArtificialIntelligence:

跳跃连接
=====================


**跳跃连接** (:term:`Skip Connection`)


前向跳跃连接
---------------------

经典前向跳跃连接
~~~~~~~~~~~~~~~~~~

结构分析
^^^^^^^^^^^^

如 :figure:numref:`fig-ForwardSkipAddConnection` 所示, :math:`{\bm w}_n, a_n` 分别表示第 :math:`n` 层的权重与激活函数, :math:`{\bm x}` 为输入, :math:`{\bm y}` 为神经网络输出. :figure:numref:`fig-ForwardSkipAddConnection` (a) 所示为无跳跃连接的网络结构, :figure:numref:`fig-ForwardSkipAddConnection` (b) 所示为前向跳跃连接结构示意图, 其中, 第 :math:`p` 层的输出跳跃连接至第 :math:`q` 层的输出, 加和后送入下一层. 网络的前向传播过程可以表示为 :eq:`equ-NetForwardPropagation_NHiddenLayers1SkipConnnection`.

.. math::
   \begin{aligned}
   {\bm y} &= a_N({\bm w}_N{\bm h}_N) \\
   &\ \ \vdots \\
   {\bm h}_{q+1} &= a_q({\bm w}_q{\bm s}_q) \\
   {\bm s}_q &= {\bm h}_p + {\bm h}_q \\
   &\ \ \vdots \\
   {\bm h}_{p+1} &= a_p({\bm w}_p{\bm h}_p) \\
   &\ \ \vdots \\
   {\bm h}_2 &= a_1({\bm w}_1{\bm h}_1) \\
   &\ \ \vdots \\
   {\bm h}_1 &= a_0({\bm w}_0{\bm x})
   \end{aligned}
   :label: equ-NetForwardPropagation_NHiddenLayers1SkipConnnection


.. _fig-ForwardSkipAddConnection:

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/SkipConnection/ForwardSkipAddConnection.*
   :alt: 前向跳跃连接示意图
   :align: center

   前向跳跃连接示意图. 第 :math:`p` 层的输出与第 :math:`q` 层的输出加和后送入下一层.



梯度传播分析
^^^^^^^^^^^^

利用链式求导法则, :figure:numref:`fig-ForwardSkipAddConnection` (a) 所示传统神经网络的梯度传播过程可以表示为 :eq:`equ-ClassicalNetGradientPropagation_NHiddenLayers`


.. math::
   \begin{aligned}
   \frac{\partial L}{\partial {\bm w}_N} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm w}_N}\\
   \frac{\partial L}{\partial {\bm w}_{N-1}} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm w}_{N-1}}\\
   &\ \ \vdots \\
   \frac{\partial L}{\partial {\bm w}_q} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_{q+1}}{\partial {\bm w}_q}\\
   &\ \ \vdots \\
   \frac{\partial L}{\partial {\bm w}_p} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_{q+1}}{\partial {\bm h}_q}\times \cdots \times \frac{\partial {\bm h}_{p+1}}{\partial {\bm w}_p}\\
   &\ \ \vdots \\
   \frac{\partial L}{\partial {\bm w}_1} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_2}{\partial {\bm w}_1}\\
   \frac{\partial L}{\partial {\bm w}_0} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_2}{\partial {\bm h}_1}\times \frac{\partial {\bm h}_1}{\partial {\bm w}_0}\\
   \end{aligned}
   :label: equ-ClassicalNetGradientPropagation_NHiddenLayers


同样地, 根据链式求导法则, :figure:numref:`fig-ForwardSkipAddConnection` (b) 所示含跳跃连接的神经网络的梯度传播过程可以表示为 :eq:`equ-NetGradientPropagation_NHiddenLayers1SkipConnnection`

.. math::
   \begin{aligned}
   \frac{\partial L}{\partial {\bm w}_N} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm w}_N}\\
   \frac{\partial L}{\partial {\bm w}_{N-1}} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm w}_{N-1}}\\
   &\ \ \vdots \\
   \frac{\partial L}{\partial {\bm w}_q} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_{q+1}}{\partial {\bm w}_q}\\
   \frac{\partial L}{\partial {\bm w}_{q-1}} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_{q+1}}{\partial {\bm s}_{q}}\times \frac{\partial {\bm s}_{q}}{\partial {\bm h}_{q}}\times \frac{\partial {\bm h}_{q}}{\partial {\bm w}_{q-1}}\\
   &\ \ \vdots \\
   \frac{\partial L}{\partial {\bm w}_p} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_{q+1}}{\partial {\bm s}_{q}}\times \frac{\partial {\bm s}_{q}}{\partial {\bm h}_{p+1}} \times \frac{\partial {\bm h}_{p+1}}{\partial {\bm w}_p}\\
   &\ \ \vdots \\
   \frac{\partial L}{\partial {\bm w}_{p-1}} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_{q+1}}{\partial {\bm s}_{q}}\times \frac{\partial {\bm s}_{q}}{\partial {\bm h}_p} \times \frac{\partial {\bm h}_{p}}{\partial {\bm w}_{p-1}}\\
   &\ \ \vdots \\
   \frac{\partial L}{\partial {\bm w}_1} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_{q+1}}{\partial {\bm s}_{q}}\times \frac{\partial {\bm s}_{q}}{\partial {\bm h}_2} \times \frac{\partial {\bm h}_2}{\partial {\bm w}_1}\\
   &\ \ \vdots \\
   \frac{\partial L}{\partial {\bm w}_0} &= \frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_{q+1}}{\partial {\bm s}_{q}}\times \frac{\partial {\bm s}_{q}}{\partial {\bm h}_1} \times \frac{\partial {\bm h}_1}{\partial {\bm w}_0}\\
   \end{aligned}
   :label: equ-NetGradientPropagation_NHiddenLayers1SkipConnnection

当 :math:`k=p+1, p+2, \cdots, q` 时, :math:`\frac{\partial {\bm s}_q}{\partial {\bm h}_k}=\frac{\partial {\bm s}_q}{\partial {\bm h}_q}\times \frac{\partial {\bm h}_q}{\partial {\bm h}_{q-1}} \times \cdots \times \frac{\partial {\bm h}_{k+1}}{\partial {\bm h}_k}`.

当 :math:`k=1, 2, \cdots, p` 时, :math:`\frac{\partial {\bm s}_q}{\partial {\bm h}_k}=\frac{\partial {\bm s}_q}{\partial {\bm h}_p}\times \frac{\partial {\bm h}_p}{\partial {\bm h}_k} = \left(\frac{\partial {\bm h}_q}{\partial {\bm h}_p} + 1\right)\times \frac{\partial {\bm h}_p}{\partial {\bm h}_k} = \left(\frac{\partial {\bm h}_q}{\partial {\bm h}_{q-1}}\times \cdots \times \frac{\partial {\bm h}_{p+1}}{\partial {\bm h}_p} + 1\right)\times \frac{\partial {\bm h}_p}{\partial {\bm h}_{p-1}}\times \cdots \times \frac{\partial {\bm h}_{k+1}}{\partial {\bm h}_k}`.


.. note::
   由 :eq:`equ-ClassicalNetGradientPropagation_NHiddenLayers` 和 :eq:`equ-NetGradientPropagation_NHiddenLayers1SkipConnnection` 可知, 与传统不含跳跃连接的神经网络相比, 从第 :math:`p` 层输出跳跃连接至第 :math:`q` 层输出的跳跃神经网络的梯度在第 :math:`p+1` 层到第 :math:`N` 层保持不变, 在第 :math:`1` 层到第 :math:`p` 层的变大, 且增量为 :math:`\frac{\partial L}{\partial {\bm y}}\times \frac{\partial {\bm y}}{\partial {\bm h}_N}\times \frac{\partial {\bm h}_N}{\partial {\bm h}_{N-1}}\times \cdots \times \frac{\partial {\bm h}_{q+1}}{\partial {\bm s}_{q}}\times \frac{\partial {\bm h}_p}{\partial {\bm h}_{p-1}}\times \cdots \times \frac{\partial {\bm h}_{k+1}}{\partial {\bm h}_k}`, (:math:`k=1,2, \cdots, p`).




后向跳跃连接
---------------------

梯度传播
~~~~~~~~~~~~~~~~~~





