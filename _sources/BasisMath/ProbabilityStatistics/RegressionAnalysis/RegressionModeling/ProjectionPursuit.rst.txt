.. _SubSection-ProjectionPursuitRegressionModelingRegressionAnalysisProbabilityStatisticsBasicMath:

投影追踪回归
=================


什么是投影追踪回归
--------------------

Friedman等人于1974年提出投影追踪 (:term:`Projection Pursuit` , PP) :cite:`Friedman1974A` , 并于1981年提出投影追踪回归 (:term:`Projection Pursuit Regression` , PPR) :cite:`Friedman1981projectionpursuit` , 这是一种单输出回归模型, 1985年提出, 多输出回归分类模型 :cite:`Friedman1985Classification` . 有关投影追踪参见 :ref:`SubSection-ProjectionPursuitEstimationMethodsRegressionAnalysisProbabilityStatisticsBasicMath` .

.. _Definition-ProjectionPursuitRegression:

.. proof:definition::  投影追踪回归

   投影追踪回归模型将随机向量 :math:`\bf y` 建模为随机向量 :math:`\bf x` 的随机变量的加权和的不同非线性映射的和, 即:

   .. math::
      {\rm y} = {\rm w}_0 + \sum_{j=1}^r f_j({\bf w}_j^T {\bf x}) + {\rm \epsilon},

其中, :math:`{\bf x}=({\rm x}_1, {\rm x}_2, \cdots, {\rm x}_n)^T` 为自变量, :math:`{\bf w}_j=({\rm w}_{j1}, {\rm w}_{j2}, \cdots, {\rm w}_{jn})^T` 为模型参数, :math:`f_j, j=1,2,\cdots, r` 为 :math:`r` 个非线性映射函数(可以相同或不同), :math:`{\rm \epsilon}` 为模型估计误差.

给定 :math:`K` 个观测样本对 :math:`{\mathbb S} = \{{\bm x}_i, y_i\}_{i=0}^K` , 定义误差函数:

.. math::
   \mathop {\min }\limits_{{f_j},{w_j}} L = \sum_{i=1}^K \left(y_i - \sum_{j=1}^r f_j({\bm w}_j^T {\bm x}_i)\right)^2
   :label: equ-labelname

:eq:`equ-labelname` 可以通过交替优化 (:term:`Alternating Optimization`) 的方法进行优化求解, 投影追踪回归采用投影追踪交替优化算法进行求解, 具体过程参见 :ref:`SubSection-ProjectionPursuitEstimationMethodsRegressionAnalysisProbabilityStatisticsBasicMath` .


.. hint::
   投影追踪回归与神经网络的区别:

   - 理论上都可以逼近任意连续函数;
   - 投影追踪回归的非线性映射可以不同, 神经网络的每层的非线性映射一般相同;
   - 投影追踪回归的非线性映射每次估计一次, 接着更新权重, 而神经网络的非线性映射一般是预先指定并同时估计的.
   - 有关反向传播 (Back-Propagation Learning, BPL) 和投影追踪学习 (Projection Pursuit Learning, PPL), 可参见文献 :cite:`Hwang1994Regression,HectorCorradaBravo2017Neural,Zhao1996Implementing` .


实验与分析
--------------------

回归实验
~~~~~~~~~~~~

实验代码
^^^^^^^^^

从这里 `projection-pursuit benchmarks <https://github.com/pavelkomarov/projection-pursuit/tree/master/benchmarks>`_ 获得 ``compare_to_neural_network.py``


实验结果
^^^^^^^^^


:math:`r` 的影响.

