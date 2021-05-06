.. _Section-OrthogonalMatchingPursuitSignalSparseDecompositionSparseSignalProcessing:


正交匹配追踪
=================


什么是正交匹配追踪
-----------------

正交匹配追踪 (:term:`Orthogonal Matching Pursuit` , OMP) 是一种信号稀疏分解方法, 由 Pati 等人 :cite:`1993:PatiOMP` 于1993年提出, OMP被广泛用于稀疏信号恢复 :cite:`Tropp.2007`. 稀疏分解旨在将信号分解为过完备字典中的尽可能少(稀疏)的原子的线性组合, 从而获得信号的简洁有效的表示.

`good <https://blog.csdn.net/alec1987/article/details/79413055>`_



正交匹配追踪算法
--------------------


正交匹配追踪算法步骤见算法1 :cite:`Tropp.2007`.

.. note:: 算法1: 正交匹配追踪算法步骤

   输入: 列归一化过完备字典矩阵 :math:`{\bm A} \in {\mathbb R}^{m \times n}`, 观测向量 :math:`{\bm y}\in {\mathbb R}^{m \times 1}`, 待恢复信号稀疏度 :math:`K`, 容忍残差模值 :math:`\epsilon`

   输出: 待估计稀疏信号 :math:`\hat{\bm x} \in {\mathbb R}^{n\times 1}`, 索引集合 :math:`{\mathbb I} \subset {\mathbb U} = \{1,2,\cdots,n\}`, 观测向量近似 :math:`\hat{\bm y}` 和残差向量 :math:`{\bm r} = {\bm y} - \hat{\bm y}`

   Step1: 初始化稀疏信号 :math:`{\bm x}_{0} = {\bm 0}`, 残差 :math:`{\bm r}_{0} = {\bm y} - \bm{A}{\bm x}_0 = {\bm y}`, 索引集合(支撑) :math:`{\mathbb I}_{0} = \empty`, 迭代计数器 :math:`k = 1`.

   Step2: 选择与残差最相关的原子, 即求解索引 :math:`i_k` 满足优化问题

   .. math::
   	  i_k = \arg \max _{i\in{\mathbb U}} |{\bm A}_i^T{\bm r}_{k-1}|.

   Step3: 更新索引集 :math:`{\mathbb I}_{k} = {\mathbb I}_{k-1} \cup {i_k}`.

   Step4: 求解新的最小二乘优化问题

         .. math::
            {\bm x}_k = \arg \min _{\bm x} \|{\bm y} - {\bm A}_{{\mathbb I}_k}{\bm x}\|_2^2

         求得的稀疏系数解为 :math:`{\bm x}_k = ({\bm A}_{{\mathbb I}_k}^T{\bm A}_{{\mathbb I}_k})^{-1}{\bm A}_{{\mathbb I}_k}^T{\bm y}`

   Step5: 计算新的投影近似, 残差

         .. math::
            \begin{aligned} \hat{\bm y}_{k} &=\bm{A}_{{\mathbb I}_k} \bm{x}_{k} \\ \bm{r}_{k} &=\bm{y}-\hat{\bm y}_{k} \end{aligned}.

   Step6: 更新迭代计数器 :math:`k = k + 1` 若 :math:`k<K` 且 :math:`||{\bm r}||_2 < \epsilon`, 重复 Step2 至 Step5, 否则停止迭代, 转 Step7.

   Step7: 输出 :math:`\hat{\bm x} = \bm{x}_{k}`, :math:`\hat{\bm y} = \hat{\bm y}_{k}`, :math:`{\bm r} = {\bm r}_k`. 其中, :math:`\hat{\bm x}` 在位置 :math:`{\mathbb I}_k` 处非零.

.. warning:: 待查证是否有相关文献, 没有的话, 是否可以发表
   实际迭代过程中, 在求解逆矩阵 :math:`({\bm A}_{{\mathbb I}_k}^T{\bm A}_{{\mathbb I}_k})^{-1}` 时容易出现其奇异的情况, 可以通过求解 :math:`({\bm A}_{{\mathbb I}_k}^T{\bm A}_{{\mathbb I}_k} + \alpha {\bm I})^{-1}` 来代替, 其中 :math:`\alpha > 0`.


.. hint::
   记 :math:`{\bm P}_k = {\bm A}_{{\mathbb I}_k}({\bm A}_{{\mathbb I}_k}^T{\bm A}_{{\mathbb I}_k})^{-1}{\bm A}_{{\mathbb I}_k}^T`, 易知 :math:`{\bm P}_k` 为正交投影矩阵(线性投影), 将向量投影到由 :math:`{\bm A}_{{\mathbb I}_k}` 的元素(类比坐标系)张成的线性空间中, 从而 :math:`{\hat{\bm y}}_k = {\bm A}_{{\mathbb I}_k} {\bm x}_k = {\bm P}_k {\bm y}`, 则投影后的误差可以表示为

   .. math::
      \begin{aligned}
      {\bm r}_k &= {\bm y} - {\hat{\bm y}}_k \\
                &= ({\bm I} - {\bm P}_k){\bm y} \\
                &= ({\bm I} - {\bm P}_k){\bm {Ax}} + ({\bm I} - {\bm P}_k){\bm n},
      \end{aligned}

   其中, :math:`({\bm I} - {\bm P}_k){\bm {Ax}}` 为残差中的信号成份, :math:`({\bm I} - {\bm P}_k){\bm n}` 为残差中的噪声成份.


