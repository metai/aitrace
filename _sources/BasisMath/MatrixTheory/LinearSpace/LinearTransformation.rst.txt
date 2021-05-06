.. _Section-LinearTransformation:

线性变换及其表示
================

线性变换
--------

什么是线性变换
~~~~~~~~~~~~~~~~~~~


.. _def-Transformation:

.. proof:definition:: 变换

   设\ :math:`{\mathbb V}`\ 是数域\ :math:`\mathbb K`\ 上的线性空间,
   :math:`T`\ 是\ :math:`{\mathbb V}`\ 到自身的一个映射, 使得对于
   :math:`\forall {\bm x} \in {\mathbb V}`,
   :math:`{\mathbb V}`\ 中都有唯一的向量\ :math:`\bm y`\ 与之对应, 则称 :math:`T`
   是\ :math:`{\mathbb V}`\ 的一个 **变换** 或 **算子** , 记为

   .. math:: T {\bm x} = {\bm y}

   称\ :math:`{\bm y}`\ 为\ :math:`{\bm x}`\ 在\ :math:`T`\ 下的象,
   :math:`{\bm x}` 为 :math:`{\bm y}` 的原象.

.. warning::

	-  :math:`T`\ 是\ :math:`{\mathbb V}`\ 到自身的一个映射:
	   即变换前后都在线性空间\ :math:`{\mathbb V}`\ 中,
	   **如果变换前后不在同一线性空间中?**.

	-  定义中说明了\ :math:`{\mathbb V}`\ 中的元素为向量,
	   实际上\ :math:`{\mathbb V}`\ 中元素不一定是向量.


.. _def-LinearTransformation:

.. proof:definition:: 线性变换

   设\ :math:`T`\ 是数域\ :math:`K`\ 上线性空间\ :math:`{\mathbb V}`\ 中的一个变换,
   对于\ :math:`\forall k, l\in K`, 若满足

   .. math:: T(k{\bm x} \oplus l{\bm y}) = kT({\bm x}) \oplus lT(\bm y)

   则称\ :math:`T`\ 是\ :math:`{\mathbb V}`\ 的线性变换.


线性变换的特性
~~~~~~~~~~~~~~~

若线性空间 :math:`{\mathbb V}` 中的 :math:`{\bm x}_1, {\bm x}_2, \cdots, {\bm x}_m` 线性相关, 则线性变换 :math:`T` 对其变换后仍线性相关.

即若存在不全为零的数 :math:`c_1, c_2, \cdots, c_m \in K` , 使得

.. math:: c_1 \odot {\bm x}_1 \oplus c_2 \odot {\bm x}_2 \oplus \cdots \oplus c_m \odot {\bm x}_m = {\bm 0}

成立, 则亦有下式成立

.. math:: c_1 \odot (T{\bm x}_1) \oplus c_2 \odot (T{\bm x}_2) \oplus \cdots \oplus c_m \odot (T{\bm x}_m) = T{\bm 0} = {\bm 0}



线性变换的运算
--------------

涉线性变换的加法, 数乘, 乘法, 逆与幂, 以及单位变换, 零变换, 负变换, 逆变换, 多项式. 有关对称变换, 正交变换, 酉变换参见 :ref:`Section-SpecialLinearSpace` 小节

.. hint::
	可以证明上述变换均为线性变换!

基本线性变换
~~~~~~~~~~~~~~


单位变换
^^^^^^^^^

将线性空间 :math:`{\mathbb V}` 中的任一元素 :math:`{\bm x}` 变为自身的变换称为 **单位变换** , 即

.. math::
	(T_e){\bm x} = {\bm x} , \   (\forall {\bm x} \in {\mathbb V})


零变换
^^^^^^

将线性空间 :math:`{\mathbb V}` 中的任一元素 :math:`{\bm x}` 变为零元素 :math:`{\bm 0}`  的变换称为 **零变换** , 即

.. math::
	(T_0){\bm x} = {\bm 0} , \   (\forall {\bm x} \in {\mathbb V})


负变换
^^^^^^

设 :math:`T` 是线性空间 :math:`{\mathbb V}` 的线性变换, 线性变换 :math:`T` 的 **负变换** 定义为

