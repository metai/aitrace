
集合的概念与性质
====================

一般集合
----------

概念
~~~~~~~~

**定义**: 集合 (:term:`set`)是指具有某种特定性质的具体的或抽象的对象构成的总体. 其中, 构成集合的这些对象称为该集合的 **元素** .

.. note:: 将上述定义的集合称为一般集合. 一个元素是否在一个集合中, 在于该元素是否具备上述特定性质, 该性质是具体的明确的, 如果该性质不具体不明确呢?

一般地集合是指具有如下性质的集合:

1. 确定性: 即任给一元素, 它要么在该集合中, 要么不在.
2. 互异性: 即该集合中的任意两个元素不同, 每个元素只能出现一次.
3. 无序性: 即该集合中的元素无顺序关系.

.. note:: 关于上述性质, 思考如下:

   0. 上述定义的一般集合的概念可以概括所有集合, 即对象全体吗?

   1. 确定性: 如果元素以一定的可能性在呢?元素不确定, 上述特定性质不确定?

   2. 互异性: 如果有两个及以上的元素相同呢? 如果出现多次呢?可否定义集合规则: 可以出现 :math:`N` 次的对象全体?(可以, 不过还是普通集合); 可否定义集合规则: 可以出现 随机次数的对象全体?(可以, 不过还是普通集合); 如给定对象全体 :math:`\{1, 2, 2, 3, 3, 3\}`, 如果不指明特定性质, 是不能判断它是否是一般的集合. 如果定义集合为: 出现次数等于其数值且小于4的正整数集, 上述对象化为一般集合 :math:`\{1, 2, 3\}`.

   3. 无序性: 若有序呢? 可否定义集合规则: 对象全体?

元素与集合的关系
~~~~~~~~~~~~~~~~~

给定集合 :math:`\mathbb{S}`, 元素 :math:`x`, 定义如下关系:

1. 属于(:math:`\in`): :math:`x \in \mathbb{S}`
2. 不属于(:math:`\notin`): :math:`x \notin \mathbb{S}`


集合与集合的关系
~~~~~~~~~~~~~~~~~

给定集合 :math:`\mathbb{A}`, :math:`\mathbb{B}`, 定义如下关系:

- 包含 (:math:`\subseteq`): :math:`\mathbb{A} \subseteq \mathbb{B}` , 称 :math:`\mathbb{A}` 包含于 :math:`\mathbb{B}` 或 :math:`\mathbb{B}` 包含 :math:`\mathbb{A}` .
- 真包含 (:math:`\subsetneq`): :math:`\mathbb{A} \subsetneq \mathbb{B}` , 称 :math:`\mathbb{A}` 真包含于 :math:`\mathbb{B}` 或 :math:`\mathbb{B}` 真包含 :math:`\mathbb{A}` .
- 等于 (:math:`=`): :math:`\mathbb{A} = \mathbb{B}` , 集合 :math:`\mathbb{A}` 中的元素都在集合 :math:`\mathbb{B}` 中, 且集合 :math:`\mathbb{B}` 中的元素都在集合 :math:`\mathbb{A}` 中.
- 不等于 (:math:`\neq`): :math:`\mathbb{A} \neq \mathbb{B}`, 集合 :math:`\mathbb{A}` 中, 至少有一个元素不在集合 :math:`\mathbb{B}` 中.


**定义**: 子集 ( :term:`Subset` ), 一般地, 对于集合 :math:`\mathbb{A}`, :math:`\mathbb{B}` , 若集合 :math:`\mathbb{A}` 中的元素都是集合 :math:`\mathbb{B}` 中的元素, 即 :math:`\forall x \in \mathbb{A}` , 有 :math:`x \in \mathbb{B}` , 则称这两个集合具有包含关系, 称 :math:`\mathbb{A}` 包含于(:math:`\subseteq`) :math:`\mathbb{B}` 或 :math:`\mathbb{B}` 包含( :math:`\supseteq` ) :math:`\mathbb{A}` . 空集(没有任何元素, 记为 :math:`\mathbb{\emptyset}`) 是任何集合的子集.

**定义**: 真子集 ( :term:`Proper Subset` ) 如果集合 :math:`\mathbb{A}` 是 :math:`\mathbb{B}` 的子集, 且 :math:`\mathbb{A} \neq \mathbb{B}`, 即 :math:`\mathbb{B}` 中至少有一个元素不属于 :math:`\mathbb{A}` , 那么 :math:`\mathbb{A}` 就是 :math:`\mathbb{B}` 的真子集, 可记作: :math:`\mathbb{A} \subsetneq \mathbb{B}` .


