.. _Section-LinearSubspace:

线性子空间
==========

线性子空间
----------

什么是线性子空间
~~~~~~~~~~~~~~~~~

.. _def-LinearlyDependent:

.. proof:definition:: 线性子空间

   设 :math:`{\mathbb V}_1` 是数域 :math:`{\mathbb K}` 上的线性空间 :math:`{\mathbb V}`
   的非空子集，若对任意的
   :math:`k\in {\mathbb K}`\ ，\ :math:`{\bm x}, {\bm y} \in {\mathbb V}_1`\ ，满足
   :math:`{\mathbb V}` 中加法与数乘运算的封闭性，则称 :math:`{\mathbb V}_1` 是 :math:`{\mathbb V}`
   的 **线性子空间** (:term:`Linear Subspace`) ，即满足：

   1. 加法运算\ :math:`\oplus`\ 封闭性:
      :math:`{\bm x} \oplus {\bm y} \in {\mathbb V}_1`
   2. 数乘运算\ :math:`\odot`\ 封闭性: :math:`k \odot {\bm x} \in {\mathbb V}_1`


.. note::
	举例: 对于三维欧式线性空间 :math:`{\mathbb V}^3` :

	1. :math:`{\mathbb V}^3` 中的任意一条直线构成其子空间 :math:`{\mathbb V}_1`

	2. :math:`{\mathbb V}^3` 中的任意两条不同的直线不构成其子空间

	.. image:: ../../../_static/figs/BasisMath/MatrixTheory/LinearSpace/xxzkjsl.png
	   :scale: 50%
	   :align: center


子空间的运算及其性质
~~~~~~~~~~~~~~~~~~~~

设\ :math:`{\mathbb V}_1 , {\mathbb V}_2` 是 :math:`{\mathbb V}` 的子空间，定义如下三种运算：

-  交(\ :math:`\cap`): :math:`{\mathbb V}_1 \cap {\mathbb V}_2`;
-  并(\ :math:`\cup`): :math:`{\mathbb V}_1 \cup {\mathbb V}_2`;
-  和(\ :math:`+`): :math:`{\mathbb V}_1 + {\mathbb V}_2`.

性质：

-  :math:`{\mathbb V}_1 \cap {\mathbb V}_2  \subseteq {\mathbb V}_1 \cup {\mathbb V}_2 \subseteq {\mathbb V}_1 + {\mathbb V}_2`
-  :math:`{\mathbb V}_1 \cap {\mathbb V}_2 = {\mathbb V}_2 \cap {\mathbb V}_1`,
   :math:`({\mathbb V}_1 \cap {\mathbb V}_2) \cap {\mathbb V}_3 = {\mathbb V}_1 \cap ({\mathbb V}_2 \cap {\mathbb V}_3)`
-  :math:`{\mathbb V}_1 + {\mathbb V}_2 = {\mathbb V}_2 + {\mathbb V}_1`,
   :math:`({\mathbb V}_1 + {\mathbb V}_2) + {\mathbb V}_3 = {\mathbb V}_1 + ({\mathbb V}_2 + {\mathbb V}_3)`
-  交(\ :math:`\cap`): :math:`{\mathbb V}_1 \cap {\mathbb V}_2` 是 :math:`{\mathbb V}` 的子空间;
-  和(\ :math:`+`): :math:`{\mathbb V}_1 + {\mathbb V}_2` 是 :math:`{\mathbb V}` 的子空间.
-  并(\ :math:`\cup`): :math:`{\mathbb V}_1 \cup {\mathbb V}_2` 不是 :math:`{\mathbb V}` 的子空间;
-  维数公式:

   .. math:: \underbrace{\dim {{\mathbb V}_1} }_{n_1} + \underbrace{\dim {{\mathbb V}_2} }_{n_2} = \underbrace{\dim ({{\mathbb V}_1} + {{\mathbb V}_2}) }_n + \underbrace{\dim ({{\mathbb V}_1} {\cap} {{\mathbb V}_2}) }_m

