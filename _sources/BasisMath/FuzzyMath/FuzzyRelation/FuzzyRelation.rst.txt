.. _Section-FuzzyRelation:

模糊关系
=====================

明确关系与模糊关系
------------------

.. _defCrispRelation:

.. proof:definition:: 明确关系(Crisp Relation)

   给定明确集合 :math:`{\mathbb X}, {\mathbb Y}` , 直积 :math:`{\mathbb X} \times {\mathbb Y} = \{(x, y)|x\in {\mathbb X}, y\in {\mathbb Y}\}` 的一个子集 :math:`{\mathbb R}` 称为集合 :math:`\mathbb X` 到 :math:`\mathbb Y` 的一个 **明确关系** (Crisp Relation). 这种关系可以用特征函数表示为

   .. math::
      \mu_{\mathbb R}(x,y) : {\mathbb X} \times {\mathbb Y} \rightarrow \{0, 1\}

   更近一步地, 可表示为:

   .. math::
      \mu_{\mathbb R}(x,y) = \left\{ {\begin{array}{lll}
      {1, \;\;{\rm if}(x,y)\in{\mathbb R}}\\
      {0, \;\;{\rm otherwise}}
      \end{array}} \right.


.. _defFuzzyRelation:

.. proof:definition:: 模糊关系(Fuzzy Relation)

   给定明确集合 :math:`{\mathbb X}, {\mathbb Y}` , 直积 :math:`{\mathbb X} \times {\mathbb Y} = \{(x, y)|x\in {\mathbb X}, y\in {\mathbb Y}\}` 的一个模糊子集 :math:`{\mathbb R}` 称为集合 :math:`\mathbb X` 到 :math:`\mathbb Y` 的一个 **模糊关系** . 用隶属函数可以表示为

   .. math::
      \mu_{\mathbb R}(x,y) : {\mathbb X} \times {\mathbb Y} \rightarrow [0, 1],

   反应了 :math:`{\mathbb X}, {\mathbb Y}` 之间的关系程度.


模糊矩阵
------------------

设集合 :math:`\mathbb X` 含有 :math:`m` 个元素, 集合 :math:`\mathbb Y` 含有 :math:`n` 个元素, 模糊子集 :math:`{\mathbb R}` 为集合 :math:`\mathbb X` 到 :math:`\mathbb Y` 的一个模糊关系, 则模糊关系可以用 :math:`m\times n` 的矩阵表示, 称为 **模糊关系矩阵** 或 **隶属矩阵**, 简称 **模糊矩阵** (Fuzzy Matrix).

.. math::
   {\mu _{\mathbb R}} = \left[ {\begin{array}{cccc}
   {{\mu _{\mathbb R}}({x_1},{y_1})}&{{\mu _{\mathbb R}}({x_1},{y_2})}& \cdots &{{\mu _{\mathbb R}}({x_1},{y_n})}\\
   {{\mu _{\mathbb R}}({x_2},{y_1})}&{{\mu _{\mathbb R}}({x_2},{y_2})}& \cdots &{{\mu _{\mathbb R}}({x_2},{y_n})}\\
    \vdots & \vdots & \vdots & \vdots \\
   {{\mu _{\mathbb R}}({x_m},{y_1})}&{{\mu _{\mathbb R}}({x_m},{y_2})}& \cdots &{{\mu _{\mathbb R}}({x_m},{y_n})}
   \end{array}} \right]


模糊关系的性质
------------------

- 自反性: :math:`\mu_{\mathbb R}(x, x) = 1`
- 对称性: :math:`\mu_{\mathbb R}(x, y) = \mu_{\mathbb R}(y, x)`
- 传递性:


