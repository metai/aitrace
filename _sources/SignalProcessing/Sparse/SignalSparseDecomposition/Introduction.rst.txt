.. _Section-IntroductionSignalSparseDecompositionSparseSignalProcessing:

简介
=====================


什么是信号稀疏分解
-------------------

与频谱估计类似, 信号分解 (:term:`Signal Decomposition`) 目的在于将信号分解成原子 (:term:`atom`) 或基 (basis) 的组合(线性或非线性), 信号稀疏分解 (:term:`Signal Sparse Decomposition`) 目的在于将信号分解成少量原子 (:term:`atom`) 基 (basis) 的组合(线性或非线性)

假设有过完备字典 :math:`{\bm A} = [{\bm a}_1, {\bm a}_2, \cdots, {\bm a}_n]\in {\mathbb R}^{m\times n}`, 其中每一列称为一个原子, 信号稀疏分解是指将信号 :math:`{\bm y}` 分解为过完备字典 :math:`{\bm A}` 中的尽可能少( :math:`{\bm x}` 稀疏)的原子的线性组合

.. math::
   {\bm y} = {\bm A}{\bm x} = {x}_1 {\bm a}_1 + {x}_2 {\bm a}_2 + \cdots {x}_n {\bm a}_n,
   :label: equ-OmpProb

其中, :math:`{\bm x}` 仅有少量元素非零(稀疏), 称为稀疏分解系数. 对于稀疏信号恢复问题, :math:`{\bm x}` 被当作稀疏信号, :math:`{\bm y}` 被当作观测信号, 字典相当于观测矩阵. 若考虑噪声成份, 则有

.. math::
   {\bm y} = {\bm A}{\bm x} + {\bm n},

其中, :math:`{\bm n} \in {\mathbb R}^{m\times 1}` 为噪声向量.

.. hint::
   对于字典 :math:`{\bm D}\in {\mathbb C}^{m\times n}`, 完备字典是指字典 :math:`{\bm D}` 中的所有原子恰好能够张成 :math:`m` 维空间, 当 :math:`n >> m` 且 :math:`{\bm D}` 中的原子可以张成 :math:`m` 维空间时, 称 :math:`{\bm D}` 是过完备的.

   上述分解中的过完备字典也可以是完备字典, 比如DCT逆变换对应的矩阵, 那么稀疏系数 :math:`\bm x` 对应信号 :math:`\bm y` 的频率成分.


常见稀疏分解算法
-------------------

匹配追踪, 正交匹配追踪





