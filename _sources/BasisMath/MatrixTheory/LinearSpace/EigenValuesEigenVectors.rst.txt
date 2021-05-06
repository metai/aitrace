.. _Section-EigenValuesEigenVectors:

特征值与特征向量
=====================

如何选择线性空间的基, 使得线性变换在该基下的矩阵表示最为简单. 涉及 特征值(eigenvalue) 与特征向量(eigenvector)

特征值与特征向量
-------------------

线性变换的特征值与特征向量
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _def-LinearTransformationEigenValuesEigenVectors:

.. proof:definition:: 线性变换的特征值与特征向量

   设 :math:`T` 是数域 :math:`{\mathbb K}` 上的线性空间 :math:`{\mathbb V}^n` 上的线性变换, 且对于数域 :math:`{\mathbb K}` 中的数 :math:`\lambda` , 若存在非零向量 :math:`{\bm x} \in {\mathbb V}^n` 满足如下条件

   .. math::
      T{\bm x} = \lambda {\bm x}

   则称 :math:`\lambda` 为 :math:`T` 的 **特征值** , :math:`{\bm x}` 为 :math:`T` 的属于特征值 :math:`\lambda` 的特征向量.


.. note::
   由上述定义知:

   - 线性变换不改变特征向量的方向

   - 特征值被特征向量唯一确定, 特征向量不被特征值唯一确定( :math:`T(k{\bm x}) = k\lambda {\bm x}` )


矩阵的特征值与特征向量
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _def-MatrixEigenValuesEigenVectors:

.. proof:definition:: 矩阵的特征值与特征向量

   设有矩阵 :math:`{\bm A}` , 且对于数域 :math:`{\mathbb K}` 中的数 :math:`\lambda` , 若存在非零向量 :math:`{\bm x} \in {\mathbb V}^n` 满足如下条件

   .. math::
      {\bm A}{\bm x} = \lambda {\bm x}


   则称 :math:`\lambda` 为矩阵 :math:`{\bm A}` 的 **特征值** , :math:`{\bm x}` 为 :math:`{\bm A}` 的属于特征值 :math:`\lambda` 的特征向量.


特征值与特征向量的关系
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. note::
   - 特征值被特征向量唯一确定, 特征向量不被特征值唯一确定( :math:`T(k{\bm x}) = k\lambda {\bm x}` )
   - 互不相同的特征值对应的特征向量线性无关

实例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


编程生成二维平面 :math:`(x, y)` 中的点, 这些点落在一个椭圆内, 长轴为 :math:`6` , 短轴为 :math:`2` , 如 :figure:numref:`fig-ellipseEigenVisual` 所示, 其主要的方向有两个, 长轴方向(红色), 短轴方向(蓝).

对这些二维数据做主成分分析 ( :term:`Principal Component Analysis`, PCA), 可得两个主要方向:

#. 零均值化数据
#. 计算数据的协方差(即两个维度间的)
#. 计算协方差矩阵的特征值与特征向量

.. _fig-ellipseEigenVisual:

.. figure:: ../../../_static/figs/BasisMath/MatrixTheory/LinearSpace/eigen/eigen_ellipse.png
   :scale: 80 %
   :alt: eigen ellipse
   :align: center

   椭圆内点的特征向量可视化

   对椭圆内的点进行特征分解, 得到两个特征方向, 并进行特征向量可视化, 长轴(红), 短轴(蓝).


.. warning::
   注意这里是对数据的协方差矩阵作特征值分解, 是否可以不求协方差矩阵直接对原始数据矩阵进行分析得到主方向. 特征值特征向量是针对变换矩阵而言的, 对数据矩阵是否有相关理论.

实现代码, 参见文件 `demo_eigen_ellipse.py <../../../_static/src/python/BasisMath/MatrixTheory/LinearSpace/demo_eigen_ellipse.py>`_  .

.. literalinclude:: ../../../_static/src/python/BasisMath/MatrixTheory/LinearSpace/demo_eigen_ellipse.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 55
   :linenos:
   :caption: demo_eigen_ellipse.py
   :name: bind-id


广义特征向量
-------------------

概念与内涵
~~~~~~~~~~~~~

一般, 若 :math:`\lambda^*` 是矩阵 :math:`{\bm A}` 的 :math:`k` 重特征值, 则对应的线性无关的特征向量 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_k` 可由下列方程组求出

.. math::
   (\lambda^* {\bm I}-{\bm A}){\bm x}_i = - {\bm x}_{i-1}

其中, :math:`i = 1, 2, \cdots, k` , 且规定 :math:`{\bm x}_0 = {\bm 0}` , 将求得的 :math:`k` 个向量 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_k` 称为矩阵 :math:`{\bm A}` 的 **广义特征向量** .

