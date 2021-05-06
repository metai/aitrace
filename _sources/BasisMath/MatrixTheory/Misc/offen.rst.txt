.. _Section-Often:


常用总结
=============


顺序主子式
----------

设有 :math:`n` 阶方阵 :math:`{\bm A}`

.. math::
   {\bm A} = \left[ {\begin{array}{cccc}
   {{a_{11}}}&{{a_{12}}}& \cdots &{{a_{1n}}}\\
   {{a_{21}}}&{{a_{22}}}& \cdots &{{a_{2n}}}\\
    \vdots & \vdots & \ddots & \vdots \\
   {{a_{n1}}}&{{a_{n2}}}& \cdots &{{a_{nn}}}
   \end{array}} \right]


则其 :math:`i, (0 \leq i \leq n)` 阶顺序主子式为行列式

.. math::
   D_i = \left| {\begin{array}{cccc}
   {{a_{11}}}&{{a_{12}}}& \cdots &{{a_{1i}}}\\
   {{a_{21}}}&{{a_{22}}}& \cdots &{{a_{2i}}}\\
    \vdots & \vdots & \ddots & \vdots \\
   {{a_{i1}}}&{{a_{i2}}}& \cdots &{{a_{ii}}}
   \end{array}} \right|

矩阵 :math:`{\bm A}` 所有阶顺序主子式 :math:`D_1, D_2, \cdots, D_n` 组成 :math:`{\bm A}` 的顺序主子式.


- 矩阵 :math:`{\bm A}` 为正定矩阵的充要条件是 :math:`{\bm A}` 的所有顺序主子式 :math:`D_i` 大于零;
- 矩阵 :math:`{\bm A}` 有唯一LU分解的充要条件是 :math:`{\bm A}` 的所有顺序主子式 :math:`D_i` 不等于零;


伴随矩阵
--------

**定义** :  对于方阵 :math:`{\bm A} = (a_{ij})_{n\times n}` , 将矩阵 :math:`{\bm A}` 的第 :math:`i` 行第 :math:`j` 列去掉后, 剩下的元素按原来的顺序组成一个新的 :math:`n-1` 阶矩阵, 新矩阵的行列式称为元素 :math:`a_{ij}` 的 **余子式** , 记为 :math:`M_{ij}` ;  称 :math:`A_{ij} = (-1)^{i+j}M_{ij}` 为 :math:`a_{ij}` 的代数余子式; 将所有元素的代数余子式按如下规律组成一个矩阵, 将此矩阵称为方阵 :math:`{\bm A}` 的 **伴随矩阵** , 记为: 方阵 :math:`{\bm A}^{*}`

.. math::
   {\bm A}^{*} = \left[ {\begin{array}{cccc}
   {{A_{11}}}&{{A_{21}}}& \cdots &{{A_{n1}}}\\
   {{A_{12}}}&{{A_{22}}}& \cdots &{{A_{n2}}}\\
    \vdots & \vdots & \vdots & \vdots \\
   {{A_{1n}}}&{{A_{2n}}}& \ldots &{{A_{nn}}}
   \end{array}} \right]

性质:

- :math:`{\bm A}` 可逆 :math:`\leftrightarrow` :math:`{\bm A}^*` 可逆
- :math:`{\bm A}` 可逆 :math:`\leftrightarrow` :math:`({\bm A}^{-1})^* = ({\bm A}^*)^{-1}`
- :math:`{\bm A}` 可逆 :math:`\leftrightarrow` :math:`{\bm A}^* = |{\bm A}|{\bm A}^{-1}`
- :math:`({\bm A}^*)^* = (|{\bm A}|{\bm A}^{-1})^* = |{\bm A}|^{n-1}({\bm A}^*)^{-1}`
- :math:`({\bm A}^T)^* = ({\bm A}^*)^T`
- :math:`(k{\bm A})^* = k^{n-1}{\bm A}^*`
- :math:`({\bm A}{\bm B})^* = {\bm B}^*{\bm A}^*`
- :math:`|{\bm A}^*| = |{\bm A}|^{n-1}`


矩阵的逆
--------

性质
~~~~~~~

设 :math:`{\bm A}, {\bm B}` 为 :math:`n` 阶可逆矩阵, 数 :math:`\lambda \neq 0` , 则

