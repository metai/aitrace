.. _Section-MembershipFunction:

隶属函数
=====================

什么是隶属函数
---------------------

**隶属函数** (:term:`Membership Function`) 是模糊集合的核心概念, 反映了元素属于模糊集合的隶属度(:term:`Membership Degree`, :term:`Membership Grade`). 模糊集的隶属函数与明确集的指示函数(:term:`Indicator function`)或特征函数(:term:`characteristic function`)相对应.

 The membership function of a fuzzy set is a generalization of the indicator function in classical sets. In fuzzy logic, it represents the degree of truth as an extension of valuation. Degrees of truth are often confused with probabilities, although they are conceptually distinct, because fuzzy truth represents membership in vaguely defined sets, not likelihood of some event or condition. Membership functions were introduced by Zadeh in the first paper on fuzzy sets (1965). Zadeh, in his theory of fuzzy sets, proposed using a membership function (with a range covering the interval (0,1)) operating on the domain of all possible values.

.. _defMembershipFunction:

.. proof:definition:: 隶属函数

   对于任意集合 :math:`\mathbb X`, 其上的 **隶属函数** 为从 :math:`\mathbb X` 到区间 :math:`[0, 1]` 的任意映射函数 :math:`f: {\mathbb X} \rightarrow [0, 1]` . 

隶属函数与模糊集合一一对应, 模糊集合 :math:`{\mathbb A} \subset {\mathbb X}` 的隶属函数通常表示为 :math:`\mu_{\mathbb A}` , 对于 :math:`x\in{\mathbb X}`, :math:`\mu_{\mathbb A}(x)` 表示隶属度, :math:`\mu_{\mathbb A}(x) = 0` 意味着 :math:`x` 不属于 :math:`\mathbb A` ; :math:`\mu_{\mathbb A}(x) = 1` 意味着 :math:`x` 完全属于 :math:`\mathbb A`; :math:`0 < \mu_{\mathbb A}(x) < 1` 意味着 :math:`x` 部分属于 :math:`\mathbb A` .


.. figure:: ../../../_static/figs/BasisMath/FuzzyMath/FuzzySets/MembershipFunction.png
   :scale: 100 %
   :alt: Membership Function of crisp set and fuzzy set
   :align: center

   Membership Function of crisp set(blue) and fuzzy set (green).

   Membership Function of crisp set and fuzzy set.


常见隶属函数
---------------------

钟形曲线
~~~~~~~~~~~~~

钟形 (bell shape) 隶属函数表达式如下:

.. math::
   f(x) = \frac{1}{1 + |\frac{x-c}{a}|^{2b}}

其中, :math:`c` 决定了钟形曲线的位置, :math:`a, b` 决定了钟形曲线的形状.

.. figure:: ../../../_static/figs/BasisMath/FuzzyMath/FuzzySets/BellShapeMF.png
   :scale: 100 %
   :alt: Bell Shape Membership Function
   :align: center

   Bell Shape Membership Function.

   Bell Shape Membership Function.


高斯函数
~~~~~~~~~~~~~

高斯函数 (Gauss Function) 也称高斯径向基函数(Gauss Radial Basis function, RBF), 其表达式如下:

.. math::
   f(x) = {\rm exp}\left(\frac{-\|x-c\|^2}{a^2}\right)

其中, :math:`c` 为中心/均值, :math:`a` 表示标准差.

.. figure:: ../../../_static/figs/BasisMath/FuzzyMath/FuzzySets/GaussMF.png
   :scale: 100 %
   :alt: Gauss Membership Function
   :align: center

   Gauss Membership Function.

   Gauss Membership Function.