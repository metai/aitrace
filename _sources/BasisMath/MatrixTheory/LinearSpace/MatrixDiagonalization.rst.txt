.. _Section-MatrixDiagonalization:

矩阵对角化
=====================


多项式矩阵及其标准形
---------------------

多项式矩阵
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _def-PolynomialMatrix:

.. proof:definition:: 多项式矩阵

   称如下矩阵为 **多项式矩阵** :

   .. math::
      {\bm{A}}(\lambda ) = \left[ {\begin{array}{cccc}
      {{a_{11}}(\lambda )}&{{a_{12}}(\lambda )}& \cdots &{{a_{1n}}(\lambda )}\\
      {{a_{21}}(\lambda )}&{{a_{22}}(\lambda )}& \cdots &{{a_{2n}}(\lambda )}\\
       \vdots & \vdots & \vdots & \vdots \\
      {{a_{n1}}(\lambda )}&{{a_{n2}}(\lambda )}& \cdots &{{a_{nn}}(\lambda )}
      \end{array}} \right]

   其中, :math:`a_{ij}(\lambda)` 为数域 :math:`K` 上的 :math:`\lambda` 的多项式. 易知数域上的 :math:`n` 阶矩阵  :math:`{\bm A}` 的特征矩阵是一个 **多项式矩阵** (:term:`Polynomial Matrix`) .


首一多项式
~~~~~~~~~~~~~~~~~~~~~~~~~~~

定义: 最高次数项为首项, 且首项系数是 :math:`1` 的多项式为 **首1多项式** .

如: :math:`\lambda^2 + 2\lambda` 是首 :math:`1` 多项式, :math:`2\lambda^2 + \lambda` 不是首一多项式.


.. note::

   定理: 矩阵 :math:`{\bm A}` 的最小多项式 :math:`m(\lambda)` 可以整除以 :math:`{\bm A}` 为根的任意首1多项式 :math:`\phi(\lambda)` , 即 :math:`m(\lambda)|\phi(\lambda)`
   定理: 矩阵 :math:`{\bm A}` 的最小多项式 :math:`m(\lambda)` 与其特征多项式 :math:`\varphi(\lambda)` 具有相同的零点(不计重数).


多项式矩阵的标准形
~~~~~~~~~~~~~~~~~~~~


多项式矩阵的标准形是指具有如下形式的多项式矩阵:

.. math::
   {\bm{A}}(\lambda ) = \left[ {\begin{array}{ccccccc}
   {{d_1}(\lambda )}&{}&{}&{}&{}&{}&{}\\
   {}&{{d_2}(\lambda )}&{}&{}&{}&{}&{}\\
   {}&{}& \ddots &{}&{}&{}&{}\\
   {}&{}&{}&{{d_s}(\lambda )}&{}&{}&{}\\
   {}&{}&{}&{}&0&{}&{}\\
   {}&{}&{}&{}&{}& \ddots &{}\\
   {}&{}&{}&{}&{}&{}&0
   \end{array}} \right]


其中, :math:`d_i(\lambda)` 是首一多项式, :math:`d_{i-1}(\lambda)` 可以整除 :math:`d_i(\lambda)`  , 记为 :math:`d_{i-1}(\lambda)|d_{i}(\lambda)` , :math:`i=1,2,\cdots,s, s\leq n` .



不变因子与初等因子
-------------------

对于多项式矩阵 :math:`{\bm A}(\lambda)` , 采用初等变换 (行列均可) 可以化为标准形.


不变因子
~~~~~~~~~~~~~~~~~~~~

多项式矩阵 :math:`{\bm A}(\lambda)` 的标准形式的对角线上的非零元素 :math:`d_i(\lambda), (i=1, 2, \cdots, s)` 不随初等变换而改变, 称之为多项式矩阵 :math:`{\bm A}(\lambda)` 的 **不变因子** 或 **不变因式** , 可由下式计算:

.. math::
   d_i(\lambda) = \frac{D_i(\lambda)}{D_{i-1}(\lambda)}, D_0(\lambda) = 1 (i=1,2,\cdots,s)