.. math::
	(-T){\bm x} = -(T{\bm x}) , \   (\forall {\bm x} \in {\mathbb V})


逆变换
^^^^^^

设 :math:`T, T^{-1}` 是线性空间 :math:`{\mathbb V}` 的线性变换, 若满足下述条件, 则称线性变换 :math:`T` 与 :math:`T^{-1}` 互为 **逆变换** (Inverse transformation) , 即

.. math::
	(T T^{-1}){\bm x} = (T^{-1} T){\bm x} = {\bm x} , \   (\forall {\bm x} \in {\mathbb V})

亦即:

.. math::
	(T T^{-1}) = (T^{-1} T) = T_e


加法
~~~~~~~~~

定义
^^^^^^

设 :math:`T_1, T_2` 是线性空间 :math:`{\mathbb V}` 的两个线性变换, 线性变换的 **加法** 定义为

.. math::
  	(T_1 + T_2){\bm x} = T_1{\bm x} \oplus T_2{\bm x}, \    (\forall {\bm x} \in {\mathbb V})

性质
^^^^^^

#. 交换律: :math:`T_1 + T_2 = T_2 + T_1`
#. 结合律: :math:`(T_1 + T_2) + T_3 = T_1 + (T_2 + T_3)`
#. 有零元: :math:`T + T_0 = T`
#. 有负元: :math:`T + (-T) = T_0`

.. hint:: 对照线性空间定义中的加法的性质.



数乘
~~~~~~~~~

定义
^^^^^^

设 :math:`k \in K` , :math:`T` 为线性空间 :math:`{\mathbb V}` 的线性变换, 定义数 :math:`k` 与变换 :math:`T` 的乘积( **数乘** ) :math:`kT`  为

.. math::
	(kT){\bm x} = k\odot(T{\bm x}) , \  (\forall {\bm x} \in {\mathbb V})


性质
^^^^^^

#. 乘1律: :math:`1T = T`
#. 数因子分配律: :math:`k(T_1 + T_2) = kT_1 + kT_2`
#. 数乘分配率: :math:`(k + l)T = kT + lT`
#. 数乘结合率: :math:`(kl)T = k(lT)`

.. hint:: 对照线性空间定义中的数乘的性质.



乘法
~~~~~~~~~

定义
^^^^^^

设 :math:`T_1, T_2` 是线性空间 :math:`{\mathbb V}` 的两个线性变换, 定义 :math:`T_1` 与 :math:`T_2` 的 **乘积** :math:`T_1T_2` 为

.. math::
     	(T_1T_2){\bm x} = T_1(T_2 {\bm x}) , \  (\forall {\bm x} \in {\mathbb V})


性质
^^^^^^

#. 结合律: :math:`(T_1T_2)T_3 = T_1(T_2T_3)`
#. 分配律1: :math:`T_1(T_2 + T_3) = T_1T_2 + T_1T_3`
#. 分配率2: :math:`(T_1 + T_2)T_3 = T_1T_3 + T_2T_3`


幂
~~~~~~~~~

定义
^^^^^^

设 :math:`n` 是正整数, :math:`T` 是线性空间 :math:`{\mathbb V}` 中的线性变换, 定义其 :math:`n` **次幂** 为

.. math::
   	T^n = T^{n-1}T  , \   (n=2,3,\cdots)

定义 :math:`T` 的 **零次幂** 为:

.. math::
	T^0 = T_e

性质
^^^^^^

#. 性质1: :math:`T^{m+n} = T^m T^n`
#. 性质2: :math:`(T^m)^n = T^{mn}`
#. 性质3: :math:`T^{(-n)} = (T^{-1})^n`


线性变换的多项式
~~~~~~~~~~~~~~~~~~

定义
^^^^^^

数量 :math:`t` 的 :math:`m` 次多项式可以定义为

.. math::
	f(t) = a_m t^m + a_{m-1} t^{m-1} + \cdots + a_1t + a_0

类似地, 线性变换 :math:`T` 的 :math:`m` 次多项式可以定义为

.. math::
	f(T) = a_m T^m + a_{m-1} T^{m-1} + \cdots + a_1T + a_0

性质
^^^^^^

