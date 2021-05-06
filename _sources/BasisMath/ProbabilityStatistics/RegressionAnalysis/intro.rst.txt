.. _Section-IntroductionRegressionAnalysisProbabilityStatisticsBasicMath:


回归分析简介
=================


什么是回归分析
---------------

回归分析 ( :term:`Regression Analysis` ) 是确定两种或两种以上变量间相互依赖的定量关系的一种统计分析方法.

设有随机向量 :math:`{\bf x}=({\rm x}_1, {\rm x}_2, \cdots, {\rm x}_n)^T` , :math:`{\bf y}=({\rm y}_1, {\rm y}_2, \cdots, {\rm y}_m)^T` , 以及一组观测值数据样本对 :math:`{\mathbb S} = \{{\bm x}_i, {\bm y}_i\}_{i=0}^K` , 其中 :math:`{\bm x}_i = (x_{1_i}, x_{2_i}, \cdots, x_{n_i})^T` , :math:`{\bm y}_i = (y_{1_i}, y_{2_i}, \cdots, y_{m_i})^T` , :math:`n, m , K \in {\mathbb Z}^+` , 回归分析旨在确定随机变量 :math:`{\bf x}, {\bf y}` 间的关系, 这种关系的数学化称为建模. 用 :math:`\mathcal G` 表示模型, 则:

.. math::
    {\bf y} = {\mathcal G}({\bf x}).
    :label: equ-RegressionAnalysis

模型可以有参数, 也可以无参数. 若模型为有参的, 记 :math:`{\bm \beta}` 为模型参数, 从而 :eq:`equ-RegressionAnalysis` 可表示为:

.. math::
    {\bf y} = {\mathcal G}({\bf x}, {\bm \beta}).
    :label: equ-RegressionAnalysis_Params

即回归分析的目的是在给出一组数据样本对 :math:`{\mathbb S} = \{{\bm x}_i, {\bm y}_i\}_{i=0}^K` 的情况下, 求解一个模型 :math:`\mathcal G` , 使得该模型可以很好地拟合数据. 记 :math:`\hat{\bf y}` 为模型预测输出, 为评测模型的预测结果与实际观测数据在结果上的一致性, 通常定义评测准则, 如定义评测准则为损失函数 (你完全可以定义其它函数), 假设损失函数为均方误差 (:term:`Mean Squared Error`, MSE):

.. math::
    L = \frac{1}{K}\sum_{i=1}^K \| \hat{\bf y}_i - {\bf y}_i \|_2^2 = \frac{1}{K}\sum_{i=1}^K \|{\mathcal G}\left({\bf x}_i) - {\bf y}_i\right\|_2^2,
    :label: equ-RegressionAnalysis_MSE

一般通过优化 :eq:`equ-RegressionAnalysis_MSE` 求解模型.

.. hint::
    本书中的符号表示与一般概率论统计书籍中有所区别:

    - 随机变量: :math:`{\rm x}` , 随机变量取值 :math:`x` , 如 :math:`P({\rm x} = x)`
    - 随机向量: :math:`{\bf x}` , 随机向量取值 :math:`\bm x` , 如 :math:`P({\bf x} = {\bm x})`


回归分析的类型
-----------------

1. 若模型为无参的, 称为无参数回归 (:term:`Nonparametric Regression`);
2. 若模型为有参的, 称为有参数回归 (:term:`Parametric Regression`);
3. 若 :math:`n=1, m=1` , 称为单重回归 (:term:`Simple Regression`), 一个输入, 单个输出;
4. 若 :math:`n>1, m=1` , 称为多重回归 (:term:`Multiple Regression`), 多个输入, 单个输出;
5. 若 :math:`n\in {\mathbb Z}^+, m>1` , 称为多元回归 (:term:`Multivariate Regression`), 多个输出;
6. 若 :math:`{\mathcal G}({\bf x}) = {\bm \beta}{\bf x} + {\bm \beta}_0` 即满足线性关系, 称为线性回归 (:term:`Linear Regression`)
7. 若 :math:`{\mathcal G}({\bf x}) \neq {\bm \beta}{\bf x} + {\bm \beta}_0` 即满足非线性关系, 称为非线性回归 (:term:`Nonlinear Regression`)
8. 投影追踪回归 (:term:`Projection Pursuit Regression`)
9. 贝叶斯回归 (:term:`Bayesian Regression`)






