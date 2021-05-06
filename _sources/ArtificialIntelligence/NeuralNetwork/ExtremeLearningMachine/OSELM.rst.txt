.. _Section-OnilineSequentialExtremeLearningMachine:

在线极速学习机
=============================


简介
--------------------





OSELM 原理
-----------------

下面介绍 **在线极速学习机** (Oniline Sequential Extreme Learning Machine, OS-ELM) 原理.

考虑如下ELM问题

.. math::
   \bm{H} \boldsymbol{\beta}=\bm{T}

其最小二乘解为

.. math::
   \hat{\boldsymbol{\beta}}=\left(\bm{H}^{\bm{T}} \bm{H}\right)^{-\bm{1}} \bm{H}^{\bm{T}} \bm{T}

如果 :math:`\bm{H}^{\bm{T}} \bm{H}` 趋于奇异, 可以选择较小的隐层神经元节点数 :math:`L` , 或者增加样本数量.

给定初始训练集 :math:`{\mathbb S}_0 = \{({\bm x}_i, {\bm t}_i)\}_{i=1}^{N_0}` , 其中, :math:`N_0` 为样本数, 且 :math:`N_0 > L` . 从而有初始解

.. math::
   {\bm \beta_{0}}=\bm{K}_{0}^{-1} \bm{H}_{0}^{T} \bm{T}_{0}, \;\bm{K}_{0}=\bm{H}_{0}^{T} \bm{H}_{0}

假如又可以获得训练集 :math:`{\mathbb S}_1 = \{({\bm x}_i, {\bm t}_i)\}_{i=N_0+1}^{N_0+N_1}` , 其中 :math:`N_1` 为新样本数目, 问题变为最小化

.. math::
   \left\| \left[ \begin{array}{l}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right] {\bm \beta}-\left[ \begin{array}{l}{\bm{T}_{0}} \\ {\bm{T}_{1}}\end{array}\right] \right\|

其解为:

.. math::
   \boldsymbol{\beta}_{1}=\bm{K}_{1}^{-1} \left[ \begin{array}{c}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right]^{T} \left[ \begin{array}{c}{\bm{T}_{0}} \\ {\bm{T}_{1}}\end{array}\right], \; \bm{K}_{1}=\left[ \begin{array}{l}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right]^{T} \left[ \begin{array}{l}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right]

又因为

.. math::
   \begin{aligned} \bm{K}_{1} &=\left[ \begin{array}{cc}{\bm{H}_{0}^{T}} & {\bm{H}_{1}^{T}}\end{array}\right] \left[ \begin{array}{l}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right] \\ &=\bm{K}_{0}+\bm{H}_{1}^{T} \bm{H}_{1} \end{aligned}

且

.. math::
   \begin{aligned} \left[ \begin{array}{c}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right]^{T} \left[ \begin{array}{c}{\bm{T}_{0}} \\ {\bm{T}_{1}}\end{array}\right] &=\bm{H}_{0}^{T} \bm{T}_{0}+\bm{H}_{1}^{T} \bm{T}_{1} \\ &=\bm{K}_{0} \bm{K}_{0}^{-1} \bm{H}_{0}^{T} \bm{T}_{0}+\bm{H}_{1}^{T} \bm{T}_{1} \\ &=\bm{K}_{0} {\bm \beta_{0}}+\bm{H}_{1}^{T} \bm{T}_{1} \\ &=\left(\bm{K}_{1}-\bm{H}_{1}^{T} \bm{H}_{1}\right) {\bm \beta_{0}}+\bm{H}_{1}^{T} \bm{T}_{1} \\ &=\bm{K}_{1} {\bm \beta_{0}}-\bm{H}_{1}^{T} \bm{H}_{1} \boldsymbol{\beta}_{0}+\bm{H}_{1}^{T} \bm{T}_{1} \end{aligned}

所以, :math:`{\boldsymbol \beta}_1` 可以表示成 :math:`{\boldsymbol \beta}_0` 的函数

.. math::
   \begin{aligned} {\bm \beta_{1}} &=\bm{K}_{1}^{-1} \left[ \begin{array}{c}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right]^{T} \left[ \begin{array}{c}{\bm{T}_{0}} \\ {\bm{T}_{1}}\end{array}\right] \\ &=\bm{K}_{1}^{-1}\left(\bm{K}_{1} \boldsymbol{\beta}_{0}-\bm{H}_{1}^{T} \bm{H}_{1} \boldsymbol{\beta}_{0}+\bm{H}_{1}^{T} \bm{T}_{1}\right) \\ &=\boldsymbol{\beta}_{0}+\bm{K}_{1}^{-1} \bm{H}_{1}^{T}\left(\bm{T}_{1}-\bm{H}_{1} {\bm \beta_{0}}\right) \end{aligned}

其中, :math:`\bm{K}_{1}=\bm{K}_{0}+\bm{H}_{1}^{T} \bm{H}_{1}` . 依次类推, 可以得到权重 :math:`\bm \beta` 的迭代更新公式

.. math::
   \begin{aligned} \bm{K}_{k+1} &=\bm{K}_{k}+\bm{H}_{k+1}^{T} \bm{H}_{k+1} \\ {\bm \beta}_{k+1} &={\bm \beta}_{k}+\bm{K}_{k+1}^{-1} \bm{H}_{k+1}^{T}\left(\bm{T}_{k+1}-\bm{H}_{k+1} \boldsymbol{\beta}_{k}\right), \end{aligned}
   :label: equ-OSELM_Solution_Beta_Iterative