集合间的运算
~~~~~~~~~~~~~

- 交(:math:`\cap`): :math:`\mathbb{A} \cap \mathbb{B} = \{x \mid x\in \mathbb{A} 且 x \in \mathbb{B} \}`, 如 :math:`\mathbb{A} \cap \mathbb{B}` .
- 并(:math:`\cup`): :math:`\mathbb{A} \cup \mathbb{B} = \{x \mid x\in \mathbb{A} 或 x \in \mathbb{B} \}`, 如 :math:`\{1, 2\} \cup \{3, 4, 5\} = \{1, 2, 3, 4, 5\}` .
- 和(:math:`+`): :math:`\mathbb{A} + \mathbb{B} = \{x+y \mid x\in \mathbb{A}, y \in \mathbb{B} \}`, 如 :math:`\{1, 2\} + \{2, 4\} = \{3, 4, 5, 6\}` .
- 差(:math:`-`): :math:`\mathbb{A} - \mathbb{B} = \{x \mid x\in \mathbb{A}, x \notin \mathbb{B} \}`, 也称相对补集, 如 :math:`\{1, 2\} + \{2, 4\} = \{1\}` .
- 补(:math:`\complement`), 设 :math:`\mathbb{U}` 是一个集合，:math:`\mathbb{A}` 是 :math:`\mathbb{U}` 的一个子集, 由 :math:`\mathbb{U}` 中所有不属于 :math:`\mathbb{A}` 的元素组成的集合, 叫做子集 :math:`\mathbb{A}` 在 :math:`\mathbb{U}` 中的补集, 也称绝对补集, 记作 :math:`\complement _{\mathbb{U}}\mathbb{A}` .

集合间的运算定律
~~~~~~~~~~~~~~~~~

#. 交换律: :math:`\mathbb{A} \cap \mathbb{B}`, :math:`\mathbb{A} \cup \mathbb{B}`, :math:`\mathbb{A} + \mathbb{B}`

#. 结合律: :math:`\mathbb{A} \cap (\mathbb{B} \cap \mathbb{C}) = (\mathbb{A} \cap \mathbb{B}) \cap \mathbb{C}`, :math:`\mathbb{A} \cup (\mathbb{B} \cup \mathbb{C}) = (\mathbb{A} \cup \mathbb{B}) \cup \mathbb{C}`, :math:`(\mathbb{A} + \mathbb{B}) + \mathbb{C} = \mathbb{A} + (\mathbb{B} + \mathbb{C})`

#. 分配律: :math:`\mathbb{A} \cap (\mathbb{B} \cup \mathbb{C}) = (\mathbb{A} \cap \mathbb{B}) \cup (\mathbb{A} \cap \mathbb{C})`, :math:`\mathbb{A} \cup (\mathbb{B} \cap \mathbb{C}) = (\mathbb{A} \cup \mathbb{B}) \cap (\mathbb{A} \cup \mathbb{C})`

#. 对偶律: :math:`xxx`

#. 同一律: :math:`\mathbb{A} \cap \mathbb{U} = \mathbb{A}, \mathbb{A} \cup \mathbb{\emptyset} = \mathbb{A}`

#. 零一律: :math:`\mathbb{A} \cap \mathbb{\emptyset} = \mathbb{\emptyset}, \mathbb{A} \cup \mathbb{U} = \mathbb{U}`

#. 吸收律: :math:`\mathbb{A}\cap (\mathbb{A}\cup \mathbb{B}) = \mathbb{A}, \mathbb{A} \cup (\mathbb{A}\cap \mathbb{B}) = \mathbb{A}`

#. 等幂律: :math:`\mathbb{A} \cap \mathbb{A} = \mathbb{A}, \mathbb{A} \cup \mathbb{A} = \mathbb{A}`

#. 反演律(德·摩根律): :math:`\complement_{\mathbb{U}}{\mathbb{A} \cap \mathbb{B}} = \complement_{\mathbb{U}}{\mathbb{A}} \cup \complement_{\mathbb{U}}{\mathbb{B}}`, :math:`\complement_{\mathbb{U}}{\mathbb{A} \cup \mathbb{B}} = \complement_{\mathbb{U}}{\mathbb{A}} \cap \complement_{\mathbb{U}}{\mathbb{B}}`



其它集合
----------------

模糊集
~~~~~~~~~