::

   hidden_layer_sizes, max_iter:  200 200
   r, stage_maxiter, backfit_maxiter:  20 200 200
   Average squared error per training example for MLPRegressor: 33.561744644172634
   Average squared error per training example for ProjectionPursuitRegressor: 0.7212472748844135
   Average squared error per testing example for MLPRegressor: 22.095682612129952
   Average squared error per testing example for ProjectionPursuitRegressor: 23.26310438760661
   Training time for MLPRegressor: 0.6172130107879639
   Training time for ProjectionPursuitRegressor: 93.76978826522827

   hidden_layer_sizes, max_iter:  200 200
   r, stage_maxiter, backfit_maxiter:  10 200 200
   Average squared error per training example for MLPRegressor: 25.894054755430098
   Average squared error per training example for ProjectionPursuitRegressor: 2.0112607496432418
   Average squared error per testing example for MLPRegressor: 46.90504990729163
   Average squared error per testing example for ProjectionPursuitRegressor: 23.705301000070467
   Training time for MLPRegressor: 0.6327333450317383
   Training time for ProjectionPursuitRegressor: 26.458088159561157

   hidden_layer_sizes, max_iter:  200 200
   r, stage_maxiter, backfit_maxiter:  5 200 200
   Average squared error per training example for MLPRegressor: 25.394874641020802
   Average squared error per training example for ProjectionPursuitRegressor: 3.9056643659649666
   Average squared error per testing example for MLPRegressor: 36.865379854954945
   Average squared error per testing example for ProjectionPursuitRegressor: 20.50523972734486
   Training time for MLPRegressor: 0.6016314029693604
   Training time for ProjectionPursuitRegressor: 12.463459730148315

隐层神经元数的影响: ::


   hidden_layer_sizes, max_iter:  200 200
   r, stage_maxiter, backfit_maxiter:  5 200 200
   Average squared error per training example for MLPRegressor: 25.394874641020802
   Average squared error per training example for ProjectionPursuitRegressor: 3.9056643659649666
   Average squared error per testing example for MLPRegressor: 36.865379854954945
   Average squared error per testing example for ProjectionPursuitRegressor: 20.50523972734486
   Training time for MLPRegressor: 0.6016314029693604
   Training time for ProjectionPursuitRegressor: 12.463459730148315

   hidden_layer_sizes, max_iter:  512 200
   r, stage_maxiter, backfit_maxiter:  5 200 200
   Average squared error per training example for MLPRegressor: 19.539311275178886
   Average squared error per training example for ProjectionPursuitRegressor: 4.754953589272597
   Average squared error per testing example for MLPRegressor: 39.934009948538275
   Average squared error per testing example for ProjectionPursuitRegressor: 20.004689504319465
   Training time for MLPRegressor: 1.225292682647705
   Training time for ProjectionPursuitRegressor: 14.15251898765564

   hidden_layer_sizes, max_iter:  1024 200
   r, stage_maxiter, backfit_maxiter:  5 200 200
   Average squared error per training example for MLPRegressor: 21.09513135671064
   Average squared error per training example for ProjectionPursuitRegressor: 4.805062370738948
   Average squared error per testing example for MLPRegressor: 16.876270527353554
   Average squared error per testing example for ProjectionPursuitRegressor: 18.131646272884936
   Training time for MLPRegressor: 3.123934745788574
   Training time for ProjectionPursuitRegressor: 10.765942096710205

迭代次数的影响:::

   hidden_layer_sizes, max_iter:  200 1000
   r, stage_maxiter, backfit_maxiter:  5 200 200
   Average squared error per training example for MLPRegressor: 17.596837460636106
   Average squared error per training example for ProjectionPursuitRegressor: 4.219905575343612
   Average squared error per testing example for MLPRegressor: 27.622677425433874
   Average squared error per testing example for ProjectionPursuitRegressor: 14.879565144602562
   Training time for MLPRegressor: 1.9046266078948975
   Training time for ProjectionPursuitRegressor: 14.236632347106934

   hidden_layer_sizes, max_iter:  200 2000
   r, stage_maxiter, backfit_maxiter:  5 200 200
   Average squared error per training example for MLPRegressor: 17.660446224053825
   Average squared error per training example for ProjectionPursuitRegressor: 9.443822651593512
   Average squared error per testing example for MLPRegressor: 27.116718449437933
   Average squared error per testing example for ProjectionPursuitRegressor: 112.54856398900877
   Training time for MLPRegressor: 1.456831932067871
   Training time for ProjectionPursuitRegressor: 19.396251440048218

分类实验
~~~~~~~~~~~~

实验代码
^^^^^^^^^

从这里 `projection-pursuit benchmarks <https://github.com/pavelkomarov/projection-pursuit/tree/master/benchmarks>`_ 获得 ``compare_classifier.py``

实验结果
^^^^^^^^^