实验与分析
--------------------

主要分析OMP算法在信号稀疏分解上的性能, 有关OMP在压缩感知中的应用参见 :ref:`SubsubSection_CSOMPSparseSignal` 小节.


仿真数据实验
~~~~~~~~~~~~~~~~~

实验中通过仿真生成含有三个频率成分的信号 :math:`{\bm y} = {\rm sin}2πf_1t + {\rm sin}2πf_2t +{\rm sin}2πf_3t`, 仿真参数设置如下:

- 频率成分: :math:`f_1 = 10Hz, f_2 = 20Hz,f_3 = 70Hz`
- 采样频率: :math:`F_s = 256Hz`
- 采样时间: :math:`T_s = 1s`
- 采样点数: :math:`N_s = F_s T_s = 256`

构造过完备DCT字典(参见 :ref:`SubSection_ODCTDICT`), 字典大小为 :math:`M\times N`, 其中 :math:`M=N_s, N=R*M`, :math:`R` 为一可调变量, 通过OMP求解稀疏系数 :math:`{\bm x}`, 并利用 :eq:`equ-OmpProb` 恢复信号 :math:`{\bm y}`.

实现代码, 参见文件 `demo_omp_sin3_decomposition.py <https://github.com/antsfamily/pysparse/tree/master/examples/decomposition/demo_omp_sin3_decomposition.py>`_  .

.. literalinclude:: https://github.com/antsfamily/pysparse/tree/master/examples/decomposition/demo_omp_sin3_decomposition.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 43-49
   :linenos:
   :caption: demo_omp_sin3_decomposition.py
   :name: bind-id

仿真生成的信号 :math:`{\bm y}` 如下图(左)所示, 其DCT变换后的系数如下图(右)所示

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/SignalSparseDecomposition/OMP/sin3OMPOrignalSignalCoefficients.*
   :scale: 100 %
   :alt: Signal in Time and Frequency domains.
   :align: center

   Signal in Time (left, :math:`{\bm y}` ) and Frequency (right, :math:`{\bm x}`) domains.


如图中所示, 三种频率成分对应六个峰, 峰的位置为频率的二倍(**这是因为DCT变换中分母为** :math:`2N`, **而不是** :math:`N`), 峰的上下两个方向对应正频和负频.


:math:`R=2` 即 :math:`N = 2M` 时, 设置不同稀疏度下的信号重构均方误差结果如下:

::

   ---MSE(y, y1) with k = 2:  0.937048086151075
   ---MSE(y, y2) with k = 4:  0.5420001800721357
   ---MSE(y, y3) with k = 6:  0.25283463530586237
   ---MSE(y, y4) with k = 100:  0.002307660406098402

求解的频域稀疏系数为

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/SignalSparseDecomposition/OMP/sin3R2OMPRecoveryCoefficients.*
   :scale: 100 %
   :alt: Recovered signal in frequency domain with different sparse degree :math:`k`.
   :align: center

   Recovered signal in frequency domain with different sparse degree :math:`k`.

恢复的信号为

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/SignalSparseDecomposition/OMP/sin3R2OMPRecoverySignal.*
   :scale: 100 %
   :alt: Recovered signal in time domain with different sparse degree :math:`k`.
   :align: center

   Recovered signal in time domain with different sparse degree :math:`k`.


:math:`R=1` 即 :math:`N = M` 时, 设置不同稀疏度下的信号重构均方误差结果如下:

::

   ---MSE(y, y1) with k = 2:  0.9865788586325661
   ---MSE(y, y2) with k = 4:  0.5829159447924545
   ---MSE(y, y3) with k = 6:  0.3169739132218109
   ---MSE(y, y4) with k = 100:  0.0023321884115169826

求解的频域稀疏系数为

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/SignalSparseDecomposition/OMP/sin3R1OMPRecoveryCoefficients.*
   :scale: 100 %
   :alt: Recovered signal in frequency domain with different sparse degree :math:`k`.
   :align: center

   Recovered signal in frequency domain with different sparse degree :math:`k`.

恢复的信号为

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/SignalSparseDecomposition/OMP/sin3R1OMPRecoverySignal.*
   :scale: 100 %
   :alt: Recovered signal in time domain with different sparse degree :math:`k`.
   :align: center

   Recovered signal in time domain with different sparse degree :math:`k`.


:math:`R=0.5` 即 :math:`N = M/2` 时, 设置不同稀疏度下的信号重构均方误差结果如下:

::

   ---MSE(y, y1) with k = 2:  1.031848207375802
   ---MSE(y, y2) with k = 4:  0.6615399428007099
   ---MSE(y, y3) with k = 6:  0.4982313612363407
   ---MSE(y, y4) with k = 100:  0.32437796224425747

求解的频域稀疏系数为

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/SignalSparseDecomposition/OMP/sin3R5e-1OMPRecoveryCoefficients.*
   :scale: 100 %
   :alt: Recovered signal in frequency domain with different sparse degree :math:`k`.
   :align: center

   Recovered signal in frequency domain with different sparse degree :math:`k`.

恢复的信号为

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/SignalSparseDecomposition/OMP/sin3R5e-1OMPRecoverySignal.*
   :scale: 100 %
   :alt: Recovered signal in time domain with different sparse degree :math:`k`.
   :align: center

   Recovered signal in time domain with different sparse degree :math:`k`.


真实数据实验
~~~~~~~~~~~~~~~~~





