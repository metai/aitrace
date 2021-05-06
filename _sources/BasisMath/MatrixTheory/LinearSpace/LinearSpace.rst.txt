.. _Section-LinearSpace:

线性空间
========

基础概念
--------


域
~~~~~~~

-  域: 一种集合
-  数域: 满足四则运算封闭
-  事件域: 满足交并补运算封闭

映射
~~~~~~~

-  像: 映射后, 相当于因变量
-  原像: 映射前, 相当于自变量
-  相等: 变换后相同, \ :math:`\sigma_1`, :math:`\sigma_2`
   是集合\ :math:`S_1`\ 到\ :math:`S_2`\ 的映射, 若
   :math:`\forall a \in S_1`\ , 有\ :math:`\sigma_1(a) = \sigma_2(a)`\ , 则
   :math:`\sigma_1 = \sigma_2`
-  乘积: 设 :math:`\sigma`, :math:`\tau` 分别为 :math:`S` 到
   :math:`S_1`\ , \ :math:`S_1`\ 到\ :math:`S_2`\ 的映射, 则映射的乘积定义为
   :math:`(\tau\sigma)(a) = \tau(\sigma(a))`


线性空间概念及性质
-----------------

定义
~~~~~~~

涉及一个集合和一个数域, 五种运算, 分别为:

-  集合内

   -  加法(元素的加法): :math:`\oplus`

-  数域内

   -  加法(数的加法): :math:`+`
   -  乘法(数的乘法): :math:`\times` 或省略

-  集合与数域间

   -  乘法(数乘): :math:`\odot`


.. _def-LinearSpace:

.. proof:definition:: 线性空间

   给定数域 :math:`{\mathbb K}`, 非空集合 :math:`{\mathbb V}`,
   定义集合内的加法运算（\ :math:`\oplus`\ ）和数域与集合间的数乘运算（\ :math:`\odot`\ ）,
   若满足以下条件, 则称 :math:`{\mathbb V}` 是数域 :math:`{\mathbb K}` 上的 **线性空间** ( :term:`Linear Space` ) .

   #. 运算封闭性:

      *  加法封闭性: 对 :math:`\forall {\bm x}, {\bm y} \in {\mathbb V}`\ , 有唯一的和 :math:`{\bm x} \oplus {\bm y} ∈ {\mathbb V}`
      *  数乘封闭性: 对 :math:`\forall k \in {\mathbb K}, \forall {\bm x} \in {\mathbb V}`, 有唯一的元素 :math:`\forall k {\bm x} \in {\mathbb V}`

   #. 交换律: \ :math:`{\bm x} \oplus {\bm y} = {\bm y} \oplus {\bm x}`

   #. 结合律: \ :math:`({\bm x} \oplus {\bm y}) \oplus {\bm z} = {\bm x} \oplus ({\bm y} \oplus {\bm z})`

   #. 有零元: \ :math:`\forall {\bm x} \in {\mathbb V}, \exists {\bm 0} \in {\mathbb V}` 使得 :math:`{\bm x} \oplus {\bm 0} = {\bm x}`

   #. 有负元: \ :math:`\forall {\bm x} \in {\mathbb V}, \exists {\bm y} \in {\mathbb V}` 使得 :math:`{\bm x} \oplus {\bm y} = {\bm 0}`

   #. 乘1律: \ :math:`1 \odot {\bm x} = {\bm x}`
   #. 数因子分配律: \ :math:`k \odot (\bm{x} + \bm{y}) = k \odot {\bm x} + k \odot {\bm y}`
   #. 数乘分配律: \ :math:`(k+l) \odot {\bm x} = k \odot {\bm x} + l \odot {\bm x}`
   #. 数乘结合律: \ :math:`k \odot (l \odot {\bm x}) = (kl) \odot {\bm x}`


性质
~~~~~

:math:`\forall {\bm x} \in {\mathbb V}, 0,1\in {\mathbb K}`, 有:

1. :math:`0 \odot {\bm x} = {\bm 0}`\ : 数 :math:`0`
   乘以 :math:`{\mathbb V}` 中任意元素 :math:`{\bm x}` 的结果为 :math:`{\mathbb V}` 中零元素
   :math:`{\bm 0}`
