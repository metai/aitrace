.. _Section-GeneralizedInverseLinearEquations:

广义逆矩阵与线性方程组
=======================


基本概念
---------------------


考虑非齐次 ( :term:`Non-Homogeneous` ) 线性方程组 ( :term:`System of linear equations` )

.. math::
   {\bm A}{\bm x} = {\bm b}

其中, :math:`{\bm A}\in {\mathbb C}^{m\times n}, {\bm b}\in {\mathbb C}^m` , :math:`{\bm x}\in {\mathbb C}^n` 为待求解向量. 若存在 :math:`{\bm x}` 满足上述方程, 则称方程组 **相容** 或 **有解** , 否则称方程组 **不相容** 或 **无解** .

.. hint::

   - 线性 ( 可以表示成 :math:`{\bm{Ax=b}}` ) , 非线性 ( 不能表示成 :math:`{\bm{Ax=b}}` ):
   - 齐次 ( :math:`{\bm b} = 0` ) , 非齐次 ( :math:`{\bm b} \neq 0` ):
   - 相容 ( 有解, 不矛盾 ) , 不相容 ( 无解, 矛盾 ):


几种常见解
----------------------

- 线性方程组相容的充要条件: :math:`{\bm A}{\bm A}^{(1)}{\bm b} = {\bm b}` , 不唯一
- 不相容线性方程组的最小二乘解: :math:`{\bm x} = {\bm A}^{(1,3)}{\bm b}` , 不唯一
- 相容线性方程组的极小范数解: :math:`{\bm x} = {\bm A}^{(1,4)}{\bm b}` , 唯一, 且在 :math:`R({\bm A}^H)` 中
- 不相容线性方程组的极小范数最小二乘解: :math:`{\bm x} = {\bm A}^+{\bm b}` , 唯一

对应地还有:

- 相容线性方程组的通解: :math:`{\bm x} = {\bm A}^{(1)}{\bm b} + ({\bm I}-{\bm A}^{(1)}{\bm A}{\bm y})` , :math:`{\bm y}\in {\mathbb C}^n`
- 设 :math:`{\bm X}\in {\mathbb C}^{n\times m}` , 若 :math:`\forall {\bm b}\in {\mathbb C}^m` , 有 :math:`{\bm x} = {\bm{Xb}}` 是 :math:`{\bm A}{\bm x} = {\bm b}` 的最小二乘解, 则 :math:`{\bm X} \in {\bm A}\{1,3\}`
- 设 :math:`{\bm X}\in {\mathbb C}^{n\times m}` , 若 :math:`\forall {\bm b}\in {\mathbb C}^m` , 有 :math:`{\bm x} = {\bm{Xb}}` 是 :math:`{\bm A}{\bm x} = {\bm b}` 的极小范数解, 则 :math:`{\bm X} \in {\bm A}\{1,4\}`
- 设 :math:`{\bm X}\in {\mathbb C}^{n\times m}` , 若 :math:`\forall {\bm b}\in {\mathbb C}^m` , 有 :math:`{\bm x} = {\bm{Xb}}` 是 :math:`{\bm A}{\bm x} = {\bm b}` 的极小范数最小二乘解, 则 :math:`{\bm X} = {\bm A}^+`
