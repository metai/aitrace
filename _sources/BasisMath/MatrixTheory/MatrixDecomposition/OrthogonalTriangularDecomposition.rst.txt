.. _Section-OrthogonalTriangularDecomposition:

正交三角分解
==========================================

什么是正交三角分解
------------------------------------

正交三角分解 ( :term:`Orthogonal Triangular Decomposition` ), 是指将一矩阵分解正 (酉) 交矩阵 :math:`{\bm Q}`  与非奇异上三角矩阵 :math:`{\bm R}` 两个矩阵的乘积的分解.

.. _def-OrthogonalTriangularDecomposition:

.. proof:definition:: 正交三角分解

   设 :math:`{\bm A} \in {\mathbb C}_{m\times n}` , 若存在矩阵 :math:`{\bm Q} \in {\mathbb C}`  和 :math:`{\bm R} \in {\mathbb C}` 使得

   .. math::
      {\bm A}_{m\times n} = {\bm Q}_{m\times n} {\bm R}_{n\times n}

   则称上述分解为 **正交三角分解** ,  简称 **QR 分解** .




求解方法
------------------------------------

Schmidt 正交化方法
~~~~~~~~~~~~~~~~~~~~~~~~

对矩阵 :math:`{\bm A} \in {\mathbb C}_{m\times n}` 进行QR分解的步骤如下:

#. 记矩阵 :math:`{\bm A} = ({\bm a}_1, {\bm a}_2, \cdots, {\bm a}_n)` , 其中 :math:`{\bm a}_j` 为矩阵 :math:`{\bm A}` 的第 :math:`j` 列;
#. 正交化向量组 :math:`{\bm a}_1, {\bm a}_2, \cdots, {\bm a}_n` , 得正交化后的向量组 :math:`{\bm b}_1, {\bm b}_2, \cdots, {\bm b}_n` ;
#. 单位化向量组 :math:`{\bm b}_1, {\bm b}_2, \cdots, {\bm b}_n` , 得单位化后的向量组 :math:`{\bm q}_1, {\bm q}_2, \cdots, {\bm q}_n` , 其中 :math:`{\bm q}_j = \frac{1}{|{\bm b}_j|}{\bm b}_j` , :math:`j = 1, 2, \cdots, n` ;
#. 将正交化的向量组按顺序组成矩阵 :math:`{\bm Q} = ({\bm q}_1, {\bm q}_2, \cdots, {\bm q}_n)` ;
#. 计算上三角矩阵 :math:`{\bm R} = {\rm diag}(|{\bm b}_1|, |{\bm b}_2|, \cdots, |{\bm b}_n|) \cdot {\bm C}` ;

其中,

.. math::
   {\bm C} = \left[ {\begin{array}{cccc}
   {\rm{1}}&{{k_{21}}}& \cdots &{{k_{n1}}}\\
   {}&1& \cdots &{{k_{n2}}}\\
   {}&{}& \ddots &{}\\
   {}&{}&{}&1
   \end{array}} \right]

且 :math:`k_{ij} = \frac{\left\langle {\bm a}_i{\bm b}_j \right\rangle}{\left\langle {\bm b}_j{\bm b}_j \right\rangle}` , :math:`j < i` .