其中, :math:`D_i(\lambda)` 为多项式矩阵 :math:`{\bm A}(\lambda)` 的 *所有* :math:`i` 阶子式(行列式)的最大公因式, 也称为多项式矩阵 :math:`{\bm A}(\lambda)` 的 :math:`i` 阶行列式因子, 不随初等变换而改变.


初等因子
~~~~~~~~~~~~~~~~~~~~

把多项式矩阵 :math:`{\bm A}(\lambda)` 的的每个次数大于零的不变因子 :math:`d_i(\lambda)` 分解为不可约因式的乘积, 这些不可约因式及它们的幂指数称为 多项式矩阵 :math:`{\bm A}(\lambda)` 的一个 **初等因子** , 初等因子的全体称为多项式矩阵 :math:`{\bm A}(\lambda)` 的 **初等因子组** .


举例
~~~~~~~~~~~~~~~~

举例如下, 用以说明以上概念, 通过初等变换将多项式矩阵 :math:`{\bm A}()\lambda` 化为标准形:


.. math::
   \begin{array}{lll}
   {{\bm{A}}(\lambda ) = \left[ {\begin{array}{ccc}
   { - \lambda  + 1}&{2\lambda  - 1}&\lambda \\
   \lambda &{{\lambda ^2}}&{ - \lambda }\\
   {{\lambda ^2}{\rm{ + }}1}&{{\lambda ^2}{\rm{ + }}\lambda  - 1}&{ - {\lambda ^2}}
   \end{array}} \right]\mathop  \to \limits^{{c_1} + {c_3}} \left[ {\begin{array}{ccc}
   1&{2\lambda  - 1}&\lambda \\
   0&{{\lambda ^2}}&{ - \lambda }\\
   1&{{\lambda ^2}{\rm{ + }}\lambda  - 1}&{ - {\lambda ^2}}
   \end{array}} \right]}\\
   {\mathop  \to \limits^{{r_3} - {r_1}} \left[ {\begin{array}{ccc}
   1&{2\lambda  - 1}&\lambda \\
   0&{{\lambda ^2}}&{ - \lambda }\\
   0&{{\lambda ^2} - \lambda }&{ - {\lambda ^2} - \lambda }
   \end{array}} \right]\mathop  \to \limits^{\begin{array}{ccc}
   {{c_2} + (1 - 2\lambda ){c_1}}\\
   {{c_3} + ( - \lambda ){c_1}}
   \end{array}} \left[ {\begin{array}{ccc}
   1&0&0\\
   0&{{\lambda ^2}}&{ - \lambda }\\
   0&{{\lambda ^2} - \lambda }&{ - {\lambda ^2} - \lambda }
   \end{array}} \right]}\\
   {\mathop  \to \limits^{\begin{array}{ccc}
   {{c_2} + \lambda {c_3}}\\
   {{c_2} \leftrightarrow {c_3}}
   \end{array}} \left[ {\begin{array}{ccc}
   1&0&0\\
   0&{ - \lambda }&0\\
   0&{ - {\lambda ^2} - \lambda }&{ - {\lambda ^3} - \lambda }
   \end{array}} \right]\mathop  \to \limits^{{r_3} + ( - \lambda  - 1){r_2}} \left[ {\begin{array}{ccc}
   1&0&0\\
   0&{ - \lambda }&0\\
   0&0&{ - {\lambda ^3} - \lambda }
   \end{array}} \right]}\\
   {\mathop  \to \limits^{ - {r_2}, - {r_3}} \left[ {\begin{array}{ccc}
   1&0&0\\
   0&\lambda &0\\
   0&0&{{\lambda ^3}{\rm{ + }}\lambda }
   \end{array}} \right]}
   \end{array}


易知, :math:`d_1(\lambda) = 1` , :math:`d_2(\lambda) = \lambda` , :math:`d_3(\lambda) = \lambda^3 + \lambda` 为 :math:`{\bm A}(\lambda)` 的不变因子.

大于零的不变因子有 :math:`d_2(\lambda) = \lambda` , :math:`d_3(\lambda) = \lambda^3 + \lambda` ;