.. note::

	举例：

	-  :math:`{\mathbb V}_1`: :math:`x` 轴上的点
	-  :math:`{\mathbb V}_2`: :math:`y` 轴上的点
	-  :math:`{\mathbb V}_1 \cap {\mathbb V}_2`: 原点
	-  :math:`{\mathbb V}_1 \cup {\mathbb V}_2`: :math:`x` 轴和 :math:`y` 轴上的点
	-  :math:`{\mathbb V}_1 + {\mathbb V}_2`: 二维平面
	-  维数公式： :math:`n_1 + n_2 = n + m \Rightarrow 1 + 1 = 2 + 0`

直和
----

什么是直和
~~~~~~~~~~~~~~

和的特例，即存在唯一分解.

.. _def-DirectSum:

.. proof:definition:: 直和

   若\ :math:`\forall {\bm z} \in {\mathbb V}_1 + {\mathbb V}_2`, 有唯一的
   :math:`{\bm x}\in {\mathbb V}_1, {\bm y}\in {\mathbb V}_2`, 则称 :math:`{\mathbb V}_1 + {\mathbb V}_2`
   为 **直和** (:term:`Direct Sum`) , 记为 :math:`{\mathbb V}_1 + {\mathbb V}_2` 或 :math:`{\mathbb V}_1 \oplus {\mathbb V}_2`.

性质
~~~~

-  :math:`{\mathbb V}_1 \oplus {\mathbb V}_2 \Leftrightarrow {\mathbb V}_1 \cap {\mathbb V}_2 = L({\bm 0})  \Leftrightarrow  {\dim} ({\mathbb V}_1) + {\dim} ({\mathbb V}_2) = {\dim} ({\mathbb V}_1+{\mathbb V}2)`

生成的子空间
------------

什么是生成子空间
~~~~~~~~~~~~~~~

.. _def-LinearSpan:

.. proof:definition:: 生成子空间

   设 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_m` 是数域 :math:`{\mathbb K}` 上的线性空间 :math:`{\mathbb V}` 上的一组向量, 其\ **所有**\ 线性组合的集合

   .. math:: {\mathbb V}_1 = \left \{ {k_1 {\bm x}_1} + {k_2 {\bm x}_2} + \cdots + {k_m {\bm x}_m} \right \}, k_i \in {\mathbb K}, i = 1, 2, \cdots, m

   是 :math:`{\mathbb V}` 的一个线性子空间, 称其为由
   :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_m` **张成/生成的子空间** (:term:`Linear Span`) ，记为

   .. math:: L({\bm x}_1, {\bm x}_2, \cdots, {\bm x}_m) = \left \{ {k_1 {\bm x}_1 } + {k_2 {\bm x}_2 } + \cdots + {k_m {\bm x}_m} \right \}

矩阵的列空间、核空间、秩与零度
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

设有矩阵 :math:`{\bm A} = (a_{ij})\in {\mathbb R}^{m\times n}`,
:math:`{\bm a}_i(i=1,2,\cdots, n)` 为\ :math:`{\bm A}`
的地\ :math:`i`\ 个列向量, 称矩阵 :math:`{\bm A}`
的所有列向量张成的空间
:math:`L({\bm a}_1, {\bm a}_2, \cdots, {\bm a}_n)` 为矩阵
:math:`{\bm A}` 的\ **列空间(值域)**, 记为

.. math:: {\mathcal R}({\bm A}) = L({\bm a}_1, {\bm a}_2, \cdots, {\bm a}_n)

则矩阵 :math:`{\bm A}` 列空间的维度定义为矩阵 :math:`{\bm A}` 的 **秩**

.. math:: {\rm rank}{\bm A} = {\dim} {\mathcal R}({\bm A})

设有矩阵
:math:`{\bm A} = (a_{ij})\in R^{m\times n}, {\bm a}_i(i=1,2,\cdots,n)`
, 称集合 :math:`\{ {\bm x} {\lvert} {\bm A} {\bm x} = {\bm 0} \}`
为矩阵 :math:`{\bm A}` 的 **核空间** (:term:`Kernel Space`) 或 **零空间** (:term:`Null Space`) , 记为