.. note::
   举个例子, 求如下矩阵的QR分解,

   .. math::
      {\bm A} = \left[ {\begin{array}{ccc}
      0&2&2\\
      2&1&2\\
      0&2&1
      \end{array}} \right]

   解: 由题意有,

   令 :math:`{\bm a}_1 = (0, 2, 0)^T` , :math:`{\bm a}_2 = (2, 1, 2)^T` , :math:`{\bm a}_3 = (2, 2, 1)^T`

   正交化得

   :math:`{\bm b}_1 = {\bm a}_1 = (0, 2, 0)^T` , :math:`k_{21} = \frac{\left\langle{\bm a_2}, {\bm b}_1\right\rangle }{\left\langle{\bm b}_1, {\bm  b}_1\right\rangle } = \frac{1}{2}`

   :math:`{\bm b}_2 = {\bm a}_2 - k_{21}{\bm b}_1` :math:`= (2, 1, 2)^T - \frac{1}{2}(0, 2, 0)^T = (2, 0, 2)^T` , :math:`k_{32} = \frac{\left\langle{\bm a_3}, {\bm b}_2\right\rangle }{\left\langle{\bm b}_2, {\bm  b}_2\right\rangle } = \frac{3}{4}` , :math:`k_{31} = \frac{\left\langle{\bm a_3}, {\bm b}_1\right\rangle }{\left\langle{\bm b}_1, {\bm  b}_1\right\rangle } = 1`

   :math:`{\bm b}_3 = {\bm a}_3 - k_{32}{\bm b}_2 - k_{31}{\bm b}_1` :math:`= (2, 2, 1)^T - \frac{3}{4}(2, 0, 2)^T - 1(0, 2, 0)^T = (\frac{1}{2}, 0, \frac{-1}{2})^T`

   单位化得

   :math:`{\bm q}_1 = \frac{(0, 2, 0)^T}{2} = (0, 1, 0)^T` , :math:`{\bm q}_2 = \frac{(2, 0, 2)^T}{2\sqrt 2} = (\frac{1}{\sqrt 2}, 0, \frac{1}{\sqrt 2})^T` , :math:`{\bm q}_3 = \frac{(\frac{1}{2}, 0, \frac{-1}{2})^T}{\frac{1}{\sqrt 2}} = (\frac{\sqrt 2}{2}, 0, \frac{-\sqrt 2}{2})^T`

   从而有

   .. math::
      {\bm{C}} = \left[ {\begin{array}{ccc}
      1&{{k_{21}}}&{{k_{31}}}\\
      0&1&{{k_{32}}}\\
      0&0&1
      \end{array}} \right] = \left[ {\begin{array}{ccc}
      1&{\frac{1}{2}}&{1}\\
      0&1&{\frac{3}{4}}\\
      0&0&1
      \end{array}} \right]

   由 :math:`{\bm R} = {\rm diag}(|{\bm b}_1|, |{\bm b}_2|, |{\bm b}_3|) \cdot {\bm C}` 知

   .. math::
      {\bm R} = \left[ {\begin{array}{ccc}
                     {2 }&0&0\\
                     0&{2\sqrt 2 }&0\\
                     0&0&{\frac{1}{\sqrt 2}}
                     \end{array}} \right]\left[ {\begin{array}{ccc}
                     1&{\frac{1}{2}}&{1}\\
                     0&1&{\frac{3}{4}}\\
                     0&0&1
                     \end{array}} \right] = \left[ {\begin{array}{ccc}
                     {2}&{1}&{2}\\
                     0&{2\sqrt 2}&{\frac{3}{\sqrt 2}}\\
                     0&0&{\frac{1}{\sqrt 2}}
                     \end{array}} \right]

   .. math::
      {\bm{Q}} = \left[ {\begin{array}{ccc}
      {0}&{\frac{1}{{\sqrt 2}}}&{\frac{\sqrt 2}{2}}\\
      {1}&{0}&0\\
      {0}&{\frac{1}{{\sqrt 2}}}&{\frac{-\sqrt 2}{2}}
      \end{array}} \right]
      = \left[ {\begin{array}{ccc}
      0&{\frac{1}{{\sqrt 2 }}}&{\frac{1}{{\sqrt 2 }}}\\
      1&0&0\\
      0&{\frac{1}{{\sqrt 2 }}}&{\frac{{ - 1}}{{\sqrt 2 }}}
      \end{array}} \right]

