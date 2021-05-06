.. _Section-NormApplication:

范数的应用
=====================


矩阵的谱半径
-----------------

什么是谱半径
~~~~~~~~~~~~~~

.. _def-SpectralRadius:

.. proof:definition:: 矩阵的谱半径

   设 :math:`{\bm A} \in {\mathbb C}^{n\times n}` 的 :math:`n` 个特征值为 :math:`\lambda_1, \lambda_2, \cdots, \lambda_n` , 称

   .. math::
      \rho({\bm A}) =  \mathop {\max }\limits_i |\lambda_i|

   为 **谱半径** (:term:`Spectral Radius`).

.. hint::
   1. 矩阵 :math:`{\bm A}` 的谱半径是正实数
   2. 矩阵 :math:`{\bm A}` 的谱半径是矩阵的特征值的模值, 且为最大的那个
   3. 矩阵 :math:`{\bm A}` 的2-范数是 :math:`{\bm A}^H{\bm A}` 的最大特征值的平方根
   4. 矩阵 :math:`{\bm A}` 的谱半径不超过矩阵的范数 :math:`\|{\bm A}\|`

性质
~~~~~~~~~~

#. 设 :math:`{\bm A} \in {\mathbb C}^{n\times n}` , 则对于 :math:`{\mathbb C}^{n\times n}` 上的任意矩阵范数 :math:`\|\cdot\|_M` , 都有

   .. math::
      \rho({\bm A}) \leq \|{\bm A}\|_M


   .. hint::
      取与矩阵范数 :math:`\|\cdot\|_M` 相容的向量范数 :math:`\|\cdot\|_V` , 设矩阵 :math:`{\bm A}` 的特征值 :math:`\lambda` 对应的特征向量为 :math:`{\bm x}` , 则

      .. math::
         |\lambda|\|{\bm x}\|_V = \|\lambda{\bm x}\|_V = \|{\bm{Ax}}\|_V \leq \|{\bm A}\|_M \|{\bm x}\|_V

      由 :math:`{\bm x} \neq {\bm 0}` 得, :math:`\rho({\bm A}) \leq \|{\bm A}\|_M` .
#. 设 :math:`{\bm A} \in {\mathbb C}^{n\times n}` , 则 :math:`\rho({\bm A}^k) = [\rho({\bm A})]^k`
#. 设 :math:`{\bm A} \in {\mathbb C}^{n\times n}` , 则 :math:`\|{\bm A}\|_2 = \rho^{1/2}({\bm A}^H{\bm A}) = \rho^{1/2}({\bm A} {\bm A}^H)` , 当 :math:`{\bm A}` 为Hermite正定阵时, :math:`\|{\bm A}\|_2 = \rho({\bm A})`
#. 设 :math:`{\bm A} \in {\mathbb C}^{n\times n}` , 则 :math:`\forall \epsilon \in {\mathbb Z}^+` , 存在某种矩阵范数 :math:`\|\cdot\|_M` 使得 :math:`\|{\bm A}\|_M \leq \rho({\bm A})+\epsilon`


矩阵非奇异性条件
------------------------

设 :math:`{\bm A} \in {\mathbb C}^{n\times n}` , 若对 :math:`{\mathbb C}^{n\times n}` 上的某种矩阵范数 :math:`\|\cdot\|_M` 有 :math:`\|{\bm A}\| < 1` , 则矩阵 :math:`{\bm I} - {\bm A}` 非奇异, 且

.. math::
   \|({\bm I} - {\bm A})^{-1}\|_M \leq \frac{\|{\bm I}\|_M}{1-\|{\bm A}\|_M}

.. math::
   \|{\bm I} - ({\bm I} - {\bm A})^{-1}\|_M \leq \frac{\|{\bm A}\|_M}{1-\|{\bm A}\|_M}

逆矩阵的摄动与条件数
------------------------

设 :math:`{\bm A} \in {\mathbb C}^{n\times n}` , 且非奇异, :math:`{\bm B} \in {\mathbb C}^{n\times n}`
若对 :math:`{\mathbb C}^{n\times n}` 上的某种矩阵范数 :math:`\|\cdot\|_M` , 有 :math:`\|{\bm A}^{-1}{\bm B}\|_M < 1` , 则

#. :math:`{\bm A} + {\bm B}` 非奇异
#. :math:`\|{\bm I} - ({\bm I} + {\bm A}^{-1}{\bm B})^{-1}\|_M \leq \frac{\|{\bm A}^{-1}{\bm B}\|_M}{1 - \|{\bm A}^{-1}{\bm B}\|_M}`
#. :math:`\frac{\|{\bm A}^{-1} - ({\bm A} + {\bm B})^{-1}\|_M}{\|{\bm A}\|_M} \leq \frac{\|{\bm A}^{-1} {\bm B}\|_M}{1 - \|{\bm A}^{-1}{\bm B}\|_M}`



矩阵的摄动
~~~~~~~~~~

设 :math:`{\bm A} = (a_{ij}) \in {\mathbb C}^{n\times n}` , :math:`\delta{\bm A} = (\delta a_{ij}) \in {\mathbb C}^{n\times n}` , 且 :math:`\delta a_{ij}` 表示元素 :math:`a_{ij}` 的误差, 称矩阵 :math:`\delta {\bm A}` 为 :math:`{\bm A}` 的 **摄动矩阵** .


条件数
~~~~~~~~~~~


设 :math:`{\bm A} = (a_{ij}) \in {\mathbb C}^{n\times n}` 非奇异, :math:`\|{\bm A}\|_M` 为 :math:`{\mathbb C}^{n\times n}` 上的某种矩阵范数, 则称

.. math::
   {\rm{cond}}({\bm A}) = \|{\bm A}\|_M\|{\bm A}^{-1}\|_M

为矩阵 :math:`{\bm A}` 的 **条件数** .

对应地, 当 :math:`\|{\bm A}^{-1} \delta{\bm A}\|_M < 1` 时有

#. :math:`\|{\bm I} - ({\bm I} + {\bm A}^{-1}\delta{\bm A})^{-1}\|_M \leq \frac{{\rm{cond}}({\bm A})\frac{\|\delta {\bm A}\|_M}{\|{\bm A}\|_M}}{1 - {\rm{cond}}({\bm A})\frac{\|\delta {\bm A}\|_M}{\|{\bm A}\|_M}}`
#. :math:`\frac{\|{\bm A}^{-1} - ({\bm A} + \delta{\bm A})^{-1}\|_M}{\|{\bm A}\|_M} \leq \frac{{\rm{cond}}({\bm A})\frac{\|\delta {\bm A}\|_M}{\|{\bm A}\|_M}}{1 - {\rm{cond}}({\bm A})\frac{\|\delta {\bm A}\|_M}{\|{\bm A}\|_M}}`