对于实数域, 它们分别可以分解为 :math:`\lambda` , :math:`\lambda(\lambda^2 + 1)` , 所以初等因子组为 :math:`\lambda, \lambda, \lambda^2+1` ;
对于复数域, 它们分别可以分解为 :math:`\lambda` , :math:`\lambda(\lambda + j)(\lambda - j)` , 所以初等因子组为 :math:`\lambda, \lambda, \lambda + j, \lambda - j` .



Jordan标准型
-------------------

对于 :math:`n` 阶矩阵 :math:`{\bm A}` , 存在可逆矩阵 :math:`{\bm P}` , 使得

.. math::
   {\bm P}^{-1}{\bm A}{\bm P} = {\bm J}.


概念与内涵
~~~~~~~~~~~

Jordan标准型是指具有如下形式的矩阵:

.. math::
   {\bm{J}}{\rm{ = }}{\left[ {\begin{array}{cccc}
   {{{\bm{J}}_1}({\lambda _1})}&{}&{}&{}\\
   {}&{{{\bm{J}}_{\bm{2}}}({\lambda _2})}&{}&{}\\
   {}&{}& \ddots &{}\\
   {}&{}&{}&{{{\bm{J}}_s}({\lambda _s})}
   \end{array}} \right]_{n \times n}},

其中, 每个Jordan标准形具有如下形式:

.. math::
   {{\bm{J}}_i}({\lambda _i}){\rm{ = }}{\left[ {\begin{array}{cccc}
   {{\lambda _i}}&1&{}&{}\\
   {}&{{\lambda _i}}& \ddots &{}\\
   {}&{}& \ddots &1\\
   {}&{}&{}&{{\lambda _i}}
   \end{array}} \right]_{{m_i} \times {m_i}}}.

Jordan标准形的对角元素为矩阵 :math:`{\bm A}` 的特征值.


求解方法
~~~~~~~~~~~~~~~~~

在复数域 :math:`\mathbb C` 上求解 :math:`n` 阶矩阵 :math:`{\bm A}` 的Jordan标准形的步骤如下:

#. 求特征矩阵的初等因子组, 记为 :math:`(\lambda-\lambda_1)^{m_1}, (\lambda-\lambda_2)^{m_2}, \cdots, (\lambda-\lambda_s)^{m_s}` , 其中 :math:`\lambda_i` 为矩阵 :math:`{\bm A}` 的特征值, 且可以相同, :math:`m_i` 为对于特征值 :math:`\lambda_i` 的特征值的重数, 也可相同;
#. 写出每个初等因子 :math:`(\lambda-\lambda_i)^{m_i}` , :math:`i=1,2,\cdots, s` 对应的Jordan块;
#. 写出以这些Jordan块构成的Jordan标准形.


举例
~~~~~~~~~~~~~


求如下矩阵的Jordan标准形:

.. math::
   {\bm{A}} = \left[ {\begin{array}{ccc}
   0&2&2\\
   2&1&2\\
   0&2&1
   \end{array}} \right]

