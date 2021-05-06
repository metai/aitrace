.. _Section-DesignPrinciples:

自步函数设计准则
=====================


--------------


自步函数 :math:`g(v_i, \lambda)` 一般需要满足以下条件 :cite:`Jiang.2014`:

1. :math:`g(v_i, \lambda)` 在区间 :math:`[0, 1]` 上是凸函数, 以此保证 :math:`v_i^*` 是唯一的;
2. :math:`v_i^*(l_i, \lambda)` 关于 :math:`l_i` 是单调递减的, 这样可以引导模型选择较容易地样本;
3. :math:`v_i^*(l_i, \lambda)` 关于 :math:`\lambda` 是单调递增的, 大的 :math:`\lambda` 可以容忍更大的损失, 可以逐渐把复杂样例包含进来.