计算步骤
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 写出特征多项式矩阵 :math:`\lambda {\bm I}-{\bm A}`
#. 令特征多项式矩阵对应的行列式的值为 :math:`|\lambda {\bm I}-{\bm A}| = 0`
#. 求解得特征值 :math:`\lambda`
#. 对于单重特征值: 代入方程组 :math:`(\lambda {\bm I}-{\bm A}){\bm x} = {\bm 0}` , 求解特征向量.
#. 对于多重特征值: 代入方程组 :math:`(\lambda^* {\bm I}-{\bm A}){\bm x}_i = - {\bm x}_{i-1}` , 求解广义特征向量.


.. _Example-EigenValues:

例子(广义特征向量)
-------------------


.. note::
   求如下矩阵的特征值与特征向量/广义特征向量

   .. math::
      {\bm{A}} = \left[ {\begin{array}{ccc}
      0&2&2\\
      2&1&2\\
      0&2&1
      \end{array}} \right]

   解:

   1. 特征多项式矩阵为

   .. math::
      \lambda {\bm I}-{\bm A} = {\left[ {\begin{array}{ccc}
      \lambda &{ - 2}&{ - 2}\\
      { - 2}&{\lambda  - 1}&{ - 2}\\
      0&{ - 2}&{\lambda  - 1}
      \end{array}} \right]}

   可使用初等变换稍微化简, 方便求行列式的值 :math:`|\lambda {\bm I}-{\bm A}| = {{{(\lambda  + 1)}^2}(\lambda  - 4)}`

   2. 求解 :math:`|\lambda {\bm I}-{\bm A}| = {{{(\lambda  + 1)}^2}(\lambda  - 4)} = 0` 的解为 :math:`\lambda_1 = 4, \lambda_2 = \lambda_3 = -1`

   3. 由 :math:`(\lambda_1 {\bm I}-{\bm A}){\bm x}_1 = {\bm 0}` 求解出对应于 :math:`\lambda_1` 的特征向量 :math:`{\bm x}_1 = (5, 6, 4)^T`  , 由 :math:`(\lambda_2 {\bm I}-{\bm A}){\bm x}_2 = {\bm 0}` , :math:`(\lambda_3 {\bm I}-{\bm A}){\bm x}_3 = -{\bm x}_2` 求解广义特征向量 :math:`{\bm x}_2 = (0, 1, -1)^T` , :math:`{\bm x}_3 = (1, -1, 1/2)^T`




特征多项式与最小多项式
----------------------

特征多项式
~~~~~~~~~~~~~~~~~~~~~~~~~~~

设 :math:`T` 是 :math:`{\mathbb V}^n` 中的线性变换, :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_n` 是线性空间 :math:`{\mathbb V}^n` 中的基, :math:`T` 在该基下的矩阵为 :math:`{\bm A}` , 再设 :math:`{\bm x} = {\xi}_1  {\bm x}_1 + {\xi}_2  {\bm x}_2 + \cdots + {\xi}_n  {\bm x}_n` 为 :math:`T` 的属于特征值 :math:`\lambda` 的特征向量, 则由 :math:`T{\bm x} = \lambda {\bm x}` 知

.. math::
   {\bm A}\left[ {\begin{array}{lll}{{\xi _1}}\\{{\xi _2}}\\ \vdots \\{{\xi _n}}\end{array}} \right] = \lambda \left[ {\begin{array}{lll}{{\xi _1}}\\{{\xi _2}}\\ \vdots \\{{\xi _n}}\end{array}} \right]

从而有

.. math::
   (\lambda {\bm I} - {\bm A}) \left[ {\begin{array}{lll}{{\xi _1}}\\{{\xi _2}}\\ \vdots \\{{\xi _n}}\end{array}} \right] = {\bm 0}

由 :math:`{\bm x} \neq {\bm 0}` 知, :math:`{\xi _1}, {\xi _2}, \cdots, {\xi _n}` 不全为零, 从而方程组有非零解, 则

.. math::
   {\varphi}(\lambda) = {\rm det}(\lambda {\bm I} - {\bm A}) = \left | \lambda {\bm I} - {\bm A} \right | = (\lambda - \lambda_1)(\lambda - \lambda_2)\cdots(\lambda - \lambda_n)

.. _def-CharacteristicPolynomial:

.. proof:definition:: 特征多项式

   设有数域 :math:`{\mathbb K}` 上的 :math:`n` 阶方阵 :math:`{\bm A}` , 变量 :math:`\lambda` , 矩阵 :math:`{\bm A}` 的 **特征矩阵** :math:`\lambda {\bm I} - {\bm A}` 的行列式 :math:`{\rm det}(\lambda {\bm I} - {\bm A})` 称为矩阵 :math:`{\bm A}` 的 **特征多项式** . 记为 :math:`\varphi (\lambda)` , 其根 :math:`\lambda_i` 为 :math:`{\bm A}` 的 **特征值** , 非零解向量 ::math:`({\xi _1}, {\xi _2}, \cdots, {\xi _n})^T` 为 :math:`{\bm A}` 的属于特征值 :math:`\lambda_i` 的 **特征向量** .

.. note::
   线性变换 :math:`T` 的特征值与特征向量, 与 :math:`T` 的矩阵 :math:`{\bm A}` 的特征值与特征向量一一对应:

   -  :math:`T` 与 :math:`{\bm A}` 的特征值一致
   -  :math:`T` 的特征向量在基下的坐标与 :math:`{\bm A}` 的特征向量一致
   -  线性变换 :math:`T` 的矩阵 :math:`{\bm A}` 的特征多项式与基的选择无关

   即, 若 :math:`{\bm A}` 为 :math:`T` 在基 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_n` 下的矩阵, :math:`({\xi _1}, {\xi _2}, \cdots, {\xi _n})^T` 为矩阵 :math:`{\bm A}` 的属于特征值 :math:`\lambda` 的特征向量, 则

   -  :math:`\lambda` 是 :math:`T` 的特征值
   -  :math:`{\bm x} = {\xi}_1  {\bm x}_1 + {\xi}_2  {\bm x}_2 + \cdots + {\xi}_n  {\bm x}_n` 是 :math:`T` 的属于特征值 :math:`\lambda` 的特征向量
   -  线性变换 :math:`T` 的矩阵 :math:`{\bm A}` 的特征多项式与基的选择无关


