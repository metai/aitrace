.. _Section-ConvexPolygonRegionFillingAlgorithmDesignComputerScience:

凹多边形区域填充
=====================


问题分析
----------------






该方法的核心思想是根据 **多边形内的点满足多边形区域的边构成的不等式方程组** 的思想, 即找到凸多边形区域内一点(如重心 :math:`P_c=(x_c, y_c)^T`), 判断改点确定的多边形的边构成的不等式方程组的符号, 然后对于待填充点 :math:`P_0=(x_0, y_0)^T`, 代入方程组并判断符号是否与 :math:`P_c` 一致, 若一致则在多边形区域内. 设有由 :math:`N` 个顶点 :math:`{\mathbb V}={(x_i, y_i)^T}_{i=1}^N` 按顺序构成的多边形 :math:`\mathcal P`, 将其边构成的方程组记为

.. math::
   \begin{aligned}
   l_1 &: a_1 x + b_1 y + c_1 = 0\\
   l_2 &: a_2 x + b_2 y + c_2 = 0\\
       & {\ \vdots} \\
   l_{N-1} &: a_{N-1} x + b_{N-1} y + c_{N-1} = 0
   \end{aligned}.
   :label: equ-PolygonEdgeEquation

将重心 :math:`P_c` 的坐标代入方程组 :eq:`equ-PolygonEdgeEquation` 并判断符号, 记为 :math:`{\bm f}_c=(f_{c_1}, f_{c_2}, \cdots, f_{c_{N-1}})^T`, 其中大于等于0记为 :math:`1`, 小于0记为 :math:`0`.

对于待填充点 :math:`P_0=(x_0, y_0)^T`, 代入方程组 :eq:`equ-PolygonEdgeEquation` 并判断符号, 记为 :math:`{\bm f}_0=(f_{0_1}, f_{0_2}, \cdots, f_{0_{N-1}})^T`, 其中大于等于0记为 :math:`1`, 小于0记为 :math:`0`.

若符号向量 :math:`{\bm f}_c` 与 :math:`{\bm f}_0` 的值相同, 则待填充点在多边形区域内, 反之则不在区域内.
