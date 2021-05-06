.. _Section-VectorNorm:

向量范数
=====================


概念与内涵
-----------------

.. _def-VectorNorm:

.. proof:definition:: 向量范数

    设 :math:`{\mathbb V}` 是数域 :math:`{\mathbb K}` 上的线性空间, 若对于 :math:`{\mathbb V}` 中的任意元素 :math:`{\bm x}` , 存在实数 :math:`\|{\bm x}\|` 满足:

    #. 非负性: :math:`\|{\bm x}\| \geq 0` , 当且仅当 :math:`{\bm x} = {\bm 0}` 时, 等号成立;
    #. 齐次性: :math:`\|k \odot \bm x \| = |k|\|\bm x\|` , ( :math:`k\in {\mathbb K}` , :math:`{\bm x} \in {\mathbb V}` )
    #. 三角不等式: :math:`\|{\bm x} \oplus {\bm y}\| \leq \|{\bm x}\| + \|{\bm y}\|` , ( :math:`{\bm{x, y} \in {\mathbb V}}` )

    则称 :math:`\|{\bm x}\|` 为向量 :math:`{\bm x}` 在线性空间 :math:`{\mathbb V}` 上的 **向量范数** .


.. hint::
   - 范数是实数, 为什么不定义复数呢?
   - 注意与内积的定义比较
   - 注意与矩阵范数的定义比较


向量范数的等价性
-----------------

设 :math:`\|{\bm x}\|_{\alpha}` , :math:`\|{\bm x}\|_{\beta}` 为有限维线性空间 :math:`{\mathbb V}` 上的任意两种范数, 则存在数 :math:`c_1, c_2` 与向量无关, 且使得对于 :math:`\forall {\bm x}\in {\mathbb V}`   如下不等式成立

.. math::
   c_1\|{\bm x}\|_{\beta} \leq \|{\bm x}\|_{\alpha} \leq c_2\|{\bm x}\|_{\beta}

称其为向量范数的等价性质.


.. hint::
   如对于向量的 :math:`\ell_1, \ell_2` 范数 :math:`|{\bm x}|, \|{\bm x}\|`

   .. figure:: ../../../_static/figs/BasisMath/MatrixTheory/NormTheory/demoNormEquivalence.png
        :scale: 80 %
        :alt: Norm Equivalence
        :align: center

        向量范数的等价性

        向量范数的等价性 :math:`\ell_1` (蓝, blue), :math:`\ell_2` (红, red)

常见向量范数
---------------------

普通向量范数
~~~~~~~~~~~~~~~~~~~~

设有线性空间 :math:`{\mathbb V}^n` , :math:`{\bm x} = (\xi_1, \xi_2, \cdots, \xi_n) \in {\mathbb V}^n` , 其中, :math:`\xi_i` 为 :math:`{\bm x}` 的第 :math:`i` 个坐标, :math:`|\xi_i|` 表示 :math:`\xi` 的模, 则有以下常见范数

- **p-范数** 或 :math:`\ell_p` 范数 : :math:`\|{\bm x}\|_p = \left( \sum_{i=1}^n |\xi|^p \right)^{1/p}` , :math:`1 \leq p < +\infty`
- **∞-范数** 或 :math:`\ell_{\infty}` 范数 : :math:`\|{\bm x}\|_{\infty} = \mathop {\max }\limits_i |\xi_i|` , ( :math:`p \to +\infty` )
- **1-范数** 或 :math:`\ell_1` 范数 : :math:`\|{\bm x}\|_1 = \sum_{i=1}^n|\xi_i|` , ( :math:`p = 1` )
- **2-范数** 或 :math:`\ell_2` 范数 : :math:`\|{\bm x}\|_2 = \sqrt{\sum_{i=1}^n|\xi_i|^2}` , ( :math:`p = 2` )


当 :math:`{\mathbb V}^n` 为复空间 :math:`{\mathbb C}^n` , 或实数空间 :math:`{\mathbb R}^n` 时也有上述范数.

.. note::
  对区间 :math:`[a, b]` 上的实值连续函数集合, 和实数域 :math:`{\mathbb R}` , 定义通常函数的加法, 实数与函数的数乘运算, 构成 :math:`{\mathbb R}` 上的一个线性空间 :math:`{\mathbb V}` , 有以下范数:

  - :math:`\|f(t)\|_p = \left[ \int_a^b |f(t)|^p|{\rm d}t \right]^{1/p}` , :math:`(1\leq p <+\infty)`
  - :math:`\|f(t)\|_{+\infty} = \mathop {\max }\limits_{t\in[a, b]} |f(t)|`



加权范数
~~~~~~~~~~~~

.. _def-WeightedNorm:

.. proof:definition:: 加权范数

    设 :math:`{\bm A}` 为 :math:`n` 阶对称正定阵, :math:`{\bm x}\in {\mathbb R}^n` , 则称

    .. math::
        \|{\bm x}\|_{{\bm A}} = ({\bm x}^T{\bm A}{\bm x})^{1/2}

    为 **加权范数** (:term:`Weighted Norm`) 或 **椭圆范数** .


    同理, 设 :math:`{\bm A}` 为 :math:`n` 阶Hermite对称正定阵, :math:`{\bm x}\in {\mathbb C}^n` , 则称

    .. math::
        \|{\bm x}\|_{{\bm A}} = ({\bm x}^H{\bm A}{\bm x})^{1/2}

    为 **加权范数** (:term:`Weighted Norm`) 或 **椭圆范数** .