其中, :math:`\bm{K}_{k}^{-1} \in {\mathbb R}^{L \times L}` , :math:`\bm{H}_{k} \in {\mathbb R}^{N_k\times L}` , :math:`{\bm \beta}_k \in {\mathbb R}^{L \times m}` , :math:`{\bm T}_k \in {\mathbb R}^{N_k\times m}` :math:`k=1,2,\cdots` . 根据输出权重的迭代更新公 :eq:`equ-OSELM_Solution_Beta_Iterative` 可知, 每次更新权重都需要计算一次一个 :math:`\bm{K}_{k+1}^{-1} \in {\mathbb R}^{L \times L}` 的逆.

由 Sherman-Morrison-Woodbury 等 :eq:`equ-Sherman-Morrison-Woodbury` (参见 :ref:`part-MatrixTheory` 之 :ref:`Section-Often` 小结) 知

.. math::
   \begin{aligned} \bm{K}_{k+1}^{-1} &=\left(\bm{K}_{k}+\bm{H}_{k+1}^{T} \bm{H}_{k+1}\right)^{-1} \\ &=\bm{K}_{k}^{-1}-\bm{K}_{k}^{-1} \bm{H}_{k+1}^{T}\left(\bm{I}+\bm{H}_{\bm{k}+1} \bm{K}_{\bm{k}}^{-1} \bm{H}_{\bm{k}+1}^{\mathrm{T}}\right)^{-1} \bm{H}_{k+1} \bm{K}_{k}^{-1}. \end{aligned}

若记 :math:`{\bm P}_{k+1} = {\bm K}^{-1}_{k+1}` , 则有如下迭代公式

.. math::
   \begin{aligned} \bm{P}_{k+1} &=\bm{P}_{k}-\bm{P}_{k} \bm{H}_{k+1}^{T}\left(\bm{I}+\bm{H}_{k+1} \bm{P}_{k} \bm{H}_{k+1}^{T}\right)^{-1} \bm{H}_{k+1} \bm{P}_{k} \\ \boldsymbol{\beta}_{k+1} &=\boldsymbol{\beta}_{k}+\bm{P}_{k+1} \bm{H}_{k+1}^{T}\left(\bm{T}_{k+1}-\bm{H}_{k+1} \boldsymbol{\beta}_{k}\right) \end{aligned}
   :label: equ-OSELM_Solution_Beta_Iterative_better_ChunkByChunk

其中, :math:`{\bm I}\in{\mathbb R}^{N_k\times N_k}` 为单位矩阵, 当 :math:`N_k < L` 时, :eq:`equ-OSELM_Solution_Beta_Iterative_better_ChunkByChunk` 可以减小计算量.

若样本以 one-by-one 的形式输入 OSELM, 则更新公 :eq:`equ-OSELM_Solution_Beta_Iterative_better_ChunkByChunk` 简化为

.. math::
   \begin{array}{l}{\bm{P}_{k+1}=\bm{P}_{k}-\frac{\bm{P}_{k} \bm{h}_{k+1} \bm{h}_{k+1}^{T} \bm{P}_{k}}{1+\bm{h}_{k+1}^{T} \bm{P}_{k} \bm{h}_{k+1}}} \\ {{\bm \beta}_{k+1}={\bm \beta}_{k}+\bm{P}_{k+1} \bm{h}_{k+1}\left(\bm{t}_{k+1}^{T}-\bm{h}_{k+1}^{T} {\bm \beta}_{k}\right)}\end{array}.
   :label: equ-OSELM_Solution_Beta_Iterative_better_OneByOne


上述在线训练算法总结如下:

.. tip::
   **输入**: 样本序列 :math:`\mathbb{S}_{0}=\left\{\left(\bm{x}_{i}, \bm{t}_{i}\right)\right\}_{i=1}^{N_{0}}` , :math:`{\mathbb S}_{1}=\left\{\left(\bm{x}_{i}, \bm{t}_{i}\right)\right\}_{i=N_{0}+1}^{N_{0}+N_{1}}` , :math:`\cdots` , :math:`{\mathbb S}_{k+1}=\left\{\left(\bm{x}_{i}, \bm{t}_{i}\right)\right\}_{i=\sum_{j=1}^k N_{j}+1}^{\sum_{j=1}^{k+1} N_{j}}` , :math:`k=1, 2, \cdots, K` .

   **输出**: 更新输出层权重 :math:`{\bm \beta}_{K}`


   1. 初始训练(:math:`k=0`, :math:`N_0 > L`):

      计算初始样本集 :math:`{\mathbb S}_0` 的隐藏层输出 :math:`{\bm H}_0` , 估计初始权重 :math:`{\bm \beta}_0 = \bm{P}_{0} \bm{H}_{0}^{T} \bm{T}_{0}` , 其中 :math:`\bm{P}_{0}=\left(\bm{H}_{0}^{T} \bm{H}_{0}\right)^{-1}` , :math:`\bm{T}_{0}=\left[\bm{t}_{1}, \dots, \bm{t}_{N_{0}}\right]^{T}` .

   2. 序列学习(:math:`k=1, 2, \cdots, K`, :math:`N_k` 为样本数):

      - 若 :math:`N_k > 1` , 计算第 :math:`k+1` 个样本集 :math:`{\mathbb S}_{k+1}` 的隐藏层输出 :math:`{\bm H}_{k+1}`, 并根据 :eq:`equ-OSELM_Solution_Beta_Iterative_better_ChunkByChunk` 更新权重;
      - 若 :math:`N_k = 1` , 计算第 :math:`k+1` 个样本集 :math:`{\mathbb S}_{k+1}` 的隐藏层输出 :math:`{\bm h}_{k+1}`,  则根据 :eq:`equ-OSELM_Solution_Beta_Iterative_better_OneByOne` 更新权重;

      当 :math:`k = K` 时停止训练, 并输出权重 :math:`{\bm \beta}_{K}` .








