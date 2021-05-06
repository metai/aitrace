.. _Section-DualProblem:

优化中的对偶问题
=====================

优化中的对偶问题 ( :term:`Dual Problem` )




Fenchel's duality theorem

Wolfe dual problem


约束优化的对偶问题
----------------

设有原优化问题

.. math::
    P: {\rm max}\ f({\bm x}) = {\bm c}^T {\bm x} \\
    {\rm s.t.} \left\{\begin{array}{r}{{\bm A}{\bm x}\leq {\bm b}} \\ {{\bm x} \geq {\bm 0}}\end{array}\right.
    :label: equ-DualProblem_P

其对偶优化问题为

.. math::
    D: {\rm min}\ g({\bm y}) = {\bm b}^T {\bm y} \\
    {\rm s.t.} \left\{\begin{array}{r}{{\bm A}^T{\bm y}\geq {\bm c}^T} \\ {{\bm y} \geq {\bm 0}\ }\end{array}\right.
    :label: equ-DualProblem_D


上述问题 :math:`P` 和 :math:`D` 称为一对对偶优化问题.

