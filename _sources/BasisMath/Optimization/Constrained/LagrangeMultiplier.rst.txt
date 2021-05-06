.. _Section-LagrangeMultiplier:

拉格朗日乘子法
=====================

概念与内涵
------------


在优化理论中, **拉格朗日乘子** (:term:`Lagrange Multiplier`) 法是用于求解等式约束优化问题的局部极小极大问题. 其基本思想是将约束优化问题转化为无约束优化问题. 函数的不动点/稳定点(stationary point)也满足等式约束, 即函数在该不动点的梯度可以表示成约束在该点的梯度的线性组合, 从而原始问题可转化为拉格朗日函数形式 (Lagrangian Function).


.. _def-LagrangianFunction: 拉格朗日函数

.. proof:definition::

    设有等式约束优化问题:

    .. math::
        {P}_0: {\rm min}_{\bm x}\ f({\bm x})\ \ {\rm s.t.}\ \ g_i({\bm x}) = 0,
       :label: equ-EqualityConstraintOptimizationProb

    其中, :math:`g_i, i=1,2,\cdots,M` 为 :math:`M` 个等式约束. 化为无约束优化的拉格朗日函数形式为

    .. math::
        {P}_1: {\rm min}_{\bm x}\  L({\bm x}, {\bm \lambda}) = f({\bm x}) - \sum_{i=1}^M \lambda_i g_i({\bm x}),
       :label: equ-LagrangianFunctionFormulation

    其中, :math:`\lambda_i, i=1,2,\cdots,M` 为 **拉格朗日乘子** (Lagrange Multiplier), 等号右边两项可以为加也可以为减. 其矩阵形式为

    .. math::
        {P}_1: {\rm min}_{\bm x}\  L({\bm x}, {\bm \lambda}) = f({\bm x}) - {\bm \lambda}^T {\bm g},
       :label: equ-LagrangianFunctionFormulation_matrix

    其中, :math:`{\bm \lambda} = [\lambda_1, \lambda_2, \cdots, \lambda_M]^T` 为 :math:`M` 个拉格朗日乘子构成的向量, :math:`{\bm x} = [x_1, x_2, \cdots, x_N]^T` 为 :math:`N` 个变量构成的向量, :math:`{\bm g} = [g_1({\bm x}), g_2({\bm x}),\cdots, g_M(\bm x)]^T` 为 :math:`M` 个约束构成的向量.

易知 :eq:`equ-LagrangianFunctionFormulation_matrix` 对 :math:`{\bm \lambda}` 求导为

.. math::
    \nabla_{\bm \lambda} L({\bm x}, {\bm \lambda}) = {\bm g}

:eq:`equ-LagrangianFunctionFormulation_matrix` 对 :math:`{\bm x}` 求导为

.. math::
    \nabla_{\bm x} L({\bm x}, \lambda) = {\nabla}_{\bm x}f({\bm x}) - \sum_{i=1}^M \lambda_i{\nabla}_{\bm x}g_i(\bm x) = {\nabla}_{\bm x}f({\bm x}) - {\bm \lambda}^T{\nabla}_{\bm x}{\bm g}

从而有

.. math::
    {\nabla}_{{\bm x},{\bm \lambda}}L({\bm x}, {\bm \lambda}) = 0  \Longleftrightarrow
    \left\{\begin{array}{l}{\nabla f({\bm x}) = {\bm \lambda}^T {\nabla}_{\bm x}{\bm g} = \sum_{i=1}^M\lambda_i {\nabla}_{\bm x}g_i({\bm x})} \\ {g_{1}({\bm x})=\cdots=g_M({\bm x})=0}\end{array}\right.
    :label: equ-GradientLagrangianFunction


拉格朗日函数的对偶问题
--------------------





约束优化与流形学习
------------------

寻找满足等式/不等式约束的极小极大问题, 可推广为寻找不同流形 :math:`{\mathcal M}` 上的最小值与最大值. :math:`{\mathcal M}` 不一定是欧式空间, 也可以是黎曼空间.

`Modern formulation via differentiable manifolds <http://en.volupedia.org/wiki/Lagrange_multiplier>`_


实验与分析
------------------