1. 写出特征多项式矩阵, 并化简为标准形:

   .. math::
      \begin{array}{lll}
      {\left[ {\begin{array}{ccc}
      \lambda &{ - 2}&{ - 2}\\
      { - 2}&{\lambda  - 1}&{ - 2}\\
      0&{ - 2}&{\lambda  - 1}
      \end{array}} \right]\mathop  \to \limits^{2{r_1}} \left[ {\begin{array}{ccc}
      {2\lambda }&{ - 4}&{ - 4}\\
      { - 2}&{\lambda  - 1}&{ - 2}\\
      0&{ - 2}&{\lambda  - 1}
      \end{array}} \right]}\\
      {\mathop  \to \limits^{{r_1} + \lambda {r_2}} \left[ {\begin{array}{ccc}
      0&{\lambda (\lambda  - 1) - 4}&{ - 2\lambda  - 4}\\
      { - 2}&{\lambda  - 1}&{ - 2}\\
      0&{ - 2}&{\lambda  - 1}
      \end{array}} \right]}\\
      {\mathop  \to \limits^{} \left[ {\begin{array}{ccc}
      0&{\lambda (\lambda  - 1) - 4}&{ - 2\lambda  - 4}\\
      1&0&0\\
      0&{ - 2}&{\lambda  - 1}
      \end{array}} \right]}\\
      {\mathop  \to \limits^{2{c_3}} \left[ {\begin{array}{ccc}
      0&{\lambda (\lambda  - 1) - 4}&{ - 4\lambda  - 8}\\
      1&0&0\\
      0&{ - 2}&{2(\lambda  - 1)}
      \end{array}} \right]}\\
      {\mathop  \to \limits^{\begin{array}{ccc}
      {{c_3} + (\lambda  - 1){c_2}}\\
      {\;\;\;\; - \frac{1}{2}{r_3}}
      \end{array}} \left[ {\begin{array}{ccc}
      0&{\lambda (\lambda  - 1) - 4}&{{\lambda ^3} - 2{\lambda ^2} - 7\lambda  - 4}\\
      1&0&0\\
      0&1&0
      \end{array}} \right]}\\
      {\mathop  \to \limits^{{r_1} - [\lambda (\lambda  - 1) - 4]{r_3}} \left[ {\begin{array}{ccc}
      0&0&{{{(\lambda  + 1)}^2}(\lambda  - 4)}\\
      1&0&0\\
      0&1&0
      \end{array}} \right]}\\
      { = \left[ {\begin{array}{ccc}
      1&0&0\\
      0&1&0\\
      0&0&{{{(\lambda  + 1)}^2}(\lambda  - 4)}
      \end{array}} \right]}
      \end{array}

2. 初等因子组为 :math:`(\lambda+1)^2` , :math:`\lambda-4` , 它们对于的Jordan标准形为

   .. math::
      \left[ {\begin{array}{ccc}
      1&1\\
      {}&1
      \end{array}} \right],\;\left[ 4 \right]

3. 所求矩阵的Jordan标准形为

   .. math::
      \left[ {\begin{array}{ccc}
      4&{}&{}\\
      {}&{ - 1}&1\\
      {}&{}&{ - 1}
      \end{array}} \right]


.. hint::
   在进行因式分解时, 可以使用赋值数分解法, 假设有 :math:`m` 次多项式 :math:`f(\lambda)` , 代入 :math:`\lambda=a` , 有 :math:`f(a) = X` , 若 :math:`X` 可以分解为 :math:`m` 个数的乘积, 可以据此分解因式.

   如对 :math:`f(\lambda) = \lambda^3 -2\lambda^2 -7\lambda -4` , 有 :math:`f(1) = -12` , 而 :math:`-3\times 2\times 2 = -12` , 可猜想 :math:`f(\lambda) = (\lambda + a)(\lambda + b)(\lambda + c)` , :math:`a = -4, b=1, c=1` .

   在Matlab中进行因式分解很简单

   ::

      >> syms x
      >> y = x^3 - 2*x^2 - 7*x - 4
      >> factor(y)

         ans =

         [ x - 4, x + 1, x + 1]


在 Matlab 中可以很容易的实现Jordan标准形分解

::

   >> A = [0 2 2;2 1 2;0 2 1]
   >> jordan(A)

   ans =

        4     0     0
        0    -1     1
        0     0    -1



非奇异矩阵P的求法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

求矩阵 :math:`{\bm A}` 的特征值与特征向量/广义特征向量, 将特征向量和广义特征向量组成矩阵 :math:`{\bm P}` , 即可.


以 :ref:`Example-EigenValues` 为例, 求矩阵 :math:`{\bm P}` , 使得矩阵 :math:`{\bm A}` 与对角矩阵 :math:`{\bm J}` 相似.

解: 依据 :ref:`Example-EigenValues` 的求解步骤求出矩阵 :math:`{\bm A}` 的特征值为 :math:`\lambda_1 = 4, \lambda_2 = \lambda_3 = -1` ,对应于 :math:`\lambda_1` 的特征向量 :math:`{\bm x}_1 = (5, 6, 4)^T`  , 对应于 :math:`\lambda_2 = \lambda_3 = -1` 的特征向量和广义特征向量 :math:`{\bm x}_2 = (0, 1, -1)^T` , :math:`{\bm x}_3 = (1, -1, 1/2)^T` .

所以取

