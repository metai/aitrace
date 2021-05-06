.. _Section-CommonSelfPacedFunction:

常用自步函数
=====================

文献 :cite:`Jiang.2014` 中总结了一些常见的自步函数, 设有 :math:`N` 个样本, 样本容易度向量记为 :math:`{\bm v}∈[0, 1]^N`, 自步函数记为 :math:`f({\bm v}; \lambda)`, 其中, :math:`λ = \frac{1}{k}`, 最优解记为 :math:`{\bm v}^* = [v_1^*, v_2^*, \cdots, v_N^*]`.


二值加权
------------

二值加权自步函数的表达式为

.. math::
   f(\bm{v}, k) =  = -λ\|{\bm v}\|_1 = -λ\sum_{n=1}^N v_n
   :label: equ-SPL_BinaryFunction

其最优解为

.. math::
   v_{n}^* = \left\{\begin{array}{ll}{1,} & {l_{n}<\lambda} \\ {0,} & {l_{n}>=\lambda}\end{array}\right.
   :label: equ-SPL_BinaryUpdate



线性加权
------------

线性加权自步函数的表达式为

.. math::
   f(\bm{v}, \lambda)=\lambda\left(\frac{1}{2}\|\bm{v}\|_{2}^{2}-\sum_{n=1}^{N} v_{n}\right)
   :label: equ-SPL_LinearFunction

其最优解为

.. math::
   v_{n}^* = {\rm max}\{1-l_n/\lambda, 0\}
   :label: equ-SPL_LinearUpdate



对数加权
------------

对数加权自步函数的表达式为

.. math::
   f(\bm{v}, \lambda) = \sum_{n=1}^{N}\left(\zeta v_{n}-\frac{\zeta^{v_{n}}}{{\rm log} \zeta}\right)
   :label: equ-SPL_LogarithmicFunction

其中, :math:`\zeta=1-\lambda, 0<\lambda<1`

其最优解为

.. math::
   v_{n}^{*}=\left\{\begin{array}{ll}{0,} & {l_{n}>=\lambda} \\ {\log \left(l_{n}+\zeta\right) / \log \xi,} & {l_{n}<\lambda}\end{array}\right.
   :label: equ-SPL_LogarithmicUpdate


混合加权
-------------

混合加权自步函数的表达式为

.. math::
   f\left(\bm{v}, λ \right)=-\zeta \sum_{n=1}^{N} \log \left(v_{n}+\zeta / λ \right)
   :label: equ-SPL_MixtureFunction

其中, :math:`ζ= \frac{1}{k^{\prime} - k} = \frac{\lambda^{\prime}\lambda}{\lambda-\lambda^{\prime}}`, :math:`k^{\prime}>k>0`, :math:`0<\lambda^{\prime}<\lambda`

其最优解为

.. math::
   v_{n}^{*}=\left\{\begin{array}{ll}{1,} & {l_{n} \leq \lambda^{\prime}} \\ {0,} & {l_{n} \geq \lambda} \\ {\zeta / l_{n}-\zeta / \lambda,} & {\text { otherwise }}\end{array}\right.
   :label: equ-SPL_MixtureUpdate