- :math:`({\bm A}^{-1})^{-1} = {\bm A}`
- :math:`({\bm A}^T)^{-1} = ({\bm A}^{-1})^T`
- :math:`(\lambda{\bm A})^{-1} = \lambda^{-1}{\bm A}^{-1}`
- :math:`({\bm A}{\bm B})^{-1} = {\bm B}^{-1}{\bm A}^{-1}`


特殊矩阵的逆
~~~~~~~~~~~~

二阶方阵的逆
^^^^^^^^^^^^^^


.. math::
   {\left[ {\begin{array}{ccc}a&b\\c&d\end{array}} \right]^{ - 1}} = \frac{1}{{ad - bc}}\left[ {\begin{array}{ccc}d&{ - b}\\{ - c}&a\end{array}} \right]

.. hint::
   上述公式源于伴随矩阵求逆原理.


三角矩阵的逆
^^^^^^^^^^^^^^

.. math::
	{\bm{C}} = \left[ {\begin{array}{ccccc}1&{}&{}&{}&{}\\1&1&{}&{}&{}\\1&1& \ddots &{}&{}\\ \vdots & \vdots & \ddots &1&{}\\1&1& \cdots &1&1\end{array}} \right],\;{{\bm{C}}^{ - 1}} = \left[ {\begin{array}{ccccc}1&{}&{}&{}&{}\\{ - 1}&1&{}&{}&{}\\{}&{ - 1}& \ddots &{}&{}\\{}&{}& \ddots &1&{}\\{}&{}&{}&{ - 1}&1\end{array}} \right]


求解方法
~~~~~~~~

以以下矩阵为例:

:math:`{\bm A} = \left[ {\begin{array}{ccc}1&2&2\\2&1&2\\2&0&1\end{array}} \right]`

伴随矩阵求逆
^^^^^^^^^^^^^^^^

由 :math:`{\bm A}^* = |{\bm A}|{\bm A}^{-1}` 知 :math:`{\bm A}^{-1} = \frac{1}{|{\bm A}|}{\bm A}^*` , 故可根据此式计算.

例如:

.. math::
   \begin{array}{l}
   {A_{11}} = \;\,{( - 1)^{1 + 1}}\left| {\begin{array}{ccc}
   1&2\\
   0&1
   \end{array}} \right| = 1,\;\,\,\,\,{A_{12}} = {( - 1)^{1 + 2}}\left| {\begin{array}{ccc}
   2&2\\
   2&1
   \end{array}} \right| = 2,\;\,\,\,\,{A_{13}} = {( - 1)^{1 + 3}}\left| {\begin{array}{ccc}
   2&1\\
   2&0
   \end{array}} \right| =  - 2\\
   {A_{21}} = {( - 1)^{2 + 1}}\left| {\begin{array}{ccc}
   2&2\\
   0&1
   \end{array}} \right| =  - 2,\;{A_{22}} = {( - 1)^{2 + 2}}\left| {\begin{array}{ccc}
   1&2\\
   2&1
   \end{array}} \right| =  - 3,\;{A_{23}} = {( - 1)^{2 + 3}}\left| {\begin{array}{ccc}
   1&2\\
   2&0
   \end{array}} \right| =  4\\
   {A_{31}} = {( - 1)^{3 + 1}}\left| {\begin{array}{ccc}
   2&2\\
   1&2
   \end{array}} \right| = 2,\;\;\;{A_{32}} = {( - 1)^{3 + 2}}\left| {\begin{array}{ccc}
   1&2\\
   2&2
   \end{array}} \right| =  2,\;{A_{33}} = {( - 1)^{3 + 3}}\left| {\begin{array}{ccc}
   1&2\\
   2&1
   \end{array}} \right| =  - 3
   \end{array}

从而有

.. math::
   {{\bm{A}}^{1}} = \frac{1}{|{\bm A}|}\left[ {\begin{array}{ccc}
   {{A_{11}}}&{{A_{21}}}&{{A_{31}}}\\
   {{A_{12}}}&{{A_{22}}}&{{A_{32}}}\\
   {{A_{13}}}&{{A_{23}}}&{{A_{33}}}
   \end{array}} \right] = \left[ {\begin{array}{ccc}
   1&{ - 2}&2\\
   2&{ - 3}&{ 2}\\
   { - 2}&{ 4}&{ - 3}
   \end{array}} \right]