.. math::
   {\bm P} = \left[ {\begin{array}{ccc}
   5&0&1\\
   6&1& - \\
   4&{-1}&{1{\rm{/}}2}
   \end{array}1} \right]


可以验证 :math:`{\bm P}^{-1}{\bm A}{\bm P} = {\bm J}.`

matlab代码验证如下::

   >> A=[0 2 2;2 1 2;0 2 1]

   A =

        0     2     2
        2     1     2
        0     2     1

   >> P=[5 6 4;0 1 -1;1 -1 1/2]'

   P =

       5.0000         0    1.0000
       6.0000    1.0000   -1.0000
       4.0000   -1.0000    0.5000

   >> inv(P)*A*P

   ans =

       4.0000   -0.0000    0.0000
      -0.0000   -1.0000    1.0000
       0.0000         0   -1.0000

   >> % [1 -1 1/2] --> [2 -2 1]
   >> P=[5 6 4;0 1 -1;2 -2 1]'

   P =

       5.0000         0    2.0000
       6.0000    1.0000   -2.0000
       4.0000   -1.0000    1.0000

   >> inv(P)*A*P

   ans =

       4.0000   -0.0000    0.0000
      -0.0000   -1.0000    2.0000
       0.0000         0   -1.0000




Jordan标准型求解微分线性方程组
--------------------------------



计算步骤
~~~~~~~~~~~

#. 将微分线性方程组写成矩阵形式 :math:`\frac{{\rm d}{\bm x}}{{\rm d}t} = {\bm A}{\bm x}` ;
#. 求解矩阵 :math:`{\bm A}` 的特征值和广义特征向量, 组成矩阵 :math:`{\bm P}` 和Jordan标准形;
#. 进行非奇异线性变换 :math:`{\bm x} = {\bm P}{\bm y} \Rightarrow \frac{{\rm d}{\bm x}}{{\rm d}t} = {\bm P}\frac{{\rm d}{\bm y}}{{\rm d}t}` , 从而 :math:`\frac{{\rm d}{\bm y}}{{\rm d}t} = {\bm P}^{-1}\frac{{\rm d}{\bm x}}{{\rm d}t} = {\bm P}^{-1}{\bm A}{\bm P}{\bm y}` ;
#. 由 :math:`\frac{{\rm d}{\bm y}}{{\rm d}t} = {\bm J}{\bm y}` 求解出一般解;
#. 再由 :math:`{\bm x} = {\bm P}{\bm y}` 求解出原微分方程的一般解.


举例
~~~~~~~~~~~

求解如下微分线性方程组的通解