2. :math:`1 \odot {\bm x} = {\bm x}`\ : 数 :math:`1`
   乘以 :math:`{\mathbb V}` 中任意元素 :math:`{\bm x}` 的结果仍为元素
   :math:`{\bm x}`
3. :math:`-1 \odot {\bm x} = - {\bm x}`\ : 数 :math:`-1`
   乘以 :math:`{\mathbb V}` 中任意元素 :math:`{\bm x}`
   的结果为\ :math:`{\bm x}`\ 的负元素 :math:`-{\bm x}`


.. note::

   - :math:`(0 \odot {\bm x}) \oplus {\bm x} = (0 + 1) \odot {\bm x} = {\bm x}`     :math:`\Longrightarrow`     :math:`0 \odot {\bm x} = {\bm 0}`
   - :math:`(-1 \odot {\bm x}) \oplus {\bm x} = (-1 + 1) \odot {\bm x} = {\bm x} = 0 \odot {\bm x} = {\bm 0}`     :math:`\Longrightarrow`    :math:`-1 \odot {\bm x}` 为 :math:`{\bm x}` 的负元素
   - :math:`k \odot ({\bm x} \oplus (-1\odot{\bm x})) = k\odot {\bm x} \oplus k \odot (- {\bm x}) = k \odot {\bm x} \oplus (-1)\odot(k\odot {\bm x}) = {\bm 0}`


线性组合与线性表示
~~~~~~~~~~~~~~~~~~

.. _def-LinearCombination:

.. proof:definition:: 线性组合

   设 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_m` 为线性空间 :math:`{\mathbb V}` 中的 :math:`m` 个元素, :math:`{\bm x} \in {\mathbb V}` , 若存在数 :math:`c_1, c_2, \cdots, c_m \in {\mathbb K}` , 使

   .. math::
      {\bm x} = c_1 \odot {\bm x}_1 \oplus c_2 \odot {\bm x}_2 \oplus \cdots \oplus c_m \odot {\bm x}_m

   则称 :math:`{\bm x}` 为 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_m` 的 **线性组合** (:term:`Linear Combination`), 也称 :math:`{\bm x}` 可由 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_m` **线性表示** (:term:`Linear Representation`).


.. note::
   对比稀疏表示, 字典学习:

   - 原子可看作上述向量;

   - 字典可看作上述向量组;

   - 稀疏表示系数就是上述线性组合系数.


线性相关与线性无关
~~~~~~~~~~~~~~~~~~

.. _def-LinearlyDependent:

.. proof:definition:: 线性无关

   设 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_m` 为线性空间 :math:`{\mathbb V}` 中的 :math:`m` 个元素, 若 **存在一组不全为零的数** :math:`c_1, c_2, \cdots, c_m \in {\mathbb K}` , 使

   .. math:: c_1 \odot {\bm x}_1 \oplus c_2 \odot {\bm x}_2 \oplus \cdots \oplus c_m \odot {\bm x}_m = {\bm 0}

   则称 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_m` **线性相关** ( :term:`Linearly Dependent` ), 否则, 称其 **线性无关** ( :term:`Linearly Independent` ).


.. hint:: 若 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_m`  线性无关, 则当且仅当 :math:`c_1, c_2, \cdots, c_m \in {\mathbb K}` 全为零时, :math:`c_1 \odot {\bm x}_1 \oplus c_2 \odot {\bm x}_2 \oplus \cdots \oplus c_m \odot {\bm x}_m = {\bm 0}` 成立.

线性空间的基、坐标与维数
------------------------

定义
~~~~~~~~~

.. _def-LinearlyDependent:

