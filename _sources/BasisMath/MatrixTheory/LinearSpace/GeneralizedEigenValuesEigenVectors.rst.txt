.. _Section-GeneralizedEigenValuesEigenVectors:

广义特征值与特征向量
=====================



广义特征值与特征向量
--------------------------

矩阵的广义特征值与特征向量
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _def-GeneralizedEigenValuesEigenVectors:

.. proof:definition:: 矩阵的广义特征值与特征向量

   设有矩阵 :math:`{\bm A}, {\bm B}` , 且对于数域 :math:`{\mathbb K}` 中的数 :math:`\lambda` , 若存在非零向量 :math:`{\bm x} \in {\mathbb V}^n` 满足如下条件

   .. math::
      {\bm A}{\bm x} = \lambda {\bm B}{\bm x}

   则称 :math:`\lambda` 为矩阵 :math:`{\bm A}` 相对于矩阵 :math:`{\bm B}` 的 **广义特征值** ( Generalized Eigenvalue ) , :math:`{\bm x}` 为 :math:`{\bm A}` 相对于矩阵 :math:`{\bm B}` 的属于特征值 :math:`\lambda` 的 **广义特征向量** ( Generalized Eigenvector ). 上述问题称为 **广义特征值问题** ( :term:`Generalized eigenvalue problem` ) .

特征值与特征向量的关系
~~~~~~~~~~~~~~~~~~~~~~~~~~~~



广义特征值问题的等价形式
~~~~~~~~~~~~~~~~~~~~~~~~~~~


第一种形式
^^^^^^^^^^^^

当 :math:`{\bm B}` 正定即可逆时, 有第一种等价形式

.. math::
   {\bm B}^{-1}{\bm A}{\bm x} = \lambda{\bm x},

此时, 广义特征值问题退化为矩阵 :math:`{\bm B}^{-1}{\bm A}` 的普通特征值问题.



第二种形式
^^^^^^^^^^^^

当 :math:`{\bm B}` 正定即可逆时, 对其进行 Cholesky 分解 :math:`{\bm B} = {\bm G}{\bm G}^T` , 其中 :math:`{\bm G}` 是下三角矩阵, 则有

.. math::
   {\bm A}{\bm x} = \lambda{\bm G}{\bm G}^T{\bm x},

令 :math:`{\bm y} = {\bm G}^T{\bm x}` , 则 :math:`{\bm x} = ({\bm G}^{-1})^T{\bm y}` , 则广义特征值问题变为

.. math::
   {\bm S}{\bm y} = \lambda{\bm y}

此时, 广义特征值问题退化为矩阵 :math:`{\bm S} = {\bm G}^{-1}{\bm A}({\bm G}^{-1})^T` 的普通特征值问题.




实例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~















