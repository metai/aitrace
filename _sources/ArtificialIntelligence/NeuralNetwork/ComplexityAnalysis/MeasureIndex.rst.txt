.. _Section-MeasureIndex:

衡量指标
=====================

通常用参数量（params）、乘累加量（Fused multiply–add， Madd）、浮点数运算量（FLOPs）以及内存读写量来衡量网络的运算复杂度. 有关FLOPS参见 :ref:`Section-ComputationalComplexityPerformance` 小节.



运算量计算
-----------------


卷积层
~~~~~~~~~

卷积层的 :math:`\text {FLOPs}` 可由下式计算 :cite:`Molchanov.2016`

.. math::
    \text { FLOPs }=2 H W\left(C_{in} K^{2}+1\right) C_{out}
    :label: equ-conv_FLOPs

其中, :math:`H, W` 分别为输入特征图的高和宽, :math:`C_{in}, C_{out}` 分别为输入特征图和输出特征图的通道数, :math:`K` 为卷积和的大小.

由式 :eq:`equ-ClassicalConv2dIN4d` 和 :eq:`equ-ClassicalConv2d` 知, 单个卷积核与单个输入卷积需要执行 :math:`H_k W_k H_0 W_0` 乘法, :math:`(H_k W_k-1) H_0 W_0` 加法, :math:`C_i` 个卷积核相加需要执行 :math:`H_oW_o(C_i-1)`, 对于每个卷积输出加上偏置, 还需要执行 :math:`H_oW_o` 次加法, 那么单个输入单个卷积层的总运算量为

.. math::
   \begin{aligned}
   \text { FLOPs } &= \left[H_{k} W_{k} H_{o} W_{o} C_{i}+\left(H_{k} W_{k}-1\right) H_{o} W_{o} C_{i}+H_{o} W_{o}\left(C_{i}-1\right)+H_{o} W_{o}\right] C_{o}\\
                   &= 2 H_{k} W_{k} H_{o} W_{o} C_{i} C_{o}.
   \end{aligned}
   :label: equ-ClassicalConv2dOneInputFLOPs


全连接层
~~~~~~~~~~



.. math::
    \text { FLOPs }=(2 I-1) O

其中, :math:`I, O` 分别为全连接层的输入与输出神经元节点数.