.. proof:definition:: 线性空间的基、坐标与维数

   设 :math:`{\mathbb V}` 是数域 :math:`{\mathbb K}` 上的线性空间, :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_n (n \geq 1)` 是属于  :math:`{\mathbb V}` 的任意  :math:`n` 个元素, 若它们满足:

   (1) :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_n (n \geq 1)` 线性无关;
   (2) :math:`\forall {\bm x} \in {\mathbb V}` , 均可由 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_n (n \geq 1)` 线性表示, 记为
      .. math::
         {\bm x} = {\xi}_1 \odot {\bm x}_1 \oplus {\xi}_2 \odot {\bm x}_2 \oplus \cdots \oplus {\xi}_n \odot {\bm x}_n

   则称

   - :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_n (n \geq 1)` 是 :math:`{\mathbb V}` 一个 **基** 或 **基底** ;
   - :math:`{\xi}_1, {\xi}_2, \cdots, {\xi}_n (n \geq 1)` 为 :math:`{\bm x}` 在该基下的 **坐标**.
   - :math:`{\mathbb V}` 中最大线性无关的元素的数目为线性空间 :math:`\mathbb V` 的 **维数**, 记为 :math:`{\rm dim}({\mathbb V})` 

.. hint::

   1. 基不一定是向量, 可能是矩阵, 或者其它更为抽象的;
   2. 坐标是数.



基变换与坐标变换
----------------
从一个基到另一个基时, 坐标的变化.

.. hint::
   以下部分, 在不引起混淆时, 对集合内的加法 ( :math:`\oplus` ) 与数域内的加法 ( :math:`+` ) , 及数乘 ( :math:`\odot` ) 与数域内的乘法 (:math:`\times` 或省略 ) 不作区分.

两个基之间的转换
~~~~~~~~~~~~~~~~