.. math::
   \left\{ {\begin{array}{lll}
   {\frac{{{\rm{d}}{x_1}}}{{{\rm{d}}t}} = 2{x_2} + 2{x_3}}\\
   {\frac{{{\rm{d}}{x_2}}}{{{\rm{d}}t}} = 2{x_1} + {x_2} + 2{x_3}}\\
   {\frac{{{\rm{d}}{x_3}}}{{{\rm{d}}t}} = 2{x_2} + {x_3}}
   \end{array}} \right.


解:

1. 写成矩阵形式 :math:`\frac{{\rm d}{\bm x}}{{\rm d}t} = {\bm A}{\bm x}` , 其中

   .. math::
      {\bm{A}} = \left[ {\begin{array}{ccc}
      0&2&2\\
      2&1&2\\
      0&2&1
      \end{array}} \right]

2. 求解矩阵 :math:`{\bm A}` 的特征值与广义特征向量与 :math:`{\bm P}`

   由 :ref:`Example-EigenValues` 知其特征值为 :math:`\lambda_1 = 4, \lambda_2 = \lambda_3 = -1` ,对应于 :math:`\lambda_1` 的特征向量 :math:`{\bm x}_1 = (5, 6, 4)^T`  , 对应于 :math:`\lambda_2 = \lambda_3 = -1` 的广义特征向量 :math:`{\bm x}_2 = (0, 1, -1)^T` , :math:`{\bm x}_3 = (2, -2, 1)^T` .

   所以取

   .. math::
      {\bm P} = \left[ {\begin{array}{ccc}
      5&0&1\\
      6&1& - \\
      4&{-1}&{1{\rm{/}}2}
      \end{array}1} \right]

3. 由 :math:`{\bm P}^{-1}{\bm A}{\bm P}` 或者初等因子组求解出Jordan标准形

   .. math::
      {\bm J} = \left[ {\begin{array}{ccc}
      4&{}&{}\\
      {}&{ - 1}&1\\
      {}&{}&{ - 1}
      \end{array}} \right]

4. 求解 :math:`\frac{{\rm d}{\bm y}}{{\rm d}t} = {\bm J}{\bm y}` 一般解

.. math::
   \left\{ {\begin{array}{lll}
   {\frac{{{\rm{d}}{y_1}}}{{{\rm{d}}t}} = 4{y_1}}\\
   {\frac{{{\rm{d}}{y_2}}}{{{\rm{d}}t}} =  - {y_2} + {y_3}}\\
   {\frac{{{\rm{d}}{y_3}}}{{{\rm{d}}t}} =  - {y_3}}
   \end{array}} \right.\;\; \Rightarrow \left\{ {\begin{array}{lll}
   {{y_1} = {c_1}{e^{4t}}}\\
   {\frac{{{\rm{d}}{y_2}}}{{{\rm{d}}t}} =  - {y_2} + {c_3}{e^{ - t}}}\\
   {{y_3} = {c_3}{e^{ - t}}}
   \end{array}} \right. \Rightarrow \left\{ {\begin{array}{lll}
   {{y_1} = {c_1}{e^{4t}}}\\
   {{y_2} = {c_2}{e^{ - t}} + {c_3}t{e^{ - t}}}\\
   {{y_3} = {c_3}{e^{ - t}}}
   \end{array}} \right.

5. 由 :math:`{\bm x} = {\bm P}{\bm y}`  知

.. math::
   {\bm{x}} = {\bm{Py}} = \left[ {\begin{array}{ccc}
   5&0&1\\
   6&1& - \\
   4&{ - 1}&{1{\rm{/}}2}
   \end{array}1} \right]\left[ {\begin{array}{ccc}
   {{y_1}}\\
   {{y_2}}\\
   {{y_3}}
   \end{array}} \right]

.. math::
    \Rightarrow \left\{ {\begin{array}{lll}
   {{x_1} = 5{y_1} + {y_3}}\\
   {{x_2} = 6{y_1} + {y_2} - {y_3}}\\
   {{x_3} = 4{y_1} - {y_2} + {y_3}/2}
   \end{array}} \right. \Rightarrow \left\{ {\begin{array}{lll}
   {{x_1} = 5{c_1}{e^{4t}} + {c_3}{e^{ - t}}}\\
   {{x_2} = 6{c_1}{e^{4t}} + {c_2}{e^{ - t}} + {c_3}t{e^{ - t}} - {c_3}{e^{ - t}}}\\
   {{x_3} = 4{c_1}{e^{4t}} - {c_2}{e^{ - t}} - {c_3}t{e^{ - t}} + {c_3}{e^{ - t}}/2}
   \end{array}} \right.

.. hint::
   在Matlab中可以使用 ``dsolve`` 函数求解微分方程组, 如对于 :math:`\frac{{\rm d}\bm x}{{\rm d}t} = -{\bm x}`

   ::

      >> syms x(t)
         Dx = diff(x);
         dsolve(diff(Dx) == -x, Dx(0) == 1)

         ans =

         sin(t) + C3*cos(t)


总结
------------------

可对角化
~~~~~~~~~~~~~

#. 互不相同的特征值对于的特征向量线性无关
#. :math:`n` 阶矩阵 :math:`{\bm A}` 有 :math:`n` 个线性无关的特征向量 :math:`\Leftrightarrow` :math:`{\bm A}` 与对角阵相似
#. :math:`n` 阶矩阵 :math:`{\bm A}` 有 :math:`n` 个互不相同的特征值 :math:`\Leftrightarrow` :math:`{\bm A}` 与对角阵相似
#. :math:`n` 阶矩阵 :math:`{\bm A}` 的秩为 :math:`n`  :math:`\Leftrightarrow` :math:`{\bm A}` 与对角阵相似

