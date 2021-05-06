.. _Section-DualAscent:

对偶上升算法
=====================


概念与内涵
------------

对偶上升法 (:term:`Dual Ascent`) :cite:`S.Boyd.2011` p5


考虑如下等式约束凸优化问题

.. math::
    P_0: \begin{array}{ll}{\rm{min}_{\bm x}} & {f({\bm x})} \\ {\text { s.t. }} & {{\bm A}{\bm x} = {\bm b}}\end{array}
    :label: equ-OrignalProblem

其中, :math:`{\bm x}\in{\mathbb R}^{N\times 1}`, :math:`{\bm A}\in{\mathbb R}^{M\times N}`, :math:`f: {\mathbb R}^{N\times 1} \rightarrow {\mathbb R}` 为凸函数. 问题 :math:`P_0` ( :eq:`equ-OrignalProblem`) 的拉格朗日函数形式为

.. math::
    L({\bm x}, {\bm \lambda}) = f({\bm x}) + {\bm \lambda}^T({\bm{Ax}-{\bm b}})

其对偶函数为

.. math::
    {D}: {\rm max}\ g({\bm x}) = {\rm inf}_{\bm x} L({\bm x}, {\bm \lambda}) = -f^{*}(-{\bm A}^T{\bm \lambda}) - {\bm b}^T{\bm \lambda},

其中, :math:`{\bm \lambda}` 为对偶变量也是拉格朗日乘子变量, :math:`f^{*}` 是函数 :math:`f` 的凸共轭.


对偶上升法迭代更新过程为

.. math::
    \begin{aligned} {\bm x}^{k+1} & :=\underset{{\bm x}}{\operatorname{argmin}} L\left({\bm x}, {\bm \lambda}^{k}\right) \\ {\bm \lambda}^{k+1} & :={\bm \lambda}^{k}+\mu^{k}\left({\bm A} {\bm x}^{k+1}-{\bm b}\right) \end{aligned}

其中, :math:`k` 为迭代次数, :math:`{\mu}^k` 为迭代步长. 选择合适的 :math:`{\mu}^k`, 对偶函数每次迭代后会上升 (:math:`g({\bm x})`), 因而称为对偶上升法.



实验与分析
------------

