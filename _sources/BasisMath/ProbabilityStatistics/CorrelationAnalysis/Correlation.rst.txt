.. _Section-CorrelationCorrelationAnalysisProbabilityStatistics:


相关的概念
=================

- 互相关

    - 互相关矩阵 ``-->`` 随机向量

    - 互相关函数 ``-->`` 随机过程

- 自相关

    - 自相关矩阵 ``-->`` 随机向量

    - 自相关函数 ``-->`` 随机过程

- 自协方差

- 互协方差


符号说明:

- 随机向量 :math:`\bf x`
- 随机变量 :math:`\rm x`
- 随机变量的取值 :math:`x`

.. hint::
   数学中确定性信号的相关概念参见 :ref:`Section-CorrelationLinearOperatorFunctionalAnalysisBasicMath` 小节.

互相关
-------------

在概率论与统计学中, 互相关用于描述两个随机向量 :math:`\bf x, \bf y` 的元素间的相关性.

互相关函数
~~~~~~~~~~~~

设两个随机过程 :math:`({\rm x}_t, {\rm y}_t)` , :math:`t` 为时间, 可离散或连续, 两个随机过程在时刻 :math:`t` 的均值和方差分别为 :math:`{\mu}_{{\rm x}_t}, {\mu}_{{\rm y}_t}` , :math:`{\sigma}^2_{{\rm x}_t}, {\sigma}^2_{{\rm y}_t}` , 互相关函数定义为

.. math::
    {\bf R}_{{\rm x}{\rm y}}(t_1,t_2) = {\rm E}[{\rm x}_{t_1}, \overline{{\rm y}_{t_2}}]


互相关矩阵
~~~~~~~~~~~~

设两个随机向量 :math:`\bf x = (\rm x_1, \rm x_2, \cdots, \rm x_m)^T` , :math:`\bf y = (\rm y_1, \rm y_2, \cdots, \rm y_m)^T` 的期望与方差存在, 则它们的 **互相关矩阵** ( :term:`Cross Correlation Matrix` ) 定义为

.. math::
    {{\bf{R}}_{{\bf{xy}}}}{ = }{\mathop{\rm E}\nolimits} \left[ {{\bf{x}}{{\bf{y}}^T}} \right] = \left[ {\begin{array}{cccc}{{\mathop{\rm E}\nolimits} [{{\rm x}_1}{{\rm y}_1}]}&{{\mathop{\rm E}\nolimits} [{{\rm x}_1}{{\rm y}_2}]}& \cdots &{{\mathop{\rm E}\nolimits} [{{\rm x}_1}{{\rm y}_n}]}\\{{\mathop{\rm E}\nolimits} [{{\rm x}_2}{{\rm y}_1}]}&{{\mathop{\rm E}\nolimits} [{{\rm x}_2}{{\rm y}_2}]}& \cdots &{{\mathop{\rm E}\nolimits} [{{\rm x}_2}{{\rm y}_n}]}\\ \vdots & \vdots & \vdots & \vdots \\{{\mathop{\rm E}\nolimits} [{{\rm x}_m}{{\rm y}_1}]}&{{\mathop{\rm E}\nolimits} [{{\rm x}_m}{{\rm y}_2}]}& \cdots &{{\mathop{\rm E}\nolimits} [{{\rm x}_m}{{\rm y}_n}]}\end{array}} \right]


.. hint::
    当随机向量 :math:`\bf x = (\rm x_1, \rm x_2, \cdots, \rm x_m)^T` , :math:`\bf y = (\rm y_1, \rm y_2, \cdots, \rm y_m)^T` 为复数随机向量时, 互相关矩阵定义为 :math:`\bf R_{\bf{xy}} = {\rm E}[\bf x \bf y^H]` .


性质
^^^^^^^^^


- 实随机向量 :math:`\bf x, \bf y` 不相关 :math:`\Leftrightarrow` :math:`{\rm E}[\bf x \bf y^T] = {\rm E}[\bf x]{\rm E}[\bf y]^T`
- 复随机向量 :math:`\bf x, \bf y` 不相关 :math:`\Leftrightarrow` :math:`{\rm E}[\bf x \bf y^H] = {\rm E}[\bf x]{\rm E}[\bf y]^H`


互协方差矩阵
~~~~~~~~~~~~~~~


设两个随机向量 :math:`\bf x = (\rm x_1, \rm x_2, \cdots, \rm x_m)^T` , :math:`\bf y = (\rm y_1, \rm y_2, \cdots, \rm y_m)^T` 的期望与方差存在, 则它们的 **互协方差矩阵** ( :term:`Cross Covariance Matrix` ) 定义为