Givens 变换方法
~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   举个例子, 求如下矩阵的QR分解,

   .. math::
      {\bm A} = \left[ {\begin{array}{ccc}
      0&2&2\\
      2&1&2\\
      0&2&1
      \end{array}} \right]

   解: 由题意有,

   记 :math:`{\bm A}^{(1)} = {\bm A}` , 取 :math:`{\bm A}^{(1)}` 的第一列 :math:`{\bm a}_1^{(1)} = (0, 2, 0)^T` , 构造Givens矩阵, 使得 :math:`{\bm G}^{(1)}{\bm a}_1^{(1)} = |{\bm a}_1^{(1)}| {\bm e}_1` :

   取 :math:`{\bm G}^{(1)}_{1,2} = \left[ {\begin{array}{ccc} 0&1&0\\ {{-}1}&0&0\\ 0&0&1 \end{array}} \right]` , 其中, :math:`c = \frac{\xi_1}{\sqrt{\xi_1^2 + \xi_2^2}} = \frac{0}{\sqrt{0^2 + 2^2}} = 0` , :math:`s = \frac{\xi_2}{\sqrt{\xi_1^2 + \xi_2^2}} = \frac{2}{\sqrt{0^2 + 2^2}} = 1` .

   从而 :math:`{\bm G}^{(1)}_{1,2}{\bm a}_1^{(1)} = (2, 0, 0)^T = 2 {\bm e}_1   ` , 将 :math:`{\bm a}_1^{(1)}` 的第二坐标分量变为 :math:`0` , 又第三坐标分量为 :math:`0` , 所以无需再构造 :math:`{\bm G}^{(1)}_{1,3}` 使第三坐标分量为 :math:`0` , 当然也可以对 :math:`(2, 0, 0)^T` 继续构造

   :math:`{\bm G}^{(1)}_{1,3} = \left[ {\begin{array}{ccc} 1&0&0\\ 0&1&0\\ 0&0&1 \end{array}} \right]` , 其中, :math:`c = \frac{\sqrt{\xi_1^2+\xi_2^2}}{\sqrt{\xi_1^2 + \xi_2^2 +\xi_3^2}} = \frac{\sqrt{2^2+0^2}}{\sqrt{2^2 + 0^2 + 0^2}} = 1` , :math:`s = \frac{\xi_3}{\sqrt{\xi_1^2 + \xi_2^2 +\xi_3^2}} = \frac{0}{\sqrt{2^2 + 0^2 + 0^2}} = 0` , 可见 :math:`{\bm G}^{(1)}_{1,3}` 为单位阵.

   从而有

   .. math::
      {\bm G}^{(1)}{\bm A}^{(1)} = {\bm G}^{(1)}_{1,3}{\bm G}^{(1)}_{1,2}{\bm A}^{(1)}
      = \left[ {\begin{array}{ccc}
      1&0&0\\
      0&1&0\\
      0&0&1
      \end{array}} \right]\left[ {\begin{array}{ccc}
      0&1&0\\
      {{\rm{ - }}1}&0&0\\
      0&0&1
      \end{array}} \right]\left[ {\begin{array}{ccc}
      0&2&2\\
      2&1&2\\
      0&2&1
      \end{array}} \right] \\
      = \left[ {\begin{array}{ccc}
      2&1&2\\
      0&{{-}2}&{{-}2}\\
      0&2&1
      \end{array}} \right]

   对 :math:`{\bm A}^{(2)} = \left[ {\begin{array}{cc}{-2}&{-2}\\2&1\end{array}} \right]` , 取其第一列 :math:`{\bm a}_1^{(2)} = (-2, 2)^T` , 构造Givens矩阵, 使得 :math:`{\bm G}^{(2)}{\bm a}_1^{(2)} =  |{\bm a}_1^{(2)}| {\bm e}_1` :

   取 :math:`{\bm G}^{(2)}_{1,2} = \left[ {\begin{array}{cc}{\frac{{{\rm{ - }}1}}{{\sqrt 2 }}}&{\frac{1}{{\sqrt 2 }}}\\{\frac{{{\rm{ - }}1}}{{\sqrt 2 }}}&{\frac{{{\rm{ - }}1}}{{\sqrt 2 }}}\end{array}} \right]` , 其中, :math:`c = \frac{\xi_1}{\sqrt{\xi_1^2 + \xi_2^2}} = \frac{-2}{\sqrt{{-2}^2 + 2^2}} = \frac{-1}{\sqrt 2}` , :math:`s = \frac{\xi_2}{\sqrt{\xi_1^2 + \xi_2^2}} = \frac{2}{\sqrt{{-2}^2 + 2^2}} = \frac{1}{\sqrt 2}` .

   从而有

   .. math::
      {\bm G}^{(2)}{\bm A}^{(2)} = {\bm G}^{(2)}_{1,2}{\bm A}^{(2)} =
      \left[ {\begin{array}{cc}
      {\frac{{{\rm{ - }}1}}{{\sqrt 2 }}}&{\frac{1}{{\sqrt 2 }}}\\
      {\frac{{{\rm{ - }}1}}{{\sqrt 2 }}}&{\frac{{{\rm{ - }}1}}{{\sqrt 2 }}}
      \end{array}} \right]\left[ {\begin{array}{cc}
      {{\rm{ - }}2}&{{\rm{ - }}2}\\
      2&1
      \end{array}} \right]{\rm{ = }}\left[ {\begin{array}{cc}
      {2\sqrt 2 }&{\frac{3}{{\sqrt 2 }}}\\
      0&{\frac{1}{{\sqrt 2 }}}
      \end{array}} \right]

   最后, 令

   .. math::
      {\bm G} = \left[ {\begin{array}{cc} 1&{}\\ {}&{{{\bm{G}}^{(2)}}} \end{array}} \right]{{\bm{G}}^{(1)}}
      = \left[ {\begin{array}{ccc}
      1&0&0\\
      0&{\frac{{ - 1}}{{\sqrt 2 }}}&{\frac{1}{{\sqrt 2 }}}\\
      0&{\frac{{ - 1}}{{\sqrt 2 }}}&{\frac{{ - 1}}{{\sqrt 2 }}}
      \end{array}} \right]\left[ {\begin{array}{ccc}
      0&1&0\\
      {{\rm{ - }}1}&0&0\\
      0&0&1
      \end{array}} \right] = \left[ {\begin{array}{ccc}
      0&1&0\\
      {\frac{1}{{\sqrt 2 }}}&0&{\frac{1}{{\sqrt 2 }}}\\
      {\frac{1}{{\sqrt 2 }}}&0&{\frac{{ - 1}}{{\sqrt 2 }}}
      \end{array}} \right]

   则有

   .. math::
      {\bm Q} = {\bm G}^T = \left[ {\begin{array}{ccc}
      0&{\frac{1}{{\sqrt 2 }}}&{\frac{1}{{\sqrt 2 }}}\\
      1&0&0\\
      0&{\frac{1}{{\sqrt 2 }}}&{\frac{{ - 1}}{{\sqrt 2 }}}
      \end{array}} \right]

   .. math::
      {\bm{R}}{\rm{ = }}\left[ {\begin{array}{ccc}
      2&1&2\\
      0&{2\sqrt 2 }&{\frac{{3\sqrt 2 }}{2}}\\
      0&0&{\frac{{\sqrt 2 }}{2}}
      \end{array}} \right] = \left[ {\begin{array}{ccc}
      2&1&2\\
      0&{2\sqrt 2 }&{\frac{3}{{\sqrt 2 }}}\\
      0&0&{\frac{1}{{\sqrt 2 }}}
      \end{array}} \right]


