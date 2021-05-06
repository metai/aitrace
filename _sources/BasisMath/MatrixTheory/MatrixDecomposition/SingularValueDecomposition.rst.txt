.. _Section-SingularValueDecomposition:

奇异值分解
=============


概念
----------

矩阵的奇异值
~~~~~~~~~~~~~

.. _def-SingularValue:

.. proof:definition:: 奇异值

    设 :math:`{\bm A}\in{\mathbb C}_r^{m\times n} (r>0)` , :math:`{\bm A}^H{\bm A}` 的特征值为

    .. math::
       \lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_r \ge \lambda_{r+1} = \cdots = \lambda_n = 0

    则称 :math:`\sigma_i = \sqrt{\lambda_i}, (i=1, 2, \cdots, n)` 为 :math:`{\bm A}` 的 **奇异值** (:term:`Singular Value`); 当矩阵 :math:`{\bm A}` 为零矩阵时, 奇异值全为零.

- :math:`{\bm A}` 的奇异值的个数等于 :math:`{\bm A}` 的列数;
- :math:`{\bm A}` 的非零奇异值的个数等于 :math:`{\bm A}` 的秩;

.. _theo-TheoremSingularValueDiagonalization:

.. proof:theorem:: 奇异值对角化定理

    设 :math:`{\bm A}\in{\mathbb C}_r^{m\times n} (r>0)` , 则存在 :math:`m` 阶酉矩阵 :math:`{\bm U}` 和 :math:`n` 阶酉矩阵 :math:`{\bm V}` , 使得

    .. math::
       {\bm U}^H{\bm A}{\bm V} = \left[ {\begin{array}{lll}
                                              {\bm{\Sigma }}&{\bm{O}}\\
                                              {\bm{O}}&{\bm{O}}
                                              \end{array}} \right]

    其中, :math:`{\bm \Sigma} = {\rm diag}(\sigma_1, \sigma_2, \cdots, \sigma_r)` , :math:`\sigma_i (i=1, 2, \cdots, r)` 为矩阵 :math:`{\bm A}` 的全部非零特征值.


奇异值分解
~~~~~~~~~~~~~~

奇异值分解 ( :term:`Singular Value Decomposition` ) 是把一个矩阵 :math:`{\bm A}_{m \times n}` 分解为一个酉矩阵 ( unitary matrix) :math:`{\bm U}_{m\times m}` , 矩形对角矩阵 :math:`{\bm S}_{m\times n}` 与一个酉矩阵 :math:`{\bm V}_{n\times n}` 共轭转置乘积的分解.


.. _def-SingularValueDecomposition:

.. proof:definition:: 奇异值分解

    称满足如下形式的矩阵分解为 **奇异值分解** :

    .. math::
          {\bm A}_{m \times n} = {\bm U}_{m\times m} {\bm S}_{m\times n} {\bm V}_{n\times n}^H

    其中, :math:`{\bm S}_{m\times n} = \left[ {\begin{array}{lll} {\bm{\Sigma }}_{r\times r}&{\bm{O}}_{r\times (n-r)}\\ {\bm{O}}_{(m-r)\times r}&{\bm{O}}_{(m-r)\times(n-r)} \end{array}} \right]` .


:figure:numref:`fig-Singular-Value-Decomposition` 所示为奇异值分解示意图.

.. _fig-Singular-Value-Decomposition:

.. figure:: ../../../_static/figs/BasisMath/MatrixTheory/MatrixDecomposition/SVD/Singular-Value-Decomposition.png
   :scale: 50 %
   :alt: Singular Value Decomposition
   :align: center

   奇异值分解示意图

   奇异值分解示意图



.. hint::

   - 矩阵 :math:`{\bm A}` 的奇异值由 :math:`{\bm A}` 唯一确定;
   - 矩阵 :math:`{\bm A}` 的奇异值分解不唯一, 因为 :math:`{\bm U, V}` 一般不唯一;
   - 矩阵 :math:`{\bm U}` 是 :math:`{\bm A}{\bm A}^H` 的特征向量
   - 矩阵 :math:`{\bm V}` 是 :math:`{\bm A}^H{\bm A}` 的特征向量

