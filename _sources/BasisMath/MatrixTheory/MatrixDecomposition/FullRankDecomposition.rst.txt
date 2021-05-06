.. _Section-FullRankDecomposition:

满秩分解
=====================

什么是满秩分解
---------------

满秩分解( :term:`Full Rank Decomposition` ) 是指将一矩阵分解为行满秩与列满秩的两个矩阵的乘积的分解.

.. _def-FullRankDecomposition:

.. proof:definition:: 满秩分解

   设 :math:`{\bm A} \in {\mathbb C}_r^{m\times n} (r>0)` , 若存在矩阵 :math:`{\bm F} \in {\mathbb C}_r^{m\times r} (r>0)`  和 :math:`{\bm G} \in {\mathbb C}_r^{r\times n} (r>0)` 使得

   .. math::
   	{\bm A}_r^{m\times n} = {\bm F}_r^{m\times r} {\bm G}_r^{r\times n}

   则称上述分解为 **满秩分解** . 其中, :math:`r` 为矩阵 :math:`{\bm A}, {\bm F} , {\bm G}` 的秩.


求解方法
---------

初等行变换法
~~~~~~~~~~~~~

对矩阵 :math:`{\bm A} \in {\mathbb C}_r^{m\times n} (r>0)` 进行满秩分解的步骤如下:

#. 仅使用初等行变换, 将 :math:`{\bm A} \in {\mathbb C}_r^{m\times n} (r>0)` 化为行阶梯标准型 :math:`{\bm B} \in {\mathbb C}_r^{m\times n} (r>0)` ;
#. 列满秩矩阵 :math:`{\bm F}_r^{m\times r}` 取为矩阵 :math:`{\bm A}` 的前 :math:`r` 列构成的 :math:`{m\times r}` 的矩阵;
#. 行满秩矩阵 :math:`{\bm G}_r^{r\times n}` 取为矩阵 :math:`{\bm B}` 的前 :math:`r` 行构成的 :math:`{r\times n}` 的矩阵.


.. hint::
	行阶梯标准型又称 **Hermite标准型** , 是指满足如下条件的矩阵 :math:`{\bm B} \in {\mathbb C}_r^{m\times n} (r>0)`

	1. :math:`{\bm B}` 的前 :math:`r` 行中每一行至少含一个非零元素, 且第一个非零元素是 :math:`1` , 后 :math:`m-r` 行元素均为零;
	2. :math:`{\bm B}` 的前 :math:`r` 列为单位阵 :math:`{\bm I}_m` 的前 :math:`r` 列.

   可见, Hermite标准型矩阵具备如下形式:

   .. math::
      {\bm{B}} = \left[ {\begin{array}{ll}
      {{{\bm{I}}_{r \times r}}}&{{{\bm{K}}_{r \times (n - r)}}}\\
      {{{\bm{O}}_{(m - r) \times r}}}&{{{\bm{O}}_{(m - r) \times (n - r)}}}
      \end{array}} \right]

   其中, :math:`\bm K` 为任意 :math:`r\times(n-r)` 矩阵.

	如矩阵 :math:`\left[ {\begin{array}{cccc}1&0&0&0\\0&1&{{\rm{ - }}1}&{{\rm{ - }}1}\\0&0&0&0\\0&0&0&0\end{array}} \right]`


.. note::
   举个例子, 求如下矩阵的满秩分解

   .. math::
      {\bm A} = \left[ {\begin{array}{cccc}
      1&0&0&1\\
      1&1&0&0\\
      0&1&1&0\\
      0&0&1&1
      \end{array}} \right]

   1. 仅使用初等行变换将其化为Hermite标准形:

   .. math::
      \left[ {\begin{array}{cccc}
      1&0&0&1\\
      1&1&0&0\\
      0&1&1&0\\
      0&0&1&1
      \end{array}} \right]\mathop  \to \limits^{{r_2} - {r_1}} \left[ {\begin{array}{cccc}
      1&0&0&1\\
      0&1&0&{ - 1}\\
      0&1&1&0\\
      0&0&1&1
      \end{array}} \right]\mathop  \to \limits^{{r_3} - {r_2}} \left[ {\begin{array}{cccc}
      1&0&0&1\\
      0&1&0&{ - 1}\\
      0&0&1&1\\
      0&0&1&1
      \end{array}} \right]\mathop  \to \limits^{{r_4} - {r_3}} \left[ {\begin{array}{cccc}
      1&0&0&1\\
      0&1&0&{ - 1}\\
      0&0&1&1\\
      0&0&0&0
      \end{array}} \right] = {\bm{B}}

   可见 :math:`r = 3` .

   2. 列满秩矩阵 :math:`{\bm F}_r^{m\times r}` 取为矩阵 :math:`{\bm A}` 的前 :math:`r` 列构成的 :math:`{m\times r}` 的矩阵

   .. math::
      \left[ {\begin{array}{cc}
      {\begin{array}{c}
      1\\
      1\\
      0\\
      0
      \end{array}}&{\begin{array}{c}
      0\\
      1\\
      1\\
      0
      \end{array}}
      \end{array}} \right]


   3. 行满秩矩阵 :math:`{\bm G}_r^{r\times n}` 取为矩阵 :math:`{\bm B}` 的前 :math:`r` 行构成的 :math:`{r\times n}` 的矩阵

   .. math::
      \left[ {\begin{array}{cc}
      {\begin{array}{cccc}
      1&0&0&1
      \end{array}}\\
      {\begin{array}{cccc}
      0&1&0&{ - 1}
      \end{array}}
      \end{array}} \right]

   则有如下满秩分解：

   .. math::
      {{\bm{A}}_{4 \times 4}} = {{\bm{F}}_{4 \times 3}}{{\bm{G}}_{3 \times 4}} = \left[ {\begin{array}{ccc}
      {\begin{array}{cccc}
      1\\
      1\\
      0\\
      0
      \end{array}}&{\begin{array}{cccc}
      0\\
      1\\
      1\\
      0
      \end{array}}&{\begin{array}{cccc}
      0\\
      0\\
      1\\
      1
      \end{array}}
      \end{array}} \right]\left[ {\begin{array}{lll}
      {\begin{array}{cccc}
      1&0&0&1
      \end{array}}\\
      {\begin{array}{cccc}
      0&1&0&{ - 1}
      \end{array}}\\
      {\begin{array}{cccc}
      0&0&1&1
      \end{array}}
      \end{array}} \right]


