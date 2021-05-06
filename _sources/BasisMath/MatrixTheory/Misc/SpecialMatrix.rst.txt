常见矩阵概念
=============


奇异非奇异
----------


奇异(singular)与非奇异(non-singular)和不可逆(non-invertible)与可逆(invertible)是相同的,

- 首先是指方阵 :math:`{\bm A}^{n\times n}` ;
- 非奇异阵 :math:`\leftrightarrow` 可逆矩阵 :math:`\leftrightarrow` 满秩 :math:`\leftrightarrow` 行列式不等于零 :math:`\|{\bm A}\| {\neq} 0` :math:`\leftrightarrow` 正定阵;
- 奇异阵 :math:`\leftrightarrow` 非可逆矩阵 :math:`\leftrightarrow` 非满秩 :math:`\leftrightarrow` 行列式等于零 :math:`\|{\bm A}\| = 0` :math:`\leftrightarrow` 非正定阵;



特殊矩阵
----------

概念汇总
~~~~~~~~~~

#. 对称矩阵

   - 实对称: :math:`{\bm A}^T = {\bm A}` , :math:`{\bm A}\in {\mathbb R}^{n\times n}`

   - 酉对称: :math:`{\bm A}^H = {\bm A}` , :math:`{\bm A}\in {\mathbb C}^{n\times n}`, 也叫Hermite矩阵

   - 复对称: :math:`{\bm A}^T = {\bm A}` , :math:`{\bm A}\in {\mathbb C}^{n\times n}`

#. 正规矩阵 ( :term:`Normal Matrix` )

   - 正规矩阵: :math:`{\bm A}^H{\bm A} = {\bm A}{\bm A}^H` , :math:`{\bm A}\in {\mathbb C}^{n\times n}`

   - 正交矩阵, 酉矩阵, 对角矩阵, 实对称矩阵及酉对称矩阵均为正规矩阵

#. 正交矩阵

   - 实正交矩阵: :math:`{\bm A}^T{\bm A} = {\bm A}{\bm A}^T = {\bm I}` , :math:`{\bm A}\in {\mathbb R}^{n\times n}`

   - 复正交矩阵: :math:`{\bm A}^H{\bm A} = {\bm A}{\bm A}^H = {\bm I}` , :math:`{\bm A}\in {\mathbb C}^{n\times n}` , 也叫酉矩阵


`Hermitian matrix <http://en.volupedia.org/wiki/Hermitian_matrix>`_  也叫自伴随矩阵 (self-adjoint matrix)

结论
~~~~~~~~~~~~

设 :math:`{\bm A}\in {\mathbb C}_{r}^{m\times n} , (r>0)` , 则

#. :math:`{\bm A}^H{\bm A}` 是 Hermite矩阵, 即 :math:`({\bm A}^H{\bm A})^H = {\bm A}^H{\bm A}` , 其特征值为非负实数;
#. :math:`{\rm rank}({\bm A}^H{\bm A}) = {\rm rank}({\bm A}{\bm A}^H) = {\rm rank}({\bm A})` ;
#. :math:`{\bm A} = {\bm 0}` 的充要条件是 :math:`{\bm A}^H{\bm A} = {\bm 0}` , 此时, :math:`r=0`

