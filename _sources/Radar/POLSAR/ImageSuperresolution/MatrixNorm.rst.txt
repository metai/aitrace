.. _Section-MatrixNorm:

矩阵范数
=====================

概念与内涵
-----------------

若对于 :math:`{\bm A}\in {\mathbb C}^{m\times n}` , 定义实值函数 :math:`\|{\bm A}\|` , 满足以下条件  

#. 非负性: :math:`\|{\bm A}\| \geq 0` , 当且仅当 :math:`{\bm A} = {\bm 0}` 时, 等号成立; 
#. 齐次性: :math:`\|k \bm A \| = |k|\|\bm A\|` , ( :math:`k\in {\mathbb C}` 
#. 三角不等式: :math:`\|{\bm A} + {\bm B}\| \leq \|{\bm A}\| + \|{\bm B}\|` , ( :math:`{\bm{B} \in {\mathbb C}^{m\times n}}` ) 
#. 相容性: :math:`\|{\bm A}{\bm B}\| \leq \|A\|\|B\|` ( :math:`{\bm B} \in {\bm C}^{n\times l}` )

若满足1, 2, 3 则称 :math:`\|{\bm A}\|` 为矩阵 :math:`{\bm A}` 的 **广义矩阵范数** .       
若满足1, 2, 3, 4 则称 :math:`\|{\bm A}\|` 为矩阵 :math:`{\bm A}` 的 **矩阵范数** .       


.. hint::
   - 范数是实数, 为什么不定义复数呢?
   - 注意与内积的定义比较
   - 注意与向量范数的定义比较


矩阵范数与向量范数的相容性
-----------------------------

设有 :math:`{\mathbb C}^{m\times n}` 上的矩阵范数 :math:`\|\cdot\|_M` 和 :math:`{\mathbb C}^m` 与 :math:`{\mathbb C}^n` 上的同类向量范数 :math:`\|\cdot\|_{V}` , 若

.. math::
   \|{\bm A}{\bm x}\|_V \leq \|{\bm A}\|_M \|{\bm x}\|_V  , ( \forall {\bm A}\in {\mathbb C}^{m\times n}, \forall {\bm x}\in {\mathbb C}^n )  

则称矩阵范数  :math:`\|\cdot\|_M` 与向量范数 :math:`\|\cdot\|_{V}` **相容** .



常见矩阵范数
---------------------


设有 :math:`{\bm A} = (a_{ij})_{m\times n} \in {\mathbb C}^{m\times n}` ,则  

.. math::
      \|{\bm A}\|_F = \left( \sum_{i=1}^m\sum_{j=1}^n |a_{ij}|^2 \right)^{1/2} = ({\rm{tr}}({\bm A}^H {\bm A}))^{1/2}

是 :math:`{\mathbb C}^{m\times n}` 上的矩阵范数, 且与向量范数 :math:`\|\cdot\|_2` 相容. 也称为 **Frobenius 范数**
, 或简称 **F-范数** .

定理: 给矩阵左乘或右乘一个酉矩阵其F-范数不变, 即设 :math:`{\bm A}\in {\mathbb C}^{m\times n}` , 且 :math:`{\bm P}\in {\mathbb C}^{m\times m}` , :math:`{\bm Q}\in {\mathbb C}^{n\times n}` 为酉矩阵, 则

.. math::
   \|{\bm P}{\bm A}\|_F = \|{\bm A}\|_F = \|{\bm A}{\bm Q}\|_F


从属范数
~~~~~~~~~~~~~~~~~~~~~~

矩阵范数与向量范数密切相关, 一一对应.

设有 :math:`{\mathbb C}^m, {\mathbb C}^n` 上的同类向量范数 :math:`\|\cdot\|` , :math:`{\bm A}\in {\mathbb C}^{m\times n}` , 则函数

.. math::
   \|{\bm A}\| = \mathop {\max }\limits_{\|{\bm x}\|=1} \|{\bm A}{\bm x}\|

是 :math:`{\mathbb C}^{m\times n}` 上的矩阵范数, 且与向量范数 :math:`\|\cdot\|` 相容. 由上式给出的矩阵范数称为 **由向量导出的矩阵范数** , 简称 **从属范数** .  


据此可以定义以下常见矩阵范数:
 
- **∞-范数** 或 **行和范数** : :math:`\|{\bm A}\|_{\infty} = \mathop {\max }\limits_i \sum_{j=1}^n|a_{ij}|`  
- **1-范数** 或 **列和范数** : :math:`\|{\bm A}\|_1 = \mathop {\max }\limits_j \sum_{i=1}^m|a_{ij}|`  
- **2-范数** 或 **谱范数**  : :math:`\|{\bm A}\|_2 = \sqrt{\lambda_1} = \sqrt{{\rm max}\lambda({\bm A}^H {\bm A} )} = {\rm max}\sigma_i` , ( :math:`\lambda_1` 为 :math:`{\bm A}^H{\bm A}` 的最大特征值 ) 


.. hint::
   设 :math:`{\bm A}\in {\mathbb C}_r^{m\times n} , r>0` , 则 :math:`{\bm A}^H{\bm A}` 为正定阵, 其特征值均为非负实数, 奇异值 :math:`\sigma_i = \sqrt{\lambda_i}` , :math:`(i = 1, 2, \cdots, n)`     


.. note::
   
   `谱范数正则（Spectral Norm Regularization）的理解 <https://blog.csdn.net/StreamRock/article/details/83539937>`_  

   谱范数正则（Spectral Norm Regularization，简称为SNR）最早来自于2017年5月日本国立信息研究所Yoshida的一篇论文[2]，他们后续又于2018年2月再再arXiv发了一篇SNR用于Gan的论文[3]，以阐明SNR的有效性。因为当SGD（统计梯度下降）的批次（Batch size）一大的时候，其泛化性能却会降低，SNR能有效地解决这一问题。

   SNR的讨论是从网络的泛化（（Generalizability））开始的。对于Deep Learning而言，泛化是一个重要的性能指标，直觉上它与扰动（Perturbation）的影响有关。我们可以这样理解：局部最小点附近如果是平坦（flatness）的话，那么其泛化的性能将较好，反之，若是不平坦（sharpness）的话，稍微一点变动，将产生较大变化，则其泛化性能就不好。因此，我们可以从网络对抗扰动的性能入手来提升网络的泛化能力。
