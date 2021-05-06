.. _Section-LineCircleAnalyticGeometryGeometryBasisMath:

直线和圆
====================

直线方程与圆的方程
---------------------

一般式方程

.. math::
   Ax + By + C = 0
   :label: equ-GeneralEquationLine


.. math::
   (x-x_0)^2 + (y-y_0)^2 = r^2
   :label: equ-GeneralEquationCircle



直线与圆的交点
------------------

本小节利用直线和圆的一般式方程, 推导直线与圆之间的交点, 易知该交点满足如下方程组:

.. math::
   \left\{\begin{array}{l}
   Ax + By + C = 0 \\
   (x-x_0)^2 + (y-y_0)^2 = r^2
   \end{array}\right.
   :label: equ-GeneralEquationLineCircle

当 :math:`B=0` 时有, 若 :math:`r^2 < (\frac{C}{A}+x_0)^2`, 则无交点; 若 :math:`r^2 = (\frac{C}{A}+x_0)^2` 则相切于点 :math:`(-\frac{C}{A}, y_0)`; 若 :math:`r^2 > (\frac{C}{A}+x_0)^2` 则相交于点 :math:`(-\frac{C}{A}, y_0\pm \sqrt{r^2-\left(\frac{C}{A}+x_0\right)^2})`;

当 :math:`B≠0` 时有交点 :math:`\left(\frac{-b\pm \sqrt{b^2-4ac}}{2a}, y=\frac{-Ax-C}{B}\right)`, 其中, :math:`a=1+\frac{A^2}{B^2}`, :math:`B=\frac{2AC}{B^2}+\frac{2y_0A}{B}-2x_0`, :math:`c=x_0^2+(\frac{C}{B}+y_0)^2-r^2`.

线段与圆的交点
-------------------

