.. _Section-EntropyLossFunctionsNeuralNetwork:

基于熵的损失函数
=====================


什么是熵
------------------

熵通常用来衡量信息量, 为香浓信息量的期望

离散变量的熵
~~~~~~~~~~~~~~~~~~

.. math::
   H(p) = {\rm E}_p [{\rm log}_2 \frac{1}{p}] = \sum_{i}p_i{\rm log}_2\frac{1}{p_i} = -\sum_{i}p_i{\rm log}_2{p_i}
   :label: equ-Entropy



交叉熵损失函数
------------------

离散变量的交叉熵
~~~~~~~~~~~~~~~~~~

.. math::
   H(p,q) = {\rm E}_p [{\rm log}_2 \frac{1}{q}] = \sum_{i}p_i{\rm log}_2\frac{1}{q_i} = -\sum_{i}p_i{\rm log}_2{q_i}
   :label: equ-CrossEntropy


相对熵损失函数
------------------

相对熵(relative entropy)又称KL散度(Kullback–Leibler divergence), 用于衡量两个分布的距离


离散变量的相对熵
~~~~~~~~~~~~~~~~~~

.. math::
   D_{KL}(p||q) = \sum_i p_i{\rm log}_2\frac{p_i}{q_i} = H(p,q)-H(p)
   :label: equ-RelativeEntropy



二值交叉熵损失函数
------------------


.. math::
   \begin{aligned}
   L(p,q) &= -\sum_{i∈\{1,2\}}p_i{\rm log}_2{q_i}\\ &= -p_1{\rm log}_2q_1 - p_2{\rm log}_2q_2\\ &= -p_1{\rm log}_2q_1 - (1-p_1){\rm log}_2(1-q_1)
   \end{aligned}
   :label: equ-BinaryCrossEntropyLoss