#. 性质1: 若 :math:`h(t) = f(t)g(t)` , 则 :math:`h(T) = f(T)g(T)`
#. 性质2: 若 :math:`p(t) = f(t) + g(t)` , 则 :math:`p(T) = f(T) + g(T)`
#. 性质3: :math:`f(T)g(T) = g(T)f(T)` (同一线性变换的多项式相乘可交换)


线性变换与矩阵
--------------

线性变换的矩阵表示
~~~~~~~~~~~~~~~~~~

设 :math:`T` 是线性空间 :math:`{\mathbb V}` 中的线性变换, :math:`{\bm x} \in {\mathbb V}^n` , 且 :math:`{\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n` 是 :math:`{\mathbb V}^n` 的一个基 (原象基组), 则

.. math::
 	{\bm x} = a_1\odot{\bm x}_1 \oplus a_2\odot{\bm x}_2 \oplus \cdots \oplus a_n\odot{\bm x}_n

.. math::
 	T{\bm x} = a_1\odot(T{\bm x}_1) \oplus a_2\odot(T{\bm x}_2) \oplus \cdots \oplus a_n\odot(T{\bm x}_n)

故 :math:`{\bm x}` 在变换 :math:`T` 下得到的象 :math:`T{\bm X}` 可以由基象组线性表示, 而基像组仍在线性空间 :math:`{\mathbb V}` 中, 故可用原象组线性表示为