.. math:: {\mathcal N}({\bm A}) = \{ {\bm x} {\lvert} {\bm A}{\bm x} = {\bm 0} \}

则矩阵 :math:`{\bm A}` 核空间的维度定义为矩阵 :math:`{\bm A}`
的 **零度**

.. math:: n({\bm A}) = {\dim} {\mathcal N}({\bm A})


.. hint::
   设 :math:`{\bm u}, {\bm v}` 是方程组 :math:`{\bm A}{\bm x} = {\bm b}` 的两个解, 则有

   .. math::
      \begin{aligned}
         {\bm A}{\bm u} &={\bm b} \\ {\bm A}{\bm v} &={\bm b}
      \end{aligned}
      \Rightarrow {\bm A}({\bm u}-{\bm v}) = {\bm b}-{\bm b} = {\bm 0}

   故任意不同的两个线性方程组的解的差位于矩阵 :math:`\bm A` 的零空间中.

   进一步地, 设 :math:`{\bm v}` 是方程组 :math:`{\bm A}{\bm x} = {\bm b}` 的一个解, 那么其任意解集可表示为

   .. math::
      \{\bm{v}+\bm{x} | {\bm A} \bm{v}=\bm{b} \wedge \bm{x} \in {\mathcal N}({\bm A})\}
      :label: equ-Equ_Solution

矩阵的Spark
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

设有矩阵 :math:`{\bm A}`, 称其列空间中线性相关的向量数目为矩阵 :math:`{\bm A}` 的 **Spark**, 记为 :math:`{\rm Spark}({\bm A})` .


.. hint::
   - 矩阵的Rank是最大线性无关的列数
   - 矩阵的Spark是最小线性相关的列数

   .. math::
      {\bm A}_{1}=\left[\begin{array}{llll}{1} & {0} & {0} & {1} \\ {0} & {1} & {0} & {0} \\ {0} & {0} & {1} & {0}\end{array}\right] \Leftrightarrow\left\{\begin{array}{l}{\operatorname{Rank}({\bm A})=3} \\ {\operatorname{Spark}({\bm A})=2}\end{array}\right.

   .. math::
      {\bm A}_{2}=\left[\begin{array}{cccc}{1} & {0} & {0} & {1} \\ {0} & {1} & {0} & {1} \\ {0} & {0} & {1} & {0}\end{array}\right] \Leftrightarrow\left\{\begin{array}{l}{\operatorname{Rank}({\bm A})=3} \\ {\operatorname{Spark}({\bm A})=3}\end{array}\right.

   .. math::
      {\bm A}_{3}=\left[\begin{array}{llll}{1} & {0} & {0} & {1} \\ {0} & {1} & {0} & {1} \\ {0} & {0} & {1} & {1}\end{array}\right] \Leftrightarrow\left\{\begin{array}{l}{\operatorname{Rank}({\bm A})=3} \\ {\operatorname {Spark}({\bm A})=4}\end{array}\right.


总结
~~~~~~~~

-  矩阵的列空间/值域:

   .. math:: {\mathcal R}({\bm A}) =  \left \{ {\bm A} {\bm x} {\lvert} {\bm x} \in {R^n} \right \}

-  矩阵的核空间/零空间:

   .. math:: {\mathcal N}({\bm A}) = \left \{ {\bm x} {\lvert} {\bm A}{\bm x} = {0} \right \}

-  矩阵的秩(列空间的维度):
   :math:`{\rm rank} {\bm A} = {\dim} {\mathcal R}({\bm A})`
-  矩阵的零度(核空间的维度):
   :math:`n({\bm A}) = {\dim} {\mathcal N}({\bm A})`
-  :math:`{\rm rank} {\bm A} + n({\bm A})  = n`
-  :math:`{\rm rank} {\bm A^T} + n({\bm A}^T)  = m`
-  :math:`n({\bm A}) - n({\bm A}^T)  = n-m`