.. note::
   奇异值分解证明



求解方法
---------------

设有矩阵 :math:`{\bm A}\in{\mathbb C}_r^{m\times n} (r>0)` , 求其奇异值分解的步骤如下:

#. 计算矩阵 :math:`{\bm A}^H{\bm A}` 及其特征值和特征向量, 秩 :math:`r` ;
#. 根据特征值 :math:`\lambda_i` , 求奇异值 :math:`\sigma_i` , 并写出矩阵 :math:`{\bm \Sigma}_{r}\times{r}` 及矩形对角阵 :math:`{\bm S}_{m \times n}` ;
#. 根据特征向量, 标准化特征向量并将特征向量按列依奇异值顺序排成矩阵 :math:`{\bm V}` , 取前 :math:`r` 列构成 :math:`{\bm V}_1`  ;
#. 根据 :math:`{\bm U}_1 = {\bm A}{\bm V}_1{\bm{\Sigma}}^{-1}` 计算 :math:`{\bm U}_1` ;
#. 取与 :math:`{\bm U}_1` 正交的矩阵 :math:`{\bm U}_2` , 合并得到 :math:`{\bm U} = [{\bm U}_1 | {\bm U}_2]` ;
#. 最终求得矩阵 :math:`{\bm A}` 的奇异值分解 :math:`{\bm A} = {\bm U} {\bm S} {\bm V}^H` .


实例
~~~~~~~~~~

求如下矩阵的 SVD分解

.. math::
   {\bm A} = \left[ {\begin{array}{ccc}
   { - 1}&0\\
   0&1\\
   2&2
   \end{array}} \right]

解: 由题意有

.. math::
   {{\bm{A}}^H}{\bm{A}} = \left[ {\begin{array}{ccc}
   { - 1}&0&2\\
   0&1&2
   \end{array}} \right]\left[ {\begin{array}{ccc}
   { - 1}&0\\
   0&1\\
   2&2
   \end{array}} \right] = \left[ {\begin{array}{ccc}
   5&4\\
   4&5
   \end{array}} \right]

#. 求得 :math:`{{\bm{A}}^H}{\bm{A}}` 特征值与特征向量分别为 :math:`\lambda_1 = 9, \lambda_2 = 1` , 对应特征向量 :math:`{\bm x}_1 = (1, -1)^T` , :math:`{\bm x}_2 = (1, 1)^T`

#. 从而有奇异值 :math:`\sigma_1 = 3, \sigma_2 = 1` , 于是有

   .. math::
      {\bm{\Sigma }} = \left[ {\begin{array}{ccc}
      {{\sigma _1}}&{}\\
      {}&{{\sigma _2}}
      \end{array}} \right],\;\;{\bm{S}} = \left[ {\begin{array}{ccc}
      {{\sigma _1}}&0\\
      0&{{\sigma _2}}\\
      0&0
      \end{array}} \right] = \left[ {\begin{array}{ccc}
      3&0\\
      0&1\\
      0&0
      \end{array}} \right]

#. 根据特征向量, 标准化特征向量并将特征向量按列依奇异值顺序排成矩阵, 由于秩 :math:`r = 2` , 所以

   .. math::
      {\bm V}_1 = {\bm V} = \left[ {\begin{array}{ccc}
      {\frac{1}{{\sqrt 2 }}}&{\frac{1}{{\sqrt 2 }}}\\
      {\frac{1}{{\sqrt 2 }}}&{\frac{{ - 1}}{{\sqrt 2 }}}
      \end{array}} \right]

