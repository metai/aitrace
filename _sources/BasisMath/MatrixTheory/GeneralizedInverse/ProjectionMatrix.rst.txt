.. _Section-ProjectionMatrix:

投影矩阵
=====================

投影算子与投影矩阵
-----------------------

什么是投影
~~~~~~~~~


.. _def-Projection:

.. proof:definition:: 投影

   设 :math:`\mathbb L` 和 :math:`\mathbb M` 均为 :math:`{\mathbb C}^n` 的子空间, 且 :math:`\mathbb L \oplus \mathbb M = {\mathbb C}^n` , :math:`\forall {\bm x} \in {\mathbb C}^n` 可分解为

   .. math::
        	{\bm x} = {\bm y} + {\bm z} , {\bm y}\in \mathbb L , {\bm z} \in \mathbb M

   称 :math:`{\bm y}` 是 :math:`{\bm x}` 沿着 :math:`\mathbb M` 到 :math:`\mathbb L` 的 **投影** .

.. figure:: ../../../_static/figs/BasisMath/MatrixTheory/GeneralizedInverse/ProjectionMatrix/DefProjection.png
   :scale: 80 %
   :alt: demo of Projection
   :align: center

   二维空间中的投影示意

   二维空间中的投影示意


投影算子与投影矩阵
~~~~~~~~~~~~~~~~~~~

.. _def-ProjectionOperatorProjectionMatrix:

.. proof:definition:: 投影算子与投影矩阵

   将 :math:`\forall {\bm x} \in {\mathbb C}^n` 沿着 :math:`\mathbb M` 到 :math:`\mathbb L` 的投影变换称为沿着 :math:`\mathbb M` 到 :math:`\mathbb L` 的 **投影算子** , 记为 :math:`P_{\mathbb L, \mathbb M}` , 即

   .. math::
       	P_{\mathbb L, \mathbb M}{\bm x} = {\bm y}.

   投影算子 :math:`P_{\mathbb L, \mathbb M}` 在 :math:`{\mathbb C}^n` 中的基 :math:`{\bm e}_1, {\bm e}_2, \cdots, {\bm e}_n` 下的矩阵称为 **投影矩阵** .

线性投影算子
~~~~~~~~~~~~

.. _def-LinearProjectionOperator:

.. proof:definition:: 线性投影算子

   若对于 :math:`\forall {\bm x}_1, {\bm x}_2 \in {\mathbb C}^n` 和 :math:`\lambda, \mu \in {\mathbb C}` , 恒有

   .. math::
       	P_{\mathbb L, \mathbb M}(\lambda {\bm x}_1 + \mu {\bm x}_2) = \lambda P_{\mathbb L, \mathbb M}{\bm x}_1 + \mu P_{\mathbb L, \mathbb M}{\bm x}_2

   则称 :math:`P_{L,M}` 为 **线性算子** .


正交投影算子与正交投影矩阵
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _def-OrthogonalProjectionOperatorMatrix:

.. proof:definition:: 正交投影算子与正交投影矩阵

   设 :math:`L` 是 :math:`{\mathbb  C}^n` 的子空间, 称沿着 :math:`{\mathbb L}^{\perp}` 到 :math:`\mathbb L` 的投影算子 :math:`P_{\mathbb L, \mathbb L^{\perp}}` 为 **正交投影算子** , 简记为 :math:`P_{\mathbb L}` .

   正交投影算子 :math:`P_{\mathbb L, \mathbb L^{\perp}}` 在 :math:`{\mathbb C}^n` 中的基 :math:`{\bm e}_1, {\bm e}_2, \cdots, {\bm e}_n` 下的矩阵称为 **正交投影矩阵** .

性质
~~~~~~

- 矩阵 :math:`{\bm P}` 为投影矩阵 :math:`\leftrightarrow` :math:`{\bm P}` 为幂等矩阵.
- 矩阵 :math:`{\bm P}` 为正交投影矩阵 :math:`\leftrightarrow` :math:`{\bm P}` 为幂等Hermite矩阵.


.. hint::
	若 :math:`{\bm P}^2 = {\bm P}{\bm P} = {\bm P}` , 则称 :math:`{\bm P}` 为 **幂等矩阵** .


正交投影阵的求解
~~~~~~~~~~~~~~~~~~~~~~~~

