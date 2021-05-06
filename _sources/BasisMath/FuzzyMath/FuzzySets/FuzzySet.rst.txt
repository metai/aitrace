.. _Section-FuzzySet:

模糊集合
=====================

引言(不确定集合)
----------------

在经典集合论中(参见 :ref:`Section-SetConcept`), 元素 :math:`x` 是否属于集合 :math:`\mathbb S` 是确定的, 且只有两种情况, 即属于或不属于. 如果元素 :math:`x` 以一定的可能性属于或不属于集合 :math:`\mathbb S` 呢? 这就是 **模糊集合** (:term:`Fuzzy Set`).

Zadeh于1965年提出模糊集合 :cite:`L.A.Zadeh.1965` , 作为对经典集合的扩展, 在模糊集理论中, 经典集合通常被称为 **明确集合** (:term:`Crisp Set`), 通过引入隶属函数(:term:`Membership Function`)与隶属度(:term:`Membership Degree`), 来衡量元素的模糊性, 从而明确集为模糊集的特例, 即隶属函数仅有两个值( :math:`0, 1` ), 隶属度为 :math:`0` 或 :math:`1`.

.. note::
   比如, 对于 "58岁是不是老年人" 这个问题, 很难说 "是" 还是 "不是" , 很容易想到的方法是用 :math:`[0, 1]` 之间的一个数来表示, 如 :math:`0.8` 表示: 58岁的人有 :math:`80\%` 的可能性是老年人. 如果用 :math:`[0, 100]` 来表示岁数, 那么一个岁数为 :math:`x \in [0, 100]` 的人, 是否是老年人可以用隶属函数 :math:`f(x) = x/100` 表示, 隶属度为 :math:`f(x)` 的值. 然而, 对于超过 :math:`100` 岁的人呢, 此时 :math:`f(x) > 1` .

容易发现, 实际应用中, 我们很难确认隶属函数的具体形式. 因而, Pawlak 于1982年提出基于等价关系的近似表示方法，即用两个隶属函数的上下近似来表示, 从而引入 **粗糙集** (:term:`Rough Set`) 的概念 :cite:`Pawlak.1982` .


模糊集的定义
-------------

.. _defCrispSet:

.. proof:definition:: 明确集合

   **明确集合** 的定义可以扩展为集合(或论域) :math:`\mathbb X` 和映射 :math:`f : {\mathbb X} \rightarrow \{0, 1\}` 的二元组 :math:`{\mathbb A} = ({\mathbb X}, f)` , 其中, :math:`f` 为集合 :math:`\mathbb A` 的特征函数(也称示性函数, 参见 :ref:`SubsubSection-SetCharacteristicFunction`)

   .. math::
      f(x) = \left\{ {\begin{array}{lll}
      {1\;\;if\;x \in \mathbb A}\\
      {0\;\;if\;x ∉ \mathbb A}
      \end{array}} \right. .

扩展上述定义, 可以得到模糊集合的定义

.. _defFuzzySet:

.. proof:definition:: 模糊集合

   设有集合(或论域) :math:`\mathbb X` 和映射 :math:`f : {\mathbb X} \rightarrow [0, 1]` 的组合, 二元组 :math:`{\mathbb A} = ({\mathbb X}, f)` 确定了一个集合, 称为 **模糊集合** (:term:`Fuzzy Set`). 函数 :math:`f(x) = \mu_{\mathbb A}` 称为模糊集 :math:`\mathbb A` 的 **隶属函数** (:term:`Membership Function`). 对于 :math:`\forall x \in {\mathbb X}`, 称 :math:`f(x)` 为元素 :math:`x` 在模糊集 :math:`\mathbb A` 中的 **隶属度** (:term:`Membership Degree`, :term:`Membership Grade`). 记 :math:`F({\mathbb X})` 为集合 :math:`\mathbb X` 的全体模糊子集.


举例说明如何使用模糊集对语言表达进行建模, 如要表示 "年轻" 的概念, 可以用模糊集 :math:`{\mathbb A} = ({\mathbb X}, f)` 表示, 其中岁数集合为 :math:`\mathbb \in [0, 100]` , 隶属函数可以表示为

.. math::
   \mu_{\mathbb A} = \left\{ {\begin{array}{lll}
   {1\;\;\;\;\;\;\;{\rm if}\;0 \le x \le 20}\\
   {\frac{{40 - x}}{{20}}\;\;{\rm if}\;20 \le x \le 40}\\
   {0\;\;\;\;\;\;\;{\rm otherwise}\;\;}
   \end{array}} \right.


.. hint::
   明确集相当于模糊集的特例, 即当模糊集的隶属函数取明确集的特征函数时 (即: :math:`f : {\mathbb X} \rightarrow \{0, 1\}` ), 模糊集退化为明确集.

\geq

模糊集与明确集
--------------

给定模糊集 :math:`{\mathbb A} = ({\mathbb X}, f)` , :math:`\alpha \in [0, 1]` , 有如下明确集:

- **α-割集** (α-cut set, α-level set): :math:`{\mathbb A}^{\ge\alpha} = {\mathbb A}_{\alpha} = \{x\in {\mathbb X} | f(x)\geq \alpha\}`
- **强α-割集** (strong α-cut set, strong α-level set): :math:`{\mathbb A}^{ >\alpha} = {\mathbb A}^{'}_{\alpha} = \{x\in {\mathbb X} | f(x) > \alpha\}`
- **紧集** (support set): :math:`S({\mathbb A}) = Supp({\mathbb A}) = {\mathbb A}^{ > 0} = \{x\in {\mathbb X} | f(x) > 0\}`
- **核集** (core set, kernel set): :math:`C({\mathbb A}) = Core({\mathbb A}) = {\mathbb A}^{=1} = \{x\in {\mathbb X} | f(x)= 1\}`

模糊集的表示
--------------

记模糊集 :math:`\mathbb A` , 隶属函数为 :math:`\mu_{\mathbb A}` , 元素 :math:`x` 属于模糊集 :math:`\mathbb A` 的隶属度为 :math:`\mu_{\mathbb A}(x)` , 简记为 :math:`\mu(x)` . 则有以下表示方法.

Zadeh表示法
~~~~~~~~~~~~~~

Zadeh表示法如下:

.. math::
   {\mathbb A} = \frac{\mu(x_1)}{x_1} + \frac{\mu(x_2)}{x_2} + \cdots + \frac{\mu(x_n)}{x_n},

或

.. math::
   {\mathbb A} = \mu(x_1)/{x_1} + \mu(x_2)/{x_2} + \cdots + {\mu(x_n)}/{x_n},

其中, 符号 :math:`+, /` 不表示四则运算中的加法和除法, :math:`\frac{\mu(x_i)}{x_i}` 表示元素 :math:`x_i` 隶属于模糊集 :math:`\mathbb A` 的隶属度是 :math:`\mu(x_i)` .

若集合 :math:`\mathbb A` 为无限集合, 则有以下表示方法

.. math::
   {\mathbb A} = \int\frac{\mu(x)}{x}


序偶表示法
~~~~~~~~~~~~~~

.. math::
   {\mathbb A} = \left\{({x_1}, \mu(x_1)), ({x_2}, \mu(x_2)), \cdots, ({x_n}, \mu(x_n))\right\},

向量表示法
~~~~~~~~~~~~~~

.. math::
   {\mathbb A} = (\mu(x_1), \mu(x_2), \cdots, \mu(x_n))

特殊模糊集
--------------

由于模糊集合用隶属度表征, 因而对于两个模糊集合 :math:`{\mathbb A}, {\mathbb B}` , 其隶属函数分别为 :math:`\mu_{\mathbb A}` , :math:`\mu_{\mathbb B}` , 则

- **空集** (Empty Set): :math:`{\mathbb A} = \emptyset` :math:`\Leftrightarrow` :math:`\mu_{\mathbb A}(x) = 0`
- **全集** (Full Set): :math:`{\mathbb A} = {\mathbb E}` :math:`\Leftrightarrow` :math:`\mu_{\mathbb A}(x) = 1`
- **子集** (Subset): :math:`{\mathbb B}\subset {\mathbb A}` :math:`\Leftrightarrow` :math:`\mu_{\mathbb B}(x) \le \mu_{\mathbb A}(x)`
- **相等** (equal): :math:`{\mathbb A} = {\mathbb B}` :math:`\Leftrightarrow` :math:`\mu_{\mathbb A}(x) = \mu_{\mathbb B}(x)`


模糊集的运算
--------------

.. _SubsubSectionFFuzzyOperator:

模糊算子
~~~~~~~~~~~~

由于模糊集合用隶属度表征, 因而对于两个模糊集合 :math:`{\mathbb A}, {\mathbb B}` , 其隶属函数分别为 :math:`\mu_{\mathbb A}` , :math:`\mu_{\mathbb B}` , 一般地, 定义


- **交** (Intersection): :math:`{\mathbb A} \cap {\mathbb B}` :math:`\Leftrightarrow` :math:`\mu_{{\mathbb A} \cap {\mathbb B}}(x) = {\rm min}(\mu_{\mathbb A}(x), \mu_{\mathbb B}(x)) = \mu_{\mathbb A}(x) \wedge \mu_{\mathbb B}(x)`
- **并** (Union): :math:`{\mathbb A} \cup {\mathbb B}` :math:`\Leftrightarrow` :math:`\mu_{{\mathbb A} \cup {\mathbb B}}(x) = {\rm max}(\mu_{\mathbb A}(x), \mu_{\mathbb B}(x)) = \mu_{\mathbb A}(x) \vee \mu_{\mathbb B}(x)`
- **补** (Complement): :math:`\bar{\mathbb A} = {\mathbb B}` :math:`\Leftrightarrow` :math:`\mu_{\bar{\mathbb A}}(x) = 1- \mu_{\mathbb A}(x)`

两个模糊集合的运算的实质是隶属度函数的运算, 上述定义中采用 :math:`{\rm max}, {\rm min}` 常用模糊算子, 也可以采用其它算子.

- **交** (Intersection): :math:`{\mathbb C} = {\mathbb A} \cap {\mathbb B}`
   - 模糊交算子: :math:`\mu_{\mathbb C}(x) = {\rm min}(\mu_{\mathbb A}(x), \mu_{\mathbb B}(x))`
   - 代数积算子: :math:`\mu_{\mathbb C}(x) = \mu_{\mathbb A}(x) \cdot \mu_{\mathbb B}(x)`
   - 有界积算子: :math:`\mu_{\mathbb C}(x) = {\rm max}(0, \mu_{\mathbb A}(x) + \mu_{\mathbb B}(x)-1)`
- **并** (Union): :math:`{\mathbb C} = {\mathbb A} \cup {\mathbb B}`
   - 模糊并算子: :math:`\mu_{\mathbb C}(x) = {\rm max}(\mu_{\mathbb A}(x), \mu_{\mathbb B}(x))`
   - 代数和算子: :math:`\mu_{\mathbb C}(x) = \mu_{\mathbb A}(x) + \mu_{\mathbb B}(x) - \mu_{\mathbb A}(x) \cdot \mu_{\mathbb B}(x)`
   - 有界和算子: :math:`\mu_{\mathbb C}(x) = {\rm min}(1, \mu_{\mathbb A}(x) + \mu_{\mathbb B}(x)-1)`
- 平衡算子: :math:`\mu_{{\mathbb C}}(x) = [\mu_{\mathbb A}(x) \cdot \mu_{\mathbb B}(x)]^{1-\gamma} \cdot [1 - (1-\mu_{\mathbb A}(x))(1-\mu_{\mathbb B}(x))]` , :math:`\gamma \in [0, 1]`

.. hint::
   取最大最小不可避免地会丢失信息, 平衡算子可以起到信息补偿作用.


模糊集间的运算定律
~~~~~~~~~~~~~~~~~~~~~~

#. 交换律: :math:`\mathbb{A} \cap \mathbb{B}`, :math:`\mathbb{A} \cup \mathbb{B}`

#. 结合律: :math:`\mathbb{A} \cap (\mathbb{B} \cap \mathbb{C}) = (\mathbb{A} \cap \mathbb{B}) \cap \mathbb{C}`, :math:`\mathbb{A} \cup (\mathbb{B} \cup \mathbb{C}) = (\mathbb{A} \cup \mathbb{B}) \cup \mathbb{C}`

#. 分配律: :math:`\mathbb{A} \cap (\mathbb{B} \cup \mathbb{C}) = (\mathbb{A} \cap \mathbb{B}) \cup (\mathbb{A} \cap \mathbb{C})`, :math:`\mathbb{A} \cup (\mathbb{B} \cap \mathbb{C}) = (\mathbb{A} \cup \mathbb{B}) \cap (\mathbb{A} \cup \mathbb{C})`

#. 对偶律: :math:`\overline{\mathbb{A} \cup \mathbb{B}} = \bar{\mathbb A} \cap \bar{\mathbb B}` , :math:`\overline{\mathbb{A} \cap \mathbb{B}} = \bar{\mathbb A} \cup \bar{\mathbb B}`

#. 两极律: :math:`\mathbb{A} \cap \mathbb{E} = \mathbb{A}, \mathbb{A} \cup \mathbb{E} = \mathbb{E}`

#. 零一律: :math:`\mathbb{A} \cap \mathbb{\emptyset} = \mathbb{\emptyset}, \mathbb{A} \cup \mathbb{\emptyset} = \mathbb{A}`

#. 吸收律: :math:`\mathbb{A}\cap (\mathbb{A}\cup \mathbb{B}) = \mathbb{A}, \mathbb{A} \cup (\mathbb{A}\cap \mathbb{B}) = \mathbb{A}`

#. 等幂律: :math:`\mathbb{A} \cap \mathbb{A} = \mathbb{A}, \mathbb{A} \cup \mathbb{A} = \mathbb{A}`

#. 复原率: :math:`\bar{\bar{\mathbb A}} = {\mathbb A}`