.. _theo-HamiltonCayley:

.. proof:theorem:: Hamilton-Cayley

   :math:`n` 阶矩阵 :math:`{\bm A}` 是其特征多项式 :math:`{\varphi}(\lambda)` 的矩阵根. 即若有

   .. math::
         {\varphi}(\lambda) = {\rm det}(\lambda {\bm I} - {\bm A}) = \lambda^n + a_1\lambda^{n-1} + \cdots + a_{n-1}\lambda + a_n

   则

   .. math::
         {\varphi}({\bm A}) = {\bm A}^n + a_1{\bm A}^{n-1} + \cdots + a_{n-1}{\bm A} + a_n{\bm I} = {\bm O}.

最小多项式
~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _def-MinimalPolynomial:

.. proof:definition:: 最小多项式

   定义: 首项系数是1, 次数最小, 且以矩阵 :math:`{\bm A}` 为根的 :math:`\lambda` 的多项式, 称为 :math:`{\bm A}` 的 **最小多项式** (:term:`MinimalPolynomial`) , 常用 :math:`m(\lambda)` 表示.



特征子空间与不变子空间
-----------------------------

什么是特征子空间
~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _def-CharacteristicSubspace:

.. proof:definition:: 特征子空间

   定义: 设 :math:`T` 是线性空间 :math:`{\mathbb V}^n` 的线性变换, :math:`\lambda` 是 :math:`T` 的一个特征值, 称 :math:`{\mathbb V}^n` 的子空间 :math:`{\mathbb V}^n_{\lambda}` 是 :math:`T` 的属于 :math:`\lambda` 的 **特征子空间** (:term:`Characteristic Subspace`) , 其中

   .. math::
      {\mathbb V}^n_{\lambda} = \{ {\bm x} | T{\bm x} = \lambda {\bm x} , {\bm x} \in {\mathbb V}^n  \}.


.. hint::
   1. 特征子空间是线性子空间
   2. 特征子空间是由特征向量加上零向量构成的子空间.


什么是不变子空间
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _def-InvariantSubspace:

.. proof:definition:: 不变子空间

   若 :math:`T` 是线性空间 :math:`{\mathbb V}` 的线性变换, :math:`{\mathbb V}_1` 是 :math:`{\mathbb V}` 的子空间, 且 :math:`\forall {\bm x} \in {\mathbb V}_1` , 有 :math:`T{\bm x} \in {\mathbb V}_1` , 则称 :math:`{\mathbb V}_1` 是 :math:`T` 的 **不变子空间** (:term:`Invariant Subspace`).





信号子空间与噪声子空间
-----------------------------


在数字信号处理领域经常定义 **信号子空间** (:term:`Signal Subspace`) 与 **噪声子空间** (:term:`Noise Subspace`)








