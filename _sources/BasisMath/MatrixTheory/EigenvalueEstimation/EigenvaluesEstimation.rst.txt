.. _Section-EigenvalueEstimation:

特征值估计
=====================

特征值的界
-----------------

定理1: 设 :math:`{\bm A} = (a_{ij})_{n\times n} \in {\mathbb R}^{n\times n}` , 令 :math:`M = \mathop {{\rm{max}}}\limits_{1 \le i,j \le n} \frac{1}{2}|{a_{ij}} - {a_{ji}}|` , 若 :math:`\lambda` 表示 :math:`{\bm A}` 的任一特征值, 则 :math:`\lambda` 的虚部 :math:`{\rm Im}(\lambda)` 满足不等式

.. math::
   |{Im(\lambda)}| \leq M\sqrt{\frac{n(n-1)}{2}}.


定理2: 设 :math:`{\bm A}\in {\mathbb C}^{n\times n}` , 则 :math:`{\bm A}` 的任一特征值 :math:`\lambda` 满足

.. math::
   |\lambda| \leq \|{\bm A}\|_{m_{\infty}}, \\
   |{\rm Re}(\lambda)| \leq \frac{1}{2}\|{\bm A} + {\bm A}^H\|_{m_{\infty}},  \\
   |{\rm Im}(\lambda)| \leq \frac{1}{2}\|{\bm A} - {\bm A}^H\|_{m_{\infty}} .

定理3: 设 :math:`{\bm A} = (a_{ij})_{n\times n} \in {\mathbb C}^{n\times n}` 的特征值为 :math:`\lambda_1, \lambda_2, \cdots, \lambda_n` , 则

.. math::
   \sum_{i=1}^n{ |\lambda_i|^2 \leq \sum_{i,j=1}^n{|a_{ij}|^2} = \|{\bm A}\|_F^2 } ,

当且仅当 :math:`{\bm A}^H {\bm A} = {\bm A}{\bm A}^H` 时, 等号成立.




特征值的包含区域
-----------------------

盖尔圆
~~~~~~~~~~~~~~

什么是盖尔圆
^^^^^^^^^^^


.. _def-Gerschgorin:

.. proof:definition:: 盖尔圆(一般教材定义)

   设 :math:`{\bm A} = (a_{ij})_{n\times n} \in {\mathbb C}^{n\times n}` , 称不等式

   .. math::
      |z - a_{ii}| \leq R_i  , R_i = R_i({\bm A}) = \sum_{j=1,j\neq i}^n |a_{ij}|

   在复平面上所确定的区域为矩阵 :math:`{\bm A}` 的第 :math:`i` 个 **盖尔圆 (Gerschgorin)** , 记为 :math:`G_i` , :math:`{\bm R}_i` 为不包括 :math:`a_{ii}` 的行和, 称为盖尔圆 :math:`G_i` , :math:`(i = 1, 2, \cdots, n)` 的半径.

.. _def-GerschgorinZhi:

.. proof:definition:: 盖尔圆(我的定义)

   实际上, 在上述定义中, 若令半径为

   .. math::
      |z - {a_{ii}}| \le {R_i},{R_i} = {R_i}({\bm{A}}) = \min \left( {\sum\limits_{j = 1,j \ne i}^n | {a_{ij}}|{\rm{,}}\;\sum\limits_{i = 1,i \ne j}^n | {a_{ij}}|} \right)

   显然确定特征值范围会变得更为简单, 不知道为什么不这样定义.

.. note::

    半径 :math:`R_i` 也可以按列求和得到, 这是因为 :math:`{\bm A}` 与 :math:`{\bm A}^T` 的特征值相同.


定理与结论
^^^^^^^^^^^

- 盖尔圆定理1: 矩阵 :math:`{\bm A} = (a_{ij})_{n\times n} \in {\mathbb C}^{n\times n}` 的一切特征值都在它的 :math:`n` 个盖尔圆的并集内.

- 盖尔圆定理2: 矩阵 :math:`{\bm A} = (a_{ij})_{n\times n} \in {\mathbb C}^{n\times n}` 的联通部分由几个盖尔圆组成, 该部分就包含几个特征值 (盖尔圆相重时重复计数, 特征值相同时重复计数).

.. note::

   结论:

   - 若矩阵 :math:`{\bm A}` 的盖尔圆 :math:`G_i` 关于实轴对称, 则特征值 :math:`\lambda_i` 为实数.

   - 若矩阵 :math:`{\bm A}` 的盖尔圆 :math:`G_i` 各自孤立不连通, 则 :math:`{\bm A}` 有 :math:`n` 个互不相同的特征值.