.. math::
   \left\{ {\begin{array}{ccc}
   {T{{\bm{x}}_1} = {a_{11}}\odot{{\bm{x}}_1} \oplus {a_{21}}\odot{{\bm{x}}_2} \oplus  \cdots  \oplus {a_{n1}}\odot{{\bm{x}}_n}}\\
   {T{{\bm{x}}_2} = {a_{12}}\odot{{\bm{x}}_1} \oplus {a_{22}}\odot{{\bm{x}}_2} \oplus  \cdots  \oplus {a_{n2}}\odot{{\bm{x}}_n}}\\
    \vdots \\
   {T{{\bm{x}}_n} = {a_{1n}}\odot{{\bm{x}}_1} \oplus {a_{2n}}\odot{{\bm{x}}_2} \oplus  \cdots  \oplus {a_{nn}}\odot{{\bm{x}}_n}}
   \end{array}} \right.

将上述方程组矩阵化可得, 线性变换 :math:`T` 在基 :math:`{\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n` 下的矩阵表示为

.. math::
	T({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n)
	= (T{\bm x}_1 , T{\bm x}_2 , \cdots, T{\bm x}_n)
	= ({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n){\bm A}

其中

.. math::
	{\bm A} = \left[ {\begin{array}{cccc}{{a_{11}}}&{{a_{12}}}& \cdots &{{a_{1n}}}\\{{a_{21}}}&{{a_{22}}}& \cdots &{{a_{2n}}}\\ \vdots & \vdots &{}& \vdots \\{{a_{n1}}}&{{a_{n2}}}& \cdots &{{a_{nn}}}\end{array}} \right]

矩阵 :math:`{\bm A}` 的第 :math:`i` 列为 :math:`T{\bm x}_i` 的坐标. 当 :math:`\oplus` 表示普通向量加法, :math:`\odot` 表示普通数与向量乘法时, 上式退化为普通矩阵乘.


.. note::
   举个例子, 定义线性空间 :math:`{\mathbb R}^{2\times 2}` 中的线性变换

   .. math::
      T{\bm X} = \left[ {\begin{array}{cc} a&b\\ c&d \end{array}} \right] {\bm X}

   求线性变换 :math:`T` 在基 :math:`{\bm E}_{11}, {\bm E}_{12}, {\bm E}_{21}, {\bm E}_{22}` 下的矩阵.

   解: 由题意有

   .. math::
      \left\{ {\begin{array}{ccc}
      {T{{\bm{E}}_{11}} = \left[ {\begin{array}{ccc}
      a&b\\
      c&d
      \end{array}} \right]\left[ {\begin{array}{ccc}
      1&0\\
      0&0
      \end{array}} \right] = \left[ {\begin{array}{ccc}
      a&0\\
      c&0
      \end{array}} \right] = a{{\bm{E}}_{11}} + c{{\bm{E}}_{21}}}\\
      {T{{\bm{E}}_{12}} = \left[ {\begin{array}{ccc}
      a&b\\
      c&d
      \end{array}} \right]\left[ {\begin{array}{ccc}
      0&1\\
      0&0
      \end{array}} \right] = \left[ {\begin{array}{ccc}
      0&a\\
      0&c
      \end{array}} \right] = a{{\bm{E}}_{12}} + c{{\bm{E}}_{22}}}\\
      {T{{\bm{E}}_{21}} = \left[ {\begin{array}{ccc}
      a&b\\
      c&d
      \end{array}} \right]\left[ {\begin{array}{ccc}
      0&0\\
      1&0
      \end{array}} \right] = \left[ {\begin{array}{ccc}
      b&0\\
      d&0
      \end{array}} \right] = b{{\bm{E}}_{11}} + d{{\bm{E}}_{21}}}\\
      {T{{\bm{E}}_{22}} = \left[ {\begin{array}{ccc}
      a&b\\
      c&d
      \end{array}} \right]\left[ {\begin{array}{ccc}
      0&0\\
      0&1
      \end{array}} \right] = \left[ {\begin{array}{ccc}
      0&b\\
      0&d
      \end{array}} \right] = b{{\bm{E}}_{12}} + d{{\bm{E}}_{22}}}
      \end{array}} \right.

   由上式得到 :math:`T` 在所给基下的矩阵为

   .. math::
      {\bm A} = \left[ {\begin{array}{cccc}
      a&0&b&0\\
      0&a&0&b\\
      c&0&d&0\\
      0&c&0&d
      \end{array}} \right]

   满足 :math:`T({\bm E}_{11}, {\bm E}_{12}, {\bm E}_{21}, {\bm E}_{22}) = ({\bm E}_{11}, {\bm E}_{12}, {\bm E}_{21}, {\bm E}_{22}) {\bm A}`


.. hint::

	1. 零变换的矩阵为零矩阵: :math:`{\bm O}`

	2. 单位变换的矩阵为单位矩阵: :math:`{\bm I}`

	3. 数乘变换的矩阵为数量矩阵: :math:`m{\bm I}`


性质
~~~~~~~~

#. :math:`(T_1 + T_2)({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n) = ({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n)({\bm A}+{\bm B})`
#. :math:`(kT_1)({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n) = ({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n)(k{\bm A})`
#. :math:`(T_1 T_2)({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n) = ({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n){\bm A}{\bm B}`
#. :math:`(T_1^{-1})({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n) = ({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n){\bm A}^{-1}`


像与原像的坐标转换
~~~~~~~~~~~~~~~~~~

设有线性空间 :math:`{\mathbb V}^n` 中的元素 :math:`{\bm x}` , 线性变换 :math:`T` , 一组基 :math:`{\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n` ; :math:`{\bm x}` 在该基下的坐标为 :math:`(\xi_1, \xi_2, \cdots, \xi_n)^T` , :math:`T` 在该基下的的矩阵为 :math:`{\bm A}` ; 则 :math:`T{\bm x}` 在该基下的坐标为

.. math::
    \left[ {\begin{array}{lll}{{\eta _1}}\\{{\eta _2}}\\ \vdots \\{{\eta _n}}\end{array}} \right] = {\bm{A}}\left[ {\begin{array}{lll}{{\xi _1}}\\{{\xi _2}}\\ \vdots \\{{\xi _n}}\end{array}} \right]

.. hint::
	.. math::
		T{\bm{x}} = T({{\bm{x}}_1},\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n})\left[ {\begin{array}{lll}{{\xi _1}}\\{{\xi _2}}\\ \vdots \\{{\xi _n}}\end{array}} \right] = ({{\bm{x}}_1},\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}){\bm{A}}\left[ {\begin{array}{lll}{{\xi _1}}\\{{\xi _2}}\\ \vdots \\{{\xi _n}}\end{array}} \right]


线性变换在不同基下的矩阵转换
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

设有线性空间 :math:`{\mathbb V}^n` 中的线性变换 :math:`T` , 在基 :math:`{\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n` 和基 :math:`{\bm y}_1 , {\bm y}_2 , \cdots, {\bm y}_n` 下的矩阵分别为 :math:`{\bm A}, {\bm B}` , 且由基1到基2的过度矩阵为 :math:`{\bm C}` , 则有

.. math::
    	{\bm B} = {\bm C}^{-1}{\bm A}{\bm C}

.. hint::

	.. math::
		\begin{array}{l}T{\bm{x}} = T({{\bm{x}}_1},\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}) = ({{\bm{x}}_1},\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}){\bm{A}}\\T{\bm{y}} = T({{\bm{y}}_1},\;{{\bm{y}}_2}, \cdots ,{{\bm{y}}_n}) = ({{\bm{y}}_1},\;{{\bm{y}}_2}, \cdots ,{{\bm{y}}_n}){\bm{B}}\\T{\bm{y}} = T({{\bm{y}}_1},\;{{\bm{y}}_2}, \cdots ,{{\bm{y}}_n}) = T({{\bm{x}}_1},\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}){\bm{C}}\\\;\;\;\; = ({{\bm{x}}_1},\;{{\bm{x}}_2}, \cdots ,{{\bm{x}}_n}){\bm{AC}}{\rm{ = }}({{\bm{y}}_1},\;{{\bm{y}}_2}, \cdots ,{{\bm{y}}_n}){{\bm{C}}^{{\rm{ - }}1}}{\bm{AC}}\end{array}