初等行变换求逆
^^^^^^^^^^^^^^^^^

将待求逆矩阵与单位矩阵拼成一个矩阵, 对新矩阵只进行 **初等行变换** , 使得待求逆矩阵部分变为单位矩阵, 那么对应的原始的单位阵变为待求逆矩阵的逆, 即

.. math::
   [{\bm A} | {\bm I}] \rightarrow [{\bm I} | {\bm A}^{-1}]

例如:

.. figure:: ../../../_static/figs/BasisMath/MatrixTheory/Misc/Offen/demoElementaryTransformationINV.png
   :scale: 60 %
   :alt: some text
   :align: center

   初等变换求逆

   初等变换求逆


Sherman-Morrison-Woodbury公式
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设 :math:`{\bm A}\in {\mathbb R}^{n\times n}` 非奇异, :math:`{\bm u}, {\bm v}\in {\mathbb R}^n` , 则有 Sherman-Morrison 等式

.. math::
   \left({\bm A} + {\bm u} {\bm v}^{T}\right)^{-1}={\bm A}^{-1}-{\bm A}^{-1} {\bm u}\left({\bm I} + {\bm v}^{T} {\bm A}^{-1} {\bm u}\right)^{-1} {\bm v}^{T} {\bm A}^{-1}.
   :label: equ-Sherman-Morrison

.. hint::
   Sherman-Morrison等式可以通过求解线性方程组 :math:`({\bm A} + {\bm u}{\bm v}^T){\bm x} = {\bm b}` 得到.


由 Sherman-Morrison 公 :eq:`equ-Sherman-Morrison` , 令 :math:`{\bm U}\in {\mathbb R}^{n\times k}` , :math:`{\bm V}\in {\mathbb R}^{n\times k}` , 则有 Sherman-Morrison-Woodbury 等式

.. math::
   \left({\bm A} + {\bm U} {\bm V}^{T}\right)^{-1}={\bm A}^{-1}-{\bm A}^{-1} {\bm U}\left({\bm I} + {\bm V}^{T} {\bm A}^{-1} {\bm U}\right)^{-1} {\bm V}^{T} {\bm A}^{-1}.
   :label: equ-Sherman-Morrison-Woodbury

矩阵的秩
-------------

性质
~~~~~~~~~

- :math:`0 \leq {\rm rank}({\bm A}_{m \times n}) \leq {\rm min} \{m, n\}`
- :math:`{\rm rank}({\bm A}^T) = {\rm rank}({\bm A})`
- :math:`{\rm rank}({\bm A}{\bm B}) \leq {\rm min}\{ {\rm rank}({\bm A}), {\rm rank}({\bm B})\}`
- :math:`{\rm rank}({\bm A}+{\bm B}) \leq {\rm rank}({\bm A}) + {\rm rank}({\bm B})`
- :math:`{\rm max}\{ {\rm rank}({\bm A}), {\rm rank}({\bm B})\} \leq {\rm rank}({\bm A}, {\bm B}) \leq {\rm rank}({\bm A}) + {\rm rank}({\bm B})`
- 若 :math:`{\bm A} \sim {\bm B}` , 则 :math:`{\rm rank}({\bm A}) = {\rm rank}({\bm B})`
- 若 :math:`{\bm P} , {\bm Q}` 可逆 , 则 :math:`{\rm rank}({\bm P}{\bm A}{\bm Q}) = {\rm rank}({\bm A})`
- 若 :math:`{\bm A}_{m\times n}{\bm B}_{n\times l} = {\bm O}` , 则 :math:`{\rm rank}({\bm A}) + {\rm rank}({\bm B}) \leq n`
- 若 :math:`{\bm A}` 为列满秩矩阵, 且 :math:`{\bm A}{\bm B} = {\bm O}` , 则 :math:`{\bm B} = {\bm O}`


矩阵的迹行列式特征值
-----------------------

- 方阵 :math:`{\bm A}` 的行列式与特征值的关系: :math:`|{\bm A}| = \lambda_1\lambda_2 \cdots \lambda_n`
- 方阵 :math:`{\bm A}` 的迹与特征值的关系: :math:`{tr}({\bm A}) = \lambda_1 + \lambda_2 + \cdots + \lambda_n`




