.. _Section-SparsitySparsitySamplingReconSparseSignalProcessing:

稀疏性分析
=====================

稀疏信号
-------------

.. _defkSparseSignal:

.. proof:definition:: 稀疏信号 (Sparse Signal)

   若信号 :math:`\bm x` 仅含有 :math:`k` 个非零元素, 即 :math:`\|{\bm x}\|_0 \leq k`, 则称该信号为 :math:`k` 稀疏的. 对于非稀疏信号 :math:`\bm x`, 若存在一组基 :math:`\bm \Psi`, 使得 :math:`{\bm x} = {\bm \Psi}{\bm \alpha}`, 且 :math:`\|{\bm \alpha}\|_0 \leq k`, 此时, 仍称该信号为 :math:`k` 稀疏的. 进一步地, 定义 :math:`k` 稀疏信号集合

   .. math::
      {\mathbb V}_k = \left\{{\bm x} \big| \|{\bm x}\|_0 \leq k\right\}.


.. warning::
    在数字信号处理中, 信号常常由向量表示, 是否有其它表示方法?