相似矩阵
~~~~~~~~~~~

什么是相似矩阵
^^^^^^^^^^^^^^

由线性变换在不同基下的矩阵关系引出矩阵相似定义:

.. _def-SimilarMatrix:

.. proof:definition:: 相似矩阵

   设有矩阵 :math:`{\bm A}, {\bm B}` , 若存在 *非奇异矩阵* :math:`{\bm P}` 使得 :math:`{\bm B} = {\bm P}^{-1}{\bm A}{\bm P}` , 则称 :math:`{\bm A}` **相似于** :math:`{\bm B}` , 记作 :math:`{\bm A} \sim {\bm B}` .

.. warning:: 矩阵合同是指 :math:`{\bm B} = {\bm P}^{T}{\bm A}{\bm P}`


若 :math:`{\bm B} = {\bm P}^{-1}{\bm A}{\bm P}` , 且 :math:`f(t)` 是数域 :math:`K` 上的多项式, 则有

.. math::
 	f({\bm B}) = {\bm P}^{-1} f({\bm A}) {\bm P}

性质
^^^^^^^^^

#. 反身性: :math:`A \sim A`
#. 对称性: 若 :math:`{\bm A} \sim {\bm B}` , 则 :math:`{\bm B} \sim {\bm A}`
#. 传递性: 若 :math:`{\bm A} \sim {\bm B}, {\bm B} \sim {\bm C}` , 则 :math:`{\bm A} \sim {\bm C}`


线性变换多项式的矩阵
~~~~~~~~~~~~~~~~~~~

数量 :math:`t` 的 :math:`m` 次多项式可以定义为

.. math::
	f(t) = a_m t^m + a_{m-1} t^{m-1} + \cdots + a_1t + a_0

类似地, 线性空间 :math:`{\mathbb V}^n` 中，线性变换 :math:`T` 的 :math:`m` 次多项式可以定义为

.. math::
	f(T) = a_m T^m + a_{m-1} T^{m-1} + \cdots + a_1T + a_0

设线性空间 :math:`{\mathbb V}^n` 中，线性变换 :math:`T` 在基 :math:`{\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n` 下的矩阵为 :math:`{\bm A}` , 即

