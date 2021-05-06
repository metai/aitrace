.. _Section-KKTCondition:

KKT条件
=====================

:term:`Karush–Kuhn–Tucker` (KKT) 条件给出了一类约束优化问题的解的约束, 通过这些约束可以求解优化问题.


概念与内涵
------------


考虑如下非线性最小或最大化问题


.. math::
    {P}_0 : \begin{array}{l}{\min_{\bm x} f({\bm x})} \\ {\text {s.t.}} \left\{\begin{array}{c}{g_{i}({\bm x}) = 0, i=1,2, \ldots, M_g} \\ {h_{j}({\bm x}) \leq 0, j=1,2, \ldots, M_h}\end{array}\right. \end{array}

其中, :math:`{\bm x}, {\bm \alpha}, {\bm \beta}` 为待求变量. :math:`{\bm \alpha}, {\bm \beta}` 为由KKT乘子组成的向量, 上式转化为拉格朗日函数

.. math::
    {P}_1 : L({\bm x}, {\bm \alpha}, {\bm \beta}) = f({\bm x}) + \sum_{i=1}^{M_g}{\alpha_i}g_i({\bm x}) + \sum_{j=1}^{M_h}{\beta_j}h_j({\bm x})
    :label: equ-LagrangianFunctionKKT

则其解满足如下KKT条件

.. math::
    \begin{aligned} \nabla_{{\bm x}} L({\bm x}^{*}, {\bm \alpha}^{*}, {\bm \beta}^{*}) &=0 \\ \beta_{j}^{*} h_{j}({\bm x}^{*}) &=0, j=1,2, \ldots, M_h \\ g_{i}({\bm x}^{*}) &=0, i=1,2, \ldots, M_g \\ h_{j}({\bm x}^{*}) & \leq 0, j=1,2, \ldots, M_h \\ \beta_{j}^{*} & \geq 0, j=1,2, \ldots, M_h \end{aligned}
    :label: equ-KKTCondition

其中, :math:`{\bm \alpha}^{*}=[\alpha_1^{*},\alpha_2^{*},\cdots,\alpha_{M_g}^{*}]^T`, :math:`{\bm \beta}^{*}=[\beta_1^{*},\beta_2^{*},\cdots,\beta_{M_g}^{*}]`, :math:`{\bm x}^{*}=[x_1^{*},x_2^{*},\cdots,x_{N}^{*}]`.

KKT条件是使一组解成为最优解的必要条件, 当原问题是凸优化问题的时, KKT条件也是充分条件.


.. hint::
    当 :math:`M_h = 0` 即不含不等式约束时, 一般称为拉格朗日乘子法.






