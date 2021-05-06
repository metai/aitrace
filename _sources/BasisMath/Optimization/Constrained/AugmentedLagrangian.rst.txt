.. _Section-AugmentedLagrangian:

增广拉格朗日法
=====================

增广拉格朗日法 (:term:`Augmented Lagrangian Method`, ALM)


概念与内涵
------------


设有等式约束优化问题:

.. math::
    {P}_0: {\rm min}_{\bm x}\ f({\bm x})\ \ {\rm s.t.}\ \ g_i({\bm x}) = 0,
   :label: equ-EqualityConstraintOptimizationProbOriginal

其中, :math:`g_i, i=1,2,\cdots,M` 为 :math:`M` 个等式约束. 化为无约束优化的曾广拉格朗日函数形式为

.. math::
    {P}_1: {\rm min}_{\bm x}\  L({\bm x}, {\bm \lambda}, \mu) = f({\bm x}) - \sum_{i=1}^M \lambda_i g_i({\bm x}) + \frac{\mu}{2}\sum_{i=1}^M g_i({\bm x})^2,
   :label: equ-AugmentedLagrangianFunctionFormulation

其中, :math:`i=1,2,\cdots,M`, :math:`\lambda_i` 为 **拉格朗日乘子** (Lagrange Multiplier), :math:`\mu` 为增广拉格朗日乘子 (Augmented Lagrange Multiplier). 其矩阵形式为

.. math::
    {P}_1: {\rm min}_{\bm x}\  L({\bm x}, {\bm \lambda}, \mu) = f({\bm x}) - {\bm \lambda}^T {\bm g} + \frac{\mu}{2} \|{\bm g}\|_2^2,
   :label: equ-AugmentedLagrangianFunctionFormulation_matrix

其中, :math:`{\bm \lambda} = [\lambda_1, \lambda_2, \cdots, \lambda_M]^T` 为 :math:`M` 个拉格朗日乘子构成的向量, :math:`{\bm x} = [x_1, x_2, \cdots, x_N]^T` 为 :math:`N` 个变量构成的向量, :math:`{\bm g} = [g_1({\bm x}), g_2({\bm x}),\cdots, g_M(\bm x)]^T` 为 :math:`M` 个约束构成的向量. :math:`\|\|_2^2` 表示向量的 :math:`\ell_2` 范数.


即增广拉格朗日在拉格朗日的基础上加上了一个光滑惩罚项 :math:`\|{\bm g}\|_2^2`.

与对偶上升法类似 (:ref:`Section-DualAscent`), 其迭代迭代更新规则为

.. math::
    \begin{aligned} {\bm x}^{k+1} & :=\underset{{\bm x}}{\operatorname{argmin}}\ L\left({\bm x}, {\bm \lambda}^{k}\right) \\ {\bm \lambda}^{k+1} & :={\bm \lambda}^{k} - {\mu}_k {\bm g}({\bm x}^{k+1}) \end{aligned}






实验与分析
-------------------

