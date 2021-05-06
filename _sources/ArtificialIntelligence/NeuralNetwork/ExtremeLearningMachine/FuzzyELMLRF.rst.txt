.. _Section-FuzzyExtremeLearningMachineLocalReceptiveFields:

基于局部感受野的模糊极速学习机
============================


简介
--------------------

现实世界中, 每个训练样本的重要性不一, 通常一些训练样本比另外一些更重要, 我们希望有意义的样本被正确分类, 而不关心噪声样本是否被错分 :cite:`ChunFuLin.2002` . 在基于局部感受野的极速学习机 (Local Receptive Fields based Extreme Learning Machine, ELM-LRF) 上引入模糊性, 使得模型对噪声更加鲁邦, 得到基于局部感受野的模糊极速学习机 (Local Receptive Fields based Fuzzy Extreme Learning Machine, FELM-LRF).


.. hint::
   - 模糊集合的概念参见章节 :ref:`Chapter-FuzzySets`
   - 有关基于局部感受野的极速学习机参见章节 :ref:`Section-ExtremeLearningMachineLocalReceptiveFields`.


FELM-LRF原理
-----------------




.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ExtremeLearningMachine/FELMLRF/frameworkELMLRF.*
   :align: center
   :alt: Framework of FELM-LRF.

   Framework of FELM-LRF.


对于分类问题, 假设有训练样本集 :math:`\tilde{\mathbb S} = \{({\bm x}_i, {\bm y}_i, u_i)\}_{i=1}^N`, 其中, :math:`N` 为样本数目, :math:`u_i \in {\mathbb R}` 为样本 :math:`{\bm x}_i\in{\mathbb R}^n` 对应的隶属度, :math:`{\bm y}_i` 为 :math:`{\bm x}_i` 对应的标签, 在损失函数中引入隶属度, 从而有 FELM-LRF 的优化问题

.. math::
   {\rm min} \|\bm{\beta}\|_{p}^{\sigma_{1}}+C\|{\bm U}({\bm H}{\bm \beta}-{\bm T})\|_{q}^{\sigma_{2}}
   :label: equ-FELM-LRF_problem

其中, :math:`\sigma_{1}>0, \sigma_{2}>0, \quad p, q>0` , :math:`{\bm U} = {\rm diag}(u_1, u_2, \cdots, u_N) \in {\mathbb R}^{N \times N}` 为由所有训练样本的隶属度组成的对角矩阵, :math:`\bm{\beta}\in{\mathbb R}^{L \times m}` 输出层权重矩阵, :math:`{\bm T}\in {\mathbb R}^{N\times m}` 为由样本标签组成的 one-hot 矩阵, 满足

.. math::
   {{\bf{T}}_{ij}} = \left\{ {\begin{array}{lll}
   {1,\;\;j = {{\bf{y}}_i}}\\
   {0,\;\;j \neq {{\bf{y}}_i}}
   \end{array}} \right. .

记 :math:`{\bm H}_F = {\bm U}{\bm H}`, :math:`{\bm T}_F = {\bm U}{\bm T}` , 则 FELM-LRF 的优化问题 :eq:`equ-FELM-LRF_problem` 变为

.. math::
   {\rm min} \|\bm{\beta}\|_{p}^{\sigma_{1}}+C\|({\bm H}_F{\bm \beta}-{\bm T}_F)\|_{q}^{\sigma_{2}}
   :label: equ-FELM-LRF_problem_final

当 :math:`\sigma_{1}=\sigma_{2}=p=q=2` 时, 容易求得 :eq:`equ-FELM-LRF_problem_final` 的解为

.. math::
   \bm{\beta}=\left\{\begin{array}{ll}{{\bm H}_F^{T}\left(\frac{\bm{I}}{C}+{\bm H}_F {\bm H}_F^{T}\right)^{-1} {\bm T}_F,} & {\text { if } N \leq L} \\ {\left(\frac{\bm{I}}{C}+{\bm H}_F^{T} {\bm H}_F\right)^{-1} {\bm H}_F^{T} {\bm T}_F,} & {\text { if } N \geq L}\end{array}\right.
   :label: equ-FELM-LRF_problem_solution

其中, :math:`{\bm H}_F = {\bm U}{\bm H}`, :math:`{\bm T}_F = {\bm U}{\bm T}`.



隶属函数选择
-----------------

关于隶属函数选择可以参考章节 :ref:`SubsubSection-FSVM_MembershipFuncSelection`





实验及结果
--------------

实验说明
~~~~~~~~~~~~~~~~


NORB数据集, 共5类, 分别为: Animal, Human, Airplane, Truck, Car, 其中, 含24300个训练样本数, 20000个测试样本. 实验中, 随机产生 :math:`0.8\%` 噪声样本, 设置平衡因子为: 0.001, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09,  0.1, 0.2, 0.3, 0.4, 0.5 0.6 0.7 0.8 0.9, 用含噪声的训练样本分别训练 ELM-LRF 和 FELM-LRF. 实验代码可在 `这里 <https://github.com/antsfamily/FELM-LRF>`_ 下载.


实验结果
~~~~~~~~~~~~~~~~





.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ExtremeLearningMachine/FELMLRF/TrainingAccVsC.*
   :align: center
   :alt: Training accuracy vs balance factor :math:`C`.

   Training accuracy vs balance factor :math:`C`.



.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ExtremeLearningMachine/FELMLRF/TrainingTimeVsC.*
   :align: center
   :alt: Training time vs balance factor :math:`C`.

   Training time vs balance factor :math:`C`.



.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ExtremeLearningMachine/FELMLRF/TestingAccVsC.*
   :align: center
   :alt: Testing accuracy vs balance factor :math:`C`.

   Testing accuracy vs balance factor :math:`C`.
