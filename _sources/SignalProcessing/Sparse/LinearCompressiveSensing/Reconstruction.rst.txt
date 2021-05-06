.. _Section-ReconstructionLinearCompressiveSensingSparseSignalProcessing:

线性压缩感知重构
=====================





重构算法
------------------

OMP
~~~~~~~~~~~~~~~~~~

.. note:: 算法1: 正交匹配追踪算法步骤

   输入: 观测矩阵 :math:`{\bm \Phi} \in {\mathbb R}^{m \times n}`, 观测向量 :math:`{\bm y}\in {\mathbb R}^{m \times 1}`, 待恢复信号稀疏度 :math:`k`

   输出: 估计信号 :math:`\hat{\bm x} \in {\mathbb R}^{n\times 1}`, 索引集合 :math:`{\mathbb I}_{k} \subset {\mathbb U} = \{1,2,\cdots,n\}`, 观测向量近似 :math:`\hat{\bm y}` 和残差向量 :math:`{\bm r} = {\bm y} - \hat{\bm y}`

   Step1: 初始化残差 :math:`{\bm r}_0 = {\bm y}`, 索引集合 :math:`{\mathbb I}_{0} = \empty`, 迭代计数器 :math:`t = 1`.

   Step2: 求解索引 :math:`\lambda_t` 满足优化问题

   .. math::
        i_t = \arg \max _{j\in{\mathbb U}} |{\bm \phi}_j{\bm r}_{t-1}|.

   Step3: 更新索引集 :math:`{\mathbb I}_{t} = {\mathbb I}_{t-1} \cup {i_t}`.

   Step4: 求解新的最小二乘优化问题

            .. math::
                 {\bm x}_t = \arg \max _{\bm x} \|{\bm y} - {\bm \Phi}_{{\mathbb I}_t}{\bm x}\|_2^2

           求得的解为 :math:`{\bm x}_t = ({\bm \Phi}_{{\mathbb I}_t}^T{\bm \Phi}_{{\mathbb I}_t})^{-1}{\bm \Phi}_{{\mathbb I}_t}^T{\bm y}`

   Step5: 计算新的投影近似, 残差

              .. math::
                  \begin{aligned} \hat{\bm y}_{t} &=\bm{\Phi}_{{\mathbb I}_t} \bm{x}_{t} \\ \bm{r}_{t} &=\bm{y}-\hat{\bm y}_{t} \end{aligned}.

   Step6: 更新迭代计数器 :math:`t = t + 1` 若 :math:`t<k`, 重复 Step2 至 Step5, 否则停止迭代, 转 Step7.

   Step7: 输出 :math:`\hat{\bm x} = \bm{x}_{t}`, :math:`\hat{\bm y} = \hat{\bm y}_{t}`, :math:`{\bm r} = {\bm r}_t`. 其中, :math:`\hat{\bm x}` 在位置 :math:`{\mathbb I}_t` 处非零.

.. warning:: 待查证是否有相关文献, 没有的话, 是否可以发表
   实际迭代过程中, 在求解逆矩阵 :math:`({\bm \Phi}_{{\mathbb I}_t}^T{\bm \Phi}_{{\mathbb I}_t})^{-1}` 时容易出现其奇异的情况, 可以通过求解 :math:`({\bm \Phi}_{{\mathbb I}_t}^T{\bm \Phi}_{{\mathbb I}_t} \alpha {\bm I})^{-1}` 来代替, 其中 :math:`\alpha > 0`.


.. hint::
   记 :math:`{\bm P}_t = {\bm \Phi}({\bm \Phi}_{{\mathbb I}_t}^T{\bm \Phi}_{{\mathbb I}_t})^{-1}{\bm \Phi}_{{\mathbb I}_t}^T`, 易知 :math:`{\bm P}_t` 为正交投影矩阵. 从而

   .. math::
       \begin{aligned} {\bm x}_t &= {\bm P}_t {\bm y} \\ {\bm r}_t &= {\bm y} - {\bm x}_t \end{aligned}