**基变换:** 设 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_n` 是 :math:`{\mathbb V}^{n}` 的旧基, :math:`{\bm y}_1, {\bm y}_2, \cdots, {\bm y}_n` 是 :math:`{\mathbb V}^{n}` 的新基, 则有

.. math::  \left\{ {\begin{array}{ccc}{{{\bm{y}}_1} = {c_{11}}\odot{{\bm{x}}_1} \oplus {c_{21}}\odot{{\bm{x}}_2} \oplus  \cdots  \oplus {c_{n1}}\odot{{\bm{x}}_n}}\\{{{\bm{y}}_2} = {c_{12}}\odot{{\bm{x}}_1} \oplus {c_{22}}\odot{{\bm{x}}_2} \oplus  \cdots  \oplus {c_{n2}}\odot{{\bm{x}}_n}}\\ \vdots \\{{{\bm{y}}_n} = {c_{1n}}\odot{{\bm{x}}_1} \oplus {c_{2n}}\odot{{\bm{x}}_2} \oplus  \cdots  \oplus {c_{nn}}\odot{{\bm{x}}_n}}\end{array}} \right.

写成矩阵形式为

.. math:: {\rm{(}}{{\bm{y}}_1}{\rm{,}}\;{{\bm{y}}_2}, \cdots ,{{\bm{y}}_n}{\rm{)}}\;{\rm{ = }}\;{\rm{(}}{{\bm{x}}_1}{\rm{,}}\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}{\rm{)}}\;\left[ {\begin{array}{cccc}{{c_{11}}}&{{c_{12}}}& \cdots &{{c_{1n}}}\\{{c_{21}}}&{{c_{22}}}& \cdots &{{c_{2n}}}\\ \vdots & \vdots & \ddots & \vdots \\{{c_{n1}}}&{{c_{n2}}}& \cdots &{{c_{nn}}}\end{array}} \right] = \;{\rm{(}}{{\bm{x}}_1}{\rm{,}}\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}{\rm{)}}\;{\bm{C}}

即:

.. math::
   {\rm{(}}{{\bm{y}}_1}{\rm{,}}\;{{\bm{y}}_2}, \cdots ,{{\bm{y}}_n}{\rm{)}}\;{\rm{ = }}\;{\rm{(}}{{\bm{x}}_1}{\rm{,}}\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}{\rm{)}}\;{\bm{C}}

同理可得从新基变回旧基的表达式:

.. math::
   {\rm{(}}{{\bm{x}}_1}{\rm{,}}\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}{\rm{)}}\;{\rm{ = }}\; {\rm{(}}{{\bm{y}}_1}{\rm{,}}\;{{\bm{y}}_2}, \cdots ,{{\bm{y}}_n}{\rm{)}}\; {\bm{A}} {\rm{ = }}\;{\rm{(}}{{\bm{x}}_1}{\rm{,}}\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}{\rm{)}}\;{\bm{C}} {\bm{A}}

显然, ::math:`{\bm{A}} = {\bm{C}}^{-1}`



多个基之间的转换
~~~~~~~~~~~~~~~~

设有线性空间 ::math:`{\mathbb V}^n` , 及其三个基:

- 基1: :math:`{\bm X}_1, {\bm X}_2, \cdots, {\bm X}_n`
- 基2: :math:`{\bm Y}_1, {\bm Y}_2, \cdots, {\bm Y}_n`
- 基3: :math:`{\bm Z}_1, {\bm Z}_2, \cdots, {\bm Z}_n`

且设由基3到基1的过度矩阵为 :math:`{\bm C}_1` , 且由基3到基2的过度矩阵为 :math:`{\bm C}_2` , 则由基1到基2的过度矩阵为 :math:`{\bm C}_1^{-1}{\bm C}_2` 由基2到基1的过度矩阵为 :math:`{\bm C}_2^{-1}{\bm C}_1` , 即

.. figure:: ../../../_static/figs/BasisMath/MatrixTheory/LinearSpace/jjgdjzgx.png
   :scale: 30%
   :alt: 多个基之间的转换
   :align: center

   多个基之间的转换

   多个基之间的转换关系

.. math::
   {\rm{(}}{{\bm{Y}}_1}{\rm{,}}\;{{\bm{Y}}_2}, \cdots ,{{\bm{Y}}_n}{\rm{)}}\;{\rm{ = }}\;{\rm{(}}{{\bm{X}}_1}{\rm{,}}\;{{\bm{X}}_2}, \cdots ,{{\bm{X}}_n}{\rm{)}}\;{\bm{C}_1^{-1}}{{\bm C}_2}


.. math::
   {\rm{(}}{{\bm{X}}_1}{\rm{,}}\;{{\bm{X}}_2}, \cdots ,{{\bm{X}}_n}{\rm{)}}\;{\rm{ = }}\; {\rm{(}}{{\bm{Y}}_1}{\rm{,}}\;{{\bm{Y}}_2}, \cdots ,{{\bm{Y}}_n}{\rm{)}}\;{\bm{C}_2^{-1}}{{\bm C}_1}


坐标变换
~~~~~~~~~~~~~~~~

**坐标变换:** 设向量 :math:`\bm z` 在上述旧基与新基下可表示为:

.. math::
   {\bm z}  = {\xi}_1 {\bm x}_1 + {\xi}_2 {\bm x}_2 + \cdots + {\xi}_n {\bm x}_n = {\eta}_1 {\bm y}_1 + {\eta}_2 {\bm y}_2 + \cdots + {\eta}_n {\bm y}_n

则

.. math::
   {\bm{z}} = ({{\bm{x}}_1},{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n})\left[ {\begin{array}{ccc}{{\xi _1}}\\{{\xi _2}}\\ \vdots \\{{\xi _n}}\end{array}} \right] = ({{\bm{y}}_1},{{\bm{y}}_2}, \cdots ,{{\bm{y}}_n})\left[ {\begin{array}{ccc}{{\eta _1}}\\{{\eta _2}}\\ \vdots \\{{\eta _n}}\end{array}} \right] = ({{\bm{x}}_1},{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}){\bm{C}}\left[ {\begin{array}{ccc}{{\eta _1}}\\{{\eta _2}}\\ \vdots \\{{\eta _n}}\end{array}} \right]

从而有

.. math::
   ({{\bm{x}}_1},{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n})\left[ {\begin{array}{ccc}{{\xi _1}}\\{{\xi _2}}\\ \vdots \\{{\xi _n}}\end{array}} \right] = ({{\bm{x}}_1},{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}){\bm{C}}\left[ {\begin{array}{ccc}{{\eta _1}}\\{{\eta _2}}\\ \vdots \\{{\eta _n}}\end{array}} \right]

由此得坐标变换公式

.. math::
   \left[ {\begin{array}{ccc}{{\eta _1}}\\{{\eta _2}}\\ \vdots \\{{\eta _n}}\end{array}} \right] = {{\bm{C}}^{ - 1}}\left[ {\begin{array}{ccc}{{\xi _1}}\\{{\xi _2}}\\ \vdots \\{{\xi _n}}\end{array}} \right]