.. math::
    {\bf K}_{\bf{xy}} = {\rm E}[({\bf x}-{\rm E}[\bf x])({\bf y} - {\rm E}[\bf y])^T]

.. hint::
    当随机向量 :math:`\bf x = (\rm x_1, \rm x_2, \cdots, \rm x_m)^T` , :math:`\bf y = (\rm y_1, \rm y_2, \cdots, \rm y_m)^T` 为复数随机向量时, 互相关矩阵定义为

    .. math::
        {\bf K}_{\bf{xy}} = {\rm E}[({\bf x}-{\rm E}[\bf x])({\bf y} - {\rm E}[\bf y])^H].


互相关与互协方差矩阵间关系
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 实随机向量: :math:`{\bf K}_{\bf{xy}} = {\rm E}[({\bf x}-{\rm E}[\bf x])({\bf y} - {\rm E}[\bf y])^T] = {\bf R}_{\bf{xy}} - E[\bf x]E[\bf y]^T`
- 复随机向量: :math:`{\bf K}_{\bf{xy}} = {\rm E}[({\bf x}-{\rm E}[\bf x])({\bf y} - {\rm E}[\bf y])^H] = {\bf R}_{\bf{xy}} - E[\bf x]E[\bf y]^H`




自相关
-------------

当互相关中的随机向量为同一向量时, 对应的互相关矩阵, 互协方差矩阵分别变为自相关矩阵, 自协方差矩阵.

自相关矩阵
~~~~~~~~~~~~

设随机向量 :math:`\bf x = (\rm x_1, \rm x_2, \cdots, \rm x_m)^T` 的期望与方差存在, 则它的 **自相关矩阵** ( :term:`Auto Correlation Matrix` ) 定义为

.. math::
    {{\bf{R}}_{{\bf{xx}}}}{ = }{\mathop{\rm E}\nolimits} \left[ {{\bf{x}}{{\bf{x}}^T}} \right] = \left[ {\begin{array}{cccc}{{\mathop{\rm E}\nolimits} [{{\rm x}_1}{{\rm x}_1}]}&{{\mathop{\rm E}\nolimits} [{{\rm x}_1}{{\rm x}_2}]}& \cdots &{{\mathop{\rm E}\nolimits} [{{\rm x}_1}{{\rm x}_m}]}\\{{\mathop{\rm E}\nolimits} [{{\rm x}_2}{{\rm x}_1}]}&{{\mathop{\rm E}\nolimits} [{{\rm x}_2}{{\rm x}_2}]}& \cdots &{{\mathop{\rm E}\nolimits} [{{\rm x}_2}{{\rm x}_m}]}\\ \vdots & \vdots & \vdots & \vdots \\{{\mathop{\rm E}\nolimits} [{{\rm x}_m}{{\rm x}_1}]}&{{\mathop{\rm E}\nolimits} [{{\rm x}_m}{{\rm x}_2}]}& \cdots &{{\mathop{\rm E}\nolimits} [{{\rm x}_m}{{\rm x}_m}]}\end{array}} \right]


.. hint::
    当随机向量 :math:`\bf x = (\rm x_1, \rm x_2, \cdots, \rm x_m)^T` 为复数随机向量时, 自相关矩阵定义为 :math:`\bf R_{\bf{xx}} = {\rm E}[\bf x \bf x^H]` .


自协方差矩阵
~~~~~~~~~~~~~~~


设两个随机向量 :math:`\bf x = (\rm x_1, \rm x_2, \cdots, \rm x_m)^T` 的期望与方差存在, 则它们的 **自协方差矩阵** ( :term:`Auto Covariance Matrix` ) 定义为


.. math::
    {\bf K}_{\bf{xx}} = {\rm E}[({\bf x}-{\rm E}[\bf x])({\bf x} - {\rm E}[\bf x])^T]

.. hint::
    当随机向量 :math:`\bf x = (\rm x_1, \rm x_2, \cdots, \rm x_m)^T` 为复数随机向量时, 自相关矩阵定义为

    .. math::
        {\bf K}_{\bf{xx}} = {\rm E}[({\bf x}-{\rm E}[\bf x])({\bf x} - {\rm E}[\bf x])^H].



自相关与自协方差矩阵间关系
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 实随机向量: :math:`{\bf K}_{\bf{xx}} = {\rm E}[({\bf x}-{\rm E}[\bf x])({\bf x} - {\rm E}[\bf x])^T] = {\bf R}_{\bf{xx}} - E[\bf x]E[\bf x]^T`
- 复随机向量: :math:`{\bf K}_{\bf{xx}} = {\rm E}[({\bf x}-{\rm E}[\bf x])({\bf x} - {\rm E}[\bf x])^H] = {\bf R}_{\bf{xx}} - E[\bf x]E[\bf x]^H`