#. 根据 :math:`{\bm U}_1 = {\bm A}{\bm V}_1{\bm{\Sigma}}^{-1}` 计算 :math:`{\bm U}_1`

   .. math::
      {\bm U}_1 = {\bm A}{\bm V}{\bm{\Sigma}}^{-1}
      = \left[ {\begin{array}{ccc}
         { - 1}&0\\
         0&1\\
         2&2
         \end{array}} \right]\left[ {\begin{array}{ccc}
         {\frac{1}{{\sqrt 2 }}}&{\frac{1}{{\sqrt 2 }}}\\
         {\frac{1}{{\sqrt 2 }}}&{\frac{{ - 1}}{{\sqrt 2 }}}
         \end{array}} \right]{\left[ {\begin{array}{ccc}
         3&0\\
         0&1
         \end{array}} \right]^{ - 1}} = \left[ {\begin{array}{ccc}
         {\frac{{ - 1}}{{3\sqrt 2 }}}&{\frac{{ - 1}}{{\sqrt 2 }}}\\
         {\frac{1}{{3\sqrt 2 }}}&{\frac{{ - 1}}{{\sqrt 2 }}}\\
         {\frac{4}{{3\sqrt 2 }}}&0
         \end{array}} \right]

#. 取与 :math:`{\bm U}_1` 正交的矩阵 :math:`{\bm U}_2` , 合并得到 :math:`{\bm U} = [{\bm U}_1 | {\bm U}_2]`

   .. math::
      {{\bm{U}}_2} = \left[ {\begin{array}{ccc}
      {\frac{2}{3}}\\
      {\frac{{ - 2}}{3}}\\
      {\frac{1}{3}}
      \end{array}} \right],\;{\bm{U}} = \left[ {\begin{array}{ccc}
      {\frac{{ - 1}}{{3\sqrt 2 }}}&{\frac{{ - 1}}{{\sqrt 2 }}}&{\frac{2}{3}}\\
      {\frac{1}{{3\sqrt 2 }}}&{\frac{{ - 1}}{{\sqrt 2 }}}&{\frac{{ - 2}}{3}}\\
      {\frac{4}{{3\sqrt 2 }}}&0&{\frac{1}{3}}
      \end{array}} \right]

#. 最终求得矩阵 :math:`{\bm A}` 的奇异值分解 :math:`{\bm A} = {\bm U} {\bm S} {\bm V}^H` .

代码实现
~~~~~~~~~~~~

matlab代码

.. code-block:: matlab
   :emphasize-lines: 9
   :linenos:
   :caption: demo_svd.m
   :name: bind-id

   >> A=[-1 0;0 1;2 2]

   A =

       -1     0
        0     1
        2     2

   >> [U, S, V]=svd(A)

   U =

      -0.2357   -0.7071    0.6667
       0.2357   -0.7071   -0.6667
       0.9428   -0.0000    0.3333


   S =

       3.0000         0
            0    1.0000
            0         0


   V =

       0.7071    0.7071
       0.7071   -0.7071


例子2

.. code-block:: matlab
   :emphasize-lines: 9
   :linenos:
   :name: bind-id

   >> A=[1 0 1;0 1 1; 0 0 0]

   A =

        1     0     1
        0     1     1
        0     0     0

   >> [U, S, V]=svd(A)

   U =

       0.7071   -0.7071         0
       0.7071    0.7071         0
            0         0    1.0000


   S =

       1.7321         0         0
            0    1.0000         0
            0         0         0


   V =

       0.4082   -0.7071    0.5774
       0.4082    0.7071    0.5774
       0.8165    0.0000   -0.5774

   >> U*S*V

   ans =

       0.2113   -1.3660    0.2989
       0.7887   -0.3660    1.1154
            0         0         0

   >> U*S*V'

   ans =

       1.0000   -0.0000    1.0000
       0.0000    1.0000    1.0000
            0         0         0


奇异值分解应用
-----------------------

http://en.volupedia.org/wiki/Singular_value_decomposition

SVD与谱分解
~~~~~~~~~~~~~~~~~~~~