特征值的隔离问题
^^^^^^^^^^^^^^^^^^^^^^^^^

设矩阵 :math:`{\bm A} = (a_{ij})_{n\times n} \in {\mathbb C}^{n\times n}` , 构造对角矩阵 :math:`{\bm D} = {\rm diag}(d_1, d_2, \cdots, d_n)` , 其中 :math:`d_i > 0, i = 1, 2, \cdots, n` , 由于矩阵

.. math::
   {\bm B} = {\bm D}{\bm A}{\bm D}^{-1} = \left(\frac{d_i}{d_j}a_{ij}\right)_{n\times n}

相似于 :math:`{\bm A}` , 所以矩阵 :math:`{\bm B}, {\bm A}` 的特征值集合相同.

.. hint::

   - 取 :math:`d_i < 1, d_k = 1, k \neq i` , 可使第 :math:`i` 个盖尔圆的半径减小

   - 取 :math:`d_i > 1, d_k = 1, k \neq i` , 可使第 :math:`i` 个盖尔圆的半径增大


举个例子

应用盖尔圆定理隔离如下矩阵的特征值

.. math::
   {\bm{A}} = \left[ {\begin{array}{ccc}
               {20}&3&1\\
               2&{10}&2\\
               8&1&0
               \end{array}} \right]

解: 矩阵 :math:`{\bm A}` 的三个盖尔圆为 :math:`G_1: |z-20| \leq 4` , :math:`G_2: |z-10| \leq 4` , :math:`G_3: |z-0| \leq 9` , 如图所示

易知盖尔圆 :math:`G_2, G_3` 相交, :math:`G_1` 孤立, 构造矩阵 :math:`D = {\rm diag}(1, 1, 1/2)` 使得 :math:`G_3` 的半径减小, 则有

.. math::
   {\bm{B}}{\rm{ = }}{\bm{DA}}{{\bm{D}}^{ - 1}} = \left[ {\begin{array}{ccc}
   1&{}&{}\\
   {}&1&{}\\
   {}&{}&{1/2}
   \end{array}} \right]\left[ {\begin{array}{ccc}
   {20}&3&1\\
   2&{10}&2\\
   8&1&0
   \end{array}} \right]\left[ {\begin{array}{ccc}
   1&{}&{}\\
   {}&1&{}\\
   {}&{}&2
   \end{array}} \right] = \left[ {\begin{array}{ccc}
   {20}&3&1\\
   2&{10}&4\\
   4&{1/2}&0
   \end{array}} \right]

矩阵 :math:`{\bm B}^T` 的三个盖尔圆为 :math:`G_1: |z-20| \leq 4` , :math:`G_2: |z-10| \leq 4` , :math:`G_3: |z-0| \leq 9` , 如 :figure:numref:`fig-demo_Gerschgorin_exp1` 所示, 它们相互孤立,


.. _fig-demo_Gerschgorin_exp1:

.. figure:: ../../../_static/figs/BasisMath/MatrixTheory/EigenvalueEstimation/demo_Gerschgorin_exp1.png
   :scale: 80 %
   :alt: Gerschgorin
   :align: center

   矩阵 :math:`{\bm A}, {\bm A}^T, {\bm B}^T`  的盖尔圆

   矩阵 :math:`{\bm A}, {\bm A}^T, {\bm B}^T`  的盖尔圆示意图.

实际上若采用盖尔圆定义2, 可以很容易得到 :figure:numref:`fig-demo_Gerschgorin` 所示结果

.. _fig-demo_Gerschgorin_exp1:

.. figure:: ../../../_static/figs/BasisMath/MatrixTheory/EigenvalueEstimation/demo_Gerschgorin.png
   :scale: 80 %
   :alt: Gerschgorin
   :align: center

   矩阵 :math:`{\bm A}` 的盖尔圆

   矩阵 :math:`{\bm A}` 的盖尔圆示意图, 每个盖尔圆的半径取为元素所在行元素和, 与元素所在列元素和中最小的那个.

上述结果实验代码为

.. literalinclude:: ../../../_static/src/python/BasisMath/MatrixTheory/EngenvalueEstimation/demo_Gerschgorin.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 13-15
   :linenos:
   :caption: demo_Gerschgorin.py



应用
^^^^^^^^^^^^^^^^^^


- 判定矩阵是否可逆: 矩阵的行列式的值等于矩阵特征值的乘积, 由于行列式不为零的矩阵可逆, 所以可逆矩阵的特征值不等于零, 借助盖尔圆判定特征值的取值