.. math::
	T({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n)
	= ({\bm x}_1 , {\bm x}_2 , \cdots, {\bm x}_n){\bm A}

则 :math:`f(T)` **在该基下的的矩阵** 为

.. math::
	f({\bm A}) = a_m{\bm A}^m + a_{m-1}{\bm A}^{m-1} + \cdots + a_{1}{\bm A} + a_0{\bm I}

上式也称为方阵 :math:`{\bm A}` 的多项式.



常见线性变换
~~~~~~~~~~~~~~~~~~~

伸缩, 旋转, 对称变换举例

- 伸缩: :math:`\left[ {\begin{array}{rrr}k&0\\0&k\end{array}} \right]\left[ {\begin{array}{ccc}{{x_1}}\\{{x_2}}\end{array}} \right] = \left[ {\begin{array}{ccc}{k{x_1}}\\{k{x_2}}\end{array}} \right],\;\;\left[ {\begin{array}{rrr}{{k_1}}&0\\0&{{k_2}}\end{array}} \right]\left[ {\begin{array}{rrr}{{x_1}}\\{{x_2}}\end{array}} \right] = \left[ {\begin{array}{rrr}{{k_1}{x_1}}\\{{k_2}{x_2}}\end{array}} \right]`
- 逆时针旋转: :math:`\left[ {\begin{array}{rrr}{\cos \theta }&{ - \sin \theta }\\{\sin \theta }&{\cos \theta }\end{array}} \right]\left[ {\begin{array}{ccc}{{x_1}}\\{{x_2}}\end{array}} \right] = \left[ {\begin{array}{ccc}{{x_1}\cos \theta  - {x_2}\sin \theta }\\{{x_1}\sin \theta  + {x_2}\cos \theta }\end{array}} \right]`
- 顺时针旋转: :math:`\left[ {\begin{array}{rrr}{\cos \theta }&{\sin \theta }\\{ - \sin \theta }&{\cos \theta }\end{array}} \right]\left[ {\begin{array}{ccc}{{x_1}}\\{{x_2}}\end{array}} \right] = \left[ {\begin{array}{ccc}{{x_1}\cos \theta  + {x_2}\sin \theta }\\{ - {x_1}\sin \theta  + {x_2}\cos \theta }\end{array}} \right]`
- 轴对称: :math:`\left[ {\begin{array}{rrr}1&0\\0&{ - 1}\end{array}} \right]\left[ {\begin{array}{ccc}{{x_1}}\\{{x_2}}\end{array}} \right] = \left[ {\begin{array}{ccc}{{x_1}}\\{ - {x_2}}\end{array}} \right],\;\;\left[ {\begin{array}{rrr}{ - 1}&0\\0&1\end{array}} \right]\left[ {\begin{array}{ccc}{{x_1}}\\{{x_2}}\end{array}} \right] = \left[ {\begin{array}{ccc}{ - {x_1}}\\{{x_2}}\end{array}} \right]`

.. figure:: ../../../_static/figs/BasisMath/MatrixTheory/LinearSpace/transformation.png
   :scale: 50 %
   :alt: example transformation
   :align: center

   变换举例

   变换举例, 伸缩, 旋转, 对称变换

.. hint::
   记忆旋转变换

   - 逆时针旋转: 第一象限一个向量, 逆时针旋转一个小角度, :math:`x` 坐标减小, :math:`y` 坐标增大
   - 顺时针旋转: 第一象限一个向量, 逆时针旋转一个小角度, :math:`x` 坐标增大, :math:`y` 坐标减小

下面借助 ``Python`` 工具实现旋转变换的验证:

1. 产生二维平面内椭圆内的随机点构成椭圆面 :math:`S` ;
2. 将椭圆面 :math:`S` 分别进行逆时针与顺时针旋转;
3. 绘制旋转前后的图像.

结果如下图

.. figure:: ../../../_static/figs/BasisMath/MatrixTheory/LinearSpace/Transformation/demo_rotation.png
   :scale: 30 %
   :alt: demo of rotation
   :align: center

   旋转变换举例.

   旋转变换举例: 原始图(左), 逆时针旋转 :math:`30` 度(中), 顺时针旋转 :math:`30` 度(右).


实现代码, 参见文件 `demo_rotation_ellipse.py <../../../_static/src/python/BasisMath/MatrixTheory/LinearSpace/demo_rotation_ellipse.py>`_  .

.. literalinclude:: ../../../_static/src/python/BasisMath/MatrixTheory/LinearSpace/demo_rotation_ellipse.py
   :emphasize-lines: 32, 43
   :linenos:
   :caption: demo_rotation_ellipse.py
   :name: bind-id

总结
-------

-  线性变换对向量组相关性的影响
   -  线性相关向量组 --> 线性变换 --> 线性相关
   -  线性无关向量组 --> 线性变换 --> 线性无关或线性相关（如零变换）

-  线性变换 :math:`T` 与其对应矩阵 :math:`A`
   -  它们的值域、核、秩、亏相同
