.. _Section-GeneralizedInverseDefinitionProperties:

广义逆的定义与性质
=====================

Moore-Penrose 逆
------------------

概念
~~~~~~~~~~~~

设有矩阵 :math:`{\bm A} \in {\mathbb C}^{m\times n}` , 矩阵 :math:`{\bm X} \in {\mathbb C}^{n\times m}` 和以下 Penrose 方程:

(1) :math:`{\bm A}{\bm X}{\bm A} = {\bm A}`
(2) :math:`{\bm X}{\bm A}{\bm X} = {\bm X}`
(3) :math:`({\bm A}{\bm X})^H = {\bm A}{\bm X}`
(4) :math:`({\bm X}{\bm A})^H = {\bm X}{\bm A}`

若矩阵 :math:`{\bm X}` 满足 Penrose 方程组中的 :math:`(i), (j), \cdots, (k)` 方程, 则称 :math:`{\bm X}` 为 :math:`{\bm A}` 的 :math:`\{i, j, \cdots, k\}` -逆, 记为 :math:`{\bm A}^{(i,j\cdots,k)}` , 全体记为 :math:`{\bm A}{\{i,j\cdots,k\}}` .

若矩阵 :math:`{\bm X}` 满足 Penrose 方程组中的 :math:`(1), (2), (3), (4)` 方程, 则称 :math:`{\bm X}` 为 :math:`{\bm A}` 的 Moore-Penrose 逆, 记为 :math:`{\bm A}^{+}` .

易知:

- :math:`{\bm A}^{+} = {\bm A}^{(1,2,3,4)}`
- 满足Penrose方程的广义逆共有 :math:`C_4^1 + C_4^2 + C_4^3 + C_4^4 = 15` 类


结论与性质
~~~~~~~~~~~~~


#. 一般地, :math:`{\bm A}{\bm A}^+ \neq {\bm A}^+{\bm A} \neq {\bm I}`
#. 若矩阵 :math:`{\bm A}` 非奇异, 则 :math:`{\bm A}^{+} = {\bm A}^{-1}`
#. 若矩阵 :math:`{\bm A}\in {\mathbb C}^{m\times n}` , 则 :math:`{\bm A}^{+}` 存在且唯一
#. 若矩阵 :math:`{\bm A}\in {\mathbb C}^{m\times n}` , 则 :math:`{\bm Y} = ({\bm A}^H {\bm A})^{(1)}{\bm A}^H` :math:`\in {\bm A}\{1,2,3\}`
#. 若矩阵 :math:`{\bm A}\in {\mathbb C}^{m\times n}` , 则 :math:`{\bm Y} = {\bm A}^H({\bm A}{\bm A}^H)^{(1)}`  :math:`\in {\bm A}\{1,2,4\}`
#. 若矩阵 :math:`{\bm A}\in {\mathbb C}_n^{m\times n}` , 则 :math:`{\bm A}^+ = ({\bm A}^H {\bm A})^{-1}{\bm A}^H`
#. 若矩阵 :math:`{\bm A}\in {\mathbb C}_m^{m\times n}` , 则 :math:`{\bm A}^+ = {\bm A}^H({\bm A}{\bm A}^H)^{-1}`
#. 若矩阵 :math:`{\bm A}\in {\mathbb C}^{m\times n}` , :math:`{\bm B}\in {\bm C}^{n\times l}` , 不一定有 :math:`({\bm{AB}})^+ = {\bm B}^+{\bm A}^+`


.. hint::
   如设 :math:`{\bm A} = (1, 0)` , :math:`{\bm B} = (1, 1)^T` , 则 :math:`{\bm{AB}} = [1]` , :math:`({\bm{AB}})^+ = [1]` , :math:`{\bm A}^+ = (1, 0)^T` , :math:`{\bm B}^+ = (1/2, 1/2)` , :math:`{\bm A}^+{\bm B}^+ = [1/2]`