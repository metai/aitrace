.. _Section-MatchingPursuitSignalSparseDecompositionSparseSignalProcessing:


匹配追踪
=================


什么是匹配追踪
---------------

匹配追踪 (:term:`Matching Pursuit` , MP) 最初被提出来是用于信号的稀疏分解 :cite:`1993.MP.Mallat`, 匹配追踪在很多领域中有应用, 匹配追踪用于量子模拟 :cite:`2003JChPh.118.6720W`.




匹配追踪算法
----------------


匹配追踪算法步骤见算法1.

.. note:: 算法1: 匹配追踪算法步骤

   输入: 列归一化过完备字典矩阵 :math:`{\bm A} \in {\mathbb R}^{m \times n}`, 待分解信号 :math:`{\bm y}\in {\mathbb R}^{m \times 1}`, 稀疏度 :math:`K`, 容忍残差模值 :math:`\epsilon`

   输出: 稀疏分解系数 :math:`\hat{\bm x} \in {\mathbb R}^{n\times 1}`, 索引集合 :math:`{\mathbb I} \subset {\mathbb U} = \{1,2,\cdots,n\}`, 待分解信号近似 :math:`\hat{\bm y}` 和残差向量 :math:`{\bm r} = {\bm y} - \hat{\bm y}`

   Step1: 初始化稀疏信号 :math:`{\bm x}_{0} = {\bm 0}`, 残差 :math:`{\bm r}_{0} = {\bm y} - \bm{A}{\bm x}_0 = {\bm y}`, 索引集合(支撑) :math:`{\mathbb I}_{0} = \empty`, 迭代计数器 :math:`k = 1`.

   Step2: 选择与残差最相关的原子, 即求解索引 :math:`\lambda_k` 满足优化问题

   .. math::
      i_k = \arg \max _{i\in{\mathbb U}} |{\bm A}_i^T{\bm r}_{k-1}|.

   Step3: 更新索引集 :math:`{\mathbb I}_{k} = {\mathbb I}_{k-1} \cup {i_k}`

   Step4: 更新稀疏分解系数 :math:`x[i_k] = {\langle {\bm A}_{i_k}, {\bm r}_{k-1} \rangle} = {\bm A}_{i_k}^T{\bm r}_{k-1}`

   Step5: 计算新的残差 :math:`{\bm r}_{k} = {\bm r}_{k-1} - {\bm A}_{i_k}x[i_k]`

   Step6: 更新迭代计数器 :math:`k = k + 1` 若 :math:`k<K` 且 :math:`||{\bm r}||_2 < \epsilon` , 重复 Step2 至 Step6, 否则停止迭代, 转 Step7.

   Step7: 输出 :math:`\hat{\bm x} = \bm{x}`, :math:`\hat{\bm y} = \hat{\bm y}_{k}`, :math:`{\bm r} = {\bm r}_k`. 其中, :math:`\hat{\bm x}` 在位置 :math:`{\mathbb I}_k` 处非零.





实验与分析
------------------