Householder 变换方法
~~~~~~~~~~~~~~~~~~~~~~~~



.. note::
   举个例子, 求如下矩阵的QR分解,

   .. math::
      {\bm A} = \left[ {\begin{array}{ccc}
      0&2&2\\
      2&1&2\\
      0&2&1
      \end{array}} \right]

   解: 由题意有,

   记 :math:`{\bm A}^{(1)} = {\bm A}` , 取 :math:`{\bm A}^{(1)}` 的第一列 :math:`{\bm a}_1^{(1)} = (0, 2, 0)^T` , 构造Householder矩阵, 使得 :math:`{\bm H}^{(1)}{\bm a}_1^{(1)} =  |{\bm a}_1^{(1)}| {\bm e}_1` :

   :math:`{\bm b}_1^{(1)} = {\bm a}_1^{(1)} - |{\bm a}_1^{(1)}|{\bm e}_1 = (0, 2, 0)^T - 2(1, 0, 0)^T = (-2, 2, 0)^T` , :math:`{\bm u}_1^{(1)} = \frac{{\bm b}_1^{(1)}}{|{\bm b}_1^{(1)}|} = \frac{(-2, 2, 0)^T}{2\sqrt{2}} = (\frac{-1}{\sqrt 2}, \frac{1}{\sqrt 2}, 0)^T`

   .. math::
      {\bm u}_1^{(1)}{{\bm u}_1^{(1)}}^T = \left[ {\begin{array}{ccc}{\frac{1}{2}}&{\frac{{ - 1}}{2}}&0\\{\frac{{ - 1}}{2}}&{\frac{1}{2}}&0\\0&0&0\end{array}} \right]

   .. math::
      {{\bm{H}}^{(1)}} = {\bm{I}} - 2{\bm u}_1^{(1)}{{\bm u}_1^{(1)}}^T =
      \left[ {\begin{array}{ccc}
      1&0&0\\
      0&1&0\\
      0&0&1
      \end{array}} \right] - \left[ {\begin{array}{ccc}
      1&{ - 1}&0\\
      { - 1}&1&0\\
      0&0&0
      \end{array}} \right] = \left[ {\begin{array}{ccc}
      0&1&0\\
      1&0&0\\
      0&0&1
      \end{array}} \right]

   .. math::
      {{\bm{H}}^{(1)}}{{\bm{A}}^{(1)}} = \left[ {\begin{array}{ccc}
      0&1&0\\
      1&0&0\\
      0&0&1
      \end{array}} \right]\left[ {\begin{array}{ccc}
      0&2&2\\
      2&1&2\\
      0&2&1
      \end{array}} \right] = \left[ {\begin{array}{ccc}
      2&1&2\\
      0&2&2\\
      0&2&1
      \end{array}} \right]

   对 :math:`{\bm A}^{(2)} = \left[ {\begin{array}{cc}2&2\\2&1\end{array}} \right]` , 取其第一列 :math:`{\bm a}_1^{(2)} = (2, 2)^T` , 构造Householder矩阵, 使得 :math:`{\bm H}^{(2)}{\bm a}_1^{(2)} =  |{\bm a}_1^{(2)}| {\bm e}_1` :

   :math:`{\bm b}_1^{(2)} = {\bm a}_1^{(2)} - |{\bm a}_1^{(2)}|{\bm e}_1 = (2, 2)^T - 2{\sqrt 2}(1, 0)^T = (2-2{\sqrt 2}, 2)^T` , :math:`{\bm u}_1^{(2)} = \frac{{\bm b}_1^{(2)}}{|{\bm b}_1^{(2)}|} = \frac{(2-2{\sqrt 2}, 2)^T}{2{\sqrt{4-2\sqrt 2}}} = \frac{(1-{\sqrt 2}, 1)^T}{{\sqrt{4-2\sqrt 2}}}`

   .. math::
      {\bm u}_1^{(2)}{{\bm u}_1^{(2)}}^T = \frac{1}{{4{-}2\sqrt 2 }}\left[ {\begin{array}{cc}
      {1{-}\sqrt 2 }\\
      1
      \end{array}} \right]\left[ {\begin{array}{ccc}
      {1{-}\sqrt 2 }&1
      \end{array}} \right]{\rm{ = }}\frac{1}{{4{-}2\sqrt 2 }}\left[ {\begin{array}{ccc}
      {3{-}2\sqrt 2 }&{1{-}\sqrt 2 }\\
      {1{-}\sqrt 2 }&1
      \end{array}} \right]

   .. math::
      {{\bm{H}}^{(2)}} = {\bm{I}} - 2{\bm u}_1^{(2)}{{\bm u}_1^{(2)}}^T = \left[ {\begin{array}{ccc}
      1&0\\
      0&1
      \end{array}} \right] - \frac{1}{{{\rm{2 - }}\sqrt 2 }}\left[ {\begin{array}{ccc}
      {3{-}2\sqrt 2 }&{1{-}\sqrt 2 }\\
      {1{-}\sqrt 2 }&1
      \end{array}} \right]{\rm{ = }}\left[ {\begin{array}{ccc}
      {\frac{{\sqrt 2 }}{2}}&{\frac{{\sqrt 2 }}{2}}\\
      {\frac{{\sqrt 2 }}{2}}&{\frac{{{-}\sqrt 2 }}{2}}
      \end{array}} \right]

   .. math::
      {{\bm{H}}^{{\rm{(2)}}}}{{\bm{A}}^{{\rm{(2)}}}} = \left[ {\begin{array}{ccc}
      {\frac{{\sqrt 2 }}{2}}&{\frac{{\sqrt 2 }}{2}}\\
      {\frac{{\sqrt 2 }}{2}}&{\frac{{{-}\sqrt 2 }}{2}}
      \end{array}} \right]\left[ {\begin{array}{ccc}
      2&2\\
      2&1
      \end{array}} \right]{\rm{ = }}\left[ {\begin{array}{ccc}
      {2\sqrt 2 }&{\frac{{3\sqrt 2 }}{2}}\\
      0&{\frac{{\sqrt 2 }}{2}}
      \end{array}} \right]

   再令

   .. math::
      {\bm{S}} = \left[ {\begin{array}{ccc}
      1&0\\
      0&{{{\bm{H}}^{{\rm{(2)}}}}}
      \end{array}} \right]{{\bm{H}}^{{\rm{(1)}}}}{\rm{ = }}\left[ {\begin{array}{ccc}
      1&0&0\\
      0&{\frac{{\sqrt 2 }}{2}}&{\frac{{\sqrt 2 }}{2}}\\
      0&{\frac{{\sqrt 2 }}{2}}&{\frac{{{-}\sqrt 2 }}{2}}
      \end{array}} \right]\left[ {\begin{array}{ccc}
      0&1&0\\
      1&0&0\\
      0&0&1
      \end{array}} \right]

   从而

   .. math::
      {\bm Q} = {\bm S}^T = \left[ {\begin{array}{ccc}
      0&{\frac{1}{{\sqrt 2 }}}&{\frac{1}{{\sqrt 2 }}}\\
      1&0&0\\
      0&{\frac{1}{{\sqrt 2 }}}&{\frac{{ - 1}}{{\sqrt 2 }}}
      \end{array}} \right]

   且

   .. math::
      {\bm{R}} = \left[ {\begin{array}{ccc}
      2&1&2\\
      0&{2\sqrt 2 }&{\frac{3}{{\sqrt 2 }}}\\
      0&0&{\frac{1}{{\sqrt 2 }}}
      \end{array}} \right]


代码实现
~~~~~~~~~~~~~~~~~~~

matlab代码

::

   >> A = [0 2 2;2 1 2;0 2 1]

   A =

        0     2     2
        2     1     2
        0     2     1

   >> [Q, R] = qr(A)

   Q =

            0    0.7071   -0.7071
      -1.0000         0         0
            0    0.7071    0.7071

   R =

      -2.0000   -1.0000   -2.0000
            0    2.8284    2.1213
            0         0   -0.7071
