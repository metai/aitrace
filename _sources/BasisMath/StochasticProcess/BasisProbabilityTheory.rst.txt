.. _Chapter-BasisProbabilityTheory:

概率论基础
===================

概率空间与随机变量
-------------------

柯尔莫哥洛夫概率公理化体系
+++++++++++++++++++++++++

概率论公里化有三种学派：主观（任何命题都看作事件）、客观（频率的极限）、以测度论为基础（柯尔莫哥洛夫）

是什么
^^^^^^^

- 是一种概率论公里化方法，结合了集合论、测度论、实变函数论（与复变函数论关系？）；
- 是一个概率空间 :math:`(\Omega, \mathcal{F}, \mathbb{P})` 的可测描述；
- 测度为概率、可测函数为随机变量、全直线对应概率空间、点集对应事件集；

为什么
^^^^^^^

19世纪下半叶，概率论自身有了一定的发展，但诸如概率、收敛性、随机变量数学期望等没有严格定义。

- 为什么要有公里化方法：
- 为什么会想到用测度论：


怎么办
^^^^^^^

- 怎么结合集合论、测度论、实变函数论公里化概率论
- 怎么用这种公里化系统

1. 概率空间

概率空间可以用一个三元组表示为 :math:`(\Omega, \mathcal{F}, \mathbb{P})` ，即样本空间 :math:`\Omega` 上的事件 :math:`\mathcal{F}` 对应的概率测度 :math:`\mathbb{P}` ，其中：

- **事件域：** 事件域 :math:`\mathcal{F}` 为样本空间 :math:`\Omega` 的子集生成的 :math:`\sigma` -代数，即满足：

  - 空集是任意集合的子集： :math:`\emptyset \in \mathcal{F}`
  - 补运算封闭性： 若 :math:`A \in \mathcal{F}` ，则 :math:`A^c \in \mathcal{F}`
  - 并集运算封闭性： 若 :math:`{A_1, A_2, ..., A_n, ...} \subset \mathcal{F}` ，则 :math:`{\bigcup}_{n=1}^{\infty} \in \mathcal{F}`

- **概率测度：** 概率测度 :math:`\mathbb{P}` 是定义在事件域 :math:`\mathcal{F}` 上，取值为 :math:`[0, 1]` 的函数

  - 非负性：:math:`P(A) > 0`
  - 规范性：测度空间为1， :math:`P(\Omega) = 1`
  - 可列（完全）可加性：相互独立事件联合概率为各自概率和，若 :math:`{A_1, A_2, ..., A_n, ...} \subset \mathcal{F}` 且两两互不相交（:math:`A_m \bigcap A_n = \emptyset, m \neq n`）


.. hint:: :math:`\sigma` -代数又称 :math:`\sigma` -域，是一个集合，是一个满足对交并补运算封闭的集合（数域是满足四则运算封闭的集合），集合 :math:`X` 上的 :math:`\sigma` -代数 是集合 :math:`X` 的所有子集集合（幂集）的一个子集。



2. 随机变量

设有概率空间 :math:`(\Omega, \mathcal{F}, \mathbb{P})` ，随机变量 :math:`X(\omega)` 为样本空间 :math:`\Omega` 上的取值在 :math:`\mathbb{R}^d` 上的 :math:`\mathcal{F}` 可测函数，即 :math:`X(\omega): \Omega \rightarrow \mathbb{R}^d`


还有什么
^^^^^^^

- 随机性的本质依然未解决
- 随机性与确定性界限
- 定义也是人为定义的，未必是严密的






傅立叶变换
+++++++++++++++++++








