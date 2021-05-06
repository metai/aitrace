.. _SubSection-IntroductionRegressionModelingRegressionAnalysisProbabilityStatisticsBasicMath:


回归分析简介
=================


什么是回归分析
---------------

回归分析 ( :term:`Regression Analysis` ) 是确定两种或两种以上变量间相互依赖的定量关系的一种统计分析方法.

假设变量 :math:`{\bf x} = ({\rm x_1}, {\rm x_2}, \cdots, {\rm x_n})^T` 和 :math:`{\bf y} = ({\rm y_1}, {\rm y_2}, \cdots, {\rm y_m})^T` 满足模型:

.. math::
    {\bf y} = {\mathcal G}({\bf x})

记 :math:`{\bm \beta}` 为模型参数, 则

.. math::
    {\bf y} = {\mathcal G}({\bf x}, {\bm \beta})


回归分析的目的是在给出一组数据样本对 :math:`{\mathbb S} = \{{\bf x}_i, {\bf y}_i\}_{i=0}^K` 的情况下, 求解一个模型 :math:`\mathcal G` , 使得该模型可以很好地拟合数据. 求解方法一般是通过定义损失函数并优化损失来求解模型参数, 如定义损失函数为均方误差:

.. math::
    L =


:math:`\ell_1` 范数被广泛应用于各种领域: 统计学, 信号处理, 压缩感知等等.

记 :math:`{\bf X} = ({\bf x}_1, {\bf x}_2, \cdots, {\bf x}_K)` , :math:`{\bf Y} = ({\bf y}_1, {\bf y}_2, \cdots, {\bf y}_K)` , 则模型

1. 若 :math:`{\mathcal G}({\bf x}) = {\bf A}{\bf x}` 即表示成线性关系, 则有


:guilabel:`Previous`

.. confval:: collapse_navigation

    :type: boolean
    :default: ``True``

    With this enabled, navigation entries are not expandable -- the ``[+]``
    icons next to each entry are removed.

Setting :confval:`collapse_navigation` to False






