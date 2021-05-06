.. _Section-MatrixFunction:


矩阵函数
====================


概念
------------------


求解方法
------------------

- 方法1: 待定系数法;
- 方法2: 数项级数求和法, 写成矩阵级数求和形式, 计算 :math:`{\bm A}^k` , 代入求解;
- 方法3: 对角矩阵法, 根据 :math:`{\bm A} = {\bm P}{\bm \Lambda}{\bm P}^{-1}` , 有 :math:`{\bm A}^k = {\bm P}{\bm \Lambda}^k{\bm P}^{-1}` 可知 :math:`f({\bm A}) = {\bm P}f({\bm \Lambda}){\bm P}^{-1}` , 其中 :math:`f({\bm \Lambda}) = (f(\Lambda_{ii})) = (f(\lambda_i))` 据此可求;
- 方法4: Jordan标准型法, 对于不能化为对角阵的矩阵, 采用此方法, 注意此时 :math:`f({\bm \Lambda}) {\neq} (f(\Lambda_{ii}))`


待定系数法
~~~~~~~~~~~~~~~~~~~~~

数项级数求和法
~~~~~~~~~~~~~~~~~~~~~~~

对角矩阵法
~~~~~~~~~~~~~~~~~~~~~~

根据 :math:`{\bm A} = {\bm P}{\bm \Lambda}{\bm P}^{-1}` , 有 :math:`{\bm A}^k = {\bm P}{\bm \Lambda}^k{\bm P}^{-1}` 可知 :math:`f({\bm A}) = {\bm P}f({\bm \Lambda}){\bm P}^{-1}` , 其中 :math:`f({\bm \Lambda}) = (f(\Lambda_{ii})) = (f(\lambda_i))`


Jordan标准型法
~~~~~~~~~~~~~~~~~~~~

对于不能化为对角阵的, 采用Jordan标准形法来求

.. math::
   f({\bm{A}}) = \sum\limits_{k = 0}^\infty  {{c_k}{{\bm{A}}^k}}  = \sum\limits_{k = 0}^\infty  {{c_k}{\bm{P}}{{\bm{J}}^k}{{\bm{P}}^{ - 1}}}  = {\bm{P}}\left( {\sum\limits_{k = 0}^\infty  {{c_k}{{\bm{J}}^k}} } \right){{\bm{P}}^{ - 1}}

即

.. math::
   f({\bm{A}}) = {\bm{P}}\left[ {\begin{array}{ccccc}
   {f({{\bm{J}}_1})}&{}&{}\\
   {}& \ddots &{}\\
   {}&{}&{f({{\bm{J}}_s})}
   \end{array}} \right]{{\bm{P}}^{ - 1}}

其中

.. math::
   f({{\bm{J}}_i}) = \left[ {\begin{array}{ccccc}
   {f({\lambda _i})}&{\frac{{{f^{(1)}}({\lambda _i})}}{{1!}}}&{\frac{{{f^{(2)}}({\lambda _i})}}{{2!}}}& \cdots &{\frac{{{f^{({m_i} - 1)}}({\lambda _i})}}{{({m_i} - 1)!}}}\\
   {}&{f({\lambda _i})}&{\frac{{{f^{(1)}}({\lambda _i})}}{{1!}}}& \ddots & \vdots \\
   {}&{}& \ddots & \ddots &{\frac{{{f^{(2)}}({\lambda _i})}}{{2!}}}\\
   {}&{}&{}&{f({\lambda _i})}&{\frac{{{f^{(1)}}({\lambda _i})}}{{1!}}}\\
   {}&{}&{}&{}&{f({\lambda _i})}
   \end{array}} \right]

其中, :math:`m_i` 为Jordan块 :math:`{\bm J}_i` 的阶数, 也是特征值 :math:`\lambda_i` 的重数.

.. hint::
   只需要求出第一行, 斜向右下顺着写即可.


总结
-------------------------

- :math:`e^z = 1 + \frac{z}{1!} + \frac{z^2}{2!}  + \frac{z^3}{3!} + \cdots`
- :math:`{\rm{cos}}z = 1 - \frac{z^2}{2!} + \frac{z^4}{4!} - \cdots`
- :math:`{\rm{sin}}z = \frac{z}{1!} - \frac{z^3}{3!} + \frac{z^5}{5!} - \cdots`
- :math:`\frac{1}{1-z} = \sum_{n=0}^{\infty}z^n, |z|<1`
- :math:`e^{jz} = {\rm cos}z + j{\rm sin}z`
- :math:`{\rm cos}z = \frac{e^{jz} + e^{-jz}}{2}`
- :math:`{\rm sin}z = \frac{e^{jz} - e^{-jz}}{2}`
- :math:`{\rm cos}(-z) = {\rm cos}z`
- :math:`{\rm sin}(-z) = -{\rm sin}z`


- :math:`e^{\bm A} = 1 + \frac{{\bm A}}{1!} + \frac{{\bm A}^2}{2!}  + \frac{{\bm A}^3}{3!} + \cdots`
- :math:`{\rm{cos}}{\bm A} = 1 - \frac{{\bm A}^2}{2!} + \frac{{\bm A}^4}{4!} - \cdots`
- :math:`{\rm{sin}}{\bm A} = \frac{{\bm A}}{1!} - \frac{{\bm A}^3}{3!} + \frac{{\bm A}^5}{5!} - \cdots`
- :math:`{({\bm I} - {\bm A})^{-1}} = \sum_{n=0}^{\infty}{\bm A}^n`
- :math:`e^{j{\bm A}} = {\rm cos}{\bm A} + j{\rm sin}{\bm A}`
- :math:`{\rm cos}{\bm A} = \frac{e^{j{\bm A}} + e^{-j{\bm A}}}{2}`
- :math:`{\rm sin}{\bm A} = \frac{e^{j{\bm A}} - e^{-j{\bm A}}}{2}`
- :math:`{\rm cos}(-{\bm A}) = {\rm cos}{\bm A}`
- :math:`{\rm sin}(-{\bm A}) = -{\rm sin}{\bm A}`

- 当 :math:`{\bm{AB}} {\neq} {\bm{BA}}` 时, :math:`e^{\bm A}e^{\bm B} {\neq} e^{\bm B}e^{\bm A} {\neq} e^{\bm{AB}}`
- 当 :math:`{\bm{AB}} = {\bm{BA}}` 时, :math:`e^{\bm A}e^{\bm B} = e^{\bm B}e^{\bm A} = e^{\bm{AB}}`