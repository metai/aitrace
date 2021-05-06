.. _Section-OnilineSequeExtremeLearningMachineLocalReceptiveFields:

基于局部感受野的在线极速学习机
=============================



简介
--------------------

一般来说, 隐藏层节点要足够多, ELM 算法如果要取得较好的效果, 一方面由于训练数据集往往比较大, 不能一次性送入ELM进行训练, 另一方面, 现实生活中, 数据往往不能一次性获得.


.. hint::
   - 在线极速学习机参见章节 :ref:`Section-OnilineSequentialExtremeLearningMachine`
   - 有关基于局部感受野的极速学习机参见章节 :ref:`Section-ExtremeLearningMachineLocalReceptiveFields`.


OSELM-LRF原理
-----------------

下面介绍 **基于局部感受野的在线极速学习机** (Local Receptive Fields based Oniline Sequential Extreme Learning Machine, OSELM-LRF) 原理.


考虑如下ELM问题

.. math::
   \|\boldsymbol{\beta}\|_{2}^{2}+C\|\bm{H} \boldsymbol{\beta}-\bm{T}\|_{2}^{2}

其最小二乘解为

.. math::
   {\bm \beta}=\left\{\begin{array}{ll}{\bm{H}^{T}\left(\frac{\bm{I}}{C}+\bm{H} \bm{H}^{T}\right)^{-1} \bm{T},} & {\text { if } N \leq L} \\ {\left(\frac{\bm{I}}{C}+\bm{H}^{T} \bm{H}\right)^{-1} \bm{H}^{T} \bm{T},} & {\text { if } N>L}\end{array}\right.

考虑解 :math:`\left(\frac{\bm{I}}{C}+\bm{H}^{T} \bm{H}\right)^{-1} \bm{H}^{T} \bm{T}` .

.. hint::
   虽然初始样本数 :math:`N_0 < L` , 但随着样本源源不断地到来, 最终会有 :math:`\sum_{j=1}^k N_k > L` .

给定初始训练集 :math:`{\mathbb S}_0 = \{({\bm x}_i, {\bm t}_i)\}_{i=1}^{N_0}` , 其中, :math:`N_0` 为样本数, 且 :math:`N_0 > L` . 从而有初始解

.. math::
   {\bm \beta_{0}}=\bm{K}_{0}^{-1} \bm{H}_{0}^{T} \bm{T}_{0}, \;\bm{K}_{0}=\frac{\bm{I}}{C} + \bm{H}_{0}^{T} \bm{H}_{0}

假如又可以获得训练集 :math:`{\mathbb S}_1 = \{({\bm x}_i, {\bm t}_i)\}_{i=N_0+1}^{N_0+N_1}` , 其中 :math:`N_1` 为新样本数目, 问题变为最小化

.. math::
   \left\| {\bm{\beta }} \right\|_2^2 + C\left\| {\left[ {\begin{array}{ccc}
   {{{\bf{H}}_0}}\\
   {{{\bf{H}}_1}}
   \end{array}} \right]{\bm{\beta }} - \left[ {\begin{array}{ccc}
   {{{\bf{T}}_0}}\\
   {{{\bf{T}}_1}}
   \end{array}} \right]} \right\|_2^2

其解为:

.. math::
   \boldsymbol{\beta}_{1}=\bm{K}_{1}^{-1} \left[ \begin{array}{c}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right]^{T} \left[ \begin{array}{c}{\bm{T}_{0}} \\ {\bm{T}_{1}}\end{array}\right],

其中,

.. math::
   \begin{aligned} \bm{K}_{1} &=\frac{\bm{I}}{C}+\left[ \begin{array}{c}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right]^{T} \left[ \begin{array}{c}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right] \\ &=\frac{\bm{I}}{C}+\bm{H}_{0}^{T} \bm{H}_{0}+\bm{H}_{1}^{T} \bm{H}_{1} \\ &=\bm{K}_{0}+\bm{H}_{1}^{T} \bm{H}_{1} \end{aligned}

又

.. math::
   \begin{aligned} \left[ \begin{array}{c}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right]^{T} \left[ \begin{array}{c}{\bm{T}_{0}} \\ {\bm{T}_{1}}\end{array}\right] &=\bm{H}_{0}^{T} \bm{T}_{0}+\bm{H}_{1}^{T} \bm{T}_{1} \\ &=\bm{K}_{0} \bm{K}_{0}^{-1} \bm{H}_{0}^{T} \bm{T}_{0}+\bm{H}_{1}^{T} \bm{T}_{1} \\ &=\bm{K}_{0} {\bm \beta_{0}}+\bm{H}_{1}^{T} \bm{T}_{1} \\ &=\left(\bm{K}_{1}-\bm{H}_{1}^{T} \bm{H}_{1}\right) {\bm \beta_{0}}+\bm{H}_{1}^{T} \bm{T}_{1} \\ &=\bm{K}_{1} {\bm \beta_{0}}-\bm{H}_{1}^{T} \bm{H}_{1} \boldsymbol{\beta}_{0}+\bm{H}_{1}^{T} \bm{T}_{1} \end{aligned}

所以, :math:`{\boldsymbol \beta}_1` 可以表示成 :math:`{\boldsymbol \beta}_0` 的函数

.. math::
   \begin{aligned} {\bm \beta_{1}} &=\bm{K}_{1}^{-1} \left[ \begin{array}{c}{\bm{H}_{0}} \\ {\bm{H}_{1}}\end{array}\right]^{T} \left[ \begin{array}{c}{\bm{T}_{0}} \\ {\bm{T}_{1}}\end{array}\right] \\ &=\bm{K}_{1}^{-1}\left(\bm{K}_{1} \boldsymbol{\beta}_{0}-\bm{H}_{1}^{T} \bm{H}_{1} \boldsymbol{\beta}_{0}+\bm{H}_{1}^{T} \bm{T}_{1}\right) \\ &=\boldsymbol{\beta}_{0}+\bm{K}_{1}^{-1} \bm{H}_{1}^{T}\left(\bm{T}_{1}-\bm{H}_{1} {\bm \beta_{0}}\right) \end{aligned}

其中, :math:`\bm{K}_{1}=\bm{K}_{0}+\bm{H}_{1}^{T} \bm{H}_{1}` . 依次类推, 可以得到权重 :math:`\bm \beta` 的迭代更新公式

.. math::
   \begin{aligned} \bm{K}_{k+1} &=\bm{K}_{k}+\bm{H}_{k+1}^{T} \bm{H}_{k+1} \\ {\bm \beta}_{k+1} &={\bm \beta}_{k}+\bm{K}_{k+1}^{-1} \bm{H}_{k+1}^{T}\left(\bm{T}_{k+1}-\bm{H}_{k+1} \boldsymbol{\beta}_{k}\right), \end{aligned}
   :label: equ-OSELMLRF_Solution_Beta_Iterative

可见, 含权重正则的 OSELM 问题与不含权重正则的 OSELM 问题的权重迭代更新公式相同, 区别在于初始化权重 :math:`{\bm \beta}_0` 的计算. 根据 :ref:`Section-OnilineSequentialExtremeLearningMachine` 小节推导, 可知含权重正则的基于局部感受野的在线极速学习机的权重更新公式为

.. math::
   \begin{aligned} \bm{P}_{k+1} &=\bm{P}_{k}-\bm{P}_{k} \bm{H}_{k+1}^{T}\left(\bm{I}+\bm{H}_{k+1} \bm{P}_{k} \bm{H}_{k+1}^{T}\right)^{-1} \bm{H}_{k+1} \bm{P}_{k} \\ \boldsymbol{\beta}_{k+1} &=\boldsymbol{\beta}_{k}+\bm{P}_{k+1} \bm{H}_{k+1}^{T}\left(\bm{T}_{k+1}-\bm{H}_{k+1} \boldsymbol{\beta}_{k}\right) \end{aligned}
   :label: equ-OSELMLRF_Solution_Beta_Iterative_better_ChunkByChunk

其中, :math:`{\bm I}\in{\mathbb R}^{N_k\times N_k}` 为单位矩阵, 当 :math:`N_k < L` 时, :eq:`equ-OSELM_Solution_Beta_Iterative_better_ChunkByChunk` 可以减小计算量.

若样本以 one-by-one 的形式输入 OSELM, 则更新公 :eq:`equ-OSELMLRF_Solution_Beta_Iterative_better_ChunkByChunk` 简化为

.. math::
   \begin{array}{l}{\bm{P}_{k+1}=\bm{P}_{k}-\frac{\bm{P}_{k} \bm{h}_{k+1} \bm{h}_{k+1}^{T} \bm{P}_{k}}{1+\bm{h}_{k+1}^{T} \bm{P}_{k} \bm{h}_{k+1}}} \\ {{\bm \beta}_{k+1}={\bm \beta}_{k}+\bm{P}_{k+1} \bm{h}_{k+1}\left(\bm{t}_{k+1}^{T}-\bm{h}_{k+1}^{T} {\bm \beta}_{k}\right)}\end{array}.
   :label: equ-OSELM_Solution_Beta_Iterative_better_OneByOne

基于局部感受野的在线极速学习机训练算法总结如下:

.. note::
   **输入**: 样本序列 :math:`\mathbb{S}_{0}=\left\{\left(\bm{x}_{i}, \bm{t}_{i}\right)\right\}_{i=1}^{N_{0}}` , :math:`{\mathbb S}_{1}=\left\{\left(\bm{x}_{i}, \bm{t}_{i}\right)\right\}_{i=N_{0}+1}^{N_{0}+N_{1}}` , :math:`\cdots` , :math:`{\mathbb S}_{k+1}=\left\{\left(\bm{x}_{i}, \bm{t}_{i}\right)\right\}_{i=\sum_{j=1}^k N_{j}+1}^{\sum_{j=1}^{k+1} N_{j}}` , :math:`k=1, 2, \cdots, K` , 最大训练代数 :math:`O` .

   **输出**: 更新输出层权重 :math:`{\bm \beta}_{O}`


   1. 初始训练(:math:`k=0`, :math:`N_0 > L`):

      计算初始样本集 :math:`{\mathbb S}_0` 的隐藏层输出 :math:`{\bm H}_0` , 估计初始权重 :math:`{\bm \beta}_0 = \bm{P}_{0} \bm{H}_{0}^{T} \bm{T}_{0}` , 其中 :math:`\bm{P}_{0}= \left(\frac{\bm I}{C} + \bm{H}_{0}^{T} \bm{H}_{0}\right)^{-1}` , :math:`\bm{T}_{0}=\left[\bm{t}_{1}, \dots, \bm{t}_{N_{0}}\right]^{T}` .

   2. 序列学习(:math:`k=1, 2, \cdots, K`, :math:`N_k` 为样本数):

      - 若 :math:`N_k > 1` , 计算第 :math:`k+1` 个样本集 :math:`{\mathbb S}_{k+1}` 的隐藏层输出 :math:`{\bm H}_{k+1}\in {\mathbb R}^{N_k\times L}`, 并根据下式更新权重;

         .. math::
            \begin{aligned} \bm{P}_{k+1} &=\bm{P}_{k}-\bm{P}_{k} \bm{H}_{k+1}^{T}\left(\bm{I}+\bm{H}_{k+1} \bm{P}_{k} \bm{H}_{k+1}^{T}\right)^{-1} \bm{H}_{k+1} \bm{P}_{k} \\ \boldsymbol{\beta}_{k+1} &=\boldsymbol{\beta}_{k}+\bm{P}_{k+1} \bm{H}_{k+1}^{T}\left(\bm{T}_{k+1}-\bm{H}_{k+1} \boldsymbol{\beta}_{k}\right) \end{aligned}

      - 若 :math:`N_k = 1` , 计算第 :math:`k+1` 个样本集 :math:`{\mathbb S}_{k+1}` 的隐藏层输出 :math:`{\bm h}_{k+1}\in {\mathbb R}^{L\times 1}`,  则根据下式更新权重;

        .. math::
           \begin{array}{l}{\bm{P}_{k+1}=\bm{P}_{k}-\frac{\bm{P}_{k} \bm{h}_{k+1} \bm{h}_{k+1}^{T} \bm{P}_{k}}{1+\bm{h}_{k+1}^{T} \bm{P}_{k} \bm{h}_{k+1}}} \\ {\boldsymbol{\beta}_{k+1}=\boldsymbol{\beta}_{k}+\bm{P}_{k+1} \bm{h}_{k+1}\left(\bm{t}_{k+1}^{T}-\bm{h}_{k+1}^{T} \boldsymbol{\beta}_{k}\right)}\end{array}

      当 :math:`k = K` 时完成一代训练, 并输出权重 :math:`{\bm \beta}_{o} = {\bm \beta}_{K}` , :math:`o = o + 1` .

   3. 随机打乱样本集 :math:`\mathbb{S}_{k}, k=1,2,\cdots, K` 的顺序, 并重复步骤2至最大训练代数 :math:`o = O` 时停止.

